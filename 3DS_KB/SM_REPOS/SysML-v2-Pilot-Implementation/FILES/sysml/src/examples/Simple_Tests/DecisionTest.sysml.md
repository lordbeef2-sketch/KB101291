# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Simple Tests/DecisionTest.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Simple Tests/DecisionTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Simple Tests/DecisionTest.sysml
- source_bytes: 318
- source_sha256: `0bf09fa4d406a51ea70498885818fbd020a868e2230993081463df77ff74b5cb`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
action def DecisionTest {
	attribute x = 1;
	
	decide 'test x';
	if x == 1 then A1; 
	if x > 1 then A2;
	else A3; 
	
	then decide D; 
	if true then A1;
	if false then A2;
	
	action A1;
	action A2;
	action A3;
	
	succession S first A1 
		if x == 0 then A2;
		
	first A3;
		if x > 0 then 'test x';
}
````
