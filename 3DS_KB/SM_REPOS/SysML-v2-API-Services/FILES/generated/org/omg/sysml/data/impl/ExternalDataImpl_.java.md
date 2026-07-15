# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/generated/org/omg/sysml/data/impl/ExternalDataImpl_.java

- repository: `SysML-v2-API-Services`
- source_path: `generated/org/omg/sysml/data/impl/ExternalDataImpl_.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/generated/org/omg/sysml/data/impl/ExternalDataImpl_.java
- source_bytes: 729
- source_sha256: `a7a75444d3be6c339c1f1c4aab136e552097f6ff080c74b2d65f9eeb9d6691aa`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.data.impl;

import java.net.URI;
import java.util.UUID;
import javax.annotation.processing.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value = "org.hibernate.jpamodelgen.JPAMetaModelEntityProcessor")
@StaticMetamodel(ExternalDataImpl.class)
public abstract class ExternalDataImpl_ extends org.omg.sysml.lifecycle.impl.DataImpl_ {

	public static volatile SingularAttribute<ExternalDataImpl, URI> resourceIdentifier;
	public static volatile SingularAttribute<ExternalDataImpl, UUID> id;

	public static final String RESOURCE_IDENTIFIER = "resourceIdentifier";
	public static final String ID = "id";

}


````
