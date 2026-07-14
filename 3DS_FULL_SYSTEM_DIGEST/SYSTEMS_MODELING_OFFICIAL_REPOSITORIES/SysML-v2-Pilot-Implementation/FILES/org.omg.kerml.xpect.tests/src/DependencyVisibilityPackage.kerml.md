# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyVisibilityPackage.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyVisibilityPackage.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyVisibilityPackage.kerml
- source_bytes: 1041
- source_sha256: `b24fda58a53148a026a274f92b198eea1611c787a1dc87a5c1ca73633aa60a9b`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package VisibilityPackage {
			private class c_Private{
				private class c_private{}
				public class c_public{}
			}
			
			public class c_Public{
				private class c_private{}
				public class c_public{}
				protected class c_protected{}
			}
			
			public class c_Public_alias{
				public class c_public{}
				private alias alias_private for c_public; 
				protected alias alias_protected for c_public;
				public alias alias_public for c_public;
				protected class c_protected{}
				protected alias alias_protected_is_c_protected for c_protected;
			}
			
			private class c_Private_alias{
				public class c_public{}
				private alias alias_private for c_public; 
				protected alias alias_protected for c_public;
				public alias alias_public for c_public;
			}
			
			public class c_clazz{
				protected class c_Protect{
					public class c_publicc{}
					protected class c_protect{}
				}
				public class c_Public{
					protected class c_protect{}
					public class c_publicc{}
				}
			}
		}
````
