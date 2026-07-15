# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/expression/15_01-Constants.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/expression/15_01-Constants.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/expression/15_01-Constants.sysml.xt
- source_bytes: 5566
- source_sha256: `ae35c40b8f0b1b45c893b0f69ea753bc614021e022b246f5225c45388b89b119`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.sysml.xpect.tests.expression.SysMLTests
        ResourceSet {
                ThisFile {}
                    File {from ="/library.kernel/Base.kerml"}
                    File {from ="/library.kernel/Links.kerml"}
                    File {from ="/library.kernel/Occurrences.kerml"}
                    File {from ="/library.kernel/Performances.kerml"}
                    File {from ="/library.kernel/ScalarValues.kerml"}
                    File {from ="/library.kernel/BaseFunctions.kerml"}
                    File {from ="/library.kernel/DataFunctions.kerml"}
                	File {from ="/library.kernel/ScalarFunctions.kerml"}
                	File {from ="/library.kernel/RealFunctions.kerml"}
                	File {from ="/library.systems/Items.sysml"}
                	File {from ="/library.systems/Parts.sysml"}
                	File {from ="/library.systems/Constraints.sysml"}
                	File {from ="/library.domain/Quantities and Units/USCustomaryUnits.sysml"}
					File {from ="/library.domain/Quantities and Units/Quantities.sysml"}
					File {from ="/library.domain/Quantities and Units/MeasurementReferences.sysml"}
					File {from ="/library.domain/Quantities and Units/ISQBase.sysml"}
					File {from ="/library.domain/Quantities and Units/ISQAtomicNuclear.sysml"}
					File {from ="/library.domain/Quantities and Units/ISQChemistryMolecular.sysml"}
					File {from ="/library.domain/Quantities and Units/ISQElectromagnetism.sysml"}
					File {from ="/library.domain/Quantities and Units/ISQLight.sysml"}
					File {from ="/library.domain/Quantities and Units/ISQMechanics.sysml"}
					File {from ="/library.domain/Quantities and Units/ISQSpaceTime.sysml"}
					File {from ="/library.domain/Quantities and Units/ISQThermodynamics.sysml"}
					File {from ="/library.domain/Quantities and Units/ISQ.sysml"}
					File {from ="/library.domain/Quantities and Units/SI.sysml"}
					File {from ="/library.domain/Quantities and Units/SIPrefixes.sysml"}
        }
        Workspace {
                JavaProject {
                        SrcFolder {
                                ThisFile {}
                                File {from ="/library.kernel/Base.kerml"}
                    			File {from ="/library.kernel/Links.kerml"}
                                File {from ="/library.kernel/Occurrences.kerml"}
                                File {from ="/library.kernel/Performances.kerml"}
                                File {from ="/library.kernel/ScalarValues.kerml"}
                                File {from ="/library.kernel/BaseFunctions.kerml"}
                                File {from ="/library.kernel/DataFunctions.kerml"}
                				File {from ="/library.kernel/ScalarFunctions.kerml"}
                				File {from ="/library.kernel/RealFunctions.kerml"}
                				File {from ="/library.systems/Items.sysml"}
                				File {from ="/library.systems/Parts.sysml"}
                				File {from ="/library.systems/Constraints.sysml"}
                				File {from ="/library.domain/Quantities and Units/USCustomaryUnits.sysml"}
                                File {from ="/library.domain/Quantities and Units/Quantities.sysml"}
								File {from ="/library.domain/Quantities and Units/MeasurementReferences.sysml"}
								File {from ="/library.domain/Quantities and Units/ISQBase.sysml"}
								File {from ="/library.domain/Quantities and Units/ISQAtomicNuclear.sysml"}
								File {from ="/library.domain/Quantities and Units/ISQChemistryMolecular.sysml"}
								File {from ="/library.domain/Quantities and Units/ISQElectromagnetism.sysml"}
								File {from ="/library.domain/Quantities and Units/ISQLight.sysml"}
								File {from ="/library.domain/Quantities and Units/ISQMechanics.sysml"}
								File {from ="/library.domain/Quantities and Units/ISQSpaceTime.sysml"}
								File {from ="/library.domain/Quantities and Units/ISQThermodynamics.sysml"}
								File {from ="/library.domain/Quantities and Units/ISQ.sysml"}
								File {from ="/library.domain/Quantities and Units/SI.sysml"}
								File {from ="/library.domain/Quantities and Units/SIPrefixes.sysml"}
                        }
                }
        }
END_SETUP
*/
// XPECT noErrors ---> ""
package '15_01-Constants' {
	public import MeasurementReferences::*;
    public import SI::*;
    public import RealFunctions::*;

    package 'Mathematical Constants' {
     	
        attribute e: Real {
        	assert constraint { round(e * 1E20) == 271828182845904523536.0 }
        }
        attribute pi: Real {
        	assert constraint { round(pi * 1E20) == 314159265358979323846.0 }
        }
    }

    package 'Fundamental Physical Constants' {    	
        attribute 'fine structure constant'      : DimensionOneValue = 7.2973525693E-3[one];  // 2018 CODATA attribute 7.2973525693E-3;  uncertainty = 0.0000000011E-3
        attribute 'electron to proton mass ratio': DimensionOneValue = 5.44617021487E-4[one]; // 2018 CODATA attribute 5.44617021487E-4; uncertainty = 0.00000000033E-4 
        attribute 'speed of light in vacuum'     : SpeedValue = 299792458[m/s];               // 2018 CODATA attribute 299792458 m s^-1; (exact)
     }

    package 'Global Context' {
        attribute 'nominal earth gravitational acceleration': AccelerationValue = 9.80665['m/s²'];
    }

    package 'Model X Context' {
        attribute 'amplifier gain': DimensionOneValue = 3.5[one];
    }
}


````
