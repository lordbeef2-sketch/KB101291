# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xtext.ui/src/org/omg/kerml/xtext/ui/outline/ImplicitNode.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xtext.ui/src/org/omg/kerml/xtext/ui/outline/ImplicitNode.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xtext.ui/src/org/omg/kerml/xtext/ui/outline/ImplicitNode.java
- source_bytes: 1564
- source_sha256: `3d76febc68f5a26ed7f28badd9e43069258e4437cff7c19b0cac10e2d5c1cd94`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 * SysML 2 Pilot Implementation
  * Copyright (c) 2020 Model Driven Solutions, Inc. 
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
 *  Zoltan Ujhelyi, MDS
 */
package org.omg.kerml.xtext.ui.outline;

import org.eclipse.emf.ecore.EClass;
import org.eclipse.swt.graphics.Image;
import org.eclipse.xtext.ui.editor.outline.IOutlineNode;
import org.eclipse.xtext.ui.editor.outline.impl.AbstractOutlineNode;

/**
 * This class is used as an alternative outline node implementation for
 * generalization classes that do not expect a related EObject to be added.
 *
 */
public class ImplicitNode extends AbstractOutlineNode {

	public ImplicitNode(IOutlineNode parent, Image image, EClass eClass) {
		super(parent, image, eClass.getName() + " (implicit)", false);
	}
	
	public ImplicitNode(IOutlineNode parent, Image image, String text) {
		super(parent, image, text + " (implicit)", false);
	}
	
}

````
