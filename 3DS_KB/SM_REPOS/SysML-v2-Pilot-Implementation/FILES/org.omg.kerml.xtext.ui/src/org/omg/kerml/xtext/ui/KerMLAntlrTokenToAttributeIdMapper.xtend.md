# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xtext.ui/src/org/omg/kerml/xtext/ui/KerMLAntlrTokenToAttributeIdMapper.xtend

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xtext.ui/src/org/omg/kerml/xtext/ui/KerMLAntlrTokenToAttributeIdMapper.xtend`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xtext.ui/src/org/omg/kerml/xtext/ui/KerMLAntlrTokenToAttributeIdMapper.xtend
- source_bytes: 1703
- source_sha256: `8e7a248e52ac096329f5c983a33b869ac7e8b96f5208f65ce077f9d867ea9af4`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtend
/*****************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2023 Model Driven Solutions, Inc.
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
package org.omg.kerml.xtext.ui;

import org.eclipse.xtext.ide.editor.syntaxcoloring.HighlightingStyles;
import org.eclipse.xtext.ui.editor.syntaxcoloring.DefaultAntlrTokenToAttributeIdMapper;

class KerMLAntlrTokenToAttributeIdMapper extends DefaultAntlrTokenToAttributeIdMapper {

	protected override calculateId(String tokenName, int tokenType) {
		if("RULE_STRING_VALUE".equals(tokenName))
			HighlightingStyles.STRING_ID
		else if ("RULE_DECIMAL_VALUE".equals(tokenName) || "RULE_EXP_VALUE".equals(tokenName))
			HighlightingStyles.NUMBER_ID
		else if("RULE_ML_NOTE".equals(tokenName) || "RULE_SL_NOTE".equals(tokenName))
			HighlightingStyles.COMMENT_ID
		else
			super.calculateId(tokenName, tokenType);
	}

}

````
