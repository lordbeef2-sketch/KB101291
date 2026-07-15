# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/expression/SimpleArithmeticExpression.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/expression/SimpleArithmeticExpression.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/expression/SimpleArithmeticExpression.sysml.xt
- source_bytes: 1714
- source_sha256: `b6797a3fbd5d01a1c8750503d95f6c47c8e5d33d6580a0478868e28b7d31facc`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.sysml.xpect.tests.expression.SysMLTests
       ResourceSet {
            ThisFile {}
            File {from ="/library.kernel/Base.kerml"}
            File {from ="/library.kernel/Links.kerml"}
            File {from ="/library.kernel/Occurrences.kerml"}
            File {from ="/library.kernel/Objects.kerml"}
            File {from ="/library.kernel/Performances.kerml"}
            File {from ="/library.kernel/ScalarValues.kerml"}
            File {from ="/library.kernel/DataFunctions.kerml"}
            File {from ="/library.kernel/ScalarFunctions.kerml"}
            File {from ="/library.systems/Items.sysml"}
            File {from ="/library.systems/Parts.sysml"}
        }
        Workspace {
            JavaProject {
                SrcFolder {
                    ThisFile {}
			            File {from ="/library.kernel/Base.kerml"}
			            File {from ="/library.kernel/Links.kerml"}
			            File {from ="/library.kernel/Occurrences.kerml"}
			            File {from ="/library.kernel/Objects.kerml"}
			            File {from ="/library.kernel/Performances.kerml"}
			            File {from ="/library.kernel/ScalarValues.kerml"}
			            File {from ="/library.kernel/DataFunctions.kerml"}
			            File {from ="/library.kernel/ScalarFunctions.kerml"}
			            File {from ="/library.systems/Items.sysml"}
			            File {from ="/library.systems/Parts.sysml"}
                }
            }
        }
END_SETUP
*/
// XPECT noErrors ---> ""
package P {
    part def Vehicle {
        public import ScalarValues::*;
        attribute a: Integer = 5;
        attribute b: Integer = 5 * a;
    }
}

````
