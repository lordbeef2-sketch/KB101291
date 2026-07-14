# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml.library/Domain Libraries/Analysis/AnalysisTooling.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml.library/Domain Libraries/Analysis/AnalysisTooling.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml.library/Domain Libraries/Analysis/AnalysisTooling.sysml
- source_bytes: 831
- source_sha256: `9c42e7b07c31d0c6f5add4da41e2c6b08fd7d07adeac79b69619c7887a8c0a60`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
standard library package AnalysisTooling {
	doc
	/*
	 * This package contains definitions for metadata annotations related
	 * to analysis tool integration.
	 */

	private import ScalarValues::*;
	
	metadata def ToolExecution {
		doc
		/*
		 * ToolExecution metadata identifies an external analysis tool to be
		 * used to implement the annotated action.
		 */
	
		attribute toolName : String;
		attribute uri : String;
	}
	
	metadata def ToolVariable {
		doc
		/*
		 * ToolVariable metadata is used in the context of an action that has
		 * been annotated with ToolExecution metadata. It is used to annotate
		 * a parameter or other feature of the action with the name of the
		 * variable in the tool that is to correspond to the annotated
		 * feature.
		 */
	
		attribute name : String;
	}
	
}
````
