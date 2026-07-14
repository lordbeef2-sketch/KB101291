# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/lifecycle/impl/BranchImpl.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/lifecycle/impl/BranchImpl.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/lifecycle/impl/BranchImpl.java
- source_bytes: 3414
- source_sha256: `23d6e1ba21131719e26cdf49fa9e7c248bc2ded297b543d42cec97f6961cc80b`
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

package org.omg.sysml.lifecycle.impl;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import jackson.RecordSerialization;
import org.omg.sysml.lifecycle.Branch;
import org.omg.sysml.lifecycle.Commit;
import org.omg.sysml.lifecycle.Project;
import org.omg.sysml.record.impl.RecordImpl;

import javax.persistence.*;
import javax.validation.constraints.NotNull;
import java.time.ZonedDateTime;

@Entity(name = "Branch")
public class BranchImpl extends RecordImpl implements Branch {
    private Project owningProject;
    private Commit head;
    private ZonedDateTime created;

    @Override
    @JsonProperty(required = true)
    public @NotNull String getName() {
        return super.getName();
    }

    @Override
    @JsonProperty(required = true)
    public void setName(@NotNull String name) {
        super.setName(name);
    }

    @Override
    @ManyToOne(targetEntity = ProjectImpl.class, fetch = FetchType.LAZY)
    @JsonSerialize(as = ProjectImpl.class, using = RecordSerialization.RecordSerializer.class)
    public Project getOwningProject() {
        return owningProject;
    }

    @JsonDeserialize(as = ProjectImpl.class, using = RecordSerialization.ProjectDeserializer.class)
    public void setOwningProject(Project owningProject) {
        this.owningProject = owningProject;
    }

    @Override
    @ManyToOne(targetEntity = CommitImpl.class, fetch = FetchType.LAZY)
    @JsonSerialize(as = CommitImpl.class, using = RecordSerialization.RecordSerializer.class)
    public Commit getHead() {
        return head;
    }

    @JsonDeserialize(as = CommitImpl.class, using = RecordSerialization.CommitDeserializer.class)
    public void setHead(Commit head) {
        this.head = head;
    }

    @Override
    @Transient
    @JsonSerialize(as = CommitImpl.class, using = RecordSerialization.RecordSerializer.class)
    public Commit getReferencedCommit() {
        return Branch.super.getReferencedCommit();
    }

    @Override
    @Column
    public ZonedDateTime getCreated() {
        return created;
    }

    public void setCreated(ZonedDateTime created) {
        this.created = created;
    }

    @Override
    @Transient
    public ZonedDateTime getDeleted() {
        return null;
    }

    @Transient
    @JsonProperty("@type")
    public String getType() {
        return Branch.NAME;
    }
}

````
