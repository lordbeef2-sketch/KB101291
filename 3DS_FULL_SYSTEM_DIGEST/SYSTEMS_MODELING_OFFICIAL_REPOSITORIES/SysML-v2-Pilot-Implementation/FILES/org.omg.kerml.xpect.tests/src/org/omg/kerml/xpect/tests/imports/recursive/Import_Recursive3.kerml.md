# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive3.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive3.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive3.kerml
- source_bytes: 301
- source_sha256: `749098209eded4ecb7dc386c7502e00e612cad205884b071c2115a3474410bee`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
 package P {
    class X {
    	class X1;
    }
    package Q {
      class Y;
      package R {
        class Z;
      }
    }
    package S {
      class S1 specializes X;
      package T {
        class T1;
        package U {
        	class U1;
        }
      }
    }
    
  }
````
