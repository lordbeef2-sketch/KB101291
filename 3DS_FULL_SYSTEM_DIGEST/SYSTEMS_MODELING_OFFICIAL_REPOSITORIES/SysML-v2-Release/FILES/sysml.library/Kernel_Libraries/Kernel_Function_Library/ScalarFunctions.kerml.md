# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml.library/Kernel Libraries/Kernel Function Library/ScalarFunctions.kerml

- repository: `SysML-v2-Release`
- source_path: `sysml.library/Kernel Libraries/Kernel Function Library/ScalarFunctions.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml.library/Kernel Libraries/Kernel Function Library/ScalarFunctions.kerml
- source_bytes: 2627
- source_sha256: `4432f9d2eb9d871934e467d89b9a657ab9139897c85baf6ae60e971341e1de98`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
standard library package ScalarFunctions {
	doc
	/*
	 * This package defines abstract functions that specialize the DataFunctions for use with ScalarValues. 
	 */

	public import ScalarValues::*;
	
	abstract function '+' specializes DataFunctions::'+' { in x: ScalarValue[1]; in y: ScalarValue[0..1]; return : ScalarValue[1]; }
	abstract function '-' specializes DataFunctions::'-' { in x: ScalarValue[1]; in y: ScalarValue[0..1]; return : ScalarValue[1]; }
	abstract function '*' specializes DataFunctions::'*' { in x: ScalarValue[1]; in y: ScalarValue[1]; return : ScalarValue[1]; }
	abstract function '/' specializes DataFunctions::'/' { in x: ScalarValue[1]; in y: ScalarValue[1]; return : ScalarValue[1]; }
	abstract function '**' specializes DataFunctions::'**' { in x: ScalarValue[1]; in y: ScalarValue[1]; return : ScalarValue[1]; }
	abstract function '^' specializes DataFunctions::'^' { in x: ScalarValue[1]; in y: ScalarValue[1]; return : ScalarValue[1]; }
	abstract function '%' specializes DataFunctions::'%' { in x: ScalarValue[1]; in y: ScalarValue[1]; return : ScalarValue[1]; }
	
	abstract function 'not' specializes DataFunctions::'not' { in x: ScalarValue[1]; return : ScalarValue[1]; }
	abstract function 'xor' specializes DataFunctions::'xor' { in x: ScalarValue[1]; in y: ScalarValue[1]; return : ScalarValue[1]; }

	abstract function '~' specializes DataFunctions::'~' { in x: ScalarValue[1]; return : ScalarValue[1]; }	
	abstract function '|' specializes DataFunctions::'|' { in x: ScalarValue[1]; in y: ScalarValue[1]; return : ScalarValue[1]; }
	abstract function '&' specializes DataFunctions::'&' { in x: ScalarValue[1]; in y: ScalarValue[1]; return : ScalarValue[1]; }
	
	abstract function '<' specializes DataFunctions::'<' { in x: ScalarValue[1]; in y: ScalarValue[1]; return : Boolean[1]; }
	abstract function '>' specializes DataFunctions::'>' { in x: ScalarValue[1]; in y: ScalarValue[1]; return : Boolean[1]; }
	abstract function '<=' specializes DataFunctions::'<=' { in x: ScalarValue[1]; in y: ScalarValue[1]; return : Boolean[1]; }
	abstract function '>=' specializes DataFunctions::'>=' { in x: ScalarValue[1]; in y: ScalarValue[1]; return : Boolean[1]; }
	
	abstract function max specializes DataFunctions::max { in x: ScalarValue[1]; in y: ScalarValue[1]; return : ScalarValue[1]; }
	abstract function min specializes DataFunctions::min { in x: ScalarValue[1]; in y: ScalarValue[1]; return : ScalarValue[1]; }
	
	abstract function '..' specializes DataFunctions::'..' { in lower: ScalarValue[1]; in upper: ScalarValue[1]; return : ScalarValue[0..*]; }
}
````
