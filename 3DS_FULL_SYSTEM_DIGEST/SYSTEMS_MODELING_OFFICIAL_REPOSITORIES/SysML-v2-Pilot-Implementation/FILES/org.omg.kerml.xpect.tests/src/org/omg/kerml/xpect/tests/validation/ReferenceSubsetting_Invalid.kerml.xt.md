# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ReferenceSubsetting_Invalid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ReferenceSubsetting_Invalid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ReferenceSubsetting_Invalid.kerml.xt
- source_bytes: 827
- source_sha256: `4f08c0b767dd077d7df7e4e30c4a5d8b202143b36311572abd2ecfe9a93514ba`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
       	File {from ="/library/Links.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
		       	File {from ="/library/Links.kerml"}
			}
		}
	}
END_SETUP 
*/
package ReferenceSubsetting_invalid {
	feature a;
	feature b references a;
	feature c references a subsets b;
	//XPECT errors --> "At most one reference subsetting is allowed" at "c"
	feature d references b references c;
	
	connector cc {
		end x ::> a;
		//*XPECT errors --- 
		   "At most one reference subsetting is allowed" at "c"
		   "At most one reference subsetting is allowed" at "d"
		   ---
		  */
		end y ::> b ::> c ::> d;
	}
}

````
