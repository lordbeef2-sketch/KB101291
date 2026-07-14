# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Simple Tests/Expressions.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Simple Tests/Expressions.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Simple Tests/Expressions.kerml
- source_bytes: 1883
- source_sha256: `bde514f7236c6206848574ca416688c1ee34b6e12d2dc522db166b8977f8b041`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Expressions {
	private import ScalarFunctions::*;
	private import BaseFunctions::ToString;
	private import ControlFunctions::*;
	
	a: Integer;
	aa : Boolean;
	x = ToString(a * a + 3 == 4);
	y = NumericalFunctions::'+'(1,2);
	z : Boolean = aa & true xor zz | false implies z;
	zz : Boolean = aa and true xor aa or false implies z;
	grp = -x + x * y * y + a ** 3 ^ 4;
	
	b = if x > y? x-y else y-x;
	c = x->collect {in xx; xx + 1}; 
	c1 = x.{in xx; xx + 1}; 
	d = x->select {in xx; xx != null};
	d1 = x.?{in xx; xx != null};
	e = x->reduce {in s; in t; s + t}->reduce '+';
	
	behavior w { inout v : Integer;
	    step : ControlPerformances::LoopPerformance {
    		in expr whileTest {v > 3}
    		in step body {
    			step decrement {
    				out v_decr : Integer = v - 1;			
    			}
    			succession decrement then update;
    			step update : FeatureReferencingPerformances::FeatureWritePerformance {
    				in onOccurrence = w::self {
    					feature redefines startingAt : w {
    						inout feature redefines accessedFeature redefines v;
    					}
    				}
    				inout replacementValues = decrement.v_decr;
    			}
    		}
		}
	}
	
	xx = if x == 1 and y == 2? a
	     else if x == 2? b
	     else if x == 3? c
	     else 0;
    
    function TotalMass { in partMass; in subparts;
		partMass + (subparts->collect {in p; totalMass(partMass, subparts)}->reduce '+' ?? 0.0)
	}
	
	expr totalMass: TotalMass { in mass; in sub; }
	
	feature f {
		expr s { in x; return : Boolean; }
	}
	
	bb : Boolean = f.s(1);
	
	class C {
		var count : ScalarValues::Integer := 0;
	}
	
	feature obj1 : C;
	feature obj2 : C;
	
	test1 = obj1 === obj2;
	test2 = x !== obj2;
	
	class L {
		feature c : C[*];
		feature count : ScalarValues::Integer =  c#(1).count;
	}
	
	feature l = new L();
	feature w1 = w(xx);
}
````
