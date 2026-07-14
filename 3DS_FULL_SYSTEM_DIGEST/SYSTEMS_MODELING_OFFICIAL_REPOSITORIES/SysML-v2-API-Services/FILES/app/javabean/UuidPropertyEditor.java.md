# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/javabean/UuidPropertyEditor.java

- repository: `SysML-v2-API-Services`
- source_path: `app/javabean/UuidPropertyEditor.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/javabean/UuidPropertyEditor.java
- source_bytes: 1081
- source_sha256: `37a76cf9ae0563bd5a8fce0a69ab9359014bcc9330488116932e6a91bf1c547f`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*
 * SysML v2 REST/HTTP Pilot Implementation
 * Copyright (C) 2022-2023 Twingineer LLC
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

package javabean;

import java.beans.PropertyEditorSupport;
import java.util.UUID;

public class UuidPropertyEditor extends PropertyEditorSupport {

    @Override
    public void setAsText(String text) throws IllegalArgumentException {
        setValue(text != null ? UUID.fromString(text) : null);
    }
}

````
