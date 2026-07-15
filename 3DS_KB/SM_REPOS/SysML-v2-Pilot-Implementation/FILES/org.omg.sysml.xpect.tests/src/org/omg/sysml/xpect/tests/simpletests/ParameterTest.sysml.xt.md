# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/ParameterTest.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/ParameterTest.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/ParameterTest.sysml.xt
- source_bytes: 2310
- source_sha256: `d5c212818748ae59d6e07f95b4f969606086a70acc9db4f100de27feddff10c4`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.sysml.xpect.tests.simpletests.SysMLTests
	ResourceSet {
		ThisFile {} 
 		File {from ="/library.kernel/Base.kerml"}
 		File {from ="/library.kernel/Links.kerml"}
       	File {from ="/library.kernel/Occurrences.kerml"}
       	File {from ="/library.kernel/Objects.kerml"}
		File {from ="/library.kernel/BaseFunctions.kerml"}
		File {from ="/library.kernel/Performances.kerml"}
		File {from ="/library.kernel/ControlPerformances.kerml"}
		File {from ="/library.kernel/TransitionPerformances.kerml"}
		File {from ="/library.kernel/Transfers.kerml"}
		File {from ="/library.kernel/ScalarFunctions.kerml"}
		File {from ="/library.kernel/ScalarValues.kerml"}
		File {from ="/library.systems/Attributes.sysml"}
		File {from ="/library.systems/Items.sysml"}
 		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Actions.sysml"}
		File {from ="/library.systems/Calculations.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {} 
		 		File {from ="/library.kernel/Base.kerml"}
		 		File {from ="/library.kernel/Links.kerml"}
		       	File {from ="/library.kernel/Occurrences.kerml"}
		       	File {from ="/library.kernel/Objects.kerml"}
				File {from ="/library.kernel/BaseFunctions.kerml"}
				File {from ="/library.kernel/Performances.kerml"}
				File {from ="/library.kernel/ControlPerformances.kerml"}
				File {from ="/library.kernel/TransitionPerformances.kerml"}
				File {from ="/library.kernel/Transfers.kerml"}
				File {from ="/library.kernel/ScalarFunctions.kerml"}
				File {from ="/library.kernel/ScalarValues.kerml"}
				File {from ="/library.systems/Attributes.sysml"}
				File {from ="/library.systems/Items.sysml"}
		 		File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Actions.sysml"}
				File {from ="/library.systems/Calculations.sysml"}
			}
		}
	}
END_SETUP
*/
// XPECT noErrors ---> ""
package ParameterTest {
	attribute def A {
		attribute x : ScalarValues::String;
		attribute y : A;
	}
	
	attribute a : A;
	
	calc def F {
		in p : A;
		in q : ScalarValues::Integer;
		return : ScalarValues::Integer;
	}
	
	attribute f = F(a, 2);
	attribute g = F(q = 1, p = a);
	
	attribute b = new A(y=a, x=""); 
	attribute c = new A("test2");
}
````
