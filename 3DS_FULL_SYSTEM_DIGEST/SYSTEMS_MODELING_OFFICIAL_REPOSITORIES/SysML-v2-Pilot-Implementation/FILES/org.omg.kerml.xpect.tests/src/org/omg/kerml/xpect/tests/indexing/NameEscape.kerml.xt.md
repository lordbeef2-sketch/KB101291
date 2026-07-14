# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/indexing/NameEscape.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/indexing/NameEscape.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/indexing/NameEscape.kerml.xt
- source_bytes: 723
- source_sha256: `e989e5fb4efbc09727d8f5276a1f2d7ae90579f4890395ef349604db737356e6`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* XPECT_SETUP org.omg.kerml.xpect.tests.indexing.KerMLIndexerTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/library/Occurrences.kerml"}
		File {from ="/library/Performances.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/library/Occurrences.kerml"}
				File {from ="/library/Performances.kerml"}
			}
		}
	}
END_SETUP 
*/

//*
XPECT exportedObjects ---
sysml::Feature: NameEscape::..::parameter
sysml::Function: NameEscape::..
sysml::Package: NameEscape
--- */

package NameEscape {
	
	function '..' {
		in parameter: Base::Anything;
		return : Base::Anything;
	}
	
}
````
