# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/SysMLXpectRuntimeModule.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/SysMLXpectRuntimeModule.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/SysMLXpectRuntimeModule.java
- source_bytes: 352
- source_sha256: `b2e054473ae7e48cf47d94379ae7d383a7ceb70adb42e3a88503c0302914b354`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.xpect;

import org.eclipse.xtext.scoping.IGlobalScopeProvider;
import org.omg.sysml.xtext.SysMLRuntimeModule;

public class SysMLXpectRuntimeModule extends SysMLRuntimeModule {
  @Override
  public Class<? extends IGlobalScopeProvider> bindIGlobalScopeProvider() {
    return SysMLXpectGlobalScopeProvider.class;
  }
}

````
