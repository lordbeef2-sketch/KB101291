# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyMultipleImport_Feature_FT.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyMultipleImport_Feature_FT.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyMultipleImport_Feature_FT.kerml
- source_bytes: 93
- source_sha256: `d2f43c6c05fa9f44d9deaa9b81e52444d7a5dce5e84ab1a37ce7d3d77aaf2081`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package OuterPackage2{
	public import OuterPackage::*;
	feature C : B{
		feature c;
	}
}
````
