# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyMultipleImport_Feature_Rdef.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyMultipleImport_Feature_Rdef.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyMultipleImport_Feature_Rdef.kerml
- source_bytes: 99
- source_sha256: `47f932413c8359e16323ca71fed57d1e9a255183175f1734e3008c8cfc76f022`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package OuterPackage2{
	public import OuterPackage::*;
	feature C subsets B{
		feature c;
	}
}
````
