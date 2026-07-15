# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_LiteralExpression.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_LiteralExpression.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_LiteralExpression.kerml.xt
- source_bytes: 884
- source_sha256: `a757d77a1dec9a015849ba1406bba49e5c191f64cc29b99e0c53466b1a2225e8`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/library/Links.kerml"}
		File {from ="/library/Performances.kerml"}
		File {from ="/library/ScalarValues.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/library/Links.kerml"}
				File {from ="/library/Performances.kerml"}
				File {from ="/library/ScalarValues.kerml"}
			}
		}
	}
END_SETUP 
*/

// XPECT noErrors ---> ""
package P {
    i0 = 1;
    iu = *;
        
    r0 = 0.08;
    r1 = .08;
    r2 = 5.4321;
    r3 = 1.0;
    r4 = 1e-5; 
    r5 = .1e-05; 
    r6 = 3.1e+05; 
    r7 = 3e5;

    b0 = true;
    b1 = false;

    s0 = "aaa";
    
    // Should not parse "1." as a real literal
    x[1..*];
}

````
