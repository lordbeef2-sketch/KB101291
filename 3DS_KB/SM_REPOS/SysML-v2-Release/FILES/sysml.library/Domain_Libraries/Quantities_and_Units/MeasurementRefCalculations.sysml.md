# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml.library/Domain Libraries/Quantities and Units/MeasurementRefCalculations.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml.library/Domain Libraries/Quantities and Units/MeasurementRefCalculations.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml.library/Domain Libraries/Quantities and Units/MeasurementRefCalculations.sysml
- source_bytes: 1630
- source_sha256: `4eca94723410a11906abf2183db2bc82f849a63b8e6323b27beef363e42e298c`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
standard library package MeasurementRefCalculations {
	doc
	/*
	 * This package package defines calculations on MeasurementUnits and CoordinateFrames.
	 */
	 
    private import ScalarValues::String;
    private import ScalarValues::Real;
    private import MeasurementReferences::MeasurementUnit;
    private import MeasurementReferences::ScalarMeasurementReference;
    private import MeasurementReferences::CoordinateFrame;
        
    /* MeasurementUnit operations */
    calc def '*' specializes DataFunctions::'*' { in x: MeasurementUnit[1]; in y: MeasurementUnit[1]; return : MeasurementUnit[1]; }
    calc def '/' specializes DataFunctions::'/' { in x: MeasurementUnit[1]; in y: MeasurementUnit[1]; return : MeasurementUnit[1]; }
    calc def '**' specializes DataFunctions::'**' { in x: MeasurementUnit[1]; in y: Real[1]; return : MeasurementUnit[1]; }
    calc def '^' specializes DataFunctions::'^' { in x: MeasurementUnit[1]; in y: Real[1]; return : MeasurementUnit[1]; }

    /* CoordinateFrame and MeasurementUnit operations */
    calc def 'CoordinateFrame*' specializes DataFunctions::'*' { in x: CoordinateFrame[1]; in y: MeasurementUnit[1]; return : CoordinateFrame[1]; }
    calc def 'CoordinateFrame/' specializes DataFunctions::'/' { in x: CoordinateFrame[1]; in y: MeasurementUnit[1]; return : CoordinateFrame[1]; }

    calc def ToString specializes BaseFunctions::ToString { 
        doc 
        /*
         * Returns the Unicode string symbol representing a scalar measurement reference.
         */
        in x: ScalarMeasurementReference[1]; return : String[1];
    }
}

````
