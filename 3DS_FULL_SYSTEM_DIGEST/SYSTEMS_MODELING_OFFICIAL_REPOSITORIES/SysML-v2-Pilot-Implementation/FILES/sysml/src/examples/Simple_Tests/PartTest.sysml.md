# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Simple Tests/PartTest.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Simple Tests/PartTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Simple Tests/PartTest.sysml
- source_bytes: 957
- source_sha256: `0ac5a9b5f70b5c0fe1efd89dcc5da88a24dcfdd4a90429d81ba2068bae11200f`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package PartTest {
	
	part f: A;

	public part def A {
		part <'1'> b: B;
		protected port c: C;
		constant attribute x[0..2];
		derived constant ref attribute y :> x;
		ref z : ScalarValues::Integer;
	}
	
	item def S;
	
	abstract part def <xx> B {
		public abstract part a: A[1..2];
		public abstract part b subsets a;
		public abstract part c[0..1] subsets a;
		port x: ~C {
		    port p;
		    ref port q;
		}
		package P { }
		
		succession flow x.p to a1.aa.receiver;
		
		action a1 {
			accept S via x;
			action aa accept S;
		}
		perform action a2;
		
		state s1;
		exhibit state s2;
	}
	
	private port def C {
		private in ref y: A, B {
		    part B_b redefines B::b;
		    part B_c redefines B::c;
		    port B_x redefines B::x;
		}
		alias z1 for y;
		alias z2 for y;
		port c1 : C;
		ref port c2 : C;
	}
	
    part p1 :> p2;
    part p2 :> p3; 
    part p3 :> p1;
    
    part p4 :> p4;
	
}
````
