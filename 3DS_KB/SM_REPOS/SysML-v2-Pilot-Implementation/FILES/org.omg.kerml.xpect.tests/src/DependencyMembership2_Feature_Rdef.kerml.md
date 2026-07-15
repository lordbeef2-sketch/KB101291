# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyMembership2_Feature_Rdef.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyMembership2_Feature_Rdef.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyMembership2_Feature_Rdef.kerml
- source_bytes: 112
- source_sha256: `feec2a405a349dce5db66f5e38ba793b19cd8fd2055a0c70eb2a7d93e11126d7`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package OuterPackage3{
	public import OuterPackage2::C;
	feature D subsets C{
		feature f redefines b;
	}
}
````
