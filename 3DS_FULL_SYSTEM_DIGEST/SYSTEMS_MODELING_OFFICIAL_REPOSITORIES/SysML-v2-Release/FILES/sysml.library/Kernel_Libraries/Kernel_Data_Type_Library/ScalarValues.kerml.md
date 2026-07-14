# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml.library/Kernel Libraries/Kernel Data Type Library/ScalarValues.kerml

- repository: `SysML-v2-Release`
- source_path: `sysml.library/Kernel Libraries/Kernel Data Type Library/ScalarValues.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml.library/Kernel Libraries/Kernel Data Type Library/ScalarValues.kerml
- source_bytes: 885
- source_sha256: `399ab6eea810f3cd9ea7b6f03b7b45cccebe9000069e6f8ac12c76e922157398`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
standard library package ScalarValues {
	doc
	/*
	 * This package contains a basic set of primitive scalar (non-collection) data types. 
	 * These include Boolean and String types and a hierarchy of concrete Number types, from 
	 * the most general type of Complex numbers to the most specific type of Positive integers.</p>
	 */

	private import Base::DataValue;
	
	abstract datatype ScalarValue specializes DataValue;
	datatype Boolean specializes ScalarValue;
	datatype String specializes ScalarValue;
	abstract datatype NumericalValue specializes ScalarValue;
	
    abstract datatype Number specializes NumericalValue;
	datatype Complex specializes Number;
	datatype Real specializes Complex;	
	datatype Rational specializes Real;
	datatype Integer specializes Rational;
	datatype Natural specializes Integer;
    datatype Positive specializes Natural;	
}		

````
