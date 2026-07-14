# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/42. Views/Views Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/42. Views/Views Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/42. Views/Views Example.sysml
- source_bytes: 813
- source_sha256: `a68e2eb8682f328e837b2acca53dea9386906d07a3815a2edfda363c1e481ad5`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Views Example' {
	private import Views::*;
	private import 'Viewpoint Example'::*;
	private import 'Filtering Example-2'::*;
	
	view def 'Part Structure View' {
		satisfy 'system structure perspective';		
		filter @SysML::PartUsage;
	}
	
	view 'vehicle structure view' : 'Part Structure View' {
		expose vehicle::**;
		render asTreeDiagram;
	}
	
	rendering asTextualNotationTable :> asElementTable {
		view :>> columnView[1] {
			render asTextualNotation;
		}
	}

	view 'vehicle tabular views' {
		
		view 'safety features view' : 'Part Structure View' {
			expose vehicle::**[@Safety];
			render asTextualNotationTable;
		}
		
		view 'non-safety features view' : 'Part Structure View' {
			expose vehicle::**[not (@Safety)];
			render asTextualNotationTable;
		}
	}
	
}
````
