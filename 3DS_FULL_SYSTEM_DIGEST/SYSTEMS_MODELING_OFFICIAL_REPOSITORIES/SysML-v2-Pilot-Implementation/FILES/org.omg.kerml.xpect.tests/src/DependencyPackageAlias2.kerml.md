# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyPackageAlias2.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyPackageAlias2.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyPackageAlias2.kerml
- source_bytes: 118
- source_sha256: `94d6bb4289b9d3c94d2c7b31989c1b94359742ac638d9f81aca0ff261c327af6`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package PackageAlias2{
	public import PackageAlias1::*;
	class B specializes A_alias{
		alias b for a_alias;
	}
}
````
