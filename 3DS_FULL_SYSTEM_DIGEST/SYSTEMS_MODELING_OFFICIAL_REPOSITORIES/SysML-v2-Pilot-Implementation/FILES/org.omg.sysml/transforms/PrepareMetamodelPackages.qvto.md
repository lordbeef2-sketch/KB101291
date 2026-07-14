# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml/transforms/PrepareMetamodelPackages.qvto

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml/transforms/PrepareMetamodelPackages.qvto`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml/transforms/PrepareMetamodelPackages.qvto
- source_bytes: 1836
- source_sha256: `22bbf23bc5cc0349c8adcc4098da859fb1bc40442db0222ca3aa0ce32bccae34`
- decoded_as: `utf-8`


## EXACT SOURCE

````qvto
/*****************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2022, 2023 Model Driven Solutions, Inc.
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
 *  Ed Seidewitz
 * 
 *****************************************************************************/
import PrepareMetamodel;

modeltype UML uses "http://www.eclipse.org/uml2/5.0.0/UML";

transformation PrepareMetamodelPackages(in export: UML, in standard: UML, out prepared: UML)
	extends PrepareMetamodel;

main() {
	run()
}

helper mapModel(syntax : Package, model: Model) {
	var kermlSyntax = syntax.ownedMember[Package]![name = 'KerML'];
	var sysmlSyntax = syntax.ownedMember[Package]![name = 'SysML'];
	kermlSyntax.ownedMember[Package].map Package(model);	
	sysmlSyntax.ownedMember[Package].map Package(model);	
}

mapping Package::Package(inout model: Model) {
	log("Top-level package " + nameOf(self));
	if self <> model then {
		var package = object Package {
			name := self.name;
		};
		model.packagedElement += package;
		self.ownedMember[Package]->map Namespace(package);
		package.packagedElement[Package]->destroy();
	} endif;
}
````
