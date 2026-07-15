# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xtext.ui/src/org/omg/sysml/xtext/ui/xmi/EcoreEditorOpener.xtend

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xtext.ui/src/org/omg/sysml/xtext/ui/xmi/EcoreEditorOpener.xtend`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xtext.ui/src/org/omg/sysml/xtext/ui/xmi/EcoreEditorOpener.xtend
- source_bytes: 1643
- source_sha256: `af2889d740fc1bd764d75474906e958ec89503248dcada08cc80f7a3bd422374`
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

import org.eclipse.xtext.ui.editor.LanguageSpecificURIEditorOpener
import org.eclipse.ui.IEditorPart
import org.eclipse.emf.common.util.URI
import org.eclipse.emf.ecore.EReference
import org.eclipse.emf.ecore.presentation.EcoreEditor

class EcoreEditorOpener extends LanguageSpecificURIEditorOpener {
	
	
	override protected selectAndReveal(IEditorPart openEditor, URI uri, EReference crossReference, int indexInList, boolean select) {
		if (uri.fragment !== null){
			val editor = openEditor.getAdapter(EcoreEditor)
			val eObject = editor.editingDomain.resourceSet.getEObject(uri, false)
			editor.selectionToViewer = #[eObject]
		}
	}
	
	override protected getEditorId() {
		'org.omg.sysml.lang.sysml.presentation.SysMLxEditorID'
	}
	
}
````
