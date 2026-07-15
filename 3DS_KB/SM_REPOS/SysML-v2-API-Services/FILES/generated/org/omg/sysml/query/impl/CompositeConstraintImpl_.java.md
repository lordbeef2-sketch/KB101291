# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/generated/org/omg/sysml/query/impl/CompositeConstraintImpl_.java

- repository: `SysML-v2-API-Services`
- source_path: `generated/org/omg/sysml/query/impl/CompositeConstraintImpl_.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/generated/org/omg/sysml/query/impl/CompositeConstraintImpl_.java
- source_bytes: 873
- source_sha256: `fa6b46b1f03da726943e4a83b336490f39d717b48369f5896ece6d96524e4b1e`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.query.impl;

import javax.annotation.processing.Generated;
import javax.persistence.metamodel.CollectionAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;
import org.omg.sysml.query.CompositeOperator;
import org.omg.sysml.query.Constraint;

@Generated(value = "org.hibernate.jpamodelgen.JPAMetaModelEntityProcessor")
@StaticMetamodel(CompositeConstraintImpl.class)
public abstract class CompositeConstraintImpl_ extends org.omg.sysml.query.impl.ConstraintImpl_ {

	public static volatile CollectionAttribute<CompositeConstraintImpl, Constraint> constraint;
	public static volatile SingularAttribute<CompositeConstraintImpl, CompositeOperator> operator;

	public static final String CONSTRAINT = "constraint";
	public static final String OPERATOR = "operator";

}


````
