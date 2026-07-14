# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/AttributeUsage_invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/AttributeUsage_invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/AttributeUsage_invalid.sysml.xt
- source_bytes: 2356
- source_sha256: `31667ff3958af2677566175ab1c3acfc7d919238c01e52ebc8ec7e981a9b7d0a`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.sysml.xpect.tests.validation.invalid.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/Occurrences.kerml"}
		File {from ="/library.kernel/Objects.kerml"}
		File {from ="/library.kernel/Performances.kerml"}
		File {from ="/library.kernel/BaseFunctions.kerml"}
		File {from ="/library.kernel/ScalarValues.kerml"}
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Ports.sysml"}
		File {from ="/library.systems/Attributes.sysml"}
		File {from ="/library.systems/Connections.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
		       	File {from ="/library.kernel/Occurrences.kerml"}
				File {from ="/library.kernel/Objects.kerml"}
				File {from ="/library.kernel/Performances.kerml"}
				File {from ="/library.kernel/BaseFunctions.kerml"}
				File {from ="/library.kernel/ScalarValues.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
				File {from ="/library.systems/Attributes.sysml"}
				File {from ="/library.systems/Connections.sysml"}
			}
		}
	}
END_SETUP 
*/
package 'ValueProperty Example' {
	port def P;
	part def A {
		part a: A;
		port p: P;
	}
	part def Vehicle {
		// XPECT errors ---> "An attribute must be typed by attribute definitions." at "attribute a : A;"
		attribute a : A;
		// XPECT errors --> "An attribute must be typed by attribute definitions." at "attribute b : A::a;"
		// XPECT warnings --> "Duplicate of inherited member name 'self' from DataValue, Part" at "attribute b : A::a;"
		attribute b : A::a;
		// XPECT errors ---> "An attribute must be typed by attribute definitions." at "attribute s : P;"
		attribute s : P;
		// XPECT errors --> "An attribute must be typed by attribute definitions." at "attribute un : A::p;"
		// XPECT warnings --> "Duplicate of inherited member name 'self' from DataValue, Port" at "attribute un : A::p;"
		attribute un: A::p;
		// XPECT errors ---> "An attribute must be typed by attribute definitions." at "attribute n: AB;"
		attribute n: AB;
	}
	connection def  AB {
		end : A;
		end : A;
	}
}

````
