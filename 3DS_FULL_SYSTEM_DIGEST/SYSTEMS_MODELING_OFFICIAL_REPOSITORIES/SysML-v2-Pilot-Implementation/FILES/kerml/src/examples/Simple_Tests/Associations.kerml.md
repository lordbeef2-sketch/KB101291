# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Simple Tests/Associations.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Simple Tests/Associations.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Simple Tests/Associations.kerml
- source_bytes: 414
- source_sha256: `7847ecc8040da796396255a14da86644ca5721833508928a7f87918d6dedfd49`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Associations {
    datatype X;
    class Y;
    
	assoc A {
		end x_cross [1..1] feature x : X; 
		end y_cross [1..*] feature y : Y;
	}
	
	assoc B specializes A {
		end x1;
		end [0..*] feature y1 redefines y;
	}
	
	assoc struct C {
		const end [1] feature a;
		const end feature b;
	}
	
	metaclass M;	
	assoc XY {
		end [0..1] feature x : X {
			@M;
		}
		end feature y : Y;
	}
}
````
