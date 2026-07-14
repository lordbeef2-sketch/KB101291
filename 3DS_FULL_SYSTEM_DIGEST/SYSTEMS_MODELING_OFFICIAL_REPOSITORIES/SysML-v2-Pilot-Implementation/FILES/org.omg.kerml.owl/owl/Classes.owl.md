# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.owl/owl/Classes.owl

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.owl/owl/Classes.owl`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.owl/owl/Classes.owl
- source_bytes: 1154
- source_sha256: `fc0a80537754b86dbf0629c16cf92236e58304759bdc552accb2c47e7959891c`
- decoded_as: `utf-8`


## EXACT SOURCE

````xml
Prefix ( : = <http://www.omg.org/SysML/ontology/Classes#> ) 
Ontology ( <http://www.omg.org/SysML/ontology/Classes> 
ObjectPropertyDomain ( :Classes.A.b-Feature :Classes.A-Class ) 
ObjectPropertyDomain ( :Classes.B.x-Feature :Classes.B-Class ) 
ObjectPropertyRange ( :Classes.B.x-Feature :Classes.A-Class ) 
Declaration ( ObjectProperty ( :Classes.B.x-Feature ) ) 
ObjectPropertyRange ( :Classes.A.b-Feature :Classes.B-Class ) 
Declaration ( ObjectProperty ( :Classes.A.b-Feature ) ) 
ObjectPropertyDomain ( :Classes.A.c-Feature :Classes.A-Class ) 
SubClassOf ( :Classes.C-Class :Classes.B-Class ) 
ObjectPropertyDomain ( :Classes.C.y-Feature :Classes.C-Class ) 
SubClassOf ( :Classes.P.D-Class :Classes.C-Class ) 
ObjectPropertyRange ( :Classes.C.y-Feature :Classes.P.D-Class ) 
Declaration ( ObjectProperty ( :Classes.C.y-Feature ) ) 
ObjectPropertyRange ( :Classes.A.c-Feature :Classes.C-Class ) 
Declaration ( ObjectProperty ( :Classes.A.c-Feature ) ) 
Declaration ( Class ( :Classes.A-Class ) ) 
Declaration ( Class ( :Classes.B-Class ) ) 
Declaration ( Class ( :Classes.C-Class ) ) 
Declaration ( Class ( :Classes.P.D-Class ) ) )
````
