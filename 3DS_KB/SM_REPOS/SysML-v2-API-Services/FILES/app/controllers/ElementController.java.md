# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/controllers/ElementController.java

- repository: `SysML-v2-API-Services`
- source_path: `app/controllers/ElementController.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/controllers/ElementController.java
- source_bytes: 5260
- source_sha256: `c38041fc5d97652b40e03e19e644cb68e6aa00117849b14a91931f22abc34d76`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*
 * SysML v2 REST/HTTP Pilot Implementation
 * Copyright (C) 2020 InterCAX LLC
 * Copyright (C) 2020 California Institute of Technology ("Caltech")
 * Copyright (C) 2021-2022 Twingineer LLC
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
import config.MetamodelProvider;
import jackson.JacksonHelper;
import jackson.jsonld.DataJsonLdAdorner;
import jackson.jsonld.JsonLdAdorner;
import org.omg.sysml.data.ProjectUsage;
import org.omg.sysml.metamodel.Element;
import play.Environment;
import play.libs.Json;
import play.mvc.Http.Request;
import play.mvc.Result;
import play.mvc.Results;
import services.ElementService;

import javax.inject.Inject;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

@SuppressWarnings("OptionalUsedAsFieldOrParameterType")
public final class ElementController extends JsonLdController<Element, DataJsonLdAdorner.Parameters> {

    private final ElementService elementService;
    private final MetamodelProvider metamodelProvider;
    private final JsonLdAdorner<Element, DataJsonLdAdorner.Parameters> adorner;

    @Inject
    public ElementController(ElementService elementService, MetamodelProvider metamodelProvider, Environment environment) {
        this.elementService = elementService;
        this.metamodelProvider = metamodelProvider;
        this.adorner = new DataJsonLdAdorner<>(metamodelProvider, environment, INLINE_JSON_LD_CONTEXT);
    }

    public Result getElementsByProjectIdCommitId(UUID projectId, UUID commitId, Optional<Boolean> excludeUsed, Request request) {
        PageRequest<UUID> pageRequest = uuidRequest(request);
        List<Element> elements = elementService.getElementsByProjectIdCommitId(projectId, commitId, excludeUsed.orElse(false), pageRequest.getAfter(), pageRequest.getBefore(), pageRequest.getSize());
        return buildPaginatedResult(elements, projectId, commitId, request, pageRequest);
    }

    public Result getElementByProjectIdCommitIdElementId(UUID projectId, UUID commitId, UUID elementId, Optional<Boolean> excludeUsed, Request request) {
        Optional<Element> element = elementService.getElementByProjectIdCommitIdElementId(projectId, commitId, elementId, excludeUsed.orElse(false));
        return buildResult(element.orElse(null), request, new DataJsonLdAdorner.Parameters(projectId, commitId));
    }

    public Result getProjectUsageByProjectIdCommitIdElementId(UUID projectId, UUID commitId, UUID elementId, Request request) {
        if (respondWithJsonLd(request)) {
            // TODO implement
            return Results.status(NOT_IMPLEMENTED);
        }
        Optional<ProjectUsage> projectUsage = elementService.getProjectUsageByProjectIdCommitIdElementId(projectId, commitId, elementId);
        if (projectUsage.isEmpty()) {
            return Results.notFound();
        }
        JsonNode json = JacksonHelper.objectToTree(
                projectUsage,
                Json.mapper()
        );
        return Results.ok(json);
    }

    public Result getRootsByProjectIdCommitId(UUID projectId, UUID commitId, Optional<Boolean> excludeUsed, Request request) {
        PageRequest<UUID> pageRequest = uuidRequest(request);
        List<Element> roots = elementService.getRootsByProjectIdCommitId(projectId, commitId, excludeUsed.orElse(false), pageRequest.getAfter(), pageRequest.getBefore(), pageRequest.getSize());
        return buildPaginatedResult(roots, projectId, commitId, request, pageRequest);
    }

    public Result getElementByProjectIdCommitIdQualifiedName(UUID projectId, UUID commitId, String qualifiedName, Request request) {
        Optional<Element> element = elementService.getElementByProjectIdCommitIdQualifiedName(projectId, commitId, qualifiedName);
        return buildResult(element.orElse(null), request, new DataJsonLdAdorner.Parameters(projectId, commitId));
    }

    private Result buildPaginatedResult(List<Element> elements, UUID projectId, UUID commitId, Request request, PageRequest<UUID> pageRequest) {
        return uuidResponse(
                buildResult(elements, List.class, metamodelProvider.getImplementationClass(Element.class), request, new DataJsonLdAdorner.Parameters(projectId, commitId)),
                elements.size(),
                idx -> elements.get(idx).getElementId(),
                request,
                pageRequest
        );
    }

    @Override
    protected JsonLdAdorner<Element, DataJsonLdAdorner.Parameters> getAdorner() {
        return adorner;
    }
}

````
