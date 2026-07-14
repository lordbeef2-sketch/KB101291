# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/generated/org/omg/sysml/internal/impl/WorkingDataVersionImpl_.java

- repository: `SysML-v2-API-Services`
- source_path: `generated/org/omg/sysml/internal/impl/WorkingDataVersionImpl_.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/generated/org/omg/sysml/internal/impl/WorkingDataVersionImpl_.java
- source_bytes: 829
- source_sha256: `abd6857a76706ae1d90cd324c6cc4134f5860828a8fc43357bb6069fed94431f`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.internal.impl;

import javax.annotation.processing.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;
import org.omg.sysml.data.impl.ProjectUsageImpl;
import org.omg.sysml.lifecycle.impl.DataVersionImpl;

@Generated(value = "org.hibernate.jpamodelgen.JPAMetaModelEntityProcessor")
@StaticMetamodel(WorkingDataVersionImpl.class)
public abstract class WorkingDataVersionImpl_ extends org.omg.sysml.record.impl.RecordImpl_ {

	public static volatile SingularAttribute<WorkingDataVersionImpl, DataVersionImpl> dataVersion;
	public static volatile SingularAttribute<WorkingDataVersionImpl, ProjectUsageImpl> source;

	public static final String DATA_VERSION = "dataVersion";
	public static final String SOURCE = "source";

}


````
