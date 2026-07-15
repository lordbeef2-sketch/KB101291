# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/33. Analysis/Trade Study Analysis Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/33. Analysis/Trade Study Analysis Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/33. Analysis/Trade Study Analysis Example.sysml
- source_bytes: 1399
- source_sha256: `a0192f0b535d6ad71458f4f955e69e514fad83aeaafee77375dbe7313547cff0`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Trade Study Analysis Example' {
	private import ScalarValues::Real;
	private import TradeStudies::*;
	
	part def Engine;
	part engine4cyl : Engine;
	part engine6cyl : Engine;
	
	calc def PowerRollup { in engine : Engine; return : ISQ::PowerValue; }
	calc def MassRollup { in engine : Engine; return : ISQ::MassValue; }
	calc def EfficiencyRollup { in engine : Engine; return : Real; }
	calc def CostRollup { in engine : Engine; return : Real; }
	
	calc def EngineEvaluation { 
		in power : ISQ::PowerValue;
		in mass : ISQ::MassValue;
		in efficiency : Real;
		in cost : Real;
		return evaluation : Real;
		// Compute evaluation...
	}
		
	analysis engineTradeStudy : TradeStudy {
		subject : Engine = (engine4cyl, engine6cyl);
		objective : MaximizeObjective;

		calc :>> evaluationFunction {
			in part anEngine :>> alternative : Engine;
			
			calc powerRollup: PowerRollup { in engine = anEngine; return power; }
			calc massRollup: MassRollup { in engine = anEngine; return mass; }
			calc efficiencyRollup: EfficiencyRollup { in engine = anEngine; return efficiency; }
			calc costRollup: CostRollup { in engine = anEngine; return cost; }
			
			return :>> result : Real = EngineEvaluation(
				powerRollup.power, massRollup.mass, efficiencyRollup.efficiency, costRollup.cost
			);
		}
		
		return part :>> selectedAlternative : Engine;
	}
	
}
````
