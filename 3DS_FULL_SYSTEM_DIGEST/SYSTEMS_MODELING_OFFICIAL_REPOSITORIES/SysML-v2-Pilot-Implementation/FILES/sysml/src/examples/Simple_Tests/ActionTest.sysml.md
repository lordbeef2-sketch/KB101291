# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Simple Tests/ActionTest.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Simple Tests/ActionTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Simple Tests/ActionTest.sysml
- source_bytes: 861
- source_sha256: `5d41213f104eae1c6180257d9e2969da37e42fb90365e984b73afdadebe69abd`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package ActionTest {
	action def A{ in x; }
	
	action a: A { 
		first start;
		
		action b { in y = x; }
		
		bind x = b.y;
	}
	
	attribute def S;
	
	action a1 {
		first start;		
		then merge m;
		then accept S;
		then accept sig after 10[SI::s]; 
		then accept at new Time::Iso8601DateTime("2022-01-30T01:00:00Z");
		
		then send new S() to b;
		then accept when b.f;
		then decide;
			if true then m;
			else done;
	}
	
	action a2 {
		in s : S;
		action aa {
			out part target;
		}
		flow aa.target to snd.receiver;
		action snd send { 
			in :>> payload = s;
		}
		action snd2 send via this to aa.target;
		bind s = snd2.payload;
	}
	
	action b {
		attribute f : ScalarValues::Boolean;
		ref action a : A;
	}
	
	action def c {
		first start;
		then action c1 {
			terminate c1;
		}
		then terminate;
	}	
}
````
