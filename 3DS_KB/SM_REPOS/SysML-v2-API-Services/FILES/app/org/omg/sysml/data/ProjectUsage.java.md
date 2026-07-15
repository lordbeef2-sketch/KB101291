# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/data/ProjectUsage.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/data/ProjectUsage.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/data/ProjectUsage.java
- source_bytes: 1064
- source_sha256: `f92028833c23d7c4a58f5529e188b05b50d84431eabe8c6a754747db5853ad35`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*
 * SysML v2 REST/HTTP Pilot Implementation
 * Copyright (C) 2021-2022 Twingineer LLC
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
 * You should have received a copy of the Eclipse Public License
 * along with this program.  If not, see <https://www.eclipse.org/legal/epl-2.0/>.
 *
 * @license EPL-2.0 <http://spdx.org/licenses/EPL-2.0>
 */

package org.omg.sysml.data;

import org.omg.sysml.lifecycle.Commit;
import org.omg.sysml.lifecycle.Data;
import org.omg.sysml.lifecycle.Project;

public interface ProjectUsage extends Data {

    String NAME = "ProjectUsage";

    Commit getUsedCommit();

    Project getUsedProject();
}

````
