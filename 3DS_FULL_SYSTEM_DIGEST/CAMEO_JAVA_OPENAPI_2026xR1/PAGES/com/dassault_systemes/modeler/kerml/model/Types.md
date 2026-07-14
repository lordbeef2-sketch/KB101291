# JAVA OPENAPI: Types (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Types.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Types.html`
- source_sha256: `f4c0bfd215e32ab0ede67ea76e3ce3c4bddffebdd061c9f27c43ab923ad85881`
- captured_utc: `2026-07-14T16:44:48.530849+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Types

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Types

@OpenApiAllpublic classTypes
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`Type`](kerml/Type.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Types](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static boolean`
`[anyConforms](#anyConforms(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Type](kerml/Type.html)> subTypes,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Type](kerml/Type.html)> superTypes)`
Checks whether any subtype in the given collection conforms to any supertype
 in the other collection.
`static boolean`
`[conforms](#conforms(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) subtype,
 [Type](kerml/Type.html) supertype)`
Checks whether the given subtype conforms to the specified supertype.
`static <F extends [Feature](kerml/Feature.html)> 
F`
`[getFeature](#getFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class))([Type](kerml/Type.html) type,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<F> featureKind)`
Retrieves a feature of the given type, searching owned first, then inherited.
`static [Feature](kerml/Feature.html)`
`[getFeature](#getFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate))([Type](kerml/Type.html) type,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Feature](kerml/Feature.html)> predicate)`
Retrieves a feature matching the given predicate.
`static <F extends [Feature](kerml/Feature.html)> 
F`
`[getFeature](#getFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate,java.lang.Class))([Type](kerml/Type.html) type,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<F> predicate,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<F> featureKind)`
Retrieves a feature of the given type matching the predicate, searching owned
 first, then inherited.
`static <T extends [FeatureMembership](kerml/FeatureMembership.html),
F extends [Feature](kerml/Feature.html)> 
F`
`[getFeatureByMembership](#getFeatureByMembership(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class))([Type](kerml/Type.html) type,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> membershipKind)`
Retrieves a feature of the given membership kind, searching owned first,
 then inherited.
`static <T extends [FeatureMembership](kerml/FeatureMembership.html)> 
T`
`[getFeatureMembership](#getFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class))([Type](kerml/Type.html) type,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> membershipKind)`
Retrieves a feature membership of the given kind, searching owned first,
 then inherited.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FeatureMembership](kerml/FeatureMembership.html)>`
`[getInheritedFeatureMemberships](#getInheritedFeatureMemberships(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Retrieves all inherited feature memberships of the given type.
`static [Feature](kerml/Feature.html)`
`[getOwnedFeature](#getOwnedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate))([Type](kerml/Type.html) type,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Feature](kerml/Feature.html)> predicate)`
Retrieves an owned feature matching the given predicate.
`static <T extends [FeatureMembership](kerml/FeatureMembership.html),
F extends [Feature](kerml/Feature.html)> 
F`
`[getOwnedFeatureByMembership](#getOwnedFeatureByMembership(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class))([Type](kerml/Type.html) type,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> membershipKind)`
Retrieves an owned feature of the given membership kind.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Documentation](kerml/Documentation.html)>`
`[getOwnedOrFirstInheritedDocumentationFromNonStandardLibrary](#getOwnedOrFirstInheritedDocumentationFromNonStandardLibrary(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.foundation.project.ModelElementProject))([Type](kerml/Type.html) element,
 [ModelElementProject](../../foundation/project/ModelElementProject.html) project)`
Retrieves documentation owned by the type or the first inherited documentation
 from a non-standard-library supertype.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getOwnedOrFirstInheritedName](#getOwnedOrFirstInheritedName(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.foundation.project.ModelElementProject))([Type](kerml/Type.html) element,
 [ModelElementProject](../../foundation/project/ModelElementProject.html) project)`
Retrieves the name owned by the type or the first inherited name
 from a non-standard library supertype.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getOwnedOrFirstInheritedShortName](#getOwnedOrFirstInheritedShortName(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.foundation.project.ModelElementProject))([Type](kerml/Type.html) element,
 [ModelElementProject](../../foundation/project/ModelElementProject.html) project)`
Retrieves the short name owned by the type or the first inherited short name
 from a non-standard library supertype.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getOwnedOrFirstInheritedStringProperty](#getOwnedOrFirstInheritedStringProperty(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.foundation.project.ModelElementProject,java.util.function.Function))([Type](kerml/Type.html) element,
 [ModelElementProject](../../foundation/project/ModelElementProject.html) project,
 [Function](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html)<[Type](kerml/Type.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> function)`
Retrieves a string property (name, short name, etc.) owned by the type or
 inherited from the first non-standard-library supertype.
`static boolean`
`[isFeatureOf](#isFeatureOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type))([Feature](kerml/Feature.html) feature,
 [Type](kerml/Type.html) type)`
Checks whether the given feature belongs to the specified type.
`static boolean`
`[isFeatureOf](#isFeatureOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Type))([Feature](kerml/Feature.html) feature,
 [Type](kerml/Type.html) featureOwningType,
 [Type](kerml/Type.html) type)`
Checks whether the given feature belongs to the specified type, using the
 owning type if available.
`static [Type](kerml/Type.html)`
`[resolveType](#resolveType(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Resolves the underlying type if the given type is a Feature, otherwise returns it unchanged.
`static boolean`
`[specializes](#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) subType,
 [Type](kerml/Type.html) supertype)`
Checks whether the given subtype specializes (is the same as or inherits from)
 the specified supertype.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Types
public Types()
 ============ METHOD DETAIL ========== 
Method Details
specializes
public static boolean specializes([Type](kerml/Type.html) subType,
 [Type](kerml/Type.html) supertype)
Checks whether the given subtype specializes (is the same as or inherits from)
 the specified supertype.
Parameters:
`subType` - the type to check
`supertype` - the potential supertype
Returns:
true if subType is the same as or specializes supertype
anyConforms
public static boolean anyConforms([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Type](kerml/Type.html)> subTypes,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Type](kerml/Type.html)> superTypes)
Checks whether any subtype in the given collection conforms to any supertype
 in the other collection.
Parameters:
`subTypes` - collection of possible subtypes
`superTypes` - collection of possible supertypes
Returns:
true if at least one subtype conforms to at least one supertype
conforms
public static boolean conforms([Type](kerml/Type.html) subtype,
 [Type](kerml/Type.html) supertype)
Checks whether the given subtype conforms to the specified supertype.
Parameters:
`subtype` - the type being checked
`supertype` - the type to conform to
Returns:
true if subtype conforms to supertype
resolveType
@CheckForNullpublic static [Type](kerml/Type.html) resolveType(@CheckForNull
 [Type](kerml/Type.html) type)
Resolves the underlying type if the given type is a Feature, otherwise returns it unchanged.
Parameters:
`type` - the type to resolve
Returns:
the resolved type or null
getOwnedOrFirstInheritedShortName
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getOwnedOrFirstInheritedShortName([Type](kerml/Type.html) element,
 [ModelElementProject](../../foundation/project/ModelElementProject.html) project)
Retrieves the short name owned by the type or the first inherited short name
 from a non-standard library supertype.
Parameters:
`element` - the type whose name is requested
`project` - the project context
Returns:
the short name or null
getOwnedOrFirstInheritedName
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getOwnedOrFirstInheritedName([Type](kerml/Type.html) element,
 [ModelElementProject](../../foundation/project/ModelElementProject.html) project)
Retrieves the name owned by the type or the first inherited name
 from a non-standard library supertype.
Parameters:
`element` - the type whose name is requested
`project` - the project context
Returns:
the name or null
getOwnedOrFirstInheritedStringProperty
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getOwnedOrFirstInheritedStringProperty([Type](kerml/Type.html) element,
 [ModelElementProject](../../foundation/project/ModelElementProject.html) project,
 [Function](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html)<[Type](kerml/Type.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> function)
Retrieves a string property (name, short name, etc.) owned by the type or
 inherited from the first non-standard-library supertype.
Parameters:
`element` - the type to inspect
`project` - the project context
`function` - function extracting the string property
Returns:
the property value or null
getOwnedOrFirstInheritedDocumentationFromNonStandardLibrary
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Documentation](kerml/Documentation.html)> getOwnedOrFirstInheritedDocumentationFromNonStandardLibrary([Type](kerml/Type.html) element,
 [ModelElementProject](../../foundation/project/ModelElementProject.html) project)
Retrieves documentation owned by the type or the first inherited documentation
 from a non-standard-library supertype.
Parameters:
`element` - the type to inspect
`project` - the project context
Returns:
a list of documentation entries (never null)
getOwnedFeatureByMembership
@CheckForNullpublic static <T extends [FeatureMembership](kerml/FeatureMembership.html),
F extends [Feature](kerml/Feature.html)>
F getOwnedFeatureByMembership([Type](kerml/Type.html) type,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> membershipKind)
Retrieves an owned feature of the given membership kind.
Type Parameters:
`T` - membership type
`F` - feature type
Parameters:
`type` - the type to inspect
`membershipKind` - the membership class to search for
Returns:
the owned feature or null
getFeatureMembership
@CheckForNullpublic static <T extends [FeatureMembership](kerml/FeatureMembership.html)> T getFeatureMembership([Type](kerml/Type.html) type,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> membershipKind)
Retrieves a feature membership of the given kind, searching owned first,
 then inherited.
Type Parameters:
`T` - membership type
Parameters:
`type` - the type to inspect
`membershipKind` - the membership class to search for
Returns:
the membership or null
getInheritedFeatureMemberships
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[FeatureMembership](kerml/FeatureMembership.html)> getInheritedFeatureMemberships([Type](kerml/Type.html) type)
Retrieves all inherited feature memberships of the given type.
Parameters:
`type` - the type to inspect
Returns:
list of inherited feature memberships
getFeatureByMembership
@CheckForNullpublic static <T extends [FeatureMembership](kerml/FeatureMembership.html),
F extends [Feature](kerml/Feature.html)>
F getFeatureByMembership([Type](kerml/Type.html) type,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> membershipKind)
Retrieves a feature of the given membership kind, searching owned first,
 then inherited.
Type Parameters:
`T` - membership type
`F` - feature type
Parameters:
`type` - the type to inspect
`membershipKind` - the membership class to search for
Returns:
the feature or null
getFeature
@CheckForNullpublic static <F extends [Feature](kerml/Feature.html)> F getFeature([Type](kerml/Type.html) type,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<F> featureKind)
Retrieves a feature of the given type, searching owned first, then inherited.
Type Parameters:
`F` - feature type
Parameters:
`type` - the type to inspect
`featureKind` - the feature class to search for
Returns:
the feature or null
getFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) getFeature([Type](kerml/Type.html) type,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Feature](kerml/Feature.html)> predicate)
Retrieves a feature matching the given predicate.
Parameters:
`type` - the type to inspect
`predicate` - the filter predicate
Returns:
the feature or null
getOwnedFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) getOwnedFeature([Type](kerml/Type.html) type,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Feature](kerml/Feature.html)> predicate)
Retrieves an owned feature matching the given predicate.
Parameters:
`type` - the type to inspect
`predicate` - the filter predicate
Returns:
the owned feature or null
getFeature
@CheckForNullpublic static <F extends [Feature](kerml/Feature.html)> F getFeature([Type](kerml/Type.html) type,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<F> predicate,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<F> featureKind)
Retrieves a feature of the given type matching the predicate, searching owned
 first, then inherited.
Type Parameters:
`F` - feature type
Parameters:
`type` - the type to inspect
`predicate` - the filter predicate
`featureKind` - the feature class to search for
Returns:
the feature or null
isFeatureOf
public static boolean isFeatureOf([Feature](kerml/Feature.html) feature,
 [Type](kerml/Type.html) type)
Checks whether the given feature belongs to the specified type.
Parameters:
`feature` - the feature to check
`type` - the type to check against
Returns:
true if the feature belongs to the type
isFeatureOf
public static boolean isFeatureOf([Feature](kerml/Feature.html) feature,
 @CheckForNull
 [Type](kerml/Type.html) featureOwningType,
 [Type](kerml/Type.html) type)
Checks whether the given feature belongs to the specified type, using the
 owning type if available.
Parameters:
`feature` - the feature to check
`featureOwningType` - the owning type of the feature (may be null)
`type` - the type to check against
Returns:
true if the feature belongs to the type

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Types">Class Types</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Types</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Types</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Type</code></a></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Types</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#anyConforms(java.util.Collection,java.util.Collection)">anyConforms</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; subTypes,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; superTypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether any subtype in the given collection conforms to any supertype
 in the other collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#conforms(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Type)">conforms</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> subtype,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> supertype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given subtype conforms to the specified supertype.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;F extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;<br/>F</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class)">getFeature</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;F&gt; featureKind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves a feature of the given type, searching owned first, then inherited.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate)">getFeature</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; predicate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves a feature matching the given predicate.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;F extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;<br/>F</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate,java.lang.Class)">getFeature</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;F&gt; predicate,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;F&gt; featureKind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves a feature of the given type matching the predicate, searching owned
 first, then inherited.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a>,<wbr/>
F extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;<br/>F</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFeatureByMembership(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class)">getFeatureByMembership</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; membershipKind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves a feature of the given membership kind, searching owned first,
 then inherited.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class)">getFeatureMembership</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; membershipKind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves a feature membership of the given kind, searching owned first,
 then inherited.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInheritedFeatureMemberships(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getInheritedFeatureMemberships</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves all inherited feature memberships of the given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate)">getOwnedFeature</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; predicate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves an owned feature matching the given predicate.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a>,<wbr/>
F extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;<br/>F</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedFeatureByMembership(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class)">getOwnedFeatureByMembership</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; membershipKind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves an owned feature of the given membership kind.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Documentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Documentation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedOrFirstInheritedDocumentationFromNonStandardLibrary(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.foundation.project.ModelElementProject)">getOwnedOrFirstInheritedDocumentationFromNonStandardLibrary</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> element,
 <a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves documentation owned by the type or the first inherited documentation
 from a non-standard-library supertype.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedOrFirstInheritedName(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.foundation.project.ModelElementProject)">getOwnedOrFirstInheritedName</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> element,
 <a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves the name owned by the type or the first inherited name
 from a non-standard library supertype.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedOrFirstInheritedShortName(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.foundation.project.ModelElementProject)">getOwnedOrFirstInheritedShortName</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> element,
 <a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves the short name owned by the type or the first inherited short name
 from a non-standard library supertype.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedOrFirstInheritedStringProperty(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.foundation.project.ModelElementProject,java.util.function.Function)">getOwnedOrFirstInheritedStringProperty</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> element,
 <a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; function)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves a string property (name, short name, etc.) owned by the type or
 inherited from the first non-standard-library supertype.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isFeatureOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">isFeatureOf</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given feature belongs to the specified type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isFeatureOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Type)">isFeatureOf</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> featureOwningType,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given feature belongs to the specified type, using the
 owning type if available.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#resolveType(com.dassault_systemes.modeler.kerml.model.kerml.Type)">resolveType</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Resolves the underlying type if the given type is a Feature, otherwise returns it unchanged.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Type)">specializes</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> subType,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> supertype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given subtype specializes (is the same as or inherits from)
 the specified supertype.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>Types</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Types</span>()</div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="specializes(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>specializes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">specializes</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> subType,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> supertype)</span></div>
<div class="block">Checks whether the given subtype specializes (is the same as or inherits from)
 the specified supertype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>subType</code> - the type to check</dd>
<dd><code>supertype</code> - the potential supertype</dd>
<dt>Returns:</dt>
<dd>true if subType is the same as or specializes supertype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="anyConforms(java.util.Collection,java.util.Collection)">
<h3>anyConforms</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">anyConforms</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; subTypes,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; superTypes)</span></div>
<div class="block">Checks whether any subtype in the given collection conforms to any supertype
 in the other collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>subTypes</code> - collection of possible subtypes</dd>
<dd><code>superTypes</code> - collection of possible supertypes</dd>
<dt>Returns:</dt>
<dd>true if at least one subtype conforms to at least one supertype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="conforms(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>conforms</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">conforms</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> subtype,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> supertype)</span></div>
<div class="block">Checks whether the given subtype conforms to the specified supertype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>subtype</code> - the type being checked</dd>
<dd><code>supertype</code> - the type to conform to</dd>
<dt>Returns:</dt>
<dd>true if subtype conforms to supertype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resolveType(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>resolveType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></span> <span class="element-name">resolveType</span><wbr/><span class="parameters">(@CheckForNull
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Resolves the underlying type if the given type is a Feature, otherwise returns it unchanged.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to resolve</dd>
<dt>Returns:</dt>
<dd>the resolved type or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedOrFirstInheritedShortName(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.foundation.project.ModelElementProject)">
<h3>getOwnedOrFirstInheritedShortName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getOwnedOrFirstInheritedShortName</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> element,
 <a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Retrieves the short name owned by the type or the first inherited short name
 from a non-standard library supertype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the type whose name is requested</dd>
<dd><code>project</code> - the project context</dd>
<dt>Returns:</dt>
<dd>the short name or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedOrFirstInheritedName(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.foundation.project.ModelElementProject)">
<h3>getOwnedOrFirstInheritedName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getOwnedOrFirstInheritedName</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> element,
 <a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Retrieves the name owned by the type or the first inherited name
 from a non-standard library supertype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the type whose name is requested</dd>
<dd><code>project</code> - the project context</dd>
<dt>Returns:</dt>
<dd>the name or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedOrFirstInheritedStringProperty(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.foundation.project.ModelElementProject,java.util.function.Function)">
<h3>getOwnedOrFirstInheritedStringProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getOwnedOrFirstInheritedStringProperty</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> element,
 <a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; function)</span></div>
<div class="block">Retrieves a string property (name, short name, etc.) owned by the type or
 inherited from the first non-standard-library supertype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the type to inspect</dd>
<dd><code>project</code> - the project context</dd>
<dd><code>function</code> - function extracting the string property</dd>
<dt>Returns:</dt>
<dd>the property value or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedOrFirstInheritedDocumentationFromNonStandardLibrary(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.foundation.project.ModelElementProject)">
<h3>getOwnedOrFirstInheritedDocumentationFromNonStandardLibrary</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Documentation.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Documentation</a>&gt;</span> <span class="element-name">getOwnedOrFirstInheritedDocumentationFromNonStandardLibrary</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> element,
 <a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Retrieves documentation owned by the type or the first inherited documentation
 from a non-standard-library supertype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the type to inspect</dd>
<dd><code>project</code> - the project context</dd>
<dt>Returns:</dt>
<dd>a list of documentation entries (never null)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedFeatureByMembership(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class)">
<h3>getOwnedFeatureByMembership</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a>,<wbr/>
F extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span>
<span class="return-type">F</span> <span class="element-name">getOwnedFeatureByMembership</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; membershipKind)</span></div>
<div class="block">Retrieves an owned feature of the given membership kind.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - membership type</dd>
<dd><code>F</code> - feature type</dd>
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dd><code>membershipKind</code> - the membership class to search for</dd>
<dt>Returns:</dt>
<dd>the owned feature or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class)">
<h3>getFeatureMembership</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">getFeatureMembership</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; membershipKind)</span></div>
<div class="block">Retrieves a feature membership of the given kind, searching owned first,
 then inherited.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - membership type</dd>
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dd><code>membershipKind</code> - the membership class to search for</dd>
<dt>Returns:</dt>
<dd>the membership or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInheritedFeatureMemberships(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getInheritedFeatureMemberships</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a>&gt;</span> <span class="element-name">getInheritedFeatureMemberships</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Retrieves all inherited feature memberships of the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dt>Returns:</dt>
<dd>list of inherited feature memberships</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFeatureByMembership(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class)">
<h3>getFeatureByMembership</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a>,<wbr/>
F extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span>
<span class="return-type">F</span> <span class="element-name">getFeatureByMembership</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; membershipKind)</span></div>
<div class="block">Retrieves a feature of the given membership kind, searching owned first,
 then inherited.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - membership type</dd>
<dd><code>F</code> - feature type</dd>
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dd><code>membershipKind</code> - the membership class to search for</dd>
<dt>Returns:</dt>
<dd>the feature or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class)">
<h3>getFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;F extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="return-type">F</span> <span class="element-name">getFeature</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;F&gt; featureKind)</span></div>
<div class="block">Retrieves a feature of the given type, searching owned first, then inherited.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>F</code> - feature type</dd>
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dd><code>featureKind</code> - the feature class to search for</dd>
<dt>Returns:</dt>
<dd>the feature or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate)">
<h3>getFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getFeature</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; predicate)</span></div>
<div class="block">Retrieves a feature matching the given predicate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dd><code>predicate</code> - the filter predicate</dd>
<dt>Returns:</dt>
<dd>the feature or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate)">
<h3>getOwnedFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOwnedFeature</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; predicate)</span></div>
<div class="block">Retrieves an owned feature matching the given predicate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dd><code>predicate</code> - the filter predicate</dd>
<dt>Returns:</dt>
<dd>the owned feature or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate,java.lang.Class)">
<h3>getFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;F extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="return-type">F</span> <span class="element-name">getFeature</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;F&gt; predicate,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;F&gt; featureKind)</span></div>
<div class="block">Retrieves a feature of the given type matching the predicate, searching owned
 first, then inherited.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>F</code> - feature type</dd>
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dd><code>predicate</code> - the filter predicate</dd>
<dd><code>featureKind</code> - the feature class to search for</dd>
<dt>Returns:</dt>
<dd>the feature or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFeatureOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isFeatureOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFeatureOf</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Checks whether the given feature belongs to the specified type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature to check</dd>
<dd><code>type</code> - the type to check against</dd>
<dt>Returns:</dt>
<dd>true if the feature belongs to the type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFeatureOf(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isFeatureOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFeatureOf</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 @CheckForNull
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> featureOwningType,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Checks whether the given feature belongs to the specified type, using the
 owning type if available.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature to check</dd>
<dd><code>featureOwningType</code> - the owning type of the feature (may be null)</dd>
<dd><code>type</code> - the type to check against</dd>
<dt>Returns:</dt>
<dd>true if the feature belongs to the type</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
