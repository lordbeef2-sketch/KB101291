# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml.library/Systems Library/Allocations.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml.library/Systems Library/Allocations.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml.library/Systems Library/Allocations.sysml
- source_bytes: 816
- source_sha256: `77c881254d552847ee3ac5686ff84fa7baaa9e90541b59f2b3221cc1752be56f`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
standard library package Allocations {
	doc
	/*
	 * This package defines the base types for allocations and related structural elements
	 * in the SysML language.
	 */

	private import Base::Anything;
	private import Connections::*;

	allocation def Allocation :> BinaryConnection {
		doc
		/*
		 * Allocation is the most general class of allocation, represented as a connection 
		 * between the source of the allocation and the target. Allocation is the base type 
		 * of all AllocationDefinitions.
		 */
	
		end source: Anything :>> BinaryConnection::source;
		end target: Anything :>> BinaryConnection::target;
	}
	
	abstract allocation allocations: Allocation[0..*] nonunique :> binaryConnections {
		doc
		/*
		 * allocations is the base feature of all AllocationUsages.
		 */
	}
}
````
