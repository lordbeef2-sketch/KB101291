# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyPackageAlias2_Feature_Rdef.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyPackageAlias2_Feature_Rdef.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyPackageAlias2_Feature_Rdef.kerml
- source_bytes: 118
- source_sha256: `cefda70e09ec26e6b65e734e39d6a69cf8f3005ce3589ea72645485f3e39b62c`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package PackageAlias2{
	public import PackageAlias1::*;
	feature B redefines A_alias{
		alias b for a_alias;
	}
}
````
