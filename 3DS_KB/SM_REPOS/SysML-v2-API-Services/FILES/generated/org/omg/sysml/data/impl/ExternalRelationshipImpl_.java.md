# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/generated/org/omg/sysml/data/impl/ExternalRelationshipImpl_.java

- repository: `SysML-v2-API-Services`
- source_path: `generated/org/omg/sysml/data/impl/ExternalRelationshipImpl_.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/generated/org/omg/sysml/data/impl/ExternalRelationshipImpl_.java
- source_bytes: 1037
- source_sha256: `e2614d58675530c9ea45416dce813c58762f05b994b6079834f9949fce3b01c8`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.data.impl;

import java.util.UUID;
import javax.annotation.processing.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value = "org.hibernate.jpamodelgen.JPAMetaModelEntityProcessor")
@StaticMetamodel(ExternalRelationshipImpl.class)
public abstract class ExternalRelationshipImpl_ extends org.omg.sysml.lifecycle.impl.DataImpl_ {

	public static volatile SingularAttribute<ExternalRelationshipImpl, String> specification;
	public static volatile SingularAttribute<ExternalRelationshipImpl, String> language;
	public static volatile SingularAttribute<ExternalRelationshipImpl, UUID> id;
	public static volatile SingularAttribute<ExternalRelationshipImpl, ExternalDataImpl> externalDataEnd;

	public static final String SPECIFICATION = "specification";
	public static final String LANGUAGE = "language";
	public static final String ID = "id";
	public static final String EXTERNAL_DATA_END = "externalDataEnd";

}


````
