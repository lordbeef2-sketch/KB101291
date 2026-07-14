# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/queryx/failing/QPE-Wildcard.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/queryx/failing/QPE-Wildcard.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/queryx/failing/QPE-Wildcard.sysml.xt
- source_bytes: 1454
- source_sha256: `ba7115e1827d184f59f60dcad42a4df54736c5ffb77638b285c53fca9cb2d8e7`
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

    // '/*' is prohibited, so we use '.*' or '.**' for wildcards

    value vw_single: Integer[0..*] = .*/cylinders;

    value vw_recursive: Integer[0..*] = .**/cylinders;
}

````
