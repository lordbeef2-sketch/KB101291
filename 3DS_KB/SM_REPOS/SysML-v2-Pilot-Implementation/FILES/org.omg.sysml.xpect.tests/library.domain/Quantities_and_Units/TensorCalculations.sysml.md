# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/library.domain/Quantities and Units/TensorCalculations.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/library.domain/Quantities and Units/TensorCalculations.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/library.domain/Quantities and Units/TensorCalculations.sysml
- source_bytes: 2485
- source_sha256: `8d115b571eaa29a069102bc3074b9240a69421b1a5470a47fc9c2c6def83c50c`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
standard library package TensorCalculations {
	doc
	/*
	 * This package package defines calculations for the construction of and computations on TensorQuantityValues.
	 */
	 
    private import ScalarValues::Boolean;
    private import ScalarValues::Number;
    private import Quantities::ScalarQuantityValue;
    private import Quantities::VectorQuantityValue;
    private import Quantities::TensorQuantityValue;
    private import MeasurementReferences::TensorMeasurementReference;
    private import MeasurementReferences::CoordinateTransformation;
    
    calc def '[' specializes BaseFunctions::'[' { 
    	in elements: Number[1..n] ordered; 
    	in mRef: TensorMeasurementReference[1]; 
    	return quantity: TensorQuantityValue[1];
    	private attribute n = mRef.flattenedSize;
    }

    calc def isZeroTensorQuantity { 
    	in x : TensorQuantityValue[1]; 
    	return : Boolean[1];
    }
    calc def isUnitTensorQuantity { 
    	in x : TensorQuantityValue[1]; 
    	return : Boolean[1];
    }

    /* Addition and subtraction */
    calc def '+' :> DataFunctions::'+' { in : TensorQuantityValue[1]; in : TensorQuantityValue[1]; return : TensorQuantityValue[1]; }
    calc def '-' :> DataFunctions::'-' { in : TensorQuantityValue[1]; in : TensorQuantityValue[1]; return : TensorQuantityValue[1]; }

    /* Multiplication and division */
    calc def scalarTensorMult { in : Number[1]; in : TensorQuantityValue[1]; return : TensorQuantityValue[1]; }
    calc def TensorScalarMult { in : TensorQuantityValue[1]; in : Number[1]; return : TensorQuantityValue[1]; }
    calc def scalarQuantityTensorMult { in : ScalarQuantityValue[1]; in : TensorQuantityValue[1]; return : TensorQuantityValue[1]; }
    calc def TensorScalarQuantityMult { in : TensorQuantityValue[1]; in : ScalarQuantityValue[1]; return : TensorQuantityValue[1]; }
    calc def tensorVectorMult { in : TensorQuantityValue[1]; in : VectorQuantityValue[1]; return : VectorQuantityValue[1]; }
    calc def vectorTensorMult { in : VectorQuantityValue[1]; in : TensorQuantityValue[1]; return : VectorQuantityValue[1]; }
    calc def tensorTensorMult { in : TensorQuantityValue[1]; in : TensorQuantityValue[1]; return : TensorQuantityValue[1]; }
    
    /* Tensor transformation */
    calc def transform {
        in transformation : CoordinateTransformation;
        in sourceTensor : TensorQuantityValue;
        return targetTensor : TensorQuantityValue;
    }
}
````
