# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.owl/src/org/omg/kerml/owl/qvt/KerML2OWL.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.owl/src/org/omg/kerml/owl/qvt/KerML2OWL.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.owl/src/org/omg/kerml/owl/qvt/KerML2OWL.java
- source_bytes: 2276
- source_sha256: `84faae8deb404fd5ddfca5059d8f5ec1b16541ef46c468441d9c3b6718aaafb5`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*****************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2018 Model Driven Solutions, Inc.
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

package org.omg.kerml.owl.qvt;

import java.nio.file.Paths;

import org.omg.kerml.owl.OwlStandaloneSetup;
import org.omg.kerml.owl.owl.OwlPackage;
import org.omg.kerml.xtext.KerMLStandaloneSetup;
import org.omg.sysml.lang.sysml.SysMLPackage;
import org.omg.sysml.qvt.QVTRunner;

public class KerML2OWL extends QVTRunner {

	@SuppressWarnings("unused")
	protected void initialize() {
		super.initialize();
		
	    SysMLPackage sysml = SysMLPackage.eINSTANCE;
	    
	    KerMLStandaloneSetup.doSetup();
	    
	    OwlPackage owl = OwlPackage.eINSTANCE;
	    OwlStandaloneSetup.doSetup();
	}
	
	@Override
	protected String constructOutputPath(final String... resourcePaths) {
		int n = resourcePaths.length;
		
		// Second to last resource path is presumed to be the input file path.
		String fileName = Paths.get(resourcePaths[n - 2]).getFileName().toString();
		int i = fileName.indexOf('.');
		if (i >= 0) {
			fileName = fileName.substring(0, i);
		}
		
		// Last resource path is presumed to be the output directory path,
		// to which the input file name is appended.
		return resourcePaths[n - 1] + "/" + fileName + ".owl";
	}
	
	public static void main(String[] args) {
		new KerML2OWL().run(args, 3, "KerML2OWL [-l logPath] qvtPath inputPaths outputPath");
	}

}

````
