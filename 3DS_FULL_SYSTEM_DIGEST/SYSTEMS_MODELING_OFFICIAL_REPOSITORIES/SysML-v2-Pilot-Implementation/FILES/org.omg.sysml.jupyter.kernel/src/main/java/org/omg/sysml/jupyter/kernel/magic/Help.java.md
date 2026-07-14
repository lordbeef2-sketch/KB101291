# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.jupyter.kernel/src/main/java/org/omg/sysml/jupyter/kernel/magic/Help.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.jupyter.kernel/src/main/java/org/omg/sysml/jupyter/kernel/magic/Help.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.jupyter.kernel/src/main/java/org/omg/sysml/jupyter/kernel/magic/Help.java
- source_bytes: 1636
- source_sha256: `479bb8b3f386c7be5ca71348b78232bf26b26991d32463a1de59632f862e7aaa`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*
 * SysML 2 Pilot Implementation
 * Copyright (C) 2023 Model Driven Solutions, Inc.
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

public class Help {
    private static final MagicsArgs SHOW_ARGS = MagicsArgs.builder().onlyKnownKeywords().onlyKnownFlags()
    		.optional("command")
            .flag("help", 'h', "true")
    		.build();

    @LineMagic
    public static String help(List<String> args) {
        Map<String, List<String>> vals = SHOW_ARGS.parse(args);
        List<String> names = vals.get("command");
        String name = names.isEmpty()? null: names.get(0);
        List<String> help = vals.get("help");
        return ISysML.getKernelInstance().getInteractive().help(name, help);
    }
}

````
