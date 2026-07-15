# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/ElementFilter.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/ElementFilter.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/ElementFilter.sysml.xt
- source_bytes: 2889
- source_sha256: `2608d36e02f68fdae697a87122f8c51c6f483df91d9d5c73c3977b3939c1276f`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.sysml.xpect.tests.simpletests.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/Links.kerml"}
       	File {from ="/library.kernel/Occurrences.kerml"}
       	File {from ="/library.kernel/Objects.kerml"}
       	File {from ="/library.kernel/Performances.kerml"}
       	File {from ="/library.kernel/ScalarValues.kerml"}
       	File {from ="/library.kernel/BaseFunctions.kerml"}
       	File {from ="/library.kernel/ControlFunctions.kerml"}
       	File {from ="/library.kernel/KerML.kerml"}
       	File {from ="/library.systems/Attributes.sysml"}
 		File {from ="/library.systems/Items.sysml"}
 		File {from ="/library.systems/Parts.sysml"}
 		File {from ="/library.systems/Ports.sysml"}
 		File {from ="/library.systems/Metadata.sysml"}
 		File {from ="/library.systems/SysML.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
				File {from ="/library.kernel/Links.kerml"}
		       	File {from ="/library.kernel/Occurrences.kerml"}
		       	File {from ="/library.kernel/Objects.kerml"}
		       	File {from ="/library.kernel/Performances.kerml"}
		       	File {from ="/library.kernel/ScalarValues.kerml"}
		       	File {from ="/library.kernel/BaseFunctions.kerml"}
		       	File {from ="/library.kernel/ControlFunctions.kerml"}
		       	File {from ="/library.kernel/KerML.kerml"}
		       	File {from ="/library.systems/Attributes.sysml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
 				File {from ="/library.systems/Ports.sysml"}
 				File {from ="/library.systems/Metadata.sysml"}
 				File {from ="/library.systems/SysML.sysml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package ElementFilterTest {
	abstract metadata def PartInfo {
		attribute isMandatory: ScalarValues::Boolean[0..1];
	}
	metadata def Safety :> PartInfo;
	metadata def Security :> PartInfo {
		attribute :> isMandatory = false;
	}
	
	part vehicle1_c1 {
		part interior {
			part alarm {@Security;}
			part seatBelt[2] {@Safety{isMandatory = true;}}
			part frontSeat[2];
			part driverAirBag {@Safety;}
		}
		part bodyAssy {
			part body;
			part bumper {@Safety;}
			part keylessEntry {@Security;}
		}
		part wheelAssy {
			part wheel[2];
			part antilockBrakes[2] {@Safety{isMandatory = false;}}
		}
	}
	
	package 'Safety Features' {
		public import vehicle1_c1::**;
		filter @Safety;
	}
	
	package 'Security Features' {
		public import vehicle1_c1::interior::*[@Security];
	}
	
	package 'Safety & Security Features' {
		public import vehicle1_c1::**;
		filter @Safety or @Security;
	}
	
	package 'Mandatory Features' {
		public import vehicle1_c1::**[@Safety and (as PartInfo).isMandatory];
	}
}

````
