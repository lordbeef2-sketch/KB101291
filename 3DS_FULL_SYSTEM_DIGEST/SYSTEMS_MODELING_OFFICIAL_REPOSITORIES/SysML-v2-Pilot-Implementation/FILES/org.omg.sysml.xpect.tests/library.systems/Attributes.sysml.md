# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/library.systems/Attributes.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/library.systems/Attributes.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/library.systems/Attributes.sysml
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
