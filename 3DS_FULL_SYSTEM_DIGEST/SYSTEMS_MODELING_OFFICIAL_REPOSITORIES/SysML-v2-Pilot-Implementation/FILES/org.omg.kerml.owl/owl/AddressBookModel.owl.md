# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.owl/owl/AddressBookModel.owl

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.owl/owl/AddressBookModel.owl`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.owl/owl/AddressBookModel.owl
- source_bytes: 1926
- source_sha256: `7851b7f42588cf2edf6f76c6ea95f5bd33058c4d7c76bfb2d6a6fdf4c55c2ab3`
- decoded_as: `utf-8`


## EXACT SOURCE

````xml
Prefix ( : = <http://www.omg.org/SysML/ontology/AddressBookModel#> ) 
Ontology ( <http://www.omg.org/SysML/ontology/AddressBookModel>
 
Declaration ( Class ( :AddressBookModel.Entry-Class ) ) 
Declaration ( ObjectProperty ( :AddressBookModel.Entry.name-Feature ) ) 
ObjectPropertyDomain ( :AddressBookModel.Entry.name-Feature :AddressBookModel.Entry-Class ) 
EquivalentClasses ( :AddressBookModel.Entry-Class ObjectMinCardinality ( 1 :AddressBookModel.Entry.name-Feature ) ) 
EquivalentClasses ( :AddressBookModel.Entry-Class ObjectMaxCardinality ( 1 :AddressBookModel.Entry.name-Feature ) ) 
ObjectPropertyRange ( :AddressBookModel.Entry.name-Feature :PrimitiveTypes.String-Class ) 
Declaration ( ObjectProperty ( :AddressBookModel.Entry.address-Feature ) ) 
ObjectPropertyDomain ( :AddressBookModel.Entry.address-Feature :AddressBookModel.Entry-Class ) 
EquivalentClasses ( :AddressBookModel.Entry-Class ObjectMinCardinality ( 1 :AddressBookModel.Entry.address-Feature ) ) 
EquivalentClasses ( :AddressBookModel.Entry-Class ObjectMaxCardinality ( 1 :AddressBookModel.Entry.address-Feature ) ) 
ObjectPropertyRange ( :AddressBookModel.Entry.address-Feature :PrimitiveTypes.String-Class ) Declaration ( Class ( :AddressBookModel.AddressBook-Class ) ) 
Declaration ( ObjectProperty ( :AddressBookModel.AddressBook.entries-Feature ) ) 
ObjectPropertyDomain ( :AddressBookModel.AddressBook.entries-Feature :AddressBookModel.AddressBook-Class ) 
ObjectPropertyRange ( :AddressBookModel.AddressBook.entries-Feature :AddressBookModel.Entry-Class ) ) 

Prefix ( : = <http://www.omg.org/SysML/ontology/PrimitiveTypes#> ) 
Ontology ( <http://www.omg.org/SysML/ontology/PrimitiveTypes> 
Declaration ( Class ( :PrimitiveTypes.Integer-Class ) ) 
Declaration ( Class ( :PrimitiveTypes.Real-Class ) ) 
Declaration ( Class ( :PrimitiveTypes.String-Class ) ) 
Declaration ( Class ( :PrimitiveTypes.Timestamp-Class ) ) )
````
