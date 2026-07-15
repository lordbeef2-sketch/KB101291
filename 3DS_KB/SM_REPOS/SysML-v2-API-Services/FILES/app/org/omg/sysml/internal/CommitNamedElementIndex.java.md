# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/internal/CommitNamedElementIndex.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/internal/CommitNamedElementIndex.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/internal/CommitNamedElementIndex.java
- source_bytes: 460
- source_sha256: `84725fd031c8535476c850fa24cf5f262ded8e80a7a7306e25bdb0ceb32e9d00`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.internal;

import org.omg.sysml.lifecycle.Commit;
import org.omg.sysml.metamodel.Element;

import java.util.Map;
import java.util.UUID;

public interface CommitNamedElementIndex {

    UUID getId();

    void setId(UUID id);

    Commit getCommit();

    void setCommit(Commit commit);

    Map<String, Element> getWorkingNamedElement();

    void setWorkingNamedElement(Map<String, Element> workingNamedElement);
}

````
