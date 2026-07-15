# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyOuterPackage.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyOuterPackage.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyOuterPackage.kerml
- source_bytes: 85
- source_sha256: `1b0053fd44a8b336d1abe538419d82a1e65e664a8f255db8b18b6ce0e641ac73`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package OuterPackage{
	class A{
		class a1{}
	}
	class B{
		feature b: A;
	}
}
````
