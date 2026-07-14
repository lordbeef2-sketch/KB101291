# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyOuterPackage_Feature_Rdef.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyOuterPackage_Feature_Rdef.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyOuterPackage_Feature_Rdef.kerml
- source_bytes: 100
- source_sha256: `0edb372fbbeff485be0a388dca3a1e1fbf5a0ca578813e1156678393373a4e09`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package OuterPackage{
	feature A{
		feature a1{}
	}
	feature B{
		feature b redefines A;
	}
}
````
