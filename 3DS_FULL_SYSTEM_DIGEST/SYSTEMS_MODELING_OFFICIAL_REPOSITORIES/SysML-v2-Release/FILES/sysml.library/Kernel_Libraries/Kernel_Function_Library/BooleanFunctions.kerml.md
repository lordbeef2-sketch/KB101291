# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml.library/Kernel Libraries/Kernel Function Library/BooleanFunctions.kerml

- repository: `SysML-v2-Release`
- source_path: `sysml.library/Kernel Libraries/Kernel Function Library/BooleanFunctions.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml.library/Kernel Libraries/Kernel Function Library/BooleanFunctions.kerml
- source_bytes: 984
- source_sha256: `4da6ad54f1e36ecf22f538a4b5153cb2a9831870b190b291e73e4c7a21e7ac50`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
standard library package BooleanFunctions {
	doc
	/*
	 * This package defines functions on Boolean values, including those corresponding to 
	 * (non-conditional) logical operators in the KerML expression notation.
	 */

	public import ScalarValues::*;
	
	function 'not' specializes ScalarFunctions::'not' { in x: Boolean[1]; return : Boolean[1]; }
	function 'xor' specializes ScalarFunctions::'xor' { in x: Boolean[1]; in y: Boolean[1]; return : Boolean[1]; }
	
	function '|' specializes ScalarFunctions::'|' { in x: Boolean[1]; in y: Boolean[1]; return : Boolean[1]; }
	function '&' specializes ScalarFunctions::'&' { in x: Boolean[1]; in y: Boolean[1]; return : Boolean[1]; }
	
	function '==' specializes DataFunctions::'==' { in x: Boolean[0..1]; in y: Boolean[0..1]; return : Boolean[1]; }
	
	function ToString specializes BaseFunctions::ToString { in x: Boolean[1]; return : String[1]; }
	function ToBoolean { in x: String[1]; return : Boolean[1]; }
	
}
	

````
