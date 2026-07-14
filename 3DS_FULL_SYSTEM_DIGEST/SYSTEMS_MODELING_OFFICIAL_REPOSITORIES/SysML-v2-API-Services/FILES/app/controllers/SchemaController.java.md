# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/controllers/SchemaController.java

- repository: `SysML-v2-API-Services`
- source_path: `app/controllers/SchemaController.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/controllers/SchemaController.java
- source_bytes: 3381
- source_sha256: `1a215f68126f10379061d4c83839e4c6c89a9d9aa4e8a4858ffb6cac93bd3807`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*
 * SysML v2 REST/HTTP Pilot Implementation
 * Copyright (C) 2022 Twingineer LLC
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

package controllers;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import jackson.jsonld.RecordAdorners.ProjectContainmentParameters;
import org.omg.sysml.lifecycle.Branch;
import play.libs.Json;
import play.mvc.Http.Request;
import play.mvc.Result;
import play.mvc.Results;
import services.SchemaService;

import javax.inject.Inject;
import java.util.*;

public class SchemaController extends BaseController {

    private final SchemaService schemaService;

    @Inject
    public SchemaController(SchemaService schemaService) {
        this.schemaService = schemaService;
    }

    public Result getSchemas(Request request) {
        PageRequest<String> pageRequest = stringRequest(request);
        List<JsonNode> schemas = schemaService.get(
                pageRequest.getAfter(),
                pageRequest.getBefore(),
                pageRequest.getSize()
        );
        return stringResponse(
                !schemas.isEmpty() ? Results.ok(format(schemas)) : Results.notFound(),
                schemas.size(),
                idx -> schemas.get(idx).path("$id").asText(null),
                request,
                pageRequest
        );
    }

    public Result getSchemaById(String schemaId) {
        Optional<JsonNode> schema = schemaService.getById(schemaId);
        if (schema.isEmpty()) {
            return Results.notFound();
        }
        return Results.ok(schema.get());
    }

    private JsonNode format(List<JsonNode> schemas) {
        ObjectNode object = Json.mapper().createObjectNode();
        String schemaValue = schemas.get(0).path("$schema").asText(null);
        if (schemaValue != null) {
            object.put("$schema", schemaValue);
        }
        ObjectNode defs = object.putObject("$defs");
        for (JsonNode schema : schemas) {
            String id = Objects.requireNonNull(schema.path("$id").asText(null));
            ObjectNode schemaNode = defs.putObject(id);
            Iterator<Map.Entry<String, JsonNode>> fieldIterator = schema.fields();
            while (fieldIterator.hasNext()) {
                Map.Entry<String, JsonNode> field = fieldIterator.next();
                String fieldName = field.getKey();
                switch (fieldName) {
                    case "$schema":
                    case "$defs":
                        break;
                    default:
                        schemaNode.put(fieldName, field.getValue());
                }
            }
        }
        return object;
    }
}

````
