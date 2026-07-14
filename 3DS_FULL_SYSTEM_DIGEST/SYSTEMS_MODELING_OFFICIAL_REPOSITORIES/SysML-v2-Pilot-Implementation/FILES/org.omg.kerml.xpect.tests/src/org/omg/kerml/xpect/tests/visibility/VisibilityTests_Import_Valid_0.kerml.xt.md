# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Valid_0.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Valid_0.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Valid_0.kerml.xt
- source_bytes: 1840
- source_sha256: `c1324208cc29686ca5a9b188494e6b85386bb072c1ac8fa438fa57aff4e1e671`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.visibility.KerMLVisibilityTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencyVisibilityPackage.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencyVisibilityPackage.kerml"}
			}
		}
	}
END_SETUP 
*/

//XPECT noErrors ---> ""
package Test3{
	public import VisibilityPackage::*;
	
	classifier A specializes c_Public{
		classifier AA specializes c_public{}
 		classifier BB specializes A::c_public{}
 		classifier CC specializes Test3::A::c_public{}
	}
	classifier B specializes c_Public::c_public{}
	
	classifier C specializes c_Public_alias{
		classifier AA specializes c_public{}
  		classifier BB specializes alias_public{}
  		classifier CC specializes C::c_public{}
  		classifier DD specializes Test3::C::c_public{}
  		classifier EE specializes C::alias_public{}
  		classifier FF specializes Test3::C::alias_public{}
	}
	classifier D specializes c_Public_alias::c_public{}
	classifier E specializes c_Public_alias::alias_public{}
	
	classifier F specializes c_clazz{
		classifier AA specializes c_Public{
			classifier AAA specializes c_publicc{}
			classifier BBB specializes AA::c_publicc{}
			classifier CCC specializes F::AA::c_publicc{}
			classifier DDD specializes Test3::F::AA::c_publicc{}
		}
		classifier BB specializes c_Public::c_publicc{}
		classifier CC specializes F::c_Public{}
		classifier DD specializes F::c_Public{}
		classifier EE specializes F::c_Public::c_publicc{}
		classifier FF specializes Test3::F::c_Public{}
		classifier GG specializes Test3::F::c_Public::c_publicc{}
	}
	classifier G specializes c_clazz::c_Public{
		classifier AA specializes c_publicc{}
	}	
}

````
