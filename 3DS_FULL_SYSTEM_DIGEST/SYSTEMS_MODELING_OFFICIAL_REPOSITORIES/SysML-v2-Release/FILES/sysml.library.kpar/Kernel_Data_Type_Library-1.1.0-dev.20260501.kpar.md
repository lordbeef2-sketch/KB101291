# OFFICIAL REPOSITORY BINARY INVENTORY: SysML-v2-Release/sysml.library.kpar/Kernel_Data_Type_Library-1.1.0-dev.20260501.kpar

- repository: `SysML-v2-Release`
- source_path: `sysml.library.kpar/Kernel_Data_Type_Library-1.1.0-dev.20260501.kpar`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml.library.kpar/Kernel_Data_Type_Library-1.1.0-dev.20260501.kpar
- source_bytes: 3636
- source_sha256: `435957d0c3245f90af7c7d3d7ab7b6678d4b50e0987d81682ace4370eafe8512`
- payload_status: binary metadata only
- reason: final knowledge base is Markdown-only; binary bytes are not executable knowledge

## ARCHIVE CONTENTS

### ENTRY: .project.json

- bytes: 278
- crc32: `6ac18ac8`
- decoded_as: `utf-8`

````json
{"name":"Kernel Data Type Library","description":"Standard data type library for the Kernel Modeling Language (KerML)","version":"1.1.0-dev.20260501","usage":[{"resource":"https://www.omg.org/spec/KerML/20250201/Semantic-Library.kpar","versionConstraint":"1.1.0-dev.20260501"}]}
````

### ENTRY: .meta.json

- bytes: 573
- crc32: `3103a313`
- decoded_as: `utf-8`

````json
{"index":{"Collections":"Collections.kerml","ScalarValues":"ScalarValues.kerml","VectorValues":"VectorValues.kerml"},"created":"2025-03-13T00:00:00Z","metamodel":"https://www.omg.org/spec/KerML/20250201","checksum":{"VectorValues.kerml":{"value":"7b22f8867e1cf46ac6a8226175db4405f6c29f047b3d6ad54a044fef3ce683dc","algorithm":"SHA256"},"Collections.kerml":{"value":"6caea283ebdb11d0a960615276358abcdc99aaa12c2aa05b42a740e8a73688b1","algorithm":"SHA256"},"ScalarValues.kerml":{"value":"4db25ce00dd170fd67261f6e7e21a2616bda15d233579dc5fb3193aaf61fa5a5","algorithm":"SHA256"}}}
````

### ENTRY: VectorValues.kerml

- bytes: 1888
- crc32: `2aa6159a`
- decoded_as: `utf-8`

````kerml
standard library package VectorValues {
	doc
	/*
	 * This package provides a basic model of abstract vectors as well as concrete vectors
	 * whose components are numerical values. The package VectorFunctions defines the 
	 * corresponding vector-space functions.
	 */

	private import ScalarValues::NumericalValue;
	private import ScalarValues::Real;
	private import Collections::Array;
	
	abstract datatype VectorValue {
		doc
		/*
		 * A VectorValue is an abstract data type whose values may be operated on using
		 * VectorFunctions.
		 */
	}
	
	datatype NumericalVectorValue :> VectorValue, Array intersects VectorValue, Array {
		doc
		/*
		 * A NumericalVectorValue is a kind of VectorValue that is specifically represented
		 * as a one-dimensional array of NumericalValues. The dimension is allowed to be empty,
		 * permitting a NumericalVectorValue of rank 0, which is essentially isomorphic to a
		 * scalar NumericalValue.
		 */
	
		feature dimension[0..1] :>> dimensions;
		feature :>> elements : NumericalValue;
	}
	
	datatype CartesianVectorValue :> NumericalVectorValue {
		doc
		/*
		 * CartesianVectorValue is a specialization Numerical VectorValue for which there are 
		 * specific implementations in VectorFunctions of the abstract vector-space functions.
		 * 
		 * Note: The restriction of the element type to Real is to facilitate
		 * the complete definition of these functions.
		 */
	
		feature :>> elements : Real;
	}

	datatype ThreeVectorValue :> NumericalVectorValue {
		doc
		/*
		 * A ThreeVectorValue is a NumericalVectorValue that has dimension 3.
		 */
	
		feature :>> dimension = 3;
	}
	
	datatype CartesianThreeVectorValue :> CartesianVectorValue, ThreeVectorValue 
		intersects CartesianVectorValue, ThreeVectorValue {
		doc
		/*
		 * A CartesianThreeVectorValue is a NumericalVectorValue that is both Cartesian and
		 * has dimension 3.
		 */
	}	
}
````

### ENTRY: Collections.kerml

- bytes: 6272
- crc32: `da6d2a4c`
- decoded_as: `utf-8`

````kerml
standard library package Collections {
    doc
    /*
     * This package defines a standard set of Collection data types. Unlike sequences of values 
     * defined directly using multiplicity, these data types allow for the possibility of collections 
     * as elements of collections.
     */

    private import Base::*;
    private import ScalarValues::*;
    private import SequenceFunctions::size;
    private import SequenceFunctions::equals;
    private import IntegerFunctions::*;
    private import ControlFunctions::*;

    abstract datatype Collection {
        doc
        /*
         * A Collection is a DataValue that represents a collection of elements of a given type.
         */
        
        feature elements[0..*] nonunique {
            doc
            /*
             * The contents of the Collection.
             */
        }
    }

    abstract datatype OrderedCollection :> Collection {
        doc
        /*
         * An OrderedCollection is a Collection of which the elements are ordered and not necessarily unique.
         */
        
        feature elements[0..*] ordered nonunique :>> Collection::elements;
    }

    abstract datatype UniqueCollection :> Collection {
        doc
        /*
         * A UniqueCollection is a Collection of which the elements are unique and not necessarily ordered.
         */
        
        feature elements[0..*] :>> Collection::elements {
            doc
            /* Note: Redefinition of 'elements' is unique by default. */
        }
    }

    datatype Array :> OrderedCollection {
        doc
        /*
         * An Array is a fixed size, multi-dimensional Collection of which the elements are nonunique and ordered. 
         * Its dimensions specify how many dimensions the array has, and how many elements there are in each dimension. 
         * The rank is equal to the number of dimensions. The flattenedSize is equal to the total number of elements 
         * in the array.
         * 
         * Feature elements is a flattened sequence of all elements of an Array and can be accessed by a tuple of indices. 
         * The number of indices is equal to rank. The elements are packed according to row-major convention.
         * 
         * The elements of an Array can be accessed by a tuple of indices. The number of indices in such tuple is equal to rank. 
         * The elements are packed according to the row-major convention.
         * 
         * Note 1. Feature dimensions may be empty, which denotes a zero dimensional array, allowing an Array to collapse to a single element. 
         * This is useful to allow for specialization of an Array into a type restricted to represent a scalar. 
         * The flattenedSize of a zero dimensional array is 1.
         * 
         * Note 2: An Array can represent the generalized mathematical concept of an infinite matrix of any rank, i.e. not limited to rank two.
         */
         
        feature dimensions: Positive[0..*] ordered nonunique {
            doc
               /* 
                * Defines the N-dimensional shape of the Array.
                */
        }
        
        feature rank: Natural[1] = size(dimensions) {
            doc
            /*
             * The number of dimensions.
             */
        }
        
        feature flattenedSize: Positive[1] = dimensions->reduce '*' ?? 1 {
            doc
            /*
             * The number of elements in the Array, given as the product of the dimensions,
             * or 1 if dimensions is empty.
             */
        }
        
        inv { flattenedSize == size(elements) }
    }
    
    datatype Bag :> Collection {
        doc
        /*
         * A Bag is a variable-size Collection of which the elements are unordered and nonunique.
         */        
    }
    
    datatype Set :> UniqueCollection {
        doc
        /*
         * A Set is a variable-size Collection of which the elements are unique and unordered.
         */
    }

    datatype OrderedSet :> OrderedCollection, UniqueCollection 
        intersects OrderedCollection, UniqueCollection {
        doc
        /*
         * An OrderedSet is a variable-size Collection of which the elements are unique and ordered.
         */    
        
        feature elements[0..*] ordered :>> OrderedCollection::elements, UniqueCollection::elements {
            doc
            /* Note: Redefinition of elements is unique by default. */
        }
    }
        
    datatype List :> OrderedCollection {
        doc
        /*
         * A List is a variable-size Collection of which the elements are nonunique and ordered.
         */
    }

    datatype KeyValuePair {
        doc
        /*
         * A KeyValuePair is a DataValue that represents a pair of a key and an associated val, 
         * primarily for use in Maps.
         */
        
        feature key: Anything[0..*] ordered nonunique;
        feature val: Anything[0..*] ordered nonunique;
    }

    datatype Map :> Collection {
        doc
        /*
         * Map is a variable-size Collection of which the elements are KeyValuePairs. 
         * The keys must be unique within the Map. The vals need not be unique.
         */
        
        feature elements: KeyValuePair[0..*] :>> Collection::elements {
            doc
            /* Note: Redefinition of elements is unique by default.*/    
        }
        
        inv { 
            elements->forAll{ in e1 : KeyValuePair; 
                not elements->exists{ in e2 : KeyValuePair; 
                    e1 != e2 and e1.key->equals(e2.key) }
            }
        }
    }

    datatype OrderedMap :> Map, OrderedCollection {
        doc
        /*
         * An OrderedMap is a variable-size Map that maintains an ordering of its elements.
         *
         * The ordering may be by key of the KeyValuePair elements, or by order of construction,
         * or any other method. The essential aspect is that ordering is maintained and guaranteed across 
         * accesses to the OrderedMap. 
         */

        feature elements: KeyValuePair[0..*] ordered :>> Map::elements, OrderedCollection::elements {
            doc
            /* Note: Redefinition of elements is unique by default. */
        }
    }
}
````

### ENTRY: ScalarValues.kerml

- bytes: 862
- crc32: `c8d24cdb`
- decoded_as: `utf-8`

````kerml
standard library package ScalarValues {
	doc
	/*
	 * This package contains a basic set of primitive scalar (non-collection) data types. 
	 * These include Boolean and String types and a hierarchy of concrete Number types, from 
	 * the most general type of Complex numbers to the most specific type of Positive integers.</p>
	 */

	private import Base::DataValue;
	
	abstract datatype ScalarValue specializes DataValue;
	datatype Boolean specializes ScalarValue;
	datatype String specializes ScalarValue;
	abstract datatype NumericalValue specializes ScalarValue;
	
    abstract datatype Number specializes NumericalValue;
	datatype Complex specializes Number;
	datatype Real specializes Complex;	
	datatype Rational specializes Real;
	datatype Integer specializes Rational;
	datatype Natural specializes Integer;
    datatype Positive specializes Natural;	
}		

````

