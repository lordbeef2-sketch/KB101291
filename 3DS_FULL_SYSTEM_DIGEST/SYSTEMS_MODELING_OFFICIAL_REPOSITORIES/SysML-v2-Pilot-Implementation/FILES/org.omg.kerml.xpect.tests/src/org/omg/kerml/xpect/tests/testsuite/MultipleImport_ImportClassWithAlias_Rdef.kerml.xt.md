# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MultipleImport_ImportClassWithAlias_Rdef.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MultipleImport_ImportClassWithAlias_Rdef.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MultipleImport_ImportClassWithAlias_Rdef.kerml.xt
- source_bytes: 1592
- source_sha256: `550264b529f974d105335aa40a4ebe2d7f8ac90d3854f7cd975564ae9075a427`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencyOuterPackage_Feature_Rdef.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencyOuterPackage_Feature_Rdef.kerml"}
			}
		}
	}
END_SETUP 
*/

// XPECT noErrors ---> ""
package test{
	alias aliass for OuterPackage::A;
	//XPECT linkedName at aliass --> OuterPackage.A
	feature C {
		//* XPECT scope at aliass---
           C, C.self, C.that, C.that.self, OuterPackage.A, OuterPackage.A.a1,
           OuterPackage.A.a1.self, OuterPackage.A.a1.that, OuterPackage.A.a1.that.self, OuterPackage.A.self,
           OuterPackage.A.that, OuterPackage.A.that.self, OuterPackage.B, OuterPackage.B.b,
           OuterPackage.B.b.a1, OuterPackage.B.b.a1.self, OuterPackage.B.b.a1.that,
           OuterPackage.B.b.a1.that.self, OuterPackage.B.b.self, OuterPackage.B.b.that, OuterPackage.B.b.that.self,
           OuterPackage.B.self, OuterPackage.B.that, OuterPackage.B.that.self, aliass, aliass.a1,
           aliass.a1.self, aliass.a1.that, aliass.a1.that.self, aliass.self, aliass.that,
           aliass.that.self, self, test.C, test.C.self, test.C.that, test.C.that.self, test.aliass,
           test.aliass.a1, test.aliass.a1.self, test.aliass.a1.that, test.aliass.a1.that.self,
           test.aliass.self, test.aliass.that, test.aliass.that.self, that, that.self
		--- */
		feature c redefines aliass;
	}
}

````
