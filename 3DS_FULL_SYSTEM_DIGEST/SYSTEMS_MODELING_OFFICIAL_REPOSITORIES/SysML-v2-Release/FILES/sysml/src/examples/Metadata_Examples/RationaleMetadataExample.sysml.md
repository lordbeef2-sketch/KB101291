# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Metadata Examples/RationaleMetadataExample.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Metadata Examples/RationaleMetadataExample.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Metadata Examples/RationaleMetadataExample.sysml
- source_bytes: 856
- source_sha256: `48db19d9cf384cb77ff21413002578d696d9fc9cb31083afb2f15d58428e0db8`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package RationaleMetadataExample {
	private import ModelingMetadata::Rationale;
	
    /* Example: the following provides the rationale for selecting the engine4cyl based on a trade study analysis. 
    The rationale could be contained in the vehicle configuration with the selected engine */
    
    part engine;
    part engine4cyl :> engine;
    part engine6cyl :> engine;
    
    metadata engineSelectionRationale : Rationale about engine4cyl {
    	text = "This rationale for selecting the engine4cyl refers to the engineTradeOffAnalysis.";
    	explanation = engineTradeOffAnalysis;
    }
    
    private import TradeStudies::*;
    analysis engineTradeOffAnalysis:TradeStudy{
        subject alternatives :> engine [2] = (engine4cyl, engine6cyl);

        /* ... */
        
        return selectedEngine :> engine;
     }
}
````
