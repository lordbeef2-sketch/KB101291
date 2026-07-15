# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/generated/org/omg/sysml/metamodel/impl/ElementImpl_.java

- repository: `SysML-v2-API-Services`
- source_path: `generated/org/omg/sysml/metamodel/impl/ElementImpl_.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/generated/org/omg/sysml/metamodel/impl/ElementImpl_.java
- source_bytes: 2717
- source_sha256: `47e156b68b4ef6aa7d0fec288917ae26a658a87f1ea0b0df0ca5940aa5ef665e`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.metamodel.impl;

import java.util.UUID;
import javax.annotation.processing.Generated;
import javax.persistence.metamodel.ListAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;
import org.omg.sysml.metamodel.Annotation;
import org.omg.sysml.metamodel.Documentation;
import org.omg.sysml.metamodel.Element;
import org.omg.sysml.metamodel.Relationship;
import org.omg.sysml.metamodel.TextualRepresentation;

@Generated(value = "org.hibernate.jpamodelgen.JPAMetaModelEntityProcessor")
@StaticMetamodel(ElementImpl.class)
public abstract class ElementImpl_ extends org.omg.sysml.lifecycle.impl.DataImpl_ {

	public static volatile SingularAttribute<ElementImpl, UUID> elementId;
	public static volatile ListAttribute<ElementImpl, TextualRepresentation> textualRepresentation;
	public static volatile SingularAttribute<ElementImpl, String> declaredShortName;
	public static volatile SingularAttribute<ElementImpl, Boolean> isLibraryElement;
	public static volatile ListAttribute<ElementImpl, Annotation> ownedAnnotation;
	public static volatile ListAttribute<ElementImpl, Element> ownedElement;
	public static volatile ListAttribute<ElementImpl, String> aliasIds;
	public static volatile ListAttribute<ElementImpl, Relationship> ownedRelationship;
	public static volatile SingularAttribute<ElementImpl, String> qualifiedName;
	public static volatile ListAttribute<ElementImpl, Documentation> documentation;
	public static volatile SingularAttribute<ElementImpl, Boolean> isImpliedIncluded;
	public static volatile SingularAttribute<ElementImpl, String> name;
	public static volatile SingularAttribute<ElementImpl, String> declaredName;
	public static volatile SingularAttribute<ElementImpl, String> shortName;

	public static final String ELEMENT_ID = "elementId";
	public static final String TEXTUAL_REPRESENTATION = "textualRepresentation";
	public static final String DECLARED_SHORT_NAME = "declaredShortName";
	public static final String IS_LIBRARY_ELEMENT = "isLibraryElement";
	public static final String OWNED_ANNOTATION = "ownedAnnotation";
	public static final String OWNED_ELEMENT = "ownedElement";
	public static final String ALIAS_IDS = "aliasIds";
	public static final String OWNED_RELATIONSHIP = "ownedRelationship";
	public static final String QUALIFIED_NAME = "qualifiedName";
	public static final String DOCUMENTATION = "documentation";
	public static final String IS_IMPLIED_INCLUDED = "isImpliedIncluded";
	public static final String NAME = "name";
	public static final String DECLARED_NAME = "declaredName";
	public static final String SHORT_NAME = "shortName";

}


````
