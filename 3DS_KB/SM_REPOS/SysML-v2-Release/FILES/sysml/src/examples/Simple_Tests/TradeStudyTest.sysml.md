# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Simple Tests/TradeStudyTest.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Simple Tests/TradeStudyTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Simple Tests/TradeStudyTest.sysml
- source_bytes: 413
- source_sha256: `8cbd294cb83db2bea01cd45d1c6c3a541bcca63385bf88e2377605e7aa14a9ca`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package TradeStudyTest {
	private import ScalarValues::Real;
	private import TradeStudies::*;
	
	part def Engine;
	part engine1: Engine;
	part engine2: Engine;
	
	analysis engineTradeStudy : TradeStudy {
		subject : Engine[1..*] = (engine1, engine2);
		objective : MaximizeObjective;

		calc :>> evaluationFunction {
			in part : Engine;
			return : Real;
		}
		
		return part : Engine;
	}
	
}
````
