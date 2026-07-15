# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.jupyter.kernel/src/main/java/org/omg/sysml/jupyter/kernel/magic/Viz.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.jupyter.kernel/src/main/java/org/omg/sysml/jupyter/kernel/magic/Viz.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.jupyter.kernel/src/main/java/org/omg/sysml/jupyter/kernel/magic/Viz.java
- source_bytes: 2350
- source_sha256: `faca340f0a1d773c2b96bc24b38d75f8d0154849d55b33807acf63347f47b2a3`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*
 * SysML 2 Pilot Implementation
 * Copyright (c) 2020 Mgnite Inc.
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

import io.github.spencerpark.jupyter.kernel.display.DisplayData;
import io.github.spencerpark.jupyter.kernel.magic.registry.LineMagic;
import io.github.spencerpark.jupyter.kernel.magic.registry.MagicsArgs;
import org.omg.sysml.jupyter.kernel.ISysML;
import org.omg.sysml.interactive.VizResult;

import java.util.List;
import java.util.Map;

public class Viz {
    private static final MagicsArgs VIZ_ARGS
      = (MagicsArgs.builder().onlyKnownKeywords().onlyKnownFlags()
         .varargs("element")
         .keyword("view")
         .keyword("style")
         .flag("help", 'h', "true")
         .build());

    @LineMagic
    public static DisplayData viz(List<String> args) {
        Map<String, List<String>> vals = VIZ_ARGS.parse(args);

        List<String> elements = vals.get("element");
        List<String> views = vals.get("view");
        List<String> styles = vals.get("style");
        List<String> help = vals.get("help");

        VizResult vr = ISysML.getKernelInstance().getInteractive().viz(elements, views, styles, help);

        DisplayData dd = new DisplayData();

        switch (vr.kind) {
        case EXCEPTION:
        	dd.putText(vr.formatException());
        	break;
        case PLANTUML:
        	dd.putText(vr.getPlantUML());
        	break;
        case SVG:
        	dd.putSVG(vr.getSVG());
        	break;
        case TEXT:
        	dd.putText(vr.getText());
        	break;
        case EMPTY:
        	dd.putText("");
        	break;
        }
        return dd;
    }
}

````
