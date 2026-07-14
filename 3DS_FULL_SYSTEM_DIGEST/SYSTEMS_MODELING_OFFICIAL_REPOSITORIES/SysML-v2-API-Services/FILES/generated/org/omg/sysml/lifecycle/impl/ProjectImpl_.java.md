# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/generated/org/omg/sysml/lifecycle/impl/ProjectImpl_.java

- repository: `SysML-v2-API-Services`
- source_path: `generated/org/omg/sysml/lifecycle/impl/ProjectImpl_.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/generated/org/omg/sysml/lifecycle/impl/ProjectImpl_.java
- source_bytes: 965
- source_sha256: `7584caad215c5e6daaace0db56509006538625d2bdafc7d39ce19a4026df5ddb`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.lifecycle.impl;

import java.time.ZonedDateTime;
import javax.annotation.processing.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value = "org.hibernate.jpamodelgen.JPAMetaModelEntityProcessor")
@StaticMetamodel(ProjectImpl.class)
public abstract class ProjectImpl_ extends org.omg.sysml.record.impl.RecordImpl_ {

	public static volatile SingularAttribute<ProjectImpl, ZonedDateTime> created;
	public static volatile SingularAttribute<ProjectImpl, BranchImpl> defaultBranch;
	public static volatile SingularAttribute<ProjectImpl, String> name;
	public static volatile SingularAttribute<ProjectImpl, String> description;

	public static final String CREATED = "created";
	public static final String DEFAULT_BRANCH = "defaultBranch";
	public static final String NAME = "name";
	public static final String DESCRIPTION = "description";

}


````
