# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/controllers/RelationshipController.java

- repository: `SysML-v2-API-Services`
- source_path: `app/controllers/RelationshipController.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/controllers/RelationshipController.java
- source_bytes: 3888
- source_sha256: `9ec620785c94b5f034b8c5033cc249835c3d71bb2b855fbb271a8883d04737ea`
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

package controllers;

import config.MetamodelProvider;
import jackson.jsonld.DataJsonLdAdorner;
import jackson.jsonld.JsonLdAdorner;
import org.omg.sysml.metamodel.Relationship;
import org.omg.sysml.util.RelationshipDirection;
import play.Environment;
import play.mvc.Http.Request;
import play.mvc.Result;
import services.RelationshipService;

import javax.inject.Inject;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

public final class RelationshipController extends JsonLdController<Relationship, DataJsonLdAdorner.Parameters> {

    private final RelationshipService relationshipService;
    private final MetamodelProvider metamodelProvider;
    private final JsonLdAdorner<Relationship, DataJsonLdAdorner.Parameters> adorner;

    @Inject
    public RelationshipController(RelationshipService relationshipService, MetamodelProvider metamodelProvider, Environment environment) {
        this.relationshipService = relationshipService;
        this.metamodelProvider = metamodelProvider;
        this.adorner = new DataJsonLdAdorner<>(metamodelProvider, environment, INLINE_JSON_LD_CONTEXT);
    }

    @SuppressWarnings("OptionalUsedAsFieldOrParameterType")
    public Result getRelationshipsByProjectIdCommitIdRelatedElementId(UUID projectId, UUID commitId, UUID relatedElementId, Optional<String> direction, Optional<Boolean> excludeUsed, Request request) {
        PageRequest<UUID> pageRequest = uuidRequest(request);
        RelationshipDirection relationshipDirection = direction
                .flatMap(d -> Arrays.stream(RelationshipDirection.values())
                        .filter(rd -> rd.toString().equalsIgnoreCase(d))
                        .findAny())
                .orElse(RelationshipDirection.BOTH);

        List<Relationship> relationships = relationshipService.getRelationshipsByProjectCommitRelatedElement(
                projectId,
                commitId,
                relatedElementId,
                relationshipDirection,
                excludeUsed.orElse(false),
                pageRequest.getAfter(),
                pageRequest.getBefore(),
                pageRequest.getSize()
        );
        return buildPaginatedResult(relationships, projectId, commitId, request, pageRequest);
    }

    private Result buildPaginatedResult(List<Relationship> relationships, UUID projectId, UUID commitId, Request request, PageRequest pageRequest) {
        return uuidResponse(
                buildResult(relationships, List.class, metamodelProvider.getImplementationClass(Relationship.class), request, new DataJsonLdAdorner.Parameters(projectId, commitId)),
                relationships.size(),
                idx -> relationships.get(idx).getElementId(),
                request,
                pageRequest
        );
    }

    @Override
    protected JsonLdAdorner<Relationship, DataJsonLdAdorner.Parameters> getAdorner() {
        return adorner;
    }
}

````
