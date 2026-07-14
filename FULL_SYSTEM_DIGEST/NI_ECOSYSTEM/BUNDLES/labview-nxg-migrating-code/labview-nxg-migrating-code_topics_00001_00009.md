# NI DOCUMENT BUNDLE: labview-nxg-migrating-code

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-migrating-code start=1 end=9 -->
<!--NI_TOPIC bundle=labview-nxg-migrating-code path=addressing-placeholder-nodes.html language=enus -->
## TOPIC 00001: Addressing Placeholders to Correct Converted Code

- bundle_id: `labview-nxg-migrating-code`
- source_path: `addressing-placeholder-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-migrating-code/raw/resource/enus/addressing-placeholder-nodes.html
- document_id: `labview-nxg-migrating-code`
- page_type: `leaf`
- content_type: `task`
- source_description: Placeholders represent nodes on the diagram that existed in the original version of LabVIEW but do not exist in the converted LabVIEW NXG code. Fix placeholders in your converted code to replicate the functionality of the original source code. Evaluate the placeholder in the context of your entire a

Addressing Placeholders to Correct Converted Code

Placeholders represent nodes on the diagram that existed in the original version of LabVIEW but do not exist in the converted LabVIEW NXG code. 
 Fix placeholders in your converted code to replicate the functionality of the original source code.

Evaluate the placeholder in the context of your entire application to determine whether you need the feature the placeholder represents.

| Issue | Solution |
| --- | --- |
| The placeholder represents functionality that is not essential. | Delete the placeholder. |
| The placeholder represents functionality that is essential. | Replicate the functionality using features supported in LabVIEW NXG. If you cannot replicate the functionality using LabVIEW NXG features, consider moving the functionality into a subVI in the original version of LabVIEW and use the VI Interop node to call the subVI from your LabVIEW NXG application. Note Each time you call code from the original version of LabVIEW using the VI Interop node, the efficiency of your code decreases because the VI Interop node introduces performance overhead. Instead of using multiple VI Interop nodes to replace individual missing nodes, modularize calls to the original version of LabVIEW into as few VI Interop nodes as possible. |

If the previous steps do not resolve your code, wait to migrate your code until LabVIEW NXG can support the required functionality.

Parent topic:

Migrating LabVIEW Source Code to LabVIEW NXG

Related information:

- nihelp://node-ref/vi-interop/

<!--NI_TOPIC bundle=labview-nxg-migrating-code path=ambiguous-type-definition-name-not-supported.html language=enus -->
## TOPIC 00002: AmbiguousTypeDefinitionNameNotSupported

- bundle_id: `labview-nxg-migrating-code`
- source_path: `ambiguous-type-definition-name-not-supported.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-migrating-code/raw/resource/enus/ambiguous-type-definition-name-not-supported.html
- document_id: `labview-nxg-migrating-code`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Code Conversion Utility renamed a type definition because it found one or more type definitions with the same qualified name. The Code Conversion Utility disconnected all instances of this type definition because it could not link the instances to the appropriate G Type. What to Do Review the di

AmbiguousTypeDefinitionNameNotSupported

The 
 **Code Conversion Utility** renamed a type definition because it found one or more type definitions with the same qualified name. The 
 **Code Conversion Utility** disconnected all instances of this type definition because it could not link the instances to the appropriate G Type.

#### What to Do

Review the disconnected instances in the converted code and link them to the appropriate G Types. Alternatively, you can rename type definitions in the original source code and convert the code again. If multiple projects have type definitions with the same qualified name, convert those projects separately.

This message can also occur if references to a type definition get out of sync with the type definition. NI recommends that you mass compile your files before conversion to ensure all file references are correct.

Parent topic:

Conversion Messages

<!--NI_TOPIC bundle=labview-nxg-migrating-code path=array-to-cluster-naming-changed.html language=enus -->
## TOPIC 00003: ArrayToClusterNamingChanged

- bundle_id: `labview-nxg-migrating-code`
- source_path: `array-to-cluster-naming-changed.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-migrating-code/raw/resource/enus/array-to-cluster-naming-changed.html
- document_id: `labview-nxg-migrating-code`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Code Conversion Utility inserted a coerce to type node to preserve cluster element names after an Array to Cluster node. All cluster elements require a unique name because this version of LabVIEW NXG does not allow unnamed cluster elements. The Code Conversion Utility inserted nodes to preserve

ArrayToClusterNamingChanged

The 
 **Code Conversion Utility** inserted a coerce to type node to preserve cluster element names after an Array to Cluster node.

All cluster elements require a unique name because this version of LabVIEW NXG does not allow unnamed cluster elements. The 
 Code Conversion Utility inserted nodes to preserve the original cluster element names so that downstream nodes are correct.

#### What to Do

No action is required. However, if performance is a concern, consider removing the inserted nodes and updating downstream nodes.

Parent topic:

Conversion Messages

<!--NI_TOPIC bundle=labview-nxg-migrating-code path=byte-array-to-string-changed.html language=enus -->
## TOPIC 00004: ByteArrayToStringChanged

- bundle_id: `labview-nxg-migrating-code`
- source_path: `byte-array-to-string-changed.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-migrating-code/raw/resource/enus/byte-array-to-string-changed.html
- document_id: `labview-nxg-migrating-code`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Code Conversion Utility changed the behavior of Byte Array To String by wiring an extended ASCII encoding enum constant to try and preserve the original behavior of the application. LabVIEW NXG does not support flattening or unflattening data to a binary string because LabVIEW NXG uses UTF-8 str

ByteArrayToStringChanged

The 
 **Code Conversion Utility** changed the behavior of Byte Array To String by wiring an extended ASCII encoding enum constant to try and preserve the original behavior of the application.

LabVIEW NXG does not support flattening or unflattening data to a binary string because LabVIEW NXG uses UTF-8 string encoding. LabVIEW uses ASCII encoding, sothe 
 Code Conversion Utility automatically replaces instances of Flatten to String and Unflatten from String with Flatten to Byte Array and Unflatten from Byte Array, causing the flattened data type to change from a string to a byte array.This change may lead to broken wires on the diagram.

#### What to Do

Review flattened data types for correctness and fix any broken wires.

#### Alternate Workarounds

If the previous suggestions don't restore the functionality of the affected code and the code isn't essential to the core functionality of your application, you can remove the portion of code. If the code is part of the core functionality of the application, you can use the VI Interop node to call your existing code, provided that the new code organization meets the architectural goals of your application. If neither solution meets the requirements of your application, do not migrate to LabVIEW NXG at this time.

Parent topic:

Conversion Messages

Related information:

- VI Interop

<!--NI_TOPIC bundle=labview-nxg-migrating-code path=call-library-node-path-diagram-not-supported.html language=enus -->
## TOPIC 00005: CallLibraryNodePathOnDiagramNotSupported

- bundle_id: `labview-nxg-migrating-code`
- source_path: `call-library-node-path-diagram-not-supported.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-migrating-code/raw/resource/enus/call-library-node-path-diagram-not-supported.html
- document_id: `labview-nxg-migrating-code`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Code Conversion Utility replaced a Call Library Function Node with a placeholder node. This version of LabVIEW NXG does not support Call Library Function Nodes that call DLLs or shared libraries using the path in input. If your application uses a Call Library Function Node where you specified yo

CallLibraryNodePathOnDiagramNotSupported

The 
 **Code Conversion Utility** replaced a Call Library Function Node with a placeholder node. This version of LabVIEW NXG does not support Call Library Function Nodes that call DLLs or shared libraries using the **path in** input.

If your application uses a Call Library Function Node where you specified your path to a DLL instead of using the **path in** input, LabVIEW NXG converts the Call Library Function Node to an SLI. This version of LabVIEW NXG does not support DLLs being dynamically loaded using the **path in** input. Performance implications may occur because the DLL can no longer be dynamically loaded or unloaded.

#### What to Do

If your shared library is widely used in your application, consider updating the Call Library Function Node in LabVIEW to statically reference the DLL and then reconvert your application to LabVIEW NXG. Making this change and reconverting your application automatically generates the SLI document and correctly replaces all the Call Library Function Nodes with SLI calls. If you use your library sparingly, you can create an SLI document for the DLL and replace the placeholder with an SLI call. Creating an SLI document does not require reconverting.

#### Alternate Workarounds

If the previous suggestions don't restore the functionality of the affected code and the code isn't essential to the core functionality of your application, you can remove the portion of code. If the code is part of the core functionality of the application, you can use the VI Interop node to call your existing code, provided that the new code organization meets the architectural goals of your application. If neither solution meets the requirements of your application, do not migrate to LabVIEW NXG at this time.

Parent topic:

Conversion Messages

Related information:

- nihelp://language-integration/shared-library-interfaces/
- nihelp://migration/addressing-placeholder-nodes/
- VI Interop

<!--NI_TOPIC bundle=labview-nxg-migrating-code path=type-def-changes-not-applied.html language=enus -->
## TOPIC 00006: TypeDefinitionChangesNotApplied

- bundle_id: `labview-nxg-migrating-code`
- source_path: `type-def-changes-not-applied.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-migrating-code/raw/resource/enus/type-def-changes-not-applied.html
- document_id: `labview-nxg-migrating-code`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Code Conversion Utility did not convert a value because the value type does not match its type definition. LabVIEW NXG may not apply any changes made to the type definition for this usage. Mismatches can happen if changes were made to the type definition while the usage was not loaded. The Code

TypeDefinitionChangesNotApplied

The 
 **Code Conversion Utility** did not convert a value because the value type does not match its type definition. LabVIEW NXG may not apply any changes made to the type definition for this usage.

Mismatches can happen if changes were made to the type definition while the usage was not loaded. The 
 Code Conversion Utility replaced the stale usage with a new reference to the type definition, which can result in broken wires on the diagram.

#### What to Do

Review the type definition usage for correctness. Fix any broken wires. NI recommends that you mass compile your files before conversion to ensure all file references are correct.

Parent topic:

Conversion Messages

<!--NI_TOPIC bundle=labview-nxg-migrating-code path=type-on-node-not-supported.html language=enus -->
## TOPIC 00007: TypeOnNodeNotSupported

- bundle_id: `labview-nxg-migrating-code`
- source_path: `type-on-node-not-supported.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-migrating-code/raw/resource/enus/type-on-node-not-supported.html
- document_id: `labview-nxg-migrating-code`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Code Conversion Utility encountered a node with a data type wired to it that the node does not support in this version of LabVIEW NXG. The type cannot not be preserved. What to Do Change the node type to a supported type for the node.

TypeOnNodeNotSupported

The 
 **Code Conversion Utility** encountered a node with a data type wired to it that the node does not support in this version of LabVIEW NXG.

The type cannot not be preserved.

#### What to Do

Change the node type to a supported type for the node.

Parent topic:

Conversion Messages

<!--NI_TOPIC bundle=labview-nxg-migrating-code path=units-moved-to-annotations.html language=enus -->
## TOPIC 00008: UnitsMovedToAnnotations

- bundle_id: `labview-nxg-migrating-code`
- source_path: `units-moved-to-annotations.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-migrating-code/raw/resource/enus/units-moved-to-annotations.html
- document_id: `labview-nxg-migrating-code`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Code Conversion Utility moved the units on the control to the Annotation field located in the Item tab. This version of LabVIEW NXG does not support units. In LabVIEW, you could set controls to have specific units, and wires propagated that unit. This version of LabVIEW NXG does not support sett

UnitsMovedToAnnotations

The 
 **Code Conversion Utility** moved the units on the control to the 
 Annotation field located in the 
 **Item** tab. This version of LabVIEW NXG does not support units.

In LabVIEW, you could set controls to have specific units, and wires propagated that unit. This version of LabVIEW NXG does not support setting controls to have specific units, but the units associated with each control are preserved as annotations.

#### What to Do

No action required.

Parent topic:

Conversion Messages

<!--NI_TOPIC bundle=labview-nxg-migrating-code path=value-type-not-supported.html language=enus -->
## TOPIC 00009: ValueOfTypeNotSupported

- bundle_id: `labview-nxg-migrating-code`
- source_path: `value-type-not-supported.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-migrating-code/raw/resource/enus/value-type-not-supported.html
- document_id: `labview-nxg-migrating-code`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Code Conversion Utility was unable to convert a value of the specified type because the data type of the value is not supported in this version of LabVIEW NXG. The Code Conversion Utility replaced the unsupported type with a generic reference. This change may cause broken wires on the diagram. W

ValueOfTypeNotSupported

The 
 **Code Conversion Utility** was unable to convert a value of the specified type because the data type of the value is not supported in this version of LabVIEW NXG.

The 
 Code Conversion Utility replaced the unsupported type with a generic reference. This change may cause broken wires on the diagram.

#### What to Do

Review the diagram for broken wires. If you identify broken wires on the diagram caused by this change, determine if there is a supported type that can replace the unsupported type.

#### Alternate Workarounds

If the previous suggestions don't restore the functionality of the affected code and the code isn't essential to the core functionality of your application, you can remove the portion of code. If the code is part of the core functionality of the application, you can use the VI Interop node to call your existing code, provided that the new code organization meets the architectural goals of your application. If neither solution meets the requirements of your application, do not migrate to LabVIEW NXG at this time.

Parent topic:

Conversion Messages

Related information:

- VI Interop
