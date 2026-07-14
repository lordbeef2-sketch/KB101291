# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyMultipleImport.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyMultipleImport.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyMultipleImport.kerml
- source_bytes: 101
- source_sha256: `73849f633268506fa3326ef91471bf2bceb87213a445f6106c93a34faf2a0638`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package OuterPackage2{
	public import OuterPackage::*;
	class C specializes B{
		feature c;
	}
}
````
