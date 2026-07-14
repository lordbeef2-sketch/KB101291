# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/generated/org/omg/sysml/query/impl/QueryImpl_.java

- repository: `SysML-v2-API-Services`
- source_path: `generated/org/omg/sysml/query/impl/QueryImpl_.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/generated/org/omg/sysml/query/impl/QueryImpl_.java
- source_bytes: 869
- source_sha256: `b41909c8ed035f4d1ac266f61eb6b1478448407eff26c048a6dd4274cb53e019`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.query.impl;

import javax.annotation.processing.Generated;
import javax.persistence.metamodel.SetAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;
import org.omg.sysml.lifecycle.impl.ProjectImpl;

@Generated(value = "org.hibernate.jpamodelgen.JPAMetaModelEntityProcessor")
@StaticMetamodel(QueryImpl.class)
public abstract class QueryImpl_ extends org.omg.sysml.record.impl.RecordImpl_ {

	public static volatile SetAttribute<QueryImpl, String> select;
	public static volatile SingularAttribute<QueryImpl, String> name;
	public static volatile SingularAttribute<QueryImpl, ProjectImpl> owningProject;

	public static final String SELECT = "select";
	public static final String NAME = "name";
	public static final String OWNING_PROJECT = "owningProject";

}


````
