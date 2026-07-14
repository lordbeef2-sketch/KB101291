# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xtext/src/org/omg/kerml/xtext/validation/KerMLResourceValidator.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xtext/src/org/omg/kerml/xtext/validation/KerMLResourceValidator.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xtext/src/org/omg/kerml/xtext/validation/KerMLResourceValidator.java
- source_bytes: 1716
- source_sha256: `76a0fa90154b00d8b6f3f66dd7d5f659a5fa810246e894b47195f87fa088d930`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*****************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2024 Model Driven Solutions, Inc.
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
 * You should have received a copy of theEclipse Public License
 * along with this program.  If not, see <https://www.eclipse.org/legal/epl-2.0/>.
 *
 * @license EPL-2.0 <http://spdx.org/licenses/EPL-2.0>
 * 
 * Contributors:
 *  Ed Seidewitz
 * 
 *****************************************************************************/

package org.omg.kerml.xtext.validation;

import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.xtext.util.CancelIndicator;
import org.eclipse.xtext.validation.ResourceValidatorImpl;
import org.omg.kerml.xtext.linking.KerMLLazyLinkingResource;
import org.omg.sysml.util.ElementUtil;

public class KerMLResourceValidator extends ResourceValidatorImpl {

	@Override
	protected void resolveProxies(Resource resource, CancelIndicator monitor) {
		ElementUtil.transformAll(resource, false);
		getOperationCanceledManager().checkCanceled(monitor);
		if (resource instanceof KerMLLazyLinkingResource) {
			((KerMLLazyLinkingResource)resource).clearUnresolvableURIFragments();
		}
		super.resolveProxies(resource, monitor);
	}

}

````
