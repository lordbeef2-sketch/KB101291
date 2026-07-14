# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Simple Tests/Connectors.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Simple Tests/Connectors.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Simple Tests/Connectors.kerml
- source_bytes: 699
- source_sha256: `368e6ee6200753e84659b229b6a0ff9a998260058c67d69eeef049731a18f84b`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Connectors {
	
	class A {
		feature a : A;
		feature b : A;
		
		connector c1 from a to b;
		abstract connector c2 = c1;
		connector = c2 {
			end feature references a;
			end feature references b;
		}
		
		binding a = b;
		binding ab of a = b;
		binding {
			end feature references a;
			end feature references b;
		}
		binding ab1 : AS of a = b;
		
		succession a then b;
		succession s first a then b;
		succession {
			end feature references a;
			end feature references b;
		}
		succession s1 : AS first a then b;
		
	}
	
	class B {
	    feature a : A; 
	    connector :> a.c1 from a.a to a.b;
	}
	
	assoc struct AS {
		end a;
		end b;
	}
	
	
}
````
