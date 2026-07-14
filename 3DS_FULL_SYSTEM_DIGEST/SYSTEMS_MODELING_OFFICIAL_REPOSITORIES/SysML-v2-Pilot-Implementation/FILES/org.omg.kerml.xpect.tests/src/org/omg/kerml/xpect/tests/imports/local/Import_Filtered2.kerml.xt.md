# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/local/Import_Filtered2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/local/Import_Filtered2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/local/Import_Filtered2.kerml.xt
- source_bytes: 687
- source_sha256: `ae279b34c76e9e91fa78666dddeb7cd4fcd48a54a818ae084ce9e0c769686567`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.imports.local.KerMLImportLocalTest
	ResourceSet {
		ThisFile {}
			File {from ="/library/Base.kerml"}
			File {from ="/library/Performances.kerml"}
			File {from ="/library/BaseFunctions.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
			   	File {from ="/library/Performances.kerml"}
				File {from ="/library/BaseFunctions.kerml"}
			}
		}
	}
END_SETUP 
*/
package Import_Filtered {
	public import P1::*;
	
	package P1 {
		feature f {
            feature a;
        }
		
	}
	
	package P2 {
		public import P1::*[false];
		feature x :> f.a;		
	}
}
````
