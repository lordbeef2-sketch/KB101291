# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/KernelLibraryTest.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/KernelLibraryTest.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/KernelLibraryTest.sysml.xt
- source_bytes: 4187
- source_sha256: `9e6299d990c44e22168f7e56192efca5740f20ddef8c3938526d33f943772d47`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.sysml.xpect.tests.validation.valid.SysMLTests

	ResourceSet {
		ThisFile {} 
 		File {from ="/library.kernel/Base.kerml"}
 		File {from ="/library.kernel/Links.kerml"}
       	File {from ="/library.kernel/Occurrences.kerml"}
       	File {from ="/library.kernel/Objects.kerml"}
		File {from ="/library.kernel/BaseFunctions.kerml"}
		File {from ="/library.kernel/Performances.kerml"}
		File {from ="/library.kernel/ControlPerformances.kerml"}
		File {from ="/library.kernel/TransitionPerformances.kerml"}
		File {from ="/library.kernel/Transfers.kerml"}
		File {from ="/library.kernel/DataFunctions.kerml"}
		File {from ="/library.kernel/ScalarFunctions.kerml"}
		File {from ="/library.kernel/NumericalFunctions.kerml"}
		File {from ="/library.kernel/ControlFunctions.kerml"}
		File {from ="/library.kernel/ScalarValues.kerml"}
		File {from ="/library.systems/Items.sysml"}
 		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Actions.sysml"}
		File {from ="/library.systems/Calculations.sysml"}
		File {from ="/library.domain/Quantities and Units/ISQBase.sysml"}
		File {from ="/library.domain/Quantities and Units/ISQ.sysml"}
		File {from ="/library.domain/Quantities and Units/ISQAtomicNuclear.sysml"}
		File {from ="/library.domain/Quantities and Units/ISQChemistryMolecular.sysml"}
		File {from ="/library.domain/Quantities and Units/ISQElectromagnetism.sysml"}
		File {from ="/library.domain/Quantities and Units/ISQLight.sysml"}
		File {from ="/library.domain/Quantities and Units/ISQMechanics.sysml"}
		File {from ="/library.domain/Quantities and Units/ISQSpaceTime.sysml"}
		File {from ="/library.domain/Quantities and Units/ISQThermodynamics.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {} 
		 		File {from ="/library.kernel/Base.kerml"}
		 		File {from ="/library.kernel/Links.kerml"}
		       	File {from ="/library.kernel/Occurrences.kerml"}
		       	File {from ="/library.kernel/Objects.kerml"}
				File {from ="/library.kernel/BaseFunctions.kerml"}
				File {from ="/library.kernel/Performances.kerml"}
				File {from ="/library.kernel/ControlPerformances.kerml"}
				File {from ="/library.kernel/TransitionPerformances.kerml"}
				File {from ="/library.kernel/Transfers.kerml"}
				File {from ="/library.kernel/DataFunctions.kerml"}
				File {from ="/library.kernel/ScalarFunctions.kerml"}
				File {from ="/library.kernel/NumericalFunctions.kerml"}
				File {from ="/library.kernel/ControlFunctions.kerml"}
				File {from ="/library.kernel/ScalarValues.kerml"}
				File {from ="/library.systems/Items.sysml"}
		 		File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Actions.sysml"}
				File {from ="/library.systems/Calculations.sysml"}
				File {from ="/library.domain/Quantities and Units/ISQBase.sysml"}
				File {from ="/library.domain/Quantities and Units/ISQ.sysml"}
				File {from ="/library.domain/Quantities and Units/ISQAtomicNuclear.sysml"}
				File {from ="/library.domain/Quantities and Units/ISQChemistryMolecular.sysml"}
				File {from ="/library.domain/Quantities and Units/ISQElectromagnetism.sysml"}
				File {from ="/library.domain/Quantities and Units/ISQLight.sysml"}
				File {from ="/library.domain/Quantities and Units/ISQMechanics.sysml"}
				File {from ="/library.domain/Quantities and Units/ISQSpaceTime.sysml"}
				File {from ="/library.domain/Quantities and Units/ISQThermodynamics.sysml"}
			}
		}
	}
END_SETUP
*/
	
	
// XPECT noErrors ---> ""
package KernelLibraryTest {

	public import ScalarValues::**; //public import ScalarValues::Real;
	public import NumericalFunctions::**; //public import NumericalFunctions::sum;
	public import ISQ::**; //ISQ::MassValue
	
	part vehicle {
		attribute m: Real;
		attribute totalMass: MassValue;
		
		part eng {
			attribute m: Real;
		}
		
		part trans {
			attribute m: Real;
		}
	}
	
	calc def MassSum {
		in partMasses : Real[0..*];
		return totalMass : Real;
		
		sum(partMasses)
	}
	
	calc ms: MassSum {
		in partMasses = (vehicle.eng.m, vehicle.trans.m);
	}
	
	totalMass = vehicle.m;

}


````
