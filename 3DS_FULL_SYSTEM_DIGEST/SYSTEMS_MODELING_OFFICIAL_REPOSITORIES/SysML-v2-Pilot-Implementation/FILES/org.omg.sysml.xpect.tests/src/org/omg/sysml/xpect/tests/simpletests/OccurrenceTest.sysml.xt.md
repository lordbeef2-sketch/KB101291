# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/OccurrenceTest.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/OccurrenceTest.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/OccurrenceTest.sysml.xt
- source_bytes: 1424
- source_sha256: `5621c69416b76f4a23edcef05148e35e6616ea0ffdebd7ef6b86b7eecb43d583`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.sysml.xpect.tests.simpletests.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
       	File {from ="/library.kernel/Occurrences.kerml"}
       	File {from ="/library.kernel/Objects.kerml"}
       	File {from ="/library.systems/Attributes.sysml"}
       	File {from ="/library.systems/Items.sysml"}
       	File {from ="/library.systems/Parts.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
		       	File {from ="/library.kernel/Occurrences.kerml"}
		       	File {from ="/library.kernel/Objects.kerml"}
		      	File {from ="/library.systems/Attributes.sysml"}
		       	File {from ="/library.systems/Items.sysml"}
		       	File {from ="/library.systems/Parts.sysml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package OccurrenceTest {
	occurrence def Occ {
		attribute a;
		ref occurrence occ1 : Occ;
		occurrence occ2 : Occ;
		item x;
		part y;
		
		individual snapshot s : Ind;
		timeslice t;
	}
	
	occurrence occ : Occ {
		occurrence o1 : Occ;
		ref occurrence o2 : Occ;
		item z;
	}

	individual occurrence def Ind {
		snapshot s2;
		timeslice t2;
	}
	individual occurrence ind : Ind, Occ {
		snapshot s3;
		individual timeslice t3 :> ind;
        individual snapshot s4 : Ind;
	}

	occurrence o1 {
	  occurrence o2;
	}
}
````
