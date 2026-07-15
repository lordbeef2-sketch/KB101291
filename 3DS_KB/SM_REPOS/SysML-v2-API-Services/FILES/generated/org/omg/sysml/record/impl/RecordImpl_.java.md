# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/generated/org/omg/sysml/record/impl/RecordImpl_.java

- repository: `SysML-v2-API-Services`
- source_path: `generated/org/omg/sysml/record/impl/RecordImpl_.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/generated/org/omg/sysml/record/impl/RecordImpl_.java
- source_bytes: 893
- source_sha256: `ea0824bd1530007d35bf022ced7cc0ccb1a0a07b0d284bb0e397595f50673021`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.record.impl;

import java.util.UUID;
import javax.annotation.processing.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value = "org.hibernate.jpamodelgen.JPAMetaModelEntityProcessor")
@StaticMetamodel(RecordImpl.class)
public abstract class RecordImpl_ {

	public static volatile SingularAttribute<RecordImpl, String> name;
	public static volatile SetAttribute<RecordImpl, String> alias;
	public static volatile SingularAttribute<RecordImpl, String> description;
	public static volatile SingularAttribute<RecordImpl, UUID> id;

	public static final String NAME = "name";
	public static final String ALIAS = "alias";
	public static final String DESCRIPTION = "description";
	public static final String ID = "id";

}


````
