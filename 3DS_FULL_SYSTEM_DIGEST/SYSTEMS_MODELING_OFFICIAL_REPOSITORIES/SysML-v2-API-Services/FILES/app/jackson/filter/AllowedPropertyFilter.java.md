# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/jackson/filter/AllowedPropertyFilter.java

- repository: `SysML-v2-API-Services`
- source_path: `app/jackson/filter/AllowedPropertyFilter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/jackson/filter/AllowedPropertyFilter.java
- source_bytes: 1446
- source_sha256: `be32e82ffb6c6aa06d4bd7bc7983cc2279df7f6d54f1a38b2ad228b1ddbb7975`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*
 * SysML v2 REST/HTTP Pilot Implementation
 * Copyright (C) 2020  InterCAX LLC
 * Copyright (C) 2020  California Institute of Technology ("Caltech")
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

package jackson.filter;

import com.fasterxml.jackson.databind.ser.impl.SimpleBeanPropertyFilter.FilterExceptFilter;

import java.util.Collections;
import java.util.Set;

public class AllowedPropertyFilter extends FilterExceptFilter {

    private Set<String> allowedProperties;

    public AllowedPropertyFilter(Set<String> properties) {
        super(properties);
    }

    public Set<String> getAllowedProperties() {
        if (allowedProperties == null) {
            allowedProperties = Collections.unmodifiableSet(_propertiesToInclude);
        }
        return allowedProperties;
    }
}

````
