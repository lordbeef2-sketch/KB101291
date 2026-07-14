# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/19. Terminate Actions/Terminate Actions Example-1.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/19. Terminate Actions/Terminate Actions Example-1.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/19. Terminate Actions/Terminate Actions Example-1.sysml
- source_bytes: 532
- source_sha256: `4a753b35e2ecfcbdd3726c9ebb4c17052bf643f572544bed2a706c0a769dd23f`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Terminate Actions Example-1' {
	private import ScalarValues::Boolean;
	
	action monitorCriticalActivity;
	action criticalActivity;
	action waitForTimeOut;
	
	action def MonitoredActivity {
		first start;

		then fork;
			then performCriticalActivity;
			then waitForTimeOut;
					
		action performCriticalActivity {
			perform monitorCriticalActivity;
			
			perform criticalActivity;
			then terminate;
		}
		then stop;
		
		action waitForTimeOut;
		then stop;
				
		action stop terminate;
	}
}
````
