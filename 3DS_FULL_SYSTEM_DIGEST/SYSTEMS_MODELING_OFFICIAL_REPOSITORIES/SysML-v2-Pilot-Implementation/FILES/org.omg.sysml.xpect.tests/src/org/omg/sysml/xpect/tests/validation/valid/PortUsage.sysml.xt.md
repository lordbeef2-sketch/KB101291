# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/PortUsage.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/PortUsage.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/PortUsage.sysml.xt
- source_bytes: 1293
- source_sha256: `bab58752387543662c2fad73f05aec11033d6f1c1314916e7d684b1e82491d82`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.sysml.xpect.tests.validation.valid.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/BaseFunctions.kerml"}
		File {from ="/library.kernel/Objects.kerml"}
		File {from ="/library.kernel/Occurrences.kerml"}
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Ports.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
				File {from ="/library.kernel/BaseFunctions.kerml"}
				File {from ="/library.kernel/Objects.kerml"}
				File {from ="/library.kernel/Occurrences.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}		}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package 'Port Example' {
	part def ABlock;
	port def OutPort {
		out ref anout : ABlock;
		in ref ain : ABlock;
	}
	port def InPort;
	part def ABlock1 {
		port aport : OutPort;
	}
	part def ABlock2 {
		port aport : ~InPort;
	}
	part tank: ABlock1 {
		port aredefinedport redefines aport {
			out ref redefines anout;
			in ref redefines ain;
		}	
	}
}

````
