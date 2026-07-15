# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.expressions.xtext/build.properties

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.expressions.xtext/build.properties`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.expressions.xtext/build.properties
- source_bytes: 700
- source_sha256: `1972ae7cb81da9e516e1f24978bef309b642e3c062583d498e2f8f2e981790b8`
- decoded_as: `utf-8`


## EXACT SOURCE

````properties
source.. = src/,\
           src-gen/,\
           xtend-gen/
bin.includes = .,\
               META-INF/
bin.excludes = **/*.mwe2,\
               **/*.xtend
additional.bundles = org.eclipse.xtext.xbase,\
                     org.eclipse.xtext.common.types,\
                     org.eclipse.xtext.xtext.generator,\
                     org.eclipse.emf.codegen.ecore,\
                     org.eclipse.emf.mwe.utils,\
                     org.eclipse.emf.mwe2.launch,\
                     org.eclipse.emf.mwe2.lib,\
                     org.objectweb.asm,\
                     org.apache.commons.logging,\
                     org.apache.log4j,\
                     com.ibm.icu

````
