# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/data/impl/ExternalDataImpl.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/data/impl/ExternalDataImpl.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/data/impl/ExternalDataImpl.java
- source_bytes: 2496
- source_sha256: `cf1b7e418c03e3e6f70fc3f118755b223093dde8c0cff65f93b45bd397f07c25`
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

package org.omg.sysml.data.impl;

import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.annotation.JsonTypeName;
import org.hibernate.annotations.FetchMode;
import org.omg.sysml.data.ExternalData;
import org.omg.sysml.lifecycle.impl.DataImpl;

import javax.persistence.Column;
import javax.persistence.DiscriminatorValue;
import javax.persistence.Entity;
import javax.persistence.SecondaryTable;
import java.net.URI;
import java.util.UUID;

import static jackson.RecordSerialization.IDENTITY_FIELD;

@Entity(name = "ExternalDataImpl")
@SecondaryTable(name = "ExternalData")
@org.hibernate.annotations.Table(appliesTo = "ExternalData", fetch = FetchMode.SELECT, optional = false)
@DiscriminatorValue(value = "ExternalData")
@JsonTypeName(value = "ExternalData")
@JsonTypeInfo(use = JsonTypeInfo.Id.NAME)
public class ExternalDataImpl extends DataImpl implements ExternalData {

    private UUID id;

    @Column(name = "id", table = "ExternalData")
    @JsonGetter(value = IDENTITY_FIELD)
    public UUID getId() {
        return id;
    }

    @JsonSetter(value = IDENTITY_FIELD)
    public void setId(UUID id) {
        this.id = id;
    }

    private URI resourceIdentifier;

    @JsonGetter
    @Column(name = "resourceIdentifier")
    public URI getResourceIdentifier() { return resourceIdentifier; }

    @JsonSetter
    public void setResourceIdentifier(URI resourceIdentifier) {
        this.resourceIdentifier = resourceIdentifier;
    }
}

````
