# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.plantuml/src/org/omg/sysml/plantuml/SysML2PlantUMLSvc.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.plantuml/src/org/omg/sysml/plantuml/SysML2PlantUMLSvc.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.plantuml/src/org/omg/sysml/plantuml/SysML2PlantUMLSvc.java
- source_bytes: 4112
- source_sha256: `4cfac73337af2318ead422bff174ea9f1ddf7ba83597ada8afa54639f13caaa1`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*****************************************************************************
 * SysML 2 Pilot Implementation, PlantUML Visualization
 * Copyright (c) 2020, 2021 Mgnite Inc.
 * Copyright (c) 2021 Model Driven Solutions, Inc.
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
 *  Ed Seidewitz, Model Driven Solutions, Inc.
 * 
 *****************************************************************************/

package org.omg.sysml.plantuml;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.List;

import org.eclipse.emf.ecore.EObject;

import net.sourceforge.plantuml.FileFormat;
import net.sourceforge.plantuml.FileFormatOption;
import net.sourceforge.plantuml.OptionFlags;
import net.sourceforge.plantuml.SourceStringReader;

public class SysML2PlantUMLSvc {
    private final SysML2PlantUMLText s2Text;

    public void setGraphVizPath(String path) {
        OptionFlags.getInstance().setDotExecutable(path);
    }

    private SysML2PlantUMLText.MODE mode = SysML2PlantUMLText.MODE.Default;

    private static <T extends Enum<?>> String getPossibleValues(Class<T> en) {
        StringBuilder sb = new StringBuilder();
        for (T e : en.getEnumConstants()) {
            sb.append(e.name());
            sb.append(' ');
        }
        return sb.toString();
    }

    public void setView(String view) {
        for (SysML2PlantUMLText.MODE m: SysML2PlantUMLText.MODE.values()) {
            if (m.name().equalsIgnoreCase(view)) {
                this.mode = m;
                return;
            }
        }
        throw new IllegalArgumentException("Invalid View: " + view
                                           + " View candidates are: "
                                           + getPossibleValues(SysML2PlantUMLText.MODE.class));
    }

    private void applyStyle(List<String> styles) {
        s2Text.clearStyle();
        boolean addDefault = true;
        if (styles != null) {
            for (String style: styles) {
                SysML2PlantUMLStyle s = SysML2PlantUMLStyle.get(style);
                if (s.isPrimary()) addDefault = false;
                s2Text.addStyle(s);
            }
        }
        if (addDefault) {
            s2Text.addStyle(SysML2PlantUMLStyle.getDefault());
        }
    }

    public String getPlantUMLCode(List<?extends EObject> eObjs, List<String> styles) {
        if (eObjs.isEmpty()) return null;
        // Setup Visualization Mode with the first item.
        s2Text.setupVisualizationEObjects(eObjs.get(0));
        s2Text.setMode(mode);
        applyStyle(styles);

        StringBuilder sb = new StringBuilder("@startuml\n");
        sb.append(s2Text.sysML2PUML(eObjs));
        sb.append("@enduml\n");

        return sb.toString();
    }
    
    public String getSVG(List<?extends EObject> eObjs, List<String> styles) throws IOException {
        String pcode = getPlantUMLCode(eObjs, styles);

        final FileFormatOption ffo = new FileFormatOption(FileFormat.SVG);
        ByteArrayOutputStream bos = new ByteArrayOutputStream();

        SourceStringReader reader = new SourceStringReader(pcode);
        reader.outputImage(bos, ffo);

        return bos.toString("UTF-8");
    }

    public SysML2PlantUMLSvc(SysML2PlantUMLLinkProvider linkProvider) {
        this.s2Text = new SysML2PlantUMLText(linkProvider);
    }
}

````
