# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/Vehicle.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/Vehicle.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/Vehicle.sysml
- source_bytes: 553
- source_sha256: `226c92d6cba8de92fab6464a04f63c0b9c52f03e80b8728070ed5800443f4dfd`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package Vehicle {
    part def Vehicle {
        attribute cylinders: ScalarValues::Integer = 3;
        attribute mass: ScalarValues::Real = 1000.1;
    }

    part vehicle_1 : Vehicle {
        attribute cylinders :>> Vehicle::cylinders = 4;
        attribute mass :>> Vehicle::mass = 1.1;
    }

    part vehicle_1a :> vehicle_1 {
        attribute cylinders :>> vehicle_1::cylinders = 6;
        attribute mass :>> vehicle_1::mass = 2.1;

        part experiment {
            attribute cylinders: Integer = 1;
        }
    }
}

````
