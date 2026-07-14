# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/expression/PathExpressions.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/expression/PathExpressions.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/expression/PathExpressions.sysml.xt
- source_bytes: 2446
- source_sha256: `3f7d1b4deb599dfe926bb33ae51577de3bd2eb63ec88003d0b26151bb29e66bc`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* XPECT_SETUP org.omg.sysml.xpect.tests.expression.SysMLTests
        ResourceSet {
                ThisFile {}
                File {from ="/library.kernel/Base.kerml"}
                File {from ="/library.kernel/Links.kerml"}
                File {from ="/library.kernel/Occurrences.kerml"}
                File {from ="/library.kernel/Objects.kerml"}
                File {from ="/library.kernel/Performances.kerml"}
                File {from ="/library.kernel/ScalarValues.kerml"}
                File {from ="/library.kernel/BaseFunctions.kerml"}
                File {from ="/library.kernel/DataFunctions.kerml"}
                File {from ="/library.kernel/ControlFunctions.kerml"}
                File {from ="/library.systems/Items.sysml"}
                File {from ="/library.systems/Parts.sysml"}
                File {from ="/src/Vehicle.sysml"}
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
                                File {from ="/library.kernel/BaseFunctions.kerml"}
                                File {from ="/library.kernel/DataFunctions.kerml"}
                				File {from ="/library.kernel/ControlFunctions.kerml"}
                				File {from ="/library.systems/Items.sysml"}
                				File {from ="/library.systems/Parts.sysml"}
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

    attribute v1_cylinders: Integer = vehicle_1.cylinders;

    attribute v1_mass: Real = vehicle_1.mass;

    attribute v2_mass: Real = vehicle_1a.mass;
    
    part vehicle4cyl: Vehicle = (vehicle_1, vehicle_1a).{in ref v:Vehicle; v.cylinders == 4};

    part vehicles[*]: Vehicle = (all Vehicle).{in ref v:Vehicle; v.mass > 100};
}

````
