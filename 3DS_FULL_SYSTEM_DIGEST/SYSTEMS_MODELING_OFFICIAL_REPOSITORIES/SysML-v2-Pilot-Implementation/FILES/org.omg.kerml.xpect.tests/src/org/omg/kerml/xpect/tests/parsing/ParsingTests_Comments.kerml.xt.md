# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Comments.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Comments.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Comments.kerml.xt
- source_bytes: 1302
- source_sha256: `dd21aa37e2f00a82c5195cec2d6162fe8ae5bed9e3b20c9448f2448e080ec2e5`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
        ResourceSet {
                ThisFile {}
                File {from ="/library/Base.kerml"}

        }
        Workspace {
                JavaProject {
                        SrcFolder {
                                ThisFile {}
                                File {from ="/library/Base.kerml"}

                        }
                }
        }
END_SETUP
*/

// XPECT noErrors ---> ""
/* AAA */
//a lexical comment ("note") is not a part of model
package Comments {
	// inside package
	/*
*AAA
 * BBB*/	
 /*
    *
    *
    * AAA  ***   
    *BBB
    								*/

   /*
 *       AAAA
 *       BBBB           */	
 /* AAAA
 
 
  * BBBB
 *
 * CCCC
 */
 locale "en_US" /*
 * AAAA
 * BBBB
 *    CCC DDD    
 */
	
	/* comment inside a package */
	comment cmt /* Named Comment */	
	comment cmt_cmt about cmt /* Other Comment about Comment */
	
	classifier C {
		doc locale "en_US"/* Documentation on Class C */
		comment /* Comment in Class C */
		comment about Comments /* Comment about Package */
		
	}
	/* abc */
	classifier A {
		doc <a> /* Documentation comment on A*/
		comment about a locale "en_US" /* Comment about documenation with ID 'a' */		
	}
}

````
