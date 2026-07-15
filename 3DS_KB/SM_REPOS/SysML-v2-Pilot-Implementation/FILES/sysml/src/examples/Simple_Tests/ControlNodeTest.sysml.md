# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Simple Tests/ControlNodeTest.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Simple Tests/ControlNodeTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Simple Tests/ControlNodeTest.sysml
- source_bytes: 363
- source_sha256: `b77d91adcfd9c0e079177a4b48b0c4f86ae5c094c1187a7c9d1018b62961da1d`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
action def ControlNodeTest {
	action A1;
	then J;
	
	action A2 {
	    out a;
	}
	then J;
	
	flow A2.a to F.a;
	
	join J;
	then fork F {
	    in a;
	    out b1;
	    out b2;
	}
	then B1;
	then B2;
	
	flow F.b1 to B1.b;
	flow F.b2 to B2.b;
		
	action B1 {
	    in b;
	}
	then M;
	
	action B2 {
	    in b;
	}
	then M; 
	
	merge M;
}
````
