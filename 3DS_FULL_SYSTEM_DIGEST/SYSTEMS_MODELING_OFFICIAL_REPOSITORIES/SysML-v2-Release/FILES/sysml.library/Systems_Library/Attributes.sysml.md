# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml.library/Systems Library/Attributes.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml.library/Systems Library/Attributes.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml.library/Systems Library/Attributes.sysml
- source_bytes: 650
- source_sha256: `eb853c5bc97965d726478e6de7e1323ea7c236b0ad69fb03fb43852b2f711bf1`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
standard library package Attributes {
doc
/*
 * This package defines the base types for attributes and related structural elements 
 * in the SysML language.
 */

	private import Base::DataValue;
	private import Base::dataValues;

	alias AttributeValue for DataValue {
		doc
		/*
		 * AttributeValue is the most general type of data values that represent qualities or characteristics 
		 * of a system or part of a system. AttributeValue is the base type of all AttributeDefinitions.
		 */
	}
			
	alias attributeValues for dataValues {
		doc
		/*
		 * attributeValues is the base feature for all AttributeUsages.
		 */
	}		
}
````
