# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/expression/SimpleUnitExpression.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/expression/SimpleUnitExpression.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/expression/SimpleUnitExpression.sysml.xt
- source_bytes: 3383
- source_sha256: `2ba5529c57e400ca6f8fa0de574279dc8d65c6ef0b7cce2c7a72de52aaf69589`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.sysml.xpect.tests.expression.SysMLTests
        ResourceSet {
            ThisFile {}
            File {from ="/library.kernel/Base.kerml"}
            File {from ="/library.kernel/Links.kerml"}
            File {from ="/library.kernel/Objects.kerml"}
            File {from ="/library.kernel/Performances.kerml"}
            File {from ="/library.kernel/ScalarValues.kerml"}
            File {from ="/library.kernel/BaseFunctions.kerml"}
            File {from ="/library.kernel/DataFunctions.kerml"}
            File {from ="/library.kernel/ScalarFunctions.kerml"}
            File {from ="/library.systems/Items.sysml"}
            File {from ="/library.systems/Parts.sysml"}
			File {from ="/library.domain/Quantities and Units/Quantities.sysml"}
			File {from ="/library.domain/Quantities and Units/ISQBase.sysml"}
            File {from ="/library.domain/Quantities and Units/ISQ.sysml"}
            File {from ="/library.domain/Quantities and Units/ISQAtomicNuclear.sysml"}
			File {from ="/library.domain/Quantities and Units/ISQChemistryMolecular.sysml"}
			File {from ="/library.domain/Quantities and Units/ISQElectromagnetism.sysml"}
			File {from ="/library.domain/Quantities and Units/ISQLight.sysml"}
			File {from ="/library.domain/Quantities and Units/ISQMechanics.sysml"}
			File {from ="/library.domain/Quantities and Units/ISQSpaceTime.sysml"}
			File {from ="/library.domain/Quantities and Units/ISQThermodynamics.sysml"}
            File {from ="/library.domain/Quantities and Units/SI.sysml"}
        }
        Workspace {
            JavaProject {
                SrcFolder {
                    ThisFile {}
                    File {from ="/library.kernel/Base.kerml"}
                    File {from ="/library.kernel/Links.kerml"}
                    File {from ="/library.kernel/Objects.kerml"}
                    File {from ="/library.kernel/Performances.kerml"}
    				File {from ="/library.kernel/ScalarValues.kerml"}
    				File {from ="/library.kernel/BaseFunctions.kerml"}
    				File {from ="/library.kernel/DataFunctions.kerml"}
    				File {from ="/library.kernel/ScalarFunctions.kerml"}
    				File {from ="/library.systems/Items.sysml"}
    				File {from ="/library.systems/Parts.sysml"}
					File {from ="/library.domain/Quantities and Units/Quantities.sysml"}
					File {from ="/library.domain/Quantities and Units/ISQBase.sysml"}
	                File {from ="/library.domain/Quantities and Units/ISQ.sysml"}
	                File {from ="/library.domain/Quantities and Units/ISQAtomicNuclear.sysml"}
					File {from ="/library.domain/Quantities and Units/ISQChemistryMolecular.sysml"}
					File {from ="/library.domain/Quantities and Units/ISQElectromagnetism.sysml"}
					File {from ="/library.domain/Quantities and Units/ISQLight.sysml"}
					File {from ="/library.domain/Quantities and Units/ISQMechanics.sysml"}
					File {from ="/library.domain/Quantities and Units/ISQSpaceTime.sysml"}
					File {from ="/library.domain/Quantities and Units/ISQThermodynamics.sysml"}
	                File {from ="/library.domain/Quantities and Units/SI.sysml"}
                }
            }
        }
END_SETUP
*/
// XPECT noErrors ---> ""
package P {
    public import SI::*;
    part def Vehicle {
        attribute mass:MassValue = 1200 [kg];
    }
}


````
