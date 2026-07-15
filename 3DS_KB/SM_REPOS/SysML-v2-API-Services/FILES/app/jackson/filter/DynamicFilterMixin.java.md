# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/jackson/filter/DynamicFilterMixin.java

- repository: `SysML-v2-API-Services`
- source_path: `app/jackson/filter/DynamicFilterMixin.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/jackson/filter/DynamicFilterMixin.java
- source_bytes: 1056
- source_sha256: `7402d92b517446e6963b8da361abf17a332f71e3fe61445f50662a16cc907a9f`
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

import com.fasterxml.jackson.annotation.JsonFilter;

@JsonFilter(DynamicFilterMixin.FILTER_NAME)
public class DynamicFilterMixin {
    public static final String FILTER_NAME = "_dynamicFilter";
}

````
