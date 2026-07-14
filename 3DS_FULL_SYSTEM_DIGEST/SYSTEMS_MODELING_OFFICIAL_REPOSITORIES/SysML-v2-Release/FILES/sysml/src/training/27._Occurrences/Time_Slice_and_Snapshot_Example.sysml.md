# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/27. Occurrences/Time Slice and Snapshot Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/27. Occurrences/Time Slice and Snapshot Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/27. Occurrences/Time Slice and Snapshot Example.sysml
- source_bytes: 468
- source_sha256: `01103847bb6aba185350c5111b0984ac30a40d2e76b22c08a7d5ea0afc5e6617`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Time Slice and Snapshot Example' {
		
	attribute def Date;
	item def Person;
	
	part def Vehicle {
		timeslice assembly;
		
		first assembly then delivery;
		
		snapshot delivery {
			attribute deliveryDate : Date;
		}
		
		then timeslice ownership[0..*] ordered {
			snapshot sale = start;
			
			ref item owner : Person[1];
			
			timeslice driven[0..*] {
				ref item driver : Person[1];
			}
		}
		
		snapshot junked = done;
	}
}
````
