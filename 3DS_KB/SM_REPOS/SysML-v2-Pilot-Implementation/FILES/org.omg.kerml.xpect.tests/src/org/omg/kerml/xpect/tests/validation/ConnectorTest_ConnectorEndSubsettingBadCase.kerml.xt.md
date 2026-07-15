# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ConnectorTest_ConnectorEndSubsettingBadCase.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ConnectorTest_ConnectorEndSubsettingBadCase.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ConnectorTest_ConnectorEndSubsettingBadCase.kerml.xt
- source_bytes: 763
- source_sha256: `fd8df30d67e2d7e348a2f3cec69ef3b01c9494743288e90ee6ee54aa681b275b`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/library/Links.kerml"}
		File {from ="/library/Occurrences.kerml"}
		File {from ="/library/Performances.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/library/Links.kerml"}
				File {from ="/library/Occurrences.kerml"}
				File {from ="/library/Performances.kerml"}
			}
		}
	}
END_SETUP 
*/

package test{
	feature x;
	feature y;
	
	connector c {
		feature f;
		end a ::> x :> f[1];
		//XPECT errors --> "Couldn't resolve reference to Feature 'f'." at "f"
		end b ::> f[1];
		end c ::> y[1];
	}
}

````
