# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/35. Use Cases/Use Case Usage Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/35. Use Cases/Use Case Usage Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/35. Use Cases/Use Case Usage Example.sysml
- source_bytes: 1104
- source_sha256: `a3cbe81d5d72920e91501db8eed4e5a2ccaeee892c32fd4286f10fd85a116c9f`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Use Case Usage Example' {
	
	private import 'Use Case Definition Example'::*;
	
	part def 'Fuel Station';
	
	use case 'provide transportation' : 'Provide Transportation' {
	    subject vehicle;
	    	
		first start;
		
		then include use case 'enter vehicle' : 'Enter Vehicle' {
		    subject vehicle;
			actor driver = 'provide transportation'::driver;
			actor passengers = 'provide transportation'::passengers;
		}
		
		then use case 'drive vehicle' {
            subject vehicle;
			actor driver = 'provide transportation'::driver;
			actor environment = 'provide transportation'::environment;
			
			include 'add fuel'[0..*] { 
                subject vehicle;
				actor fueler = driver;
			}
		}
		
		then include use case 'exit vehicle' : 'Exit Vehicle' {
            subject vehicle;
			actor driver = 'provide transportation'::driver;
			actor passengers = 'provide transportation'::passengers;
		}
		
		then done;		
	}
	
	use case 'add fuel' {
		subject vehicle : Vehicle;
		actor fueler : Person;
		actor 'fuel station' : 'Fuel Station';
	}
}
````
