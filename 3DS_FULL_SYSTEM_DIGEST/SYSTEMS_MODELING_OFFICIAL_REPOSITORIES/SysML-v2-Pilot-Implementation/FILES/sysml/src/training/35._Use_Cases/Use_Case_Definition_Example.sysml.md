# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/35. Use Cases/Use Case Definition Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/35. Use Cases/Use Case Definition Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/35. Use Cases/Use Case Definition Example.sysml
- source_bytes: 712
- source_sha256: `5c842109c23d6ea04432b63c75aaa13b17fa9be220c78875f06e0f22eb6d944f`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Use Case Definition Example' {
	
	part def Vehicle;
	part def Person;
	part def Environment;
	part def 'Fuel Station';
	
	use case def 'Provide Transportation' {
		subject vehicle : Vehicle;
		
		actor driver : Person;
		actor passengers : Person[0..4];
		actor environment : Environment;
		
		objective {
			doc 
			/* Transport driver and passengers from starting location 
			 * to ending location.
			 */
		}		
	}
	
	use case def 'Enter Vehicle' {
		subject vehicle : Vehicle;
		actor driver : Person;
		actor passengers : Person[0..4];
	}
	
	use case def 'Exit Vehicle' {
		subject vehicle : Vehicle;
		actor driver : Person;
		actor passengers : Person[0..4];
	}
}
````
