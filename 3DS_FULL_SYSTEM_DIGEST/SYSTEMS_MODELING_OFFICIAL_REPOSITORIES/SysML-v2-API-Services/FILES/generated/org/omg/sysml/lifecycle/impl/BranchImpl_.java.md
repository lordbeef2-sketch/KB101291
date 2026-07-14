# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/generated/org/omg/sysml/lifecycle/impl/BranchImpl_.java

- repository: `SysML-v2-API-Services`
- source_path: `generated/org/omg/sysml/lifecycle/impl/BranchImpl_.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/generated/org/omg/sysml/lifecycle/impl/BranchImpl_.java
- source_bytes: 943
- source_sha256: `5f11879386f202aa49e8f166edbc1a23d45cc70c6f255ba13d74223000085dd3`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.lifecycle.impl;

import java.time.ZonedDateTime;
import javax.annotation.processing.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value = "org.hibernate.jpamodelgen.JPAMetaModelEntityProcessor")
@StaticMetamodel(BranchImpl.class)
public abstract class BranchImpl_ extends org.omg.sysml.record.impl.RecordImpl_ {

	public static volatile SingularAttribute<BranchImpl, CommitImpl> head;
	public static volatile SingularAttribute<BranchImpl, ZonedDateTime> created;
	public static volatile SingularAttribute<BranchImpl, String> name;
	public static volatile SingularAttribute<BranchImpl, ProjectImpl> owningProject;

	public static final String HEAD = "head";
	public static final String CREATED = "created";
	public static final String NAME = "name";
	public static final String OWNING_PROJECT = "owningProject";

}


````
