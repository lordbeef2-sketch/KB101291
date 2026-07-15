# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ConnectorTest_NestedConnectorConnectingEndsGoodCase.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ConnectorTest_NestedConnectorConnectingEndsGoodCase.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ConnectorTest_NestedConnectorConnectingEndsGoodCase.kerml.xt
- source_bytes: 652
- source_sha256: `06269a94a669c942b5c83dce1966a27d4fae09c2ad007c5b5fdabf9e6f2d98d4`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/library/Links.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/library/Links.kerml"}
			}
		}
	}
END_SETUP 
*/

package test{
	feature x;
	feature y;
	assoc A {
		end end1;
		end end2;
		
		feature f {
			feature z;
		}
		
		connector c from end1 to f.z;
	}
	
	connector a:A from x to y;
	
	// Checks that ends from connector c are redefined.
	connector :> a.c from a.end1 to a.f.z;
}

````
