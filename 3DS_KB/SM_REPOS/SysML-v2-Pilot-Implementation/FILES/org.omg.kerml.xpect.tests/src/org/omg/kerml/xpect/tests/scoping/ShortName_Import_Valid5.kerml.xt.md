# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/scoping/ShortName_Import_Valid5.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/scoping/ShortName_Import_Valid5.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/scoping/ShortName_Import_Valid5.kerml.xt
- source_bytes: 1262
- source_sha256: `58b0ee40ff6e1022c95b1db848a2b7998751780f89d841855e623093112a14f6`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.scoping.KerMLScopingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
			}
		}
	}
END_SETUP 
*/

//XPECT noErrors ---> ""
package Test {

	package Test0 {
		public import Test2::VP_Id::*;
		//XPECT linkedName at VVP_Id::VVVP_Id--> Test.Test2.VP.VVP.VVVP
		classifier A specializes VVP_Id::VVVP_Id;
		//XPECT linkedName at VVP::VVVP_Id--> Test.Test2.VP.VVP.VVVP
		classifier B specializes VVP::VVVP_Id;
		//XPECT linkedName at VVP_Id::VVVP--> Test.Test2.VP.VVP.VVVP
		classifier C specializes VVP_Id::VVVP;
		//XPECT linkedName at VVP_Id::VVVP_Id::VVVVP_Id_alias--> Test.Test2.VP.VVP.VVVP.VVVVP
		classifier D specializes VVP_Id::VVVP_Id::VVVVP_Id_alias;
		
	}
	package Test1 {
		public import Test2::VP_Id::*;
		//XPECT linkedName at VVP_Id --> Test.Test2.VP.VVP
		classifier A specializes VVP_Id;
	}
	
	package Test2 {
		public classifier <'VP_Id'> VP {	
			public classifier <'VVP_Id'> VVP {
				public classifier <'VVVP_Id'> VVVP{
					public classifier <'VVVVP_Id'> VVVVP;
					alias VVVVP_Id_alias for VVVVP_Id;
				}
			}
		}
		
	}
	
}

	
````
