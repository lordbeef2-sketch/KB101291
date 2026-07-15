# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml.library/Kernel Libraries/Kernel Function Library/IntegerFunctions.kerml

- repository: `SysML-v2-Release`
- source_path: `sysml.library/Kernel Libraries/Kernel Function Library/IntegerFunctions.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml.library/Kernel Libraries/Kernel Function Library/IntegerFunctions.kerml
- source_bytes: 2620
- source_sha256: `a5ba453320ab2bfc780073125461080500a3de6c79eae077e8cd41b78eeec7d6`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
standard library package IntegerFunctions {
	doc
	/*
	 * This package defines functions on Integer values, including concrete specializations of the 
	 * general arithmetic and comparison operations.
	 */

	public import ScalarValues::*;
	
	function abs specializes RationalFunctions::abs { in x: Integer[1]; return : Natural[1]; }
	
	function '+' specializes RationalFunctions::'+' { in x: Integer[1]; in y: Integer[0..1]; return : Integer[1]; }
	function '-' specializes RationalFunctions::'-' { in x: Integer[1]; in y: Integer[0..1]; return : Integer[1]; }
	function '*' specializes RationalFunctions::'*' { in x: Integer[1]; in y: Integer[1]; return : Integer[1]; }
	function '/' specializes RationalFunctions::'/' { in x: Integer[1]; in y: Integer[1]; return : Rational[1]; }
	function '**' specializes RationalFunctions::'**' { in x: Integer[1]; in y: Natural[1]; return : Integer[1]; }
	function '^' specializes RationalFunctions::'^' { in x: Integer[1]; in y: Natural[1]; return : Integer[1]; }
	function '%' specializes NumericalFunctions::'%' { in x: Integer[1]; in y: Integer[1]; return : Integer[1]; }
	
	function '<' specializes RationalFunctions::'<' { in x: Integer[1]; in y: Integer[1]; return : Boolean[1]; }
	function '>' specializes RationalFunctions::'>' { in x: Integer[1]; in y: Integer[1]; return : Boolean[1]; }
	function '<=' specializes RationalFunctions::'<=' { in x: Integer[1]; in y: Integer[1]; return : Boolean[1]; }
	function '>=' specializes RationalFunctions::'>=' { in x: Integer[1]; in y: Integer[1]; return : Boolean[1]; }

	function max specializes RationalFunctions::max { in x: Integer[1]; in y: Integer[1]; return : Integer[1]; }
	function min specializes RationalFunctions::min { in x: Integer[1]; in y: Integer[1]; return : Integer[1]; }

	function '==' specializes DataFunctions::'==' { in x: Integer[0..1]; in y: Integer[0..1]; return : Boolean[1]; }
	
	function '..' specializes ScalarFunctions::'..' { in lower: Integer[1]; in upper: Integer[1]; return : Integer[0..*]; }
	
	function ToString specializes RationalFunctions::ToString { in x: Integer[1]; return : String[1]; }
	function ToNatural { in x: Integer[1]; return : Natural[1]; }
	function ToInteger { in x: String[1]; return : Integer[1]; }
	
	function sum specializes RationalFunctions::sum { in collection: Integer[0..*]; 
		return : Integer[1] default NumericalFunctions::sum0(collection, 0);
	}
	
	function product specializes RationalFunctions::product { in collection: Integer[0..*];
		return : Integer[1] default NumericalFunctions::product1(collection, 1);
	}
}	

````
