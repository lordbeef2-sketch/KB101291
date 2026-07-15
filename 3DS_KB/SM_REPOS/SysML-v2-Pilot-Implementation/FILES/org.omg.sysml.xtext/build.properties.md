# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xtext/build.properties

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xtext/build.properties`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xtext/build.properties
- source_bytes: 723
- source_sha256: `d2cde43868706522abe6aa3a910c71f191e5647e9f3e2eab2d7d6f0ea3767071`
- decoded_as: `utf-8`


## EXACT SOURCE

````properties
source.. = src/,\
           src-gen/,\
           xtend-gen/
bin.includes = .,\
               META-INF/,\
               lib/
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
