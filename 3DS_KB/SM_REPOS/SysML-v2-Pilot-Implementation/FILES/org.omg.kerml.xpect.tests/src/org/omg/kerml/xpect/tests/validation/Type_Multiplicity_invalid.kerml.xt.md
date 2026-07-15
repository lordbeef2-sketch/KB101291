# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Type_Multiplicity_invalid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Type_Multiplicity_invalid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Type_Multiplicity_invalid.kerml.xt
- source_bytes: 704
- source_sha256: `d384047752ed6601c6da16188bd023b91c3adb67237735c9b46ef8db08ef29f0`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* XPECT_SETUP org.omg.kerml.xpect.tests.validation.KerMLValidationTest
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
package Type_Multiplicity {
	classifier C {
		multiplicity subsets Base::zeroOrOne;
		
		// XPECT errors--->"Only one multiplicity is allowed" at "multiplicity subsets Base::zeroToMany;"
		multiplicity subsets Base::zeroToMany;
	}
}

````
