# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/EnumerationUsage_invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/EnumerationUsage_invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/EnumerationUsage_invalid.sysml.xt
- source_bytes: 1869
- source_sha256: `8621a33c5b5aa68f1ae8b3199c09bec94ce55fb5a19dbafd5132c98540db3b54`
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
			}
		}
	}
END_SETUP 
*/
package EnumerationUsage_invalid {
	attribute def A;
	enum def E {a; b; c;}
	enum def EE;
	
	attribute a1 : E;
	// XPECT errors --> "An enumeration attribute cannot have more than one type." at "attribute a2 : E, A;"
	attribute a2 : E, A;
	// XPECT errors --> "An enumeration attribute cannot have more than one type." at "attribute a3 : E, EE;"
	attribute a3 : E, EE;
	
	enum e1 : E;
	// XPECT errors ---> "An enumeration must be typed by one enumeration definition." at "enum e2 : A;"
	enum e2 : A;
	// XPECT errors --> "An enumeration must be typed by one enumeration definition." at "enum e3 : E, EE;"
	enum e3 : E, EE;
}

````
