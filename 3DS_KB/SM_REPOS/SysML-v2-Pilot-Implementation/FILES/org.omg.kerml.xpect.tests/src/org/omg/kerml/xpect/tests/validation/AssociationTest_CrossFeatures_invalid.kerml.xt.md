# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/AssociationTest_CrossFeatures_invalid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/AssociationTest_CrossFeatures_invalid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/AssociationTest_CrossFeatures_invalid.kerml.xt
- source_bytes: 1465
- source_sha256: `8e443e6118ff5a530da8cef237afefefb45ddfe632f10b04864c3934cca6eb62`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/library/Links.kerml"}
		File {from ="/library/Occurrences.kerml"}
		File {from ="/library/Objects.kerml"}
		File {from ="/library/Performances.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/library/Links.kerml"}
				File {from ="/library/Occurrences.kerml"}
				File {from ="/library/Objects.kerml"}
				File {from ="/library/Performances.kerml"}
			}
		}
	}
END_SETUP 
*/
package AssociationTest_CrossFeatures_invalid {
	class C1 {
		feature a : C2;
	}
	
	class C2 {
		feature b : C1;
		feature c subsets b;
	}
	
	assoc A1 {
		end x : C1 crosses y.b;
		//* XPECT errors --- 
		   "Cross feature must have same type as feature" at "y.b"
		   "Cross subsetting must chain through an opposite end feature" at "y.b"
		   ---
		*/
		end y : C2 crosses y.b;
	}
	
	assoc A2 specializes A1 {
		end x : C1 crosses y.c;
		// XPECT errors --> "Cross feature must specialized redefined-end cross features" at "x.a"
		end y : C2 crosses x.a;
	}
	
	assoc A3 {
		// XPECT errors --> "Must be the cross feature" at "x1 [0..1]"
		end x1 [0..1] feature x : C1 crosses y.b {
			public import y::y1;
		}
		end feature y : C2 crosses x.y1 {
			member feature y1 [0..1] featured by C1;
		}
	}
}

````
