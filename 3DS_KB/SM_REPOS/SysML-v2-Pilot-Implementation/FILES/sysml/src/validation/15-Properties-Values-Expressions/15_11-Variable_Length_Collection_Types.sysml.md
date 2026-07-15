# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/validation/15-Properties-Values-Expressions/15_11-Variable Length Collection Types.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/validation/15-Properties-Values-Expressions/15_11-Variable Length Collection Types.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/validation/15-Properties-Values-Expressions/15_11-Variable Length Collection Types.sysml
- source_bytes: 845
- source_sha256: `591ccf783a3e4b867526654dccbd3cd441e3d283b078d0696c2717f9245d00cd`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package '15_11-Variable Length Collection Types' {
	private import ScalarValues::*;
	private import Collections::*;
	
	part def SparePart;
	part def Person;
	
	/* Examples of declaring syntactic sugar-like names for instantiating collection types. */
	
	attribute def 'Bag<SparePart>' :> Bag {
		ref part :>> elements: SparePart;
	}
	
	attribute def 'List<Integer>' :> List {
		value :>> elements: Integer;
	}
	
	attribute def 'Set<String>' :> Set {
		attribute :>> elements: String;
	}
	
	attribute def 'OrderedSet<Person>' :> OrderedSet {
		ref part :>> elements: Person;
	}
	
	attribute def 'List<Set<Person>>' :> List {
		attribute :>> elements: Set {
			ref part :>> elements: Person;
		}
	}
	
	attribute def 'Array<Real>[4]' :> Array {
		attribute :>> elements: Real;
		attribute :>> dimensions = 4;
	}
}
````
