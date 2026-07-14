# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/generated/org/omg/sysml/lifecycle/impl/TagImpl_.java

- repository: `SysML-v2-API-Services`
- source_path: `generated/org/omg/sysml/lifecycle/impl/TagImpl_.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/generated/org/omg/sysml/lifecycle/impl/TagImpl_.java
- source_bytes: 950
- source_sha256: `c70d1c7ce651f0e60b39dfe48caa375ee590784419c4f6fb578cc3f19598710e`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.lifecycle.impl;

import java.time.ZonedDateTime;
import javax.annotation.processing.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value = "org.hibernate.jpamodelgen.JPAMetaModelEntityProcessor")
@StaticMetamodel(TagImpl.class)
public abstract class TagImpl_ extends org.omg.sysml.record.impl.RecordImpl_ {

	public static volatile SingularAttribute<TagImpl, CommitImpl> taggedCommit;
	public static volatile SingularAttribute<TagImpl, ZonedDateTime> created;
	public static volatile SingularAttribute<TagImpl, String> name;
	public static volatile SingularAttribute<TagImpl, ProjectImpl> owningProject;

	public static final String TAGGED_COMMIT = "taggedCommit";
	public static final String CREATED = "created";
	public static final String NAME = "name";
	public static final String OWNING_PROJECT = "owningProject";

}


````
