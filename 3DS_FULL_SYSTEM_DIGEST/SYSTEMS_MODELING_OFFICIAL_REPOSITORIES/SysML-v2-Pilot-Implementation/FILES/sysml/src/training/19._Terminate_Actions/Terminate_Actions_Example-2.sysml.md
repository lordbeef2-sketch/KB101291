# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/19. Terminate Actions/Terminate Actions Example-2.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/19. Terminate Actions/Terminate Actions Example-2.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/19. Terminate Actions/Terminate Actions Example-2.sysml
- source_bytes: 343
- source_sha256: `454fd7804319cea7390c5e6e49a4f94419da1848bfe0b69012ba3c42a52cf969`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Terminate Actions Example-2' {
	action def WorkflowProcess;
	
	part def Processor {
		ref action workflowProcess : WorkflowProcess;
		
		action internalProcess {
			// ...
		}
	}
		
	action terminateProcessing {
		in processor : Processor;
		
		terminate processor.workflowProcess;
				
		terminate processor;
	}

}
````
