# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyPackageAlias1.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyPackageAlias1.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyPackageAlias1.kerml
- source_bytes: 182
- source_sha256: `470271548b3c9d7acc81394d25950df1dbeefe2addc23a2d9c368aab84e01405`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package PackageAlias1{
	alias A_alias for A;
	class A{
		class a{}
			alias a_alias for a;
	}
	alias AA_alias for AA;
	class AA{
		class aa{}
		alias aa_alias for aa;
	}
}
````
