# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.plantuml/src/org/omg/sysml/plantuml/VTraverser.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.plantuml/src/org/omg/sysml/plantuml/VTraverser.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.plantuml/src/org/omg/sysml/plantuml/VTraverser.java
- source_bytes: 6635
- source_sha256: `ec25509b1ed8e81352e376f736c76435351725b5920ee5288f233a8427befb32`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*****************************************************************************
 * SysML 2 Pilot Implementation, PlantUML Visualization
 * Copyright (c) 2020-2024 Mgnite Inc.
 * Copyright (c) 2022 Model Driven Solutions, Inc.
 *    
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the Eclipse Public License as published by
 * the Eclipse Foundation, version 2 of the License.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * Eclipse Public License for more details.
 *
 * You should have received a copy of theEclipse Public License
 * along with this program.  If not, see <https://www.eclipse.org/legal/epl-2.0/>.
 *
 * @license EPL-2.0 <http://spdx.org/licenses/EPL-2.0>
 * 
 * Contributors:
 *  Hisashi Miyashita, Mgnite Inc.
 *  Ed Seidewitz, MDS
 * 
 *****************************************************************************/

package org.omg.sysml.plantuml;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.Feature;
import org.omg.sysml.lang.sysml.Import;
import org.omg.sysml.lang.sysml.Membership;
import org.omg.sysml.lang.sysml.Namespace;
import org.omg.sysml.lang.sysml.Relationship;
import org.omg.sysml.lang.sysml.Type;
import org.omg.sysml.util.ElementUtil;
import org.omg.sysml.util.FeatureUtil;

public abstract class VTraverser extends Visitor {
    private Set<Namespace> visited;

    private Membership currentMembership;
    protected Membership getCurrentMembership() {
        return currentMembership;
    }

    protected boolean checkVisited(Namespace n) {
    	if (visited.contains(n)) return true;
    	visited.add(n);
    	return false;
    }

    private List<Set<Namespace>> listOfVisited = new ArrayList<Set<Namespace>>();

    protected void pushVisited() {
        listOfVisited.add(visited);
        this.visited = new HashSet<Namespace>();
    }

    protected void popVisited() {
        int idx = listOfVisited.size() - 1;
        this.visited = listOfVisited.get(idx);
        listOfVisited.remove(idx);
    }

    private boolean markRedefining(Element e, Set<Element> covered) {
        if (covered.contains(e)) return true;
        if (!(e instanceof Feature)) return false;
        Feature f = (Feature) e;
        covered.addAll(FeatureUtil.getAllRedefinedFeaturesOf(f));
        return false;
    }

    private static boolean isModelLibrary(Element e) {
        return ElementUtil.isStandardLibraryElement(e);
    }

    private void traverseInternal(Namespace n, Set<Element> covered) {
        for (Relationship r: toOwnedRelationshipArray(n)) {
            if (r instanceof Membership) {
                Membership ms = (Membership) r;
                setInherited(false);
                Element e = ms.getMemberElement();
                markRedefining(e, covered);
                this.currentMembership = ms;
                visit(ms);
                for (Relationship r2: toOwnedRelationshipArray(ms)) {
                    setInherited(false);
                    visit(r2);
                }
            } else if (r instanceof Import) {
                setInherited(false);
                visit(r);
            }
        }
    }

    private void traverseInherited(Type typ, Set<Element> covered) {
        for (Membership ms: typ.getInheritedMembership()) {
            Element e = ms.getMemberElement();
            if (isHidden(e)) continue;
            if (markRedefining(e, covered)) continue;
            setInherited(true);
            pushVisited();
            visit(ms);
            popVisited();
        }
    }

    private void traverseRest(VPath vpath, Set<Element> covered) {
        for (Element e: vpath.rest()) {
            if (isHidden(e)) continue;
            if (markRedefining(e, covered)) continue;
            currentMembership = null;
            setInherited(true);
            visit(e);
        }
    }

    public String traverse(Namespace ns, boolean noInherit, boolean noPopNamespace) {
        VPath vpath = getVPath();
        if (!pushNamespace(ns)) return null;
        vpath.enter(ns);
        Set<Element> covered = new HashSet<Element>();
        traverseInternal(ns, covered);
        if (!noInherit) {
            inheriting(ns);
            if (showInherited()) {
            	if (ns instanceof Type) {
            		traverseInherited((Type) ns, covered);
            	}
            } else {
                traverseRest(vpath, covered);
            }
        }
        vpath.leave(ns);
        if (!noPopNamespace) {
            popNamespace();
        }
        return "";
    }

    public String traverse(Namespace ns) {
        return traverse(ns, false, false);
    }

    protected String visitMembership(Membership m) {
        this.currentMembership = m;
        return visit(m.getMemberElement());
    }

    @Override
    public String caseMembership(Membership m) {
        return visitMembership(m);
    }

    @Override
    public String caseNamespace(Namespace n) {
        if (checkVisited(n)) {
            return "";
        }
        return traverse(n);
    }

    private boolean inited = false;
    private boolean showInherited;
    private boolean showLib;

    private void init() {
        if (inited) return;
        this.showInherited = styleBooleanValue("showInherited");
        this.showLib = styleBooleanValue("showLib");
        this.inited = true;
    }
    
    protected boolean showInherited() {
        init();
        return showInherited;
    }

    private boolean showLib() {
        init();
        return showLib;
    }

    protected boolean isHidden(Element e) {
    	return !showLib() && isModelLibrary(e);
    }

    private static Set<Namespace> initVisited(Visitor prev) {
        if (prev instanceof VTraverser) {
            VTraverser vtprev = (VTraverser) prev;
            return vtprev.visited;
        }
        return new HashSet<Namespace>();
    }
    
    protected VTraverser(Visitor prev, boolean block) {
    	super(prev, block);
        this.visited = initVisited(prev);
    }
    
    protected VTraverser(Visitor prev) {
    	this(prev, false);
    }
    
    protected VTraverser() {
        this(null, false);
    }
}

````
