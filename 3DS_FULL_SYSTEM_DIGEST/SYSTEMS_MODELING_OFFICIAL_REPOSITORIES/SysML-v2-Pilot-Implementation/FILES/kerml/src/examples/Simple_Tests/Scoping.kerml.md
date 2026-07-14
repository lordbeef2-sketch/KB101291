# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Simple Tests/Scoping.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Simple Tests/Scoping.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Simple Tests/Scoping.kerml
- source_bytes: 929
- source_sha256: `47a68673ab45a281aefd0a971abec79901c60ae5965ccc5180e753c52fae1015`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Scoping {
    package P1 {
        class A {
            feature f;
        }
        package P2 {
            class A {
                feature g;
            }
            package P3 {
                class B :> A {
                    feature :>> g;
                }
            }
        }
        package Objects {
            class Object {
                feature test1;
            }
        }
        package '$' {
            class Objects {
                class Object {
                    feature test2;
                }
            }
        }
        package P4 {
            class C :> Objects::Object {
                feature :>> test1;
            }
            class D :> '$'::Objects::Object {
                feature :>> test2;
            }
            class E :> $::Objects::Object {
                feature :>> subobjects;
            }
        }
    }
}
````
