# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xtext/src/org/omg/sysml/xtext/util/SysML2JSON.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xtext/src/org/omg/sysml/xtext/util/SysML2JSON.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xtext/src/org/omg/sysml/xtext/util/SysML2JSON.java
- source_bytes: 2254
- source_sha256: `357e845c0fa029f16936dd0dba7b0b7f1c645fd4134accd7fe320540fe598d31`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*****************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021 Model Driven Solutions, Inc.
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
package org.omg.sysml.xtext.util;

import org.omg.kerml.xtext.util.KerML2JSON;
import org.omg.sysml.xtext.SysMLStandaloneSetup;

public class SysML2JSON extends KerML2JSON {

	public SysML2JSON() {
		super();
		SysMLStandaloneSetup.doSetup();
		this.addExtension(".sysml");
	}
	
	/**
	 * The main program reads the KerML and SysML resources as given by its arguments and then processes all the input
	 * resources. Elements from library resources are only included if they are referenced from an input resource.
	 * 
	 * <p>Usage:
	 * 
	 * <p>SysML2JSON [-l library-base-path] [-g] input-path [library-path library-path...]
	 * 
	 * <p>where:
	 * 
	 * <ul>
	 * <li>-l library-base-path   gives the base path to used for reading model library resources</li>
	 * <li>-g                     specifies that implicit generalizations should be generated (the default is not to)</li>
	 * <li>input-path             is a path for reading input resources</li>
	 * <li>library-paths          are paths for reading library resources, relative to the library-base-path (if one is given)</li>
	 * </ul>
	 * 
	 */
	public static void main(String[] args) {
		try {
			new SysML2JSON().run(args);
		} catch (Exception e) {
			System.out.println("Error: " + e);
		}
	}

}

````
