# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyOuterPackage_Feature_FT.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyOuterPackage_Feature_FT.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyOuterPackage_Feature_FT.kerml
- source_bytes: 92
- source_sha256: `db0920b95191af1dd0d6c26c250ce438cade270d6aad12de8f0669fa5566d4f2`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package OuterPackage{
	feature A{
		feature a1{}
	}
	feature B{
		feature b : A;
	}
}
````
