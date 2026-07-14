# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/scoping/ShortName_Scoping_Valid1.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/scoping/ShortName_Scoping_Valid1.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/scoping/ShortName_Scoping_Valid1.kerml.xt
- source_bytes: 989
- source_sha256: `55158ed2fc7f2102d574e60b36879c6a726ecc12267ea41472e663e1d8b269ba`
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

// XPECT noErrors --> ""
package Test {
	 classifier <'1'> A {
	 	classifier <'11A'> AA;
	 }

	//* XPECT scope at 1 ---
   		A, B, C, Test.A, Test.B, Test.C,
   		A.AA, B.AA, C.AA, Test.A.AA, Test.B.AA, Test.C.AA,
   		1, two, 3, Test.1, Test.two, Test.3,
        1.11A, two.11A, 3.11A, Test.1.11A, Test.two.11A, Test.3.11A, 
		1.AA, Test.1.AA,
   		A.11A, Test.A.11A, 
   		B.11A, Test.B.11A, 
   		C.11A, Test.C.11A,
   		two.AA, Test.two.AA,
   		3.AA, 3.AAA, 3.33A, Test.3.AA, Test.3.AAA,  Test.3.33A,
   		C.AAA, Test.C.AAA, 
   		C.33A, Test.C.33A
   	--- */
	 classifier <'two'> B specializes '1';
	 
	 classifier <'3'> C specializes 'two'{
	 	classifier <'33A'> AAA;
	 }
}


````
