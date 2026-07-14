# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Simple Tests/Filtering.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Simple Tests/Filtering.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Simple Tests/Filtering.kerml
- source_bytes: 1234
- source_sha256: `9de3e9969a02419eee2db0f89985e86c7012f08314bba4f2db5335e7b40f131c`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Filtering {
	private import ScalarValues::*;
	
	package Annotations {
		metaclass ApprovalAnnotation {
			approved : Boolean;
			approver : String;
			level : Natural;
		}
	}
	
	package DesignModel {
	    private import Annotations::*;
	    struct System {
	         @ApprovalAnnotation {
	            approved = true;
	            approver = "John Smith";
	            level = 2;
	        }
	    }
		composite feature system : System;
	}

	package UpperLevelApprovals {
	    private import DesignModel::**;
	    filter (as Annotations::ApprovalAnnotation).approved and 
	           (as Annotations::ApprovalAnnotation).level > 1;
	    
	    struct Test :> System;
	}
	
	package UpperLevelApprovals1 {
	    private import Annotations::**;
	    private import DesignModel::**[@Structure]
		    [(as Annotations::ApprovalAnnotation).approved and 
	         (as Annotations::ApprovalAnnotation).level > 1];
	    
	    struct Test :> System;	    
	}
	
 	private import KerML::*;
	package Meta {
		private import DesignModel::*;
		filter (Element::name == "System" and not Type::isAbstract) or 
		       Feature::isComposite;
		
		struct Test :> System; 
		feature :> system;
	}

}
````
