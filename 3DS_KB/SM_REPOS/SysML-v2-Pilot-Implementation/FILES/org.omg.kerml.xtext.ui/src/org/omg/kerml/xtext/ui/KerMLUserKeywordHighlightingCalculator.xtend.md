# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xtext.ui/src/org/omg/kerml/xtext/ui/KerMLUserKeywordHighlightingCalculator.xtend

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xtext.ui/src/org/omg/kerml/xtext/ui/KerMLUserKeywordHighlightingCalculator.xtend`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xtext.ui/src/org/omg/kerml/xtext/ui/KerMLUserKeywordHighlightingCalculator.xtend
- source_bytes: 2363
- source_sha256: `0413e8bf119031dd3864d62af4d7d595c81a39dbe0dcafb1be8d4deb06ddf25b`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtend
/*****************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2022 Model Driven Solutions, Inc.
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
 * 
 * Contributors:
 *  Ed Seidewitz, MDS
 * 
 *****************************************************************************/
 package org.omg.kerml.xtext.ui

import org.eclipse.xtext.ide.editor.syntaxcoloring.ISemanticHighlightingCalculator
import org.eclipse.xtext.resource.XtextResource
import org.eclipse.xtext.ide.editor.syntaxcoloring.IHighlightedPositionAcceptor
import org.eclipse.xtext.util.CancelIndicator
import org.eclipse.xtext.ui.editor.syntaxcoloring.DefaultHighlightingConfiguration
import org.eclipse.xtext.impl.RuleCallImpl
import org.eclipse.xtext.service.OperationCanceledManager
import com.google.inject.Inject

class KerMLUserKeywordHighlightingCalculator implements ISemanticHighlightingCalculator {
	
	@Inject
	OperationCanceledManager cancelManager;
	
	override provideHighlightingFor(XtextResource resource, IHighlightedPositionAcceptor acceptor,
		CancelIndicator cancelIndicator) {
		if (resource !== null && resource.getParseResult() !== null) {
			val root = resource.getParseResult().getRootNode();
			for (node : root.getAsTreeIterable()) {
				cancelManager.checkCanceled(cancelIndicator);
				val grammarElement = node.grammarElement
				if (grammarElement instanceof RuleCallImpl) {
					val name = grammarElement.rule.name;
					if ("PrefixMetadataMember".equals(name) || "PrefixMetadataAnnotation".equals(name)) {
						acceptor.addPosition(node.getOffset(), node.getLength(), DefaultHighlightingConfiguration.KEYWORD_ID);
					}
				}
			}
		}
	}
	
}
````
