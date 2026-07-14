# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/01. Packages/Documentation Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/01. Packages/Documentation Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/01. Packages/Documentation Example.sysml
- source_bytes: 320
- source_sha256: `0797900ad98fd6d99c6b5bbc0d1d7d0046b04ffc74039ce91c46143412bc1ca6`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Documentation Example' {
	doc /* This is documentation of the owning 
	     * package.
	     */
	
	part def Automobile {
		doc Document1 /* This documentation of Automobile. */
	}
	
	alias Car for Automobile {
		doc /* This is documentation of the alias. */
	}
	alias Torque for ISQ::TorqueValue;
}
````
