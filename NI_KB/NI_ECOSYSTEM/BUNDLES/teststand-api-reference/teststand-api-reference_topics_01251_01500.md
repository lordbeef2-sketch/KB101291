# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=1251 end=1500 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-checkremotesystemstatus.html language=enus -->
## TOPIC 01251: LabVIEWAdapter.CheckRemoteSystemStatus

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-checkremotesystemstatus.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-checkremotesystemstatus.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.CheckRemoteSystemStatus( targetIPAddress, portNumber, timeout, statusMessage) Return Value Boolean Purpose Returns a value that indicates whether a remote system is running LabVIEW and allows TestStand to connect to it. This is particularly useful on a real-time system. Paramet

### LabVIEWAdapter.CheckRemoteSystemStatus

#### Syntax

[LabVIEWAdapter](labviewadapter.html).CheckRemoteSystemStatus( targetIPAddress, portNumber, timeout, statusMessage)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether a remote system is running LabVIEW and allows TestStand to connect to it. This is particularly useful on a real-time system.

#### Parameters

targetIPAddress
 As
 [String](data-types-for-teststand.html)

[In] Specifies the remote computer. Leave this option empty to use the local computer.

portNumber
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the TCP/IP port number to use to connect to the remote system.

timeout
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the time, in milliseconds, to wait for a connection before timing out. A value of
 -1
 indicates to wait indefinitely.

statusMessage
 As
 [String](data-types-for-teststand.html)

[Out] Returns any error messages generated while checking system status.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-clearbuildandexecutecache.html language=enus -->
## TOPIC 01252: LabVIEWAdapter.ClearBuildAndExecuteCache

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-clearbuildandexecutecache.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-clearbuildandexecutecache.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.ClearBuildAndExecuteCache( clearAllFiles, sequenceFile) Purpose Clears the 'Build Source Files and Execute' cache. The cache maintains data per sequence file. This method will either clear the entire cache or the data for the sequence file specified in the sequenceFile paramete

### LabVIEWAdapter.ClearBuildAndExecuteCache

#### Syntax

[LabVIEWAdapter](labviewadapter.html).ClearBuildAndExecuteCache( clearAllFiles, sequenceFile)

#### Purpose

Clears the 'Build Source Files and Execute' cache. The cache maintains data per sequence file. This method will either clear the entire cache or the data for the sequence file specified in the sequenceFile parameter.

#### Remarks

If the data for a sequence file is cleared from the cache, the next execution of the file will force a fresh build of the Packed Project Libraries (PPLs) containing all the VIs called from that sequence file.

Use this method to recover from/reset errors or force a rebuild of the PPLs for a sequence file. Forcing a rebuild would remove any VIs called from steps that were skipped/deleted from the sequence file, in the generated PPL.

#### Parameters

clearAllFiles
 As
 [Boolean](data-types-for-teststand.html)

[In] Passing true clears the cache for all sequence files that were previously executed. If false, then the cache is cleared only for the sequence file specified in the sequenceFile parameter.

sequenceFile
 As
 
 [SequenceFile](sequencefile.html)

[In] Reference to the sequence file for which the entry in the cache should be cleared.

#### See Also

[Build Source Files and Execute](/csh?context=ts_tsref_build_and_execute)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-codetemplatepolicy.html language=enus -->
## TOPIC 01253: LabVIEWAdapter.CodeTemplatePolicy

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-codetemplatepolicy.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-codetemplatepolicy.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.CodeTemplatePolicy Data Type AdapterCodeTemplatePolicies Use the following constants with this data type: AdapterCodeTemplatePolicy_UseNewAndLegacy –(Value: 2) Specifies that the adapter searches for new and legacy code templates. AdapterCodeTemplatePolicy_UseOnlyLegacy –(Value

### LabVIEWAdapter.CodeTemplatePolicy

#### Syntax

[LabVIEWAdapter](labviewadapter.html).CodeTemplatePolicy

#### Data Type

[AdapterCodeTemplatePolicies](adaptercodetemplatepolicies.html)

Use the following constants with this data type:

- AdapterCodeTemplatePolicy_UseNewAndLegacy 
 –(Value: 2) Specifies that the adapter searches for new and legacy code templates.
- AdapterCodeTemplatePolicy_UseOnlyLegacy 
 –(Value: 1) Specifies that the adapter only searches for legacy code templates.
- AdapterCodeTemplatePolicy_UseOnlyNew 
 –(Value: 0) Specifies that the adapter only searches for new code templates.

#### Purpose

Specifies which code templates to use during code creation.
 [Policies to choose from](adaptercodetemplatepolicies.html)
 include using new templates, using legacy templates, or using both new and legacy templates.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-currentlabviewserverversion.html language=enus -->
## TOPIC 01254: LabVIEWAdapter.CurrentLabVIEWServerVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-currentlabviewserverversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-currentlabviewserverversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.CurrentLabVIEWServerVersion Data Type String Purpose Returns the version of the LabVIEW server that TestStand is using to run VIs. The version contains only the major and minor version numbers, such as "8.0". Returns AutoDetect when you select the Autodetect using VI version op

### LabVIEWAdapter.CurrentLabVIEWServerVersion

#### Syntax

[LabVIEWAdapter](labviewadapter.html).CurrentLabVIEWServerVersion

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the version of the LabVIEW server that TestStand is using to run VIs. The version contains only the major and minor version numbers, such as "8.0". Returns
 AutoDetect
 when you select the
 Autodetect using VI version
 option in the Select or Type Which LabVIEW Server to Use section of the
 [LabVIEW Adapter Configuration](../tsref/labview-adapter-configuration-dialog-box.html)
 dialog box.

#### Remarks

A LabVIEW server includes a LabVIEW Development Environment, a LabVIEW-created executable that exports the LabVIEW ActiveX Automation server interface, or a LabVIEW Run-Time Engine.

#### See Also

[LabVIEWAdapter.IsCurrentLabVIEWServerAnEditor](labviewadapter-iscurrentlabviewserveraneditor.html)

[LabVIEW Adapter Configuration dialog box](../tsref/labview-adapter-configuration-dialog-box.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-deployprojectlibrary.html language=enus -->
## TOPIC 01255: LabVIEWAdapter.DeployProjectLibrary

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-deployprojectlibrary.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-deployprojectlibrary.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.DeployProjectLibrary( targetIPAddress, libraryPath, options = DeployProjectLibraryOption_Deploy) Purpose Deploys or undeploys the shared variables defined in a LabVIEW project library file to the specified remote computer. Remarks TestStand can deploy a shared variable bound to

### LabVIEWAdapter.DeployProjectLibrary

#### Syntax

[LabVIEWAdapter](labviewadapter.html).DeployProjectLibrary( targetIPAddress, libraryPath, options = DeployProjectLibraryOption_Deploy)

#### Purpose

Deploys or undeploys the shared variables defined in a LabVIEW project library file to the specified remote computer.

#### Remarks

TestStand can deploy a shared variable bound to another shared variable only when you use an NI Publish-Subscribe Protocol (NI-PSP) URL to bind the shared variable to deploy to another shared variable. If you attempt to use a Deploy Library step to deploy a shared variable to a variable in a LabVIEW project, the deployment fails. Refer to the
 LabVIEW Help
 for more information about deploying shared variables and NI-PSP URLs.

#### Parameters

targetIPAddress
 As
 [String](data-types-for-teststand.html)

[In] Specifies the remote computer. Leave this option empty to use the local computer.

libraryPath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the path to the project library file on the local computer to deploy or undeploy.

Note

options
 As
 [DeployProjectLibraryOptions](deployprojectlibraryoptions.html)

[In] Specifies whether to deploy or undeploy the LabVIEW project library file.

This parameter has a default value of
 DeployProjectLibraryOption_Deploy
 .

#### See Also

[Deploying Network-Published Shared Variables](/csh?context=ts_tslabview_variable)

[DeployProjectLibraryOptions](deployprojectlibraryoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-displayhelpfornodeproperty.html language=enus -->
## TOPIC 01256: LabVIEWAdapter.DisplayHelpForNodeProperty

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-displayhelpfornodeproperty.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-displayhelpfornodeproperty.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.DisplayHelpForNodeProperty( libraryName, genericType, classDataName, propertyDataName, propertyUniqueID) Purpose Launches the LabVIEW Help topic for the property. Parameters libraryName As String [In] Specifies the name of the LabVIEW node library you select. genericType As Str

### LabVIEWAdapter.DisplayHelpForNodeProperty

#### Syntax

[LabVIEWAdapter](labviewadapter.html).DisplayHelpForNodeProperty( libraryName, genericType, classDataName, propertyDataName, propertyUniqueID)

#### Purpose

Launches the
 LabVIEW Help
 topic for the property.

#### Parameters

libraryName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the LabVIEW node library you select.

genericType
 As
 [String](data-types-for-teststand.html)

[In] Specifies the genericType of the LabVIEW node library you select.

classDataName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the Class Data Name of the LabVIEW node property.

propertyDataName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the Property Data Name of the LabVIEW node property.

propertyUniqueID
 As
 [String](data-types-for-teststand.html)

[In] Specifies the unique ID of the LabVIEW node property.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-enablertedebuggingandtracing.html language=enus -->
## TOPIC 01257: LabVIEWAdapter.EnableRTEDebuggingAndTracing

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-enablertedebuggingandtracing.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-enablertedebuggingandtracing.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.EnableRTEDebuggingAndTracing Data Type Boolean Purpose Specifies whether LabVIEW Runtime engine (RTE) support for debugging and tracing is enabled. Remarks Changes to this property do not take effect until you restart the TestStand engine.

### LabVIEWAdapter.EnableRTEDebuggingAndTracing

#### Syntax

[LabVIEWAdapter](labviewadapter.html).EnableRTEDebuggingAndTracing

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether LabVIEW Runtime engine (RTE) support for debugging and tracing is enabled.

#### Remarks

Changes to this property do not take effect until you restart the TestStand engine.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-enableversionindependentruntim.html language=enus -->
## TOPIC 01258: LabVIEWAdapter.EnableVersionIndependentRuntime

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-enableversionindependentruntim.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-enableversionindependentruntim.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.EnableVersionIndependentRuntime Data Type Boolean Purpose Specifies whether Version Independent Runtime Engine support is enabled in the LabVIEW Adapter. Remarks This option applies to all instances of LabVIEW development environments and LabVIEW runtimes, version 2017 or later

### LabVIEWAdapter.EnableVersionIndependentRuntime

#### Syntax

[LabVIEWAdapter](labviewadapter.html).EnableVersionIndependentRuntime

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether Version Independent Runtime Engine support is enabled in the LabVIEW Adapter.

#### Remarks

This option applies to all instances of LabVIEW development environments and LabVIEW runtimes, version 2017 or later, that are used by the TestStand application.

Note

Note

#### See Also

[Version Independent Runtime Engine Support](/csh?context=ts_tsref_vire_support)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-enableversionindependentruntim_2.html language=enus -->
## TOPIC 01259: LabVIEWAdapter.EnableVersionIndependentRuntime

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-enableversionindependentruntim_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-enableversionindependentruntim_2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.EnableVersionIndependentRuntime Data Type Boolean Purpose Specifies whether Version Independent Runtime Engine support is enabled in the LabVIEW Adapter. Remarks This option applies to all instances of LabVIEW development environments and LabVIEW runtimes, version 2017 or later

### LabVIEWAdapter.EnableVersionIndependentRuntime

#### Syntax

[LabVIEWAdapter](labviewadapter.html).EnableVersionIndependentRuntime

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether Version Independent Runtime Engine support is enabled in the LabVIEW Adapter.

#### Remarks

This option applies to all instances of LabVIEW development environments and LabVIEW runtimes, version 2017 or later, that are used by the TestStand application.

Note

Note

#### See Also

[Version Independent Runtime Engine Support](/csh?context=ts_tsref_vire_support)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-fileexistsinllb.html language=enus -->
## TOPIC 01260: LabVIEWAdapter.FileExistsInLLB

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-fileexistsinllb.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-fileexistsinllb.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.FileExistsInLLB( path) Return Value Boolean Purpose Returns a value that indicates whether the given file exists in an LLB file. Remarks The Engine.FindFileEx method does not search LLB files. Use this method whenever Engine.FindFileEx fails to find a VI. Parameters path As Str

### LabVIEWAdapter.FileExistsInLLB

#### Syntax

[LabVIEWAdapter](labviewadapter.html).FileExistsInLLB( path)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the given file exists in an LLB file.

#### Remarks

The
 [Engine.FindFileEx](engine-findfileex.html)
 method does not search LLB files. Use this method whenever
 Engine.FindFileEx
 fails to find a VI.

#### Parameters

path
 As
 [String](data-types-for-teststand.html)

[In] Specifies a string containing the absolute pathname of the VI in the LLB file.

#### See Also

[Engine.FindFileEx](engine-findfileex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-getclassesfornodelibrary.html language=enus -->
## TOPIC 01261: LabVIEWAdapter.GetClassesForNodeLibrary

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-getclassesfornodelibrary.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-getclassesfornodelibrary.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.GetClassesForNodeLibrary( libraryName, genericType, longNames, dataNames) Purpose Returns arrays that contain the long names and data names of the classes defined by the LabVIEW node library you specify. Parameters libraryName As String [In] Specifies the name of the LabVIEW no

### LabVIEWAdapter.GetClassesForNodeLibrary

#### Syntax

[LabVIEWAdapter](labviewadapter.html).GetClassesForNodeLibrary( libraryName, genericType, longNames, dataNames)

#### Purpose

Returns arrays that contain the long names and data names of the classes defined by the LabVIEW node library you specify.

#### Parameters

libraryName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the LabVIEW node library you select.

genericType
 As
 [String](data-types-for-teststand.html)

[In] Specifies the genericType of the LabVIEW node library you select.

longNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the LongNames of the available properties for the LabVIEW node library class you select.

dataNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the DataNames of the available properties of the LabVIEW node library class you select.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-getclustermemberisbinarystring.html language=enus -->
## TOPIC 01262: LabVIEWAdapter.GetClusterMemberIsBinaryString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-getclustermemberisbinarystring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-getclustermemberisbinarystring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.GetClusterMemberIsBinaryString( typeDefinition, propertyLookupString) Return Value Boolean Purpose Returns True if the cluster member that corresponds to the specified type definition property contains binary data. Remarks TestStand preserves NUL bytes when setting and getting

### LabVIEWAdapter.GetClusterMemberIsBinaryString

#### Syntax

[LabVIEWAdapter](labviewadapter.html).GetClusterMemberIsBinaryString( typeDefinition, propertyLookupString)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the cluster member that corresponds to the specified type definition property contains binary data.

#### Remarks

TestStand preserves NUL bytes when setting and getting LabVIEW string data for binary strings.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

#### See Also

[LabVIEWAdapter.GetClusterPassingEnabled](labviewadapter-getclusterpassingenabled.html)

[LabVIEWAdapter.SetClusterMemberIsBinaryString](labviewadapter-setclustermemberisbinarystring.html)

[LabVIEWParameter.PassAsBinaryString](labviewparameter-passasbinarystring.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-getclustermemberlabel.html language=enus -->
## TOPIC 01263: LabVIEWAdapter.GetClusterMemberLabel

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-getclustermemberlabel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-getclustermemberlabel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.GetClusterMemberLabel( typeDefinition, propertyLookupString) Return Value String Purpose Returns the label of the cluster member that corresponds to the specified type definition property. Parameters typeDefinition As PropertyObject [In] Specifies the type definition. This meth

### LabVIEWAdapter.GetClusterMemberLabel

#### Syntax

[LabVIEWAdapter](labviewadapter.html).GetClusterMemberLabel( typeDefinition, propertyLookupString)

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns the label of the cluster member that corresponds to the specified type definition property.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the type definition.

#### See Also

[LabVIEWAdapter.GetClusterPassingEnabled](labviewadapter-getclusterpassingenabled.html)

[LabVIEWAdapter.SetClusterMemberLabel](labviewadapter-setclustermemberlabel.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-getclusterpassingenabled.html language=enus -->
## TOPIC 01264: LabVIEWAdapter.GetClusterPassingEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-getclusterpassingenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-getclusterpassingenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.GetClusterPassingEnabled( typeDefinition) Return Value Boolean Purpose Returns a value that indicates whether a type definition allows the LabVIEW Adapter to pass instances of the type as cluster parameters to VIs. Parameters typeDefinition As PropertyObject [In] Specifies the

### LabVIEWAdapter.GetClusterPassingEnabled

#### Syntax

[LabVIEWAdapter](labviewadapter.html).GetClusterPassingEnabled( typeDefinition)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether a type definition allows the LabVIEW Adapter to pass instances of the type as cluster parameters to VIs.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

#### See Also

[LabVIEWAdapter.SetClusterPassingEnabled](labviewadapter-setclusterpassingenabled.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-getexcludefromcluster.html language=enus -->
## TOPIC 01265: LabVIEWAdapter.GetExcludeFromCluster

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-getexcludefromcluster.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-getexcludefromcluster.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.GetExcludeFromCluster( typeDefinition, propertyLookupString) Return Value Boolean Purpose Returns a value that indicates whether the specified type definition property is excluded when converting instances of the type definition into clusters to pass as parameters to VIs. Param

### LabVIEWAdapter.GetExcludeFromCluster

#### Syntax

[LabVIEWAdapter](labviewadapter.html).GetExcludeFromCluster( typeDefinition, propertyLookupString)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the specified type definition property is excluded when converting instances of the type definition into clusters to pass as parameters to VIs.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

#### See Also

[LabVIEWAdapter.GetClusterPassingEnabled](labviewadapter-getclusterpassingenabled.html)

[LabVIEWAdapter.SetExcludeFromCluster](labviewadapter-setexcludefromcluster.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-getexpressvimenustructure.html language=enus -->
## TOPIC 01266: LabVIEWAdapter.GetExpressVIMenuStructure

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-getexpressvimenustructure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-getexpressvimenustructure.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.GetExpressVIMenuStructure( refreshMenu, parentHWnd = 0) Return Value PropertyObject Purpose Returns a PropertyObject array that specifies the structure of the Express VI menu TestStand uses to select an Express VI. Remarks TestStand uses this method to create the context menu t

### LabVIEWAdapter.GetExpressVIMenuStructure

#### Syntax

[LabVIEWAdapter](labviewadapter.html).GetExpressVIMenuStructure( refreshMenu, parentHWnd = 0)

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns a PropertyObject array that specifies the structure of the Express VI menu TestStand uses to select an Express VI.

#### Remarks

TestStand uses this method to create the context menu that becomes visible when you browse for an Express VI in the LabVIEW Module pane. Each element of the array is a PropertyObject container with
 [subproperties](expressvimenuitemproperties.html)
 that specify the menu name, the path to the Express VI, and the icon for the menu.

#### Parameters

refreshMenu
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether to force TestStand to rebuild the Express VI menu. TestStand caches the menu and only rebuilds the menu when you configure the LabVIEW Adapter to use a different LabVIEW version. TestStand does not automatically refresh the menu when you select a different function palette view in LabVIEW.

parentHWnd
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the parent window handle TestStand uses for the progress window the method might display.

This parameter has a default value of
 0
 .

#### See Also

[ExpressVIMenuItemProperties](expressvimenuitemproperties.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-getmembernames.html language=enus -->
## TOPIC 01267: LabVIEWAdapter.GetMemberNames

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-getmembernames.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-getmembernames.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.GetMemberNames( projectAbsolutePath, classAbsolutePath) Return Value String Array Purpose Returns an array that contains the names for each public member VI found in the specified LabVIEW class. Parameters projectAbsolutePath As String [In] Specifies the absolute path of the La

### LabVIEWAdapter.GetMemberNames

#### Syntax

[LabVIEWAdapter](labviewadapter.html).GetMemberNames( projectAbsolutePath, classAbsolutePath)

#### Return Value

[String Array](data-types-for-teststand.html)

#### Purpose

Returns an array that contains the names for each public member VI found in the specified LabVIEW class.

#### Parameters

projectAbsolutePath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute path of the LabVIEW project. Pass an empty string if no project exists.

classAbsolutePath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute path of the LabVIEW class.

#### See Also

[LabVIEWModule.ClassPath](labviewmodule-classpath.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-getnodelibraries.html language=enus -->
## TOPIC 01268: LabVIEWAdapter.GetNodeLibraries

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-getnodelibraries.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-getnodelibraries.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.GetNodeLibraries( libraryNames, genericTypes, genericTypeNames) Purpose Returns arrays that contain the names, genericTypes, and genericTypeNames for all available LabVIEW node libraries. Parameters libraryNames As String Array [Out] Specifies the names of the available LabVIEW

### LabVIEWAdapter.GetNodeLibraries

#### Syntax

[LabVIEWAdapter](labviewadapter.html).GetNodeLibraries( libraryNames, genericTypes, genericTypeNames)

#### Purpose

Returns arrays that contain the names, genericTypes, and genericTypeNames for all available LabVIEW node libraries.

#### Parameters

libraryNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the names of the available LabVIEW node libraries.

genericTypes
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the genericTypes of the available LabVIEW node libraries.

genericTypeNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the genericTypeNames of the available LabVIEW node libraries.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-getpropertiesforlabviewclass.html language=enus -->
## TOPIC 01269: LabVIEWAdapter.GetPropertiesForLabVIEWClass

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-getpropertiesforlabviewclass.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-getpropertiesforlabviewclass.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.GetPropertiesForLabVIEWClass( libraryName, genericType, projectAbsolutePath, classAbsolutePath, classLongName, classDataName, longNames, shortNames, dataNames, uniqueIDs, helpDescriptions, options) Purpose Returns arrays that contain information about the properties of the LabV

### LabVIEWAdapter.GetPropertiesForLabVIEWClass

#### Syntax

[LabVIEWAdapter](labviewadapter.html).GetPropertiesForLabVIEWClass( libraryName, genericType, projectAbsolutePath, classAbsolutePath, classLongName, classDataName, longNames, shortNames, dataNames, uniqueIDs, helpDescriptions, options)

#### Purpose

Returns arrays that contain information about the properties of the LabVIEW node class you select, such as LongName, ShortName, DataName, HelpDescription, and options.

#### Parameters

libraryName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the LabVIEW node library you select.

genericType
 As
 [String](data-types-for-teststand.html)

[In] Specifies the genericType of the LabVIEW node library you select.

projectAbsolutePath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute path of the LabVIEW project. Pass an empty string if no LabVIEW project exists.

classAbsolutePath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute path of the LabVIEW node class you select.

classLongName
 As
 [String](data-types-for-teststand.html)

[Out] Specifies the LongName of the LabVIEW node class you select.

classDataName
 As
 [String](data-types-for-teststand.html)

[Out] Specifies the DataName of the LabVIEW node library class you select.

longNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the LongNames of the available properties for the LabVIEW node library class you select.

shortNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the ShortNames of the available properties of the LabVIEW node library class you select.

dataNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the DataNames of the available properties of the LabVIEW node library class you select.

uniqueIDs
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the unique IDs of the available properties for the LabVIEW node library class you select.

helpDescriptions
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the help descriptions of the available properties of the LabVIEW node library class you select.

options
 As
 [Long Array](data-types-for-teststand.html)

[Out] Specifies the options for the available properties of the LabVIEW node library class you select.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-getpropertiesfornodeclass.html language=enus -->
## TOPIC 01270: LabVIEWAdapter.GetPropertiesForNodeClass

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-getpropertiesfornodeclass.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-getpropertiesfornodeclass.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.GetPropertiesForNodeClass( libraryName, genericType, classDataName, longNames, shortNames, dataNames, uniqueIDs, helpDescriptions, options) Purpose Returns arrays that contain information about the properties of the LabVIEW node library class you select, such as LongName, Short

### LabVIEWAdapter.GetPropertiesForNodeClass

#### Syntax

[LabVIEWAdapter](labviewadapter.html).GetPropertiesForNodeClass( libraryName, genericType, classDataName, longNames, shortNames, dataNames, uniqueIDs, helpDescriptions, options)

#### Purpose

Returns arrays that contain information about the properties of the LabVIEW node library class you select, such as LongName, ShortName, DataName, HelpDescription, and options.

#### Parameters

libraryName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the LabVIEW node library you select.

genericType
 As
 [String](data-types-for-teststand.html)

[In] Specifies the genericType of the LabVIEW node library you select.

classDataName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the DataName of the LabVIEW node library class you select.

longNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the LongNames of the available properties for the LabVIEW node library class you select.

shortNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the ShortNames of the available properties of the LabVIEW node library class you select.

dataNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the DataNames of the available properties of the LabVIEW node library class you select.

uniqueIDs
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the unique IDs of the available properties for the LabVIEW node library class you select.

helpDescriptions
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the help descriptions of the available properties of the LabVIEW node library class you select.

options
 As
 [Long Array](data-types-for-teststand.html)

[Out] Specifies the options for the available properties of the LabVIEW node library class you select.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-getserverinfo.html language=enus -->
## TOPIC 01271: LabVIEWAdapter.GetServerInfo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-getserverinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-getserverinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.GetServerInfo( serverType, serverInformation) Purpose Returns information about the LabVIEW server that the LabVIEW Adapter is currently configured to use for running VIs. Returns AutoDetect when you select the Autodetect using VI version option in the Select or Type Which LabV

### LabVIEWAdapter.GetServerInfo

#### Syntax

[LabVIEWAdapter](labviewadapter.html).GetServerInfo( serverType, serverInformation)

#### Purpose

Returns information about the LabVIEW server that the LabVIEW Adapter is currently configured to use for running VIs. Returns
 AutoDetect
 when you select the
 Autodetect using VI version
 option in the Select or Type Which LabVIEW Server to Use section of the
 [LabVIEW Adapter Configuration](../tsref/labview-adapter-configuration-dialog-box.html)
 dialog box.

#### Remarks

The LabVIEW Adapter uses a LabVIEW ActiveX Automation server or a LabVIEW Run-Time Engine.

#### Parameters

serverType
 As
 [LabVIEWServerTypes](labviewservertypes.html)

[Out] Returns the LabVIEW server that the LabVIEW Adapter currently uses.

- "LabVIEW" - TestStand is using the active version of LabVIEW.
- - The progID for a LabVIEW ActiveX server.
- - The path to a LabVIEW Runtime (
 lvrt.dll 
 ).
- - "AutoDetect" - TestStand is using the LabVIEW Runtime that corresponds to the saved version of a VI.

serverInformation
 As
 [String](data-types-for-teststand.html)

[Out] Returns the progID of the LabVIEW ActiveX server or the path of the LabVIEW Run-Time Engine that the adapter is currently using.

#### See Also

[LabVIEW Adapter Configuration dialog box](../tsref/labview-adapter-configuration-dialog-box.html)

[LabVIEWAdapter.SetServerInfo](labviewadapter-setserverinfo.html)

[LabVIEWServerTypes](labviewservertypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-getvinamespace.html language=enus -->
## TOPIC 01272: LabVIEWAdapter.GetVINamespace

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-getvinamespace.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-getvinamespace.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.GetVINamespace( path) Return Value String Purpose Returns the LabVIEW namespace of the specified VI. The namespace of the VI is the qualified name of the owning LabVIEW project library. Remarks This method requires the LabVIEW 2012 Run-Time Engine or later to be installed. Othe

### LabVIEWAdapter.GetVINamespace

#### Syntax

[LabVIEWAdapter](labviewadapter.html).GetVINamespace( path)

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns the LabVIEW namespace of the specified VI. The namespace of the VI is the qualified name of the owning LabVIEW project library.

#### Remarks

This method requires the LabVIEW 2012 Run-Time Engine or later to be installed. Otherwise, the method returns an empty string.

#### Parameters

path
 As
 [String](data-types-for-teststand.html)

[In] Specifies a string that contains the absolute pathname of a VI.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-getviversion.html language=enus -->
## TOPIC 01273: LabVIEWAdapter.GetVIVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-getviversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-getviversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.GetVIVersion( path) Return Value String Purpose Returns the LabVIEW version that saved the specified VI. The version contains only the major and minor version numbers, such as "8.2". Parameters path As String [In] Specifies a string containing the absolute pathname of a VI.

### LabVIEWAdapter.GetVIVersion

#### Syntax

[LabVIEWAdapter](labviewadapter.html).GetVIVersion( path)

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns the LabVIEW version that saved the specified VI. The version contains only the major and minor version numbers, such as "8.2".

#### Parameters

path
 As
 [String](data-types-for-teststand.html)

[In] Specifies a string containing the absolute pathname of a VI.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-initialize.html language=enus -->
## TOPIC 01274: LabVIEWAdapter.Initialize

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-initialize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-initialize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.Initialize Purpose Initializes the LabVIEW Adapter by connecting to the configured LabVIEW server. Remarks If you do not call this method, the LabVIEW Adapter connects to the configured LabVIEW server when first needed.

### LabVIEWAdapter.Initialize

#### Syntax

[LabVIEWAdapter](labviewadapter.html).Initialize

#### Purpose

Initializes the LabVIEW Adapter by connecting to the configured LabVIEW server.

#### Remarks

If you do not call this method, the LabVIEW Adapter connects to the configured LabVIEW server when first needed.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-isbuildandexecuteenabled.html language=enus -->
## TOPIC 01275: LabVIEWAdapter.IsBuildAndExecuteEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-isbuildandexecuteenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-isbuildandexecuteenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.IsBuildAndExecuteEnabled( options, reasonDisabled) Return Value Boolean Purpose Returns a value that indicates whether the 'Build Source Files and Execute' feature is enabled. Parameters options As Long [In] Currently unused. Pass 0 which is the default value reasonDisabled As

### LabVIEWAdapter.IsBuildAndExecuteEnabled

#### Syntax

[LabVIEWAdapter](labviewadapter.html).IsBuildAndExecuteEnabled( options, reasonDisabled)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the 'Build Source Files and Execute' feature is enabled.

#### Parameters

options
 As
 [Long](data-types-for-teststand.html)

[In] Currently unused. Pass 0 which is the default value

reasonDisabled
 As
 [String](data-types-for-teststand.html)

[Out] If the feature is disabled, this string parameter describes the reason why.

#### See Also

[Build Source Files and Execute](/csh?context=ts_tsref_build_and_execute)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-iscurrentlabviewserveraneditor.html language=enus -->
## TOPIC 01276: LabVIEWAdapter.IsCurrentLabVIEWServerAnEditor

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-iscurrentlabviewserveraneditor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-iscurrentlabviewserveraneditor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.IsCurrentLabVIEWServerAnEditor Data Type Boolean Purpose Returns a value that indicates whether the LabVIEW server TestStand is using to run VIs can edit VIs. Remarks A LabVIEW server includes a LabVIEW Development Environment, a LabVIEW-created executable that exports the LabV

### LabVIEWAdapter.IsCurrentLabVIEWServerAnEditor

#### Syntax

[LabVIEWAdapter](labviewadapter.html).IsCurrentLabVIEWServerAnEditor

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the LabVIEW server TestStand is using to run VIs can edit VIs.

#### Remarks

A LabVIEW server includes a LabVIEW Development Environment, a LabVIEW-created executable that exports the LabVIEW ActiveX Automation server interface, or a LabVIEW Run-Time Engine.

#### See Also

[LabVIEWAdapter.CurrentLabVIEWServerVersion](labviewadapter-currentlabviewserverversion.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-isexpressvi.html language=enus -->
## TOPIC 01277: LabVIEWAdapter.IsExpressVI

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-isexpressvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-isexpressvi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.IsExpressVI( path, displayVIName) Return Value Boolean Purpose Returns a value that indicates whether the specified VI is an Express VI. Remarks Use the absolute path to the Express VI. Parameters path As String [In] Specifies a string containing the absolute pathname of a VI.

### LabVIEWAdapter.IsExpressVI

#### Syntax

[LabVIEWAdapter](labviewadapter.html).IsExpressVI( path, displayVIName)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the specified VI is an Express VI.

#### Remarks

Use the absolute path to the Express VI.

#### Parameters

path
 As
 [String](data-types-for-teststand.html)

[In] Specifies a string containing the absolute pathname of a VI.

displayVIName
 As
 [String](data-types-for-teststand.html)

[Out] Returns the display name of the Express VI. If the VI is not an Express VI, the method returns an empty string.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-islabviewactivexserverconnecti.html language=enus -->
## TOPIC 01278: LabVIEWAdapter.IsLabVIEWActiveXServerConnectionValid

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-islabviewactivexserverconnecti.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-islabviewactivexserverconnecti.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.IsLabVIEWActiveXServerConnectionValid Data Type Boolean Purpose Returns a value that indicates whether the LabVIEW ActiveX server connection TestStand is using is valid. See Also LabVIEWAdapter.CurrentLabVIEWServerVersion LabVIEWAdapter.IsCurrentLabVIEWServerAnEditor

### LabVIEWAdapter.IsLabVIEWActiveXServerConnectionValid

#### Syntax

[LabVIEWAdapter](labviewadapter.html).IsLabVIEWActiveXServerConnectionValid

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the LabVIEW ActiveX server connection TestStand is using is valid.

#### See Also

[LabVIEWAdapter.CurrentLabVIEWServerVersion](labviewadapter-currentlabviewserverversion.html)

[LabVIEWAdapter.IsCurrentLabVIEWServerAnEditor](labviewadapter-iscurrentlabviewserveraneditor.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-issupportedlabviewdevelopments.html language=enus -->
## TOPIC 01279: LabVIEWAdapter.IsSupportedLabVIEWDevelopmentSystemInstalled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-issupportedlabviewdevelopments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-issupportedlabviewdevelopments.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.IsSupportedLabVIEWDevelopmentSystemInstalled Data Type Boolean Purpose Returns True if any supported version of the LabVIEW Development System is installed on the machine.

### LabVIEWAdapter.IsSupportedLabVIEWDevelopmentSystemInstalled

#### Syntax

[LabVIEWAdapter](labviewadapter.html).IsSupportedLabVIEWDevelopmentSystemInstalled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if any supported version of the LabVIEW Development System is installed on the machine.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-labviewdevelopmentenvironmentb.html language=enus -->
## TOPIC 01280: LabVIEWAdapter.LabVIEWDevelopmentEnvironmentBitness

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-labviewdevelopmentenvironmentb.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-labviewdevelopmentenvironmentb.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.LabVIEWDevelopmentEnvironmentBitness Data Type LabVIEWDevelopmentEnvironmentBitnessOptions Use the following constants with this data type: LVDevelopmentEnvironmentBitness_32bit –(Value: 1) Launches the current active 32-bit LabVIEW development environment. LVDevelopmentEnviron

### LabVIEWAdapter.LabVIEWDevelopmentEnvironmentBitness

#### Syntax

[LabVIEWAdapter](labviewadapter.html).LabVIEWDevelopmentEnvironmentBitness

#### Data Type

[LabVIEWDevelopmentEnvironmentBitnessOptions](labviewdevelopmentenvironmentbitnessoptions.html)

Use the following constants with this data type:

- LVDevelopmentEnvironmentBitness_32bit 
 –(Value: 1) Launches the current active 32-bit LabVIEW development environment.
- LVDevelopmentEnvironmentBitness_64bit 
 –(Value: 2) Launches the current active 64-bit LabVIEW development environment.
- LVDevelopmentEnvironmentBitness_Default 
 –(Value: 0) Launches the current active 32-bit or 64-bit LabVIEW development environment, with a preference to match the bitness of TestStand.

#### Purpose

Specifies the bitness of the LabVIEW development environment version to use. Options include the current active 32-bit or 64-bit LabVIEW development environment, only the current active 32-bit LabVIEW development environment, or only the current active 64-bit LabVIEW development environment.

#### See Also

[LabVIEW Adapter Configuration Dialog Box](../tsref/labview-adapter-configuration-dialog-box.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-newmodule.html language=enus -->
## TOPIC 01281: LabVIEWAdapter.NewModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-newmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-newmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.NewModule Return Value LabVIEWModule Purpose Creates and returns a new LabVIEWModule object. Use this method to create a LabVIEWModule object that you can use to execute a LabVIEW VI without using a step, sequence, or execution. See Also LabVIEWModule LabVIEWModule.Execute LabV

### LabVIEWAdapter.NewModule

#### Syntax

[LabVIEWAdapter](labviewadapter.html).NewModule

#### Return Value

[LabVIEWModule](labviewmodule.html)

#### Purpose

Creates and returns a new
 [LabVIEWModule](labviewmodule.html)
 object. Use this method to create a
 LabVIEWModule
 object that you can use to execute a LabVIEW VI without using a step, sequence, or execution.

#### See Also

[LabVIEWModule](labviewmodule.html)

[LabVIEWModule.Execute](labviewmodule-execute.html)

[LabVIEWParameters.NewArguments](labviewparameters-newarguments.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-numberofthreadsusedwhenexecuti.html language=enus -->
## TOPIC 01282: LabVIEWAdapter.NumberOfThreadsUsedWhenExecutingVIsWithRTE

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-numberofthreadsusedwhenexecuti.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-numberofthreadsusedwhenexecuti.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.NumberOfThreadsUsedWhenExecutingVIsWithRTE Data Type Long Purpose Specifies the number of LabVIEW execution threads to use when executing VIs with the LabVIEW Run-Time Engine (RTE). The LabVIEW Adapter uses this property only when executing VIs using the LabVIEW RTE and the pre

### LabVIEWAdapter.NumberOfThreadsUsedWhenExecutingVIsWithRTE

#### Syntax

[LabVIEWAdapter](labviewadapter.html).NumberOfThreadsUsedWhenExecutingVIsWithRTE

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the number of LabVIEW execution threads to use when executing VIs with the LabVIEW Run-Time Engine (RTE).

Note

same as caller

#### Remarks

Changes to this property do not take effect until you restart the TestStand Engine.

#### See Also

[LabVIEWAdapter.AdditionalThreadsInheritCallingThreadsCPUAffinity](labviewadapter-additionalthreadsinheritcallin.html)

[LabVIEWAdapter.UseMultipleThreadsWhenExecutingVIsWithRTE](labviewadapter-usemultiplethreadswhenexecutin.html)

[Symmetric Multiprocessing in VIs Executed from TestStand](/csh?context=ts_tslabview_smp)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-overridemoduleoptions.html language=enus -->
## TOPIC 01283: LabVIEWAdapter.OverrideModuleOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-overridemoduleoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-overridemoduleoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.OverrideModuleOptions Data Type LabVIEWModuleOverrideOptions Use the following constants with this data type: LabVIEWModuleOverrideOption_Default –(Value: 0) Indicates that the LabVIEW Adapter runs the VI configured in the code module. LabVIEWModuleOverrideOption_PPL –(Value: 1

### LabVIEWAdapter.OverrideModuleOptions

#### Syntax

[LabVIEWAdapter](labviewadapter.html).OverrideModuleOptions

#### Data Type

[LabVIEWModuleOverrideOptions](labviewmoduleoverrideoptions.html)

Use the following constants with this data type:

- LabVIEWModuleOverrideOption_Default 
 –(Value: 0) Indicates that the LabVIEW Adapter runs the VI configured in the code module.
- LabVIEWModuleOverrideOption_PPL 
 –(Value: 1) Indicates that the LabVIEW Adapter runs the VI in the packed project library configured in the Override Module Settings window.

#### Purpose

Specifies the global override option to use.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-reserveloadedvisforexec.html language=enus -->
## TOPIC 01284: LabVIEWAdapter.ReserveLoadedVIsForExec

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-reserveloadedvisforexec.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-reserveloadedvisforexec.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.ReserveLoadedVIsForExec Data Type Boolean Purpose Specifies that LabVIEW reserves each VI to run when TestStand loads the VI. This property eliminates the need to use permanent reference VIs for sharing between step modules. Remarks When a VI is reserved for execution, referenc

### LabVIEWAdapter.ReserveLoadedVIsForExec

#### Syntax

[LabVIEWAdapter](labviewadapter.html).ReserveLoadedVIsForExec

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies that LabVIEW reserves each VI to run when TestStand loads the VI. This property eliminates the need to use permanent reference VIs for sharing between step modules.

#### Remarks

When a VI is reserved for execution, references that it creates during execution remain valid until the VI is unreserved. VIs that LabVIEW reserves take less time to call, but you cannot edit them in LabVIEW unless you click the
 Edit VI
 button in the
 [Edit LabVIEW VI Call](../tsref/edit-labview-vi-call-dialog-box.html)
 dialog box or select
 Edit Code
 from the context menu of the calling step.

TestStand unreserves a VI under the following circumstances:

- When you select
 File»Unload All Modules 
 from the
 File 
 menu.
- When the VI is unloaded based on a sequence file or step unload options.
- When you open a VI for editing from within TestStand.

You can create a reference in a VI called by one step in a sequence, use the reference in a VI called by a second step, and close the reference in a third step. For example, you can create a file refnum from Open File, use the reference in Read File or Write File, and close the reference using Close File when you no longer need the reference.

If you set the Unload Option for a step that calls a VI to Unload After Step Executes or Unload When Precondition Fails, the LabVIEW references the step creates might be destroyed on completion of the step. If you do not reserve VIs for execution, you can use the permanent reference VIs to maintain LabVIEW references between steps.

#### See Also

[Edit LabVIEW VI Call dialog box](../tsref/edit-labview-vi-call-dialog-box.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-setclustermemberisbinarystring.html language=enus -->
## TOPIC 01285: LabVIEWAdapter.SetClusterMemberIsBinaryString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-setclustermemberisbinarystring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-setclustermemberisbinarystring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.SetClusterMemberIsBinaryString( typeDefinition, propertyLookupString, val) Purpose Specifies whether the cluster member that corresponds to the specified type definition property contains binary data. Remarks TestStand preserves NUL bytes when setting and getting LabVIEW string

### LabVIEWAdapter.SetClusterMemberIsBinaryString

#### Syntax

[LabVIEWAdapter](labviewadapter.html).SetClusterMemberIsBinaryString( typeDefinition, propertyLookupString, val)

#### Purpose

Specifies whether the cluster member that corresponds to the specified type definition property contains binary data.

#### Remarks

TestStand preserves NUL bytes when setting and getting LabVIEW string data for binary strings.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

val
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to specify that the cluster member is a binary string.

#### See Also

[LabVIEWAdapter.GetClusterMemberIsBinaryString](labviewadapter-getclustermemberisbinarystring.html)

[LabVIEWAdapter.SetClusterPassingEnabled](labviewadapter-setclusterpassingenabled.html)

[LabVIEWParameter.PassAsBinaryString](labviewparameter-passasbinarystring.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-setclustermemberlabel.html language=enus -->
## TOPIC 01286: LabVIEWAdapter.SetClusterMemberLabel

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-setclustermemberlabel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-setclustermemberlabel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.SetClusterMemberLabel( typeDefinition, propertyLookupString, clusterMemberLabel) Purpose Specifies the label of the cluster member that corresponds to the specified type definition property. Parameters typeDefinition As PropertyObject [In] Specifies the type definition. This me

### LabVIEWAdapter.SetClusterMemberLabel

#### Syntax

[LabVIEWAdapter](labviewadapter.html).SetClusterMemberLabel( typeDefinition, propertyLookupString, clusterMemberLabel)

#### Purpose

Specifies the label of the cluster member that corresponds to the specified type definition property.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

clusterMemberLabel
 As
 [String](data-types-for-teststand.html)

[In] Specifies the label of the cluster member.

#### See Also

[LabVIEWAdapter.GetClusterMemberLabel](labviewadapter-getclustermemberlabel.html)

[LabVIEWAdapter.SetClusterPassingEnabled](labviewadapter-setclusterpassingenabled.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-setclusterpassingenabled.html language=enus -->
## TOPIC 01287: LabVIEWAdapter.SetClusterPassingEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-setclusterpassingenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-setclusterpassingenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.SetClusterPassingEnabled( typeDefinition, clusterPassingEnabled) Purpose Specifies whether a type definition allows the LabVIEW Adapter to pass instances of the type as cluster parameters to VIs. Parameters typeDefinition As PropertyObject [In] Specifies the type definition. Th

### LabVIEWAdapter.SetClusterPassingEnabled

#### Syntax

[LabVIEWAdapter](labviewadapter.html).SetClusterPassingEnabled( typeDefinition, clusterPassingEnabled)

#### Purpose

Specifies whether a type definition allows the LabVIEW Adapter to pass instances of the type as cluster parameters to VIs.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

clusterPassingEnabled
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether cluster passing is enabled.

#### See Also

[LabVIEWAdapter.GetClusterPassingEnabled](labviewadapter-getclusterpassingenabled.html)

[LabVIEWAdapter.SetExcludeFromCluster](labviewadapter-setexcludefromcluster.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-setexcludefromcluster.html language=enus -->
## TOPIC 01288: LabVIEWAdapter.SetExcludeFromCluster

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-setexcludefromcluster.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-setexcludefromcluster.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.SetExcludeFromCluster( typeDefinition, propertyLookupString, excludeFromCluster) Purpose Specifies whether the specified type definition property is excluded when converting instances of the type definition into clusters to pass as parameters to VIs. Parameters typeDefinition A

### LabVIEWAdapter.SetExcludeFromCluster

#### Syntax

[LabVIEWAdapter](labviewadapter.html).SetExcludeFromCluster( typeDefinition, propertyLookupString, excludeFromCluster)

#### Purpose

Specifies whether the specified type definition property is excluded when converting instances of the type definition into clusters to pass as parameters to VIs.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

excludeFromCluster
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to exclude the corresponding property. Otherwise, set this parameter to
 False
 .

#### See Also

[LabVIEWAdapter.GetExcludeFromCluster](labviewadapter-getexcludefromcluster.html)

[LabVIEWAdapter.SetClusterPassingEnabled](labviewadapter-setclusterpassingenabled.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-setserverinfo.html language=enus -->
## TOPIC 01289: LabVIEWAdapter.SetServerInfo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-setserverinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-setserverinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.SetServerInfo( serverType, serverInformation) Purpose Specifies which LabVIEW server the LabVIEW Adapter uses to run VIs. Remarks You can specify the LabVIEW ADE, a LabVIEW ActiveX server, a LabVIEW Runtime, or instruct TestStand to automatically use the LabVIEW Runtime that co

### LabVIEWAdapter.SetServerInfo

#### Syntax

[LabVIEWAdapter](labviewadapter.html).SetServerInfo( serverType, serverInformation)

#### Purpose

Specifies which LabVIEW server the LabVIEW Adapter uses to run VIs.

#### Remarks

You can specify the LabVIEW ADE, a LabVIEW ActiveX server, a LabVIEW Runtime, or instruct TestStand to automatically use the LabVIEW Runtime that corresponds to the saved version of the VI. The LabVIEW Adapter uses either a LabVIEW ActiveX Automation server or a supported LabVIEW Run-Time Engine to run VIs. If you specify an ActiveX server, it can be either a supported LabVIEW development environment or a supported version of a LabVIEW-built application that has enabled the LabVIEW ActiveX server. Refer to the
 [NI TestStand Readme](http://www.ni.com/r/tz6q4z)
 for more information about the versions of LabVIEW TestStand supports.

#### Parameters

serverType
 As
 [LabVIEWServerTypes](labviewservertypes.html)

[In] Specifies the type of LabVIEW server—either a LabVIEW ActiveX server or a LabVIEW Run-Time Engine.

serverInformation
 As
 [String](data-types-for-teststand.html)

[In] Identifies the LabVIEW server that the LabVIEW Adapter currently uses.

- - "LabVIEW" to instruct TestStand to use the active version of LabVIEW.
- - The progID for the LabVIEW ActiveX servers.
- - The path to the LabVIEW Runtime (lvrt.dll).
- - "AutoDetect" to instruct TestStand to use the LabVIEW Runtime that corresponds to the saved version of a VI.

#### See Also

[LabVIEWAdapter.GetServerInfo](labviewadapter-getserverinfo.html)

[LabVIEWServerTypes](labviewservertypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-usemultiplethreadswhenexecutin.html language=enus -->
## TOPIC 01290: LabVIEWAdapter.UseMultipleThreadsWhenExecutingVIsWithRTE

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-usemultiplethreadswhenexecutin.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-usemultiplethreadswhenexecutin.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.UseMultipleThreadsWhenExecutingVIsWithRTE Data Type Boolean Purpose Specifies to use multiple LabVIEW execution threads when executing VIs using the LabVIEW Run-Time Engine (RTE). The LabVIEW Adapter uses this property only when executing VIs using the LabVIEW RTE and the prefe

### LabVIEWAdapter.UseMultipleThreadsWhenExecutingVIsWithRTE

#### Syntax

[LabVIEWAdapter](labviewadapter.html).UseMultipleThreadsWhenExecutingVIsWithRTE

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies to use multiple LabVIEW execution threads when executing VIs using the LabVIEW Run-Time Engine (RTE).

Note

same as caller

#### Remarks

Changes to this property do not take effect until you restart the TestStand Engine.

#### See Also

[LabVIEWAdapter.AdditionalThreadsInheritCallingThreadsCPUAffinity](labviewadapter-additionalthreadsinheritcallin.html)

[LabVIEWAdapter.NumberofThreadsUsedWhenExecutingVIsWithRTE](labviewadapter-numberofthreadsusedwhenexecuti.html)

[Symmetric Multiprocessing in VIs Executed from TestStand](/csh?context=ts_tslabview_smp)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-uutiterationnumberexpression.html language=enus -->
## TOPIC 01291: LabVIEWAdapter.UUTIterationNumberExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-uutiterationnumberexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-uutiterationnumberexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.UUTIterationNumberExpression Data Type String The expression to evaluate at run time. Purpose Specifies the expression the LabVIEW Adapter evaluates at run time to generate a value to pass to the UUT # element of the Invocation Information cluster when calling a legacy VI. See

### LabVIEWAdapter.UUTIterationNumberExpression

#### Syntax

[LabVIEWAdapter](labviewadapter.html).UUTIterationNumberExpression

#### Data Type

[String](data-types-for-teststand.html)

The expression to evaluate at run time.

#### Purpose

Specifies the expression the LabVIEW Adapter evaluates at run time to generate a value to pass to the
 UUT #
 element of the
 Invocation Information
 cluster when calling a legacy VI.

#### See Also

[LabVIEWAdapter.UUTSerialNumberExpression](labviewadapter-uutserialnumberexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-uutserialnumberexpression.html language=enus -->
## TOPIC 01292: LabVIEWAdapter.UUTSerialNumberExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-uutserialnumberexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-uutserialnumberexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.UUTSerialNumberExpression Data Type String The expression to evaluate at run time. Purpose Specifies the expression the LabVIEW Adapter evaluates at run time to generate a value to pass to the UUT Info element of the Invocation Information cluster when calling a legacy VI. See

### LabVIEWAdapter.UUTSerialNumberExpression

#### Syntax

[LabVIEWAdapter](labviewadapter.html).UUTSerialNumberExpression

#### Data Type

[String](data-types-for-teststand.html)

The expression to evaluate at run time.

#### Purpose

Specifies the expression the LabVIEW Adapter evaluates at run time to generate a value to pass to the
 UUT Info
 element of the
 Invocation Information
 cluster when calling a legacy VI.

#### See Also

[LabVIEWAdapter.UUTIterationNumberExpression](labviewadapter-uutiterationnumberexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter.html language=enus -->
## TOPIC 01293: LabVIEWAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEW Adapter class to configure and obtain LabVIEW Adapter-specific information about the module adapter. Call the Engine.GetAdapter or Engine.GetAdapterByKeyName method to obtain a reference to the adapter object. To access the properties and methods of the Adapter class, us

### LabVIEWAdapter

Use objects from the LabVIEW Adapter class to configure and obtain LabVIEW Adapter-specific information about the module adapter. Call the
 
 [Engine.GetAdapter](engine-getadapter.html)
 or
 
 [Engine.GetAdapterByKeyName](engine-getadapterbykeyname.html)
 method to obtain a reference to the adapter object.

To access the properties and methods of the Adapter class, use the
 [LabVIEWAdapter.AsAdapter](labviewadapter-asadapter.html)
 method to obtain an object.

#### Properties

| AdditionalThreadsInheritCallingThreadsCPUAffinity |
| --- |
| AutoDeploySharedVariables |
| AutoUndeploySharedVariables |
| BuildAndExecuteAtStartOfExecution |
| BuildPPLsAtStartOfExecution |
| CodeTemplatePolicy |
| CurrentLabVIEWServerVersion (Read Only) |
| EnableRTEDebuggingAndTracing |
| EnableVersionIndependentRuntime |
| IsCurrentLabVIEWServerAnEditor (Read Only) |
| IsLabVIEWActiveXServerConnectionValid (Read Only) |
| IsSupportedLabVIEWDevelopmentSystemInstalled (Read Only) |
| LabVIEWDevelopmentEnvironmentBitness |
| NumberOfThreadsUsedWhenExecutingVIsWithRTE |
| OverrideModuleOptions |
| ReserveLoadedVIsForExec |
| UseMultipleThreadsWhenExecutingVIsWithRTE |
| UUTIterationNumberExpression |
| UUTSerialNumberExpression |

#### Methods

| AsAdapter |
| --- |
| CheckRemoteSystemStatus |
| ClearBuildAndExecuteCache |
| DeployProjectLibrary |
| DisplayHelpForNodeProperty |
| FileExistsInLLB |
| GetClassesForNodeLibrary |
| GetClusterMemberIsBinaryString |
| GetClusterMemberLabel |
| GetClusterPassingEnabled |
| GetExcludeFromCluster |
| GetExpressVIMenuStructure |
| GetMemberNames |
| GetNodeLibraries |
| GetPropertiesForLabVIEWClass |
| GetPropertiesForNodeClass |
| GetServerInfo |
| GetVINamespace |
| GetVIVersion |
| Initialize |
| IsBuildAndExecuteEnabled |
| IsExpressVI |
| NewModule |
| SetClusterMemberIsBinaryString |
| SetClusterMemberLabel |
| SetClusterPassingEnabled |
| SetExcludeFromCluster |
| SetServerInfo |

#### See Also

[Adapter](adapter.html)

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[Engine.GetAdapter](engine-getadapter.html)

[Engine.GetAdapterByKeyName](engine-getadapterbykeyname.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewargument-compleximaginarypart.html language=enus -->
## TOPIC 01294: LabVIEWArgument.ComplexImaginaryPart

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewargument-compleximaginarypart.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewargument-compleximaginarypart.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWArgument.ComplexImaginaryPart Data Type LabVIEWArgument Purpose Returns the LabVIEWArgument for the imaginary part of a complex number or array. See Also LabVIEWArgument LabVIEWParameter.ComplexImaginaryPartElement

### LabVIEWArgument.ComplexImaginaryPart

#### Syntax

[LabVIEWArgument](labviewargument.html).ComplexImaginaryPart

#### Data Type

[LabVIEWArgument](labviewargument.html)

#### Purpose

Returns the
 [LabVIEWArgument](labviewargument.html)
 for the imaginary part of a complex number or array.

#### See Also

[LabVIEWArgument](labviewargument.html)

[LabVIEWParameter.ComplexImaginaryPartElement](labviewparameter-compleximaginarypartelement.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewargument-complexrealpart.html language=enus -->
## TOPIC 01295: LabVIEWArgument.ComplexRealPart

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewargument-complexrealpart.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewargument-complexrealpart.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWArgument.ComplexRealPart Data Type LabVIEWArgument Purpose Returns the LabVIEWArgument for the real part of a complex number or array. See Also LabVIEWArgument LabVIEWParameter.ComplexRealPartElement

### LabVIEWArgument.ComplexRealPart

#### Syntax

[LabVIEWArgument](labviewargument.html).ComplexRealPart

#### Data Type

[LabVIEWArgument](labviewargument.html)

#### Purpose

Returns the
 [LabVIEWArgument](labviewargument.html)
 for the real part of a complex number or array.

#### See Also

[LabVIEWArgument](labviewargument.html)

[LabVIEWParameter.ComplexRealPartElement](labviewparameter-complexrealpartelement.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewargument-elements.html language=enus -->
## TOPIC 01296: LabVIEWArgument.Elements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewargument-elements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewargument-elements.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWArgument.Elements Data Type LabVIEWArguments Purpose Returns a collection of LabVIEWArguments to pass to a parameter that is a cluster or an array of clusters. See Also LabVIEWArguments LabVIEWParameter.Elements

### LabVIEWArgument.Elements

#### Syntax

[LabVIEWArgument](labviewargument.html).Elements

#### Data Type

[LabVIEWArguments](labviewarguments.html)

#### Purpose

Returns a collection of
 [LabVIEWArguments](labviewarguments.html)
 to pass to a parameter that is a cluster or an array of clusters.

#### See Also

[LabVIEWArguments](labviewarguments.html)

[LabVIEWParameter.Elements](labviewparameter-elements.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewargument-parametername.html language=enus -->
## TOPIC 01297: LabVIEWArgument.ParameterName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewargument-parametername.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewargument-parametername.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWArgument.ParameterName Data Type String Purpose Returns the name of the parameter in the VI that is associated with the argument. See Also LabVIEWParameter.ParameterName

### LabVIEWArgument.ParameterName

#### Syntax

[LabVIEWArgument](labviewargument.html).ParameterName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the parameter in the VI that is associated with the argument.

#### See Also

[LabVIEWParameter.ParameterName](labviewparameter-parametername.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewargument-value.html language=enus -->
## TOPIC 01298: LabVIEWArgument.Value

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewargument-value.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewargument-value.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWArgument.Value Data Type PropertyObject Purpose Specifies the argument value to pass for the corresponding parameter. See Also LabVIEWModule.Execute

### LabVIEWArgument.Value

#### Syntax

[LabVIEWArgument](labviewargument.html).Value

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Specifies the argument value to pass for the corresponding parameter.

#### See Also

[LabVIEWModule.Execute](labviewmodule-execute.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewargument.html language=enus -->
## TOPIC 01299: LabVIEWArgument

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewargument.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewargument.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEWArgument class to set the argument value to pass to a LabVIEW VI using the LabVIEWModule.Execute method. Properties ComplexImaginaryPart (Read Only) ComplexRealPart (Read Only) Elements (Read Only) ParameterName (Read Only) Value See Also Effectively Using LabVIEW with Te

### LabVIEWArgument

Use objects from the
 LabVIEWArgument
 class to set the argument value to pass to a LabVIEW VI using the
 [LabVIEWModule.Execute](labviewmodule-execute.html)
 method.

#### Properties

| ComplexImaginaryPart (Read Only) |
| --- |
| ComplexRealPart (Read Only) |
| Elements (Read Only) |
| ParameterName (Read Only) |
| Value |

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEWArguments](labviewarguments.html)

[LabVIEWModule.Execute](labviewmodule-execute.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewarguments-count.html language=enus -->
## TOPIC 01300: LabVIEWArguments.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewarguments-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewarguments-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWArguments.Count Data Type Long Purpose Returns the number of items in the collection.

### LabVIEWArguments.Count

#### Syntax

[LabVIEWArguments](labviewarguments.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewarguments-item.html language=enus -->
## TOPIC 01301: LabVIEWArguments.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewarguments-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewarguments-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWArguments.Item( index) Data Type LabVIEWArgument Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the item to retrieve. An argument at a specific index in the LabVIEWArguments collection

### LabVIEWArguments.Item

#### Syntax

[LabVIEWArguments](labviewarguments.html).Item( index)

#### Data Type

[LabVIEWArgument](labviewargument.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve. An argument at a specific index in the
 [LabVIEWArguments](labviewarguments.html)
 collection corresponds to the parameter at the same index in the
 [LabVIEWParameters](labviewparameters.html)
 collection that you used to create the
 LabVIEWArguments
 collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewarguments.html language=enus -->
## TOPIC 01302: LabVIEWArguments

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewarguments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewarguments.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEWArguments class to pass specific argument values to a LabVIEW VI using the LabVIEWModule.Execute method. Use the LabVIEWParameters.NewArguments method to create a new arguments collection. Properties Count (Read Only) Item (Read Only) See Also Effectively Using LabVIEW wi

### LabVIEWArguments

Use objects from the
 LabVIEWArguments
 class to pass specific argument values to a LabVIEW VI using the
 [LabVIEWModule.Execute](labviewmodule-execute.html)
 method. Use the
 [LabVIEWParameters.NewArguments](labviewparameters-newarguments.html)
 method to create a new arguments collection.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEWModule.Execute](labviewmodule-execute.html)

[LabVIEWParameters.NewArguments](labviewparameters-newarguments.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewcalltypes.html language=enus -->
## TOPIC 01303: LabVIEWCallTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewcalltypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewcalltypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the LabVIEWModule.CallType property to specify the type of call the LabVIEW module executes. LVCallType_Class_Member_Call –(Value: 1) Indicates that the VI code module calls a LabVIEW class member VI with dynamic dispatching enabled. LVCallType_Property_Node_Call –(Value: 2)

### LabVIEWCallTypes

Use these constants with the
 [LabVIEWModule.CallType](labviewmodule-calltype.html)
 property to specify the type of call the LabVIEW module executes.

- LVCallType_Class_Member_Call 
 –(Value: 1) Indicates that the VI code module calls a LabVIEW class member VI with dynamic dispatching enabled.
- LVCallType_Property_Node_Call 
 –(Value: 2) Indicates that the VI code module calls a LabVIEW Property Node.
- LVCallType_VI_Call 
 –(Value: 0) Indicates that the VI code module calls a VI without LabVIEW dynamic dispatching.

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEWModule.CallType](labviewmodule-calltype.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewdevelopmentenvironmentbitnessoptions.html language=enus -->
## TOPIC 01304: LabVIEWDevelopmentEnvironmentBitnessOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewdevelopmentenvironmentbitnessoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewdevelopmentenvironmentbitnessoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the LabVIEWAdapter.LabVIEWDevelopmentEnvironmentBitness property to specify the bitness of the LabVIEW Development Environment version to use. LVDevelopmentEnvironmentBitness_32bit –(Value: 1) Launches the current active 32-bit LabVIEW development environment. LVDevelopmentE

### LabVIEWDevelopmentEnvironmentBitnessOptions

Use these constants with the
 [LabVIEWAdapter.LabVIEWDevelopmentEnvironmentBitness](labviewadapter-labviewdevelopmentenvironmentb.html)
 property to specify the bitness of the LabVIEW Development Environment version to use.

- LVDevelopmentEnvironmentBitness_32bit 
 –(Value: 1) Launches the current active 32-bit LabVIEW development environment.
- LVDevelopmentEnvironmentBitness_64bit 
 –(Value: 2) Launches the current active 64-bit LabVIEW development environment.
- LVDevelopmentEnvironmentBitness_Default 
 –(Value: 0) Launches the current active 32-bit or 64-bit LabVIEW development environment, with a preference to match the bitness of TestStand.

#### See Also

[LabVIEWAdapter.LabVIEWDevelopmentEnvironmentBitness](labviewadapter-labviewdevelopmentenvironmentb.html)

[LabVIEW Adapter Configuration Dialog Box](../tsref/labview-adapter-configuration-dialog-box.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-asmodule.html language=enus -->
## TOPIC 01305: LabVIEWModule.AsModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-asmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-asmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.AsModule Return Value Module Purpose Returns the underlying Module object that represents the LabVIEWModule object. Remarks Use the Module object to access properties and methods common to all modules. See Also Module

### LabVIEWModule.AsModule

#### Syntax

[LabVIEWModule](labviewmodule.html).AsModule

#### Return Value

[Module](module.html)

#### Purpose

Returns the underlying Module object that represents the LabVIEWModule object.

#### Remarks

Use the Module object to access properties and methods common to all modules.

#### See Also

[Module](module.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-buildbinary.html language=enus -->
## TOPIC 01306: LabVIEWModule.BuildBinary

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-buildbinary.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-buildbinary.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.BuildBinary Return Value Boolean Purpose Builds the packed project library using the configuration specified in the Override Module Settings window if the packed project library is missing or out of date.

### LabVIEWModule.BuildBinary

#### Syntax

[LabVIEWModule](labviewmodule.html).BuildBinary

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Builds the packed project library using the configuration specified in the Override Module Settings window if the packed project library is missing or out of date.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-buildspecificationname.html language=enus -->
## TOPIC 01307: LabVIEWModule.BuildSpecificationName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-buildspecificationname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-buildspecificationname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.BuildSpecificationName Data Type String Purpose Specifies the name of the build specification used to build the packed project library.

### LabVIEWModule.BuildSpecificationName

#### Syntax

[LabVIEWModule](labviewmodule.html).BuildSpecificationName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the name of the build specification used to build the packed project library.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-callname.html language=enus -->
## TOPIC 01308: LabVIEWModule.CallName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-callname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-callname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.CallName Data Type String Purpose Returns the name of the LabVIEW class member VI the code module calls. See Also LabVIEWModule.ClassPath

### LabVIEWModule.CallName

#### Syntax

[LabVIEWModule](labviewmodule.html).CallName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the LabVIEW class member VI the code module calls.

#### See Also

[LabVIEWModule.ClassPath](labviewmodule-classpath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-calltype.html language=enus -->
## TOPIC 01309: LabVIEWModule.CallType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-calltype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-calltype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.CallType Data Type LabVIEWCallTypes Use the following constants with this data type: LVCallType_Class_Member_Call –(Value: 1) Indicates that the VI code module calls a LabVIEW class member VI with dynamic dispatching enabled. LVCallType_Property_Node_Call –(Value: 2) Indicates t

### LabVIEWModule.CallType

#### Syntax

[LabVIEWModule](labviewmodule.html).CallType

#### Data Type

[LabVIEWCallTypes](labviewcalltypes.html)

Use the following constants with this data type:

- LVCallType_Class_Member_Call 
 –(Value: 1) Indicates that the VI code module calls a LabVIEW class member VI with dynamic dispatching enabled.
- LVCallType_Property_Node_Call 
 –(Value: 2) Indicates that the VI code module calls a LabVIEW Property Node.
- LVCallType_VI_Call 
 –(Value: 0) Indicates that the VI code module calls a VI without LabVIEW dynamic dispatching.

#### Purpose

Specifies the type of call the code module executes.

#### Remarks

You must also set the appropriate properties for the type of call you want to make. For example, for a class member call, you must set the
 [LabVIEWModule.ClassPath](labviewmodule-classpath.html)
 and
 [LabVIEWModule.CallName](labviewmodule-callname.html)
 properties. You might also need to set the
 [LabVIEWModule.ProjectPath](labviewmodule-projectpath.html)
 property depending on the configuration of the code module.

#### See Also

[LabVIEWModule.CallName](labviewmodule-callname.html)

[LabVIEWModule.ClassPath](labviewmodule-classpath.html)

[LabVIEWModule.ProjectPath](labviewmodule-projectpath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-classpath.html language=enus -->
## TOPIC 01310: LabVIEWModule.ClassPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-classpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-classpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.ClassPath Data Type String Purpose Specifies the path and name of the LabVIEW class the LabVIEWModule object calls. Remarks You can specify an absolute or relative pathname for the file. Relative pathnames are relative to the TestStand search directory paths . See Also LabVIEWMo

### LabVIEWModule.ClassPath

#### Syntax

[LabVIEWModule](labviewmodule.html).ClassPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the path and name of the LabVIEW class the
 [LabVIEWModule](labviewmodule.html)
 object calls.

#### Remarks

You can specify an absolute or relative pathname for the file. Relative pathnames are relative to the TestStand
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### See Also

[LabVIEWModule](labviewmodule.html)

[LabVIEWModule.CallName](labviewmodule-callname.html)

[Search Directory Paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)

[LabVIEWModule.EditClass](labviewmodule-editclass.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-convertexpressvitostandardvi.html language=enus -->
## TOPIC 01311: LabVIEWModule.ConvertExpressVIToStandardVI

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-convertexpressvitostandardvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-convertexpressvitostandardvi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.ConvertExpressVIToStandardVI( newVIPath) Return Value Boolean Returns a value that indicates whether TestStand successfully converted the Express VI to a standard VI. Purpose Converts an Express VI to a standard VI by detaching the Express VI from the module, creating a standard

### LabVIEWModule.ConvertExpressVIToStandardVI

#### Syntax

[LabVIEWModule](labviewmodule.html).ConvertExpressVIToStandardVI( newVIPath)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns a value that indicates whether TestStand successfully converted the Express VI to a standard VI.

#### Purpose

Converts an Express VI to a standard VI by detaching the Express VI from the module, creating a standard VI on disk that calls the Express VI, and reconfigures the module to call the new VI.

#### Remarks

This method overwrites an existing VI file without prompting.

#### Parameters

newVIPath
 As
 [String](data-types-for-teststand.html)

[In] Specifies a string containing the absolute pathname of the new VI to create.

#### See Also

[LabVIEWModule.VIAttached](labviewmodule-viattached.html)

[LabVIEWModule.VIPath](labviewmodule-vipath.html)

[LabVIEWModule.VIType](labviewmodule-vitype.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-converttostandardvi.html language=enus -->
## TOPIC 01312: LabVIEWModule.ConvertToStandardVI

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-converttostandardvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-converttostandardvi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.ConvertToStandardVI( newVIPath, options) Return Value Boolean Purpose Converts a LabVIEW step configured with an embedded VI to a standard VI call by detaching the embedded VI from the code module, creating a standard VI on disk that contains the previously embedded VI, and reco

### LabVIEWModule.ConvertToStandardVI

#### Syntax

[LabVIEWModule](labviewmodule.html).ConvertToStandardVI( newVIPath, options)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Converts a LabVIEW step configured with an embedded VI to a standard VI call by detaching the embedded VI from the code module, creating a standard VI on disk that contains the previously embedded VI, and reconfiguring the step to call the new VI in a standard VI call.

#### Parameters

newVIPath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the file path for the new VI to create on disk.

options
 As
 [Long](data-types-for-teststand.html)

[In] Reserved for future use.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-createproject.html language=enus -->
## TOPIC 01313: LabVIEWModule.CreateProject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-createproject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-createproject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.CreateProject Return Value Boolean Purpose Launches LabVIEW to create the LabVIEW project associated with this module. See Also LabVIEWModule.EditProject LabVIEWModule.ProjectPath

### LabVIEWModule.CreateProject

#### Syntax

[LabVIEWModule](labviewmodule.html).CreateProject

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Launches LabVIEW to create the LabVIEW project associated with this module.

#### See Also

[LabVIEWModule.EditProject](labviewmodule-editproject.html)

[LabVIEWModule.ProjectPath](labviewmodule-projectpath.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-displayparametermappingdialog.html language=enus -->
## TOPIC 01314: LabVIEWModule.DisplayParameterMappingDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-displayparametermappingdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-displayparametermappingdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.DisplayParameterMappingDialog( commonDialogOptions) Return Value Boolean Purpose Launches the Parameter Name/Mapping dialog box to configure parameter mapping settings for a LabVIEW step type. Returns True if the step was updated. Parameters commonDialogOptions As Long [In] Pass

### LabVIEWModule.DisplayParameterMappingDialog

#### Syntax

[LabVIEWModule](labviewmodule.html).DisplayParameterMappingDialog( commonDialogOptions)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Launches the
 [Parameter Name/Mapping](../tsref/parameter-name-mapping-dialog-box.html)
 dialog box to configure parameter mapping settings for a LabVIEW step type. Returns
 True
 if the step was updated.

#### Parameters

commonDialogOptions
 As
 [Long](data-types-for-teststand.html)

[In] Pass the
 [CommonDlgOption_ReadOnly](commondialogoptions.html)
 constant to display the Parameter Name/Mapping dialog box in read-only mode when the step type cannot be changed.

#### See Also

[LabVIEWModule](labviewmodule.html)

[Parameter Name/Mapping dialog box](../tsref/parameter-name-mapping-dialog-box.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-displayselectclassfromprojectdi.html language=enus -->
## TOPIC 01315: LabVIEWModule.DisplaySelectClassFromProjectDialogEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-displayselectclassfromprojectdi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-displayselectclassfromprojectdi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.DisplaySelectClassFromProjectDialogEx( reserved, propertyValue) Return Value Boolean Purpose Launches the Select a Class from LabVIEW Project dialog box, in which you can select a LabVIEW class to call from the LabVIEW project. Returns True if the step was updated. Parameters re

### LabVIEWModule.DisplaySelectClassFromProjectDialogEx

#### Syntax

[LabVIEWModule](labviewmodule.html).DisplaySelectClassFromProjectDialogEx( reserved, propertyValue)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Launches the
 [Select a Class from LabVIEW Project](../tsref/select-a-class-from-labview-project-dialog-bo.html)
 dialog box, in which you can select a LabVIEW class to call from the LabVIEW project. Returns
 True
 if the step was updated.

#### Parameters

reserved
 As
 [Long](data-types-for-teststand.html)

[In] Reserved for future use.

propertyValue
 As
 [LabVIEWModuleOverrideTypes](labviewmoduleoverridetypes.html)

[In] Use the following constants with this data type:

- LabVIEWOverrideType_Default - (Value: 0) Indicates to use the VI specified in the step.
- LabVIEWOverrideType_PPL - (Value: 1) Indicates to use the VI specified in the packed project library configured in the Override Module Settings window.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-displayselectclassfromprojectdi2.html language=enus -->
## TOPIC 01316: LabVIEWModule.DisplaySelectClassFromProjectDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-displayselectclassfromprojectdi2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-displayselectclassfromprojectdi2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.DisplaySelectClassFromProjectDialog( reserved) Return Value Boolean Purpose Launches the Select a Class from LabVIEW Project dialog box, in which you can select a LabVIEW class to call from the LabVIEW project. Returns True if the step was updated. Parameters reserved As Long [I

### LabVIEWModule.DisplaySelectClassFromProjectDialog

#### Syntax

[LabVIEWModule](labviewmodule.html).DisplaySelectClassFromProjectDialog( reserved)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Launches the
 [Select a Class from LabVIEW Project](../tsref/select-a-class-from-labview-project-dialog-bo.html)
 dialog box, in which you can select a LabVIEW class to call from the LabVIEW project. Returns
 True
 if the step was updated.

#### Parameters

reserved
 As
 [Long](data-types-for-teststand.html)

[In] Reserved for future use.

#### See Also

[LabVIEWModule.ClassPath](labviewmodule-classpath.html)

[Select a Class from LabVIEW Project dialog box](../tsref/select-a-class-from-labview-project-dialog-bo.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-displayselectclassmemberfrompro.html language=enus -->
## TOPIC 01317: LabVIEWModule.DisplaySelectClassMemberFromProjectDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-displayselectclassmemberfrompro.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-displayselectclassmemberfrompro.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.DisplaySelectClassMemberFromProjectDialog( reserved) Return Value Boolean Purpose Launches the Select a Class Member from LabVIEW Project dialog box, in which you can select a LabVIEW class member VI to call from the LabVIEW project. Returns True if the step was updated. Paramet

### LabVIEWModule.DisplaySelectClassMemberFromProjectDialog

#### Syntax

[LabVIEWModule](labviewmodule.html).DisplaySelectClassMemberFromProjectDialog( reserved)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Launches the
 [Select a Class Member from LabVIEW Project](../tsref/select-a-class-member-from-labview-project-di.html)
 dialog box, in which you can select a LabVIEW class member VI to call from the LabVIEW project. Returns
 True
 if the step was updated.

#### Parameters

reserved
 As
 [Long](data-types-for-teststand.html)

[In] Reserved for future use.

#### See Also

[LabVIEWModule.ClassPath](labviewmodule-classpath.html)

[Select a Class Member from LabVIEW Project dialog box](../tsref/select-a-class-member-from-labview-project-di.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-displayselectmemberfromclassdia.html language=enus -->
## TOPIC 01318: LabVIEWModule.DisplaySelectMemberFromClassDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-displayselectmemberfromclassdia.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-displayselectmemberfromclassdia.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.DisplaySelectMemberFromClassDialog( reserved) Return Value Boolean Purpose Launches the Select a Class Member from LabVIEW Class dialog box, in which you can select a LabVIEW class member VI to call from the LabVIEW class. Returns True if the step was updated. Parameters reserve

### LabVIEWModule.DisplaySelectMemberFromClassDialog

#### Syntax

[LabVIEWModule](labviewmodule.html).DisplaySelectMemberFromClassDialog( reserved)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Launches the
 [Select a Class Member from LabVIEW Class](../tsref/select-a-class-member-from-labview-class-dial.html)
 dialog box, in which you can select a LabVIEW class member VI to call from the LabVIEW class. Returns
 True
 if the step was updated.

#### Parameters

reserved
 As
 [Long](data-types-for-teststand.html)

[In] Reserved for future use.

#### See Also

[LabVIEWModule.ClassPath](labviewmodule-classpath.html)

[Select a Class Member from LabVIEW Class dialog box](../tsref/select-a-class-member-from-labview-class-dial.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-displayselectvifromprojectdialo.html language=enus -->
## TOPIC 01319: LabVIEWModule.DisplaySelectVIFromProjectDialogEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-displayselectvifromprojectdialo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-displayselectvifromprojectdialo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.DisplaySelectVIFromProjectDialogEx( pathToUse, propertyValue) Return Value Boolean Purpose Launches a dialog box that displays VIs to select from the LabVIEW project. Returns True if the step was updated. Parameters pathToUse As LabVIEWProjectPathTypes [In] Pass LVProjectPathTyp

### LabVIEWModule.DisplaySelectVIFromProjectDialogEx

#### Syntax

[LabVIEWModule](labviewmodule.html).DisplaySelectVIFromProjectDialogEx( pathToUse, propertyValue)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Launches a dialog box that displays VIs to select from the LabVIEW project. Returns
 True
 if the step was updated.

#### Parameters

pathToUse
 As
 [LabVIEWProjectPathTypes](labviewprojectpathtypes.html)

[In] Pass
 [LVProjectPathType_Remote](labviewprojectpathtypes.html)
 to use the value of the
 [LabVIEWModule.RemoteProjectPath](labviewmodule-remoteprojectpath.html)
 property. Pass
 [LVProjectPathType_Local](labviewprojectpathtypes.html)
 to use the value of the
 [LabVIEWModule.ProjectPath](labviewmodule-projectpath.html)
 property.

propertyValue
 As
 [LabVIEWModuleOverrideTypes](labviewmoduleoverridetypes.html)

[In] Use the following constants with this data type:

- LabVIEWOverrideType_Default - (Value: 0) Indicates to use the VI specified in the step.
- LabVIEWOverrideType_PPL - (Value: 1) Indicates to use the VI specified in the packed project library configured in the Override Module Settings window.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-displayselectvifromprojectdialo2.html language=enus -->
## TOPIC 01320: LabVIEWModule.DisplaySelectVIFromProjectDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-displayselectvifromprojectdialo2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-displayselectvifromprojectdialo2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.DisplaySelectVIFromProjectDialog( pathToUse) Return Value Boolean Purpose Launches a dialog box with VIs from the LabVIEW project to select. Returns True if the step was updated. Parameters pathToUse As LabVIEWProjectPathTypes [In] Pass LVProjectPathType_Remote to use the value

### LabVIEWModule.DisplaySelectVIFromProjectDialog

#### Syntax

[LabVIEWModule](labviewmodule.html).DisplaySelectVIFromProjectDialog( pathToUse)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Launches a dialog box with VIs from the LabVIEW project to select. Returns
 True
 if the step was updated.

#### Parameters

pathToUse
 As
 [LabVIEWProjectPathTypes](labviewprojectpathtypes.html)

[In] Pass
 [LVProjectPathType_Remote](labviewprojectpathtypes.html)
 to use the value of the
 [LabVIEWModule.RemoteProjectPath](labviewmodule-remoteprojectpath.html)
 property. Pass
 [LVProjectPathType_Local](labviewprojectpathtypes.html)
 to use the value of the
 [LabVIEWModule.ProjectPath](labviewmodule-projectpath.html)
 property.

#### See Also

[LabVIEWModule.ProjectPath](labviewmodule-projectpath.html)

[LabVIEWModule.RemoteProjectPath](labviewmodule-remoteprojectpath.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-editclass.html language=enus -->
## TOPIC 01321: LabVIEWModule.EditClass

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-editclass.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-editclass.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.EditClass Return Value Boolean Purpose Launches LabVIEW and opens the LabVIEW class associated with the code module. See Also LabVIEWModule.ClassPath

### LabVIEWModule.EditClass

#### Syntax

[LabVIEWModule](labviewmodule.html).EditClass

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Launches LabVIEW and opens the LabVIEW class associated with the code module.

#### See Also

[LabVIEWModule.ClassPath](labviewmodule-classpath.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-editproject.html language=enus -->
## TOPIC 01322: LabVIEWModule.EditProject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-editproject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-editproject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.EditProject Return Value Boolean Purpose Launches LabVIEW to edit the LabVIEW project associated with this module. See Also LabVIEWModule.CreateProject LabVIEWModule.ProjectPath

### LabVIEWModule.EditProject

#### Syntax

[LabVIEWModule](labviewmodule.html).EditProject

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Launches LabVIEW to edit the LabVIEW project associated with this module.

#### See Also

[LabVIEWModule.CreateProject](labviewmodule-createproject.html)

[LabVIEWModule.ProjectPath](labviewmodule-projectpath.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-execute.html language=enus -->
## TOPIC 01323: LabVIEWModule.Execute

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-execute.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-execute.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.Execute( sequenceContextParam, argumentsParam) Purpose Use this method to call a LabVIEW VI directly without using a step, sequence, or Execution. Remarks When you call a LabVIEW module using this method you can evaluate the parameter expressions to determine the argument values

### LabVIEWModule.Execute

#### Syntax

[LabVIEWModule](labviewmodule.html).Execute( sequenceContextParam, argumentsParam)

#### Purpose

Use this method to call a LabVIEW VI directly without using a step, sequence, or Execution.

#### Remarks

When you call a LabVIEW module using this method you can evaluate the parameter expressions to determine the argument values or specify the argument values directly using a
 [LabVIEWArguments](labviewarguments.html)
 collection.

To use the parameter value expressions, pass a valid
 [SequenceContext](sequencecontext.html)
 object to the
 sequenceContextParam
 to use to evaluate the
 [LabVIEWParameter.ValueExpr](labviewparameter-valueexpr.html)
 expressions.

To pass specific argument values, use the
 [LabVIEWParameters.NewArguments](labviewparameters-newarguments.html)
 method to create a collection of
 [LabVIEWArgument](labviewargument.html)
 objects and set the
 [LabVIEWArgument.Value](labviewargument-value.html)
 property on each item in the collection and on each item in contained collections like the
 [LabVIEWArgument.Elements](labviewargument-elements.html)
 collection.

#### Parameters

sequenceContextParam
 As
 
 [SequenceContext](sequencecontext.html)

[In] Specifies the
 SequenceContext
 object that this method uses to evaluate each of the
 LabVIEWParameter.ValueExpr
 expressions in the module parameters. Pass
 NULL
 for this parameter if you pass a
 LabVIEWArguments
 collection to the
 argumentsParam
 parameter.

argumentsParam
 As
 [LabVIEWArguments](labviewarguments.html)

[In] Specifies the argument collection that contains the argument values to pass to the VI. Pass
 NULL
 for this parameter to pass the values obtained from evaluating each of the
 [LabVIEWParameter.ValueExpr](labviewparameter-valueexpr.html)
 expressions in the module parameters.

#### See Also

[LabVIEWArgument](labviewargument.html)

[LabVIEWArgument.Elements](labviewargument-elements.html)

[LabVIEWArgument.Value](labviewargument-value.html)

[LabVIEWArguments](labviewarguments.html)

[LabVIEWParameter.ValueExpr](labviewparameter-valueexpr.html)

[LabVIEWParameters.NewArguments](labviewparameters-newarguments.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-exportvi.html language=enus -->
## TOPIC 01324: LabVIEWModule.ExportVI

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-exportvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-exportvi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.ExportVI( pathString, options = 0) Purpose Exports the embedded VI of the module to a file. Use this function to generate a wrapper VI for a step that you configured to use an Express VI or a LabVIEW Property Node call. Remarks To import a VI, call the LabVIEWModule.ImportVI met

### LabVIEWModule.ExportVI

#### Syntax

[LabVIEWModule](labviewmodule.html).ExportVI( pathString, options = 0)

#### Purpose

Exports the embedded VI of the module to a file. Use this function to generate a wrapper VI for a step that you configured to use an Express VI or a LabVIEW Property Node call.

#### Remarks

To import a VI, call the
 [LabVIEWModule.ImportVI](labviewmodule-importvi.html)
 method.

#### Parameters

pathString
 As
 [String](data-types-for-teststand.html)

[In/Out] Specifies an existing directory path with a trailing slash or an empty string. This method returns the full path of the exported VI. The VI filename is generated using the ID of the parent step of the module. If an existing directory path is passed, the VI is exported to the given directory. If an empty string is passed, then the VI is exported to a temporary file. The temporary file is deleted when the TestStand Engine shuts down.

options
 As
 [Long](data-types-for-teststand.html)

[In] Reserved for future use. Pass
 0
 .

This parameter has a default value of
 0
 .

#### See Also

[LabVIEWModule.ImportVI](labviewmodule-importvi.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-expressviname.html language=enus -->
## TOPIC 01325: LabVIEWModule.ExpressVIName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-expressviname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-expressviname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.ExpressVIName Data Type String Purpose Returns the name of the Express VI the module is calling. Remarks If the VI type of the module is Standard, this property returns an empty string. The LabVIEW Adapter persists this property value when you specify an Express VI as the code m

### LabVIEWModule.ExpressVIName

#### Syntax

[LabVIEWModule](labviewmodule.html).ExpressVIName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the Express VI the module is calling.

#### Remarks

If the VI type of the module is Standard, this property returns an empty string.

The LabVIEW Adapter persists this property value when you specify an Express VI as the code module for a step. For an unspecified step, you must call the
 [LabVIEWModule.ImportVI](labviewmodule-importvi.html)
 method before retrieving this property.

#### See Also

[LabVIEWModule.ImportVI](labviewmodule-importvi.html)

[LabVIEWModule.VIType](labviewmodule-vitype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-findclassurlusingclasspath.html language=enus -->
## TOPIC 01326: LabVIEWModule.FindClassUrlUsingClassPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-findclassurlusingclasspath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-findclassurlusingclasspath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.FindClassUrlUsingClassPath( classUrl) Return Value Boolean Returns True if TestStand successfully finds a URL for the LabVIEW class. Purpose Obtains the LabVIEW class URL by finding an absolute class path match in the LabVIEW project you select. If TestStand cannot find a match,

### LabVIEWModule.FindClassUrlUsingClassPath

#### Syntax

[LabVIEWModule](labviewmodule.html).FindClassUrlUsingClassPath( classUrl)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if TestStand successfully finds a URL for the LabVIEW class.

#### Purpose

Obtains the LabVIEW class URL by finding an absolute class path match in the LabVIEW project you select. If TestStand cannot find a match, the
 classUrl
 parameter is empty.

#### Parameters

classUrl
 As
 [String](data-types-for-teststand.html)

[Out] Returns the LabVIEW class URL path in the LabVIEW project you select.

#### See Also

[LabVIEWModule.ClassPath](labviewmodule-classpath.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-findclassurlusingclasspathex.html language=enus -->
## TOPIC 01327: LabVIEWModule.FindClassUrlUsingClassPathEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-findclassurlusingclasspathex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-findclassurlusingclasspathex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.FindClassUrlUsingClassPathEx( propertyValue, sourceClassUrl) Return Value Boolean Returns True if TestStand successfully finds a URL for the LabVIEW class. Purpose Obtains the URL of the LabVIEW class by finding a match for the absolute path of the class in the LabVIEW project y

### LabVIEWModule.FindClassUrlUsingClassPathEx

#### Syntax

[LabVIEWModule](labviewmodule.html).FindClassUrlUsingClassPathEx( propertyValue, sourceClassUrl)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if TestStand successfully finds a URL for the LabVIEW class.

#### Purpose

Obtains the URL of the LabVIEW class by finding a match for the absolute path of the class in the LabVIEW project you select. If TestStand cannot find a match, the
 classUrl
 parameter is empty.

#### Parameters

propertyValue
 As
 [LabVIEWModuleOverrideTypes](labviewmoduleoverridetypes.html)

[In] Use the following constants with this data type:

- LabVIEWOverrideType_Default - (Value: 0) Indicates to use the VI specified in the step.
- LabVIEWOverrideType_PPL - (Value: 1) Indicates to use the VI specified in the packed project library configured in the Override Module Settings window.

sourceClassUrl
 As
 [String](data-types-for-teststand.html)

[Out] Returns the LabVIEW class URL path in the LabVIEW project you select.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-findviurlusingvipath.html language=enus -->
## TOPIC 01328: LabVIEWModule.FindVIUrlUsingVIPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-findviurlusingvipath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-findviurlusingvipath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.FindVIUrlUsingVIPath( pathToUse, viUrl) Return Value Boolean Returns a value that indicates whether TestStand successfully found a URL for the VI. Purpose Obtains the VI URL by finding an absolute VI path match in the LabVIEW project you select. If TestStand cannot find a match,

### LabVIEWModule.FindVIUrlUsingVIPath

#### Syntax

[LabVIEWModule](labviewmodule.html).FindVIUrlUsingVIPath( pathToUse, viUrl)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns a value that indicates whether TestStand successfully found a URL for the VI.

#### Purpose

Obtains the VI URL by finding an absolute VI path match in the LabVIEW project you select. If TestStand cannot find a match, the
 viUrl
 parameter is empty.

#### Parameters

pathToUse
 As
 [LabVIEWProjectPathTypes](labviewprojectpathtypes.html)

[In] Pass
 [LVProjectPathType_Remote](labviewprojectpathtypes.html)
 to use the value of the
 [LabVIEWModule.RemoteProjectPath](labviewmodule-remoteprojectpath.html)
 property. Pass
 [LVProjectPathType_Local](labviewprojectpathtypes.html)
 to use the value of the
 [LabVIEWModule.ProjectPath](labviewmodule-projectpath.html)
 property.

viUrl
 As
 [String](data-types-for-teststand.html)

[Out] Returns the VI URL path in the LabVIEW project you select.

#### See Also

[LabVIEWModule.ProjectPath](labviewmodule-projectpath.html)

[LabVIEWModule.RemoteProjectPath](labviewmodule-remoteprojectpath.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-findviurlusingvipathex.html language=enus -->
## TOPIC 01329: LabVIEWModule.FindVIUrlUsingVIPathEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-findviurlusingvipathex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-findviurlusingvipathex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.FindVIUrlUsingVIPathEx( propertyValue, pathToUse, viUrl) Return Value Boolean Returns a value that indicates whether TestStand successfully found a URL for the VI in the project. Purpose Obtains the URL of the VI by finding a match for the absolute path of the VI in the LabVIEW

### LabVIEWModule.FindVIUrlUsingVIPathEx

#### Syntax

[LabVIEWModule](labviewmodule.html).FindVIUrlUsingVIPathEx( propertyValue, pathToUse, viUrl)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns a value that indicates whether TestStand successfully found a URL for the VI in the project.

#### Purpose

Obtains the URL of the VI by finding a match for the absolute path of the VI in the LabVIEW project you select. If TestStand cannot find a match, the
 viUrl
 parameter is empty.

#### Parameters

propertyValue
 As
 [LabVIEWModuleOverrideTypes](labviewmoduleoverridetypes.html)

[In] Use the following constants with this data type:

- LabVIEWOverrideType_Default - (Value: 0) Indicates to use the VI specified in the step.
- LabVIEWOverrideType_PPL - (Value: 1) Indicates to use the VI specified in the packed project library configured in the Override Module Settings window.

pathToUse
 As
 [LabVIEWProjectPathTypes](labviewprojectpathtypes.html)

[In] Pass
 [LVProjectPathType_Remote](labviewprojectpathtypes.html)
 to use the value of the
 [LabVIEWModule.RemoteProjectPath](labviewmodule-remoteprojectpath.html)
 property. Pass
 [LVProjectPathType_Local](labviewprojectpathtypes.html)
 to use the value of the
 [LabVIEWModule.ProjectPath](labviewmodule-projectpath.html)
 property.

viUrl
 As
 [String](data-types-for-teststand.html)

[Out] Returns the VI URL path in the LabVIEW project you select.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-getbinarybuildspecifications.html language=enus -->
## TOPIC 01330: LabVIEWModule.GetBinaryBuildSpecifications

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-getbinarybuildspecifications.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-getbinarybuildspecifications.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.GetBinaryBuildSpecifications( buildSpecifications) Purpose Obtains the list of build specifications that are configured to build packed project libraries from the LabVIEW project configured in the code module. Parameters buildSpecifications As String Array [Out] Returns a list o

### LabVIEWModule.GetBinaryBuildSpecifications

#### Syntax

[LabVIEWModule](labviewmodule.html).GetBinaryBuildSpecifications( buildSpecifications)

#### Purpose

Obtains the list of build specifications that are configured to build packed project libraries from the LabVIEW project configured in the code module.

#### Parameters

buildSpecifications
 As
 [String Array](data-types-for-teststand.html)

[Out] Returns a list of the build specifications found in the project that are configured to build packed project libraries.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-getclassabsolutepath.html language=enus -->
## TOPIC 01331: LabVIEWModule.GetClassAbsolutePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-getclassabsolutepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-getclassabsolutepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.GetClassAbsolutePath( classAbsolutePath) Return Value Boolean Returns True if TestStand finds the file. Purpose Obtains the absolute path of the LabVIEW class. If the code module uses a LabVIEW project path, TestStand uses the URL the LabVIEWModule.ClassPath property defines and

### LabVIEWModule.GetClassAbsolutePath

#### Syntax

[LabVIEWModule](labviewmodule.html).GetClassAbsolutePath( classAbsolutePath)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if TestStand finds the file.

#### Purpose

Obtains the absolute path of the LabVIEW class. If the code module uses a LabVIEW project path, TestStand uses the URL the
 [LabVIEWModule.ClassPath](labviewmodule-classpath.html)
 property defines and the LabVIEW project to determine the absolute path of the LabVIEW class.

#### Parameters

classAbsolutePath
 As
 [String](data-types-for-teststand.html)

[Out] Returns the absolute path of the LabVIEW class. If TestStand does not find the class, this parameter returns an empty string.

#### See Also

[LabVIEWModule.ClassPath](labviewmodule-classpath.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-getclassabsolutepathex.html language=enus -->
## TOPIC 01332: LabVIEWModule.GetClassAbsolutePathEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-getclassabsolutepathex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-getclassabsolutepathex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.GetClassAbsolutePathEx( propertyValue, sourceClassAbsolutePath) Return Value Boolean Returns True if TestStand finds the file. Purpose Obtains the absolute path of the LabVIEW class. If the code module uses a LabVIEW project path, TestStand uses the URL the LabVIEWModule.ClassPa

### LabVIEWModule.GetClassAbsolutePathEx

#### Syntax

[LabVIEWModule](labviewmodule.html).GetClassAbsolutePathEx( propertyValue, sourceClassAbsolutePath)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if TestStand finds the file.

#### Purpose

Obtains the absolute path of the LabVIEW class. If the code module uses a LabVIEW project path, TestStand uses the URL the
 LabVIEWModule.ClassPath
 property defines and the LabVIEW project to determine the absolute path of the LabVIEW class.

#### Parameters

propertyValue
 As
 [LabVIEWModuleOverrideTypes](labviewmoduleoverridetypes.html)

[In] Use the following constants with this data type:

- LabVIEWOverrideType_Default - (Value: 0) Indicates to use the VI specified in the step.
- LabVIEWOverrideType_PPL - (Value: 1) Indicates to use the VI specified in the packed project library configured in the Override Module Settings window.

sourceClassAbsolutePath
 As
 [String](data-types-for-teststand.html)

[Out] Returns the absolute path of the LabVIEW class. If TestStand does not find the class, this parameter returns an empty string.

#### See Also

[LabVIEWModule.ClassPath](labviewmodule-classpath.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-getprojecturlpathsforclasses.html language=enus -->
## TOPIC 01333: LabVIEWModule.GetProjectUrlPathsForClasses

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-getprojecturlpathsforclasses.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-getprojecturlpathsforclasses.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.GetProjectUrlPathsForClasses Return Value String Array Purpose Obtains a list of URL paths for the LabVIEW classes in the LabVIEW project you select. If TestStand cannot find the LabVIEW project, this list is empty. See Also LabVIEWModule.ClassPath

### LabVIEWModule.GetProjectUrlPathsForClasses

#### Syntax

[LabVIEWModule](labviewmodule.html).GetProjectUrlPathsForClasses

#### Return Value

[String Array](data-types-for-teststand.html)

#### Purpose

Obtains a list of URL paths for the LabVIEW classes in the LabVIEW project you select. If TestStand cannot find the LabVIEW project, this list is empty.

#### See Also

[LabVIEWModule.ClassPath](labviewmodule-classpath.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-getprojecturlpathsforvis.html language=enus -->
## TOPIC 01334: LabVIEWModule.GetProjectUrlPathsForVIs

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-getprojecturlpathsforvis.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-getprojecturlpathsforvis.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.GetProjectUrlPathsForVIs( pathToUse, items) Purpose Obtains a list of URL paths for the VIs in the LabVIEW project you select. If TestStand cannot find the LabVIEW project, this list is empty. Parameters pathToUse As LabVIEWProjectPathTypes [In] Pass LVProjectPathType_Remote to

### LabVIEWModule.GetProjectUrlPathsForVIs

#### Syntax

[LabVIEWModule](labviewmodule.html).GetProjectUrlPathsForVIs( pathToUse, items)

#### Purpose

Obtains a list of URL paths for the VIs in the LabVIEW project you select. If TestStand cannot find the LabVIEW project, this list is empty.

#### Parameters

pathToUse
 As
 [LabVIEWProjectPathTypes](labviewprojectpathtypes.html)

[In] Pass
 [LVProjectPathType_Remote](labviewprojectpathtypes.html)
 to use the value of the
 [LabVIEWModule.RemoteProjectPath](labviewmodule-remoteprojectpath.html)
 property. Pass
 [LVProjectPathType_Local](labviewprojectpathtypes.html)
 to use the value of the
 [LabVIEWModule.ProjectPath](labviewmodule-projectpath.html)
 property.

items
 As
 [String Array](data-types-for-teststand.html)

[Out] Returns the list of URL paths for the VIs in the LabVIEW project you select.

#### See Also

[LabVIEWModule.ProjectPath](labviewmodule-projectpath.html)

[LabVIEWModule.RemoteProjectPath](labviewmodule-remoteprojectpath.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-getviabsolutepath.html language=enus -->
## TOPIC 01335: LabVIEWModule.GetVIAbsolutePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-getviabsolutepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-getviabsolutepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.GetVIAbsolutePath( viAbsolutePath) Return Value Boolean Returns True if TestStand finds the file. Purpose Obtains the absolute path of the VI. If the module uses a LabVIEW project path, TestStand uses the URL the LabVIEWModule.VIPath property defines in conjunction with the LabV

### LabVIEWModule.GetVIAbsolutePath

#### Syntax

[LabVIEWModule](labviewmodule.html).GetVIAbsolutePath( viAbsolutePath)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if TestStand finds the file.

#### Purpose

Obtains the absolute path of the VI. If the module uses a LabVIEW project path, TestStand uses the URL the
 [LabVIEWModule.VIPath](labviewmodule-vipath.html)
 property defines in conjunction with the LabVIEW project to determine the absolute path of the VI.

#### Parameters

viAbsolutePath
 As
 [String](data-types-for-teststand.html)

[Out] Returns the absolute path of the VI. If TestStand does not find the VI, this parameter returns an empty string.

#### See Also

[LabVIEWModule.ProjectPath](labviewmodule-projectpath.html)

[LabVIEWModule.VIPath](labviewmodule-vipath.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-getviabsolutepathex.html language=enus -->
## TOPIC 01336: LabVIEWModule.GetVIAbsolutePathEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-getviabsolutepathex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-getviabsolutepathex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.GetVIAbsolutePathEx( propertyValue, viAbsolutePath) Return Value Boolean Returns True if TestStand finds the file. Purpose Obtains the absolute path of the VI configured in the step. Parameters propertyValue As LabVIEWModuleOverrideTypes [In] Use the following constants with thi

### LabVIEWModule.GetVIAbsolutePathEx

#### Syntax

[LabVIEWModule](labviewmodule.html).GetVIAbsolutePathEx( propertyValue, viAbsolutePath)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if TestStand finds the file.

#### Purpose

Obtains the absolute path of the VI configured in the step.

#### Parameters

propertyValue
 As
 [LabVIEWModuleOverrideTypes](labviewmoduleoverridetypes.html)

[In] Use the following constants with this data type:

- LabVIEWOverrideType_Default - (Value: 0) Indicates to use the VI specified in the step.
- LabVIEWOverrideType_PPL - (Value: 1) Indicates to use the VI specified in the packed project library configured in the Override Module Settings window.

viAbsolutePath
 As
 [String](data-types-for-teststand.html)

[Out] Returns the absolute path of the VI. If TestStand does not find the VI, this parameter returns an empty string.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-helpcontext.html language=enus -->
## TOPIC 01337: LabVIEWModule.HelpContext

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-helpcontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-helpcontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.HelpContext Data Type String Purpose Returns the tag for the help topic of the VI the module calls. Remarks Call the LabVIEWModule.LoadVIInfo or Module.LoadPrototype method before calling this method. The values stay in memory until the sequence file closes. See Also LabVIEWModu

### LabVIEWModule.HelpContext

#### Syntax

[LabVIEWModule](labviewmodule.html).HelpContext

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the tag for the help topic of the VI the module calls.

#### Remarks

Call the
 [LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)
 or
 [Module.LoadPrototype](module-loadprototype.html)
 method before calling this method. The values stay in memory until the sequence file closes.

#### See Also

[LabVIEWModule.HelpFilePath](labviewmodule-helpfilepath.html)

[LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-helpfilepath.html language=enus -->
## TOPIC 01338: LabVIEWModule.HelpFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-helpfilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-helpfilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.HelpFilePath Data Type String Purpose Returns the absolute path to the help file of the VI the module calls. Remarks Call the LabVIEWModule.LoadVIInfo or Module.LoadPrototype method before calling this method. The values stay in memory until the sequence file closes. See Also La

### LabVIEWModule.HelpFilePath

#### Syntax

[LabVIEWModule](labviewmodule.html).HelpFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the absolute path to the help file of the VI the module calls.

#### Remarks

Call the
 [LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)
 or
 [Module.LoadPrototype](module-loadprototype.html)
 method before calling this method. The values stay in memory until the sequence file closes.

#### See Also

[LabVIEWModule.HelpContext](labviewmodule-helpcontext.html)

[LabVIEWModule.HelpPicture](labviewmodule-helppicture.html)

[LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-helppicture.html language=enus -->
## TOPIC 01339: LabVIEWModule.HelpPicture

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-helppicture.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-helppicture.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.HelpPicture Data Type Picture Purpose Returns the context help picture of the VI that the module calls. Remarks Call the LabVIEWModule.LoadVIInfo or Module.LoadPrototype method before calling this method. The values stay in memory until the sequence file closes. See Also LabVIEW

### LabVIEWModule.HelpPicture

#### Syntax

[LabVIEWModule](labviewmodule.html).HelpPicture

#### Data Type

[Picture](data-types-for-teststand.html)

#### Purpose

Returns the context help picture of the VI that the module calls.

#### Remarks

Call the
 [LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)
 or
 [Module.LoadPrototype](module-loadprototype.html)
 method before calling this method. The values stay in memory until the sequence file closes.

#### See Also

[LabVIEWModule.HelpContext](labviewmodule-helpcontext.html)

[LabVIEWModule.HelpPictureRects](labviewmodule-helppicturerects.html)

[LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-helppicturerects.html language=enus -->
## TOPIC 01340: LabVIEWModule.HelpPictureRects

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-helppicturerects.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-helppicturerects.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.HelpPictureRects Data Type PropertyObject Returns a PropertyObject array where each element of the array is a PropertyObject that represents a wired terminal on the VI connector pane. The order of the terminals corresponds to the order of the parameters the LabVIEWModule.Paramet

### LabVIEWModule.HelpPictureRects

#### Syntax

[LabVIEWModule](labviewmodule.html).HelpPictureRects

#### Data Type

[PropertyObject](propertyobject.html)

Returns a PropertyObject array where each element of the array is a PropertyObject that represents a wired terminal on the VI connector pane. The order of the terminals corresponds to the order of the parameters the
 [LabVIEWModule.Parameters](labviewmodule-parameters.html)
 property returns. Each element of the array contains two properties, LabelRect and TerminalRect. Each property contains the following four subproperties: Top, Bottom, Left, and Right that represent the absolute coordinate values of the rectangle for the label or the terminal.

#### Purpose

Returns the coordinates to the rectangles of each label and terminal in the context help picture of the VI the module calls.

#### Remarks

Call the
 [LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)
 or
 [Module.LoadPrototype](module-loadprototype.html)
 method before calling this method. The values stay in memory until the sequence file closes.

#### See Also

[LabVIEWModule.HelpPicture](labviewmodule-helppicture.html)

[LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)

[LabVIEWModule.Parameters](labviewmodule-parameters.html)

[Module.LoadPrototype](module-loadprototype.html)

[PropertyObject](propertyobject.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-importvi.html language=enus -->
## TOPIC 01341: LabVIEWModule.ImportVI

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-importvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-importvi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.ImportVI( pathString, type = ImportVIType_ExpressVIWrapper, options = 0) Purpose Imports a VI from a file into the module. Use this function to configure a LabVIEW step to call an Express VI from a template or from a wrapper VI generated by a previous call to the LabVIEWModule.E

### LabVIEWModule.ImportVI

#### Syntax

[LabVIEWModule](labviewmodule.html).ImportVI( pathString, type = ImportVIType_ExpressVIWrapper, options = 0)

#### Purpose

Imports a VI from a file into the module. Use this function to configure a LabVIEW step to call an Express VI from a template or from a wrapper VI generated by a previous call to the
 [LabVIEWModule.ExportVI](labviewmodule-exportvi.html)
 method. You can also use this function to configure a LabVIEW step to call a LabVIEW Property Node wrapper VI generated by a previous call to the
 LabVIEWModule.ExportVI
 method.

#### Remarks

To export the VI, call the
 LabVIEWModule.ExportVI
 method.

#### Parameters

pathString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the pathname of the file to import into the module. Pass an empty path to remove an imported VI from the module.

type
 As
 [ImportVITypes](importvitypes.html)

[In] Specifies the type of VI to import.

This parameter has a default value of
 ImportVIType_ExpressVIWrapper
 .

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more
 [ImportVIOptions](importvioptions.html)
 constants. Use the bitwise-OR operator to specify multiple flags.

This parameter has a default value of
 0
 .

#### See Also

[ImportVIOptions](importvioptions.html)

[ImportVITypes](importvitypes.html)

[LabVIEWModule.ExportVI](labviewmodule-exportvi.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-isprojectvalid.html language=enus -->
## TOPIC 01342: LabVIEWModule.IsProjectValid

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-isprojectvalid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-isprojectvalid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.IsProjectValid( errorDescription) Return Value Boolean Purpose Returns True if the LabVIEW project associated with this module has a valid configuration. Parameters errorDescription As String [Out] Returns a string with the error description when the method returns False .

### LabVIEWModule.IsProjectValid

#### Syntax

[LabVIEWModule](labviewmodule.html).IsProjectValid( errorDescription)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the LabVIEW project associated with this module has a valid configuration.

#### Parameters

errorDescription
 As
 [String](data-types-for-teststand.html)

[Out] Returns a string with the error description when the method returns
 False
 .

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-loadprototype.html language=enus -->
## TOPIC 01343: LabVIEWModule.LoadPrototype

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-loadprototype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-loadprototype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.LoadPrototype( discardParameterValues = False) Return Value Boolean Returns a value that indicates whether the prototype of the VI was loaded. This method usually returns True . Purpose This method is obsolete. Use the Module.LoadPrototype method instead. Remarks Loads parameter

### LabVIEWModule.LoadPrototype

#### Syntax

[LabVIEWModule](labviewmodule.html).LoadPrototype( discardParameterValues = False)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns a value that indicates whether the prototype of the VI was loaded. This method usually returns
 True
 .

#### Purpose

Note

Module.LoadPrototype

#### Remarks

Loads parameter information from the VI of the module.

You must set the
 [LabVIEWModule.VIPath](labviewmodule-vipath.html)
 property of the module before calling this method. You must call this method before accessing the
 [LabVIEWModule.Parameters](labviewmodule-parameters.html)
 property of the module.

#### Parameters

discardParameterValues
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether to reset the
 [LabVIEWParameter.ValueExpr](labviewparameter-valueexpr.html)
 property of the existing parameter values when loading a new prototype.

This parameter has a default value of
 False
 .

#### See Also

[LabVIEWModule.Parameters](labviewmodule-parameters.html)

[LabVIEWModule.VIPath](labviewmodule-vipath.html)

[LabVIEWParameter.ValueExpr](labviewparameter-valueexpr.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Obsolete LabVIEWModule Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-loadviinfo.html language=enus -->
## TOPIC 01344: LabVIEWModule.LoadVIInfo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-loadviinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-loadviinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.LoadVIInfo Return Value Boolean Returns a value that indicates whether the prototype of the VI specified in the step matches the prototype of the VI on disk. Purpose Loads information about the VI that the module calls, including default values, enumeration values, the VI help f

### LabVIEWModule.LoadVIInfo

#### Syntax

[LabVIEWModule](labviewmodule.html).LoadVIInfo

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns a value that indicates whether the prototype of the VI specified in the step matches the prototype of the VI on disk.

#### Purpose

Loads information about the VI that the module calls, including default values, enumeration values, the VI help file information, and the VI context help picture.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-matcharrayparameterstolabviewar.html language=enus -->
## TOPIC 01345: LabVIEWModule.MatchArrayParametersToLabVIEWArrayDimensions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-matcharrayparameterstolabviewar.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-matcharrayparameterstolabviewar.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.MatchArrayParametersToLabVIEWArrayDimensions Data Type Boolean Purpose When True , specifies that all array parameters of the LabVIEW Module must match the corresponding LabVIEW control or indicator in size for each dimension. Remarks There is a known issue in TestStand that cau

### LabVIEWModule.MatchArrayParametersToLabVIEWArrayDimensions

#### Syntax

[LabVIEWModule](labviewmodule.html).MatchArrayParametersToLabVIEWArrayDimensions

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

When
 True
 , specifies that all array parameters of the LabVIEW Module must match the corresponding LabVIEW control or indicator in size for each dimension.

#### Remarks

There is a known issue in TestStand that causes the array parameters in a code module to have the dimensions transposed compared to the corresponding LabVIEW control or indicator. For example, if the LabVIEW array has a size of [2][4][1], then the corresponding TestStand parameter would have a size of [1][4][2] when using default values for the parameter. This issue also causes array data to be incorrectly transposed when TestStand passes the data to LabVIEW.

Use
 MatchArrayParametersToLabVIEWArrayDimensions
 to correct this behavior on a per-step basis. This property affects the processing of all array parameters in the code module. When
 MatchArrayParametersToLabVIEWArrayDimensions
 is
 True
 , the TestStand array parameter and the LabVIEW array have the same size for default values, and the data at each index of the array in TestStand and LabVIEW will be the same when passing arrays during execution.

Note

LabVIEWModule.LoadPrototype

#### See Also

[LabVIEWModule.LoadPrototype](labviewmodule-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-namespace.html language=enus -->
## TOPIC 01346: LabVIEWModule.Namespace

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-namespace.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-namespace.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.Namespace Data Type String Purpose Returns the LabVIEW namespace of the VI. The namespace of the VI is the qualified name of the owning LabVIEW project library. See Also LabVIEWModule.ProjectPath LabVIEWModule.VIPath

### LabVIEWModule.Namespace

#### Syntax

[LabVIEWModule](labviewmodule.html).Namespace

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the LabVIEW namespace of the VI. The namespace of the VI is the qualified name of the owning LabVIEW project library.

#### See Also

[LabVIEWModule.ProjectPath](labviewmodule-projectpath.html)

[LabVIEWModule.VIPath](labviewmodule-vipath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-nodeclassdataname.html language=enus -->
## TOPIC 01347: LabVIEWModule.NodeClassDataName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-nodeclassdataname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-nodeclassdataname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.NodeClassDataName Data Type String Purpose Specifies the LabVIEW I/O Library Class Data Name when calling a LabVIEW Property Node. See Also LabVIEWModule.NodeLibraryGenericTypeName LabVIEWModule.NodeLibraryName LabVIEWModule.NodeProperties

### LabVIEWModule.NodeClassDataName

#### Syntax

[LabVIEWModule](labviewmodule.html).NodeClassDataName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the LabVIEW I/O Library Class Data Name when calling a LabVIEW Property Node.

#### See Also

[LabVIEWModule.NodeLibraryGenericTypeName](labviewmodule-nodelibrarygenerictypename.html)

[LabVIEWModule.NodeLibraryName](labviewmodule-nodelibraryname.html)

[LabVIEWModule.NodeProperties](labviewmodule-nodeproperties.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-nodeignoresinternalerrors.html language=enus -->
## TOPIC 01348: LabVIEWModule.NodeIgnoresInternalErrors

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-nodeignoresinternalerrors.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-nodeignoresinternalerrors.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.NodeIgnoresInternalErrors Data Type Boolean Purpose Indicates that a LabVIEW Property Node should continue to process any remaining properties in the node when it encounters an error while accessing a property. See Also LabVIEWModule.NodeProperties

### LabVIEWModule.NodeIgnoresInternalErrors

#### Syntax

[LabVIEWModule](labviewmodule.html).NodeIgnoresInternalErrors

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Indicates that a LabVIEW Property Node should continue to process any remaining properties in the node when it encounters an error while accessing a property.

#### See Also

[LabVIEWModule.NodeProperties](labviewmodule-nodeproperties.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-nodelibrarygenerictypename.html language=enus -->
## TOPIC 01349: LabVIEWModule.NodeLibraryGenericTypeName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-nodelibrarygenerictypename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-nodelibrarygenerictypename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.NodeLibraryGenericTypeName Data Type String Purpose Specifies the LabVIEW I/O Library Generic Type Name when calling a LabVIEW Property Node. See Also LabVIEWModule.NodeClassDataName LabVIEWModule.NodeLibraryName LabVIEWModule.NodeProperties

### LabVIEWModule.NodeLibraryGenericTypeName

#### Syntax

[LabVIEWModule](labviewmodule.html).NodeLibraryGenericTypeName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the LabVIEW I/O Library Generic Type Name when calling a LabVIEW Property Node.

#### See Also

[LabVIEWModule.NodeClassDataName](labviewmodule-nodeclassdataname.html)

[LabVIEWModule.NodeLibraryName](labviewmodule-nodelibraryname.html)

[LabVIEWModule.NodeProperties](labviewmodule-nodeproperties.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-nodelibraryname.html language=enus -->
## TOPIC 01350: LabVIEWModule.NodeLibraryName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-nodelibraryname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-nodelibraryname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.NodeLibraryName Data Type String Purpose Specifies the LabVIEW I/O Library Name when calling a LabVIEW Property Node. See Also LabVIEWModule.NodeClassDataName LabVIEWModule.NodeLibraryGenericTypeName LabVIEWModule.NodeProperties

### LabVIEWModule.NodeLibraryName

#### Syntax

[LabVIEWModule](labviewmodule.html).NodeLibraryName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the LabVIEW I/O Library Name when calling a LabVIEW Property Node.

#### See Also

[LabVIEWModule.NodeClassDataName](labviewmodule-nodeclassdataname.html)

[LabVIEWModule.NodeLibraryGenericTypeName](labviewmodule-nodelibrarygenerictypename.html)

[LabVIEWModule.NodeProperties](labviewmodule-nodeproperties.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-nodeoperationmode.html language=enus -->
## TOPIC 01351: LabVIEWModule.NodeOperationMode

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-nodeoperationmode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-nodeoperationmode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.NodeOperationMode Data Type LabVIEWNodeOperationModes Use the following constants with this data type: LVNodeOperationMode_Default –(Value: 0) Indicates that the Configure Property Node dialog box operates in default mode. LVNodeOperationMode_Restricted –(Value: 1) Indicates tha

### LabVIEWModule.NodeOperationMode

#### Syntax

[LabVIEWModule](labviewmodule.html).NodeOperationMode

#### Data Type

[LabVIEWNodeOperationModes](labviewnodeoperationmodes.html)

Use the following constants with this data type:

- LVNodeOperationMode_Default 
 –(Value: 0) Indicates that the
 Configure Property Node 
 dialog box operates in default mode.
- LVNodeOperationMode_Restricted 
 –(Value: 1) Indicates that the
 Configure Property Node 
 dialog box operates in restricted mode.

#### Purpose

Indicates the mode of operation of the
 [Configure Property Node](../tsref/configure-property-node-dialog-box.html)
 dialog box for LabVIEW property calls.

#### See Also

[Configure Property Node dialog box](../tsref/configure-property-node-dialog-box.html)

[LabVIEWModule.NodeClassDataName](labviewmodule-nodeclassdataname.html)

[LabVIEWModule.NodeIgnoresInternalErrors](labviewmodule-nodeignoresinternalerrors.html)

[LabVIEWModule.NodeLibraryGenericTypeName](labviewmodule-nodelibrarygenerictypename.html)

[LabVIEWModule.NodeLibraryName](labviewmodule-nodelibraryname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-nodeproperties.html language=enus -->
## TOPIC 01352: LabVIEWModule.NodeProperties

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-nodeproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-nodeproperties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.NodeProperties Data Type LabVIEWNodeProperties Purpose Contains the properties to use in a step configured to call a LabVIEW Property Node. See Also LabVIEWModule.NodeClassDataName LabVIEWModule.NodeIgnoresInternalErrors LabVIEWModule.NodeLibraryGenericTypeName LabVIEWModule.Nod

### LabVIEWModule.NodeProperties

#### Syntax

[LabVIEWModule](labviewmodule.html).NodeProperties

#### Data Type

[LabVIEWNodeProperties](labviewnodeproperties.html)

#### Purpose

Contains the properties to use in a step configured to call a LabVIEW Property Node.

#### See Also

[LabVIEWModule.NodeClassDataName](labviewmodule-nodeclassdataname.html)

[LabVIEWModule.NodeIgnoresInternalErrors](labviewmodule-nodeignoresinternalerrors.html)

[LabVIEWModule.NodeLibraryGenericTypeName](labviewmodule-nodelibrarygenerictypename.html)

[LabVIEWModule.NodeLibraryName](labviewmodule-nodelibraryname.html)

[LabVIEWNodeProperty.LongName](labviewnodeproperty-longname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-nodeusesdatavaluereference.html language=enus -->
## TOPIC 01353: LabVIEWModule.NodeUsesDataValueReference

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-nodeusesdatavaluereference.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-nodeusesdatavaluereference.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.NodeUsesDataValueReference Data Type Boolean Purpose Indicates that the step accesses a LabVIEW class indirectly through a Data Reference Value (DVR) rather than directly by using an object reference. Remarks This property is valid only when you build a LabVIEW Property Node for

### LabVIEWModule.NodeUsesDataValueReference

#### Syntax

[LabVIEWModule](labviewmodule.html).NodeUsesDataValueReference

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Indicates that the step accesses a LabVIEW class indirectly through a Data Reference Value (DVR) rather than directly by using an object reference.

#### Remarks

This property is valid only when you build a LabVIEW Property Node for a LabVIEW Class.

#### See Also

[LabVIEWModule.NodeClassDataName](labviewmodule-nodeclassdataname.html)

[LabVIEWModule.NodeLibraryName](labviewmodule-nodelibraryname.html)

[LabVIEWModule.NodeProperties](labviewmodule-nodeproperties.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-overridebinaryclasspath.html language=enus -->
## TOPIC 01354: LabVIEWModule.OverrideBinaryClassPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-overridebinaryclasspath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-overridebinaryclasspath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.OverrideBinaryClassPath Data Type String Purpose Specifies the path of the LabVIEW class in the packed project library, configured in the Override Module Settings window, used if Always run VI in Packed Project Library is enabled. Remarks You can specify an absolute or relative

### LabVIEWModule.OverrideBinaryClassPath

#### Syntax

[LabVIEWModule](labviewmodule.html).OverrideBinaryClassPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the path of the LabVIEW class in the packed project library, configured in the Override Module Settings window, used if Always run VI in Packed Project Library is enabled.

#### Remarks

You can specify an absolute or relative pathname for the file. Relative pathnames are relative to the TestStand
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### See Also

[LabVIEWModule](labviewmodule.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-overridebinarynamespace.html language=enus -->
## TOPIC 01355: LabVIEWModule.OverrideBinaryNamespace

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-overridebinarynamespace.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-overridebinarynamespace.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.OverrideBinaryNamespace Data Type String Purpose Returns the LabVIEW namespace of the binary VI. The namespace of the binary VI is the qualified name of the owning LabVIEW project library.

### LabVIEWModule.OverrideBinaryNamespace

#### Syntax

[LabVIEWModule](labviewmodule.html).OverrideBinaryNamespace

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the LabVIEW namespace of the binary VI. The namespace of the binary VI is the qualified name of the owning LabVIEW project library.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-overridebinaryprojectpath.html language=enus -->
## TOPIC 01356: LabVIEWModule.OverrideBinaryProjectPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-overridebinaryprojectpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-overridebinaryprojectpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.OverrideBinaryProjectPath Data Type String Purpose Specifies the path of the LabVIEW project that the LabVIEW Adapter runs when Always run VI in Packed Project Library is enabled. Remarks You can specify an absolute or relative pathname for the file. Relative pathnames are relat

### LabVIEWModule.OverrideBinaryProjectPath

#### Syntax

[LabVIEWModule](labviewmodule.html).OverrideBinaryProjectPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the path of the LabVIEW project that the LabVIEW Adapter runs when Always run VI in Packed Project Library is enabled.

#### Remarks

You can specify an absolute or relative pathname for the file. Relative pathnames are relative to the TestStand
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### See Also

[LabVIEWModule](labviewmodule.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-overridebinaryvipath.html language=enus -->
## TOPIC 01357: LabVIEWModule.OverrideBinaryVIPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-overridebinaryvipath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-overridebinaryvipath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.OverrideBinaryVIPath Data Type String Purpose Specifies the path of the VI in the packed project library, configured in the Override Module Settings window, that the LabVIEW Adapter runs if Always run VI in Packed Project Library is enabled. Remarks You can specify an absolute o

### LabVIEWModule.OverrideBinaryVIPath

#### Syntax

[LabVIEWModule](labviewmodule.html).OverrideBinaryVIPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the path of the VI in the packed project library, configured in the Override Module Settings window, that the LabVIEW Adapter runs if Always run VI in Packed Project Library is enabled.

#### Remarks

You can specify an absolute or relative pathname for the file. Relative pathnames are relative to the TestStand
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### See Also

[LabVIEWModule](labviewmodule.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-overridemoduleoptions.html language=enus -->
## TOPIC 01358: LabVIEWModule.OverrideModuleOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-overridemoduleoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-overridemoduleoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.OverrideModuleOptions Data Type LabVIEWModuleOverrideOptions Use the following constants with this data type: LabVIEWModuleOverrideOption_Default –(Value: 0) Indicates that the LabVIEW Adapter runs the VI configured in the code module. LabVIEWModuleOverrideOption_PPL –(Value: 1)

### LabVIEWModule.OverrideModuleOptions

#### Syntax

[LabVIEWModule](labviewmodule.html).OverrideModuleOptions

#### Data Type

[LabVIEWModuleOverrideOptions](labviewmoduleoverrideoptions.html)

Use the following constants with this data type:

- LabVIEWModuleOverrideOption_Default 
 –(Value: 0) Indicates that the LabVIEW Adapter runs the VI configured in the code module.
- LabVIEWModuleOverrideOption_PPL 
 –(Value: 1) Indicates that the LabVIEW Adapter runs the VI in the packed project library configured in the Override Module Settings window.

#### Purpose

Specifies the override option to use.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-parameters.html language=enus -->
## TOPIC 01359: LabVIEWModule.Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.Parameters Data Type LabVIEWParameters The collection of parameters. Purpose Returns the LabVIEWParameters collection that contains a list of the current parameters used as inputs and outputs of the corresponding module. Remarks Call the Module.LoadPrototype method before access

### LabVIEWModule.Parameters

#### Syntax

[LabVIEWModule](labviewmodule.html).Parameters

#### Data Type

[LabVIEWParameters](labviewparameters.html)

The collection of parameters.

#### Purpose

Returns the
 [LabVIEWParameters](labviewparameters.html)
 collection that contains a list of the current parameters used as inputs and outputs of the corresponding module.

#### Remarks

Call the
 [Module.LoadPrototype](module-loadprototype.html)
 method before accessing this property.

#### See Also

[LabVIEWParameters](labviewparameters.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-projectpath.html language=enus -->
## TOPIC 01360: LabVIEWModule.ProjectPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-projectpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-projectpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.ProjectPath Data Type String Purpose Specifies the path and name of the LabVIEW project the LabVIEWModule calls. Remarks You can specify an absolute or relative pathname for the file. Relative pathnames are relative to the TestStand search directory paths . See Also LabVIEWModul

### LabVIEWModule.ProjectPath

#### Syntax

[LabVIEWModule](labviewmodule.html).ProjectPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the path and name of the LabVIEW project the
 LabVIEWModule
 calls.

#### Remarks

You can specify an absolute or relative pathname for the file. Relative pathnames are relative to the TestStand
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### See Also

[LabVIEWModule.RemoteProjectPath](labviewmodule-remoteprojectpath.html)

[LabVIEWModule.VIPath](labviewmodule-vipath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-remoteconnectiontimeout.html language=enus -->
## TOPIC 01361: LabVIEWModule.RemoteConnectionTimeout

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-remoteconnectiontimeout.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-remoteconnectiontimeout.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.RemoteConnectionTimeout Data Type Long Purpose Specifies the time to wait for a connection before timing out, in milliseconds. Remarks If the LabVIEWModule.RemoteHost property is empty, this property is ignored. See Also LabVIEWModule.RemoteHost LabVIEWModule.RemotePortNumber La

### LabVIEWModule.RemoteConnectionTimeout

#### Syntax

[LabVIEWModule](labviewmodule.html).RemoteConnectionTimeout

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the time to wait for a connection before timing out, in milliseconds.

#### Remarks

If the
 [LabVIEWModule.RemoteHost](labviewmodule-remotehost.html)
 property is empty, this property is ignored.

#### See Also

[LabVIEWModule.RemoteHost](labviewmodule-remotehost.html)

[LabVIEWModule.RemotePortNumber](labviewmodule-remoteportnumber.html)

[LabVIEWModule.RemoteVIPath](labviewmodule-remotevipath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-remotehost.html language=enus -->
## TOPIC 01362: LabVIEWModule.RemoteHost

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-remotehost.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-remotehost.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.RemoteHost Data Type String Purpose Specifies the remote system on which to run the VI. Leave this property empty if you are not using a remote system. Remarks If the LabVIEWModule.SpecifyHostByExpression property is True , the value of this property must be in the format of an

### LabVIEWModule.RemoteHost

#### Syntax

[LabVIEWModule](labviewmodule.html).RemoteHost

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the remote system on which to run the VI. Leave this property empty if you are not using a remote system.

#### Remarks

If the
 [LabVIEWModule.SpecifyHostByExpression](labviewmodule-specifyhostbyexpression.html)
 property is
 True
 , the value of this property must be in the format of an expression.

#### See Also

[LabVIEWModule.RemoteConnectionTimeout](labviewmodule-remoteconnectiontimeout.html)

[LabVIEWModule.RemotePortNumber](labviewmodule-remoteportnumber.html)

[LabVIEWModule.RemoteVIPath](labviewmodule-remotevipath.html)

[LabVIEWModule.SpecifyHostByExpression](labviewmodule-specifyhostbyexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-remoteportnumber.html language=enus -->
## TOPIC 01363: LabVIEWModule.RemotePortNumber

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-remoteportnumber.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-remoteportnumber.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.RemotePortNumber Data Type Long Purpose Specifies the port number to use to connect to the remote system. Remarks If the LabVIEWModule.RemoteHost property is empty, this property is ignored. See Also LabVIEWModule.RemoteConnectionTimeout LabVIEWModule.RemoteHost LabVIEWModule.Re

### LabVIEWModule.RemotePortNumber

#### Syntax

[LabVIEWModule](labviewmodule.html).RemotePortNumber

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the port number to use to connect to the remote system.

#### Remarks

If the
 [LabVIEWModule.RemoteHost](labviewmodule-remotehost.html)
 property is empty, this property is ignored.

#### See Also

[LabVIEWModule.RemoteConnectionTimeout](labviewmodule-remoteconnectiontimeout.html)

[LabVIEWModule.RemoteHost](labviewmodule-remotehost.html)

[LabVIEWModule.RemoteVIPath](labviewmodule-remotevipath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-remoteprojectpath.html language=enus -->
## TOPIC 01364: LabVIEWModule.RemoteProjectPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-remoteprojectpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-remoteprojectpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.RemoteProjectPath Data Type String Purpose Specifies the path and name of the LabVIEW project the step calls on the remote system. Use the LabVIEWModule.RemoteVIPath property to specify the URL of the VI to call within the defined LabVIEW project. See Also LabVIEWModule.ProjectP

### LabVIEWModule.RemoteProjectPath

#### Syntax

[LabVIEWModule](labviewmodule.html).RemoteProjectPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the path and name of the LabVIEW project the step calls on the remote system. Use the
 [LabVIEWModule.RemoteVIPath](labviewmodule-remotevipath.html)
 property to specify the URL of the VI to call within the defined LabVIEW project.

#### See Also

[LabVIEWModule.ProjectPath](labviewmodule-projectpath.html)

[LabVIEWModule.RemoteConnectionTimeout](labviewmodule-remoteconnectiontimeout.html)

[LabVIEWModule.RemoteHost](labviewmodule-remotehost.html)

[LabVIEWModule.RemotePortNumber](labviewmodule-remoteportnumber.html)

[LabVIEWModule.RemoteVIPath](labviewmodule-remotevipath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-remotevipath.html language=enus -->
## TOPIC 01365: LabVIEWModule.RemoteVIPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-remotevipath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-remotevipath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.RemoteVIPath Data Type String Purpose Specifies the path and name of the VI the step calls on the remote system. Remarks If the path is relative, the remote system interprets the path as relative to the application directory, if applicable. If an absolute or relative path is spe

### LabVIEWModule.RemoteVIPath

#### Syntax

[LabVIEWModule](labviewmodule.html).RemoteVIPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the path and name of the VI the step calls on the remote system.

#### Remarks

If the path is relative, the remote system interprets the path as relative to the application directory, if applicable. If an absolute or relative path is specified, the VI is loaded into memory on the remote system, if it is not already open. If a VI of the same name is already in memory, that VI is used regardless of whether the path is the same as the path specified.

If a path is not specified for this property, the VI specified in the
 [LabVIEWModule.VIPath](labviewmodule-vipath.html)
 property downloads to the remote system if it is not already in memory and if the remote system is running LabVIEW Real-Time Module.

If the step uses a remote project path, the
 [LabVIEWModule.RemoteVIPath](labviewmodule-remotevipath.html)
 property specifies the URL of the VI within the defined LabVIEW project. If the
 [LabVIEWModule.RemoteHost](labviewmodule-remotehost.html)
 property is empty, this property is ignored.

#### See Also

[LabVIEWModule.RemoteConnectionTimeout](labviewmodule-remoteconnectiontimeout.html)

[LabVIEWModule.RemoteHost](labviewmodule-remotehost.html)

[LabVIEWModule.RemotePortNumber](labviewmodule-remoteportnumber.html)

[LabVIEWModule.VIPath](labviewmodule-vipath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-specifyhostbyexpression.html language=enus -->
## TOPIC 01366: LabVIEWModule.SpecifyHostByExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-specifyhostbyexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-specifyhostbyexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.SpecifyHostByExpression Data Type Boolean Purpose Specifies that the LabVIEWModule.RemoteHost property contains an expression the LabVIEW Adapter evaluates at run time to determine the name of the remote host. Remarks If RemoteHost is empty, this property is ignored. See Also La

### LabVIEWModule.SpecifyHostByExpression

#### Syntax

[LabVIEWModule](labviewmodule.html).SpecifyHostByExpression

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies that the
 [LabVIEWModule.RemoteHost](labviewmodule-remotehost.html)
 property contains an expression the LabVIEW Adapter evaluates at run time to determine the name of the remote host.

#### Remarks

If RemoteHost is empty, this property is ignored.

#### See Also

[LabVIEWModule.RemoteHost](labviewmodule-remotehost.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-validateoverridesettings.html language=enus -->
## TOPIC 01367: LabVIEWModule.ValidateOverrideSettings

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-validateoverridesettings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-validateoverridesettings.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.ValidateOverrideSettings( options, errorMessage) Return Value Boolean Purpose Validates the override settings and returns false if there are errors. Parameters options As Long [In] Not used. errorMessage As String [Out] Specifies the error found while validating the override set

### LabVIEWModule.ValidateOverrideSettings

#### Syntax

[LabVIEWModule](labviewmodule.html).ValidateOverrideSettings( options, errorMessage)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Validates the override settings and returns false if there are errors.

#### Parameters

options
 As
 [Long](data-types-for-teststand.html)

[In] Not used.

errorMessage
 As
 [String](data-types-for-teststand.html)

[Out] Specifies the error found while validating the override settings.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-viattached.html language=enus -->
## TOPIC 01368: LabVIEWModule.VIAttached

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-viattached.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-viattached.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.VIAttached Data Type Boolean Purpose Returns a value that indicates whether the module contains an embedded VI. Remarks You can embed a VI by calling the LabVIEWModule.ImportVI method. See Also LabVIEWModule.ExportVI LabVIEWModule.ImportVI

### LabVIEWModule.VIAttached

#### Syntax

[LabVIEWModule](labviewmodule.html).VIAttached

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the module contains an embedded VI.

#### Remarks

You can embed a VI by calling the
 [LabVIEWModule.ImportVI](labviewmodule-importvi.html)
 method.

#### See Also

[LabVIEWModule.ExportVI](labviewmodule-exportvi.html)

[LabVIEWModule.ImportVI](labviewmodule-importvi.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-vicalloptions.html language=enus -->
## TOPIC 01369: LabVIEWModule.VICallOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-vicalloptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-vicalloptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.VICallOptions Data Type Long Purpose Specifies options for calling the VI of the module. See Also LabVIEWModuleCallOptions

### LabVIEWModule.VICallOptions

#### Syntax

[LabVIEWModule](labviewmodule.html).VICallOptions

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies
 [options](labviewmodulecalloptions.html)
 for calling the VI of the module.

#### See Also

[LabVIEWModuleCallOptions](labviewmodulecalloptions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-videscription.html language=enus -->
## TOPIC 01370: LabVIEWModule.VIDescription

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-videscription.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-videscription.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.VIDescription Data Type String Purpose Returns the description of the VI. Remarks If no description exists for the VI, this property returns an empty string. The LabVIEW Adapter persists this property value when you specify a code module for a step. For an unspecified step, you

### LabVIEWModule.VIDescription

#### Syntax

[LabVIEWModule](labviewmodule.html).VIDescription

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the description of the VI.

#### Remarks

If no description exists for the VI, this property returns an empty string.

The LabVIEW Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the
 [Module.LoadPrototype](module-loadprototype.html)
 method before retrieving this property.

#### See Also

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-vipath.html language=enus -->
## TOPIC 01371: LabVIEWModule.VIPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-vipath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-vipath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.VIPath Data Type String Purpose Specifies the path and name of the VI the LabVIEWModule calls. For remote systems, this property specifies which VI the module calls unless the LabVIEWModule.RemoteVIPath property specifies a path and name of a VI. Remarks You can specify an absol

### LabVIEWModule.VIPath

#### Syntax

[LabVIEWModule](labviewmodule.html).VIPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the path and name of the VI the LabVIEWModule calls. For remote systems, this property specifies which VI the module calls unless the
 [LabVIEWModule.RemoteVIPath](labviewmodule-remotevipath.html)
 property specifies a path and name of a VI.

#### Remarks

You can specify an absolute or relative pathname for the file. Relative pathnames are relative to the TestStand
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### See Also

[LabVIEWModule.RemoteVIPath](labviewmodule-remotevipath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule-vitype.html language=enus -->
## TOPIC 01372: LabVIEWModule.VIType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule-vitype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule-vitype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWModule.VIType Data Type LabVIEWVITypes Use the following constants with this data type: LVVIType_Express –(Value: 1) Indicates that the VI module calls an Express VI. LVVIType_Standard –(Value: 0) Indicates that the VI module calls a standard VI. Purpose Specifies the type of VI the mo

### LabVIEWModule.VIType

#### Syntax

[LabVIEWModule](labviewmodule.html).VIType

#### Data Type

[LabVIEWVITypes](labviewvitypes.html)

Use the following constants with this data type:

- LVVIType_Express 
 –(Value: 1) Indicates that the VI module calls an Express VI.
- LVVIType_Standard 
 –(Value: 0) Indicates that the VI module calls a standard VI.

#### Purpose

Specifies the type of VI the module is calling.

#### Remarks

If you set
 [LabVIEWVITypes](labviewvitypes.html)
 to LVVIType_Express, you need to call
 [ImportVI](labviewmodule-importvi.html)
 to import the Express VI you want to call.

#### See Also

[LabVIEWModule.ImportVI](labviewmodule-importvi.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodule.html language=enus -->
## TOPIC 01373: LabVIEWModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEWModule class to specify and obtain LabVIEW Adapter-specific information about the code module that steps or step type substeps execute. Use the Step.Module property to obtain a reference to a LabVIEWModule object. To access the properties and methods of a specific module

### LabVIEWModule

Use objects from the
 LabVIEWModule
 class to specify and obtain LabVIEW Adapter-specific information about the code module that steps or step type substeps execute. Use the
 
 [Step.Module](step-module.html)
 property to obtain a reference to a
 LabVIEWModule
 object. To access the properties and methods of a specific module class, query the
 Module
 object for the interface of the module-specific interface you want to acquire.

Typically, you use this class only when you are writing a sequence editor.

To access the properties and methods of the
 Module
 class, use the
 [LabVIEWModule.AsModule](labviewmodule-asmodule.html)
 method to obtain an object.

Use the
 
 [Module.LoadPrototype](module-loadprototype.html)
 method to load the prototype for the module the step specifies.

#### Properties

| BuildSpecificationName |
| --- |
| CallName |
| CallType |
| ClassPath |
| ExpressVIName (Read Only) |
| HelpContext (Read Only) |
| HelpFilePath (Read Only) |
| HelpPicture (Read Only) |
| HelpPictureRects (Read Only) |
| MatchArrayParametersToLabVIEWArrayDimensions |
| Namespace |
| NodeClassDataName |
| NodeIgnoresInternalErrors |
| NodeLibraryGenericTypeName |
| NodeLibraryName |
| NodeOperationMode |
| NodeProperties (Read Only) |
| NodeUsesDataValueReference |
| OverrideBinaryClassPath |
| OverrideBinaryNamespace |
| OverrideBinaryProjectPath |
| OverrideBinaryVIPath |
| OverrideModuleOptions |
| Parameters (Read Only) |
| ProjectPath |
| RemoteConnectionTimeout |
| RemoteHost |
| RemotePortNumber |
| RemoteProjectPath |
| RemoteVIPath |
| SpecifyHostByExpression |
| VIAttached (Read Only) |
| VICallOptions |
| VIDescription (Read Only) |
| VIPath |
| VIType |

#### Methods

| AsModule |
| --- |
| BuildBinary |
| ConvertExpressVIToStandardVI |
| ConvertToStandardVI |
| CreateProject |
| DisplayParameterMappingDialog |
| DisplaySelectClassFromProjectDialog |
| DisplaySelectClassFromProjectDialogEx |
| DisplaySelectClassMemberFromProjectDialog |
| DisplaySelectMemberFromClassDialog |
| DisplaySelectVIFromProjectDialog |
| DisplaySelectVIFromProjectDialogEx |
| EditClass |
| EditProject |
| Execute |
| ExportVI |
| FindClassUrlUsingClassPath |
| FindClassUrlUsingClassPathEx |
| FindVIUrlUsingVIPath |
| FindVIUrlUsingVIPathEx |
| GetBinaryBuildSpecifications |
| GetClassAbsolutePath |
| GetClassAbsolutePathEx |
| GetProjectUrlPathsForClasses |
| GetProjectUrlPathsForVIs |
| GetVIAbsolutePath |
| GetVIAbsolutePathEx |
| ImportVI |
| IsProjectValid |
| LoadVIInfo |
| ValidateOverrideSettings |

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[Module](module.html)

[Module.LoadPrototype](module-loadprototype.html)

[Step.Module](step-module.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmodulecalloptions.html language=enus -->
## TOPIC 01374: LabVIEWModuleCallOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmodulecalloptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmodulecalloptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following constants with the LabVIEWModule.VICallOptions method to get or set options for calling the VI for the module. Use the bitwise-AND operator to determine whether either of these flags are set when obtaining the property value. Use the bitwise-OR operator to set both flags when setti

### LabVIEWModuleCallOptions

Use the following constants with the
 [LabVIEWModule.VICallOptions](labviewmodule-vicalloptions.html)
 method to get or set options for calling the VI for the module. Use the bitwise-AND operator to determine whether either of these flags are set when obtaining the property value. Use the bitwise-OR operator to set both flags when setting the property value.

- LVModuleOptions_AutoDetectLVRT 
 –(Value: 0x2) Specifies to automatically detect the version of the LabVIEW Run-Time server to call when executing the VI of the module.
- LVModuleOptions_ShowFrontPanel 
 –(Value: 0x1) Specifies to activate the front panel of the VI of the module when called.

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEWModule.VICallOptions](labviewmodule-vicalloptions.html)

Parent topic:

Adapter API-Related Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmoduleoverrideoptions.html language=enus -->
## TOPIC 01375: LabVIEWModuleOverrideOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmoduleoverrideoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmoduleoverrideoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the LabVIEWModule.OverrideModuleOptions and LabVIEWAdapter.OverrideModuleOptions properties to specify the override option to use. LabVIEWModuleOverrideOption_Default –(Value: 0) Indicates that the LabVIEW Adapter runs the VI configured in the code module. LabVIEWModuleOverr

### LabVIEWModuleOverrideOptions

Use these constants with the
 [LabVIEWModule.OverrideModuleOptions](labviewmodule-overridemoduleoptions.html)
 and
 [LabVIEWAdapter.OverrideModuleOptions](labviewadapter-overridemoduleoptions.html)
 properties to specify the override option to use.

- LabVIEWModuleOverrideOption_Default 
 –(Value: 0) Indicates that the LabVIEW Adapter runs the VI configured in the code module.
- LabVIEWModuleOverrideOption_PPL 
 –(Value: 1) Indicates that the LabVIEW Adapter runs the VI in the packed project library configured in the Override Module Settings window.

#### See Also

[LabVIEWModule.OverrideModuleOptions](labviewmodule-overridemoduleoptions.html)

[LabVIEWAdapter.OverrideModuleOptions](labviewadapter-overridemoduleoptions.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewmoduleoverridetypes.html language=enus -->
## TOPIC 01376: LabVIEWModuleOverrideTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewmoduleoverridetypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewmoduleoverridetypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the LabVIEWModule.DisplaySelectClassFromProjectDialogEx , LabVIEWModule.DisplaySelectVIFromProjectDialogEx , LabVIEWModule.FindClassUrlUsingClassPathEx , LabVIEWModule.FindVIUrlUsingVIPathEx , LabVIEWModule.GetClassAbsolutePathEx , and LabVIEWModule.GetVIAbsolutePathEx metho

### LabVIEWModuleOverrideTypes

Use these constants with the
 [LabVIEWModule.DisplaySelectClassFromProjectDialogEx](labviewmodule-displayselectclassfromprojectdi.html)
 ,
 [LabVIEWModule.DisplaySelectVIFromProjectDialogEx](labviewmodule-displayselectvifromprojectdialo.html)
 ,
 [LabVIEWModule.FindClassUrlUsingClassPathEx](labviewmodule-findclassurlusingclasspathex.html)
 ,
 [LabVIEWModule.FindVIUrlUsingVIPathEx](labviewmodule-findviurlusingvipathex.html)
 ,
 [LabVIEWModule.GetClassAbsolutePathEx](labviewmodule-getclassabsolutepathex.html)
 , and
 [LabVIEWModule.GetVIAbsolutePathEx](labviewmodule-getviabsolutepathex.html)
 methods to specify the override type.

- LabVIEWModuleOverrideType_Default 
 –(Value: 0) Directs the methods to use the VI configured in the code module.
- LabVIEWModuleOverrideType_PPL 
 –(Value: 1) Directs the methods to use the VI in the packed project library configured in the Override Module Settings window.

#### See Also

[LabVIEWModule.DisplaySelectClassFromProjectDialogEx](labviewmodule-displayselectclassfromprojectdi.html)

[LabVIEWModule.DisplaySelectVIFromProjectDialogEx](labviewmodule-displayselectvifromprojectdialo.html)

[LabVIEWModule.FindClassUrlUsingClassPathEx](labviewmodule-findclassurlusingclasspathex.html)

[LabVIEWModule.FindVIUrlUsingVIPathEx](labviewmodule-findviurlusingvipathex.html)

[LabVIEWModule.GetClassAbsolutePathEx](labviewmodule-getclassabsolutepathex.html)

[LabVIEWModule.GetVIAbsolutePathEx](labviewmodule-getviabsolutepathex.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnodeoperationmodes.html language=enus -->
## TOPIC 01377: LabVIEWNodeOperationModes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnodeoperationmodes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnodeoperationmodes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the LabVIEWModule.NodeOperationMode property to indicate the behavior of the Configure Property Node dialog box. LVNodeOperationMode_Default –(Value: 0) Indicates that the Configure Property Node dialog box operates in default mode. LVNodeOperationMode_Restricted –(Value: 1)

### LabVIEWNodeOperationModes

Use these constants with the
 [LabVIEWModule.NodeOperationMode](labviewmodule-nodeoperationmode.html)
 property to indicate the behavior of the
 [Configure Property Node](../tsref/configure-property-node-dialog-box.html)
 dialog box.

- LVNodeOperationMode_Default 
 –(Value: 0) Indicates that the
 Configure Property Node 
 dialog box operates in default mode.
- LVNodeOperationMode_Restricted 
 –(Value: 1) Indicates that the
 Configure Property Node 
 dialog box operates in restricted mode.

#### See Also

[LabVIEWModule.NodeOperationMode](labviewmodule-nodeoperationmode.html)

[Configure Property Node dialog box](../tsref/configure-property-node-dialog-box.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnodeproperties-clear.html language=enus -->
## TOPIC 01378: LabVIEWNodeProperties.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnodeproperties-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnodeproperties-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNodeProperties.Clear Purpose Removes all items from the collection.

### LabVIEWNodeProperties.Clear

#### Syntax

[LabVIEWNodeProperties](labviewnodeproperties.html).Clear

#### Purpose

Removes all items from the collection.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnodeproperties-count.html language=enus -->
## TOPIC 01379: LabVIEWNodeProperties.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnodeproperties-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnodeproperties-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNodeProperties.Count Data Type Long Purpose Returns the number of items in the collection.

### LabVIEWNodeProperties.Count

#### Syntax

[LabVIEWNodeProperties](labviewnodeproperties.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnodeproperties-delete.html language=enus -->
## TOPIC 01380: LabVIEWNodeProperties.Delete

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnodeproperties-delete.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnodeproperties-delete.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNodeProperties.Delete( index) Purpose Removes the item at the specified index. Parameters index As Long [In] Specifies the zero-based index of the item to delete.

### LabVIEWNodeProperties.Delete

#### Syntax

[LabVIEWNodeProperties](labviewnodeproperties.html).Delete( index)

#### Purpose

Removes the item at the specified index.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to delete.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnodeproperties-item.html language=enus -->
## TOPIC 01381: LabVIEWNodeProperties.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnodeproperties-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnodeproperties-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNodeProperties.Item( index) Data Type LabVIEWNodeProperty Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index.

### LabVIEWNodeProperties.Item

#### Syntax

[LabVIEWNodeProperties](labviewnodeproperties.html).Item( index)

#### Data Type

[LabVIEWNodeProperty](labviewnodeproperty.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnodeproperties-new.html language=enus -->
## TOPIC 01382: LabVIEWNodeProperties.New

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnodeproperties-new.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnodeproperties-new.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNodeProperties.New( index, longName, dataName, uniqueID, nodePropertyDirection) Purpose Adds a new item to the collection. Parameters index As Long [In] Specifies the zero-based index of the item to add. longName As String [In] Specifies the LongName of a particular property. dataName

### LabVIEWNodeProperties.New

#### Syntax

[LabVIEWNodeProperties](labviewnodeproperties.html).New( index, longName, dataName, uniqueID, nodePropertyDirection)

#### Purpose

Adds a new item to the collection.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to add.

longName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the LongName of a particular property.

dataName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the DataName of a particular property.

uniqueID
 As
 [String](data-types-for-teststand.html)

[In] Specifies the unique ID of a particular property.

nodePropertyDirection
 As
 [LabVIEWNodePropertyDirections](labviewnodepropertydirections.html)

[In] Indicates the direction of the property.
 0
 indicates an In property.
 1
 indicates an Out property.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnodeproperties.html language=enus -->
## TOPIC 01383: LabVIEWNodeProperties

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnodeproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnodeproperties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEWNodeProperties class to configure and obtain LabVIEWNodeProperties for a module that uses the LabVIEW Adapter. Use the LabVIEWModule.NodeProperties property to obtain the collection of LabVIEWNodeProperties for a module. Properties Count (Read Only) Item (Read Only) Metho

### LabVIEWNodeProperties

Use objects from the
 LabVIEWNodeProperties
 class to configure and obtain
 LabVIEWNodeProperties
 for a module that uses the LabVIEW Adapter. Use the
 [LabVIEWModule.NodeProperties](labviewmodule-nodeproperties.html)
 property to obtain the collection of
 LabVIEWNodeProperties
 for a module.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Clear |
| --- |
| Delete |
| New |

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnodeproperty-aspropertyobject.html language=enus -->
## TOPIC 01384: LabVIEWNodeProperty.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnodeproperty-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnodeproperty-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNodeProperty.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the LabVIEWPropertyNode object. Remarks Use the PropertyObject to modify, add, or remove custom properties of the object.

### LabVIEWNodeProperty.AsPropertyObject

#### Syntax

[LabVIEWNodeProperty](labviewnodeproperty.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the LabVIEWPropertyNode object.

#### Remarks

Use the PropertyObject to modify, add, or remove custom properties of the object.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnodeproperty-dataname.html language=enus -->
## TOPIC 01385: LabVIEWNodeProperty.DataName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnodeproperty-dataname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnodeproperty-dataname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNodeProperty.DataName Data Type String Purpose Specifies the DataName of a particular property. See Also LabVIEWNodeProperty.Direction LabVIEWNodeProperty.LongName LabVIEWModule.NodeProperties

### LabVIEWNodeProperty.DataName

#### Syntax

[LabVIEWNodeProperty](labviewnodeproperty.html).DataName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the DataName of a particular property.

#### See Also

[LabVIEWNodeProperty.Direction](labviewnodeproperty-direction.html)

[LabVIEWNodeProperty.LongName](labviewnodeproperty-longname.html)

[LabVIEWModule.NodeProperties](labviewmodule-nodeproperties.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnodeproperty-direction.html language=enus -->
## TOPIC 01386: LabVIEWNodeProperty.Direction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnodeproperty-direction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnodeproperty-direction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNodeProperty.Direction Data Type LabVIEWNodePropertyDirections Use the following constants with this data type: LVNodePropertyDirection_Default –(Value: 2) Indicates that the property uses the default value. LVNodePropertyDirection_In –(Value: 0) Indicates that TestStand passes the pro

### LabVIEWNodeProperty.Direction

#### Syntax

[LabVIEWNodeProperty](labviewnodeproperty.html).Direction

#### Data Type

[LabVIEWNodePropertyDirections](labviewnodepropertydirections.html)

Use the following constants with this data type:

- LVNodePropertyDirection_Default 
 –(Value: 2) Indicates that the property uses the default value.
- LVNodePropertyDirection_In 
 –(Value: 0) Indicates that TestStand passes the property to the VI.
- LVNodePropertyDirection_Out 
 –(Value: 1) Indicates that the VI returns the property.

#### Purpose

Indicates the direction of the property.
 0
 indicates an In property.
 1
 indicates an Out property.

#### See Also

[LabVIEWNodeProperty.DataName](labviewnodeproperty-dataname.html)

[LabVIEWNodeProperty.LongName](labviewnodeproperty-longname.html)

[LabVIEWModule.NodeProperties](labviewmodule-nodeproperties.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnodeproperty-longname.html language=enus -->
## TOPIC 01387: LabVIEWNodeProperty.LongName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnodeproperty-longname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnodeproperty-longname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNodeProperty.LongName Data Type String Purpose Specifies the LongName of a particular property. See Also LabVIEWNodeProperty.DataName LabVIEWNodeProperty.Direction LabVIEWModule.NodeProperties

### LabVIEWNodeProperty.LongName

#### Syntax

[LabVIEWNodeProperty](labviewnodeproperty.html).LongName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the LongName of a particular property.

#### See Also

[LabVIEWNodeProperty.DataName](labviewnodeproperty-dataname.html)

[LabVIEWNodeProperty.Direction](labviewnodeproperty-direction.html)

[LabVIEWModule.NodeProperties](labviewmodule-nodeproperties.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnodeproperty-uniqueid.html language=enus -->
## TOPIC 01388: LabVIEWNodeProperty.UniqueID

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnodeproperty-uniqueid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnodeproperty-uniqueid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNodeProperty.UniqueID Data Type String Purpose Specifies the UniqueID of a particular property. See Also LabVIEWNodeProperty.DataName LabVIEWNodeProperty.Direction LabVIEWModule.NodeProperties

### LabVIEWNodeProperty.UniqueID

#### Syntax

[LabVIEWNodeProperty](labviewnodeproperty.html).UniqueID

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the UniqueID of a particular property.

#### See Also

[LabVIEWNodeProperty.DataName](labviewnodeproperty-dataname.html)

[LabVIEWNodeProperty.Direction](labviewnodeproperty-direction.html)

[LabVIEWModule.NodeProperties](labviewmodule-nodeproperties.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnodeproperty.html language=enus -->
## TOPIC 01389: LabVIEWNodeProperty

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnodeproperty.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnodeproperty.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEWNodeProperty class to configure and obtain LabVIEWNodeProperty-specific information for an item in the LabVIEWNodeProperties collection class. Properties DataName Direction LongName UniqueID Method AsPropertyObject See Also Effectively Using LabVIEW with TestStand LabVIEW

### LabVIEWNodeProperty

Use objects from the LabVIEWNodeProperty class to configure and obtain LabVIEWNodeProperty-specific information for an item in the
 [LabVIEWNodeProperties](labviewnodeproperties.html)
 collection class.

#### Properties

| DataName |
| --- |
| Direction |
| LongName |
| UniqueID |

#### Method

| AsPropertyObject |
| --- |

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEWModule.NodeProperties](labviewmodule-nodeproperties.html)

[LabVIEWNodeProperties](labviewnodeproperties.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnodepropertydirections.html language=enus -->
## TOPIC 01390: LabVIEWNodePropertyDirections

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnodepropertydirections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnodepropertydirections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEWNodeProperty.Direction property returns one of these constants to indicate how the code module passes the property when it executes. LVNodePropertyDirection_Default –(Value: 2) Indicates that the property uses the default value. LVNodePropertyDirection_In –(Value: 0) Indicates that TestSt

### LabVIEWNodePropertyDirections

The
 [LabVIEWNodeProperty.Direction](labviewnodeproperty-direction.html)
 property returns one of these constants to indicate how the code module passes the property when it executes.

- LVNodePropertyDirection_Default 
 –(Value: 2) Indicates that the property uses the default value.
- LVNodePropertyDirection_In 
 –(Value: 0) Indicates that TestStand passes the property to the VI.
- LVNodePropertyDirection_Out 
 –(Value: 1) Indicates that the VI returns the property.

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-asadapter.html language=enus -->
## TOPIC 01391: LabVIEWNXGAdapter.AsAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-asadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-asadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter .AsAdapter Return Value Adapter Purpose Returns the underlying module Adapter object that represents the LabVIEWNXGAdapter object. Remarks Use the underlying module Adapter object to access properties and methods that are common to all adapters. See Also Adapter

### LabVIEWNXGAdapter.AsAdapter

#### Syntax

[LabVIEWNXGAdapter](/csh?context=ts_tsapiref_labviewnxgadapter).AsAdapter

#### Return Value

[Adapter](adapter.html)

#### Purpose

Returns the underlying module Adapter object that represents the LabVIEWNXGAdapter object.

#### Remarks

Use the underlying module Adapter object to access properties and methods that are common to all adapters.

#### See Also

[Adapter](/csh?context=ts_tsapiref_adapter)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-autobuildcomponentoutput.html language=enus -->
## TOPIC 01392: LabVIEWNXGAdapter.AutoBuildComponentOutput

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-autobuildcomponentoutput.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-autobuildcomponentoutput.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.AutoBuildComponentOutput Data Type Boolean Purpose Specifies whether a GLL that is absent on disk or is out of date compared to the LabVIEW NXG source project and VIs, should be built at execution time. Remarks Enabling this option allows TestStand to launch LabVIEW NXG, eve

### LabVIEWNXGAdapter.AutoBuildComponentOutput

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).AutoBuildComponentOutput

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether a GLL that is absent on disk or is out of date compared to the LabVIEW NXG source project and VIs, should be built at execution time.

#### Remarks

Enabling this option allows TestStand to launch LabVIEW NXG, even when the LabVIEW NXG adapter is set to use the Runtime Engine. This option is only applicable when the step has the source files corresponding to the GLL (the project and VI) specified.

Note

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-currentserverversion.html language=enus -->
## TOPIC 01393: LabVIEWNXGAdapter.CurrentServerVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-currentserverversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-currentserverversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.CurrentServerVersion Data Type String Purpose Returns the version of the LabVIEW NXG server that TestStand is using to run VIs. The version contains only the major and minor version numbers, such as "2.0". Remarks A LabVIEW NXG server includes a LabVIEW NXG Development Envir

### LabVIEWNXGAdapter.CurrentServerVersion

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).CurrentServerVersion

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the version of the LabVIEW NXG server that TestStand is using to run VIs. The version contains only the major and minor version numbers, such as "2.0".

#### Remarks

A LabVIEW NXG server includes a LabVIEW NXG Development Environment and a LabVIEW NXG Run-Time Engine.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-getclassesfornodelibrary.html language=enus -->
## TOPIC 01394: LabVIEWNXGAdapter.GetClassesForNodeLibrary

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-getclassesfornodelibrary.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-getclassesfornodelibrary.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.GetClassesForNodeLibrary( typeName, classLongNames, classNames) Purpose Returns arrays that contain the long names and class names of the classes defined by the LabVIEW NXG node library you specify. Parameters typeName As String [In] Specifies the genericType of the LabVIEW

### LabVIEWNXGAdapter.GetClassesForNodeLibrary

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).GetClassesForNodeLibrary( typeName, classLongNames, classNames)

#### Purpose

Returns arrays that contain the long names and class names of the classes defined by the LabVIEW NXG node library you specify.

#### Parameters

typeName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the genericType of the LabVIEW NXG node library you select.

classLongNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the LongNames of the available properties for the LabVIEW NXG node library class you select.

classNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the DataNames of the available properties of the LabVIEW NXG node library class you select.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-getclustermemberisbinarystr.html language=enus -->
## TOPIC 01395: LabVIEWNXGAdapter.GetClusterMemberIsBinaryString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-getclustermemberisbinarystr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-getclustermemberisbinarystr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.GetClusterMemberIsBinaryString( typeDefinition, propertyLookupString) Return Value Boolean Purpose Returns True if the cluster member that corresponds to the specified type definition property contains binary data. Remarks TestStand preserves NUL bytes when setting and getti

### LabVIEWNXGAdapter.GetClusterMemberIsBinaryString

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).GetClusterMemberIsBinaryString( typeDefinition, propertyLookupString)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns True if the cluster member that corresponds to the specified type definition property contains binary data.

#### Remarks

TestStand preserves NUL bytes when setting and getting LabVIEW NXG string data for binary strings.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

#### See Also

[LabVIEWNXGAdapter.GetClusterPassingEnabled](labviewnxgadapter-getclusterpassingenabled.html)

[LabVIEWNXGAdapter.SetClusterMemberIsBinaryString](labviewnxgadapter-setclustermemberisbinarystr.html)

[LabVIEWNXGParameter.PassAsBinaryString](labviewnxgparameter-passasbinarystring.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-getclustermemberlabel.html language=enus -->
## TOPIC 01396: LabVIEWNXGAdapter.GetClusterMemberLabel

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-getclustermemberlabel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-getclustermemberlabel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.GetClusterMemberLabel( typeDefinition, propertyLookupString) Return Value String Purpose Returns the label of the cluster member that corresponds to the specified type definition property. Parameters typeDefinition As PropertyObject [In] Specifies the type definition. This m

### LabVIEWNXGAdapter.GetClusterMemberLabel

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).GetClusterMemberLabel( typeDefinition, propertyLookupString)

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns the label of the cluster member that corresponds to the specified type definition property.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the type definition.

#### See Also

[LabVIEWNXGAdapter.GetClusterPassingEnabled](labviewnxgadapter-getclusterpassingenabled.html)

[LabVIEWNXGAdapter.SetClusterMemberLabel](labviewnxgadapter-setclustermemberlabel.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-getclusterpassingenabled.html language=enus -->
## TOPIC 01397: LabVIEWNXGAdapter.GetClusterPassingEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-getclusterpassingenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-getclusterpassingenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.GetClusterPassingEnabled( typeDefinition) Return Value Boolean Purpose Returns a value that indicates whether a type definition allows the LabVIEW NXG Adapter to pass instances of the type as cluster parameters to VIs. Parameters typeDefinition As PropertyObject [In] Specifi

### LabVIEWNXGAdapter.GetClusterPassingEnabled

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).GetClusterPassingEnabled( typeDefinition)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether a type definition allows the LabVIEW NXG Adapter to pass instances of the type as cluster parameters to VIs.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

#### See Also

[LabVIEWNXGAdapter.SetClusterPassingEnabled](labviewnxgadapter-setclusterpassingenabled.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-getexcludefromcluster.html language=enus -->
## TOPIC 01398: LabVIEWNXGAdapter.GetExcludeFromCluster

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-getexcludefromcluster.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-getexcludefromcluster.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.GetExcludeFromCluster( typeDefinition, propertyLookupString) Return Value Boolean Purpose Returns a value that indicates whether the specified type definition property is excluded when converting instances of the type definition into clusters to pass as parameters to VIs. Pa

### LabVIEWNXGAdapter.GetExcludeFromCluster

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).GetExcludeFromCluster( typeDefinition, propertyLookupString)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the specified type definition property is excluded when converting instances of the type definition into clusters to pass as parameters to VIs.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

#### See Also

[LabVIEWNXGAdapter.GetClusterPassingEnabled](labviewnxgadapter-getclusterpassingenabled.html)

[LabVIEWNXGAdapter.SetExcludeFromCluster](labviewnxgadapter-setexcludefromcluster.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-getitemsingll.html language=enus -->
## TOPIC 01399: LabVIEWNXGAdapter.GetItemsInGLL

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-getitemsingll.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-getitemsingll.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.GetItemsInGLL( gllAbsolutePath) Return Value String Array Purpose Returns the qualified names of the VIs in the GLL. Parameters gllAbsolutePath As String [In] Specifies a string containing the absolute path of the GLL.

### LabVIEWNXGAdapter.GetItemsInGLL

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).GetItemsInGLL( gllAbsolutePath)

#### Return Value

[String Array](data-types-for-teststand.html)

#### Purpose

Returns the qualified names of the VIs in the GLL.

#### Parameters

gllAbsolutePath
 As
 [String](data-types-for-teststand.html)

[In] Specifies a string containing the absolute path of the GLL.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-getnodelibraries.html language=enus -->
## TOPIC 01400: LabVIEWNXGAdapter.GetNodeLibraries

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-getnodelibraries.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-getnodelibraries.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.GetNodeLibraries( typeNames, displayNames) Purpose Returns arrays that contain the typeNames and displayNames for all available LabVIEW NXG node libraries. Parameters typeNames As String Array [Out] Specifies the genericTypes of the available LabVIEW NXG node libraries. disp

### LabVIEWNXGAdapter.GetNodeLibraries

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).GetNodeLibraries( typeNames, displayNames)

#### Purpose

Returns arrays that contain the
 typeNames
 and
 displayNames
 for all available LabVIEW NXG node libraries.

#### Parameters

typeNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the
 genericTypes
 of the available LabVIEW NXG node libraries.

displayNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the
 displayNames
 of the available LabVIEW NXG node libraries.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-getpropertiesfornodeclass.html language=enus -->
## TOPIC 01401: LabVIEWNXGAdapter.GetPropertiesForNodeClass

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-getpropertiesfornodeclass.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-getpropertiesfornodeclass.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.GetPropertiesForNodeClass( typeName, className, longNames, shortNames, dataNames, uniqueIDs, helpDescriptions, options) Purpose Returns arrays that contain information about the properties of the LabVIEW NXG node library class you select, such as LongName , ShortName , DataN

### LabVIEWNXGAdapter.GetPropertiesForNodeClass

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).GetPropertiesForNodeClass( typeName, className, longNames, shortNames, dataNames, uniqueIDs, helpDescriptions, options)

#### Purpose

Returns arrays that contain information about the properties of the LabVIEW NXG node library class you select, such as
 LongName
 ,
 ShortName
 ,
 DataName
 ,
 HelpDescription
 , and
 options
 .

#### Parameters

typeName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the
 genericType
 of the LabVIEW NXG node library you select.

className
 As
 [String](data-types-for-teststand.html)

[In] Specifies the
 className
 of the LabVIEW NXG node library class you select.

longNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the
 LongNames
 of the available properties for the LabVIEW NXG node library class you select.

shortNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the
 ShortNames
 of the available properties of the LabVIEW NXG node library class you select.

dataNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the
 DataNames
 of the available properties of the LabVIEW NXG node library class you select.

uniqueIDs
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the unique IDs of the available properties for the LabVIEW NXG node library class you select.

helpDescriptions
 As
 [String Array](data-types-for-teststand.html)

[Out] Specifies the help descriptions of the available properties of the LabVIEW NXG node library class you select.

options
 As
 [Long Array](data-types-for-teststand.html)

[Out] Specifies the options for the available properties of the LabVIEW NXG node library class you select.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-getviversion.html language=enus -->
## TOPIC 01402: LabVIEWNXGAdapter.GetVIVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-getviversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-getviversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.GetVIVersion( projectOrGLLAbsolutePath, qualifiedName) Return Value String Purpose Returns the LabVIEW NXG version that saved the specified VI. The version contains only the major and minor version numbers, such as 2.0 . Parameters projectOrGLLAbsolutePath As String [In] Spe

### LabVIEWNXGAdapter.GetVIVersion

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).GetVIVersion( projectOrGLLAbsolutePath, qualifiedName)

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns the LabVIEW NXG version that saved the specified VI. The version contains only the major and minor version numbers, such as
 2.0
 .

#### Parameters

projectOrGLLAbsolutePath
 As
 [String](data-types-for-teststand.html)

[In] Specifies a string containing the absolute path of the project or GLL containing the VI.

qualifiedName
 As
 [String](data-types-for-teststand.html)

[In] Specifies a string containing the Module Qualified Name or Qualified Name of the VI respectively.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-initialize.html language=enus -->
## TOPIC 01403: LabVIEWNXGAdapter.Initialize

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-initialize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-initialize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.Initialize Purpose Initializes the LabVIEW NXG Adapter by connecting to the configured LabVIEW NXG server. Remarks If you do not call this method, the LabVIEW NXG Adapter connects to the configured LabVIEW NXG server when first needed.

### LabVIEWNXGAdapter.Initialize

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).Initialize

#### Purpose

Initializes the LabVIEW NXG Adapter by connecting to the configured LabVIEW NXG server.

#### Remarks

If you do not call this method, the LabVIEW NXG Adapter connects to the configured LabVIEW NXG server when first needed.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-isactivexserverconnectionva.html language=enus -->
## TOPIC 01404: LabVIEWNXGAdapter.IsActiveXServerConnectionValid

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-isactivexserverconnectionva.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-isactivexserverconnectionva.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.IsActiveXServerConnectionValid Data Type Boolean Purpose Returns a value that indicates whether the LabVIEW NXG ActiveX server connection TestStand is using is valid.

### LabVIEWNXGAdapter.IsActiveXServerConnectionValid

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).IsActiveXServerConnectionValid

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the LabVIEW NXG ActiveX server connection TestStand is using is valid.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-iscurrentserveraneditor.html language=enus -->
## TOPIC 01405: LabVIEWNXGAdapter.IsCurrentServerAnEditor

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-iscurrentserveraneditor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-iscurrentserveraneditor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.IsCurrentServerAnEditor Data Type Boolean Purpose Returns a value that indicates whether the LabVIEW NXG server TestStand is using to run VIs can edit VIs. Remarks A LabVIEW NXG server includes a LabVIEW NXG Development Environment and a LabVIEW NXG Run-Time Engine.

### LabVIEWNXGAdapter.IsCurrentServerAnEditor

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).IsCurrentServerAnEditor

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the LabVIEW NXG server TestStand is using to run VIs can edit VIs.

#### Remarks

A LabVIEW NXG server includes a LabVIEW NXG Development Environment and a LabVIEW NXG Run-Time Engine.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-islabviewnxginstalled.html language=enus -->
## TOPIC 01406: LabVIEWNXGAdapter.IsLabVIEWNXGInstalled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-islabviewnxginstalled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-islabviewnxginstalled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.IsLabVIEWNXGInstalled( displayVersion, longVersion, installationDirectory) Return Value Boolean Purpose Returns a value indicating if a supported version of LabVIEW NXG Development System is installed in the machine. Remarks If you do not call this method, the LabVIEW NXG Ad

### LabVIEWNXGAdapter.IsLabVIEWNXGInstalled

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).IsLabVIEWNXGInstalled( displayVersion, longVersion, installationDirectory)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value indicating if a supported version of LabVIEW NXG Development System is installed in the machine.

#### Remarks

If you do not call this method, the LabVIEW NXG Adapter connects to the configured LabVIEW NXG server when first needed.

#### Parameters

displayVersion
 As
 [String](data-types-for-teststand.html)

[Out] Returns the version of a supported LabVIEW NXG Development System installed in the machine.

longVersion
 As
 [String](data-types-for-teststand.html)

[Out] Returns the major.minor version of a supported LabVIEW NXG Development System installed in the machine.

installationDirectory
 As
 [String](data-types-for-teststand.html)

[Out] Returns the path on disk to which LabVIEW NXG is installed.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-newmodule.html language=enus -->
## TOPIC 01407: LabVIEWNXGAdapter.NewModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-newmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-newmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.NewModule Return Value LabVIEWNXGModule Purpose Creates and returns a new LabVIEWNXGModule object. Use this method to create a LabVIEWNXGModule object that you can use to execute a LabVIEW NXG VI without using a step, sequence, or execution. See Also LabVIEWNXGModule LabVIEW

### LabVIEWNXGAdapter.NewModule

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).NewModule

#### Return Value

[LabVIEWNXGModule](labviewnxgmodule.html)

#### Purpose

Creates and returns a new
 LabVIEWNXGModule
 object. Use this method to create a
 LabVIEWNXGModule
 object that you can use to execute a LabVIEW NXG VI without using a step, sequence, or execution.

#### See Also

[LabVIEWNXGModule](labviewnxgmodule.html)

[LabVIEWNXGModule.Execute](labviewnxgmodule-execute.html)

[LabVIEWNXGParameters.NewArguments](labviewnxgparameters-newarguments.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-serverinfo.html language=enus -->
## TOPIC 01408: LabVIEWNXGAdapter.ServerInfo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-serverinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-serverinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.ServerInfo Data Type LabVIEWNXGServerTypes Use the following constants with this data type: LabVIEWNXGServer_ExecServer –(Value: 0) Specifies to use a LabVIEW NXG executable server. LabVIEW NXG executable servers include a LabVIEW NXG development environment or a LabVIEW NXG

### LabVIEWNXGAdapter.ServerInfo

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).ServerInfo

#### Data Type

[LabVIEWNXGServerTypes](labviewnxgservertypes.html)

Use the following constants with this data type:

- LabVIEWNXGServer_ExecServer 
 –(Value: 0) Specifies to use a LabVIEW NXG executable server. LabVIEW NXG executable servers include a LabVIEW NXG development environment or a LabVIEW NXG application that registers itself as a LabVIEW NXG ActiveX Automation server.
- LabVIEWNXGServer_RTEServer 
 –(Value: 1) Specifies to use a LabVIEW NXG run-time server.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-setclustermemberisbinarystr.html language=enus -->
## TOPIC 01409: LabVIEWNXGAdapter.SetClusterMemberIsBinaryString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-setclustermemberisbinarystr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-setclustermemberisbinarystr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.SetClusterMemberIsBinaryString( typeDefinition, propertyLookupString, val) Purpose Specifies whether the cluster member that corresponds to the specified type definition property contains binary data. Remarks TestStand preserves NUL bytes when setting and getting LabVIEW NXG

### LabVIEWNXGAdapter.SetClusterMemberIsBinaryString

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).SetClusterMemberIsBinaryString( typeDefinition, propertyLookupString, val)

#### Purpose

Specifies whether the cluster member that corresponds to the specified type definition property contains binary data.

#### Remarks

TestStand preserves NUL bytes when setting and getting LabVIEW NXG string data for binary strings.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

val
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass True to specify that the cluster member is a binary string.

#### See Also

[LabVIEWNXGAdapter.GetClusterMemberIsBinaryString](labviewnxgadapter-getclustermemberisbinarystr.html)

[LabVIEWNXGAdapter.SetClusterPassingEnabled](labviewnxgadapter-setclusterpassingenabled.html)

[LabVIEWNXGParameter.PassAsBinaryString](labviewnxgparameter-passasbinarystring.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-setclustermemberlabel.html language=enus -->
## TOPIC 01410: LabVIEWNXGAdapter.SetClusterMemberLabel

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-setclustermemberlabel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-setclustermemberlabel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.SetClusterMemberLabel( typeDefinition, propertyLookupString, clusterMemberLabel) Purpose Specifies the label of the cluster member that corresponds to the specified type definition property. Parameters typeDefinition As PropertyObject [In] Specifies the type definition. This

### LabVIEWNXGAdapter.SetClusterMemberLabel

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).SetClusterMemberLabel( typeDefinition, propertyLookupString, clusterMemberLabel)

#### Purpose

Specifies the label of the cluster member that corresponds to the specified type definition property.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

clusterMemberLabel
 As
 [String](data-types-for-teststand.html)

[In] Specifies the label of the cluster member.

#### See Also

[LabVIEWNXGAdapter.GetClusterMemberLabel](labviewnxgadapter-getclustermemberlabel.html)

[LabVIEWNXGAdapter.SetClusterPassingEnabled](labviewnxgadapter-setclusterpassingenabled.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-setclusterpassingenabled.html language=enus -->
## TOPIC 01411: LabVIEWNXGAdapter.SetClusterPassingEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-setclusterpassingenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-setclusterpassingenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.SetClusterPassingEnabled( typeDefinition, clusterPassingEnabled) Purpose Specifies whether a type definition allows the LabVIEW NXG Adapter to pass instances of the type as cluster parameters to VIs. Parameters typeDefinition As PropertyObject [In] Specifies the type definit

### LabVIEWNXGAdapter.SetClusterPassingEnabled

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).SetClusterPassingEnabled( typeDefinition, clusterPassingEnabled)

#### Purpose

Specifies whether a type definition allows the LabVIEW NXG Adapter to pass instances of the type as cluster parameters to VIs.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

clusterPassingEnabled
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether cluster passing is enabled.

#### See Also

[LabVIEWNXGAdapter.GetClusterPassingEnabled](labviewnxgadapter-getclusterpassingenabled.html)

[LabVIEWNXGAdapter.SetExcludeFromCluster](labviewnxgadapter-setexcludefromcluster.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-setexcludefromcluster.html language=enus -->
## TOPIC 01412: LabVIEWNXGAdapter.SetExcludeFromCluster

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-setexcludefromcluster.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-setexcludefromcluster.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.SetExcludeFromCluster( typeDefinition, propertyLookupString, excludeFromCluster) Purpose Specifies whether the specified type definition property is excluded when converting instances of the type definition into clusters to pass as parameters to VIs. Parameters typeDefinitio

### LabVIEWNXGAdapter.SetExcludeFromCluster

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).SetExcludeFromCluster( typeDefinition, propertyLookupString, excludeFromCluster)

#### Purpose

Specifies whether the specified type definition property is excluded when converting instances of the type definition into clusters to pass as parameters to VIs.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

excludeFromCluster
 As
 [Boolean](data-types-for-teststand.html)

[In] Set this parameter to True to exclude the corresponding property. Otherwise, set this parameter to False.

#### See Also

[LabVIEWNXGAdapter.GetExcludeFromCluster](labviewnxgadapter-getexcludefromcluster.html)

[LabVIEWNXGAdapter.SetClusterPassingEnabled](labviewnxgadapter-setclusterpassingenabled.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter-validategllpath.html language=enus -->
## TOPIC 01413: LabVIEWNXGAdapter.ValidateGLLPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter-validategllpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter-validategllpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGAdapter.ValidateGLLPath Data Type Boolean Purpose Indicates whether the specified GLL path is a valid path.

### LabVIEWNXGAdapter.ValidateGLLPath

#### Syntax

[LabVIEWNXGAdapter](labviewnxgadapter.html).ValidateGLLPath

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Indicates whether the specified GLL path is a valid path.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgadapter.html language=enus -->
## TOPIC 01414: LabVIEWNXGAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEW NXG Adapter class to configure and obtain LabVIEW NXG Adapter-specific information about the module adapter. Call the Engine.GetAdapter or Engine.GetAdapterByKeyName method to obtain a reference to the adapter object. To access the properties and methods of the Adapter c

### LabVIEWNXGAdapter

Use objects from the LabVIEW NXG Adapter class to configure and obtain LabVIEW NXG Adapter-specific information about the module adapter. Call the
 Engine.GetAdapter
 or
 Engine.GetAdapterByKeyName
 method to obtain a reference to the adapter object.

To access the properties and methods of the Adapter class, use the
 LabVIEWNXGAdapter.AsAdapter
 method to obtain an object.

#### Properties

| AutoBuildComponentOutput |
| --- |
| CurrentServerVersion (Read Only) |
| IsActiveXServerConnectionValid (Read Only) |
| IsCurrentServerAnEditor (Read Only) |
| ValidateGLLPath |

#### Methods

| AsAdapter |
| --- |
| GetClassesForNodeLibrary |
| GetClusterMemberIsBinaryString |
| GetClusterMemberLabel |
| GetClusterPassingEnabled |
| GetExcludeFromCluster |
| GetItemsInGLL |
| GetNodeLibraries |
| GetPropertiesForNodeClass |
| GetVIVersion |
| Initialize |
| IsLabVIEWNXGInstalled |
| NewModule |
| SetClusterMemberIsBinaryString |
| SetClusterMemberLabel |
| SetClusterPassingEnabled |
| SetExcludeFromCluster |

#### See Also

[Engine.GetAdapter](engine-getadapter.html)

[Engine.GetAdapterByKeyName](engine-getadapterbykeyname.html)

[LabVIEWNXGAdapter.AsAdapter](labviewnxgadapter-asadapter.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgargument-compleximaginarypart.html language=enus -->
## TOPIC 01415: LabVIEWNXGArgument.ComplexImaginaryPart

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgargument-compleximaginarypart.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgargument-compleximaginarypart.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGArgument.ComplexImaginaryPart Data Type LabVIEWNXGArgument Purpose Returns the LabVIEWNXGArgument for the imaginary part of a complex number or array. See Also LabVIEWNXGArgument LabVIEWNXGParameter.ComplexImaginaryPartElement

### LabVIEWNXGArgument.ComplexImaginaryPart

#### Syntax

[LabVIEWNXGArgument](labviewnxgargument.html).ComplexImaginaryPart

#### Data Type

[LabVIEWNXGArgument](labviewnxgargument.html)

#### Purpose

Returns the
 LabVIEWNXGArgument
 for the imaginary part of a complex number or array.

#### See Also

[LabVIEWNXGArgument](labviewnxgargument.html)

[LabVIEWNXGParameter.ComplexImaginaryPartElement](labviewnxgparameter-compleximaginaryparteleme.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgargument-complexrealpart.html language=enus -->
## TOPIC 01416: LabVIEWNXGArgument.ComplexRealPart

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgargument-complexrealpart.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgargument-complexrealpart.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGArgument.ComplexRealPart Data Type LabVIEWNXGArgument Purpose Returns the LabVIEWNXGArgument for the real part of a complex number or array. See Also LabVIEWNXGArgument LabVIEWNXGParameter.ComplexRealPartElement

### LabVIEWNXGArgument.ComplexRealPart

#### Syntax

[LabVIEWNXGArgument](labviewnxgargument.html).ComplexRealPart

#### Data Type

[LabVIEWNXGArgument](labviewnxgargument.html)

#### Purpose

Returns the
 LabVIEWNXGArgument
 for the real part of a complex number or array.

#### See Also

[LabVIEWNXGArgument](labviewnxgargument.html)

[LabVIEWNXGParameter.ComplexRealPartElement](labviewnxgparameter-complexrealpartelement.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgargument-elements.html language=enus -->
## TOPIC 01417: LabVIEWNXGArgument.Elements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgargument-elements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgargument-elements.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGArgument.Elements Data Type LabVIEWNXGArguments Purpose Returns a collection of LabVIEWNXGArguments to pass to a parameter that is a cluster or an array of clusters. See Also LabVIEWNXGArguments LabVIEWNXGParameter.Elements

### LabVIEWNXGArgument.Elements

#### Syntax

[LabVIEWNXGArgument](labviewnxgargument.html).Elements

#### Data Type

[LabVIEWNXGArguments](labviewnxgarguments.html)

#### Purpose

Returns a collection of
 LabVIEWNXGArguments
 to pass to a parameter that is a cluster or an array of clusters.

#### See Also

[LabVIEWNXGArguments](labviewnxgarguments.html)

[LabVIEWNXGParameter.Elements](labviewnxgparameter-elements.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgargument-parametername.html language=enus -->
## TOPIC 01418: LabVIEWNXGArgument.ParameterName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgargument-parametername.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgargument-parametername.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGArgument.ParameterName Data Type String Purpose Returns the name of the parameter in the VI that is associated with the argument. See Also LabVIEWNXGParameter.ParameterName

### LabVIEWNXGArgument.ParameterName

#### Syntax

[LabVIEWNXGArgument](labviewnxgargument.html).ParameterName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the parameter in the VI that is associated with the argument.

#### See Also

[LabVIEWNXGParameter.ParameterName](labviewnxgparameter-parametername.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgargument-value.html language=enus -->
## TOPIC 01419: LabVIEWNXGArgument.Value

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgargument-value.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgargument-value.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGArgument.Value Data Type PropertyObject Purpose Specifies the argument value to pass for the corresponding parameter. See Also LabVIEWNXGModule.Execute

### LabVIEWNXGArgument.Value

#### Syntax

[LabVIEWNXGArgument](labviewnxgargument.html).Value

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Specifies the argument value to pass for the corresponding parameter.

#### See Also

[LabVIEWNXGModule.Execute](labviewnxgmodule-execute.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgargument.html language=enus -->
## TOPIC 01420: LabVIEWNXGArgument

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgargument.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgargument.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEWNXGArgument class to set the argument value to pass to a LabVIEW NXG VI using the LabVIEWNXGModule.Execute; method. Properties ComplexImaginaryPart (Read Only) ComplexRealPart (Read Only) Elements (Read Only) ParameterName (Read Only) Value See Also LabVIEWNXGArguments La

### LabVIEWNXGArgument

Use objects from the
 LabVIEWNXGArgument
 class to set the argument value to pass to a LabVIEW NXG VI using the LabVIEWNXGModule.Execute; method.

#### Properties

| ComplexImaginaryPart (Read Only) |
| --- |
| ComplexRealPart (Read Only) |
| Elements (Read Only) |
| ParameterName (Read Only) |
| Value |

#### See Also

[LabVIEWNXGArguments](labviewnxgarguments.html)

[LabVIEWNXGModule.Execute](labviewnxgmodule-execute.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgarguments-count.html language=enus -->
## TOPIC 01421: LabVIEWNXGArguments.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgarguments-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgarguments-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGArguments.Count Data Type Long Purpose Returns the number of items in the collection.

### LabVIEWNXGArguments.Count

#### Syntax

[LabVIEWNXGArguments](labviewnxgarguments.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgarguments-item.html language=enus -->
## TOPIC 01422: LabVIEWNXGArguments.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgarguments-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgarguments-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGArguments.Item( index) Data Type LabVIEWNXGArgument Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the item to retrieve. An argument at a specific index in the LabVIEWNXGArguments co

### LabVIEWNXGArguments.Item

#### Syntax

[LabVIEWNXGArguments](labviewnxgarguments.html).Item( index)

#### Data Type

[LabVIEWNXGArgument](labviewnxgargument.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve. An argument at a specific index in the
 LabVIEWNXGArguments
 collection corresponds to the parameter at the same index in the LabVIEWNXGParameters collection that you used to create the
 LabVIEWNXGArguments
 collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgarguments.html language=enus -->
## TOPIC 01423: LabVIEWNXGArguments

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgarguments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgarguments.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEWNXGArguments class to pass specific argument values to a LabVIEW NXG VI using the LabVIEWNXGModule.Execute; method. Use the LabVIEWNXGParameters.NewArguments; method to create a new arguments collection. Properties Count (Read Only) Item (Read Only) See Also LabVIEWNXGMod

### LabVIEWNXGArguments

Use objects from the
 LabVIEWNXGArguments
 class to pass specific argument values to a LabVIEW NXG VI using the LabVIEWNXGModule.Execute; method. Use the LabVIEWNXGParameters.NewArguments; method to create a new arguments collection.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[LabVIEWNXGModule.Execute](labviewnxgmodule-execute.html)

[LabVIEWNXGParameters.NewArguments](labviewnxgparameters-newarguments.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgcomponentbuildoutputtypes.html language=enus -->
## TOPIC 01424: LabVIEWNXGComponentBuildOutputTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgcomponentbuildoutputtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgcomponentbuildoutputtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the type of output to create when creating a build output. LabVIEWNXGComponentBuildOutputType_Executable –(Value: 0x2) LabVIEWNXGComponentBuildOutputType_GLibrary –(Value: 0x0) LabVIEWNXGComponentBuildOutputType_Source –(Value: 0x1)

### LabVIEWNXGComponentBuildOutputTypes

Use these constants to specify the type of output to create when creating a build output.

- LabVIEWNXGComponentBuildOutputType_Executable 
 –(Value: 0x2)
- LabVIEWNXGComponentBuildOutputType_GLibrary 
 –(Value: 0x0)
- LabVIEWNXGComponentBuildOutputType_Source 
 –(Value: 0x1)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-asmodule.html language=enus -->
## TOPIC 01425: LabVIEWNXGModule.AsModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-asmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-asmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.AsModule Return Value Module Purpose Returns the underlying Module object that represents the LabVIEWNXGModule object. Remarks Use the Module object to access properties and methods common to all modules.

### LabVIEWNXGModule.AsModule

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).AsModule

#### Return Value

[Module](module.html)

#### Purpose

Returns the underlying Module object that represents the
 LabVIEWNXGModule
 object.

#### Remarks

Use the Module object to access properties and methods common to all modules.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-buildcomponent.html language=enus -->
## TOPIC 01426: LabVIEWNXGModule.BuildComponent

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-buildcomponent.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-buildcomponent.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.BuildComponent Return Value Boolean Returns a value that indicates whether the module was modified by this method call. Purpose Builds the GLL specified in a LabVIEWNXGModule . The GLL will be re-built if it is not present on disk or it is out of date compared to the correspo

### LabVIEWNXGModule.BuildComponent

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).BuildComponent

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns a value that indicates whether the module was modified by this method call.

#### Purpose

Builds the GLL specified in a
 LabVIEWNXGModule
 . The GLL will be re-built if it is not present on disk or it is out of date compared to the corresponding source files.

#### Remarks

The method requires that the LabVIEW NXG Development System is installed on the machine. The module should also have the project and
 ModuleQualifiedName
 of the VI specified.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-componentname.html language=enus -->
## TOPIC 01427: LabVIEWNXGModule.ComponentName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-componentname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-componentname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.ComponentName Data Type String Purpose Returns the name of the component ( .gcomp ) containing the VI to execute when the module is run in the LabVIEW NXG Development System.

### LabVIEWNXGModule.ComponentName

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).ComponentName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the component (
 .gcomp
 ) containing the VI to execute when the module is run in the LabVIEW NXG Development System.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-createproject.html language=enus -->
## TOPIC 01428: LabVIEWNXGModule.CreateProject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-createproject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-createproject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.CreateProject Return Value Boolean Returns a value that indicates whether the module was modified by this method call. Purpose Creates a LabVIEW NXG project in the path specified in the LabVIEWNXGModule . If no project is specified in the module, you will be prompted to choos

### LabVIEWNXGModule.CreateProject

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).CreateProject

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns a value that indicates whether the module was modified by this method call.

#### Purpose

Creates a LabVIEW NXG project in the path specified in the
 LabVIEWNXGModule
 . If no project is specified in the module, you will be prompted to choose a project path.

#### Remarks

This method requires the LabVIEW NXG Development System to be installed on the machine.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-createpropertynodevi.html language=enus -->
## TOPIC 01429: LabVIEWNXGModule.CreatePropertyNodeVI

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-createpropertynodevi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-createpropertynodevi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.CreatePropertyNodeVI Return Value Boolean Purpose Configures a LabVIEW NXG step to call the LabVIEW NXG property node specified in the Property Node dialog box.

### LabVIEWNXGModule.CreatePropertyNodeVI

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).CreatePropertyNodeVI

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Configures a LabVIEW NXG step to call the LabVIEW NXG property node specified in the Property Node dialog box.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-editproject.html language=enus -->
## TOPIC 01430: LabVIEWNXGModule.EditProject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-editproject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-editproject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.EditProject Return Value Boolean Purpose Launches LabVIEW NXG to edit the LabVIEW NXG project associated with this module. See Also LabVIEWNXGModule.CreateProject LabVIEWNXGModule.ProjectPath

### LabVIEWNXGModule.EditProject

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).EditProject

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Launches LabVIEW NXG to edit the LabVIEW NXG project associated with this module.

#### See Also

[LabVIEWNXGModule.CreateProject](labviewnxgmodule-createproject.html)

[LabVIEWNXGModule.ProjectPath](labviewnxgmodule-projectpath.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-execute.html language=enus -->
## TOPIC 01431: LabVIEWNXGModule.Execute

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-execute.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-execute.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.Execute( sequenceContextParam, argumentsParam) Purpose Calls a LabVIEW NXG VI directly without using a step, sequence, or Execution. Remarks When you call a LabVIEW NXG module using this method you can evaluate the parameter expressions to determine the argument values or spe

### LabVIEWNXGModule.Execute

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).Execute( sequenceContextParam, argumentsParam)

#### Purpose

Calls a LabVIEW NXG VI directly without using a step, sequence, or Execution.

#### Remarks

When you call a LabVIEW NXG module using this method you can evaluate the parameter expressions to determine the argument values or specify the argument values directly using a
 LabVIEWNXGArguments
 collection.

To use the parameter value expressions, pass a valid
 SequenceContext
 object to the
 sequenceContextParam
 to use to evaluate the
 LabVIEWNXGParameter.ValueExpr
 expressions.

To pass specific argument values, use the
 LabVIEWNXGParameters.NewArguments
 method to create a collection of
 LabVIEWNXGArgument
 objects and set the
 LabVIEWNXGArgument.Value
 property on each item in the collection and on each item in contained collections like the
 LabVIEWNXGArgument.Elements
 collection.

#### Parameters

sequenceContextParam
 As
 
 [SequenceContext](sequencecontext.html)

[In] Specifies the
 SequenceContext
 object that this method uses to evaluate each of the
 LabVIEWNXGParameter.ValueExpr
 expressions in the module parameters. Pass NULL for this parameter if you pass a
 LabVIEWNXGArguments
 collection to the
 argumentsParam
 parameter.

argumentsParam
 As
 [LabVIEWNXGArguments](labviewnxgarguments.html)

[In] Specifies the argument collection that contains the argument values to pass to the VI. Pass NULL for this parameter to pass the values obtained from evaluating each of the
 LabVIEWNXGParameter.ValueExpr
 expressions in the module parameters.

#### See Also

[LabVIEWNXGArguments](labviewnxgarguments.html)

[LabVIEWNXGArgument.Elements](labviewnxgargument-elements.html)

[LabVIEWNXGArgument.Value](labviewnxgargument-value.html)

[LabVIEWNXGArguments](labviewnxgarguments.html)

[LabVIEWNXGParameter.ValueExpr](labviewnxgparameter-valueexpr.html)

[LabVIEWNXGParameters.NewArguments](labviewnxgparameters-newarguments.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-getprojectreference.html language=enus -->
## TOPIC 01432: LabVIEWNXGModule.GetProjectReference

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-getprojectreference.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-getprojectreference.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.GetProjectReference Return Value LabVIEWNXGProject A reference to the LabVIEW NXG project. Purpose Returns a reference to the LabVIEW NXG project the module is configured to use. Remarks Use this method with the LabVIEW NXG module to get the LabVIEW NXG project reference from

### LabVIEWNXGModule.GetProjectReference

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).GetProjectReference

#### Return Value

[LabVIEWNXGProject](labviewnxgproject.html)

A reference to the LabVIEW NXG project.

#### Purpose

Returns a reference to the LabVIEW NXG project the module is configured to use.

#### Remarks

Use this method with the LabVIEW NXG module to get the LabVIEW NXG project reference from which the
 LabVIEWNXGProject.GetProjectItems
 method obtains the collection of project items for a module.

#### See Also

[LabVIEWNXGProject](labviewnxgproject.html)

[LabVIEWNXGModule.ProjectPath](labviewnxgmodule-projectpath.html)

[LabVIEWNXGProject.GetProjectItems](labviewnxgproject-getprojectitems.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-getviabsolutepath.html language=enus -->
## TOPIC 01433: LabVIEWNXGModule.GetVIAbsolutePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-getviabsolutepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-getviabsolutepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.GetVIAbsolutePath( viAbsolutePath) Return Value Boolean Returns True if TestStand finds the file. Purpose Returns the absolute path of the VI. Parameters viAbsolutePath As String [Out] Returns the absolute path of the VI. If TestStand does not find the VI, this parameter retu

### LabVIEWNXGModule.GetVIAbsolutePath

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).GetVIAbsolutePath( viAbsolutePath)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns True if TestStand finds the file.

#### Purpose

Returns the absolute path of the VI.

#### Parameters

viAbsolutePath
 As
 [String](data-types-for-teststand.html)

[Out] Returns the absolute path of the VI. If TestStand does not find the VI, this parameter returns an empty string.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-gllpath.html language=enus -->
## TOPIC 01434: LabVIEWNXGModule.GLLPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-gllpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-gllpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.GLLPath Data Type String Purpose Specifies the path of the GLL specified in the step. The GLL is loaded and run when executing LabVIEWNXGModules in the LabVIEW NXG Runtime Engine.

### LabVIEWNXGModule.GLLPath

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).GLLPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the path of the GLL specified in the step. The GLL is loaded and run when executing LabVIEWNXGModules in the LabVIEW NXG Runtime Engine.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-havepropertieschanged.html language=enus -->
## TOPIC 01435: LabVIEWNXGModule.HavePropertiesChanged

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-havepropertieschanged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-havepropertieschanged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.HavePropertiesChanged( changedProperties, options = 0) Return Value Boolean A Boolean value that indicates whether the method executed without errors. Purpose Returns the properties of a module that need to update. The methods only checks the properties that have been specifi

### LabVIEWNXGModule.HavePropertiesChanged

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).HavePropertiesChanged( changedProperties, options = 0)

#### Return Value

[Boolean](data-types-for-teststand.html)

A Boolean value that indicates whether the method executed without errors.

#### Purpose

Returns the properties of a module that need to update. The methods only checks the properties that have been specified in the
 options
 parameter.

#### Parameters

changedProperties
 As
 [Long](data-types-for-teststand.html)

[Out] A long value that indicates which properties were updated. The value returned can be ORed with enumerators in the
 GetUpdatedStatusOptions
 to determine which properties have changed.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specify the properties that need to be checked for changes using the
 CheckUpdatedStatusOption
 enum.

This parameter has a default value of
 0
 .

#### See Also

[GetUpdatedStatusOptions](getupdatedstatusoptions.html)

[CheckUpdatedStatusOptions](checkupdatedstatusoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-isprojectvalid.html language=enus -->
## TOPIC 01436: LabVIEWNXGModule.IsProjectValid

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-isprojectvalid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-isprojectvalid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.IsProjectValid( errorDescription) Return Value Boolean Purpose Returns a value that indicates whether the specified LabVIEW NXG project path is a valid path and the file was found on disk. Parameters errorDescription As String [Out] Returns a description of the error encounte

### LabVIEWNXGModule.IsProjectValid

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).IsProjectValid( errorDescription)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the specified LabVIEW NXG project path is a valid path and the file was found on disk.

#### Parameters

errorDescription
 As
 [String](data-types-for-teststand.html)

[Out] Returns a description of the error encountered, if any.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-loadviinfo.html language=enus -->
## TOPIC 01437: LabVIEWNXGModule.LoadVIInfo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-loadviinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-loadviinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.LoadVIInfo Return Value Boolean Returns a value that indicates whether the prototype of the VI specified in the step matches the prototype of the VI on disk and if the specified GLL path matches the expected GLL path for the given project, component and target. Purpose Loads

### LabVIEWNXGModule.LoadVIInfo

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).LoadVIInfo

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns a value that indicates whether the prototype of the VI specified in the step matches the prototype of the VI on disk and if the specified GLL path matches the expected GLL path for the given project, component and target.

#### Purpose

Loads information about the VI that the module calls, including default values, enumeration values, the expected GLL path and the VI help description.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-modulequalifiedname.html language=enus -->
## TOPIC 01438: LabVIEWNXGModule.ModuleQualifiedName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-modulequalifiedname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-modulequalifiedname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.ModuleQualifiedName Data Type String Purpose Specifies the Module Qualified Name of the VI. This value determines the VI to execute when the module is executed in the LabVIEW NXG Development System.

### LabVIEWNXGModule.ModuleQualifiedName

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).ModuleQualifiedName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the Module Qualified Name of the VI. This value determines the VI to execute when the module is executed in the LabVIEW NXG Development System.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-nodeclassname.html language=enus -->
## TOPIC 01439: LabVIEWNXGModule.NodeClassName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-nodeclassname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-nodeclassname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.NodeClassName Data Type String Purpose Specifies the LabVIEW NXG I/O Library Class Name when calling a LabVIEW NXG Property Node.

### LabVIEWNXGModule.NodeClassName

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).NodeClassName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the LabVIEW NXG I/O Library Class Name when calling a LabVIEW NXG Property Node.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-nodeignoresinternalerrors.html language=enus -->
## TOPIC 01440: LabVIEWNXGModule.NodeIgnoresInternalErrors

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-nodeignoresinternalerrors.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-nodeignoresinternalerrors.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.NodeIgnoresInternalErrors Data Type Boolean Purpose Indicates that a LabVIEW NXG Property Node should continue to process any remaining properties in the node when it encounters an error while accessing a property.

### LabVIEWNXGModule.NodeIgnoresInternalErrors

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).NodeIgnoresInternalErrors

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Indicates that a LabVIEW NXG Property Node should continue to process any remaining properties in the node when it encounters an error while accessing a property.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-nodeoperationmode.html language=enus -->
## TOPIC 01441: LabVIEWNXGModule.NodeOperationMode

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-nodeoperationmode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-nodeoperationmode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.NodeOperationMode Data Type LabVIEWNXGNodeOperationModes Use the following constants with this data type: LabVIEWNXGNodeOperationMode_Default –(Value: 0) Indicates that the Configure Property Node dialog box operates in default mode. LabVIEWNXGNodeOperationMode_Restricted –(V

### LabVIEWNXGModule.NodeOperationMode

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).NodeOperationMode

#### Data Type

[LabVIEWNXGNodeOperationModes](labviewnxgnodeoperationmodes.html)

Use the following constants with this data type:

- LabVIEWNXGNodeOperationMode_Default 
 –(Value: 0) Indicates that the Configure Property Node dialog box operates in default mode.
- LabVIEWNXGNodeOperationMode_Restricted 
 –(Value: 1) Indicates that the Configure Property Node dialog box operates in restricted mode.

#### Purpose

Indicates the mode of operation of the Configure Property Node dialog box for LabVIEW NXG property calls.

#### See Also

[Configure Property Node dialog box](../tsref/configure-property-node-dialog-box.html)

[LabVIEWNXGModule.NodeClassName](labviewnxgmodule-nodeclassname.html)

[LabVIEWNXGModule.NodeIgnoresInternalErrors](labviewnxgmodule-nodeignoresinternalerrors.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-nodeproperties.html language=enus -->
## TOPIC 01442: LabVIEWNXGModule.NodeProperties

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-nodeproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-nodeproperties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.NodeProperties Data Type LabVIEWNXGNodeProperties Purpose Contains the properties to use in a step configured to call a LabVIEW NXG Property Node.

### LabVIEWNXGModule.NodeProperties

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).NodeProperties

#### Data Type

[LabVIEWNXGNodeProperties](labviewnxgnodeproperties.html)

#### Purpose

Contains the properties to use in a step configured to call a LabVIEW NXG Property Node.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-nodetypename.html language=enus -->
## TOPIC 01443: LabVIEWNXGModule.NodeTypeName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-nodetypename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-nodetypename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.NodeTypeName Data Type String Purpose Specifies the LabVIEW NXG I/O Library Type Name when calling a LabVIEW NXG Property Node.

### LabVIEWNXGModule.NodeTypeName

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).NodeTypeName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the LabVIEW NXG I/O Library Type Name when calling a LabVIEW NXG Property Node.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-parameters.html language=enus -->
## TOPIC 01444: LabVIEWNXGModule.Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.Parameters Data Type LabVIEWNXGParameters The collection of parameters. Purpose Returns the LabVIEWNXGParameters collection that contains a list of the current parameters used as inputs and outputs of the corresponding module. Remarks Call the Module.LoadPrototype ; method be

### LabVIEWNXGModule.Parameters

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).Parameters

#### Data Type

[LabVIEWNXGParameters](labviewnxgparameters.html)

The collection of parameters.

#### Purpose

Returns the
 LabVIEWNXGParameters
 collection that contains a list of the current parameters used as inputs and outputs of the corresponding module.

#### Remarks

Call the
 Module.LoadPrototype
 ; method before accessing this property.

#### See Also

[LabVIEWNXGParameters](labviewnxgparameters.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-projectpath.html language=enus -->
## TOPIC 01445: LabVIEWNXGModule.ProjectPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-projectpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-projectpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.ProjectPath Data Type String Purpose Specifies the path of the project ( .lvproject ) containing the VI to execute when the module is run in the LabVIEW NXG Development System.

### LabVIEWNXGModule.ProjectPath

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).ProjectPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the path of the project (
 .lvproject
 ) containing the VI to execute when the module is run in the LabVIEW NXG Development System.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-qualifiedname.html language=enus -->
## TOPIC 01446: LabVIEWNXGModule.QualifiedName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-qualifiedname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-qualifiedname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.QualifiedName Data Type String Purpose Specifies the VI selected in a GLL in a LabVIEW NXG module. This value determines which VI from the GLL specified is executed when the module is run in the LabVIEW NXG Runtime Engine. It is the value displayed in the Fully Qualified Name

### LabVIEWNXGModule.QualifiedName

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).QualifiedName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the VI selected in a GLL in a LabVIEW NXG module. This value determines which VI from the GLL specified is executed when the module is run in the LabVIEW NXG Runtime Engine. It is the value displayed in the Fully Qualified Name window in the
 Item
 tab of the component
 .gcomp
 document that contains the VI, when the VI is selected in LabVIEW NXG.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-updatemodulefromstep.html language=enus -->
## TOPIC 01447: LabVIEWNXGModule.UpdateModuleFromStep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-updatemodulefromstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-updatemodulefromstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.UpdateModuleFromStep( oldStep, options, unmappedParameters) Purpose Copies parameter values and other options like use default value, logging enabled, show Front Panel etc. from the old module to the current module. Remarks The parameter values and settings are only copied fo

### LabVIEWNXGModule.UpdateModuleFromStep

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).UpdateModuleFromStep( oldStep, options, unmappedParameters)

#### Purpose

Copies parameter values and other options like use default value, logging enabled, show Front Panel etc. from the old module to the current module.

#### Remarks

The parameter values and settings are only copied for parameters that match in name and type when the parameters from the old step are compared to the parameters in the current module. The unmapped parameters are returned in
 unmappedParameters
 . Use this step to copy parameter information and other step settings from an old LabVIEW step to the equivalent LabVIEW NXG step.

#### Parameters

oldStep
 As
 
 [Module](module.html)

[In] The LabVIEW module from which parameter values need to be populated.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies which step or parameter settings should be copied from the old module.

unmappedParameters
 As
 [String Array](data-types-for-teststand.html)

[Out] Contains the names of those parameters from the old module that did not map to any parameter in the new module.

#### See Also

[LabVIEWNXGModule](labviewnxgmodule.html)

[LabVIEWModule](labviewmodule.html)

[UpdateModuleFromStepOptions](updatemodulefromstepoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-vicalloptions.html language=enus -->
## TOPIC 01448: LabVIEWNXGModule.VICallOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-vicalloptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-vicalloptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.VICallOptions Data Type Long Purpose Specifies options for calling the VI of the module. See Also LabVIEWNXGModuleCallOptions

### LabVIEWNXGModule.VICallOptions

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).VICallOptions

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies
 [options](labviewnxgmodulecalloptions.html)
 for calling the VI of the module.

#### See Also

[LabVIEWNXGModuleCallOptions](labviewnxgmodulecalloptions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-videscription.html language=enus -->
## TOPIC 01449: LabVIEWNXGModule.VIDescription

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-videscription.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-videscription.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.VIDescription Data Type String Purpose Returns the description of the VI. Remarks If no description exists for the VI, this property returns an empty string. The LabVIEW NXG Adapter persists this property value when you specify a code module for a step. For an unspecified ste

### LabVIEWNXGModule.VIDescription

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).VIDescription

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the description of the VI.

#### Remarks

If no description exists for the VI, this property returns an empty string.

The LabVIEW NXG Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the
 [Module.LoadPrototype](module-loadprototype.html)
 method before retrieving this property.

#### See Also

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule-vitarget.html language=enus -->
## TOPIC 01450: LabVIEWNXGModule.VITarget

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule-vitarget.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule-vitarget.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGModule.VITarget Data Type String Purpose Specifies the target for which the component ( .gcomp ) is selected to build.

### LabVIEWNXGModule.VITarget

#### Syntax

[LabVIEWNXGModule](labviewnxgmodule.html).VITarget

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the target for which the component (
 .gcomp
 ) is selected to build.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodule.html language=enus -->
## TOPIC 01451: LabVIEWNXGModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEWNXGModule class to specify and obtain LabVIEW NXG Adapter-specific information about the code module that steps or step type substeps execute. Use the Step.Module property to obtain a reference to a LabVIEWNXGModule object. To access the properties and methods of a specif

### LabVIEWNXGModule

Use objects from the
 LabVIEWNXGModule
 class to specify and obtain LabVIEW NXG Adapter-specific information about the code module that steps or step type substeps execute. Use the
 Step.Module
 property to obtain a reference to a
 LabVIEWNXGModule
 object. To access the properties and methods of a specific module class, query the
 Module
 object for the interface of the module-specific interface you want to acquire.

Typically, you use this class only when you are writing a sequence editor.

To access the properties and methods of the
 Module
 class, use the
 LabVIEWNXGModule.AsModule
 method to obtain an object.

You can use the
 Module.LoadPrototype
 method to load the prototype for the module the step specifies.

#### Properties

| ComponentName (Read Only) |
| --- |
| GLLPath |
| ModuleQualifiedName |
| NodeClassName |
| NodeIgnoresInternalErrors |
| NodeOperationMode |
| NodeProperties (Read Only) |
| NodeTypeName |
| Parameters (Read Only) |
| ProjectPath |
| QualifiedName |
| VICallOptions |
| VIDescription (Read Only) |
| VITarget |

#### Methods

| AsModule |
| --- |
| BuildComponent |
| CreateProject |
| CreatePropertyNodeVI |
| EditProject |
| Execute |
| GetProjectReference |
| GetVIAbsolutePath |
| HavePropertiesChanged |
| IsProjectValid |
| LoadVIInfo |
| UpdateModuleFromStep |

#### See Also

[Module](module.html)

[Module.LoadPrototype](module-loadprototype.html)

[Step.Module](step-module.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgmodulecalloptions.html language=enus -->
## TOPIC 01452: LabVIEWNXGModuleCallOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgmodulecalloptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgmodulecalloptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following constants with the LabVIEWNXGModule.VICallOptions method to get or set options for calling the VI for the module. Use the bitwise-AND operator to determine whether either of these flags are set when obtaining the property value. Use the bitwise-OR operator to set both flags when se

### LabVIEWNXGModuleCallOptions

Use the following constants with the
 [LabVIEWNXGModule.VICallOptions](labviewnxgmodule-vicalloptions.html)
 method to get or set options for calling the VI for the module. Use the bitwise-AND operator to determine whether either of these flags are set when obtaining the property value. Use the bitwise-OR operator to set both flags when setting the property value.

- LabVIEWNXGModuleCallOption_BringFrontPaneltoFront 
 –(Value: 8) Specifies to display the front panel of the loaded VI as a dialog box that is in front of TestStand's main window.
- LabVIEWNXGModuleCallOption_MakeFrontPanelModal 
 –(Value: 4) Specifies to display the front panel of the loaded VI as a dialog box that is modal to TestStand's main window.
- LabVIEWNXGModuleCallOption_None 
 –(Value: 0) Specifies no options when executing the VI of the module.
- LabVIEWNXGModuleCallOption_ReserveforExecution 
 –(Value: 1) Specifies to reserve the loaded VI of the module before execution.
- LabVIEWNXGModuleCallOption_RunInRuntimeEngine 
 –(Value: 2) Specifies to run the loaded VI in the LabVIEW NXG run-time engine.

Parent topic:

Adapter API-Related Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgnodeoperationmodes.html language=enus -->
## TOPIC 01453: LabVIEWNXGNodeOperationModes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgnodeoperationmodes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgnodeoperationmodes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the operation mode for the LabVIEW NXG node. LabVIEWNXGNodeOperationMode_Default –(Value: 0) Indicates that the Configure Property Node dialog box operates in default mode. LabVIEWNXGNodeOperationMode_Restricted –(Value: 1) Indicates that the Configure Property Node di

### LabVIEWNXGNodeOperationModes

Use these constants to specify the operation mode for the LabVIEW NXG node.

- LabVIEWNXGNodeOperationMode_Default 
 –(Value: 0) Indicates that the Configure Property Node dialog box operates in default mode.
- LabVIEWNXGNodeOperationMode_Restricted 
 –(Value: 1) Indicates that the Configure Property Node dialog box operates in restricted mode.

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgnodeproperties-clear.html language=enus -->
## TOPIC 01454: LabVIEWNXGNodeProperties.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgnodeproperties-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgnodeproperties-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGNodeProperties.Clear Purpose Removes all items from the collection.

### LabVIEWNXGNodeProperties.Clear

#### Syntax

[LabVIEWNXGNodeProperties](labviewnxgnodeproperties.html).Clear

#### Purpose

Removes all items from the collection.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgnodeproperties-count.html language=enus -->
## TOPIC 01455: LabVIEWNXGNodeProperties.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgnodeproperties-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgnodeproperties-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGNodeProperties.Count Data Type Long Purpose Returns the number of items in the collection.

### LabVIEWNXGNodeProperties.Count

#### Syntax

[LabVIEWNXGNodeProperties](labviewnxgnodeproperties.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgnodeproperties-delete.html language=enus -->
## TOPIC 01456: LabVIEWNXGNodeProperties.Delete

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgnodeproperties-delete.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgnodeproperties-delete.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGNodeProperties.Delete( index) Purpose Removes the item at the specified index. Parameters index As Long [In] Specifies the zero-based index of the item to delete.

### LabVIEWNXGNodeProperties.Delete

#### Syntax

[LabVIEWNXGNodeProperties](labviewnxgnodeproperties.html).Delete( index)

#### Purpose

Removes the item at the specified index.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to delete.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgnodeproperties-item.html language=enus -->
## TOPIC 01457: LabVIEWNXGNodeProperties.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgnodeproperties-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgnodeproperties-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGNodeProperties.Item( index) Data Type LabVIEWNXGNodeProperty Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index.

### LabVIEWNXGNodeProperties.Item

#### Syntax

[LabVIEWNXGNodeProperties](labviewnxgnodeproperties.html).Item( index)

#### Data Type

[LabVIEWNXGNodeProperty](labviewnxgnodeproperty.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgnodeproperties-new.html language=enus -->
## TOPIC 01458: LabVIEWNXGNodeProperties.New

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgnodeproperties-new.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgnodeproperties-new.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGNodeProperties.New( index, longName, dataName, uniqueID, nodePropertyDirection) Purpose Adds a new item to the collection. Parameters index As Long [In] Specifies the zero-based index of the item to add. longName As String [In] Specifies the LongName of a particular property. dataNa

### LabVIEWNXGNodeProperties.New

#### Syntax

[LabVIEWNXGNodeProperties](labviewnxgnodeproperties.html).New( index, longName, dataName, uniqueID, nodePropertyDirection)

#### Purpose

Adds a new item to the collection.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to add.

longName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the LongName of a particular property.

dataName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the DataName of a particular property.

uniqueID
 As
 [String](data-types-for-teststand.html)

[In] Specifies the unique ID of a particular property.

nodePropertyDirection
 As
 [LabVIEWNXGNodePropertyDirections](labviewnxgnodepropertydirections.html)

[In] Indicates the direction of the property.
 0
 indicates an input property.
 1
 indicates an output property.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgnodeproperties.html language=enus -->
## TOPIC 01459: LabVIEWNXGNodeProperties

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgnodeproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgnodeproperties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEWNXGNodeProperties class to configure and obtain LabVIEWNXGNodeProperties for a module that uses the LabVIEW NXG Adapter. Use the LabVIEWNXGModule.NodeProperties property to obtain the collection of LabVIEWNXGNodeProperties for a module. Properties Count (Read Only) Item (

### LabVIEWNXGNodeProperties

Use objects from the
 LabVIEWNXGNodeProperties
 class to configure and obtain
 LabVIEWNXGNodeProperties
 for a module that uses the LabVIEW NXG Adapter. Use the
 LabVIEWNXGModule.NodeProperties
 property to obtain the collection of
 LabVIEWNXGNodeProperties
 for a module.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Clear |
| --- |
| Delete |
| New |

#### See Also

[LabVIEWNXGModule.NodeProperties](labviewnxgmodule-nodeproperties.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgnodeproperty-aspropertyobject.html language=enus -->
## TOPIC 01460: LabVIEWNXGNodeProperty.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgnodeproperty-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgnodeproperty-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGNodeProperty.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the LabVIEWNXGPropertyNode object. Remarks Use the PropertyObject to modify, add, or remove custom properties of the object.

### LabVIEWNXGNodeProperty.AsPropertyObject

#### Syntax

[LabVIEWNXGNodeProperty](labviewnxgnodeproperty.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying
 PropertyObject
 that represents the
 LabVIEWNXGPropertyNode
 object.

#### Remarks

Use the
 PropertyObject
 to modify, add, or remove custom properties of the object.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgnodeproperty-dataname.html language=enus -->
## TOPIC 01461: LabVIEWNXGNodeProperty.DataName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgnodeproperty-dataname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgnodeproperty-dataname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGNodeProperty.DataName Data Type String Purpose Specifies the DataName of a particular property.

### LabVIEWNXGNodeProperty.DataName

#### Syntax

[LabVIEWNXGNodeProperty](labviewnxgnodeproperty.html).DataName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the DataName of a particular property.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgnodeproperty-direction.html language=enus -->
## TOPIC 01462: LabVIEWNXGNodeProperty.Direction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgnodeproperty-direction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgnodeproperty-direction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGNodeProperty.Direction Data Type LabVIEWNXGNodePropertyDirections Use the following constants with this data type: LabVIEWNXGNodePropertyDirection_Default –(Value: 2) Specifies that the property uses the default value. LabVIEWNXGNodePropertyDirection_In –(Value: 0) Specifies an inpu

### LabVIEWNXGNodeProperty.Direction

#### Syntax

[LabVIEWNXGNodeProperty](labviewnxgnodeproperty.html).Direction

#### Data Type

[LabVIEWNXGNodePropertyDirections](labviewnxgnodepropertydirections.html)

Use the following constants with this data type:

- LabVIEWNXGNodePropertyDirection_Default 
 –(Value: 2) Specifies that the property uses the default value.
- LabVIEWNXGNodePropertyDirection_In 
 –(Value: 0) Specifies an input property.
- LabVIEWNXGNodePropertyDirection_Out 
 –(Value: 1) Specifies an output property.

#### Purpose

Indicates the direction of the property. Use the followign constants with this data type:

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgnodeproperty-longname.html language=enus -->
## TOPIC 01463: LabVIEWNXGNodeProperty.LongName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgnodeproperty-longname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgnodeproperty-longname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGNodeProperty.LongName Data Type String Purpose Specifies the LongName of a particular property.

### LabVIEWNXGNodeProperty.LongName

#### Syntax

[LabVIEWNXGNodeProperty](labviewnxgnodeproperty.html).LongName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the LongName of a particular property.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgnodeproperty-uniqueid.html language=enus -->
## TOPIC 01464: LabVIEWNXGNodeProperty.UniqueID

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgnodeproperty-uniqueid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgnodeproperty-uniqueid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGNodeProperty.UniqueID Data Type String Purpose Specifies the UniqueID of a particular property.

### LabVIEWNXGNodeProperty.UniqueID

#### Syntax

[LabVIEWNXGNodeProperty](labviewnxgnodeproperty.html).UniqueID

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the UniqueID of a particular property.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgnodeproperty.html language=enus -->
## TOPIC 01465: LabVIEWNXGNodeProperty

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgnodeproperty.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgnodeproperty.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEWNXGNodeProperty class to configure and obtain LabVIEWNXGNodeProperty -specific information for an item in the LabVIEWNXGNodeProperties collection class. Properties DataName Direction LongName UniqueID Method AsPropertyObject

### LabVIEWNXGNodeProperty

Use objects from the
 LabVIEWNXGNodeProperty
 class to configure and obtain
 LabVIEWNXGNodeProperty
 -specific information for an item in the
 LabVIEWNXGNodeProperties
 collection class.

#### Properties

| DataName |
| --- |
| Direction |
| LongName |
| UniqueID |

#### Method

| AsPropertyObject |
| --- |

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgnodepropertydirections.html language=enus -->
## TOPIC 01466: LabVIEWNXGNodePropertyDirections

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgnodepropertydirections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgnodepropertydirections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the direction of the property. LabVIEWNXGNodePropertyDirection_Default –(Value: 2) Specifies that the property uses the default value. LabVIEWNXGNodePropertyDirection_In –(Value: 0) Specifies an input property. LabVIEWNXGNodePropertyDirection_Out –(Value: 1) Specifies an output property.

### LabVIEWNXGNodePropertyDirections

Indicates the direction of the property.

- LabVIEWNXGNodePropertyDirection_Default 
 –(Value: 2) Specifies that the property uses the default value.
- LabVIEWNXGNodePropertyDirection_In 
 –(Value: 0) Specifies an input property.
- LabVIEWNXGNodePropertyDirection_Out 
 –(Value: 1) Specifies an output property.

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-arraydimensions.html language=enus -->
## TOPIC 01467: LabVIEWNXGParameter.ArrayDimensions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-arraydimensions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-arraydimensions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.ArrayDimensions Data Type Long Purpose Returns the number of dimensions for array parameters. See Also LabVIEWNXGParameter.GetArrayIndex LabVIEWNXGParameter.GetDefaultArrayDimensionSize

### LabVIEWNXGParameter.ArrayDimensions

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).ArrayDimensions

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of dimensions for array parameters.

#### See Also

[LabVIEWNXGParameter.GetArrayIndex](labviewnxgparameter-getarrayindex.html)

[LabVIEWNXGParameter.GetDefaultArrayDimensionSize](labviewnxgparameter-getdefaultarraydimensions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-arrayelementprototype.html language=enus -->
## TOPIC 01468: LabVIEWNXGParameter.ArrayElementPrototype

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-arrayelementprototype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-arrayelementprototype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.ArrayElementPrototype Data Type LabVIEWNXGParameter Purpose Returns the cluster prototype for the elements of the array. Remarks This property is valid only for arrays of LabVIEW NXG clusters. Call the LabVIEWNXGParameter.Category property to determine whether the paramete

### LabVIEWNXGParameter.ArrayElementPrototype

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).ArrayElementPrototype

#### Data Type

[LabVIEWNXGParameter](labviewnxgparameter.html)

#### Purpose

Returns the cluster prototype for the elements of the array.

#### Remarks

This property is valid only for arrays of LabVIEW NXG clusters. Call the
 [LabVIEWNXGParameter.Category](labviewnxgparameter-category.html)
 property to determine whether the parameter is an array of LabVIEW NXG clusters. The array element prototype is a template from which new elements are copied when the size of the array increases. The array element prototype represents the expected structure of elements of the array. You can also use the array element prototype to create a TestStand custom data type that maps to the LabVIEW NXG cluster.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-aspropertyobject.html language=enus -->
## TOPIC 01469: LabVIEWNXGParameter.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the LabVIEWNXGParameter object. Remarks Use the PropertyObject to modify, add, or remove custom properties of the object. See Also PropertyObject

### LabVIEWNXGParameter.AsPropertyObject

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the
 LabVIEWNXGParameter
 object.

#### Remarks

Use the
 PropertyObject
 to modify, add, or remove custom properties of the object.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-category.html language=enus -->
## TOPIC 01470: LabVIEWNXGParameter.Category

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-category.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-category.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.Category Data Type LabVIEWNXGParameterCategories Purpose Returns the group of data types (number, string, and so on) to which this parameter belongs. Remarks After obtaining the category of the parameter, you can obtain the data type with the LabVIEWNXGParameter.Type prope

### LabVIEWNXGParameter.Category

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).Category

#### Data Type

[LabVIEWNXGParameterCategories](labviewnxgparametercategories.html)

#### Purpose

Returns the group of data types (number, string, and so on) to which this parameter belongs.

#### Remarks

After obtaining the
 [category](labviewnxgparametercategories.html)
 of the parameter, you can obtain the data type with the
 [LabVIEWNXGParameter.Type](labviewnxgparameter-type.html)
 property.

The LabVIEW NXG Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the
 [Module.LoadPrototype](module-loadprototype.html)
 method before retrieving this property.

#### See Also

[LabVIEWNXGParameter.Type](labviewnxgparameter-type.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-compleximaginaryparteleme.html language=enus -->
## TOPIC 01471: LabVIEWNXGParameter.ComplexImaginaryPartElement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-compleximaginaryparteleme.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-compleximaginaryparteleme.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.ComplexImaginaryPartElement Data Type LabVIEWNXGParameter Purpose Returns the imaginary element of a complex number or array. Remarks This method is valid only for a complex number or an array of complex number parameters. See Also LabVIEWNXGParameter.ComplexRealPartElemen

### LabVIEWNXGParameter.ComplexImaginaryPartElement

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).ComplexImaginaryPartElement

#### Data Type

[LabVIEWNXGParameter](labviewnxgparameter.html)

#### Purpose

Returns the imaginary element of a complex number or array.

#### Remarks

This method is valid only for a complex number or an array of complex number parameters.

#### See Also

[LabVIEWNXGParameter.ComplexRealPartElement](labviewnxgparameter-complexrealpartelement.html)

[LabVIEWNXGParameter.Elements](labviewnxgparameter-elements.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-complexrealpartelement.html language=enus -->
## TOPIC 01472: LabVIEWNXGParameter.ComplexRealPartElement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-complexrealpartelement.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-complexrealpartelement.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.ComplexRealPartElement Data Type LabVIEWNXGParameter Purpose Returns the real element of a complex number or array. Remarks This method is valid only for a complex number and array of complex number parameters. See Also LabVIEWNXGParameter.ComplexImaginaryPartElement LabVI

### LabVIEWNXGParameter.ComplexRealPartElement

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).ComplexRealPartElement

#### Data Type

[LabVIEWNXGParameter](labviewnxgparameter.html)

#### Purpose

Returns the real element of a complex number or array.

#### Remarks

This method is valid only for a complex number and array of complex number parameters.

#### See Also

[LabVIEWNXGParameter.ComplexImaginaryPartElement](labviewnxgparameter-compleximaginaryparteleme.html)

[LabVIEWNXGParameter.Elements](labviewnxgparameter-elements.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-createdefaultarrayelement.html language=enus -->
## TOPIC 01473: LabVIEWNXGParameter.CreateDefaultArrayElements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-createdefaultarrayelement.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-createdefaultarrayelement.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.CreateDefaultArrayElements Return Value Boolean Returns a value that indicates whether the default array elements were created. Purpose Creates all the default array elements of an array parameter. Remarks This method is valid only on array parameters and creates the eleme

### LabVIEWNXGParameter.CreateDefaultArrayElements

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).CreateDefaultArrayElements

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns a value that indicates whether the default array elements were created.

#### Purpose

Creates all the default array elements of an array parameter.

#### Remarks

This method is valid only on array parameters and creates the elements only if the array control on the VI front panel defines default elements. TestStand replaces any existing array elements the parameter previously specified.

#### See Also

[LabVIEWNXGParameter.DeleteArrayElements](labviewnxgparameter-deletearrayelements.html)

[LabVIEWNXGParameter.Type](labviewnxgparameter-type.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-defaultvalue.html language=enus -->
## TOPIC 01474: LabVIEWNXGParameter.DefaultValue

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-defaultvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-defaultvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.DefaultValue Data Type String Purpose Returns a display string that represents the default value defined for the parameter. Remarks Default values apply only to recommended and optional parameters. You must call the LabVIEWNXGModule.LoadVIInfo or Module.LoadPrototype metho

### LabVIEWNXGParameter.DefaultValue

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).DefaultValue

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns a display string that represents the default value defined for the parameter.

#### Remarks

Default values apply only to recommended and optional parameters. You must call the
 [LabVIEWNXGModule.LoadVIInfo](labviewnxgmodule-loadviinfo.html)
 or
 [Module.LoadPrototype](module-loadprototype.html)
 method before retrieving the default value. Otherwise, TestStand returns an empty string. The values stay in memory until the sequence file closes.

#### See Also

[LabVIEWNXGModule.LoadVIInfo](labviewnxgmodule-loadviinfo.html)

[LabVIEWNXGParameter.UseDefaultValue](labviewnxgparameter-usedefaultvalue.html)

[LabVIEWNXGParameter.ValueExpr](labviewnxgparameter-valueexpr.html)

[LabVIEWNXGParameter.WireRequirement](labviewnxgparameter-wirerequirement.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-deletearrayelement.html language=enus -->
## TOPIC 01475: LabVIEWNXGParameter.DeleteArrayElement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-deletearrayelement.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-deletearrayelement.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.DeleteArrayElement( index) Purpose Deletes the array element at a specified index. Remarks This method is valid only for one-dimensional array parameters. Use the LabVIEWNXGParameter.ArrayDimensions property to determine the number of array dimensions. Parameters index As

### LabVIEWNXGParameter.DeleteArrayElement

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).DeleteArrayElement( index)

#### Purpose

Deletes the array element at a specified index.

#### Remarks

This method is valid only for one-dimensional array parameters. Use the
 [LabVIEWNXGParameter.ArrayDimensions](labviewnxgparameter-arraydimensions.html)
 property to determine the number of array dimensions.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the index at which to delete the array element. This value must be greater than or equal to
 0
 and less than the number of array elements.

#### See Also

[LabVIEWNXGParameter.ArrayDimensions](labviewnxgparameter-arraydimensions.html)

[LabVIEWNXGParameter.DeleteArrayElements](labviewnxgparameter-deletearrayelements.html)

[LabVIEWNXGParameter.Type](labviewnxgparameter-type.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-deletearrayelements.html language=enus -->
## TOPIC 01476: LabVIEWNXGParameter.DeleteArrayElements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-deletearrayelements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-deletearrayelements.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.DeleteArrayElements Return Value Boolean Purpose Deletes all the array elements. Remarks This method is valid only on array parameters. See Also LabVIEWNXGParameter.DeleteArrayElement LabVIEWNXGParameter.InsertArrayElement LabVIEWNXGParameter.Type

### LabVIEWNXGParameter.DeleteArrayElements

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).DeleteArrayElements

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Deletes all the array elements.

#### Remarks

This method is valid only on array parameters.

#### See Also

[LabVIEWNXGParameter.DeleteArrayElement](labviewnxgparameter-deletearrayelement.html)

[LabVIEWNXGParameter.InsertArrayElement](labviewnxgparameter-insertarrayelement.html)

[LabVIEWNXGParameter.Type](labviewnxgparameter-type.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-description.html language=enus -->
## TOPIC 01477: LabVIEWNXGParameter.Description

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-description.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-description.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.Description Data Type String Purpose Returns the description of the parameter. Remarks This is the description available in the Description window in the Items Tab of a LabVIEW NXG VI's properties pane, when the corresponding control or indicator is selected.

### LabVIEWNXGParameter.Description

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).Description

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the description of the parameter.

#### Remarks

This is the description available in the Description window in the Items Tab of a LabVIEW NXG VI's properties pane, when the corresponding control or indicator is selected.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-direction.html language=enus -->
## TOPIC 01478: LabVIEWNXGParameter.Direction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-direction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-direction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.Direction Data Type LabVIEWNXGParameterDirections Use the following constants with this data type: LabVIEWNXGParamDirection_In –(Value: 0) Indicates that the parameter is passed to the VI. LabVIEWNXGParamDirection_Out –(Value: 1) Indicates that the parameter is returned fr

### LabVIEWNXGParameter.Direction

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).Direction

#### Data Type

[LabVIEWNXGParameterDirections](labviewnxgparameterdirections.html)

Use the following constants with this data type:

- LabVIEWNXGParamDirection_In 
 –(Value: 0) Indicates that the parameter is passed to the VI.
- LabVIEWNXGParamDirection_Out 
 –(Value: 1) Indicates that the parameter is returned from the VI.

#### Purpose

Returns a value that indicates whether the parameter is an
 [input or output](labviewnxgparameterdirections.html)
 parameter.

#### Remarks

The LabVIEW NXG Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the
 [Module.LoadPrototype](module-loadprototype.html)
 method before retrieving this property.

#### See Also

[LabVIEWNXGParameter.WireRequirement](labviewnxgparameter-wirerequirement.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-displaycreatecustomdataty.html language=enus -->
## TOPIC 01479: LabVIEWNXGParameter.DisplayCreateCustomDataTypeDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-displaycreatecustomdataty.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-displaycreatecustomdataty.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.DisplayCreateCustomDataTypeDialog( sequenceContext) Return Value Boolean Returns True if you click OK in the dialog box. False if you click Cancel . Purpose Launches the Create/Update Custom Data Type from Cluster dialog box, in which you configure a new custom data type o

### LabVIEWNXGParameter.DisplayCreateCustomDataTypeDialog

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).DisplayCreateCustomDataTypeDialog( sequenceContext)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box.
 False
 if you click
 Cancel
 .

#### Purpose

Launches the
 [Create/Update Custom Data Type from Cluster](../tsref/create-update-custom-data-type-from-cluster-d.html)
 dialog box, in which you configure a new custom data type or update an existing custom type.

#### Parameters

sequenceContext
 As
 
 [SequenceContext](sequencecontext.html)

[In] Specifies the sequence context the dialog box uses to obtain information about the sequence file. You can use the
 Engine.NewEditContext
 method to obtain an edit-time sequence context.

#### See Also

[Create/Update Custom Data Type from Cluster dialog box](../tsref/create-update-custom-data-type-from-cluster-d.html)

[Engine.NewEditContext](engine-neweditcontext.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-displaytype.html language=enus -->
## TOPIC 01480: LabVIEWNXGParameter.DisplayType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-displaytype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-displaytype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.DisplayType Data Type String Purpose Returns a localized string that describes the LabVIEW NXG data type for the parameter. Remarks The LabVIEW NXG Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the Mo

### LabVIEWNXGParameter.DisplayType

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).DisplayType

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns a localized string that describes the LabVIEW NXG data type for the parameter.

#### Remarks

The LabVIEW NXG Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the
 [Module.LoadPrototype](module-loadprototype.html)
 method before you retrieve this property value.

#### See Also

[LabVIEWNXGParameter.Type](labviewnxgparameter-type.html)

[LabVIEWNXGParameter.WireRequirement](labviewnxgparameter-wirerequirement.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-elements.html language=enus -->
## TOPIC 01481: LabVIEWNXGParameter.Elements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-elements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-elements.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.Elements Data Type LabVIEWNXGParameters Purpose Returns a collection that accesses the members of a parameter that is a cluster, or accesses the elements of a parameter that is an array of clusters. See Also LabVIEWNXGParameters

### LabVIEWNXGParameter.Elements

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).Elements

#### Data Type

[LabVIEWNXGParameters](labviewnxgparameters.html)

#### Purpose

Returns a collection that accesses the members of a parameter that is a cluster, or accesses the elements of a parameter that is an array of clusters.

#### See Also

[LabVIEWNXGParameters](labviewnxgparameters.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-exprclustertypemismatch.html language=enus -->
## TOPIC 01482: LabVIEWNXGParameter.ExprClusterTypeMismatch

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-exprclustertypemismatch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-exprclustertypemismatch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.ExprClusterTypeMismatch( sequenceContext) Return Value Boolean Purpose Returns True if you enable cluster mapping for the variable or property the expression value returns and the names or types of cluster elements do not match the LabVIEW NXG cluster the VI specifies. Oth

### LabVIEWNXGParameter.ExprClusterTypeMismatch

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).ExprClusterTypeMismatch( sequenceContext)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if you enable cluster mapping for the variable or property the expression value returns and the names or types of cluster elements do not match the LabVIEW NXG cluster the VI specifies. Otherwise this method returns
 False
 .

#### Parameters

sequenceContext
 As
 
 [SequenceContext](sequencecontext.html)

[In] Specifies the
 SequenceContext
 to use to evaluate the parameter expression value.

#### See Also

[LabVIEWNXGParameter.Type](labviewnxgparameter-type.html)

[LabVIEWNXGParameter.ValueExpr](labviewnxgparameter-valueexpr.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-getarrayelementindex.html language=enus -->
## TOPIC 01483: LabVIEWNXGParameter.GetArrayElementIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-getarrayelementindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-getarrayelementindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.GetArrayElementIndex Data Type String Purpose Returns the index of the array element as an array index string. Remarks An array index string. Array index strings are a list of numbers enclosed in brackets that index each dimension of the array. For example, the following i

### LabVIEWNXGParameter.GetArrayElementIndex

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).GetArrayElementIndex

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the index of the array element as an array index string.

#### Remarks

An array index string. Array index strings are a list of numbers enclosed in brackets that index each dimension of the array. For example, the following is an array index for a two dimensional array: [0][1].

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-getarrayindex.html language=enus -->
## TOPIC 01484: LabVIEWNXGParameter.GetArrayIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-getarrayindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-getarrayindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.GetArrayIndex( offset) Return Value String An array index string. Array index strings are a list of numbers enclosed in brackets that index each dimension of the array. For example, the following is an array index for a two dimensional array: [0][1] . Purpose Returns the i

### LabVIEWNXGParameter.GetArrayIndex

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).GetArrayIndex( offset)

#### Return Value

[String](data-types-for-teststand.html)

An array index string. Array index strings are a list of numbers enclosed in brackets that index each dimension of the array. For example, the following is an array index for a two dimensional array:
 [0][1]
 .

#### Purpose

Returns the index of the array element the
 offset
 parameter specifies.

#### Parameters

offset
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based number representing the offset of an array element in the one-dimensional physical storage of the array. The offset is in terms of the number of elements.

#### See Also

[LabVIEWNXGParameter.ArrayDimensions](labviewnxgparameter-arraydimensions.html)

[LabVIEWNXGParameter.GetDefaultArrayDimensionSize](labviewnxgparameter-getdefaultarraydimensions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-getdefaultarraydimensions.html language=enus -->
## TOPIC 01485: LabVIEWNXGParameter.GetDefaultArrayDimensionSize

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-getdefaultarraydimensions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-getdefaultarraydimensions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.GetDefaultArrayDimensionSize( dimension) Return Value Long Purpose Returns the default size of the array corresponding to the zero-based index passed as input. Remarks The default size corresponds to the default size of the array control in the front panel of a VI. Call th

### LabVIEWNXGParameter.GetDefaultArrayDimensionSize

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).GetDefaultArrayDimensionSize( dimension)

#### Return Value

[Long](data-types-for-teststand.html)

#### Purpose

Returns the default size of the array corresponding to the zero-based index passed as input.

#### Remarks

The default size corresponds to the default size of the array control in the front panel of a VI. Call the
 [LabVIEWNXGModule.LoadVIInfo](labviewnxgmodule-loadviinfo.html)
 or
 [Module.LoadPrototype](module-loadprototype.html)
 method before calling this method.

#### Parameters

dimension
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index corresponding to one of the array dimensions.

#### See Also

[LabVIEWNXGModule.LoadVIInfo](labviewnxgmodule-loadviinfo.html)

[LabVIEWNXGParameter.ArrayDimensions](labviewnxgparameter-arraydimensions.html)

[LabVIEWNXGParameter.GetArrayIndex](labviewnxgparameter-getarrayindex.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-getenumvalues.html language=enus -->
## TOPIC 01486: LabVIEWNXGParameter.GetEnumValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-getenumvalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-getenumvalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.GetEnumValues Return Value Object Array Returns an array of property objects where each property object represents an enumeration value or a ring control value. Purpose Returns the enumeration constants for an enumeration parameter or returns the ring control values for a

### LabVIEWNXGParameter.GetEnumValues

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).GetEnumValues

#### Return Value

[Object Array](data-types-for-teststand.html)

Returns an array of property objects where each property object represents an enumeration value or a ring control value.

#### Purpose

Returns the enumeration constants for an enumeration parameter or returns the ring control values for a ring control parameter.

#### Remarks

Call the
 [LabVIEWNXGModule.LoadVIInfo](labviewnxgmodule-loadviinfo.html)
 method or the
 [Module.LoadPrototype](module-loadprototype.html)
 method before calling this method. The values stay in memory until the sequence file closes.

Note

Use the name and value of the property objects in the array this method returns to determine the name and value of the enumeration constants or ring controls.

Pass the return value of this method as the
 additionalConstants
 parameter of
 [Expression.ValidateEvaluationType](expression-validateevaluationtype.html)
 when checking the
 [LabVIEWNXGParameter.ValueExpr](labviewnxgparameter-valueexpr.html)
 property for errors.

If you are using an
 
 [ExpressionEdit](../tsuiref/expressionedit.html)
 control to display the value of the
 LabVIEWNXGParameter.ValueExpr
 property, pass the return value of this method to the
 
 [ExpressionEdit.SetAdditionalEvaluationConstants](../tsuiref/expressionedit-setadditionalevaluationconstan.html)
 method to instruct the ExpressionEdit control to validate enumeration constants.

#### See Also

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[ExpressionEdit.SetAdditionalEvaluationConstants](../tsuiref/expressionedit-setadditionalevaluationconstan.html)

[LabVIEWNXGParameter.Type](labviewnxgparameter-type.html)

[LabVIEWNXGParameter.ValueExpr](labviewnxgparameter-valueexpr.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-insertarrayelement.html language=enus -->
## TOPIC 01487: LabVIEWNXGParameter.InsertArrayElement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-insertarrayelement.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-insertarrayelement.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.InsertArrayElement( index) Purpose Inserts an array element at the specified index. Remarks This method is valid only for one-dimensional array parameters. Use the LabVIEWNXGParameter.ArrayDimensions property to determine the number of array dimensions. Parameters index As

### LabVIEWNXGParameter.InsertArrayElement

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).InsertArrayElement( index)

#### Purpose

Inserts an array element at the specified index.

#### Remarks

This method is valid only for one-dimensional array parameters. Use the
 [LabVIEWNXGParameter.ArrayDimensions](labviewnxgparameter-arraydimensions.html)
 property to determine the number of array dimensions.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the index at which to insert the array element. This value must be greater than or equal to
 0
 and less than or equal to the number of array elements.

#### See Also

[LabVIEWNXGParameter.ArrayDimensions](labviewnxgparameter-arraydimensions.html)

[LabVIEWNXGParameter.DeleteArrayElement](labviewnxgparameter-deletearrayelement.html)

[LabVIEWNXGParameter.Type](labviewnxgparameter-type.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-isclustermappinginvalid.html language=enus -->
## TOPIC 01488: LabVIEWNXGParameter.IsClusterMappingInvalid

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-isclustermappinginvalid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-isclustermappinginvalid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.IsClusterMappingInvalid( reasonNotValid) Return Value Boolean Returns True when all the following conditions are true: The parameter is a cluster or cluster array The argument expression is valid and non-empty The argument or cluster mapping of the argument is invalid In a

### LabVIEWNXGParameter.IsClusterMappingInvalid

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).IsClusterMappingInvalid( reasonNotValid)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 when all the following conditions are true:

- The parameter is a cluster or cluster array
- The argument expression is valid and non-empty
- The argument or cluster mapping of the argument is invalid

In all other cases, this method returns
 False
 .

#### Purpose

Returns a value that indicates whether the argument you specify for a LabVIEW cluster or cluster array parameter is valid by checking the cluster passing information for any custom data types used to confirm that the information matches the cluster definition stored when you specified the module.

Note

#### Parameters

reasonNotValid
 As
 [String](data-types-for-teststand.html)

[Out] When this method returns
 True
 , this parameter returns the reason why the argument is invalid.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-isparametermappingvalid.html language=enus -->
## TOPIC 01489: LabVIEWNXGParameter.IsParameterMappingValid

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-isparametermappingvalid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-isparametermappingvalid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.IsParameterMappingValid( reasonNotValid) Return Value Boolean Returns True when all the following conditions are true: (1) the parameter is a cluster or cluster array or enumeration or enumeration array, (2) the argument expression is valid and not empty, (3) the cluster m

### LabVIEWNXGParameter.IsParameterMappingValid

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).IsParameterMappingValid( reasonNotValid)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 when all the following conditions are true: (1) the parameter is a cluster or cluster array or enumeration or enumeration array, (2) the argument expression is valid and not empty, (3) the cluster mapping of the argument is valid if the parameter is a cluster, and (4) the argument value is compatible with the enumeration parameter if the parameter is an enumeration.

In all other cases, returns
 False
 .

#### Purpose

Returns a value that indicates whether the argument you specify for a LabVIEW cluster or cluster array parameter is valid. This method checks the cluster passing information for any custom data types used and confirms that the information matches the cluster definition stored when you specified the module. For an enumeration parameter, the method validates that: (1) If the argument is a number or TestStand enumeration type instance, the numeric representation is compatible with the LabVIEW parameter’s representation. (2) If the argument is a TestStand enumeration type, the enumerators of the TestStand type must match the enumerators of the LabVIEW parameter in
 Number
 and
 Name and value
 .

#### Parameters

reasonNotValid
 As
 [String](data-types-for-teststand.html)

[Out] When this method returns
 False
 , this parameter returns an explanation for why the argument is invalid.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-nodeusesdefaultvalue.html language=enus -->
## TOPIC 01490: LabVIEWNXGParameter.NodeUsesDefaultValue

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-nodeusesdefaultvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-nodeusesdefaultvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.NodeUsesDefaultValue Data Type Boolean Purpose Returns a value that indicates whether the parameter is associated with a LabVIEW NXG property configured to use the default value in a call. Remarks Returns True when the parameter is associated with a LabVIEW NXG property co

### LabVIEWNXGParameter.NodeUsesDefaultValue

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).NodeUsesDefaultValue

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the parameter is associated with a LabVIEW NXG property configured to use the default value in a call.

#### Remarks

Returns
 True
 when the parameter is associated with a LabVIEW NXG property configured to use the default value.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-parametername.html language=enus -->
## TOPIC 01491: LabVIEWNXGParameter.ParameterName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-parametername.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-parametername.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.ParameterName Data Type String Purpose Returns the name of the parameter in the VI. Remarks The LabVIEW NXG Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the Module.LoadPrototype method before retriev

### LabVIEWNXGParameter.ParameterName

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).ParameterName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the parameter in the VI.

#### Remarks

The LabVIEW NXG Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the
 [Module.LoadPrototype](module-loadprototype.html)
 method before retrieving this property.

#### See Also

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-partiallyspecified.html language=enus -->
## TOPIC 01492: LabVIEWNXGParameter.PartiallySpecified

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-partiallyspecified.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-partiallyspecified.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.PartiallySpecified Data Type Boolean Purpose Returns a value that indicates whether the parameter is partially specified. Remarks A parameter is partially specified if some of the parameter elements specify to use default values while other parameter elements specify expre

### LabVIEWNXGParameter.PartiallySpecified

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).PartiallySpecified

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the parameter is partially specified.

#### Remarks

A parameter is partially specified if some of the parameter elements specify to use default values while other parameter elements specify expression values.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-passasbinarystring.html language=enus -->
## TOPIC 01493: LabVIEWNXGParameter.PassAsBinaryString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-passasbinarystring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-passasbinarystring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.PassAsBinaryString Data Type Boolean Purpose Specifies if TestStand preserves NUL bytes when setting and getting LabVIEW NXG string data. Remarks This property applies only when the LabVIEWNXGParameter.Category property of the parameter is LVParamCategory_String or LVParam

### LabVIEWNXGParameter.PassAsBinaryString

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).PassAsBinaryString

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if TestStand preserves NUL bytes when setting and getting LabVIEW NXG string data.

#### Remarks

This property applies only when the
 [LabVIEWNXGParameter.Category](labviewnxgparameter-category.html)
 property of the parameter is
 LVParamCategory_String
 or
 LVParamCategory_StringArray
 and the
 [LabVIEWNXGParameter.Type](labviewnxgparameter-type.html)
 property of the parameter is
 LabVIEWNXGParamType_String
 .

When this property is
 False
 , the LabVIEW NXG Adapter treats strings as C-style strings with a NUL character to indicate the end of the string. C-strings cannot contain binary data.

Call the
 [PropertyObject.GetValBinary](propertyobject-getvalbinary.html)
 method on the variable that stores the binary string to retrieve the raw data in TestStand when the binary data is compressed.

#### See Also

[LabVIEWNXGParameter.Category](labviewnxgparameter-category.html)

[LabVIEWNXGParameter.Type](labviewnxgparameter-type.html)

[LabVIEWNXGParameterCategories](labviewnxgparametercategories.html)

[LabVIEWNXGParameterTypes](labviewnxgparametertypes.html)

[PropertyObject.GetValBinary](propertyobject-getvalbinary.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-type.html language=enus -->
## TOPIC 01494: LabVIEWNXGParameter.Type

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-type.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.Type Data Type LabVIEWNXGParameterTypes Purpose Returns the data type of the parameter element, specifically indicating the type of number, string, and so on. Remarks Obtain the category using the LabVIEWNXGParameter.Category property before obtaining the data type of the

### LabVIEWNXGParameter.Type

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).Type

#### Data Type

[LabVIEWNXGParameterTypes](labviewnxgparametertypes.html)

#### Purpose

Returns the data type of the parameter element, specifically indicating the type of number, string, and so on.

#### Remarks

Obtain the
 [category](labviewnxgparametercategories.html)
 using the
 [LabVIEWNXGParameter.Category](labviewnxgparameter-category.html)
 property before obtaining the data type of the parameter.

The LabVIEW NXG Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the
 [Module.LoadPrototype](module-loadprototype.html)
 method before retrieving this property.

#### See Also

[LabVIEWNXGParameter.Category](labviewnxgparameter-category.html)

[LabVIEWNXGParameter.TypeDisplayString](labviewnxgparameter-typedisplaystring.html)

[LabVIEWNXGParameterCategories](labviewnxgparametercategories.html)

[LabVIEWNXGParameterTypes](labviewnxgparametertypes.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-typedisplaystring.html language=enus -->
## TOPIC 01495: LabVIEWNXGParameter.TypeDisplayString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-typedisplaystring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-typedisplaystring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.TypeDisplayString Data Type String Purpose Returns a string that describes the type of the parameter. See Also LabVIEWNXGParameter.Type

### LabVIEWNXGParameter.TypeDisplayString

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).TypeDisplayString

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns a string that describes the type of the parameter.

#### See Also

[LabVIEWNXGParameter.Type](labviewnxgparameter-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-updateclustermapping.html language=enus -->
## TOPIC 01496: LabVIEWNXGParameter.UpdateClusterMapping

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-updateclustermapping.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-updateclustermapping.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.UpdateClusterMapping( sequenceContext) Return Value Boolean Returns True if the method updates any expression values for the elements of the cluster parameter. Purpose Updates the expression values for the cluster parameter elements when the parameter specifies an expressi

### LabVIEWNXGParameter.UpdateClusterMapping

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).UpdateClusterMapping( sequenceContext)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the method updates any expression values for the elements of the cluster parameter.

#### Purpose

Updates the expression values for the cluster parameter elements when the parameter specifies an expression value that evaluates to a named data type that enables cluster passing.

#### Remarks

This method is valid only on cluster parameters.

#### Parameters

sequenceContext
 As
 
 [SequenceContext](sequencecontext.html)

[In] Pass the sequence context that the dialog box uses to evaluate all value expressions. You can use the
 [Engine.NewEditContext](engine-neweditcontext.html)
 method to obtain an edit-time sequence context.

#### See Also

[Engine.NewEditContext](engine-neweditcontext.html)

[LabVIEWNXGParameter.Type](labviewnxgparameter-type.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-usedefaultvalue.html language=enus -->
## TOPIC 01497: LabVIEWNXGParameter.UseDefaultValue

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-usedefaultvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-usedefaultvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.UseDefaultValue Data Type Boolean Purpose Specifies whether to use the default value of the parameter when calling the VI. Remarks You can use the default value for recommended or optional parameters. See Also LabVIEWNXGParameter.PartiallySpecified LabVIEWNXGParameter.Valu

### LabVIEWNXGParameter.UseDefaultValue

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).UseDefaultValue

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether to use the default value of the parameter when calling the VI.

#### Remarks

You can use the default value for recommended or optional parameters.

#### See Also

[LabVIEWNXGParameter.PartiallySpecified](labviewnxgparameter-partiallyspecified.html)

[LabVIEWNXGParameter.ValueExpr](labviewnxgparameter-valueexpr.html)

[LabVIEWNXGParameter.WireRequirement](labviewnxgparameter-wirerequirement.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-userdata.html language=enus -->
## TOPIC 01498: LabVIEWNXGParameter.UserData

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-userdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-userdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.UserData Data Type PropertyObject Purpose Holds a data item you associate with the parameter object. Remarks Typically, you do not use this property. See Also PropertyObject

### LabVIEWNXGParameter.UserData

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).UserData

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Holds a data item you associate with the parameter object.

#### Remarks

Typically, you do not use this property.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-validevaluationtypes.html language=enus -->
## TOPIC 01499: LabVIEWNXGParameter.ValidEvaluationTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-validevaluationtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-validevaluationtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.ValidEvaluationTypes Data Type EvaluationTypes Purpose Returns the valid types to which this parameter can evaluate. Remarks You can pass the value of this property to the validEvaluationTypes parameter of the Expression.ValidateEvaluationType method to determine whether t

### LabVIEWNXGParameter.ValidEvaluationTypes

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).ValidEvaluationTypes

#### Data Type

[EvaluationTypes](evaluationtypes.html)

#### Purpose

Returns the valid types to which this parameter can evaluate.

#### Remarks

You can pass the value of this property to the
 validEvaluationTypes
 parameter of the
 [Expression.ValidateEvaluationType](expression-validateevaluationtype.html)
 method to determine whether the value of the
 [LabVIEWNXGParameter.ValueExpr](labviewnxgparameter-valueexpr.html)
 property contains errors.

If you are using an ExpressionEdit control to display the value of the
 LabVIEWParameter.ValueExpr
 property, pass the value of this property to the
 
 [ExpressionEdit.SetValidEvaluationTypes](../tsuiref/expressionedit-setvalidevaluationtypes.html)
 method.

#### See Also

[EvaluationTypes](evaluationtypes.html)

[EvaluationTypes.PropertyValueTypeFlags](evaluationtypes-propertyvaluetypeflags.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[ExpressionEdit.GetValidEvaluationTypes](../tsuiref/expressionedit-getvalidevaluationtypes.html)

[ExpressionEdit.SetValidEvaluationTypes](../tsuiref/expressionedit-setvalidevaluationtypes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-valueexpr.html language=enus -->
## TOPIC 01500: LabVIEWNXGParameter.ValueExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-valueexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-valueexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.ValueExpr Data Type String Purpose Specifies an expression to define the argument to pass for the parameter when calling the VI. Remarks TestStand ignores this parameter if the LabVIEWNXGParameter.UseDefaultValue property is True . Call the LabVIEWNXGModule.LoadVIInfo meth

### LabVIEWNXGParameter.ValueExpr

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).ValueExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an expression to define the argument to pass for the parameter when calling the VI.

#### Remarks

TestStand ignores this parameter if the
 [LabVIEWNXGParameter.UseDefaultValue](labviewnxgparameter-usedefaultvalue.html)
 property is
 True
 .

Call the
 [LabVIEWNXGModule.LoadVIInfo](labviewnxgmodule-loadviinfo.html)
 method before you get or set this property to ensure that LabVIEW parameters, such as enumeration values and ring controls, are updated with their current definitions.

#### See Also

[LabVIEWNXGParameter.DefaultValue](labviewnxgparameter-defaultvalue.html)

[LabVIEWNXGParameter.UseDefaultValue](labviewnxgparameter-usedefaultvalue.html)

Parent topic:

Properties
