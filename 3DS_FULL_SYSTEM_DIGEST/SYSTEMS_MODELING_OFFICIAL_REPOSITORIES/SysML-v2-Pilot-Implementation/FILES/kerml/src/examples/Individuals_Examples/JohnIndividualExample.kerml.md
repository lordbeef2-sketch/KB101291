# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Individuals Examples/JohnIndividualExample.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Individuals Examples/JohnIndividualExample.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Individuals Examples/JohnIndividualExample.kerml
- source_bytes: 2932
- source_sha256: `7f8b010fdbf8f9c69c2ad0f2398ebbf03b2363193b0262417cd99a535e5cae44`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package JohnIndividualExample {
	private import Objects::*;
	
	class Person specializes Object {
		doc
		/*
		  This is the class of persons, each of whom has an age.
		  It is NOT restricted to maximal portions.
		  (The specialization of Object would normally be left implicit.)
		*/
	
		class Life specializes Person, Occurrences::Life;
		
		feature age : ScalarValues::Natural;
	  
	  feature redefines portions : Person {
		  doc
		  /*
		    These redefinitions enforce the "rigidity" constraint for Person.
		    They ensure that all portions of a person are also persons and 
		    that a person can only be a portion of another person. This implies
		    that the class Person must also include all the portions of any one 
		    of its instances. The redefinitions for the portion features
		    also implicitly constraint the typing of the time slice and snapshot
		    features, since they are subsets of portioning.
		    (It is currently awkward to have to declare these redefinitions
		    explicitly.)
		  */
	  }
	  feature redefines portionOf : Person;
	
	}
	
	class President specializes Person {
		doc
		/*
		  This is the class of presidents, each of which must be a time slice
		  of the life of some individual person.
		  (Note that this class is NOT "rigid".)
		*/
	
	  feature redefines timeSliceOf : Person::Life [1];
	}
	
	class John specializes Person {
		doc
		/*
		  This is the class of the specific (individual) person who is John.
		  There is at most one such person.
		*/
	
		class all JohnLife[0..1] specializes John, Occurrences::Life;
	} 
	
	class JohnAsPresident specializes John, President {
		doc
		/*
		  This is the class of time slices of John's life in which he is
		  a president.
		*/
	}
	
	class Country specializes Object {
		doc
		/*
		  This is the class of countries, each of which may have at most one
		  president.
		*/
	
		class all Life specializes Country, Occurrences::Life;

		feature presidentOfCountry : President[0..1];
	  
	  	// Rigidity constraint.
	  	feature redefines portions : Country;
	  	feature redefines portionOf : Country;
	}
	
	class UnitedStates specializes Country {
		doc
		/*
		  This is the class of the specific country that is the
		  United States. It contains a single instance. The United States
		  always has a president who must be at least 35 years old.
		*/
	
		class all USLife[1] specializes UnitedStates, Occurrences::Life ;
	  	feature presidentOfUS[1] redefines presidentOfCountry {
	   		inv { age >= 35 } 
	  	}
	}
	
	class UnitedStatesWithJohnAsPresident specializes UnitedStates {
		doc
		/*
		  This is the class of time slices of the United States during
		  which John is president of the United States.
		*/
	
	  feature redefines timeSliceOf : UnitedStates::Life;
	  feature redefines presidentOfUS : JohnAsPresident;
	}
}
````
