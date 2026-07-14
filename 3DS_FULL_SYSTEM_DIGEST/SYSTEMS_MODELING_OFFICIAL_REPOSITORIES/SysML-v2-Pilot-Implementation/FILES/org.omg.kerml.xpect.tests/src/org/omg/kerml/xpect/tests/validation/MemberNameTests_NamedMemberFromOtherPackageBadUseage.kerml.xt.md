# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/MemberNameTests_NamedMemberFromOtherPackageBadUseage.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/MemberNameTests_NamedMemberFromOtherPackageBadUseage.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/MemberNameTests_NamedMemberFromOtherPackageBadUseage.kerml.xt
- source_bytes: 475
- source_sha256: `1416aef6dfdfcba1471481cb85ccb4f11316ce9a6d052410081e6f656c04fa35`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
			}
		}
	}
END_SETUP 
*/

package test{
	package P{
		classifier A {}
		alias A_alias for A;
	}
	// XPECT errors --> "Couldn't resolve reference to Type 'P1::A_alias'." at "P1::A_alias"
	feature a: P1::A_alias;
}

````
