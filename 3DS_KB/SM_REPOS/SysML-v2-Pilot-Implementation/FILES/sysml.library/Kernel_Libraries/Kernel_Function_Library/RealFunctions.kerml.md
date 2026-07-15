# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml.library/Kernel Libraries/Kernel Function Library/RealFunctions.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml.library/Kernel Libraries/Kernel Function Library/RealFunctions.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml.library/Kernel Libraries/Kernel Function Library/RealFunctions.kerml
- source_bytes: 2773
- source_sha256: `ef861eb293190368dd4cae24f190e8803a3bb2ac01a31c6d95eda1b71ac0e2ec`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
standard library package RealFunctions {
	doc
	/*
	 * This package defines Functions on Real values, including concrete specializations of the 
	 * general arithmetic and comparison operations.
	 */

	public import ScalarValues::*;
	
	function re :> ComplexFunctions::re{ in x: Real[1]; 
        return : Real[1] = x;
	}
	function im :> ComplexFunctions::im{ in x: Real[1]; 
        return : Real[1] = 0.0;
	}
	
	function abs specializes ComplexFunctions::abs { in x: Real[1]; return : Real[1]; }
	function arg specializes ComplexFunctions::arg { in x: Real[1]; 
        return : Real[1] = 0.0;
	}

	function '+' specializes ComplexFunctions::'+' { in x: Real[1]; in y: Real[0..1]; return : Real[1]; }
	function '-' specializes ComplexFunctions::'-' { in x: Real[1]; in y: Real[0..1]; return : Real[1]; }
	function '*' specializes ComplexFunctions::'*' { in x: Real[1]; in y: Real[1]; return : Real[1]; }
	function '/' specializes ComplexFunctions::'/' { in x: Real[1]; in y: Real[1]; return : Real[1]; }
	function '**' specializes ComplexFunctions::'**' { in x: Real[1]; in y: Real[1]; return : Real[1]; }
	function '^' specializes ComplexFunctions::'^' { in x: Real[1]; in y: Real[1]; return : Real[1]; }
	
	function '<' specializes NumericalFunctions::'<' { in x: Real[1]; in y: Real[1]; return : Boolean[1]; }
	function '>' specializes NumericalFunctions::'>' { in x: Real[1]; in y: Real[1]; return : Boolean[1]; }
	function '<=' specializes NumericalFunctions::'<=' { in x: Real[1]; in y: Real[1]; return : Boolean[1]; }
	function '>=' specializes NumericalFunctions::'>=' { in x: Real[1]; in y: Real[1]; return : Boolean[1]; }

	function max specializes NumericalFunctions::max { in x: Real[1]; in y: Real[1]; return : Real[1]; }
	function min specializes NumericalFunctions::min { in x: Real[1]; in y: Real[1]; return : Real[1]; }

	function '==' specializes ComplexFunctions::'==' { in x: Real[0..1]; in y: Real[0..1]; return : Boolean[1]; }
			
	function sqrt{ in x: Real[1]; return : Real[1]; }

	function floor{ in x: Real[1]; return : Integer[1]; }
	function round{ in x: Real[1]; return : Integer[1]; }
	
	function ToString specializes ComplexFunctions::ToString { in x: Real[1]; return : String[1]; }
	function ToInteger{ in x: Real[1]; return : Integer[1]; }
	function ToRational{ in x: Real[1]; return : Rational[1]; }
	function ToReal{ in x: String[1]; return : Real[1]; }
	
	function sum specializes ComplexFunctions::sum { in collection: Real[0..*]; 
        return : Real default NumericalFunctions::sum0(collection, 0.0);
	}
	
	function product specializes ComplexFunctions::product { in collection: Real[0..*]; 
        return : Real default NumericalFunctions::product1(collection, 1.0);
	}	
}

````
