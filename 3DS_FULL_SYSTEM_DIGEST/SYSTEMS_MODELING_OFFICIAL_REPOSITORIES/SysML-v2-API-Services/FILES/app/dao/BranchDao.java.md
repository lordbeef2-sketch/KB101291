# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/dao/BranchDao.java

- repository: `SysML-v2-API-Services`
- source_path: `app/dao/BranchDao.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/dao/BranchDao.java
- source_bytes: 1331
- source_sha256: `eecab03dfead5931d18e5cf404beb90534128018f5eb8a9b581f0f7f969d786a`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*
 * SysML v2 REST/HTTP Pilot Implementation
 * Copyright (C) 2020 InterCAX LLC
 * Copyright (C) 2020 California Institute of Technology ("Caltech")
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

package dao;

import org.omg.sysml.lifecycle.Branch;
import org.omg.sysml.lifecycle.Project;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

public interface BranchDao extends Dao<Branch> {

    List<Branch> findAllByProject(Project project, UUID after, UUID before, int maxResults);

    Optional<Branch> findByProjectAndId(Project project, UUID id);

    Optional<Branch> deleteByProjectAndId(Project project, UUID id);
}

````
