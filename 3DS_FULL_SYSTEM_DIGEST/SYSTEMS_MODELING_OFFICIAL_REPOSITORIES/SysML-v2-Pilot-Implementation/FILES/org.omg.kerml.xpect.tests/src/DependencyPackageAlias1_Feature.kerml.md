# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyPackageAlias1_Feature.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyPackageAlias1_Feature.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyPackageAlias1_Feature.kerml
- source_bytes: 189
- source_sha256: `7d4bb4c0ea7a28a87259c8a76891be28319d3a675b1aa3b4353824ace819a60f`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package PackageAlias1{
	alias A_alias for A;
	feature A{
		feature a{}
		alias a_alias for a;
	}
	alias AA_alias for AA;
	feature AA{
		feature aa{}
		alias aa_alias for aa;
	}
}
````
