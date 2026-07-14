# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/01. Packages/Package Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/01. Packages/Package Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/01. Packages/Package Example.sysml
- source_bytes: 234
- source_sha256: `192bc594b48bd65304ff1b357168da77672b8295c04b29b8a8e8206a163b1c63`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Package Example' {
	public import ISQ::TorqueValue;
	private import ScalarValues::*;
	 
	private part def Automobile;
	
	public alias Car for Automobile;	                         
	alias Torque for ISQ::TorqueValue;
}
````
