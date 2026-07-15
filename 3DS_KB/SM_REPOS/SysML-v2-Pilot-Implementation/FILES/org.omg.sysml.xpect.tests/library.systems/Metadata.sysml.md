# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/library.systems/Metadata.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/library.systems/Metadata.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/library.systems/Metadata.sysml
- source_bytes: 915
- source_sha256: `2261103c64c193b2ee1495a7ce8f5cf4711027388b640011d0c380a77de9c916`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
standard library package Metadata {
doc
/*
 * This package defines the base types for metadata definitions and related 
 * metadata annotations in the SysML language.
 */

	private import Metaobjects::Metaobject;
	private import Metaobjects::metaobjects;
	private import Items::Item;
	private import Items::items;
	
	abstract metadata def MetadataItem :> Metaobject, Item {
		doc
		/*
		 * MetadataItem is the most general class of Items that represent Metaobjects. 
		 * MetadataItem is the base type of all MetadataDefinitions.
		 */
		 
		 ref self : MetadataItem redefines Metaobject::self, Item::self;
	}
	
	abstract item metadataItems : MetadataItem[0..*] :> metaobjects, items {
		doc
		/*
		 * metadataItems is the base feature of all MetadataUsages.
		 * 
		 * Note: It is not itself a MetadataUsage, because it is not being used as an
		 * AnnotatingElement here.
		 */
	}
}
````
