# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xtext.ui/src/org/omg/sysml/xtext/ui/xmi/SysMLxUIModule.xtend

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xtext.ui/src/org/omg/sysml/xtext/ui/xmi/SysMLxUIModule.xtend`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xtext.ui/src/org/omg/sysml/xtext/ui/xmi/SysMLxUIModule.xtend
- source_bytes: 1390
- source_sha256: `cee8b3c2205292e6d2759400a4674321c0d7dc62e3e93012f3bcebb50d09c11e`
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
package org.omg.sysml.xtext.ui.xmi

import org.eclipse.ui.plugin.AbstractUIPlugin
import org.eclipse.xtext.ui.resource.generic.EmfUiModule
import com.google.inject.Binder
import org.eclipse.xtext.ui.LanguageSpecific
import org.eclipse.xtext.ui.editor.IURIEditorOpener

class SysMLxUIModule extends EmfUiModule {
	
	new(AbstractUIPlugin plugin) {
		super(plugin)
	}
	
	override configureLanguageSpecificURIEditorOpener(Binder binder) {
		binder.bind(IURIEditorOpener).annotatedWith(LanguageSpecific).to(EcoreEditorOpener)
	}
	
}
````
