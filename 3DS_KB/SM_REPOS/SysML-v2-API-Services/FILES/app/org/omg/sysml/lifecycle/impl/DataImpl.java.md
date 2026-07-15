# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/lifecycle/impl/DataImpl.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/lifecycle/impl/DataImpl.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/lifecycle/impl/DataImpl.java
- source_bytes: 1576
- source_sha256: `73065ba12647d2de293e13c596a9ba627a74afe1d7555b83bef454dfd11906fa`
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

package org.omg.sysml.lifecycle.impl;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import org.omg.sysml.lifecycle.Data;

import javax.persistence.*;
import java.util.UUID;

@Entity(name = "DataImpl")
@Table(name = "Data")
@DiscriminatorColumn(name = "type", discriminatorType = DiscriminatorType.STRING, length = 63)
@Inheritance(strategy = InheritanceType.SINGLE_TABLE)
@JsonTypeInfo(use = JsonTypeInfo.Id.NAME)
public abstract class DataImpl implements Data {

    private UUID key;

    @Id
    @GeneratedValue(generator = "UseExistingOrGenerateUUIDGenerator")
    @Column(name = "key")
    @JsonIgnore
    public UUID getKey() {
        return key;
    }

    public void setKey(UUID key) {
        this.key = key;
    }
}

````
