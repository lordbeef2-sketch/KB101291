# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyMembership2_Feature_FT.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyMembership2_Feature_FT.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyMembership2_Feature_FT.kerml
- source_bytes: 98
- source_sha256: `423e8f34a4ddba84403571e411457467377958fc45eca2f0ab5434cb328bbbb3`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package OuterPackage3{
	public import OuterPackage2::C;
	feature D : C{
		feature f : b;
	}
}
````
