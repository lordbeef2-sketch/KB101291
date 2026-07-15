# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/PartTest.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/PartTest.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/PartTest.sysml.xt
- source_bytes: 1698
- source_sha256: `cb626562e75a51215108887e97a749e4b4a52fef39067e6959c963f464b48926`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.sysml.xpect.tests.simpletests.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
       	File {from ="/library.kernel/Occurrences.kerml"}
       	File {from ="/library.kernel/Objects.kerml"}
       	File {from ="/library.systems/Attributes.sysml"}
 		File {from ="/library.systems/Items.sysml"}
 		File {from ="/library.systems/Parts.sysml"}
 		File {from ="/library.systems/Ports.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
		       	File {from ="/library.kernel/Occurrences.kerml"}
		       	File {from ="/library.kernel/Objects.kerml"}
		       	File {from ="/library.systems/Attributes.sysml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
 				File {from ="/library.systems/Ports.sysml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package PartTest {
	
	part f: A;

	public part def A {
		part <'1'> b: B;
		protected port c: C;
		constant attribute x;
		derived constant ref attribute y :> x;
		ref z;
	}
	
	item def S;
	
	abstract part def <xx> B {
		public abstract part a: A;
		public abstract part b subsets a;
		public abstract part c subsets a;
		port x: ~C {
		    port p;
		    ref port q;
		}
		package P { }
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
