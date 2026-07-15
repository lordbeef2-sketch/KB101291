# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/library.kernel/ComplexFunctions.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/library.kernel/ComplexFunctions.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/library.kernel/ComplexFunctions.kerml
- source_bytes: 2314
- source_sha256: `df0347537e6f711f3d60c1798335ef354afc420726bdc5919a80fafa348cc97a`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
standard library package ComplexFunctions {
	doc
	/*
	 * This package defines functions on Complex values, including concrete specializations of the 
	 * general arithmetic and comparison operations.
	 */

	public import ScalarValues::*;
		
	feature i: Complex[1] = rect(0.0, 1.0);
	
	function rect { in re: Real[1]; in im: Real[1]; return : Complex[1]; }
	function polar { in abs: Real[1]; in arg: Real[1]; return : Complex[1]; }
	
	function re { in x: Complex[1]; return : Real[1]; }
	function im { in x: Complex[1]; return : Real[1]; }
	
	function isZero specializes NumericalFunctions::isZero { in x : Complex[1];
		return : Boolean[1] = re(x) == 0.0 and im(x) == 0.0;
	}
	function isUnit specializes NumericalFunctions::isUnit { in x : Complex[1];
		return : Boolean[1] = re(x) == 1.0 and im(x) == 0.0;
	}
	
	function abs specializes NumericalFunctions::abs { in x: Complex[1]; return : Real[1]; }
	function arg { in x: Complex[1]; return : Real[1]; }
	
	function '+' specializes NumericalFunctions::'+' { in x: Complex[1]; in y: Complex[0..1]; return : Complex[1]; }
	function '-' specializes NumericalFunctions::'-' { in x: Complex[1]; in y: Complex[0..1]; return : Complex[1]; }
	function '*' specializes NumericalFunctions::'*' { in x: Complex[1]; in y: Complex[1]; return : Complex[1]; }
	function '/' specializes NumericalFunctions::'/' { in x: Complex[1]; in y: Complex[1]; return : Complex[1]; }
	function '**' specializes NumericalFunctions::'**' { in x: Complex[1]; in y: Complex[1]; return : Complex[1]; }
	function '^' specializes NumericalFunctions::'^' { in x: Complex[1]; in y: Complex[1]; return : Complex[1]; }
	
	function '==' specializes DataFunctions::'==' { in x: Complex[0..1]; in y: Complex[0..1]; return : Boolean[1]; }
	
	function ToString specializes BaseFunctions::ToString { in x: Complex[1]; return : String[1]; }
	function ToComplex { in x: String[1]; return : Complex[1]; }
	
	function sum specializes NumericalFunctions::sum { in collection: Complex[0..*];
		return : Complex[1] default NumericalFunctions::sum0(collection, rect(0.0, 0.0));
	}
	
	function product specializes NumericalFunctions::product { in collection: Complex[0..*];
		return : Complex[1] default NumericalFunctions::product1(collection, rect(1.0, 0.0));
	}	
}

````
