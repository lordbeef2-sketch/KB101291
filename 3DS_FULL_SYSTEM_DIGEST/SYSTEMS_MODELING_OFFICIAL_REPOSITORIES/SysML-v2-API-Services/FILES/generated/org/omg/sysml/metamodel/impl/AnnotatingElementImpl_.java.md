# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/generated/org/omg/sysml/metamodel/impl/AnnotatingElementImpl_.java

- repository: `SysML-v2-API-Services`
- source_path: `generated/org/omg/sysml/metamodel/impl/AnnotatingElementImpl_.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/generated/org/omg/sysml/metamodel/impl/AnnotatingElementImpl_.java
- source_bytes: 3372
- source_sha256: `7037556b85654ff65a8ef83813d373d48a35a9e3be0f1b4f1e8c382c9c315cbe`
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
@StaticMetamodel(AnnotatingElementImpl.class)
public abstract class AnnotatingElementImpl_ extends org.omg.sysml.lifecycle.impl.DataImpl_ {

	public static volatile ListAttribute<AnnotatingElementImpl, Annotation> annotation;
	public static volatile SingularAttribute<AnnotatingElementImpl, UUID> elementId;
	public static volatile ListAttribute<AnnotatingElementImpl, TextualRepresentation> textualRepresentation;
	public static volatile SingularAttribute<AnnotatingElementImpl, String> declaredShortName;
	public static volatile SingularAttribute<AnnotatingElementImpl, Boolean> isLibraryElement;
	public static volatile ListAttribute<AnnotatingElementImpl, Annotation> ownedAnnotation;
	public static volatile ListAttribute<AnnotatingElementImpl, Element> ownedElement;
	public static volatile ListAttribute<AnnotatingElementImpl, Annotation> ownedAnnotatingRelationship;
	public static volatile ListAttribute<AnnotatingElementImpl, String> aliasIds;
	public static volatile ListAttribute<AnnotatingElementImpl, Relationship> ownedRelationship;
	public static volatile SingularAttribute<AnnotatingElementImpl, String> qualifiedName;
	public static volatile ListAttribute<AnnotatingElementImpl, Documentation> documentation;
	public static volatile ListAttribute<AnnotatingElementImpl, Element> annotatedElement;
	public static volatile SingularAttribute<AnnotatingElementImpl, Boolean> isImpliedIncluded;
	public static volatile SingularAttribute<AnnotatingElementImpl, String> name;
	public static volatile SingularAttribute<AnnotatingElementImpl, String> declaredName;
	public static volatile SingularAttribute<AnnotatingElementImpl, String> shortName;

	public static final String ANNOTATION = "annotation";
	public static final String ELEMENT_ID = "elementId";
	public static final String TEXTUAL_REPRESENTATION = "textualRepresentation";
	public static final String DECLARED_SHORT_NAME = "declaredShortName";
	public static final String IS_LIBRARY_ELEMENT = "isLibraryElement";
	public static final String OWNED_ANNOTATION = "ownedAnnotation";
	public static final String OWNED_ELEMENT = "ownedElement";
	public static final String OWNED_ANNOTATING_RELATIONSHIP = "ownedAnnotatingRelationship";
	public static final String ALIAS_IDS = "aliasIds";
	public static final String OWNED_RELATIONSHIP = "ownedRelationship";
	public static final String QUALIFIED_NAME = "qualifiedName";
	public static final String DOCUMENTATION = "documentation";
	public static final String ANNOTATED_ELEMENT = "annotatedElement";
	public static final String IS_IMPLIED_INCLUDED = "isImpliedIncluded";
	public static final String NAME = "name";
	public static final String DECLARED_NAME = "declaredName";
	public static final String SHORT_NAME = "shortName";

}


````
