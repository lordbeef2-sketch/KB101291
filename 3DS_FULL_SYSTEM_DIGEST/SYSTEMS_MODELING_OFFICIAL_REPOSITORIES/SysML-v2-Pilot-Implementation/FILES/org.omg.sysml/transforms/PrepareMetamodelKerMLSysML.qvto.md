# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml/transforms/PrepareMetamodelKerMLSysML.qvto

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml/transforms/PrepareMetamodelKerMLSysML.qvto`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml/transforms/PrepareMetamodelKerMLSysML.qvto
- source_bytes: 2237
- source_sha256: `636678586f9cd7a9de8dfa256f30ebc7481af0198cd1cdfb9ea8f417b5b00fcc`
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

transformation PrepareMetamodelKerMLSysML(in export: UML, in standard: UML, out kerml: UML, out sysml: UML)
	extends PrepareMetamodel;

main() {
	run()
}

helper run() {
	var syntax := export.objects()[Package]![name = "SysML Abstract Syntax"];
	assert fatal (syntax <> null) with log ("Abstract Syntax not found.");
	
	var kermlModel = object Model@kerml { 
		name := "kerml";
		URI := "https://www.omg.org/spec/KerML/" + version;
	};
	
	var sysmlModel = object Model@sysml { 
		name := "sysml";
		URI := "https://www.omg.org/spec/SysML/" + version;
	};
	
	mapModel(syntax, kermlModel, sysmlModel);
	fixLiteralRational();	
}

helper mapModel(syntax : Package, kermlModel: Model, sysmlModel : Model) {
	var kermlSyntax = syntax.packagedElement[Package]![name = 'KerML'];
	var sysmlSyntax = syntax.packagedElement[Package]![name = 'SysML'];
	mapPackageFlat(kermlSyntax, "Root", kermlModel);
	mapPackageFlat(kermlSyntax, "Core", kermlModel);
	mapPackageFlat(kermlSyntax, "Kernel", kermlModel);
	mapPackageFlat(sysmlSyntax, "Systems", sysmlModel);
	kermlModel.packagedElement[Package]->destroy();	
	sysmlModel.packagedElement[Package]->destroy();	
}
````
