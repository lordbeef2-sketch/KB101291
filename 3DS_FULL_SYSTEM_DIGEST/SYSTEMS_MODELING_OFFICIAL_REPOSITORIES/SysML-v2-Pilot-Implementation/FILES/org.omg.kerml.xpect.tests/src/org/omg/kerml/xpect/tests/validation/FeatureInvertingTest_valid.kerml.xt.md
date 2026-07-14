# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/FeatureInvertingTest_valid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/FeatureInvertingTest_valid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/FeatureInvertingTest_valid.kerml.xt
- source_bytes: 1010
- source_sha256: `afc8823d516f75bc23aeb506634a4b1f6699b4112aa7fbd8aa0e9383bf0074f7`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* XPECT_SETUP org.omg.kerml.xpect.tests.validation.KerMLValidationTest
        ResourceSet {
                ThisFile {}
                File {from ="/library/Base.kerml"}
                File {from ="/library/Occurrences.kerml"}
                File {from ="/library/Objects.kerml"}

        }
        Workspace {
                JavaProject {
                        SrcFolder {
                                ThisFile {}
                                File {from ="/library/Base.kerml"}
                                File {from ="/library/Occurrences.kerml"}
                 				File {from ="/library/Objects.kerml"}

                        }
                }
        }
END_SETUP
*/

// XPECT noErrors ---> ""
package Inverses {
	class A {
		feature f : B inverse of B::g disjoint from h;
		feature h : B;
	}
	
	class B {
		feature g : A;
	}
	
	inverse B::g of A::f;
	inverting Invert inverse B::g.f of A::h;
	
	feature gg : A featured by B inverse of A::f;
}

````
