# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/generated/org/omg/sysml/query/impl/PrimitiveConstraintImpl_.java

- repository: `SysML-v2-API-Services`
- source_path: `generated/org/omg/sysml/query/impl/PrimitiveConstraintImpl_.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/generated/org/omg/sysml/query/impl/PrimitiveConstraintImpl_.java
- source_bytes: 1076
- source_sha256: `69b2dcec588ee17a170aef1f60211bccf75fecea26f8282d8b0cb6f32f379c84`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.query.impl;

import javax.annotation.processing.Generated;
import javax.persistence.metamodel.ListAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;
import org.omg.sysml.query.PrimitiveOperator;

@Generated(value = "org.hibernate.jpamodelgen.JPAMetaModelEntityProcessor")
@StaticMetamodel(PrimitiveConstraintImpl.class)
public abstract class PrimitiveConstraintImpl_ extends org.omg.sysml.query.impl.ConstraintImpl_ {

	public static volatile SingularAttribute<PrimitiveConstraintImpl, Boolean> inverse;
	public static volatile SingularAttribute<PrimitiveConstraintImpl, String> property;
	public static volatile ListAttribute<PrimitiveConstraintImpl, String> value;
	public static volatile SingularAttribute<PrimitiveConstraintImpl, PrimitiveOperator> operator;

	public static final String INVERSE = "inverse";
	public static final String PROPERTY = "property";
	public static final String VALUE = "value";
	public static final String OPERATOR = "operator";

}


````
