# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Simple Tests/AllocationTest.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Simple Tests/AllocationTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Simple Tests/AllocationTest.sysml
- source_bytes: 663
- source_sha256: `dadd0da31a3b5657fdfcd68ed767c541253dd457b7605f4f6484dbdc33e6eda7`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package AllocationTest {
	part def Logical {
		part component;
	}
	
	part def Physical {
		part assembly {
			part element;
		}
	}
	
	part l : Logical {
		part :>> component;
	}
	part p : Physical {
		part :>> assembly {
			part :>> element;
		}
        allocate l.component to assembly.element;
	}
	
	allocation def A;
	
	allocation def Logical_to_Physical :> A {
		end logical : Logical;
		end physical : Physical;
	}
	
	allocation allocation1 : Logical_to_Physical allocate l to p;	
	allocation allocation2 : Logical_to_Physical allocate (
		logical ::> l,
		physical ::> p
	);

	allocate l.component to p.assembly.element;
}
````
