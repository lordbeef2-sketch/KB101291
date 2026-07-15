# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Simple Tests/Classifiers.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Simple Tests/Classifiers.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Simple Tests/Classifiers.kerml
- source_bytes: 389
- source_sha256: `a7880ec2c57a9102880e2f8099035f94094b578c623ca1533a3b31d7a42730f8`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Classifiers {
	classifier A;
	classifier B;
	
	specialization Super subclassifier A specializes B;
	specialization subclassifier B :> A;
	
	subclassifier C specializes A;
	subclassifier C specializes B;
	
	classifier C specializes A, B;
	
	classifier D disjoint from C differences A, B;
	classifier E specializes C intersects A, B;
	classifier F unions A unions B;
}
````
