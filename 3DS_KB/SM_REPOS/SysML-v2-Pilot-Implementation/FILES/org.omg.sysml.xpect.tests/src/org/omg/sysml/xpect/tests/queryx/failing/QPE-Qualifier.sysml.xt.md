# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/queryx/failing/QPE-Qualifier.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/queryx/failing/QPE-Qualifier.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/queryx/failing/QPE-Qualifier.sysml.xt
- source_bytes: 1623
- source_sha256: `50acf0437eec61558f9c6f805ca3d4e32476ef828a39c758352531f0c122deaa`
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
                File {from ="/library.kernel/ScalarFunctions.kerml"}
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
                				File {from ="/library.kernel/ScalarFunctions.kerml"}
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

    value v1_i: Integer[0..*] = .*/.*[Integer];

    value v2_r: Real[0..*] = .**[Real];

    value v1_i: Integer[0..*] = .*/.*[Integer| ./ < 3];

    value v1_i: Real[0..*] = .*/mass[./ > 3.0];
}

````
