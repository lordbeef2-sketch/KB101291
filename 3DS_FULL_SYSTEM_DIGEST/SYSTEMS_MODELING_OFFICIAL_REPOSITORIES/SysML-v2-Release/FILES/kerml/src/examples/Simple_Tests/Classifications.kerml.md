# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Simple Tests/Classifications.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Simple Tests/Classifications.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Simple Tests/Classifications.kerml
- source_bytes: 139
- source_sha256: `f8d9b7bdcf766d6dcb9a960bc79d002e00df5bfb50579ea8c2c4ab94bca93fbd`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Classifications {
	class T;
	x;
	y = x istype T or x hastype z;
	z = (all T)#(3);
	a = x as T;
	b = x meta KerML::Feature;
}
````
