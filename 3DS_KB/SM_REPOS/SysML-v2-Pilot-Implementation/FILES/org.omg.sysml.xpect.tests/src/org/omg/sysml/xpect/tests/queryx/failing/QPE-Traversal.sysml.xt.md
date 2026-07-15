# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/queryx/failing/QPE-Traversal.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/queryx/failing/QPE-Traversal.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/queryx/failing/QPE-Traversal.sysml.xt
- source_bytes: 1415
- source_sha256: `04c1102a41fd8b545437d1bf30b1afcfdeb4368081c644b77da95aa912df67e8`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* XPECT_SETUP org.omg.sysml.xpect.tests.query.failing.SysMLQueryFailingTest
        ResourceSet {
                ThisFile {}
                File {from ="/library.kernel/Base.kerml"}
                File {from ="/library.kernel/Objects.kerml"}
                File {from ="/library.kernel/Performances.kerml"}
                File {from ="/library.kernel/ScalarValues.kerml"}
                File {from ="/library.kernel/ControlFunctions.kerml"}
                File {from ="/src/Vehicle.sysml"}
        }
        Workspace {
                JavaProject {
                        SrcFolder {
                                ThisFile {}
                                File {from ="/library.kernel/Base.kerml"}
                				File {from ="/library.kernel/Objects.kerml"}
                				File {from ="/library.kernel/Performances.kerml"}
                                File {from ="/library.kernel/ScalarValues.kerml"}
                				File {from ="/library.kernel/ControlFunctions.kerml"}
                                File {from ="/src/Vehicle.sysml"}
                        }
                }
        }
END_SETUP
*/

// XPECT noErrors ---> ""
package P {
    public import ScalarValues::*;
    public import Vehicle::*;

    value v_redefining: Integer = ./vehicle_1/cylinders/@redefining;

    value v_redefined: Integer = ./Vehicle::cylinders/@redefined;
}

````
