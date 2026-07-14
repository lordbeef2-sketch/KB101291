# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/generated/org/omg/sysml/internal/impl/CommitDataVersionIndexImpl_.java

- repository: `SysML-v2-API-Services`
- source_path: `generated/org/omg/sysml/internal/impl/CommitDataVersionIndexImpl_.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/generated/org/omg/sysml/internal/impl/CommitDataVersionIndexImpl_.java
- source_bytes: 957
- source_sha256: `c4390ea716843ccd111e7965807ebc1934bcfba44c41df4111914b07e94e9f79`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.internal.impl;

import java.util.UUID;
import javax.annotation.processing.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;
import org.omg.sysml.lifecycle.impl.CommitImpl;

@Generated(value = "org.hibernate.jpamodelgen.JPAMetaModelEntityProcessor")
@StaticMetamodel(CommitDataVersionIndexImpl.class)
public abstract class CommitDataVersionIndexImpl_ {

	public static volatile SingularAttribute<CommitDataVersionIndexImpl, CommitImpl> commit;
	public static volatile SetAttribute<CommitDataVersionIndexImpl, WorkingDataVersionImpl> workingDataVersion;
	public static volatile SingularAttribute<CommitDataVersionIndexImpl, UUID> id;

	public static final String COMMIT = "commit";
	public static final String WORKING_DATA_VERSION = "workingDataVersion";
	public static final String ID = "id";

}


````
