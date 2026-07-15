# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/generated/org/omg/sysml/data/impl/ProjectUsageImpl_.java

- repository: `SysML-v2-API-Services`
- source_path: `generated/org/omg/sysml/data/impl/ProjectUsageImpl_.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/generated/org/omg/sysml/data/impl/ProjectUsageImpl_.java
- source_bytes: 739
- source_sha256: `afb060146785bd63d4fc0ebf67dac453a01ddd8fcaccf249f76ca378ebfb930b`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.data.impl;

import java.util.UUID;
import javax.annotation.processing.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;
import org.omg.sysml.lifecycle.impl.CommitImpl;

@Generated(value = "org.hibernate.jpamodelgen.JPAMetaModelEntityProcessor")
@StaticMetamodel(ProjectUsageImpl.class)
public abstract class ProjectUsageImpl_ extends org.omg.sysml.lifecycle.impl.DataImpl_ {

	public static volatile SingularAttribute<ProjectUsageImpl, UUID> id;
	public static volatile SingularAttribute<ProjectUsageImpl, CommitImpl> usedCommit;

	public static final String ID = "id";
	public static final String USED_COMMIT = "usedCommit";

}


````
