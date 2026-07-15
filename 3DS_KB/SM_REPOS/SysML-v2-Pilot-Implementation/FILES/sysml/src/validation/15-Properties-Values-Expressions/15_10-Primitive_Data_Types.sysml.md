# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/validation/15-Properties-Values-Expressions/15_10-Primitive Data Types.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/validation/15-Properties-Values-Expressions/15_10-Primitive Data Types.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/validation/15-Properties-Values-Expressions/15_10-Primitive Data Types.sysml
- source_bytes: 2065
- source_sha256: `5754c77b1c4b17f8698d4c1ef0ffe20707afd14120646359af00086c8ecb6db6`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package '15.10-Primitive Data Types' {
	/*
	 * Primitive data types are defined in normative model libraries.
	 * Any more specialized data types can be declared in user-defined 
	 * model libraries or models as needed.
	 */
	 
	private import ScalarValues::Integer {
	doc
	/*
	 * The unqualified Integer is signed, in line with integer numbers in mathematics.
	 */
	}
	
	private import ScalarValues::Natural;
	attribute def UnsignedInteger :> Natural {
		doc /* Mathematically, unsigned integers are just natural numbers (non-negative integers). */		
	}
	
	private import ScalarValues::Real {
	doc
	/*
	 * The unqualified Real is signed, in line with real numbers in mathematics.
	 */
	}
	
	attribute def UnsignedReal :> Real {
		doc
		/*
		 * Example of restriction of the base Real datatype.
		 */
		attribute x: Real :>> self;
		assert constraint { x >= 0.0 }
	}
	
	private import ScalarValues::String {
		doc
		/*
		 * String attributes are sequences of characters.
		 */
	}
	
	private import ScalarValues::Boolean {
		doc
		/*
		 * Boolean type has two legal attributes: true, false.
		 */
	}
	
	private import Time::DateTime;
	
	enum def ConditionColor {
		doc
		/*
		 * Enumerations are defined as an implicit restriction of the extent of the
		 * enumeration type to the listed enumeration values.
		 * Note: Enumerations are currently limited to attributes.
		 */
	
		enum red;
		enum yellow;
		enum green;
	}
	
	attribute def ConditionLevel {
		attribute associatedColor : ConditionColor;
	}
	
	enum def SeverityEnum :> ConditionLevel {
		danger { 
			:>> associatedColor = ConditionColor::red;
		}
		warning { 
			:>> associatedColor = ConditionColor::yellow;
		}
		normal { 
			:>> associatedColor = ConditionColor::green;
		}
	}
	
	attribute def Diameter :> ISQ::LengthValue;	
	enum def DiameterChoice :> Diameter {
		small = 60 [SI::mm];
		medium = 70 [SI::mm];
		large = 80 [SI::mm];
	}	
	attribute aperatureDiameter: DiameterChoice = DiameterChoice::small;
	
}
````
