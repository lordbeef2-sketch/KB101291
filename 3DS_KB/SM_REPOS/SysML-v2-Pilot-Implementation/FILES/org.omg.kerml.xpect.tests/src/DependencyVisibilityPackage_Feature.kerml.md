# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/DependencyVisibilityPackage_Feature.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/DependencyVisibilityPackage_Feature.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/DependencyVisibilityPackage_Feature.kerml
- source_bytes: 765
- source_sha256: `677d6ad10c26f556ed48ce17677f8c3f6260820f40be856ba3d5383c8955187f`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package VisibilityPackage {
			private feature c_Private{
				private feature c_private{}
				public feature c_public{}
			}
			
			public feature c_Public{
				private feature c_private{}
				public feature c_public{}
			}
			
			public feature c_Public_alias{
				public feature c_public{}
				private alias alias_private for c_public; 
				public alias alias_public for c_public;
			}
			
			private feature c_Private_alias{
				public feature c_public{}
				private alias alias_private for c_public; 
				public alias alias_public for c_public;
			}
			
			public feature c_clazz{
				protected feature c_Protect{
					public feature c_publicc{}
				}
				public feature c_Public{
					protected feature c_protect{}
				}
			}
		}
````
