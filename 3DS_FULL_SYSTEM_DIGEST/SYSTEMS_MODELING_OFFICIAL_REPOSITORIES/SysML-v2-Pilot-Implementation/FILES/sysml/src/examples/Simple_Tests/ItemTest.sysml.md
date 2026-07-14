# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Simple Tests/ItemTest.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Simple Tests/ItemTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Simple Tests/ItemTest.sysml
- source_bytes: 287
- source_sha256: `70546c6377bd80e51901d16108149245d46110114e0cb837c86a17b17b180439`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package ItemTest {
	
	item f: A;

	public item def A {
		item b: B;
		protected ref part c: C;
	}
	
	abstract item def B {
		public abstract part a: A;
	}
	
	private part def C {
		private in ref y: A, B;
	}
	
	port def P {
		in item a1: A;
		out item a2: A;
	}
	
}
````
