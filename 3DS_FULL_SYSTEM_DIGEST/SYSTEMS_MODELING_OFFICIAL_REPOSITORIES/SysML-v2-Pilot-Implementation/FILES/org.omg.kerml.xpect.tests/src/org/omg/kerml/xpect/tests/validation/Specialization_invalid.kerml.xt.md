# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Specialization_invalid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Specialization_invalid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Specialization_invalid.kerml.xt
- source_bytes: 2047
- source_sha256: `4cf13b3caba63eb60db43bdd3cb251a1fb40cb06ecd5d2df0cc284a06d4440f7`
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
		File {from ="/library/Objects.kerml"}
		File {from ="/library/Performances.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/library/Links.kerml"}
				File {from ="/library/Occurrences.kerml"}
				File {from ="/library/Objects.kerml"}
				File {from ="/library/Performances.kerml"}
			}
		}
	}
END_SETUP 
*/
package Specialization_invalid {
	classifier A;
	classifier B;
	classifier C conjugates A;
	
	// XPECT errors--->"Conjugated type cannot be a specialized type" at "C"
	subtype C specializes B;
	
	datatype D1;
	//* XPECT errors ---
	   "Cannot specialize class or association" at "C1"
	   "Cannot specialize class or association" at "A1"
	   ---
	*/
	// XPECT warnings ---> "Duplicate of inherited member name 'self' from DataValue, Occurrence" at "datatype D2 specializes D1, C1, A1;"
	datatype D2 specializes D1, C1, A1;
	
	class C1;
	//* XPECT errors ---
	   "Cannot specialize data type or association" at "D1"
	   "Cannot specialize data type or association" at "A1"
	   ---
	*/
	// XPECT warnings ---> "Duplicate of inherited member name 'self' from DataValue, Occurrence" at "class C2 specializes C1, D1, A1;"
	class C2 specializes C1, D1, A1;
	
	abstract assoc A1;
	abstract assoc struct A2 specializes A, A1;
	abstract interaction A3 specializes A, A1;
	
	// XPECT errors--->"Cannot specialize behavior" at "B1"
	// XPECT warnings ---> "Duplicate of inherited member name 'self' from Object, Performance" at "struct S specializes B1;"
	struct S specializes B1;

	// XPECT errors--->"Cannot specialize structure" at "S"
	// XPECT warnings ---> "Duplicate of inherited member name 'self' from Object, Performance" at "behavior B1 specializes S;"
	behavior B1 specializes S;
}

````
