# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/25. Transitions/Local Clock Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/25. Transitions/Local Clock Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/25. Transitions/Local Clock Example.sysml
- source_bytes: 617
- source_sha256: `c010674ec7a231f4e3a5f5e347bb39210decdb975f695d36334bdf9196166531`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Local Clock Example' {
	private import ScalarValues::String;
	
	item def Start;
	item def Request;
	
	part def Server {
		part :>> localClock = new Time::Clock();

		attribute today : String;
				
		port requestPort;
		
		state ServerBehavior {
			first start then off;
			
			state off;
			accept Start via requestPort
				then waiting;
			
			state waiting;
			accept request : Request via requestPort
				then responding;
			accept at new Time::Iso8601DateTime(today + "11:59:00")
				then off;
			
			state responding;
			accept after 5 [SI::min]
				then waiting;
		}
	}
}
````
