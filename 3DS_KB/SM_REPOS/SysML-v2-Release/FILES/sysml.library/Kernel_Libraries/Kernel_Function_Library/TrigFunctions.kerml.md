# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml.library/Kernel Libraries/Kernel Function Library/TrigFunctions.kerml

- repository: `SysML-v2-Release`
- source_path: `sysml.library/Kernel Libraries/Kernel Function Library/TrigFunctions.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml.library/Kernel Libraries/Kernel Function Library/TrigFunctions.kerml
- source_bytes: 1059
- source_sha256: `614c0f168370a2efc292b40712401d57a186ef065ddebfbd63dab598701a580f`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
standard library package TrigFunctions {
	doc
	/*
	 * This package defines basic trigonometric functions on real numbers.
	 */

	public import ScalarValues::Real;
	
	feature pi : Real;
	inv piPrecision { RealFunctions::round(pi * 1E20) == 314159265358979323846.0 }
	
	function deg { in theta_rad : Real[1];
		return : Real[1] = theta_rad * 180 / pi;
	}
	function rad { in theta_deg : Real;
		return : Real[1] = theta_deg * pi / 180;
	}
	
	datatype UnitBoundedReal :> Real {
		inv unitBound { -1.0 <= that & that <= 1.0 }
	}
	
	function sin { in theta : Real[1]; return : UnitBoundedReal[1]; }
	function cos { in theta : Real[1]; return : UnitBoundedReal[1]; }
	function tan { in theta : Real[1]; 
        return : Real = sin(theta) / cos(theta);
	}
	function cot { in theta : Real; 
        return : Real = cos(theta) / sin(theta);
	}
	
	function arcsin { in x : UnitBoundedReal[1]; return : Real[1]; }
	function arccos { in x : UnitBoundedReal[1]; return : Real[1]; }
	function arctan { in x : Real[1]; return : Real[1]; }
}
````
