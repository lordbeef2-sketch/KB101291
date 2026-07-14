# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Simple Tests/AliasTest.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Simple Tests/AliasTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Simple Tests/AliasTest.sysml
- source_bytes: 393
- source_sha256: `91ce2ab7419d3e860cd6bacfa597f361833b7f11cb0736790561e50e144195fe`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package AliasTest {
	private import ISQSpaceTime::breadth; // import of an alias
	attribute b :> breadth;
	
    part def P1 {
        port porig1;
        alias po1 for porig1;
    }

    part p1 : P1 {
        port po1 :>> po1;
    }

    part p2 : P1 {
        port pdest;
        alias pd1 for pdest;
    }


    connect p1.po1 to p2.pdest;
	connect p1.po1 to p2.pd1;
}
````
