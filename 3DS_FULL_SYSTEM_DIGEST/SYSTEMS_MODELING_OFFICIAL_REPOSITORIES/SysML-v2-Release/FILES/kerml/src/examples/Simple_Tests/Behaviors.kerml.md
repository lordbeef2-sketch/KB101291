# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Simple Tests/Behaviors.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Simple Tests/Behaviors.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Simple Tests/Behaviors.kerml
- source_bytes: 401
- source_sha256: `12bb9172091ee9691d25175059329b9f44d2ae2572aa0e10ce95b377bb09c082`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Behaviors {
    behavior A {
        in x;
        out y = b.y1;
        composite step b : B {
            in x1 = A::x;
        }
    }
    behavior B specializes A {
        in x1;
        out var y1;
    }
    class C {
        var z = A().y;
        step a : A;
        step b : B;
        binding z = a.y;
        flow a.y to b.x1;
    }
    abstract flow msg of C;
}
````
