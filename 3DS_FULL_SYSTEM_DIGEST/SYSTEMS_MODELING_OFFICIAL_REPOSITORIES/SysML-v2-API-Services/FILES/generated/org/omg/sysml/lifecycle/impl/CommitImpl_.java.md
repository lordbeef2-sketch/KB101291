# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/generated/org/omg/sysml/lifecycle/impl/CommitImpl_.java

- repository: `SysML-v2-API-Services`
- source_path: `generated/org/omg/sysml/lifecycle/impl/CommitImpl_.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/generated/org/omg/sysml/lifecycle/impl/CommitImpl_.java
- source_bytes: 1034
- source_sha256: `f8414ca32ea22edabe0a02f9ec2c690d21f0bc313ad93522b65edf4f790ba710`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.lifecycle.impl;

import java.time.ZonedDateTime;
import javax.annotation.processing.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value = "org.hibernate.jpamodelgen.JPAMetaModelEntityProcessor")
@StaticMetamodel(CommitImpl.class)
public abstract class CommitImpl_ extends org.omg.sysml.record.impl.RecordImpl_ {

	public static volatile SingularAttribute<CommitImpl, ZonedDateTime> created;
	public static volatile SetAttribute<CommitImpl, DataVersionImpl> change;
	public static volatile SingularAttribute<CommitImpl, CommitImpl> previousCommit;
	public static volatile SingularAttribute<CommitImpl, ProjectImpl> owningProject;

	public static final String CREATED = "created";
	public static final String CHANGE = "change";
	public static final String PREVIOUS_COMMIT = "previousCommit";
	public static final String OWNING_PROJECT = "owningProject";

}


````
