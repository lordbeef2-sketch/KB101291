# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xtext.ui/src/org/omg/kerml/xtext/ui/KerMLActivator.xtend

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xtext.ui/src/org/omg/kerml/xtext/ui/KerMLActivator.xtend`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xtext.ui/src/org/omg/kerml/xtext/ui/KerMLActivator.xtend
- source_bytes: 1690
- source_sha256: `8321db66aafcb2ce96376a21782a5d8c3252ccdb8e17338747bf6ed1c5a12d9b`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtend
/**
 * SysML 2 Pilot Implementation
 * Copyright (C) 2025 Model Driven Solutions, Inc.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the Eclipse Public License as published by
 * the Eclipse Foundation, version 2 of the License.
 * (at your option) any later version.
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
 * 
 * Contributors:
 *   Laszlo Gati, MDS
 */
package org.omg.kerml.xtext.ui

import org.omg.kerml.xtext.ui.internal.XtextActivator
import org.omg.kerml.xtext.KerMLRuntimeModule
import org.omg.kerml.xtext.xmi.KerMLxRuntimeModule
import org.omg.kerml.xtext.ui.xmi.KerMLxUIModule

class KerMLActivator extends XtextActivator {
		override getRuntimeModule(String grammar) {
			
		return switch (grammar) {
			case ORG_OMG_KERML_XTEXT_KERML: new KerMLRuntimeModule
			case KerMLxRuntimeModule::KERMLX_LANGUAGE_NAME: new KerMLxRuntimeModule
			default: throw new IllegalArgumentException(grammar)
		}
	}

	override getUiModule(String grammar) {
		return switch (grammar) {
			case ORG_OMG_KERML_XTEXT_KERML: new KerMLUiModule(this)
			case KerMLxRuntimeModule::KERMLX_LANGUAGE_NAME: new KerMLxUIModule(this)
			default: throw new IllegalArgumentException(grammar)
		}
	}
}
````
