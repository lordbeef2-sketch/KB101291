# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/FeaturePath_Invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/FeaturePath_Invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/FeaturePath_Invalid.sysml.xt
- source_bytes: 1823
- source_sha256: `738b98760bb486780d2f86a28e659b8cccf3fbeeecb2d6116e2850a56ecda8c1`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.sysml.xpect.tests.simpletests.SysMLTests
	ResourceSet {
		ThisFile {} 
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Connections.sysml"}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/BaseFunctions.kerml"}
		File {from ="/library.kernel/ControlFunctions.kerml"}
		File {from ="/library.kernel/Links.kerml"}
		File {from ="/library.kernel/Objects.kerml"}
		File {from ="/library.kernel/Occurrences.kerml"}
		File {from ="/library.kernel/Performances.kerml"}
		File {from ="/library.kernel/Transfers.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {} 
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Connections.sysml"}
				File {from ="/library.kernel/Base.kerml"}
				File {from ="/library.kernel/BaseFunctions.kerml"}
				File {from ="/library.kernel/ControlFunctions.kerml"}
				File {from ="/library.kernel/Links.kerml"}
				File {from ="/library.kernel/Objects.kerml"}
				File {from ="/library.kernel/Occurrences.kerml"}
				File {from ="/library.kernel/Performances.kerml"}
				File {from ="/library.kernel/Transfers.kerml"}
			}
		}
	}
END_SETUP
*/
package Q {
  part def F {
  	part a : A;
  }
  
  part f : F;
  
  part def A {
    // XPECT errors --> "Must be an accessible feature (use dot notation for nesting)" at "f::a"
    part g = f::a;
  }
  
  part def B {
  	part f : F;
  	part a : A;
  }
  
  part def C {
  	part b : B;
  
	part c subsets b.f {
	  	part aa subsets a;
	}
	
    // XPECT errors --> "Must be an accessible feature (use dot notation for nesting)" at "c::aa"
	connect b.f.a to c::aa;
  }
	
}

````
