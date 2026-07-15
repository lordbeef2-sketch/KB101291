# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.plantuml/src/org/omg/sysml/plantuml/SysML2PlantUMLLinkProvider.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.plantuml/src/org/omg/sysml/plantuml/SysML2PlantUMLLinkProvider.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.plantuml/src/org/omg/sysml/plantuml/SysML2PlantUMLLinkProvider.java
- source_bytes: 1341
- source_sha256: `52c9b3915f76304f6980a2155729091788d4afbf788242143941785302e86276`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*****************************************************************************
 * SysML 2 Pilot Implementation, PlantUML Visualization
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
 *
 * You should have received a copy of theEclipse Public License
 * along with this program.  If not, see <https://www.eclipse.org/legal/epl-2.0/>.
 *
 * @license EPL-2.0 <http://spdx.org/licenses/EPL-2.0>
 * 
 * Contributors:
 *  Hisashi Miyashita, Mgnite Inc.
 * 
 *****************************************************************************/

package org.omg.sysml.plantuml;

import org.eclipse.emf.ecore.EObject;

public interface SysML2PlantUMLLinkProvider {
    /* Provider must return a proper link string navigatable to eObj.
     * It would be embedded in PlantUML text and then in generated diagrams.*/
    String getLinkString(EObject eObj);

    String getText(EObject eObj);
}

````
