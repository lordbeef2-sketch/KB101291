# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/linking/GlobalQualification.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/linking/GlobalQualification.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/linking/GlobalQualification.kerml.xt
- source_bytes: 874
- source_sha256: `51647f98c356199d2c8f2fedd17e3007e7ae595171148db0a7463d1e2cdd184c`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.linking.KerMLLinkingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/library/Occurrences.kerml"}
		File {from ="/library/Objects.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/library/Occurrences.kerml"}
				File {from ="/library/Objects.kerml"}
			}
		}
	}
END_SETUP 
*/
package Classes2 {
	class A;
}

package Classes1 {
	// XPECT linkedName at A --> Classes2.A
	private class B specializes $::Classes2::A {
		// XPECT linkedName at A --> Classes1.Classes2.A
		private y: Classes2::A;
		// XPECT linkedName at A --> Classes1.$.Classes2.A
		feature x : '$'::Classes2::A; 
	}
	
	package '$' {
		class Classes2 {
			class A;
		}
	}
	
	package Classes2 {
		class A;
	}
}

````
