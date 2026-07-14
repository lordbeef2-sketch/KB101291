# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.owl/build.properties

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.owl/build.properties`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.owl/build.properties
- source_bytes: 764
- source_sha256: `f9d3f02b01a8afb37a2c4dfe6480819440e4f16309bd7504296587ab1860f3ad`
- decoded_as: `utf-8`


## EXACT SOURCE

````properties
source.. = src/,\
           src-gen/,\
           xtend-gen/
bin.includes = model/generated/,\
               .,\
               META-INF/,\
               plugin.xml
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
