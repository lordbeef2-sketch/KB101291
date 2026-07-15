# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/01. Packages/Comment Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/01. Packages/Comment Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/01. Packages/Comment Example.sysml
- source_bytes: 589
- source_sha256: `554869762367e60eba3048cd3ffa713363ff67cc7cb287d723ae9c249f0c5169`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Comment Example' {
	/* This is a comment, which is a part of the model, 
	 * annotating (by default) it's owning namespace. */
	
	comment Comment1 /* This is a named comment. */
	
	comment about Automobile
	/* This is an unnamed comment, annotating an 
	 * explicitly specified element. 
	 */
	 
	part def Automobile;
	
	alias Car for Automobile {
		/*
		 * This is a comment annotating its owning
		 * element.
		 */
	}	                         
	
	// This is a note. It is in the text, but not part 
	// of the model.
	alias Torque for ISQ::TorqueValue;
}
````
