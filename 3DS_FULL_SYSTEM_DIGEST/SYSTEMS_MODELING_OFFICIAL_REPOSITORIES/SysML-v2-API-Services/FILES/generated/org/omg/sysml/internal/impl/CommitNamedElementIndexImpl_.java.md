# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/generated/org/omg/sysml/internal/impl/CommitNamedElementIndexImpl_.java

- repository: `SysML-v2-API-Services`
- source_path: `generated/org/omg/sysml/internal/impl/CommitNamedElementIndexImpl_.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/generated/org/omg/sysml/internal/impl/CommitNamedElementIndexImpl_.java
- source_bytes: 999
- source_sha256: `e8d4396e26c2d8c9f8561711651941dca283384012746a2474345ce129c75053`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.internal.impl;

import java.util.UUID;
import javax.annotation.processing.Generated;
import javax.persistence.metamodel.MapAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;
import org.omg.sysml.lifecycle.impl.CommitImpl;
import org.omg.sysml.metamodel.Element;

@Generated(value = "org.hibernate.jpamodelgen.JPAMetaModelEntityProcessor")
@StaticMetamodel(CommitNamedElementIndexImpl.class)
public abstract class CommitNamedElementIndexImpl_ {

	public static volatile MapAttribute<CommitNamedElementIndexImpl, String, Element> workingNamedElement;
	public static volatile SingularAttribute<CommitNamedElementIndexImpl, CommitImpl> commit;
	public static volatile SingularAttribute<CommitNamedElementIndexImpl, UUID> id;

	public static final String WORKING_NAMED_ELEMENT = "workingNamedElement";
	public static final String COMMIT = "commit";
	public static final String ID = "id";

}


````
