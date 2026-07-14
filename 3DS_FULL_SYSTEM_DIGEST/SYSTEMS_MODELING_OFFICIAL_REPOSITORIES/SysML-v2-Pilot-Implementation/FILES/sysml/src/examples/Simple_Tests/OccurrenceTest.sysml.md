# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Simple Tests/OccurrenceTest.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Simple Tests/OccurrenceTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Simple Tests/OccurrenceTest.sysml
- source_bytes: 546
- source_sha256: `1ee2616adf7f32c5f3245e98252b6af8f58255ef81a62c7ab6c2348af57fdd04`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package OccurrenceTest {
	occurrence def Occ {
		attribute a;
		ref occurrence occ1 : Occ;
		occurrence occ2 : Occ;
		item x;
		part y;
		
		individual snapshot s : Ind;
		timeslice t;
	}
	
	occurrence occ : Occ {
		occurrence o1 : Occ;
		ref occurrence o2 : Occ;
		item z;
	}

	individual occurrence def Ind {
		snapshot s2;
		timeslice t2;
	}
	individual occurrence ind : Ind, Occ {
		snapshot s3;
		individual timeslice t3 :> ind;
        individual snapshot s4 : Ind;
	}

	occurrence o1 {
	  occurrence o2;
	}
}
````
