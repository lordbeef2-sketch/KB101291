# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyMultipleMembership_Feature_FT.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyMultipleMembership_Feature_FT.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyMultipleMembership_Feature_FT.kerml
- source_bytes: 93
- source_sha256: `dc29159c8ea17652ee651a7034f2bd03f2dbd9a9c06365c62407a56ff2e6f7db`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package OuterPackage2{
	public import OuterPackage::B;
	feature C : B{
		feature c;
	}
}
````
