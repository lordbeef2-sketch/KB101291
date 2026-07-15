# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Simple Tests/Classes.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Simple Tests/Classes.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Simple Tests/Classes.kerml
- source_bytes: 569
- source_sha256: `ffb8a13917841c9924cbb1a6105be515ac460a8df1b8bee92bd20454af4504f4`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Classes {
	
	feature f: A;

	public class <'1'> A { 
		feature b: B;
		protected in c: C;
		portion feature p : A;
	}
	
	abstract class <'2'> B {
		public abstract feature a: A {
			composite feature aa: A;
		}
		public composite feature a1: A;
		feature x {
			composite feature a: A {
			    portion feature q : A;
			}
			portion feature q : A;
		}
		package P { }
	}
	
	private struct C specializes Classes::'2' {
		private y: A, '2'[0..*];
		alias z for y;
		composite feature c : C {
			composite feature cc : C;
		}
	}
	
}
````
