# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.jupyter.kernel/src/main/java/org/omg/sysml/jupyter/kernel/magic/Publish.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.jupyter.kernel/src/main/java/org/omg/sysml/jupyter/kernel/magic/Publish.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.jupyter.kernel/src/main/java/org/omg/sysml/jupyter/kernel/magic/Publish.java
- source_bytes: 2110
- source_sha256: `bd8107e1c276fe218716f46568f443717c52410bddcb8bbd70a659f54b708f76`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*
 * SysML 2 Pilot Implementation
 * Copyright (C) 2020  California Institute of Technology ("Caltech")
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the Eclipse Public License as published by
 * the Eclipse Foundation, version 2 of the License.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * Eclipse Public License for more details.
 * You should have received a copy of the Eclipse Public License
 * along with this program.  If not, see <https://www.eclipse.org/legal/epl-2.0/>.
 *
 * @license EPL-2.0 <http://spdx.org/licenses/EPL-2.0>
 */

package org.omg.sysml.jupyter.kernel.magic;

import io.github.spencerpark.jupyter.kernel.magic.registry.LineMagic;
import io.github.spencerpark.jupyter.kernel.magic.registry.MagicsArgs;
import org.omg.sysml.jupyter.kernel.ISysML;

import java.util.List;
import java.util.Map;

public class Publish {
    private static final MagicsArgs SHOW_ARGS = MagicsArgs.builder().onlyKnownKeywords().onlyKnownFlags()
    		.optional("element")
    		.keyword("project")
    		.keyword("branch")
    		.flag("derived", 'd', "false")
            .flag("help", 'h', "true")
    		.build();

    @LineMagic
    public static String publish(List<String> args) {
        Map<String, List<String>> vals = SHOW_ARGS.parse(args);
        List<String> elements = vals.get("element");
        List<String> projects = vals.get("project");
        List<String> branches = vals.get("branch");
        String element = elements.isEmpty()? null:elements.get(0);
        String project = projects.isEmpty()? null:projects.get(0);
        String branch = branches.isEmpty()? null:branches.get(0);
        boolean includeDerived = !vals.get("derived").isEmpty();
        List<String> help = vals.get("help");
        return ISysML.getKernelInstance().getInteractive().publish(element, project, branch, includeDerived, help);
    }
}

````
