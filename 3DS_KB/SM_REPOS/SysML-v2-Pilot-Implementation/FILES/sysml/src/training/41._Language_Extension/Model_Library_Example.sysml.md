# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/41. Language Extension/Model Library Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/41. Language Extension/Model Library Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/41. Language Extension/Model Library Example.sysml
- source_bytes: 901
- source_sha256: `7367c07e4296c59c144caf96022206ab6051dc3bf2dcb615d4ffd72ad898e6f1`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
library package 'Model Library Example' {
	private import ScalarValues::Real;
	private import RiskMetadata::Level;
	
	abstract occurrence def Situation;
	
	abstract occurrence situations : Situation[*] nonunique;
	
	abstract occurrence def Cause {
		attribute probability : Real;
	}
	
	abstract occurrence causes : Cause[*] nonunique :> situations;
	
	abstract occurrence def Failure {
		attribute severity : Level;
	}
	
	abstract occurrence failures : Failure[*] nonunique :> situations;
	
	abstract connection def Causation :> Occurrences::HappensBefore {
		end [*] ref cause : Situation;
		end [*] ref effect : Situation;
	}
	
	abstract connection causations : Causation[*] nonunique;
	
	item def Scenario {
		occurrence :>> situations;
		occurrence :>> causes :> situations;
		occurrence :>> failures :> situations;
	}
	
	item scenarios : Scenario[*] nonunique;
}
````
