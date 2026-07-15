# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/lifecycle/CommitReference.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/lifecycle/CommitReference.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/lifecycle/CommitReference.java
- source_bytes: 1321
- source_sha256: `5e2b9604ccf5ef04733f00ea60c25e1c67d90d6be4ac6f600c1482c1c3d610a1`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*
 * SysML v2 REST/HTTP Pilot Implementation
 * Copyright (C) 2021 Twingineer LLC
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

package org.omg.sysml.lifecycle;

import org.omg.sysml.record.Record;

import javax.validation.constraints.NotNull;
import java.time.ZonedDateTime;

public interface CommitReference extends Record {

    @Override
    @NotNull
    String getName();

    @Override
    void setName(@NotNull String name);

    Project getOwningProject();

    void setOwningProject(Project owningProject);

    Commit getReferencedCommit();

    ZonedDateTime getCreated();

    ZonedDateTime getDeleted();

    void setCreated(ZonedDateTime created);
}

````
