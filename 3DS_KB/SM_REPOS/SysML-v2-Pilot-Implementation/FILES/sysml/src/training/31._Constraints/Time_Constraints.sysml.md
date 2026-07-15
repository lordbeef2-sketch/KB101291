# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/31. Constraints/Time Constraints.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/31. Constraints/Time Constraints.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/31. Constraints/Time Constraints.sysml
- source_bytes: 1013
- source_sha256: `3b0eab37f4358624ddb4b013aa58e01a3bfbe7466887439a1ef7a8a9374a77af`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Time Constraints' {
	private import ISQ::TemperatureValue;
	private import ISQ::DurationValue;
	private import Time::TimeInstantValue;
	private import Time::TimeOf;
	private import Time::DurationOf;
	private import SI::h;
	private import SI::s;

	attribute def MaintenanceDone;
	
	part def Vehicle {
		attribute maintenanceTime : TimeInstantValue;
		attribute maintenanceInterval : DurationValue;
		attribute maxTemperature : TemperatureValue;
	}
	
	state healthStates {
		in vehicle : Vehicle;
		
		entry; then normal;
		
		state normal;
		accept at vehicle.maintenanceTime
			then maintenance;
		
		state maintenance {
			assert constraint { TimeOf(maintenance) > vehicle.maintenanceTime }
			assert constraint { TimeOf(maintenance) - TimeOf(normal.done) < 2 [s] }
			entry assign vehicle.maintenanceTime := vehicle.maintenanceTime + vehicle.maintenanceInterval;
		}
		accept MaintenanceDone
			then normal;
		
		constraint { DurationOf(maintenance) <= 48 [h] }
	}
}
````
