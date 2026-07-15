# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyMultipleMembership_Feature_Rdef.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyMultipleMembership_Feature_Rdef.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyMultipleMembership_Feature_Rdef.kerml
- source_bytes: 99
- source_sha256: `597c156bbecb3db3ad0c42cbd2ae337e958b7f51a9835ec7c23bcbf168393fb6`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package OuterPackage2{
	public import OuterPackage::B;
	feature C subsets B{
		feature c;
	}
}
````
