# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Scope_0.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Scope_0.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Scope_0.kerml.xt
- source_bytes: 4370
- source_sha256: `75eb6fdf034eb87836c5cde3ba4a8355ece56a2b08d611cd0e3d28103d04522e`
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

// XPECT noErrors ---> ""
package Test3{
	public import VisibilityPackage::*;
	//XPECT linkedName at c_clazz --> VisibilityPackage.c_clazz
	//* XPECT scope at c_clazz ---
	   		
			A, A.AA, A.AA.c_publicc, A.c_Public, A.c_Public.c_publicc, 
			B, B.c_public, Test3.B, Test3.B.c_public,
			B.BB, Test3.B.BB,
			Test3.A, Test3.A.AA, Test3.A.AA.c_publicc, Test3.A.c_Public, Test3.A.c_Public.c_publicc,
			Test3.c_Public,Test3.c_Public.c_public, Test3.c_Public_alias, Test3.c_Public_alias.alias_public,
			Test3.c_Public_alias.c_public, Test3.c_clazz, Test3.c_clazz.c_Public, Test3.c_clazz.c_Public.c_publicc, 
			VisibilityPackage.c_Public, VisibilityPackage.c_Public.c_public, 
			VisibilityPackage.c_Public_alias, VisibilityPackage.c_Public_alias.alias_public, VisibilityPackage.c_Public_alias.c_public, 
			VisibilityPackage.c_clazz, VisibilityPackage.c_clazz.c_Public,VisibilityPackage.c_clazz.c_Public.c_publicc, 
			c_Public, c_Public.c_public, 
			c_Public_alias, c_Public_alias.alias_public, c_Public_alias.c_public, 
			c_clazz, c_clazz.c_Public, c_clazz.c_Public.c_publicc
	--- */
	classifier A specializes c_clazz{
		//XPECT linkedName at c_Public --> VisibilityPackage.c_clazz.c_Public
		//* XPECT scope at c_Public ---
		    AA, AA.c_publicc, c_Public.c_publicc,  
		    A, A.AA, A.AA.c_publicc, A.c_Public, A.c_Public.c_publicc,
		    B, B.c_public, Test3.B, Test3.B.c_public,
		    B.BB, Test3.B.BB,
			Test3.A, Test3.A.AA, Test3.A.AA.c_publicc, Test3.A.c_Public, Test3.A.c_Public.c_publicc,
			Test3.c_Public,Test3.c_Public.c_public, Test3.c_Public_alias, Test3.c_Public_alias.alias_public,
			Test3.c_Public_alias.c_public, Test3.c_clazz, Test3.c_clazz.c_Public, Test3.c_clazz.c_Public.c_publicc, 
			VisibilityPackage.c_Public, VisibilityPackage.c_Public.c_public, 
			VisibilityPackage.c_Public_alias, VisibilityPackage.c_Public_alias.alias_public, VisibilityPackage.c_Public_alias.c_public, 
			VisibilityPackage.c_clazz, VisibilityPackage.c_clazz.c_Public,VisibilityPackage.c_clazz.c_Public.c_publicc, 
			c_Public,  
			c_Public_alias, c_Public_alias.alias_public, c_Public_alias.c_public, 
			c_clazz, c_clazz.c_Public, c_clazz.c_Public.c_publicc,
			c_Protect,
			c_Protect.c_publicc,
		--- */
		// The following are not visible, because qualified names currently require public visibility:
		//  A.c_Protect, A.c_Protect.c_publicc, 
		//  Test3.A.c_Protect, Test3.A.c_Protect.c_publicc, Test3.c_clazz.c_Protect, Test3.c_clazz.c_Protect.c_publicc, 
		//  c_clazz.c_Protect, c_clazz.c_Protect.c_publicc
		//
		classifier AA specializes c_Public{}
	}
	//XPECT linkedName at c_Public --> VisibilityPackage.c_Public
	
	classifier B specializes c_Public{
		//* XPECT scope at c_public ---
		    BB,  c_Public.c_public, c_public,
		    A, A.AA, A.AA.c_publicc, A.c_Public, A.c_Public.c_publicc,
		    B, B.c_public, Test3.B, Test3.B.c_public,
		    B.BB, Test3.B.BB, 
			Test3.A, Test3.A.AA, Test3.A.AA.c_publicc, Test3.A.c_Public, Test3.A.c_Public.c_publicc,
			Test3.c_Public,Test3.c_Public.c_public, Test3.c_Public_alias, Test3.c_Public_alias.alias_public,
			Test3.c_Public_alias.c_public, Test3.c_clazz, Test3.c_clazz.c_Public, Test3.c_clazz.c_Public.c_publicc, 
			VisibilityPackage.c_Public, VisibilityPackage.c_Public.c_public, 
			VisibilityPackage.c_Public_alias, VisibilityPackage.c_Public_alias.alias_public, VisibilityPackage.c_Public_alias.c_public, 
			VisibilityPackage.c_clazz, VisibilityPackage.c_clazz.c_Public,VisibilityPackage.c_clazz.c_Public.c_publicc, 
			c_Public,  
			c_Public_alias, c_Public_alias.alias_public, c_Public_alias.c_public, 
			c_clazz, c_clazz.c_Public, c_clazz.c_Public.c_publicc,
			c_protected
		--- */
		// The following are not visible, because qualified names currently require public visibility:
		//  B.c_protected, Test3.B.c_protected, Test3.c_Public.c_protected, c_Public.c_protected
		classifier BB specializes c_public{}
		
	}
}

````
