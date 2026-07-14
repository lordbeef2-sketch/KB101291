# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/11. Interfaces/Interface Decomposition Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/11. Interfaces/Interface Decomposition Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/11. Interfaces/Interface Decomposition Example.sysml
- source_bytes: 475
- source_sha256: `b1f8356d72c60d634ea44c8eb97cd59e8417b569f6a82f3b2d5221e96dffc516`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Interface Decomposition Example' {
	
	port def SpigotBank;
	port def Spigot;
	
	port def Faucet;
	port def FaucetInlet;
	
	interface def WaterDelivery {
		end [1] port suppliedBy : SpigotBank {
			port hot : Spigot;
			port cold : Spigot;
		}
		end [1..*] port deliveredTo : Faucet {
			port hot : FaucetInlet;
			port cold : FaucetInlet;
		}
		
		connect suppliedBy.hot to deliveredTo.hot;
		connect suppliedBy.cold to deliveredTo.cold;
	}
	
}
````
