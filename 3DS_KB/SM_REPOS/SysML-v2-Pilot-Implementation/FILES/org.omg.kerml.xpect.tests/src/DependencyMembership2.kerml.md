# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyMembership2.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyMembership2.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyMembership2.kerml
- source_bytes: 106
- source_sha256: `a1d5074d0f9363425d0be7cb66578113c249a7225f6749560ccfc4784f51fa05`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package OuterPackage3{
	public import OuterPackage2::C;
	class D specializes C{
		feature f : b;
	}
}
````
