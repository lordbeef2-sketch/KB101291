# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive2.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive2.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/imports/recursive/Import_Recursive2.kerml
- source_bytes: 263
- source_sha256: `a537c1af8936d44ec167e09f44ebe97e3db14304c025d114a4ab9b987cd74de6`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
 package P {
    class X;
    package Q {
      class Y;
      package R {
        class Z;
      }
    }
    package S {
      class S1;
      package T {
        class T1;
        package U {
        	class U1;
        }
      }
    }
    
  }
````
