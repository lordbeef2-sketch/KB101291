# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/KerMLXpectRuntimeModule.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/KerMLXpectRuntimeModule.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/KerMLXpectRuntimeModule.java
- source_bytes: 355
- source_sha256: `92dc6e8173eee837554127b62018ca068a5a449ce3834e739231755c45d1c0d7`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.kerml.xpect;

import org.eclipse.xtext.scoping.IGlobalScopeProvider;
import org.omg.kerml.xtext.KerMLRuntimeModule;

public class KerMLXpectRuntimeModule extends KerMLRuntimeModule {
	
  @Override
  public Class<? extends IGlobalScopeProvider> bindIGlobalScopeProvider() {
    return KerMLXpectGlobalScopeProvider.class;
  }
}

````
