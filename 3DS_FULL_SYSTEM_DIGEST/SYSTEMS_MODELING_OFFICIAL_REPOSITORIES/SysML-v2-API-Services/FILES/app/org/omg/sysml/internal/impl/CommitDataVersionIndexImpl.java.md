# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/internal/impl/CommitDataVersionIndexImpl.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/internal/impl/CommitDataVersionIndexImpl.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/internal/impl/CommitDataVersionIndexImpl.java
- source_bytes: 2311
- source_sha256: `03dfc23efe2390e48629a4be037cbc4750bb9e6c452f93b962b3b8c41238d185`
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

package org.omg.sysml.internal.impl;

import org.omg.sysml.internal.CommitDataVersionIndex;
import org.omg.sysml.internal.WorkingDataVersion;
import org.omg.sysml.lifecycle.Commit;
import org.omg.sysml.lifecycle.DataVersion;
import org.omg.sysml.lifecycle.impl.CommitImpl;
import org.omg.sysml.lifecycle.impl.DataVersionImpl;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;
import java.util.UUID;

@Entity(name = "CommitIndex")
public class CommitDataVersionIndexImpl implements CommitDataVersionIndex {
    private UUID id;
    private Commit commit;
    private Set<WorkingDataVersion> workingDataVersion;

    @Id
    public UUID getId() {
        return id;
    }

    @Override
    public void setId(UUID id) {
        this.id = id;
    }

    @Override
    @JoinColumn(name = "id")
    @OneToOne(targetEntity = CommitImpl.class)
    @MapsId
    public Commit getCommit() {
        return commit;
    }

    @Override
    public void setCommit(Commit commit) {
        this.commit = commit;
    }

    @Override
    @ManyToMany(targetEntity = WorkingDataVersionImpl.class, fetch = FetchType.LAZY)
    public Set<WorkingDataVersion> getWorkingDataVersion() {
        return workingDataVersion;
    }

    @Override
    public void setWorkingDataVersion(Set<WorkingDataVersion> workingDataVersion) {
        this.workingDataVersion = workingDataVersion;
    }
}

````
