# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyPackageAlias2_Feature_FT.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyPackageAlias2_Feature_FT.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyPackageAlias2_Feature_FT.kerml
- source_bytes: 110
- source_sha256: `a218a12f0688d1c98d91498d1d38338bce1558fecb51e803ed26416ba1e851a7`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package PackageAlias2{
	public import PackageAlias1::*;
	feature B : A_alias{
		alias b for a_alias;
	}
}
````
