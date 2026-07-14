# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Simple Tests/ImportTest.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Simple Tests/ImportTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Simple Tests/ImportTest.sysml
- source_bytes: 398
- source_sha256: `46dc93640f8c0ee70b8d27931b8276919fb541405df59950b8cbcf4759f7e0cc`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package ImportTest {
    package Pkg1 {
    	private import Pkg2::Pkg21::Pkg211::P211;
    	private import Pkg2::Pkg21::*;
    	private import Pkg211::*::**;
        part p11 : Pkg211::P211;
        part def P12;
    }

    package Pkg2 {
        private import Pkg1::*;
        package Pkg21 {
        	package Pkg211 {
        		part def P211 :> P12;
        	}
        }
    }
}
````
