# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/local/Import_All.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/local/Import_All.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/local/Import_All.kerml.xt
- source_bytes: 1045
- source_sha256: `07ddf0f945b4f6a35793b2f2820ceaf590b4f25849542812dfbebdef10a21867`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.imports.local.KerMLImportLocalTest
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

 
package Import_All {
	package A {
		private classifier X;
	}
	
	package B {
		public import A::*;
		private classifier Y1;
		public classifier Y2;
	}
	
	package C {
		private import B::*;
		private classifier Z;
		private package C1 {
			public classifier U;
		}
	}
	
	package D {
		public import all C::*;

	    // XPECT errors --> "Couldn't resolve reference to Type 'X'." at "X"		
		x : X;

	    // XPECT errors --> "Couldn't resolve reference to Type 'Y1'." at "Y1"		
		y1 : Y1;
		
		// XPECT linkedName at Y2 --> Import_All.B.Y2
		y2 : Y2;
		
		// XPECT linkedName at Z --> Import_All.C.Z
		z : Z;		
	}
	
	package E {
		public import all C::**;
		public import all B::Y1;
		
		u : C1::U;
		y1 : Y1;
	}
}

````
