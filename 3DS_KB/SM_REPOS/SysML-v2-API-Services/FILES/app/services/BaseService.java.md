# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/services/BaseService.java

- repository: `SysML-v2-API-Services`
- source_path: `app/services/BaseService.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/services/BaseService.java
- source_bytes: 1729
- source_sha256: `732246a9783a7d0f9864a3a6161f1b72504276cd0111f595f07d09790f837275`
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

package services;

import dao.Dao;

import javax.annotation.Nullable;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

public class BaseService<I, D extends Dao<I>> {

    protected final D dao;

    protected BaseService(D dao) {
        this.dao = dao;
    }

    public List<I> getAll() {
        return dao.findAll();
    }

    public List<I> getAll(@Nullable UUID after, @Nullable UUID before, int maxResults) {
        return dao.findAll(after, before, maxResults);
    }

    public Optional<I> getById(UUID id) {
        return dao.findById(id);
    }

    public Optional<I> persist(I i) {
        return dao.persist(i);
    }

    public Optional<I> update(I i) {
        return dao.update(i);
    }

    public Optional<I> deleteById(UUID id) {
        return dao.deleteById(id);
    }
}

````
