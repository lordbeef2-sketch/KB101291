# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/42. Views/Viewpoint Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/42. Views/Viewpoint Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/42. Views/Viewpoint Example.sysml
- source_bytes: 1011
- source_sha256: `97151c2f3028773567dcea070c070335109dc6cfb9607fa1acf02be56daa572d`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Viewpoint Example' {	
	part def 'Systems Engineer';
	part def 'IV&V';
	
	concern 'system breakdown' {
		doc /* 
		 * To ensure that a system covers all its required capabilities,
		 * it is necessary to understand how it is broken down into
		 * subsystems and components that provide those capabilities.
		 */
		subject;
		stakeholder se : 'Systems Engineer';
		stakeholder ivv : 'IV&V';
	}
	
	concern 'modularity' {
		doc /*
		 * There should be well defined interfaces between the parts of
		 * a system that allow each part to be understood individually,
		 * as well as being part of the whole system.
		 */		 
        subject;
		stakeholder se : 'Systems Engineer';
	}
	
	viewpoint 'system structure perspective' {		
		frame 'system breakdown';
		frame 'modularity';
		
		require constraint {
			doc /*
			 * A system structure view shall show the hierarchical 
			 * part decomposition of a system, starting with a 
			 * specified root part.
			 */
		}
	}
}
````
