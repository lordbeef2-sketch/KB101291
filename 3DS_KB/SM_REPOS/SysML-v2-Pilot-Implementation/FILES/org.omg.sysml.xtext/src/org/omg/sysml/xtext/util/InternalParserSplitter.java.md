# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xtext/src/org/omg/sysml/xtext/util/InternalParserSplitter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xtext/src/org/omg/sysml/xtext/util/InternalParserSplitter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xtext/src/org/omg/sysml/xtext/util/InternalParserSplitter.java
- source_bytes: 448
- source_sha256: `b7394addb0e2ef63e5f860d81489307762428631666da118475053f0bb9e5ec4`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.xtext.util;

import org.omg.sysml.xtext.InternalParserSplitterFragment;

public class InternalParserSplitter extends InternalParserSplitterFragment {
	
	public static void main(String[] args) {
		InternalParserSplitter splitter = new InternalParserSplitter();
		splitter.setOriginalClassName(args[0]);
		splitter.setBaseName(args[1]);
		splitter.setCount(Integer.valueOf(args[2]));
		splitter.generate();
	}

}

````
