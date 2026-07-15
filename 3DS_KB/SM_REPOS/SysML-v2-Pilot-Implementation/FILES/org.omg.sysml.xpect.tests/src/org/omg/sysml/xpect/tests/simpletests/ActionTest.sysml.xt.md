# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/ActionTest.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/ActionTest.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/ActionTest.sysml.xt
- source_bytes: 4236
- source_sha256: `214b1343995bd7156c09c3723a0bdf560714bd2f1d0a2f26ac1355fe1e1ab65e`
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
		File {from ="/library.kernel/ControlPerformances.kerml"}
		File {from ="/library.kernel/TransitionPerformances.kerml"}
		File {from ="/library.kernel/Transfers.kerml"}
		File {from ="/library.kernel/ScalarValues.kerml"}
		File {from ="/library.kernel/Clocks.kerml"}
		File {from ="/library.kernel/Observation.kerml"}
		File {from ="/library.kernel/Triggers.kerml"}
		File {from ="/library.kernel/BaseFunctions.kerml"}
		File {from ="/library.kernel/ControlFunctions.kerml"}
		File {from ="/library.systems/Attributes.sysml"}
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Ports.sysml"}
		File {from ="/library.systems/Actions.sysml"}
		File {from ="/library.systems/Calculations.sysml"}
		File {from ="/library.systems/Connections.sysml"}
		File {from ="/library.systems/Flows.sysml"}
		File {from ="/library.domain/Quantities and Units/Quantities.sysml"}
		File {from ="/library.domain/Quantities and Units/MeasurementReferences.sysml"}
		File {from ="/library.domain/Quantities and Units/ISQ.sysml"}
		File {from ="/library.domain/Quantities and Units/ISQBase.sysml"}
		File {from ="/library.domain/Quantities and Units/SI.sysml"}
		File {from ="/library.domain/Quantities and Units/Time.sysml"}
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
				File {from ="/library.kernel/ControlPerformances.kerml"}
				File {from ="/library.kernel/TransitionPerformances.kerml"}
				File {from ="/library.kernel/Transfers.kerml"}
				File {from ="/library.kernel/ScalarValues.kerml"}
				File {from ="/library.kernel/Clocks.kerml"}
				File {from ="/library.kernel/Observation.kerml"}
				File {from ="/library.kernel/Triggers.kerml"}
				File {from ="/library.kernel/BaseFunctions.kerml"}
				File {from ="/library.kernel/ControlFunctions.kerml"}
				File {from ="/library.systems/Attributes.sysml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
				File {from ="/library.systems/Actions.sysml"}
				File {from ="/library.systems/Calculations.sysml"}
				File {from ="/library.systems/Connections.sysml"}
				File {from ="/library.systems/Flows.sysml"}
				File {from ="/library.domain/Quantities and Units/Quantities.sysml"}
				File {from ="/library.domain/Quantities and Units/MeasurementReferences.sysml"}
				File {from ="/library.domain/Quantities and Units/ISQ.sysml"}
				File {from ="/library.domain/Quantities and Units/ISQBase.sysml"}
				File {from ="/library.domain/Quantities and Units/SI.sysml"}
				File {from ="/library.domain/Quantities and Units/Time.sysml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package ActionTest {
	action def A{ in x; }
	
	action a: A { 
		first start;
		
		action b { in y = x; }
		
		bind x = b.y;
	}
	
	attribute def S;
	
	action a1 {
		first start;		
		then merge m;
		then accept S;
	    then accept sig after 10[SI::s]; 
		then accept at new Time::Iso8601DateTime("2022-01-30T01:00:00Z");
		
		then send new S() to b;
		then accept when b.f;
		then decide;
			if true then m;
			else done;
	}
	
	action a2 {
		in s : S;
		action aa {
			out part target;
		}
		flow aa.target to snd1.receiver;
		action snd1 send { 
			in :>> payload = s;
		}
		action snd2 send via this to aa.target;
		bind s = snd2.payload;
	}
	
	action b {
		attribute f : ScalarValues::Boolean;
		ref action a : A;
	}
	
	action def c {
		first start;
		then action c1 {
			terminate c1;
		}
		then terminate;
	}
}

````
