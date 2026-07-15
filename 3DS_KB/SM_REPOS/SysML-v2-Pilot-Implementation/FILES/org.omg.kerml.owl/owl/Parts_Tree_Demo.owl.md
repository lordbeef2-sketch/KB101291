# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.owl/owl/Parts Tree Demo.owl

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.owl/owl/Parts Tree Demo.owl`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.owl/owl/Parts Tree Demo.owl
- source_bytes: 15151
- source_sha256: `7c7ee650c2849d0ceef4a3cf5215e354a80059dfb3184c78aa82d073b2951e91`
- decoded_as: `utf-8`


## EXACT SOURCE

````xml
Prefix ( : = <http://www.omg.org/SysML/ontology/'Parts Tree Demo'#> ) 
Ontology ( <http://www.omg.org/SysML/ontology/'Parts Tree Demo'> 

Declaration ( Class ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.Vehicle-Class ) )

Declaration ( ObjectProperty ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.Vehicle.mass-Feature ) ) 
ObjectPropertyDomain ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.Vehicle.mass-Feature :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.Vehicle-Class ) 
EquivalentClasses ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.Vehicle-Class ObjectMinCardinality 
	( 1 :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.Vehicle.mass-Feature ) ) 
EquivalentClasses ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.Vehicle-Class ObjectMaxCardinality 
	( 1 :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.Vehicle.mass-Feature ) ) 

Declaration ( Class ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.AxleAssembly-Class ) ) 
Declaration ( Class ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.Axle-Class ) ) 
Declaration ( Class ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.Wheel-Class ) )
 
Declaration ( ObjectProperty ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1-Feature ) ) 
ObjectPropertyRange ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1-Feature :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.Vehicle-Class )
 
Declaration ( ObjectProperty ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ) ) 
ObjectPropertyDomain ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1-Feature ) 
EquivalentClasses ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1-Feature ObjectMinCardinality 
	( 1 :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ) ) 
EquivalentClasses ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1-Feature ObjectMaxCardinality 
	( 1 :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ) ) 
ObjectPropertyRange ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.AxleAssembly-Class ) 

Declaration ( ObjectProperty ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontAxle-Feature ) ) 
ObjectPropertyDomain ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontAxle-Feature :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ) 
EquivalentClasses ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ObjectMinCardinality 
	( 1:'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontAxle-Feature ) ) 
EquivalentClasses ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ObjectMaxCardinality 
	( 1:'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontAxle-Feature ) ) 
ObjectPropertyRange ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontAxle-Feature :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.Axle-Class ) 

Declaration ( ObjectProperty ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontWheel-Feature ) ) 
ObjectPropertyDomain ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontWheel-Feature :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ) 
EquivalentClasses ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ObjectMinCardinality 
	( 2 :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontWheel-Feature ) ) 
EquivalentClasses ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ObjectMaxCardinality 
	( 2 :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontWheel-Feature ) ) 
ObjectPropertyRange ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontWheel-Feature :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.Wheel-Class ) 

Declaration ( ObjectProperty ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ) ) 
ObjectPropertyDomain ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1-Feature ) 
EquivalentClasses ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1-Feature ObjectMinCardinality 
	( 1:'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ) ) 
EquivalentClasses ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1-Feature ObjectMaxCardinality 
	( 1:'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ) ) 
ObjectPropertyRange ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.AxleAssembly-Class ) 

Declaration ( ObjectProperty ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearAxle-Feature ) ) 
ObjectPropertyDomain ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearAxle-Feature :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ) 
EquivalentClasses ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ObjectMinCardinality 
	( 1:'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearAxle-Feature ) ) 
EquivalentClasses ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ObjectMaxCardinality 
	( 1:'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearAxle-Feature ) ) 
ObjectPropertyRange ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearAxle-Feature :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.Axle-Class ) 

Declaration ( ObjectProperty ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearWheel-Feature ) ) 
ObjectPropertyDomain ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearWheel-Feature :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ) 
EquivalentClasses ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ObjectMinCardinality 
	( 2 :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearWheel-Feature ) ) 
EquivalentClasses ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ObjectMaxCardinality 
	( 2 :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearWheel-Feature ) ) 
ObjectPropertyRange ( :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearWheel-Feature :'Parts Tree Demo'.'Create Generic Hierarchical Structure'.Wheel-Class ) 

Declaration ( Class ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.FrontAxle-Class ) ) 
Declaration ( Class ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.RearAxle-Class ) ) 

Declaration ( ObjectProperty ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1-Feature ) ) 

Declaration ( ObjectProperty ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ) ) 
ObjectPropertyDomain ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1-Feature ) 
EquivalentClasses ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1-Feature ObjectMinCardinality 
	( 1:'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ) ) 
EquivalentClasses ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1-Feature ObjectMaxCardinality 
	( 1:'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ) ) 

Declaration ( ObjectProperty ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontAxle-Feature ) ) 
ObjectPropertyDomain ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontAxle-Feature :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ) 
EquivalentClasses ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ObjectMinCardinality 
	( 1:'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontAxle-Feature ) ) 
EquivalentClasses ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ObjectMaxCardinality 
	( 1:'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontAxle-Feature ) ) 
ObjectPropertyRange ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontAxle-Feature :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.FrontAxle-Class ) 

Declaration ( ObjectProperty ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontWheel_1-Feature ) ) 
ObjectPropertyDomain ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontWheel_1-Feature :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ) 
EquivalentClasses ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ObjectMinCardinality 
	( 1:'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontWheel_1-Feature ) ) 
EquivalentClasses ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ObjectMaxCardinality 
	( 1:'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontWheel_1-Feature ) ) 

Declaration ( ObjectProperty ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontWheel_2-Feature ) ) 
ObjectPropertyDomain ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontWheel_2-Feature :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ) 
EquivalentClasses ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ObjectMinCardinality 
	( 1:'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontWheel_2-Feature ) ) 
EquivalentClasses ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly-Feature ObjectMaxCardinality 
	( 1:'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.frontAxleAssembly.frontWheel_2-Feature ) ) 

Declaration ( ObjectProperty ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ) ) 
ObjectPropertyDomain ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1-Feature ) 
EquivalentClasses ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1-Feature ObjectMinCardinality 
	( 1:'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ) ) 
EquivalentClasses ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1-Feature ObjectMaxCardinality 
	( 1:'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ) ) 

Declaration ( ObjectProperty ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearAxle-Feature ) ) 
ObjectPropertyDomain ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearAxle-Feature :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ) 
EquivalentClasses ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ObjectMinCardinality 
	( 1:'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearAxle-Feature ) ) 
EquivalentClasses ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ObjectMaxCardinality 
	( 1:'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearAxle-Feature ) ) 
ObjectPropertyRange ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearAxle-Feature :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.RearAxle-Class ) 

Declaration ( ObjectProperty ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearWheel_1-Feature ) ) 
ObjectPropertyDomain ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearWheel_1-Feature :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ) 
EquivalentClasses ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ObjectMinCardinality 
	( 1:'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearWheel_1-Feature ) ) 
EquivalentClasses ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ObjectMaxCardinality 
	( 1:'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearWheel_1-Feature ) ) 

Declaration ( ObjectProperty ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearWheel_2-Feature ) ) 
ObjectPropertyDomain ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearWheel_2-Feature :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ) 
EquivalentClasses ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ObjectMinCardinality 
	( 1:'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearWheel_2-Feature ) ) 
EquivalentClasses ( :'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly-Feature ObjectMaxCardinality 
	( 1:'Parts Tree Demo'.'Copy Generic Hierarchical Structure'.vehicle1.rearAxleAssembly.rearWheel_2-Feature ) ) 
)
````
