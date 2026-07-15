# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyMultipleMembership.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyMultipleMembership.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyMultipleMembership.kerml
- source_bytes: 101
- source_sha256: `a551856965e5d69d5fe8f522ed6cff3eb02d54a2164300d18f100152163216a8`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package OuterPackage2{
	public import OuterPackage::B;
	class C specializes B{
		feature c;
	}
}
````
