# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=251 end=500 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexserver-displayname.html language=enus -->
## TOPIC 00251: ActiveXServer.DisplayName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexserver-displayname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexserver-displayname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServer.DisplayName Data Type String Purpose Returns the display name of the server. See Also ActiveXServer.Name

### ActiveXServer.DisplayName

#### Syntax

[ActiveXServer](activexserver.html).DisplayName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the display name of the server.

#### See Also

[ActiveXServer.Name](activexserver-name.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexserver-helpcontext.html language=enus -->
## TOPIC 00252: ActiveXServer.HelpContext

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexserver-helpcontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexserver-helpcontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServer.HelpContext Data Type Long Purpose Returns the ID of the help topic for the server in the help file the ActiveXServer.HelpFilePath property specifies. See Also ActiveXServer.HelpFilePath

### ActiveXServer.HelpContext

#### Syntax

[ActiveXServer](activexserver.html).HelpContext

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the ID of the help topic for the server in the help file the
 [ActiveXServer.HelpFilePath](activexserver-helpfilepath.html)
 property specifies.

#### See Also

[ActiveXServer.HelpFilePath](activexserver-helpfilepath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexserver-helpfilepath.html language=enus -->
## TOPIC 00253: ActiveXServer.HelpFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexserver-helpfilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexserver-helpfilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServer.HelpFilePath Data Type String Purpose Returns the absolute path of the help file of the server. See Also ActiveXServer.HelpContext

### ActiveXServer.HelpFilePath

#### Syntax

[ActiveXServer](activexserver.html).HelpFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the absolute path of the help file of the server.

#### See Also

[ActiveXServer.HelpContext](activexserver-helpcontext.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexserver-id.html language=enus -->
## TOPIC 00254: ActiveXServer.Id

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexserver-id.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexserver-id.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServer.Id Data Type String Purpose Returns the GUID of the server. See Also ActiveXServer.Name

### ActiveXServer.Id

#### Syntax

[ActiveXServer](activexserver.html).Id

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the GUID of the server.

#### See Also

[ActiveXServer.Name](activexserver-name.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexserver-interfaces.html language=enus -->
## TOPIC 00255: ActiveXServer.Interfaces

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexserver-interfaces.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexserver-interfaces.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServer.Interfaces Data Type ActiveXInterfaces Purpose Returns the interfaces defined in this server. Remarks You must call the ActiveXServer.LoadTypeLibrary method to load the interfaces from the type library and populate this collection. See Also ActiveXInterfaces ActiveXServer.CoClas

### ActiveXServer.Interfaces

#### Syntax

[ActiveXServer](activexserver.html).Interfaces

#### Data Type

[ActiveXInterfaces](activexinterfaces.html)

#### Purpose

Returns the interfaces defined in this server.

#### Remarks

You must call the
 [ActiveXServer.LoadTypeLibrary](activexserver-loadtypelibrary.html)
 method to load the interfaces from the type library and populate this collection.

#### See Also

[ActiveXInterfaces](activexinterfaces.html)

[ActiveXServer.CoClasses](activexserver-coclasses.html)

[ActiveXServer.LoadTypeLibrary](activexserver-loadtypelibrary.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexserver-libraryflags.html language=enus -->
## TOPIC 00256: ActiveXServer.LibraryFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexserver-libraryflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexserver-libraryflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServer.LibraryFlags Data Type Long Purpose Returns the library flags of the server. This property can be any combination of LIBFLAGS defined in the Microsoft Windows Software Development Kit.

### ActiveXServer.LibraryFlags

#### Syntax

[ActiveXServer](activexserver.html).LibraryFlags

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the library flags of the server. This property can be any combination of LIBFLAGS defined in the Microsoft Windows Software Development Kit.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexserver-loadtypelibrary.html language=enus -->
## TOPIC 00257: ActiveXServer.LoadTypeLibrary

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexserver-loadtypelibrary.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexserver-loadtypelibrary.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServer.LoadTypeLibrary Return Value Boolean Returns True if this method updates the ActiveXServer.CoClasses and ActiveXServer.Interfaces collections from the type library. This method does nothing and returns False if the type library was not modified on disk since the last time you ca

### ActiveXServer.LoadTypeLibrary

#### Syntax

[ActiveXServer](activexserver.html).LoadTypeLibrary

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if this method updates the
 [ActiveXServer.CoClasses](activexserver-coclasses.html)
 and
 [ActiveXServer.Interfaces](activexserver-interfaces.html)
 collections from the type library. This method does nothing and returns
 False
 if the type library was not modified on disk since the last time you called this method.

#### Purpose

Populates the
 ActiveXServer.CoClasses
 and
 ActiveXServer.Interfaces
 collections from the coclasses and interfaces defined in the type library the
 [ActiveXServer.Path](activexserver-path.html)
 property specifies.

#### See Also

[ActiveXServer.CoClasses](activexserver-coclasses.html)

[ActiveXServer.Interfaces](activexserver-interfaces.html)

[ActiveXServer.Path](activexserver-path.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexserver-localeid.html language=enus -->
## TOPIC 00258: ActiveXServer.LocaleId

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexserver-localeid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexserver-localeid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServer.LocaleId Data Type Long Purpose Returns the locale ID of the server.

### ActiveXServer.LocaleId

#### Syntax

[ActiveXServer](activexserver.html).LocaleId

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the locale ID of the server.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexserver-majorversion.html language=enus -->
## TOPIC 00259: ActiveXServer.MajorVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexserver-majorversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexserver-majorversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServer.MajorVersion Data Type Long Purpose Returns the major version of the server. See Also ActiveXServer.MinorVersion ActiveXServer.VersionString

### ActiveXServer.MajorVersion

#### Syntax

[ActiveXServer](activexserver.html).MajorVersion

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the major version of the server.

#### See Also

[ActiveXServer.MinorVersion](activexserver-minorversion.html)

[ActiveXServer.VersionString](activexserver-versionstring.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexserver-minorversion.html language=enus -->
## TOPIC 00260: ActiveXServer.MinorVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexserver-minorversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexserver-minorversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServer.MinorVersion Data Type Long Purpose Returns the minor version of the server. See Also ActiveXServer.MajorVersion ActiveXServer.VersionString

### ActiveXServer.MinorVersion

#### Syntax

[ActiveXServer](activexserver.html).MinorVersion

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the minor version of the server.

#### See Also

[ActiveXServer.MajorVersion](activexserver-majorversion.html)

[ActiveXServer.VersionString](activexserver-versionstring.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexserver-name.html language=enus -->
## TOPIC 00261: ActiveXServer.Name

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexserver-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexserver-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServer.Name Data Type String Purpose Returns the name of the server. See Also ActiveXServer.DisplayName ActiveXServer.Id

### ActiveXServer.Name

#### Syntax

[ActiveXServer](activexserver.html).Name

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the server.

#### See Also

[ActiveXServer.DisplayName](activexserver-displayname.html)

[ActiveXServer.Id](activexserver-id.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexserver-path.html language=enus -->
## TOPIC 00262: ActiveXServer.Path

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexserver-path.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexserver-path.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServer.Path Data Type String Purpose Returns the absolute path of the server.

### ActiveXServer.Path

#### Syntax

[ActiveXServer](activexserver.html).Path

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the absolute path of the server.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexserver-versionstring.html language=enus -->
## TOPIC 00263: ActiveXServer.VersionString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexserver-versionstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexserver-versionstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServer.VersionString Data Type String Purpose Returns the version string of the server. Remarks This property displays the major version and minor version as hexadecimal numbers. See Also ActiveXServer.MajorVersion ActiveXServer.MinorVersion

### ActiveXServer.VersionString

#### Syntax

[ActiveXServer](activexserver.html).VersionString

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the version string of the server.

#### Remarks

This property displays the major version and minor version as hexadecimal numbers.

#### See Also

[ActiveXServer.MajorVersion](activexserver-majorversion.html)

[ActiveXServer.MinorVersion](activexserver-minorversion.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexserver.html language=enus -->
## TOPIC 00264: ActiveXServer

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexserver.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexserver.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an ActiveXServer object to obtain information about a server and its type library registered on this computer. Use the ActiveXAdapter.Servers property to obtain a collection of ActiveXServer objects. You must call the ActiveXServer.LoadTypeLibrary method before you access any type library relate

### ActiveXServer

Use an ActiveXServer object to obtain information about a server and its type library registered on this computer. Use the
 [ActiveXAdapter.Servers](activexadapter-servers.html)
 property to obtain a collection of ActiveXServer objects. You must call the
 [ActiveXServer.LoadTypeLibrary](activexserver-loadtypelibrary.html)
 method before you access any type library related properties.

#### Properties

| CoClasses (Read Only) |
| --- |
| DisplayName (Read Only) |
| HelpContext (Read Only) |
| HelpFilePath (Read Only) |
| Id (Read Only) |
| Interfaces (Read Only) |
| LibraryFlags (Read Only) |
| LocaleId (Read Only) |
| MajorVersion (Read Only) |
| MinorVersion (Read Only) |
| Name (Read Only) |
| Path (Read Only) |
| VersionString (Read Only) |

#### Method

| LoadTypeLibrary |
| --- |

#### See Also

[ActiveXAdapter.Servers](activexadapter-servers.html)

[ActiveXServer.LoadTypeLibrary](activexserver-loadtypelibrary.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexservers-count.html language=enus -->
## TOPIC 00265: ActiveXServers.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexservers-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexservers-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServers.Count Data Type Long Purpose Returns the number of items in the collection. Remarks The first time you access the ActiveXServer.Item property or this property, ActiveXServers reads the list of servers registered on the computer from the registry. See Also ActiveXServers.Item

### ActiveXServers.Count

#### Syntax

[ActiveXServers](activexservers.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

#### Remarks

The first time you access the
 [ActiveXServer.Item](activexservers-item.html)
 property or this property, ActiveXServers reads the list of servers registered on the computer from the registry.

#### See Also

[ActiveXServers.Item](activexservers-item.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexservers-item.html language=enus -->
## TOPIC 00266: ActiveXServers.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexservers-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexservers-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServers.Item( index) Data Type ActiveXServer Purpose Returns a reference to an item at the specified index in the collection. Remarks The first time you access this property or the ActiveXServer.Count property, ActiveXServers reads the list of servers registered on the computer from th

### ActiveXServers.Item

#### Syntax

[ActiveXServers](activexservers.html).Item( index)

#### Data Type

[ActiveXServer](activexserver.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Remarks

The first time you access this property or the
 [ActiveXServer.Count](activexservers-count.html)
 property, ActiveXServers reads the list of servers registered on the computer from the registry.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve.

#### See Also

[ActiveXServer](activexserver.html)

[ActiveXServers.Count](activexservers-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexservers-refresh.html language=enus -->
## TOPIC 00267: ActiveXServers.Refresh

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexservers-refresh.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexservers-refresh.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServers.Refresh Purpose Call this method to refresh the ActiveXServer objects in the collection. Remarks After calling this method, ActiveXServers contains a new collection of ActiveXServer objects. After calling this method, do not access properties or methods of any ActiveXServer obj

### ActiveXServers.Refresh

#### Syntax

[ActiveXServers](activexservers.html).Refresh

#### Purpose

Call this method to refresh the ActiveXServer objects in the collection.

#### Remarks

After calling this method, ActiveXServers contains a new collection of ActiveXServer objects. After calling this method, do not access properties or methods of any ActiveXServer object you acquired before calling this method.

#### See Also

[ActiveXServers.RefreshCount](activexservers-refreshcount.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexservers-refreshcount.html language=enus -->
## TOPIC 00268: ActiveXServers.RefreshCount

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexservers-refreshcount.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexservers-refreshcount.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServers.RefreshCount Data Type Long Purpose Returns the number of times the ActiveXServer.Refresh method has been called. Remarks Use this property to determine whether a call to the ActiveXServer.Refresh method has created new objects in the collection. See Also ActiveXServers.Refresh

### ActiveXServers.RefreshCount

#### Syntax

[ActiveXServers](activexservers.html).RefreshCount

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of times the
 [ActiveXServer.Refresh](activexservers-refresh.html)
 method has been called.

#### Remarks

Use this property to determine whether a call to the
 ActiveXServer.Refresh
 method has created new objects in the collection.

#### See Also

[ActiveXServers.Refresh](activexservers-refresh.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexservers-registertypelibrary.html language=enus -->
## TOPIC 00269: ActiveXServers.RegisterTypeLibrary

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexservers-registertypelibrary.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexservers-registertypelibrary.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServers.RegisterTypeLibrary( typeLibraryPath, newerTypeLibraryAlreadyRegistered) Return Value String Returns the GUID of the type library this method registers. Purpose Registers the specified type library on this computer. Remarks This method updates ActiveXServers' collection of Acti

### ActiveXServers.RegisterTypeLibrary

#### Syntax

[ActiveXServers](activexservers.html).RegisterTypeLibrary( typeLibraryPath, newerTypeLibraryAlreadyRegistered)

#### Return Value

[String](data-types-for-teststand.html)

Returns the GUID of the type library this method registers.

#### Purpose

Registers the specified type library on this computer.

#### Remarks

This method updates ActiveXServers' collection of ActiveXServer objects to include the type library you specified.

#### Parameters

typeLibraryPath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute path of the file that contains the type library you want to register. Typically you specify a
 .exe
 ,
 .dll
 , or
 .tlb
 file.

newerTypeLibraryAlreadyRegistered
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns
 True
 if a newer version of the type library you specified was already registered on the computer.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexservers.html language=enus -->
## TOPIC 00270: ActiveXServers

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexservers.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexservers.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of ActiveXServer objects. Use the ActiveXAdapter.Servers property to obtain a collection of ActiveXServer objects. You must call the ActiveXServer.LoadTypeLibrary method before you access any type library related properties. Properties Count (Read Only) Item (Read Only) RefreshCount (Re

### ActiveXServers

A collection of
 [ActiveXServer](activexserver.html)
 objects.

Use the
 [ActiveXAdapter.Servers](activexadapter-servers.html)
 property to obtain a collection of ActiveXServer objects. You must call the
 [ActiveXServer.LoadTypeLibrary](activexserver-loadtypelibrary.html)
 method before you access any type library related properties.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |
| RefreshCount (Read Only) |

#### Methods

| Refresh |
| --- |
| RegisterTypeLibrary |

#### See Also

[ActiveXAdapter.Servers](activexadapter-servers.html)

[ActiveXServer](activexserver.html)

[ActiveXServer.LoadTypeLibrary](activexserver-loadtypelibrary.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/adapter-api-related-constants.html language=enus -->
## TOPIC 00271: Adapter API-Related Constants

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/adapter-api-related-constants.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/adapter-api-related-constants.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains detailed information about each TestStand adapter API-related constant.

### Adapter API-Related Constants

This book contains detailed information about each TestStand adapter API-related constant.

Parent topic:

API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/adapter-api-related-enumerations.html language=enus -->
## TOPIC 00272: Adapter API-Related Enumerations

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/adapter-api-related-enumerations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/adapter-api-related-enumerations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains detailed information about each TestStand adapter API-related enumeration.

### Adapter API-Related Enumerations

This book contains detailed information about each TestStand adapter API-related enumeration.

Parent topic:

API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/adapter-aspropertyobject.html language=enus -->
## TOPIC 00273: Adapter.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/adapter-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/adapter-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Adapter.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the adapter. Remarks Use the PropertyObject to edit, add, or remove custom properties of the adapter. See Also PropertyObject

### Adapter.AsPropertyObject

#### Syntax

[Adapter](adapter.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the adapter.

#### Remarks

Use the PropertyObject to edit, add, or remove custom properties of the adapter.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/adapter-configure.html language=enus -->
## TOPIC 00274: Adapter.Configure

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/adapter-configure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/adapter-configure.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Adapter.Configure Purpose Launches the Adapter Configuration dialog box for the adapter. Remarks When Adapter.IsConfigurable is False , calling this method has no effect. See Also Adapter Configuration dialog box Adapter.IsConfigurable

### Adapter.Configure

#### Syntax

[Adapter](adapter.html).Configure

#### Purpose

Launches the
 [Adapter Configuration](../tsref/adapter-configuration-dialog-box.html)
 dialog box for the adapter.

#### Remarks

When
 [Adapter.IsConfigurable](adapter-isconfigurable.html)
 is
 False
 , calling this method has no effect.

#### See Also

[Adapter Configuration dialog box](../tsref/adapter-configuration-dialog-box.html)

[Adapter.IsConfigurable](adapter-isconfigurable.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/adapter-displayname.html language=enus -->
## TOPIC 00275: Adapter.DisplayName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/adapter-displayname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/adapter-displayname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Adapter.DisplayName Data Type String Purpose Returns the name to display for the adapter. See Also Adapter.KeyName

### Adapter.DisplayName

#### Syntax

[Adapter](adapter.html).DisplayName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name to display for the adapter.

#### See Also

[Adapter.KeyName](adapter-keyname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/adapter-hidden.html language=enus -->
## TOPIC 00276: Adapter.Hidden

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/adapter-hidden.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/adapter-hidden.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Adapter.Hidden Data Type Boolean Purpose Specifies if the adapter is present in the list of adapters. This property is used to hide the adapter. Remarks Set this property to True to hide the adapter in controls that display the list of adapters.

### Adapter.Hidden

#### Syntax

[Adapter](adapter.html).Hidden

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if the adapter is present in the list of adapters. This property is used to hide the adapter.

#### Remarks

Set this property to
 True
 to hide the adapter in controls that display the list of adapters.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/adapter-iconname.html language=enus -->
## TOPIC 00277: Adapter.IconName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/adapter-iconname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/adapter-iconname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Adapter.IconName Data Type String Purpose Returns the icon filename for the adapter. Remarks Icon files are located in the <TestStand> \Components\Icons and <TestStand Public>\Components\Icons directories. See Also Adapter.LargeIcon Adapter.SmallIcon

### Adapter.IconName

#### Syntax

[Adapter](adapter.html).IconName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the icon filename for the adapter.

#### Remarks

Icon files are located in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 and
 <TestStand Public>\Components\Icons
 directories.

#### See Also

[Adapter.LargeIcon](adapter-largeicon.html)

[Adapter.SmallIcon](adapter-smallicon.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/adapter-isconfigurable.html language=enus -->
## TOPIC 00278: Adapter.IsConfigurable

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/adapter-isconfigurable.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/adapter-isconfigurable.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Adapter.IsConfigurable Data Type Boolean Purpose Returns True if the adapter has an Adapter Configuration dialog box you can launch using the Adapter.Configure method. See Also Adapter Configuration dialog box Adapter.Configure

### Adapter.IsConfigurable

#### Syntax

[Adapter](adapter.html).IsConfigurable

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the adapter has an
 [Adapter Configuration](../tsref/adapter-configuration-dialog-box.html)
 dialog box you can launch using the
 [Adapter.Configure](adapter-configure.html)
 method.

#### See Also

[Adapter Configuration dialog box](../tsref/adapter-configuration-dialog-box.html)

[Adapter.Configure](adapter-configure.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/adapter-issupported.html language=enus -->
## TOPIC 00279: Adapter.IsSupported

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/adapter-issupported.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/adapter-issupported.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Adapter.IsSupported Data Type Boolean Purpose Indicates whether this adapter is supported by the current instance of the TestStand Engine. Remarks Use this property to check if an adapter is supported by the current instance of TestStand Engine. Unsupported adapters exist in the TestStand Eng

### Adapter.IsSupported

#### Syntax

[Adapter](adapter.html).IsSupported

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Indicates whether this adapter is supported by the current instance of the TestStand Engine.

#### Remarks

Use this property to check if an adapter is supported by the current instance of TestStand Engine.

Unsupported adapters exist in the TestStand Engine so that TestStand can open sequence files containing unsupported adapter steps. You can view and edit these sequence files, even though you cannot execute the unsupported steps.

Support for an adapter can depend on the bitness of TestStand. For example, 32-bit TestStand does not support the LabVIEW NXG Adapter.

#### See Also

[Engine.Is64Bit](engine-is64bit.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/adapter-keyname.html language=enus -->
## TOPIC 00280: Adapter.KeyName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/adapter-keyname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/adapter-keyname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Adapter.KeyName Data Type String Purpose Returns the name other TestStand API functions, such as the Engine.NewStep method, use to refer to the adapter. See Also Adapter.DisplayName Engine.NewStep

### Adapter.KeyName

#### Syntax

[Adapter](adapter.html).KeyName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name other TestStand API functions, such as the
 [Engine.NewStep](engine-newstep.html)
 method, use to refer to the adapter.

#### See Also

[Adapter.DisplayName](adapter-displayname.html)

[Engine.NewStep](engine-newstep.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/adapter-largeicon.html language=enus -->
## TOPIC 00281: Adapter.LargeIcon

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/adapter-largeicon.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/adapter-largeicon.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Adapter.LargeIcon Data Type Picture Purpose Returns a large icon that represents the adapter. See Also Adapter.IconName Adapter.LargeIconIndex Adapter.SmallIcon

### Adapter.LargeIcon

#### Syntax

[Adapter](adapter.html).LargeIcon

#### Data Type

[Picture](data-types-for-teststand.html)

#### Purpose

Returns a large icon that represents the adapter.

#### See Also

[Adapter.IconName](adapter-iconname.html)

[Adapter.LargeIconIndex](adapter-largeiconindex.html)

[Adapter.SmallIcon](adapter-smallicon.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/adapter-largeiconindex.html language=enus -->
## TOPIC 00282: Adapter.LargeIconIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/adapter-largeiconindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/adapter-largeiconindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Adapter.LargeIconIndex Data Type Long Purpose Returns a unique index for the large icon that represents the adapter. Use this index to retrieve the icon from the image list you obtain with the Engine.LargeImageListEx property. See Also Adapter.IconName Adapter.LargeIcon Adapter.SmallIconIndex

### Adapter.LargeIconIndex

#### Syntax

[Adapter](adapter.html).LargeIconIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns a unique index for the large icon that represents the adapter. Use this index to retrieve the icon from the image list you obtain with the
 [Engine.LargeImageListEx](engine-largeimagelistex.html)
 property.

#### See Also

[Adapter.IconName](adapter-iconname.html)

[Adapter.LargeIcon](adapter-largeicon.html)

[Adapter.SmallIconIndex](adapter-smalliconindex.html)

[Engine.LargeImageListEx](engine-largeimagelistex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/adapter-showargsinstepdescription.html language=enus -->
## TOPIC 00283: Adapter.ShowArgsInStepDescription

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/adapter-showargsinstepdescription.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/adapter-showargsinstepdescription.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Adapter.ShowArgsInStepDescription Data Type Boolean Purpose Specifies that the description for the step that uses the adapter includes the arguments the step passes to the methods or sequences they call. See Also Step.GetDescriptionEx

### Adapter.ShowArgsInStepDescription

#### Syntax

[Adapter](adapter.html).ShowArgsInStepDescription

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies that the description for the step that uses the adapter includes the arguments the step passes to the methods or sequences they call.

#### See Also

[Step.GetDescriptionEx](step-getdescriptionex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/adapter-smallicon.html language=enus -->
## TOPIC 00284: Adapter.SmallIcon

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/adapter-smallicon.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/adapter-smallicon.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Adapter.SmallIcon Data Type Picture Purpose Returns a small icon that represents the adapter. See Also Adapter.IconName Adapter.LargeIcon Adapter.SmallIconIndex

### Adapter.SmallIcon

#### Syntax

[Adapter](adapter.html).SmallIcon

#### Data Type

[Picture](data-types-for-teststand.html)

#### Purpose

Returns a small icon that represents the adapter.

#### See Also

[Adapter.IconName](adapter-iconname.html)

[Adapter.LargeIcon](adapter-largeicon.html)

[Adapter.SmallIconIndex](adapter-smalliconindex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/adapter-smalliconindex.html language=enus -->
## TOPIC 00285: Adapter.SmallIconIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/adapter-smalliconindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/adapter-smalliconindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Adapter.SmallIconIndex Data Type Long Purpose Returns a unique index for the small icon that represents the adapter. Use this index to retrieve the icon from the image list you obtain with the Engine.SmallImageListEx property. See Also Adapter.IconName Adapter.LargeIconIndex Adapter.SmallIcon

### Adapter.SmallIconIndex

#### Syntax

[Adapter](adapter.html).SmallIconIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns a unique index for the small icon that represents the adapter. Use this index to retrieve the icon from the image list you obtain with the
 [Engine.SmallImageListEx](engine-smallimagelistex.html)
 property.

#### See Also

[Adapter.IconName](adapter-iconname.html)

[Adapter.LargeIconIndex](adapter-largeiconindex.html)

[Adapter.SmallIcon](adapter-smallicon.html)

[Engine.SmallImageListEx](engine-smallimagelistex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/adapter.html language=enus -->
## TOPIC 00286: Adapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/adapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/adapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use Adapter objects to configure and obtain information about the module adapters . Typically, you use this class only when you write a user interface application or sequence editor. If you are considering writing a user interface application, National Instruments recommends using the TestStand User

### Adapter

Use Adapter objects to configure and obtain information about the
 [module adapters](/csh?context=ts_tsfundamentals_module_adapters)
 .

Typically, you use this class only when you write a user interface application or sequence editor.

Note

TestStand User Interface (UI) Controls

To obtain an Adapter object, call the
 [Engine.GetAdapter](engine-getadapter.html)
 method. Pass a zero-based index to specify the Adapter object for which you want to obtain a reference. To find out the number of available adapters, obtain the value of the
 [Engine.NumAdapters](engine-numadapters.html)
 property.

#### Properties

| DisplayName (Read Only) |
| --- |
| Hidden |
| IconName (Read Only) |
| IsConfigurable (Read Only) |
| KeyName (Read Only) |
| LargeIcon (Read Only) |
| LargeIconIndex (Read Only) |
| ShowArgsInStepDescription |
| SmallIcon (Read Only) |
| SmallIconIndex (Read Only) |

#### Methods

| AsPropertyObject |
| --- |
| Configure |

#### See Also

[Engine.GetAdapter](engine-getadapter.html)

[Engine.NumAdapters](engine-numadapters.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/adaptercodetemplatepolicies.html language=enus -->
## TOPIC 00287: AdapterCodeTemplatePolicies

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/adaptercodetemplatepolicies.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/adaptercodetemplatepolicies.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the LabVIEWAdapter.CodeTemplatePolicy property to specify which code templates the LabVIEW Adapter uses during code generation. AdapterCodeTemplatePolicy_UseNewAndLegacy –(Value: 2) Specifies that the adapter searches for new and legacy code templates. AdapterCodeTemplatePol

### AdapterCodeTemplatePolicies

Use these constants with the
 [LabVIEWAdapter.CodeTemplatePolicy](labviewadapter-codetemplatepolicy.html)
 property to specify which code templates the LabVIEW Adapter uses during code generation.

- AdapterCodeTemplatePolicy_UseNewAndLegacy 
 –(Value: 2) Specifies that the adapter searches for new and legacy code templates.
- AdapterCodeTemplatePolicy_UseOnlyLegacy 
 –(Value: 1) Specifies that the adapter only searches for legacy code templates.
- AdapterCodeTemplatePolicy_UseOnlyNew 
 –(Value: 0) Specifies that the adapter only searches for new code templates.

#### See Also

[LabVIEWAdapter.CodeTemplatePolicy](labviewadapter-codetemplatepolicy.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/adapterkeynames.html language=enus -->
## TOPIC 00288: AdapterKeyNames

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/adapterkeynames.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/adapterkeynames.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these names when calling TestStand API functions, such as the Engine.NewStep method. AutomationAdapterKeyName –(Value: "Automation Adapter") DotNetAdapterKeyname –(Value: "DotNet Adapter") FlexCAdapterKeyName –(Value: "DLL Flexible Prototype Adapter") FlexCVIAdapterKeyName –(Value: "C/CVI Flexib

### AdapterKeyNames

Use these names when calling TestStand API functions, such as the
 [Engine.NewStep](engine-newstep.html)
 method.

- AutomationAdapterKeyName 
 –(Value: "Automation Adapter")
- DotNetAdapterKeyname 
 –(Value: "DotNet Adapter")
- FlexCAdapterKeyName 
 –(Value: "DLL Flexible Prototype Adapter")
- FlexCVIAdapterKeyName 
 –(Value: "C/CVI Flexible Prototype Adapter")
- FlexLVAdapterKeyName 
 –(Value: "G Flexible VI Adapter")
- GAdapterKeyName 
 –(Value: "G Std Prototype Adapter")
 Note 
 This constant is obsolete. Use
 FlexLVAdapterKeyName
 instead.
- HTBasicAdapterKeyName 
 –(Value: "HTBasic Adapter")
- LabVIEWNXGAdapterKeyName 
 –(Value: "LabVIEW NXG Adapter")
- LVAdapterKeyName 
 –(Value: "G Std Prototype Adapter")
 Note 
 This constant is obsolete. Use
 FlexLVAdapterKeyName
 instead.
- NoneAdapterKeyName 
 –(Value: "None Adapter")
- PythonAdapterKeyName 
 –(Value: "Python Adapter")
- SequenceAdapterKeyName 
 –(Value: "Sequence Adapter")
- StdCVIAdapterKeyName 
 –(Value: "C/CVI Std Prototype Adapter")
 Note 
 This constant is obsolete. Use FlexCVIAdapterKeyName instead.

#### See Also

[Engine.DefaultAdapter](engine-defaultadapter.html)

[Engine.GetAdapterByKeyName](engine-getadapterbykeyname.html)

[Engine.NewStep](engine-newstep.html)

[Step.AdapterKeyName](step-adapterkeyname.html)

[Step.ChangeAdapter](step-changeadapter.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresult-areelementsincompatiblewitht.html language=enus -->
## TOPIC 00289: AdditionalResult.AreElementsIncompatibleWithType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresult-areelementsincompatiblewitht.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresult-areelementsincompatiblewitht.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResult.AreElementsIncompatibleWithType Data Type Boolean Purpose Returns True if the members of the AdditionalResult.Elements collection are incompatible with the fields defined in the type that the AdditionalResult.Type property specifies. Remarks Setting the AdditionalResult.IsAny

### AdditionalResult.AreElementsIncompatibleWithType

#### Syntax

[AdditionalResult](additionalresult.html).AreElementsIncompatibleWithType

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the members of the
 [AdditionalResult.Elements](additionalresult-elements.html)
 collection are incompatible with the fields defined in the type that the
 [AdditionalResult.Type](additionalresult-type.html)
 property specifies.

#### Remarks

Setting the
 [AdditionalResult.IsAnyType](additionalresult-isanytype.html)
 property or the
 Type
 property updates the members in the
 Elements
 collection. The members of
 Elements
 are compatible with the
 Type
 property as long as the number of
 Elements
 is the same as the number of fields the
 Type
 property defines and the
 [AdditionalResult.Name](additionalresult-name.html)
 and
 Type
 properties of each member of
 Elements
 match a corresponding field the
 Type
 defines.

#### See Also

[AdditionalResult.Elements](additionalresult-elements.html)

[AdditionalResult.IsAnyType](additionalresult-isanytype.html)

[AdditionalResult.Name](additionalresult-name.html)

[AdditionalResult.Type](additionalresult-type.html)

[AdditionalResult.UnmappedAdditionalResults](additionalresult-unmappedadditionalresults.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresult-checkedstate.html language=enus -->
## TOPIC 00290: AdditionalResult.CheckedState

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresult-checkedstate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresult-checkedstate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResult.CheckedState Data Type CheckedStates Use the following constants with this data type: CheckedState_Checked –(Value: 2) Specifies to log the additional result. CheckedState_Indeterminate –(Value: 3) Specifies to log the additional result for some but not all members of the Add

### AdditionalResult.CheckedState

#### Syntax

[AdditionalResult](additionalresult.html).CheckedState

#### Data Type

[CheckedStates](checkedstates.html)

Use the following constants with this data type:

- CheckedState_Checked 
 –(Value: 2) Specifies to log the additional result.
- CheckedState_Indeterminate 
 –(Value: 3) Specifies to log the additional result for some but not all members of the
 AdditionalResult.Elements 
 collection.
- CheckedState_Unchecked 
 –(Value: 1) Specifies not to log the additional result.

#### Purpose

Specifies to log the additional result. If the CheckedState property is
 CheckedState_Unchecked
 , TestStand does not log the additional result. The value of the CheckedState property reflects the CheckedState of the
 [AdditionalResult.Elements](additionalresult-elements.html)
 collection when the Elements collection is not empty. If all the Elements have the same CheckedState value, the CheckedState property uses the CheckedState value of the Elements. If all the Elements do not have the same CheckedState value, the value of the
 AdditionalResult.CheckedState
 property is
 CheckedState_Indeterminate
 .

Setting the CheckedState property value sets the CheckedState value of all Elements to the same value and updates the CheckedState value of the
 [AdditionalResult.ParentAdditionalResult](additionalresult-parentadditionalresult.html)
 property.

#### See Also

[AdditionalResult.Condition](additionalresult-condition.html)

[AdditionalResult.Elements](additionalresult-elements.html)

[AdditionalResult.ParentAdditionalResult](additionalresult-parentadditionalresult.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresult-condition.html language=enus -->
## TOPIC 00291: AdditionalResult.Condition

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresult-condition.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresult-condition.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResult.Condition Data Type String Purpose An expression that must be empty or evaluate to True to log the additional result. See Also AdditionalResult.CheckedState

### AdditionalResult.Condition

#### Syntax

[AdditionalResult](additionalresult.html).Condition

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

An expression that must be empty or evaluate to
 True
 to log the additional result.

#### See Also

[AdditionalResult.CheckedState](additionalresult-checkedstate.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresult-elements.html language=enus -->
## TOPIC 00292: AdditionalResult.Elements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresult-elements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresult-elements.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResult.Elements Data Type AdditionalResults Purpose If the AdditionalResult.IsAnyType property is False , this property is a collection of AdditionalResult objects that correspond to the fields of the type the AdditionalResult.Type property specifies. If the IsAnyType property is Tr

### AdditionalResult.Elements

#### Syntax

[AdditionalResult](additionalresult.html).Elements

#### Data Type

[AdditionalResults](additionalresults.html)

#### Purpose

If the
 [AdditionalResult.IsAnyType](additionalresult-isanytype.html)
 property is
 False
 , this property is a collection of
 [AdditionalResult](additionalresult.html)
 objects that correspond to the fields of the type the
 [AdditionalResult.Type](additionalresult-type.html)
 property specifies. If the
 IsAnyType
 property is
 True
 , this property is an empty collection.

#### Remarks

Setting the
 IsAnyType
 property or the
 Type
 property updates the members in the Elements collection.

#### See Also

[AdditionalResult](additionalresult.html)

[AdditionalResult.IsAnyType](additionalresult-isanytype.html)

[AdditionalResult.ParentAdditionalResult](additionalresult-parentadditionalresult.html)

[AdditionalResult.Type](additionalresult-type.html)

[AdditionalResults](additionalresults.html)

[PropertyObjectType](propertyobjecttype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresult-flags.html language=enus -->
## TOPIC 00293: AdditionalResult.Flags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresult-flags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresult-flags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResult.Flags Data Type Long Purpose Specifies the PropertyFlags TestStand sets when it logs the additional result. You can use any combination of the PropFlags_IncludeInReport , PropFlags_IsMeasurementValue , and PropFlags_IsLimit property flags. See Also PropertyFlags

### AdditionalResult.Flags

#### Syntax

[AdditionalResult](additionalresult.html).Flags

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the
 [PropertyFlags](propertyflags.html)
 TestStand sets when it logs the additional result. You can use any combination of the
 PropFlags_IncludeInReport
 ,
 PropFlags_IsMeasurementValue
 , and
 PropFlags_IsLimit
 property flags.

#### See Also

[PropertyFlags](propertyflags.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresult-isanytype.html language=enus -->
## TOPIC 00294: AdditionalResult.IsAnyType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresult-isanytype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresult-isanytype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResult.IsAnyType Data Type Boolean Purpose For a custom additional result, if this property is False , you can set the AdditionalResult.Type property to specify the type of the AdditionalResult.ValueToLog property. If this property is True , the ValueToLog property can be any type.

### AdditionalResult.IsAnyType

#### Syntax

[AdditionalResult](additionalresult.html).IsAnyType

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

For a custom additional result, if this property is
 False
 , you can set the
 [AdditionalResult.Type](additionalresult-type.html)
 property to specify the type of the
 [AdditionalResult.ValueToLog](additionalresult-valuetolog.html)
 property. If this property is
 True
 , the
 ValueToLog
 property can be any type. For a parameter additional result, this property is always
 False
 .

#### See Also

[AdditionalResult.Elements](additionalresult-elements.html)

[AdditionalResult.Type](additionalresult-type.html)

[AdditionalResult.ValueToLog](additionalresult-valuetolog.html)

[PropertyObjectType](propertyobjecttype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresult-kind.html language=enus -->
## TOPIC 00295: AdditionalResult.Kind

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresult-kind.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresult-kind.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResult.Kind Data Type AdditionalResultKinds Use the following constants with this data type: AdditionalResultKind_Call –(Value: 4) Specifies an additional result for a .NET call. AdditionalResultKind_Custom –(Value: 1) Specifies a custom additional result. AdditionalResultKind_InPar

### AdditionalResult.Kind

#### Syntax

[AdditionalResult](additionalresult.html).Kind

#### Data Type

[AdditionalResultKinds](additionalresultkinds.html)

Use the following constants with this data type:

- AdditionalResultKind_Call 
 –(Value: 4) Specifies an additional result for a .NET call.
- AdditionalResultKind_Custom 
 –(Value: 1) Specifies a custom additional result.
- AdditionalResultKind_InParameter 
 –(Value: 2) Specifies an additional result for the input value of a parameter.
- AdditionalResultKind_OutParameter 
 –(Value: 3) Specifies an additional result for the output value of a parameter.

#### Purpose

Returns the type of additional result for the object.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresult-name.html language=enus -->
## TOPIC 00296: AdditionalResult.Name

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresult-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresult-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResult.Name Data Type String Purpose An expression that evaluates to the name of the additional result. Remarks The name is usually a string literal or uses the ResStr expression function to specify a localized string.

### AdditionalResult.Name

#### Syntax

[AdditionalResult](additionalresult.html).Name

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

An expression that evaluates to the name of the additional result.

#### Remarks

The name is usually a string literal or uses the
 ResStr
 expression function to specify a localized string.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresult-parameterobject.html language=enus -->
## TOPIC 00297: AdditionalResult.ParameterObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresult-parameterobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresult-parameterobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResult.ParameterObject Data Type PropertyObject Purpose For a parameter additional result, this property returns the module parameter of which the additional result logs the value. This property returns NULL for a custom additional result. Remarks This property can specify a LabVIEW

### AdditionalResult.ParameterObject

#### Syntax

[AdditionalResult](additionalresult.html).ParameterObject

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

For a parameter additional result, this property returns the module parameter of which the additional result logs the value. This property returns
 NULL
 for a custom additional result.

#### Remarks

This property can specify a
 [LabVIEWParameter](labviewparameter.html)
 ,
 [LabVIEWParameterElement](labviewparameterelement.html)
 ,
 [CVIParameter](cviparameter.html)
 ,
 [DllParameter](dllparameter.html)
 ,
 [SequenceCallParameter](sequencecallparameter.html)
 ,
 [DotNetParameter](dotnetparameter.html)
 ,
 [DotNetCall](dotnetcall.html)
 , or
 [ActiveXParameter](activexparameter.html)
 object, depending on the step adapter and the location of the parameter in the hierarchy of module call parameters. A parameter object that is a
 CVIParameter
 or
 DllParameter
 object is also a
 [CommonCParameter](commoncparameter.html)
 object.

#### See Also

[ActiveXParameter](activexparameter.html)

[CommonCParameter](commoncparameter.html)

[CVIParameter](cviparameter.html)

[DllParameter](dllparameter.html)

[DotNetCall](dotnetcall.html)

[DotNetParameter](dotnetparameter.html)

[LabVIEWParameter](labviewparameter.html)

[LabVIEWParameterElement](labviewparameterelement.html)

[SequenceCallParameter](sequencecallparameter.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresult-parentadditionalresult.html language=enus -->
## TOPIC 00298: AdditionalResult.ParentAdditionalResult

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresult-parentadditionalresult.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresult-parentadditionalresult.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResult.ParentAdditionalResult Data Type AdditionalResult Purpose If this property is not NULL , this property returns the AdditionalResult with an AdditionalResult.Elements collection that contains this AdditionalResult. See Also AdditionalResult AdditionalResult.Elements

### AdditionalResult.ParentAdditionalResult

#### Syntax

[AdditionalResult](additionalresult.html).ParentAdditionalResult

#### Data Type

[AdditionalResult](additionalresult.html)

#### Purpose

If this property is not
 NULL
 , this property returns the AdditionalResult with an
 [AdditionalResult.Elements](additionalresult-elements.html)
 collection that contains this AdditionalResult.

#### See Also

[AdditionalResult](additionalresult.html)

[AdditionalResult.Elements](additionalresult-elements.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresult-type.html language=enus -->
## TOPIC 00299: AdditionalResult.Type

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresult-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresult-type.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResult.Type Data Type PropertyObjectType Purpose For a custom additional result, if the AdditionalResult.IsAnyType property is True , this property returns the type of the AdditionalResult.ValueToLog property. If the AdditionalResult.IsAnyType property is False , set this property t

### AdditionalResult.Type

#### Syntax

[AdditionalResult](additionalresult.html).Type

#### Data Type

[PropertyObjectType](propertyobjecttype.html)

#### Purpose

For a custom additional result, if the
 [AdditionalResult.IsAnyType](additionalresult-isanytype.html)
 property is
 True
 , this property returns the type of the
 [AdditionalResult.ValueToLog](additionalresult-valuetolog.html)
 property. If the
 AdditionalResult.IsAnyType
 property is
 False
 , set this property to a
 [PropertyObjectType](propertyobjecttype.html)
 object to specify the type of the
 AdditionalResult.ValueToLog
 property. Use the
 [PropertyObject.Type](propertyobject-type.html)
 property or the
 [Engine.NewPropertyObjectType](engine-newpropertyobjecttype.html)
 method to obtain a
 PropertyObjectType
 object to set this property to. For a parameter additional result, this property returns the type the parameter specifies.

#### Remarks

For a custom additional result, when the
 AdditionalResult.IsAnyType
 property is
 True
 , this property is
 NULL
 if the
 AdditionalResult.ValueToLog
 property is empty or contains an error. When the
 AdditionalResult.IsAnyType
 property is
 False
 , this property is the value you last set the property to.

Setting the
 [AdditionalResult.Type](additionalresult-type.html)
 property updates the members in the
 [AdditionalResult.Elements](additionalresult-elements.html)
 collection and maps existing settings from the old Elements collection to the new Elements collection based on the
 [AdditionalResult.Name](additionalresult-name.html)
 and
 Type
 properties of the members. TestStand adds Elements from the old collection that do not map to Elements in the new collection to the
 [UnmappedAdditionalResults](additionalresult-unmappedadditionalresults.html)
 collection.

#### See Also

[AdditionalResult.Elements](additionalresult-elements.html)

[AdditionalResult.IsAnyType](additionalresult-isanytype.html)

[AdditionalResult.Name](additionalresult-name.html)

[AdditionalResult.Type](additionalresult-type.html)

[AdditionalResult.UnmappedAdditionalResults](additionalresult-unmappedadditionalresults.html)

[AdditionalResult.ValueToLog](additionalresult-valuetolog.html)

[PropertyObjectType](propertyobjecttype.html)

[PropertyObject.Type](propertyobject-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresult-unmappedadditionalresults.html language=enus -->
## TOPIC 00300: AdditionalResult.UnmappedAdditionalResults

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresult-unmappedadditionalresults.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresult-unmappedadditionalresults.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResult.UnmappedAdditionalResults Data Type AdditionalResults Purpose A collection of AdditionalResult objects from an AdditionalResult.Elements collection that TestStand could not map to an updated Elements collection when you set the AdditionalResult.Type property. TestStand does n

### AdditionalResult.UnmappedAdditionalResults

#### Syntax

[AdditionalResult](additionalresult.html).UnmappedAdditionalResults

#### Data Type

[AdditionalResults](additionalresults.html)

#### Purpose

A collection of
 [AdditionalResult](additionalresult.html)
 objects from an
 [AdditionalResult.Elements](additionalresult-elements.html)
 collection that TestStand could not map to an updated
 Elements
 collection when you set the
 [AdditionalResult.Type](additionalresult-type.html)
 property. TestStand does not record the
 AdditionalResult
 objects in this collection.

#### See Also

[AdditionalResult](additionalresult.html)

[AdditionalResult.AreElementsIncompatibleWithType](additionalresult-areelementsincompatiblewitht.html)

[AdditionalResult.Elements](additionalresult-elements.html)

[AdditionalResult.Type](additionalresult-type.html)

[AdditionalResults](additionalresults.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresult-valuetolog.html language=enus -->
## TOPIC 00301: AdditionalResult.ValueToLog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresult-valuetolog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresult-valuetolog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResult.ValueToLog Data Type String Purpose An expression that specifies the value to log for the additional result.

### AdditionalResult.ValueToLog

#### Syntax

[AdditionalResult](additionalresult.html).ValueToLog

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

An expression that specifies the value to log for the additional result.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresult.html language=enus -->
## TOPIC 00302: AdditionalResult

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresult.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresult.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: An AdditionalResult specifies additional data to add to the result list when a step executes. An AdditionalResult can be an arbitrary piece of data or the value of a module parameter. An AdditionalResult is a member of the Step.AdditionalResults.ParameterResults collection, the Step.AdditionalResult

### AdditionalResult

An AdditionalResult specifies additional data to add to the result list when a step executes. An AdditionalResult can be an arbitrary piece of data or the value of a module parameter. An AdditionalResult is a member of the
 Step.AdditionalResults.ParameterResults
 collection, the
 Step.AdditionalResults.CustomResults
 collection, or the
 AdditionalResult.Elements
 collection.

#### Properties

| AreElementsIncompatibleWithType (Read Only) |
| --- |
| CheckedState |
| Condition |
| Elements (Read Only) |
| Flags |
| IsAnyType |
| Kind (Read Only) |
| Name |
| ParameterObject (Read Only) |
| ParentAdditionalResult (Read Only) |
| Type |
| UnmappedAdditionalResults (Read Only) |
| ValueToLog |

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresultkinds.html language=enus -->
## TOPIC 00303: AdditionalResultKinds

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresultkinds.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresultkinds.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the AdditionalResult.Kind property. AdditionalResultKind_Call –(Value: 4) Specifies an additional result for a .NET call. AdditionalResultKind_Custom –(Value: 1) Specifies a custom additional result. AdditionalResultKind_InParameter –(Value: 2) Specifies an additional result

### AdditionalResultKinds

Use these constants with the
 [AdditionalResult.Kind](additionalresult-kind.html)
 property.

- AdditionalResultKind_Call 
 –(Value: 4) Specifies an additional result for a .NET call.
- AdditionalResultKind_Custom 
 –(Value: 1) Specifies a custom additional result.
- AdditionalResultKind_InParameter 
 –(Value: 2) Specifies an additional result for the input value of a parameter.
- AdditionalResultKind_OutParameter 
 –(Value: 3) Specifies an additional result for the output value of a parameter.

#### See Also

[AdditionalResult.Kind](additionalresult-kind.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresults-checkeditemcount.html language=enus -->
## TOPIC 00304: AdditionalResults.CheckedItemCount

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresults-checkeditemcount.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresults-checkeditemcount.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResults.CheckedItemCount Data Type Long Purpose Returns the number of items in the collection with an AdditionalResult.CheckedState property of CheckedState_Checked or CheckedState_Indeterminate . See Also AdditionalResult.CheckedState AdditionalResults.Count CheckedStates

### AdditionalResults.CheckedItemCount

#### Syntax

[AdditionalResults](additionalresults.html).CheckedItemCount

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection with an
 [AdditionalResult.CheckedState](additionalresult-checkedstate.html)
 property of
 [CheckedState_Checked](checkedstates.html)
 or
 [CheckedState_Indeterminate](checkedstates.html)
 .

#### See Also

[AdditionalResult.CheckedState](additionalresult-checkedstate.html)

[AdditionalResults.Count](additionalresults-count.html)

[CheckedStates](checkedstates.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresults-clear.html language=enus -->
## TOPIC 00305: AdditionalResults.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresults-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresults-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResults.Clear Purpose Removes all the additional results from the collection. See Also AdditionalResults.Remove

### AdditionalResults.Clear

#### Syntax

[AdditionalResults](additionalresults.html).Clear

#### Purpose

Removes all the additional results from the collection.

#### See Also

[AdditionalResults.Remove](additionalresults-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresults-count.html language=enus -->
## TOPIC 00306: AdditionalResults.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresults-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresults-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResults.Count Data Type Long Purpose Returns the number of items in the collection. See Also AdditionalResults.CheckedItemCount

### AdditionalResults.Count

#### Syntax

[AdditionalResults](additionalresults.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[AdditionalResults.CheckedItemCount](additionalresults-checkeditemcount.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresults-insert.html language=enus -->
## TOPIC 00307: AdditionalResults.Insert

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresults-insert.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresults-insert.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResults.Insert( resultName = "", resultValueToLog = "", resultCondition = "", resultFlags = PropFlags_IncludeInReport, index = -1) Return Value AdditionalResult The additional result this method inserts into the collection. Purpose Adds a new item to the collection. Parameters resul

### AdditionalResults.Insert

#### Syntax

[AdditionalResults](additionalresults.html).Insert( resultName = "", resultValueToLog = "", resultCondition = "", resultFlags = PropFlags_IncludeInReport, index = -1)

#### Return Value

[AdditionalResult](additionalresult.html)

The additional result this method inserts into the collection.

#### Purpose

Adds a new item to the collection.

#### Parameters

resultName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the
 [AdditionalResult.Name](additionalresult-name.html)
 property of the new additional result.

This parameter has a default value of
 ""
 .

resultValueToLog
 As
 [String](data-types-for-teststand.html)

[In] Specifies the
 [AdditionalResult.ValueToLog](additionalresult-valuetolog.html)
 property for the new additional result.

This parameter has a default value of
 ""
 .

resultCondition
 As
 [String](data-types-for-teststand.html)

[In] Specifies the
 [AdditionalResult.Condition](additionalresult-condition.html)
 property of the new additional result.

This parameter has a default value of
 ""
 .

resultFlags
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the
 [AdditionalResult.Flags](additionalresult-flags.html)
 property of the new additional result.

This parameter has a default value of
 PropFlags_IncludeInReport
 .

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies where to insert the new item. Pass
 -1
 to insert the item at the end

of the collection.

This parameter has a default value of
 -1
 .

#### See Also

[AdditionalResult](additionalresult.html)

[AdditionalResult.Condition](additionalresult-condition.html)

[AdditionalResult.Flags](additionalresult-flags.html)

[AdditionalResult.Name](additionalresult-name.html)

[AdditionalResult.ValueToLog](additionalresult-valuetolog.html)

[AdditionalResults.Move](additionalresults-move.html)

[AdditionalResults.Remove](additionalresults-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresults-item.html language=enus -->
## TOPIC 00308: AdditionalResults.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresults-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresults-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResults.Item( index) Data Type AdditionalResult Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the item to retrieve. See Also AdditionalResult

### AdditionalResults.Item

#### Syntax

[AdditionalResults](additionalresults.html).Item( index)

#### Data Type

[AdditionalResult](additionalresult.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve.

#### See Also

[AdditionalResult](additionalresult.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresults-move.html language=enus -->
## TOPIC 00309: AdditionalResults.Move

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresults-move.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresults-move.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResults.Move( index, newIndex) Purpose Moves an additional result within the collection. Parameters index As Long [In] Specifies the zero-based index of the item to move. newIndex As Long [In] Specifies the zero-based index to move the item to. See Also AdditionalResults.Insert Addi

### AdditionalResults.Move

#### Syntax

[AdditionalResults](additionalresults.html).Move( index, newIndex)

#### Purpose

Moves an additional result within the collection.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to move.

newIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index to move the item to.

#### See Also

[AdditionalResults.Insert](additionalresults-insert.html)

[AdditionalResults.Remove](additionalresults-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresults-remove.html language=enus -->
## TOPIC 00310: AdditionalResults.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresults-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresults-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdditionalResults.Remove( index) Return Value AdditionalResult The additional result this method removes from the collection. Purpose Removes the specified item from this collection, if it exists. Parameters index As Long [In] Specifies the zero-based index of the item to remove. See Also Add

### AdditionalResults.Remove

#### Syntax

[AdditionalResults](additionalresults.html).Remove( index)

#### Return Value

[AdditionalResult](additionalresult.html)

The additional result this method removes from the collection.

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to remove.

#### See Also

[AdditionalResult](additionalresult.html)

[AdditionalResults.Clear](additionalresults-clear.html)

[AdditionalResults.Insert](additionalresults-insert.html)

[AdditionalResults.Move](additionalresults-move.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/additionalresults.html language=enus -->
## TOPIC 00311: AdditionalResults

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/additionalresults.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/additionalresults.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This class represents a collection of AdditionalResult objects. Use the Step.AdditionalResults.ParameterResults , Step.AdditionalResults.CustomResults , or AdditionalResult.Elements properties to obtain an AdditionalResults collection. Properties CheckedItemCount (Read Only) Count (Read Only) Item (

### AdditionalResults

This class represents a collection of
 [AdditionalResult](additionalresult.html)
 objects. Use the
 Step.AdditionalResults.ParameterResults
 ,
 Step.AdditionalResults.CustomResults
 , or
 AdditionalResult.Elements
 properties to obtain an AdditionalResults collection.

#### Properties

| CheckedItemCount (Read Only) |
| --- |
| Count (Read Only) |
| Item (Read Only) |

#### Methods

| Clear |
| --- |
| Insert |
| Move |
| Remove |

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/allowautomatictypeconflictresolutionoptions.html language=enus -->
## TOPIC 00312: AllowAutomaticTypeConflictResolutionOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/allowautomatictypeconflictresolutionoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/allowautomatictypeconflictresolutionoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these options with the StationOptions.AllowAutomaticTypeConflictResolution property. AllowAutomaticTypeConflictResolutionOption_Always –(Value: 0) Always allows automatic type conflict resolution, which can cause unintended propagation of types between files. For example, if you open a sequence

### AllowAutomaticTypeConflictResolutionOptions

Use these options with the
 [StationOptions.AllowAutomaticTypeConflictResolution](stationoptions-allowautomatictypeconflictreso.html)
 property.

- AllowAutomaticTypeConflictResolutionOption_Always 
 –(Value: 0) Always allows automatic type conflict resolution, which can cause unintended propagation of types between files. For example, if you open a sequence file with a version of a type that is higher than the version of the type currently in a type palette file, TestStand updates the type palette file and every file you subsequently open to use the higher version. The updated type propagates to other files without warning or notifying you. This behavior is the default behavior in TestStand 4.0.
 x 
 or earlier.
- AllowAutomaticTypeConflictResolutionOption_Never 
 –(Value: 3) Disallows all automatic type conflict resolution. When TestStand loads two different versions of a type, TestStand always prompts you or reports a type conflict error. When you select this option, opening files from TestStand versions earlier than the current version almost always results in type conflict prompts. Use this option only for debugging purposes or to ensure that all files have exactly the same version of every type.
- AllowAutomaticTypeConflictResolutionOption_OnlyIfATypePaletteFileHasTheHigherVersion 
 –(Value: 2) Includes the same restrictions as the Only if Type Palette Files will not be Modified (default) option, but also includes the restriction that the type must be in a type palette file for automatic type conflict resolution to occur. Effectively, this option allows automatic type conflict resolution only when a type palette file has the higher version of the type and a non-type palette file has the lower version of the type.

For example, this option does not allow automatic type conflict resolution between two sequence files for types that are not in type palette files, but the Only if Type Palette Files will not be Modified (default) option does allow this.
- AllowAutomaticTypeConflictResolutionOption_OnlyIfTypePaletteFilesWillNotBeModified 
 –(Value: 1) Disallows automatic type conflict resolution when the outcome of the resolution modifies a type palette file. This ensures that the application never uses a version of a type that is different than the version of the type in the type palette file without your explicit confirmation. This is the default behavior.

#### See Also

[StationOptions.AllowAutomaticTypeConflictResolution](stationoptions-allowautomatictypeconflictreso.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/api-classes-properties-and-methods.html language=enus -->
## TOPIC 00313: API Classes, Properties, and Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/api-classes-properties-and-methods.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/api-classes-properties-and-methods.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains detailed information about each class, property, and method of the TestStand API.

### API Classes, Properties, and Methods

This book contains detailed information about each class, property, and method of the TestStand API.

Parent topic:

TestStand API

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/api-constants.html language=enus -->
## TOPIC 00314: API Constants

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/api-constants.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/api-constants.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains information about the TestStand API constants.

### API Constants

This book contains information about the TestStand API constants.

Parent topic:

TestStand API

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/api-enumerations.html language=enus -->
## TOPIC 00315: API Enumerations

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/api-enumerations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/api-enumerations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains information about the TestStand API enumerations.

### API Enumerations

This book contains information about the TestStand API enumerations.

Parent topic:

TestStand API

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/apilocations.html language=enus -->
## TOPIC 00316: APILocations

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/apilocations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/apilocations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this enumeration with the Locations.AddAPILocation , AnalysisUtilities.ValidateExpression , AnalysisUtilities.ValidatePath , or AnalysisUtilities.ValidateRemoteHost methods to refer to a Location when using an API property or method. The syntax of the enumeration is APILocation_BaseClassName_API

### APILocations

Use this enumeration with the
 [Locations.AddAPILocation](locations-addapilocation.html)
 ,
 
 [AnalysisUtilities.ValidateExpression](../tsanalyzer/analysisutilities-validateexpression.html)
 ,
 
 [AnalysisUtilities.ValidatePath](../tsanalyzer/analysisutilities-validatepath.html)
 , or
 
 [AnalysisUtilities.ValidateRemoteHost](../tsanalyzer/analysisutilities-validateremotehost.html)
 methods to refer to a Location when using an API property or method. The syntax of the enumeration is
 APILocation_BaseClassName_APIPropertyOrMethodName
 . For example,
 APILocation_ActiveXModule_ActiveXReferenceExpr
 refers to the
 ActiveXModule.ActiveXReferenceExpr
 property.

- APILocation_ActiveXModule_ActiveXReferenceExpr 
 –(Value: 65)
- APILocation_ActiveXModule_FilePath 
 –(Value: 66)
- APILocation_ActiveXModule_RemoteHost 
 –(Value: 67)
- APILocation_ActiveXParameter_ValueExpr 
 –(Value: 68)
- APILocation_AdditionalResult_Condition 
 –(Value: 57)
- APILocation_AdditionalResult_Name 
 –(Value: 58)
- APILocation_AdditionalResult_ValueToLog 
 –(Value: 59)
- APILocation_CommonCModule_ModulePath 
 –(Value: 51)
- APILocation_CommonCModule_ProjectFilePath 
 –(Value: 52)
- APILocation_CommonCModule_SourceFilePath 
 –(Value: 53)
- APILocation_CommonCModule_WorkspaceFilePath 
 –(Value: 54)
- APILocation_CommonCParameter_StringBufferSizeExpr 
 –(Value: 56)
- APILocation_CommonCParameter_ValueExpr 
 –(Value: 55)
- APILocation_DllParameter_ImaginaryPartValueExpr 
 –(Value: 124)
- APILocation_DotNetModule_GetAssembly 
 –(Value: 63)
- APILocation_DotNetModule_ProjectFilePath 
 –(Value: 60)
- APILocation_DotNetModule_SolutionFilePath 
 –(Value: 61)
- APILocation_DotNetModule_SourceFilePath 
 –(Value: 62)
- APILocation_DotNetParameter_ParameterName 
 –(Value: 127)
- APILocation_DotNetParameter_ValueExpr 
 –(Value: 64)
- APILocation_HTBasicModule_SubroutineFilePath 
 –(Value: 70)
- APILocation_LabVIEWModule_CallName 
 –(Value: 130)
- APILocation_LabVIEWModule_ClassPath 
 –(Value: 129)
- APILocation_LabVIEWModule_GetVIAbsolutePath 
 –(Value: 48)
- APILocation_LabVIEWModule_NodeLibraryName 
 –(Value: 133)
- APILocation_LabVIEWModule_OverrideBinaryClassPath 
 –(Value: 154)
- APILocation_LabVIEWModule_OverrideBinaryProjectPath 
 –(Value: 152)
- APILocation_LabVIEWModule_OverrideBinaryVIPath 
 –(Value: 153)
- APILocation_LabVIEWModule_OverrideSourceClassPath 
 –(Value: 143)
- APILocation_LabVIEWModule_OverrideSourceProjectPath 
 –(Value: 141)
- APILocation_LabVIEWModule_OverrideSourceVIPath 
 –(Value: 142)
- APILocation_LabVIEWModule_ProjectPath 
 –(Value: 47)
- APILocation_LabVIEWModule_RemoteConnectionTimeout 
 –(Value: 46)
- APILocation_LabVIEWModule_RemoteHost 
 –(Value: 44)
- APILocation_LabVIEWModule_RemotePortNumber 
 –(Value: 45)
- APILocation_LabVIEWModule_VIPath 
 –(Value: 42)
- APILocation_LabVIEWModule_VIType 
 –(Value: 43)
- APILocation_LabVIEWNXGModule_GllPath 
 –(Value: 135)
- APILocation_LabVIEWNXGModule_ModuleQualifiedName 
 –(Value: 139)
- APILocation_LabVIEWNXGModule_ProjectPath 
 –(Value: 134)
- APILocation_LabVIEWNXGModule_QualifiedName 
 –(Value: 136)
- APILocation_LabVIEWNXGParameter_ParameterLabel 
 –(Value: 137)
- APILocation_LabVIEWNXGParameter_Type 
 –(Value: 140)
- APILocation_LabVIEWNXGParameter_ValueExpression 
 –(Value: 138)
- APILocation_LabVIEWParameter_ParameterCaption 
 –(Value: 126)
- APILocation_LabVIEWParameter_ValueExpr 
 –(Value: 49)
- APILocation_LabVIEWParameterElement_ElementCaption 
 –(Value: 125)
- APILocation_LabVIEWParameterElement_ValueExpr 
 –(Value: 50)
- APILocation_None 
 –(Value: 0) Use this value to refer to a location that is not associated with an API property or method.
- APILocation_PythonModule_ClassInstanceLocationExpr 
 –(Value: 150)
- APILocation_PythonModule_ClassName 
 –(Value: 148)
- APILocation_PythonModule_FunctionOrAttributeName 
 –(Value: 149)
- APILocation_PythonModule_InterpreterReferenceExpr 
 –(Value: 147)
- APILocation_PythonModule_ModulePath 
 –(Value: 145)
- APILocation_PythonModule_PythonVersion 
 –(Value: 144)
- APILocation_PythonModule_PythonVirtualEnvironmentPath 
 –(Value: 146)
- APILocation_PythonParameter_ValueExpr 
 –(Value: 151)
- APILocation_Sequence_DisableResults 
 –(Value: 128)
- APILocation_SequenceCallModule_CustomCPUAffinityForNewThread 
 –(Value: 71)
- APILocation_SequenceCallModule_NewExecutionBreakOnEntryExpr 
 –(Value: 72)
- APILocation_SequenceCallModule_NewExecutionModelPath 
 –(Value: 73)
- APILocation_SequenceCallModule_NewExecutionTypeMaskExpr 
 –(Value: 74)
- APILocation_SequenceCallModule_RemoteHost 
 –(Value: 75)
- APILocation_SequenceCallModule_SequenceFilePath 
 –(Value: 76)
- APILocation_SequenceCallModule_SequenceName 
 –(Value: 77)
- APILocation_SequenceCallModule_StoreActiveXReferenceExpr 
 –(Value: 78)
- APILocation_SequenceCallParameter_ValueExpr 
 –(Value: 79)
- APILocation_SequenceFile_ModelPath 
 –(Value: 123)
- APILocation_Step_BatchSyncOption 
 –(Value: 1)
- APILocation_Step_CustomActionExpression 
 –(Value: 2)
- APILocation_Step_CustomFalseAction 
 –(Value: 3)
- APILocation_Step_CustomFalseActionTargetByExpr 
 –(Value: 4)
- APILocation_Step_CustomTrueAction 
 –(Value: 5)
- APILocation_Step_CustomTrueActionTargetByExpr 
 –(Value: 6)
- APILocation_Step_EvalPrecondForInteractiveExecution 
 –(Value: 7)
- APILocation_Step_FailAction 
 –(Value: 8)
- APILocation_Step_FailActionTargetByExpr 
 –(Value: 9)
- APILocation_Step_IconName 
 –(Value: 10)
- APILocation_Step_IgnoreRTE 
 –(Value: 11)
- APILocation_Step_LoopIncExpression 
 –(Value: 12)
- APILocation_Step_LoopInitExpression 
 –(Value: 13)
- APILocation_Step_LoopStatusExpression 
 –(Value: 14)
- APILocation_Step_LoopType 
 –(Value: 15)
- APILocation_Step_LoopWhileExpression 
 –(Value: 16)
- APILocation_Step_ModuleLoadOption 
 –(Value: 17)
- APILocation_Step_ModuleUnloadOption 
 –(Value: 18)
- APILocation_Step_MutexNameOrRefExpr 
 –(Value: 19)
- APILocation_Step_PassAction 
 –(Value: 20)
- APILocation_Step_PassActionTargetByExpr 
 –(Value: 21)
- APILocation_Step_PostExpression 
 –(Value: 22)
- APILocation_Step_Precondition 
 –(Value: 23)
- APILocation_Step_PreExpression 
 –(Value: 24)
- APILocation_Step_RecordLoopIterationResults 
 –(Value: 25)
- APILocation_Step_RecordResult 
 –(Value: 26)
- APILocation_Step_ResultRecordingOption 
 –(Value: 131)
- APILocation_Step_RunMode 
 –(Value: 27)
- APILocation_Step_StatusExpression 
 –(Value: 28)
- APILocation_Step_StepFailCausesSequenceFail 
 –(Value: 29)
- APILocation_Step_SwitchExecConnectionLifetime 
 –(Value: 30)
- APILocation_Step_SwitchExecEnabled 
 –(Value: 31)
- APILocation_Step_SwitchExecMulticonnectMode 
 –(Value: 32)
- APILocation_Step_SwitchExecOperation 
 –(Value: 33)
- APILocation_Step_SwitchExecOperationOrder 
 –(Value: 34)
- APILocation_Step_SwitchExecRoutesToConnect 
 –(Value: 35)
- APILocation_Step_SwitchExecRoutesToDisconnect 
 –(Value: 36)
- APILocation_Step_SwitchExecVirtualDevice 
 –(Value: 37)
- APILocation_Step_SwitchExecWaitForDebounce 
 –(Value: 38)
- APILocation_Step_UniqueStepId 
 –(Value: 39)
- APILocation_Step_UseMutex 
 –(Value: 40)
- APILocation_Step_WindowActivation 
 –(Value: 41)
- APILocation_StepType_BatchSyncOption 
 –(Value: 108)
- APILocation_StepType_CustomActionExpression 
 –(Value: 95)
- APILocation_StepType_CustomFalseAction 
 –(Value: 97)
- APILocation_StepType_CustomFalseActionTargetByExpr 
 –(Value: 99)
- APILocation_StepType_CustomTrueAction 
 –(Value: 96)
- APILocation_StepType_CustomTrueActionTargetByExpr 
 –(Value: 98)
- APILocation_StepType_DefaultNameExpr 
 –(Value: 113)
- APILocation_StepType_DescriptionExpr 
 –(Value: 114)
- APILocation_StepType_EvalPrecondForInteractiveExecution 
 –(Value: 83)
- APILocation_StepType_FailAction 
 –(Value: 92)
- APILocation_StepType_FailActionTargetByExpr 
 –(Value: 94)
- APILocation_StepType_IconName 
 –(Value: 80)
- APILocation_StepType_IgnoreRTE 
 –(Value: 116)
- APILocation_StepType_LoopIncExpression 
 –(Value: 87)
- APILocation_StepType_LoopInitExpression 
 –(Value: 86)
- APILocation_StepType_LoopStatusExpression 
 –(Value: 89)
- APILocation_StepType_LoopType 
 –(Value: 90)
- APILocation_StepType_LoopWhileExpression 
 –(Value: 88)
- APILocation_StepType_MenuItemNameExpr 
 –(Value: 115)
- APILocation_StepType_ModuleLoadOption 
 –(Value: 81)
- APILocation_StepType_ModuleUnloadOption 
 –(Value: 82)
- APILocation_StepType_MutexNameOrRefExpr 
 –(Value: 107)
- APILocation_StepType_PassAction 
 –(Value: 91)
- APILocation_StepType_PassActionTargetByExpr 
 –(Value: 93)
- APILocation_StepType_PostExpression 
 –(Value: 110)
- APILocation_StepType_Precondition 
 –(Value: 112)
- APILocation_StepType_PreExpression 
 –(Value: 109)
- APILocation_StepType_RecordLoopIterationResults 
 –(Value: 117)
- APILocation_StepType_RecordResult 
 –(Value: 118)
- APILocation_StepType_ResultRecordingOption 
 –(Value: 132)
- APILocation_StepType_RunMode 
 –(Value: 85)
- APILocation_StepType_StatusExpression 
 –(Value: 111)
- APILocation_StepType_StepFailCausesSequenceFail 
 –(Value: 119)
- APILocation_StepType_SwitchExecConnectionLifetime 
 –(Value: 104)
- APILocation_StepType_SwitchExecEnabled 
 –(Value: 120)
- APILocation_StepType_SwitchExecMulticonnectMode 
 –(Value: 103)
- APILocation_StepType_SwitchExecOperation 
 –(Value: 101)
- APILocation_StepType_SwitchExecOperationOrder 
 –(Value: 106)
- APILocation_StepType_SwitchExecRoutesToConnect 
 –(Value: 102)
- APILocation_StepType_SwitchExecRoutesToDisconnect 
 –(Value: 105)
- APILocation_StepType_SwitchExecVirtualDevice 
 –(Value: 100)
- APILocation_StepType_SwitchExecWaitForDebounce 
 –(Value: 121)
- APILocation_StepType_UseMutex 
 –(Value: 122)
- APILocation_StepType_WindowActivation 
 –(Value: 84)

#### See Also

[AnalysisUtilities.ValidateExpression](../tsanalyzer/analysisutilities-validateexpression.html)

[AnalysisUtilities.ValidatePath](../tsanalyzer/analysisutilities-validatepath.html)

[AnalysisUtilities.ValidateRemoteHost](../tsanalyzer/analysisutilities-validateremotehost.html)

[Locations.AddAPILocation](locations-addapilocation.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/applicationlicenses.html language=enus -->
## TOPIC 00317: ApplicationLicenses

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/applicationlicenses.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/applicationlicenses.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify a type of license the application requires. Use these constants with the licenses parameter of the Engine.AcquireLicense method. ApplicationLicense_CustomEditor –(Value: 200) Specifies that the application requires a license to perform custom editor operations, such as

### ApplicationLicenses

Use these constants to specify a type of
 
 [license](/csh?context=ts_9050)
 the application requires. Use these constants with the
 licenses
 parameter of the
 [Engine.AcquireLicense](engine-acquirelicense.html)
 method.

- ApplicationLicense_CustomEditor 
 –(Value: 200) Specifies that the application requires a license to perform custom editor operations, such as editing and saving sequence files.
- ApplicationLicense_OperatorInterface 
 –(Value: 100) Specifies that the application requires a license to perform non-editing operations.
- ApplicationLicense_SequenceEditor 
 –(Value: 300) Specifies that the application requires a license to use the TestStand Sequence Editor.
- ApplicationLicense_Unspecified 
 –(Value: 0) Specifies that the application license requirements are unspecified.

#### See Also

[Engine.AcquireLicense](engine-acquirelicense.html)

[TestStand Licensing Options](/csh?context=ts_9050)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/applicationsites.html language=enus -->
## TOPIC 00318: ApplicationSites

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/applicationsites.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/applicationsites.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify how to display a location a user interface can display in more than one place. Use these constants with the Locations.ApplicationSite property and the UndoItemCreator.CreateAndPostUndoItem method. ApplicationSite_DefaultSite –(Value: 0) Specifies that the user interfac

### ApplicationSites

Use these constants to specify how to display a location a user interface can display in more than one place. Use these constants with the
 [Locations.ApplicationSite](locations-applicationsite.html)
 property and the
 [UndoItemCreator.CreateAndPostUndoItem](undoitemcreator-createandpostundoitem.html)
 method.

- ApplicationSite_DefaultSite 
 –(Value: 0) Specifies that the user interface determines where to display the location.
- ApplicationSite_ItemList 
 –(Value: 1) Specifies that the user interface displays the location in a list control, such as a list of steps or a list of sequences.
- ApplicationSite_PropertyBrowser 
 –(Value: 3) Specifies that the user interface displays the location in a control that displays a hierarchy of properties and subproperties.
- ApplicationSite_Settings 
 –(Value: 4) Specifies that the user interface displays the location in a settings panel or dialog.
- ApplicationSite_Variables 
 –(Value: 2) Specifies that the user interface displays the location in a variables control.

#### See Also

[Locations.ApplicationSite](locations-applicationsite.html)

[UndoItemCreator.CreateAndPostUndoItem](undoitemcreator-createandpostundoitem.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/arrayboundsdialogoptions.html language=enus -->
## TOPIC 00319: ArrayBoundsDialogOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/arrayboundsdialogoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/arrayboundsdialogoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the dlgOptions parameter of the PropertyObject.DisplayArrayBoundsDialog method. Use the bitwise-OR operator to specify more than one option. ArrayBounds_InitializeArray –(Value: 0x1) Initializes the array bounds to a default value ([0..9]) befor

### ArrayBoundsDialogOptions

These constants represent the options you can use with the
 dlgOptions
 parameter of the
 [PropertyObject.DisplayArrayBoundsDialog](propertyobject-displayarrayboundsdialog.html)
 method. Use the bitwise-OR operator to specify more than one option.

- ArrayBounds_InitializeArray 
 –(Value: 0x1) Initializes the array bounds to a default value ([0..9]) before launching the
 Array Bounds 
 dialog box.
- ArrayBounds_NoOptions 
 –(Value: 0x0) No options.
- ArrayBounds_ReturnOkCancel 
 –(Value: 0x2) Forces the dialog box to return
 True 
 if you click
 OK 
 and
 False 
 if you click
 Cancel 
 .

#### See Also

[Array Bounds dialog box](../tsref/array-bounds-dialog-box.html)

[PropertyObject.DisplayArrayBoundsDialog](propertyobject-displayarrayboundsdialog.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/arraydimensions-displaystring.html language=enus -->
## TOPIC 00320: ArrayDimensions.DisplayString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/arraydimensions-displaystring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/arraydimensions-displaystring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ArrayDimensions.DisplayString Data Type String Purpose Returns the upper and lower bounds of each array dimension. See Also ArrayDimensions.GetLowerBounds ArrayDimensions.GetUpperBounds ArrayDimensions.LowerBoundsString ArrayDimensions.UpperBoundsString

### ArrayDimensions.DisplayString

#### Syntax

[ArrayDimensions](arraydimensions.html).DisplayString

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the upper and lower bounds of each array dimension.

#### See Also

[ArrayDimensions.GetLowerBounds](arraydimensions-getlowerbounds.html)

[ArrayDimensions.GetUpperBounds](arraydimensions-getupperbounds.html)

[ArrayDimensions.LowerBoundsString](arraydimensions-lowerboundsstring.html)

[ArrayDimensions.UpperBoundsString](arraydimensions-upperboundsstring.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/arraydimensions-getdimensionssizes.html language=enus -->
## TOPIC 00321: ArrayDimensions.GetDimensionsSizes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/arraydimensions-getdimensionssizes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/arraydimensions-getdimensionssizes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ArrayDimensions.GetDimensionsSizes Return Value Long Array Purpose Returns an array of numbers that contains the size of each dimension in the array. Remarks For a PropertyObject that is an empty array, this method returns an array with an element for every dimension in the PropertyObject arr

### ArrayDimensions.GetDimensionsSizes

#### Syntax

[ArrayDimensions](arraydimensions.html).GetDimensionsSizes

#### Return Value

[Long Array](data-types-for-teststand.html)

#### Purpose

Returns an array of numbers that contains the size of each dimension in the array.

#### Remarks

For a
 [PropertyObject](propertyobject.html)
 that is an empty array, this method returns an array with an element for every dimension in the PropertyObject array. Each element in the array this method returns has a value of zero.

#### See Also

[ArrayDimensions.GetLowerBounds](arraydimensions-getlowerbounds.html)

[ArrayDimensions.GetUpperBounds](arraydimensions-getupperbounds.html)

[ArrayDimensions.SetBounds](arraydimensions-setbounds.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/arraydimensions-getlowerbounds.html language=enus -->
## TOPIC 00322: ArrayDimensions.GetLowerBounds

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/arraydimensions-getlowerbounds.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/arraydimensions-getlowerbounds.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ArrayDimensions.GetLowerBounds Return Value Long Array Purpose Returns an array of numbers that contains the lowest valid index for each dimension. Remarks For a PropertyObject that is an empty array, this method returns an array with an element for every dimension in the PropertyObject array

### ArrayDimensions.GetLowerBounds

#### Syntax

[ArrayDimensions](arraydimensions.html).GetLowerBounds

#### Return Value

[Long Array](data-types-for-teststand.html)

#### Purpose

Returns an array of numbers that contains the lowest valid index for each dimension.

#### Remarks

For a
 [PropertyObject](propertyobject.html)
 that is an empty array, this method returns an array with an element for every dimension in the PropertyObject array.

#### See Also

[ArrayDimensions.GetDimensionsSizes](arraydimensions-getdimensionssizes.html)

[ArrayDimensions.GetUpperBounds](arraydimensions-getupperbounds.html)

[ArrayDimensions.LowerBoundsString](arraydimensions-lowerboundsstring.html)

[ArrayDimensions.SetBounds](arraydimensions-setbounds.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/arraydimensions-getupperbounds.html language=enus -->
## TOPIC 00323: ArrayDimensions.GetUpperBounds

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/arraydimensions-getupperbounds.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/arraydimensions-getupperbounds.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ArrayDimensions.GetUpperBounds Return Value Long Array Purpose Returns an array of numbers that contains the highest valid index for each dimension. Remarks For a PropertyObject that is an empty array, this method returns an empty array. See Also ArrayDimensions.GetDimensionsSizes ArrayDimens

### ArrayDimensions.GetUpperBounds

#### Syntax

[ArrayDimensions](arraydimensions.html).GetUpperBounds

#### Return Value

[Long Array](data-types-for-teststand.html)

#### Purpose

Returns an array of numbers that contains the highest valid index for each dimension.

#### Remarks

For a
 [PropertyObject](propertyobject.html)
 that is an empty array, this method returns an empty array.

#### See Also

[ArrayDimensions.GetDimensionsSizes](arraydimensions-getdimensionssizes.html)

[ArrayDimensions.GetLowerBounds](arraydimensions-getlowerbounds.html)

[ArrayDimensions.SetBounds](arraydimensions-setbounds.html)

[ArrayDimensions.UpperBoundsString](arraydimensions-upperboundsstring.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/arraydimensions-lowerboundsstring.html language=enus -->
## TOPIC 00324: ArrayDimensions.LowerBoundsString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/arraydimensions-lowerboundsstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/arraydimensions-lowerboundsstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ArrayDimensions.LowerBoundsString Data Type String Purpose Returns an array index string that specifies the lowest valid index for each dimension. For example, a two-dimensional array with a lower bound of 0 for the first dimension and 2 for the second dimension has the lower bound string "[0

### ArrayDimensions.LowerBoundsString

#### Syntax

[ArrayDimensions](arraydimensions.html).LowerBoundsString

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns an array index string that specifies the lowest valid index for each dimension. For example, a two-dimensional array with a lower bound of
 0
 for the first dimension and
 2
 for the second dimension has the lower bound string
 "[0][2]"
 .

#### See Also

[ArrayDimensions.DisplayString](arraydimensions-displaystring.html)

[ArrayDimensions.GetLowerBounds](arraydimensions-getlowerbounds.html)

[ArrayDimensions.SetBoundsByStrings](arraydimensions-setboundsbystrings.html)

[ArrayDimensions.UpperBoundsString](arraydimensions-upperboundsstring.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/arraydimensions-numdimensions.html language=enus -->
## TOPIC 00325: ArrayDimensions.NumDimensions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/arraydimensions-numdimensions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/arraydimensions-numdimensions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ArrayDimensions.NumDimensions Data Type Long The number of dimensions in the array. Purpose Gets the number of dimensions in the array. See Also ArrayDimensions.GetDimensionSizes

### ArrayDimensions.NumDimensions

#### Syntax

[ArrayDimensions](arraydimensions.html).NumDimensions

#### Data Type

[Long](data-types-for-teststand.html)

The number of dimensions in the array.

#### Purpose

Gets the number of dimensions in the array.

#### See Also

ArrayDimensions.GetDimensionSizes

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/arraydimensions-setbounds.html language=enus -->
## TOPIC 00326: ArrayDimensions.SetBounds

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/arraydimensions-setbounds.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/arraydimensions-setbounds.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ArrayDimensions.SetBounds( lowerBounds, upperBounds) Purpose Sets the upper and lower bounds from number arrays for a PropertyObject that is an array. Remarks The elements in the array retain their values. Parameters lowerBounds As Long Array [In] An array of numbers that specifies the lowest

### ArrayDimensions.SetBounds

#### Syntax

[ArrayDimensions](arraydimensions.html).SetBounds( lowerBounds, upperBounds)

#### Purpose

Sets the upper and lower bounds from number arrays for a
 [PropertyObject](propertyobject.html)
 that is an array.

#### Remarks

The elements in the array retain their values.

#### Parameters

lowerBounds
 As
 [Long Array](data-types-for-teststand.html)

[In] An array of numbers that specifies the lowest valid index for each dimension.

upperBounds
 As
 [Long Array](data-types-for-teststand.html)

[In] An array of numbers that specifies the highest valid index for each dimension.

#### See Also

[ArrayDimensions.GetDimensionsSizes](arraydimensions-getdimensionssizes.html)

[ArrayDimensions.GetLowerBounds](arraydimensions-getlowerbounds.html)

[ArrayDimensions.GetUpperBounds](arraydimensions-getupperbounds.html)

[ArrayDimensions.SetBoundsByStrings](arraydimensions-setboundsbystrings.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/arraydimensions-setboundsbystrings.html language=enus -->
## TOPIC 00327: ArrayDimensions.SetBoundsByStrings

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/arraydimensions-setboundsbystrings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/arraydimensions-setboundsbystrings.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ArrayDimensions.SetBoundsByStrings( lowerBounds, upperBounds) Purpose Sets the upper and lower bounds from strings for a PropertyObject that is an array. Remarks The elements in the array retain their values. Parameters lowerBounds As String [In] An array index string that specifies the lowes

### ArrayDimensions.SetBoundsByStrings

#### Syntax

[ArrayDimensions](arraydimensions.html).SetBoundsByStrings( lowerBounds, upperBounds)

#### Purpose

Sets the upper and lower bounds from strings for a
 [PropertyObject](propertyobject.html)
 that is an array.

#### Remarks

The elements in the array retain their values.

#### Parameters

lowerBounds
 As
 [String](data-types-for-teststand.html)

[In] An array index string that specifies the lowest valid index for each dimension. For example, a two-dimensional array with a lower bound of
 0
 for the first dimension and
 2
 for the second dimension has the lower bound string
 "[0][2]"
 .

upperBounds
 As
 [String](data-types-for-teststand.html)

[In] An array index string that specifies the highest valid index for each dimension. For example, a two-dimensional array with an upper bound of
 2
 for the first dimension and
 4
 for the second dimension has the upper bound string
 "[2][4]"
 .

#### See Also

[ArrayDimensions.DisplayString](arraydimensions-displaystring.html)

[ArrayDimensions.LowerBoundsString](arraydimensions-lowerboundsstring.html)

[ArrayDimensions.SetBounds](arraydimensions-setbounds.html)

[ArrayDimensions.UpperBoundsString](arraydimensions-upperboundsstring.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/arraydimensions-upperboundsstring.html language=enus -->
## TOPIC 00328: ArrayDimensions.UpperBoundsString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/arraydimensions-upperboundsstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/arraydimensions-upperboundsstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ArrayDimensions.UpperBoundsString Data Type String Purpose Returns an array index string that specifies the highest valid index for each dimension. For example, a two-dimensional array with an upper bound of 2 for the first dimension and 4 for the second dimension has the upper bound string "

### ArrayDimensions.UpperBoundsString

#### Syntax

[ArrayDimensions](arraydimensions.html).UpperBoundsString

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns an array index string that specifies the highest valid index for each dimension. For example, a two-dimensional array with an upper bound of
 2
 for the first dimension and
 4
 for the second dimension has the upper bound string
 "[2][4]"
 .

#### See Also

[ArrayDimensions.DisplayString](arraydimensions-displaystring.html)

[ArrayDimensions.GetUpperBounds](arraydimensions-getupperbounds.html)

[ArrayDimensions.LowerBoundsString](arraydimensions-lowerboundsstring.html)

[ArrayDimensions.SetBoundsByStrings](arraydimensions-setboundsbystrings.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/arraydimensions.html language=enus -->
## TOPIC 00329: ArrayDimensions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/arraydimensions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/arraydimensions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the ArrayDimensions class to obtain and set array bounds information for a PropertyObject . Use the PropertyObjectType.ArrayDimensions property to obtain an instance of this class. Properties DisplayString (Read Only) LowerBoundsString (Read Only) UpperBoundsString (Read Only) Methods GetDimensi

### ArrayDimensions

Use the ArrayDimensions class to obtain and set array bounds information for a
 [PropertyObject](propertyobject.html)
 . Use the
 [PropertyObjectType.ArrayDimensions](propertyobjecttype-arraydimensions.html)
 property to obtain an instance of this class.

#### Properties

| DisplayString (Read Only) |
| --- |
| LowerBoundsString (Read Only) |
| UpperBoundsString (Read Only) |

#### Methods

| GetDimensionsSizes |
| --- |
| GetLowerBounds |
| GetUpperBounds |
| SetBounds |
| SetBoundsByStrings |

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/autocreatevariablelocationoptions.html language=enus -->
## TOPIC 00330: AutoCreateVariableLocationOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/autocreatevariablelocationoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/autocreatevariablelocationoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following constants with the StationOptions.AutoCreateVariableLocation property. AutoCreateVariableLocationOption_FileGlobals –(Value: 3) Use FileGlobals as the location. AutoCreateVariableLocationOption_Locals –(Value: 1) Use Locals as the location. AutoCreateVariableLocationOption_Paramete

### AutoCreateVariableLocationOptions

Use the following constants with the
 StationOptions.AutoCreateVariableLocation
 property.

- AutoCreateVariableLocationOption_FileGlobals 
 –(Value: 3) Use FileGlobals as the location.
- AutoCreateVariableLocationOption_Locals 
 –(Value: 1) Use Locals as the location.
- AutoCreateVariableLocationOption_Parameters 
 –(Value: 2) Use Parameters as the location.
- AutoCreateVariableLocationOption_StationGlobals 
 –(Value: 4) Use StationGlobals as the location.

#### See Also

[StationOptions.AutoCreateVariableLocation](stationoptions-autocreatevariablelocation.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/batchsynchronizationoptions.html language=enus -->
## TOPIC 00331: BatchSynchronizationOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/batchsynchronizationoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/batchsynchronizationoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the Step.BatchSyncOption and StepType.BatchSyncOption properties. BatchSyncOption_NoSync –(Value: 2) No batch synchronization is used on this step. BatchSyncOption_OneThreadOnly –(Value: 5) Use a One Thread Only section to specify that only one thread in the batch executes t

### BatchSynchronizationOptions

Use these constants with the
 [Step.BatchSyncOption](step-batchsyncoption.html)
 and
 [StepType.BatchSyncOption](steptype-batchsyncoption.html)
 properties.

- BatchSyncOption_NoSync 
 –(Value: 2) No batch synchronization is used on this step.
- BatchSyncOption_OneThreadOnly 
 –(Value: 5) Use a One Thread Only section to specify that only one thread in the batch executes the single step or the steps in the section. Typically, you use this type of section to perform an operation that applies to the batch as a whole, such as raising the temperature in a test chamber. When all threads in a batch arrive at their respective instances of the single step or an Enter step for a One Thread Only section, TestStand releases only the thread with the lowest order number. When that thread executes the single step or arrives at the Exit step for the section, all remaining threads in the batch skip the single step or jump from the Enter step to the Exit step, skipping steps within the section. The threads in the batch then continue and exit the section together.
- BatchSyncOption_Parallel 
 –(Value: 4) When all threads in the batch arrive at their respective instances of a single step or an Enter step for a Parallel section, TestStand releases all the threads at once. Each thread blocks after executing the single step or after reaching the Exit step for the section until all threads can continue and exit the section together.
- BatchSyncOption_Serial 
 –(Value: 3) Use a Serial section to ensure that each thread in the batch executes a single step sequentially or the steps in a section sequentially and in the order you specified when you created the batch. When all threads in a batch arrive at their respective instances of a single step or an Enter step for a Serial section, TestStand releases one thread at a time in ascending order according to the order number you assign to threads when you added them to the batch using the Batch Specification step type. As each thread executes the single step or reaches the Exit step for the section, the next thread in the batch executes the single step or proceeds from the Enter step. After all threads in the batch execute the single step or arrive at the Exit step, they continue and exit the section together.
- BatchSyncOption_UseModelSetting 
 –(Value: 1) Uses the same option the model is using.
- BatchSyncOption_UseSeqFileSetting 
 –(Value: 0) Uses the same option the sequence file is using.

#### See Also

[Step.BatchSyncOption](step-batchsyncoption.html)

[StepType.BatchSyncOption](steptype-batchsyncoption.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/blockflags.html language=enus -->
## TOPIC 00332: BlockFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/blockflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/blockflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Flags that indicate how a step affects the block structure of the sequence. BlockFlag_AppliesToBlockStructure –(Value: 32) The step defines or operates according to the block structure of the sequence. BlockFlag_Close –(Value: 2) The step closes a block. The step is not within the block. BlockFlag_E

### BlockFlags

Flags that indicate how a step affects the block structure of the sequence.

- BlockFlag_AppliesToBlockStructure 
 –(Value: 32) The step defines or operates according to the block structure of the sequence.
- BlockFlag_Close 
 –(Value: 2) The step closes a block. The step is not within the block.
- BlockFlag_End 
 –(Value: 8) The step is the last step within the block.
- BlockFlag_None 
 –(Value: 0) No BlockFlags are present.
- BlockFlag_Open 
 –(Value: 1) The step opens a block, matched or unmatched. The step is not within the block.
- BlockFlag_Start 
 –(Value: 4) The step is the first step within the block.
- BlockFlag_Unmatched 
 –(Value: 16) The step opens or closes a block, but the matching step does not exist.

#### See Also

[Step.BlockFlags](step-blockflags.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/browseexprdialogoptions.html language=enus -->
## TOPIC 00333: BrowseExprDialogOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/browseexprdialogoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/browseexprdialogoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the dlgOptions parameter of the Engine.DisplayBrowseExprDialogEx method and the ExpressionEdit.BrowseExprDialogOptions property. Use the bitwise-OR operator to specify more than one option. BrowseExpr_ForViewingTypes –(Value: 0x4) Use this optio

### BrowseExprDialogOptions

These constants represent the options you can use with the
 dlgOptions
 parameter of the
 [Engine.DisplayBrowseExprDialogEx](engine-displaybrowseexprdialogex.html)
 method and the
 
 [ExpressionEdit.BrowseExprDialogOptions](../tsuiref/expressionedit-browseexprdialogoptions.html)
 property. Use the bitwise-OR operator to specify more than one option.

- BrowseExpr_ForViewingTypes 
 –(Value: 0x4) Use this option to specify that the
 Expression Browser 
 dialog box show properties hidden in an instance of the type.
- BrowseExpr_ModalToAppMainWind 
 –(Value: 0x10000) By default, the dialog box is modal to the last active window of the calling thread, or if none exists, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle of the
 Engine.AppMainHwnd 
 property. Typically, you do not need to set this option.
- BrowseExpr_NoContextMenus 
 –(Value: 0x2) Use this option to disable the right-click context menus in the list control that allow users to insert, rename, and delete.
- BrowseExpr_NoOptions 
 –(Value: 0x0) No options.
- BrowseExpr_UsesCRLF 
 –(Value: 0x1) Use this option to specify that the initial expression string and the output expression string uses a carriage return/linefeed combination ("\r\n") instead of a simple linefeed ("\n") to indicate the end of a line of text. This option applies only to the
 Engine.DisplayBrowseExprDialogEx 
 method.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Engine.DisplayBrowseExprDialogEx](engine-displaybrowseexprdialogex.html)

[Expression Browser dialog box](../tsref/expression-browser-dialog-box.html)

[ExpressionEdit.BrowseExprDialogOptions](../tsuiref/expressionedit-browseexprdialogoptions.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/callbacktypes.html language=enus -->
## TOPIC 00334: CallbackTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/callbacktypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/callbacktypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the Execution.EnableCallback and Execution.IsCallbackEnabled methods to specify on which callback sequence to operate. CallbackType_ModelPostError –(Value: 0x0) ProcessModelPostError callback CallbackType_ModelPostFail –(Value: 0x1) ProcessModelPostFail callback CallbackType

### CallbackTypes

Use these constants with the
 [Execution.EnableCallback](execution-enablecallback.html)
 and
 [Execution.IsCallbackEnabled](execution-iscallbackenabled.html)
 methods to specify on which callback sequence to operate.

- CallbackType_ModelPostError 
 –(Value: 0x0) ProcessModelPostError callback
- CallbackType_ModelPostFail 
 –(Value: 0x1) ProcessModelPostFail callback
- CallbackType_ModelPostInteractive 
 –(Value: 0x2) ProcessModelPostInteractive callback
- CallbackType_ModelPostResult 
 –(Value: 0x3) ProcessModelPostResult callback
- CallbackType_ModelPostResults 
 –(Value: 0x15) ProcessModelPostResults callback
- CallbackType_ModelPostStep 
 –(Value: 0x4) ProcessModelPostStep callback
- CallbackType_ModelPreInteractive 
 –(Value: 0x5) ProcessModelPreInteractive callback
- CallbackType_ModelPreStep 
 –(Value: 0x6) ProcessModelPreStep callback
- CallbackType_SeqFilePostError 
 –(Value: 0x7) SequenceFilePostError callback
- CallbackType_SeqFilePostFail 
 –(Value: 0x8) SequenceFilePostFail callback
- CallbackType_SeqFilePostInteractive 
 –(Value: 0x9) SequenceFilePostInteractive callback
- CallbackType_SeqFilePostResult 
 –(Value: 0xA) SequenceFilePostResult callback
- CallbackType_SeqFilePostResults 
 –(Value: 0x16) SequenceFilePostResults callback
- CallbackType_SeqFilePostStep 
 –(Value: 0xB) SequenceFilePostStep callback
- CallbackType_SeqFilePreInteractive 
 –(Value: 0xC) SequenceFilePreInteractive callback
- CallbackType_SeqFilePreStep 
 –(Value: 0xD) SequenceFilePreStep callback
- CallbackType_StationPostError 
 –(Value: 0xE) StationPostError callback
- CallbackType_StationPostFail 
 –(Value: 0xF) StationPostFail callback
- CallbackType_StationPostInteractive 
 –(Value: 0x10) StationPostInteractive callback
- CallbackType_StationPostResult 
 –(Value: 0x11) StationPostResult callback
- CallbackType_StationPostResults 
 –(Value: 0x17) StationPostResults callback
- CallbackType_StationPostStep 
 –(Value: 0x12) StationPostStep callback
- CallbackType_StationPreInteractive 
 –(Value: 0x13) StationPreInteractive callback
- CallbackType_StationPreStep 
 –(Value: 0x14) StationPreStep callback

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/checkedstates.html language=enus -->
## TOPIC 00335: CheckedStates

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/checkedstates.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/checkedstates.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the AdditionalResult.CheckedState property. CheckedState_Checked –(Value: 2) Specifies to log the additional result. CheckedState_Indeterminate –(Value: 3) Specifies to log the additional result for some but not all members of the AdditionalResult.Elements collection. Checke

### CheckedStates

Use these constants with the
 [AdditionalResult.CheckedState](additionalresult-checkedstate.html)
 property.

- CheckedState_Checked 
 –(Value: 2) Specifies to log the additional result.
- CheckedState_Indeterminate 
 –(Value: 3) Specifies to log the additional result for some but not all members of the
 AdditionalResult.Elements 
 collection.
- CheckedState_Unchecked 
 –(Value: 1) Specifies not to log the additional result.

#### See Also

[AdditionalResult.CheckedState](additionalresult-checkedstate.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/checkformodifiedtypesoptions.html language=enus -->
## TOPIC 00336: CheckForModifiedTypesOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/checkformodifiedtypesoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/checkformodifiedtypesoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the options parameter of the PropertyObjectFile.CheckForModifiedTypes method. CheckForModifiedTypes_AutoIncrementVersions –(Value: 0x1) Specifies to disable the PropTypeFlags_IsModifiedType flag for a modified type and increment the version numb

### CheckForModifiedTypesOptions

These constants represent the options you can use with the
 options
 parameter of the
 [PropertyObjectFile.CheckForModifiedTypes](propertyobjectfile-checkformodifiedtypes.html)
 method.

- CheckForModifiedTypes_AutoIncrementVersions 
 –(Value: 0x1) Specifies to disable the
 PropTypeFlags_IsModifiedType 
 flag for a modified type and increment the version number of the type.
- CheckForModifiedTypes_NoAction 
 –(Value: 0x4) Specifies to perform no action if a modified type is found.
- CheckForModifiedTypes_Prompt 
 –(Value: 0x2) Specifies to launch a warning dialog box if a modified type is found.
- CheckForModifiedTypes_RemoveTypesModifiedMark 
 –(Value: 0xC) Specifies to disable the
 PropTypeFlags_IsModifiedType 
 flag for a modified type.
- CheckForModifiedTypes_UseStationOptions 
 –(Value: 0x0) Specifies to use the Before Saving Modified Types option on the
 File tab 
 of the
 Station Options 
 dialog box.

#### See Also

[File tab](../tsref/file-tab-station-options-dialog-box.html)

[PropertyObjectFile.CheckForModifiedTypes](propertyobjectfile-checkformodifiedtypes.html)

[Station Options dialog box](../tsref/station-options-dialog-box.html)

[StationOptions.TypeVersionAutoIncrementPromptOpt](stationoptions-typeversionautoincrementprompt.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/checkupdatedstatusoptions.html language=enus -->
## TOPIC 00337: CheckUpdatedStatusOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/checkupdatedstatusoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/checkupdatedstatusoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the values you can use with the options parameter of the LabVIEWNXGModule.HavePropertiesChanged method. Use the bitwise-OR operator to specify more than one option. CheckUpdatedStatusOption_All –(Value: 0x0) Perform validations for all the options. CheckUpdatedStatusOption_

### CheckUpdatedStatusOptions

These constants represent the values you can use with the options parameter of the
 LabVIEWNXGModule.HavePropertiesChanged
 method. Use the
 bitwise-OR
 operator to specify more than one option.

- CheckUpdatedStatusOption_All 
 –(Value: 0x0) Perform validations for all the options.
- CheckUpdatedStatusOption_ExpectedGLLPath 
 –(Value: 0x8) Validate that the GLL configured in the GLL Path property of the module matches the output path specified in the LabVIEW NXG component (.gcomp) selected in the step.
- CheckUpdatedStatusOption_GVIChecksum 
 –(Value: 0x2) Validate that the checksum of the GVI matches the checksum value stored in the module. Checksum changes indicate that the parameters or namespace of the GVI has changed from when the module was configured/last reloaded.
- CheckUpdatedStatusOption_GVIDescription 
 –(Value: 0x1) Validate if GVI description changed.
- CheckUpdatedStatusOption_GVIState 
 –(Value: 0x4) Validate if GVI is broken.
- CheckUpdatedStatusOption_QualifiedNamePresentInGLL 
 –(Value: 0x10) Validate that the GVI specified in the module is contained in the component(.gcomp) specified in the Module Qualified Name.

#### See Also

[LabVIEWNXGModule.HavePropertiesChanged](labviewnxgmodule-havepropertieschanged.html)

[GetUpdatedStatusOptions](getupdatedstatusoptions.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/codetemplate-description.html language=enus -->
## TOPIC 00338: CodeTemplate.Description

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/codetemplate-description.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/codetemplate-description.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CodeTemplate.Description Data Type String Purpose Returns the description of this code template.

### CodeTemplate.Description

#### Syntax

[CodeTemplate](codetemplate.html).Description

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the description of this code template.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/codetemplate-name.html language=enus -->
## TOPIC 00339: CodeTemplate.Name

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/codetemplate-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/codetemplate-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CodeTemplate.Name Data Type String Purpose Returns the name of this code template. You can use this name when you set the CommonCModule.CodeTemplateName property before calling the Module.CreateCode or CommonCModule.LoadPrototypeFromCodeTemplate methods. See Also CommonCModule.CodeTemplateNam

### CodeTemplate.Name

#### Syntax

[CodeTemplate](codetemplate.html).Name

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of this code template. You can use this name when you set the
 [CommonCModule.CodeTemplateName](commoncmodule-codetemplatename.html)
 property before calling the
 [Module.CreateCode](module-createcode.html)
 or
 [CommonCModule.LoadPrototypeFromCodeTemplate](commoncmodule-loadprototypefromcodetemplate.html)
 methods.

#### See Also

[CommonCModule.CodeTemplateName](commoncmodule-codetemplatename.html)

[CommonCModule.LoadPrototypeFromCodeTemplate](commoncmodule-loadprototypefromcodetemplate.html)

[Module.CreateCode](module-createcode.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/codetemplate-type.html language=enus -->
## TOPIC 00340: CodeTemplate.Type

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/codetemplate-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/codetemplate-type.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CodeTemplate.Type Data Type CodeTemplateTypes Use the following constants with this data type: CodeTemplateType_CppOrC –(Value: 4) Specifies a code template for the C/C++ DLL Adapter and specifies that the C/C++ Module creates code in a text file. CodeTemplateType_CVI –(Value: 3) Specifies a

### CodeTemplate.Type

#### Syntax

[CodeTemplate](codetemplate.html).Type

#### Data Type

[CodeTemplateTypes](codetemplatetypes.html)

Use the following constants with this data type:

- CodeTemplateType_CppOrC 
 –(Value: 4) Specifies a code template for the C/C++ DLL Adapter and specifies that the C/C++ Module creates code in a text file.
- CodeTemplateType_CVI 
 –(Value: 3) Specifies a code template for the LabWindows/CVI Adapter.
- CodeTemplateType_HTBasic 
 –(Value: 8) Specifies a code template for the HTBasic Adapter.
- CodeTemplateType_LabVIEW 
 –(Value: 2) Specifies a code template for the LabVIEW Adapter.
- CodeTemplateType_LabVIEWNXG 
 –(Value: 9) Specifies a code template for the LabVIEW NXG Adapter.
- CodeTemplateType_Legacy 
 –(Value: 1) Specifies the legacy template for the LabVIEW or LabWindows/CVI Adapter. The legacy code template has a fixed prototype that takes a
 TestData 
 and a
 TestError 
 parameter.
- CodeTemplateType_VisualBasicDotNet 
 –(Value: 7) Specifies a code template for the .NET Adapter and specifies that the .NET Module creates Visual Basic .NET code.
- CodeTemplateType_VisualCppDotNet 
 –(Value: 5) Specifies a code template for the C/C++ DLL Adapter and specifies that the C/C++ Module creates code in Microsoft Visual Studio.
- CodeTemplateType_VisualCSharpDotNet 
 –(Value: 6) Specifies a code template for the .NET Adapter and specifies that the .NET Module creates C# code.

#### Purpose

Returns the type of this code template. The code template type determines which adapter the code module is associated with.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/codetemplate.html language=enus -->
## TOPIC 00341: CodeTemplate

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/codetemplate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/codetemplate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this interface to obtain information about a code template. Code templates are associated with adapters and represent the default code that modules use when creating code for an instance of a step type. Use the StepType.CodeTemplates property to obtain a collection of CodeTemplate objects associ

### CodeTemplate

Use this interface to obtain information about a code template. Code templates are associated with adapters and represent the default code that modules use when creating code for an instance of a step type. Use the
 [StepType.CodeTemplates](steptype-codetemplates.html)
 property to obtain a collection of CodeTemplate objects associated with a step type.

#### Properties

| Description (Read Only) |
| --- |
| Name (Read Only) |
| Type (Read Only) |

#### See Also

[CommonCModule.CodeTemplateName](commoncmodule-codetemplatename.html)

[StepType.CodeTemplates](steptype-codetemplates.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/codetemplates-count.html language=enus -->
## TOPIC 00342: CodeTemplates.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/codetemplates-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/codetemplates-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CodeTemplates.Count Data Type Long Purpose Returns the number of items in the collection.

### CodeTemplates.Count

#### Syntax

[CodeTemplates](codetemplates.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/codetemplates-item.html language=enus -->
## TOPIC 00343: CodeTemplates.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/codetemplates-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/codetemplates-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CodeTemplates.Item( index) Data Type CodeTemplate Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the item to retrieve. See Also CodeTemplate

### CodeTemplates.Item

#### Syntax

[CodeTemplates](codetemplates.html).Item( index)

#### Data Type

[CodeTemplate](codetemplate.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve.

#### See Also

[CodeTemplate](codetemplate.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/codetemplates.html language=enus -->
## TOPIC 00344: CodeTemplates

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/codetemplates.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/codetemplates.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of CodeTemplate objects. Code templates are associated with adapters and represent the default code that modules use when creating code for an instance of a step type. Use the StepType.CodeTemplates property to obtain a collection of CodeTemplate objects associated with a step type. Pro

### CodeTemplates

A collection of
 [CodeTemplate](codetemplate.html)
 objects. Code templates are associated with adapters and represent the default code that modules use when creating code for an instance of a step type. Use the
 [StepType.CodeTemplates](steptype-codetemplates.html)
 property to obtain a collection of CodeTemplate objects associated with a step type.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[CodeTemplate](codetemplate.html)

[StepType.CodeTemplates](steptype-codetemplates.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/codetemplatetypes.html language=enus -->
## TOPIC 00345: CodeTemplateTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/codetemplatetypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/codetemplatetypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the CodeTemplate.Type property. CodeTemplateType_CppOrC –(Value: 4) Specifies a code template for the C/C++ DLL Adapter and specifies that the C/C++ Module creates code in a text file. CodeTemplateType_CVI –(Value: 3) Specifies a code template for the LabWindows/CVI Adapter.

### CodeTemplateTypes

Use these constants with the
 [CodeTemplate.Type](codetemplate-type.html)
 property.

- CodeTemplateType_CppOrC 
 –(Value: 4) Specifies a code template for the C/C++ DLL Adapter and specifies that the C/C++ Module creates code in a text file.
- CodeTemplateType_CVI 
 –(Value: 3) Specifies a code template for the LabWindows/CVI Adapter.
- CodeTemplateType_HTBasic 
 –(Value: 8) Specifies a code template for the HTBasic Adapter.
- CodeTemplateType_LabVIEW 
 –(Value: 2) Specifies a code template for the LabVIEW Adapter.
- CodeTemplateType_LabVIEWNXG 
 –(Value: 9) Specifies a code template for the LabVIEW NXG Adapter.
- CodeTemplateType_Legacy 
 –(Value: 1) Specifies the legacy template for the LabVIEW or LabWindows/CVI Adapter. The legacy code template has a fixed prototype that takes a
 TestData 
 and a
 TestError 
 parameter.
- CodeTemplateType_VisualBasicDotNet 
 –(Value: 7) Specifies a code template for the .NET Adapter and specifies that the .NET Module creates Visual Basic .NET code.
- CodeTemplateType_VisualCppDotNet 
 –(Value: 5) Specifies a code template for the C/C++ DLL Adapter and specifies that the C/C++ Module creates code in Microsoft Visual Studio.
- CodeTemplateType_VisualCSharpDotNet 
 –(Value: 6) Specifies a code template for the .NET Adapter and specifies that the .NET Module creates C# code.

#### See Also

[CodeTemplate.Type](codetemplate-type.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/color.html language=enus -->
## TOPIC 00346: Color

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/color.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/color.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Color values are typically four-byte integers and commonly use little-endian and big-endian format. Microsoft Windows and ActiveX use the little-endian format, which stores red, green, and blue color components in the 0x00BBGGRR byte positions. LabVIEW and LabWindows/CVI use the big-endian format, w

### Color

Color values are typically four-byte integers and commonly use little-endian and big-endian format. Microsoft Windows and ActiveX use the little-endian format, which stores red, green, and blue color components in the 0x00BBGGRR byte positions. LabVIEW and LabWindows/CVI use the big-endian format, which stores the color components in the 0x00RRGGBB byte positions.

If you are specifying a color value in an expression, you can use a predefined little-endian color constant, such as tsRed or tsDarkBlue. Refer to
 Constants»Color
 on the
 [Operators/Functions tab](../tsref/operators-functions-tab-expression-browser-di.html)
 of the
 [Expression Browser](../tsref/expression-browser-dialog-box.html)
 dialog box for the list of available expression color constants. Use the
 ConvertColor
 expression function to convert the two color value formats.

Some Windows and ActiveX functions support specifying a system color using the 0x800000xx byte format, where
 xx
 is a valid Win32
 GetSysColor
 index. The possible values are listed below.

- 0x00bbggrr—Where
 bb 
 specifies the intensity of the color blue,
 gg 
 specifies the intensity of the color green, and
 rr 
 specifies the intensity of the color red.
- 0x800000xx—Where
 xx 
 is a valid Win32
 GetSysColor 
 index. The possible values are listed below.
 Constant
 ValueCOLOR_SCROLLBAR
 0
 COLOR_BACKGROUND
 1
 COLOR_ACTIVECAPTION
 2
 COLOR_INACTIVECAPTION
 3
 COLOR_MENU
 4
 COLOR_WINDOW
 5
 COLOR_WINDOWFRAME
 6
 COLOR_MENUTEXT
 7
 COLOR_WINDOWTEXT
 8
 COLOR_CAPTIONTEXT
 9
 COLOR_ACTIVEBORDER
 10
 COLOR_INACTIVEBORDER
 11
 COLOR_APPWORKSPACE
 12
 COLOR_HIGHLIGHT
 13
 COLOR_HIGHLIGHTEXT
 14
 COLOR_BTNFACE
 15
 COLOR_BTNSHADOW
 16
 COLOR_GRAYTEXT
 17
 COLOR_BTNTEXT
 18
 COLOR_INACTIVECAPTIONTEXT
 19
 COLOR_BTNHIGHLIGHT
 20
 COLOR_3DDKSHADOW
 21
 COLOR_3DLIGHT
 22
 COLOR_INFOTEXT
 23
 COLOR_INFOBK
 24
 COLOR_HOTLIGHT
 26
 COLOR_GRADIENTACTIVECAPTION
 27
 COLOR_GRADIENTINACTIVECAPTION
 28
 COLOR_MENUHILIGHT
 29
 COLOR_MENUBAR
 30

Parent topic:

Data Types for TestStand

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-asadapter.html language=enus -->
## TOPIC 00347: CommonCAdapter.AsAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-asadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-asadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.AsAdapter Return Value Adapter Purpose Returns the underlying module Adapter object that represents the CommonCAdapter. Remarks Use the underlying module Adapter object to access properties and methods common to all adapters. See Also Adapter CVIAdapter DllAdapter

### CommonCAdapter.AsAdapter

#### Syntax

[CommonCAdapter](commoncadapter.html).AsAdapter

#### Return Value

[Adapter](adapter.html)

#### Purpose

Returns the underlying module Adapter object that represents the CommonCAdapter.

#### Remarks

Use the underlying module Adapter object to access properties and methods common to all adapters.

#### See Also

[Adapter](adapter.html)

[CVIAdapter](cviadapter.html)

[DllAdapter](dlladapter.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-defaultstructpacking.html language=enus -->
## TOPIC 00348: CommonCAdapter.DefaultStructPacking

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-defaultstructpacking.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-defaultstructpacking.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.DefaultStructPacking Data Type StructPassingOptions Use the following constants with this data type: StructPassing_AdapterDefault –(Value: 0x0) Specifies to use the default TestStand setting to store structure and union members. You can change the default TestStand setting by m

### CommonCAdapter.DefaultStructPacking

#### Syntax

[CommonCAdapter](commoncadapter.html).DefaultStructPacking

#### Data Type

[StructPassingOptions](structpassingoptions.html)

Use the following constants with this data type:

- StructPassing_AdapterDefault 
 –(Value: 0x0) Specifies to use the default TestStand setting to store structure and union members. You can change the default TestStand setting by modifying the
 CommonCAdapter.DefaultStructPacking 
 property or by configuring it in the C/C++ DLL Adapter Configuration
 C/C++ DLL Adapter Configuration 
 or
 LabWindows/CVI Adapter Configuration 
 dialog boxes. Do not pass
 StructPassing_AdapterDefault 
 to the
 CommonCAdapter.DefaultStructPacking 
 property itself.
- StructPassing_EightByte 
 –(Value: 0x8) Specifies to store structure and union members on an 8-byte boundary.
- StructPassing_FourByte 
 –(Value: 0x4) Specifies to store structure and union members on a 4-byte boundary.
- StructPassing_OneByte 
 –(Value: 0x1) Specifies to store structure and union members on a 1-byte boundary.
- StructPassing_SixteenByte 
 –(Value: 0x16) Specifies to store structure and union members on a 16-byte boundary.
- StructPassing_TwoByte 
 –(Value: 0x2) Specifies to store structure and union members on a 2-byte boundary.

#### Purpose

Specifies how an adapter packs the structure parameters it passes to a corresponding module. Set the packing options to match the default for structure packing in the development environment.

#### Remarks

Specify the type of struct passing by using the
 StructPassingOptions
 constants.

#### See Also

[C/C++ DLL Adapter Configuration](../tsref/c-c-dll-adapter-configuration-dialog-box.html)

[CommonCAdapter.DefaultStructPacking](commoncadapter-defaultstructpacking.html)

[CommonCAdapter.GetStructPacking](commoncadapter-getstructpacking.html)

[CommonCAdapter.SetStructPacking](commoncadapter-setstructpacking.html)

[LabWindows/CVI Adapter Configuration dialog box](../tsref/labwindows-cvi-adapter-configuration-dialog-b.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-getallowstructpassing.html language=enus -->
## TOPIC 00349: CommonCAdapter.GetAllowStructPassing

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-getallowstructpassing.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-getallowstructpassing.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.GetAllowStructPassing( typeDefinition) Return Value Boolean Purpose Returns a value that indicates whether a type definition allows the adapter to pass instances of the type as structures to the corresponding module. Parameters typeDefinition As PropertyObject [In] Specifies th

### CommonCAdapter.GetAllowStructPassing

#### Syntax

[CommonCAdapter](commoncadapter.html).GetAllowStructPassing( typeDefinition)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether a type definition allows the adapter to pass instances of the type as structures to the corresponding module.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the PropertyObject is not a type definition.

#### See Also

[CommonCAdapter.SetAllowStructPassing](commoncadapter-setallowstructpassing.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-getdllfunctions.html language=enus -->
## TOPIC 00350: CommonCAdapter.GetDllFunctions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-getdllfunctions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-getdllfunctions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.GetDllFunctions( dllPath) Return Value DllFunctions Purpose Returns the functions for a specific DLL. Remarks This method reads the specified DLL and obtains a list of functions in the DLL. If a type library exists in the same directory as the DLL and the type library has the s

### CommonCAdapter.GetDllFunctions

#### Syntax

[CommonCAdapter](commoncadapter.html).GetDllFunctions( dllPath)

#### Return Value

[DllFunctions](dllfunctions.html)

#### Purpose

Returns the functions for a specific DLL.

#### Remarks

This method reads the specified DLL and obtains a list of functions in the DLL. If a type library exists in the same directory as the DLL and the type library has the same base filename as the DLL, this method reads the type library for function parameter information.

#### Parameters

dllPath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute path of the DLL.

#### See Also

[DllFunctions](dllfunctions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-getenumerationnames.html language=enus -->
## TOPIC 00351: CommonCAdapter.GetEnumerationNames

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-getenumerationnames.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-getenumerationnames.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.GetEnumerationNames( includeEnumArrays) Return Value String Array Purpose Returns a list of TestStand type names to use to pass to enumeration parameters. The list contains all currently loaded TestStand types you can pass to enumeration parameters. Parameters includeEnumArrays

### CommonCAdapter.GetEnumerationNames

#### Syntax

[CommonCAdapter](commoncadapter.html).GetEnumerationNames( includeEnumArrays)

#### Return Value

[String Array](data-types-for-teststand.html)

#### Purpose

Returns a list of TestStand type names to use to pass to enumeration parameters. The list contains all currently loaded TestStand types you can pass to enumeration parameters.

#### Parameters

includeEnumArrays
 As
 [Boolean](data-types-for-teststand.html)

[In] Set this parameter to
 True
 to include Arrays of Enumerations in the list of TestStand type names. Otherwise, set to
 False
 .

#### See Also

[Type Properties dialog box](../tsref/type-properties-dialog-box.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-getexcludefromstruct.html language=enus -->
## TOPIC 00352: CommonCAdapter.GetExcludeFromStruct

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-getexcludefromstruct.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-getexcludefromstruct.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.GetExcludeFromStruct( typeDefinition, propertyLookupString) Return Value Boolean Purpose Returns a value that indicates whether the specified type definition property is excluded when converting instances of the type definition into structures to pass as parameters to the corre

### CommonCAdapter.GetExcludeFromStruct

#### Syntax

[CommonCAdapter](commoncadapter.html).GetExcludeFromStruct( typeDefinition, propertyLookupString)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the specified type definition property is excluded when converting instances of the type definition into structures to pass as parameters to the corresponding code module.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the PropertyObject is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

#### See Also

[CommonCAdapter.SetExcludeFromStruct](commoncadapter-setexcludefromstruct.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-getstructmemberarraystorage.html language=enus -->
## TOPIC 00353: CommonCAdapter.GetStructMemberArrayStorage

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-getstructmemberarraystorage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-getstructmemberarraystorage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.GetStructMemberArrayStorage( typeDefinition, propertyLookupString) Return Value StructMemberArrayStorageOptions Use the following constants with this data type: StructMemberStorage_ArrayPointer –(Value: 0x101) Specifies to store the array as a pointer to a memory location outsi

### CommonCAdapter.GetStructMemberArrayStorage

#### Syntax

[CommonCAdapter](commoncadapter.html).GetStructMemberArrayStorage( typeDefinition, propertyLookupString)

#### Return Value

[StructMemberArrayStorageOptions](structmemberarraystorageoptions.html)

Use the following constants with this data type:

- StructMemberStorage_ArrayPointer 
 –(Value: 0x101) Specifies to store the array as a pointer to a memory location outside of the struct.
- StructMemberStorage_InlineArray 
 –(Value 0x100) Specifies to store the array within the structure itself.
- StructMemberStorage_LabVIEWArray 
 –(Value: 0x102) Specifies to store the array in the format that the DLLs created with the LabVIEW Application Builder use.

#### Purpose

Returns the kind of array storage used for the type definition array property that the corresponding location specifies.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the PropertyObject is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

#### See Also

[CommonCAdapter.SetStructMemberArrayStorage](commoncadapter-setstructmemberarraystorage.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-getstructmemberstorage.html language=enus -->
## TOPIC 00354: CommonCAdapter.GetStructMemberStorage

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-getstructmemberstorage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-getstructmemberstorage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.GetStructMemberStorage( typeDefinition, propertyLookupString) Return Value StructMemberStorageOptions Use the following constants with this data type: StructMemberStorage_EmbeddedStruct –(Value: 32) Specifies to store a struct as a member inside the containing struct. StructMem

### CommonCAdapter.GetStructMemberStorage

#### Syntax

[CommonCAdapter](commoncadapter.html).GetStructMemberStorage( typeDefinition, propertyLookupString)

#### Return Value

[StructMemberStorageOptions](structmemberstorageoptions.html)

Use the following constants with this data type:

- StructMemberStorage_EmbeddedStruct 
 –(Value: 32) Specifies to store a struct as a member inside the containing struct.
- StructMemberStorage_InlineString 
 –(Value: 0) Specifies to store a string as an array of characters inside the struct.
- StructMemberStorage_LabVIEWString 
 –(Value: 2) Specifies to store a string in the format used by DLLs created with the LabVIEW Application Builder. The
 CommonCAdapter.GetStructMemberType 
 and
 CommonCAdapter.SetStructMemberType 
 methods do not apply when the
 CommonCAdapter.GetStructMemberStorage 
 method returns this value.
- StructMemberStorage_StringPointer 
 –(Value: 1) Specifies to store a string as a character pointer. The characters themselves are stored at a memory location outside of the containing struct.
- StructMemberStorage_StructPointer 
 –(Value: 33) Specifies to store a pointer inside the containing struct which points to a member struct at a memory location outside of the containing struct.

#### Purpose

Returns the kind of storage used for the type definition property that the corresponding location specifies.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the PropertyObject is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

#### See Also

[CommonCAdapter.GetStructMemberStorage](commoncadapter-getstructmemberstorage.html)

[CommonCAdapter.GetStructMemberType](commoncadapter-getstructmembertype.html)

[CommonCAdapter.SetStructMemberStorage](commoncadapter-setstructmemberstorage.html)

[CommonCAdapter.SetStructMemberType](commoncadapter-setstructmembertype.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-getstructmemberstringbuffersiz.html language=enus -->
## TOPIC 00355: CommonCAdapter.GetStructMemberStringBufferSize

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-getstructmemberstringbuffersiz.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-getstructmemberstringbuffersiz.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.GetStructMemberStringBufferSize( typeDefinition, propertyLookupString) Return Value Long Purpose Returns the string buffer size that corresponds to the property that the corresponding location specifies. Parameters typeDefinition As PropertyObject [In] Specifies the type defini

### CommonCAdapter.GetStructMemberStringBufferSize

#### Syntax

[CommonCAdapter](commoncadapter.html).GetStructMemberStringBufferSize( typeDefinition, propertyLookupString)

#### Return Value

[Long](data-types-for-teststand.html)

#### Purpose

Returns the string buffer size that corresponds to the property that the corresponding location specifies.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the PropertyObject is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

#### See Also

[CommonCAdapter.SetStructMemberStringBufferSize](commoncadapter-setstructmemberstringbuffersiz.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-getstructmembertype.html language=enus -->
## TOPIC 00356: CommonCAdapter.GetStructMemberType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-getstructmembertype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-getstructmembertype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.GetStructMemberType( typeDefinition, propertyLookupString) Return Value StructMemberTypes Purpose Returns the type of the type definition property that the corresponding location specifies. Parameters typeDefinition As PropertyObject [In] Specifies the type definition. This met

### CommonCAdapter.GetStructMemberType

#### Syntax

[CommonCAdapter](commoncadapter.html).GetStructMemberType( typeDefinition, propertyLookupString)

#### Return Value

[StructMemberTypes](structmembertypes.html)

#### Purpose

Returns the type of the type definition property that the corresponding location specifies.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the PropertyObject is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

#### See Also

[CommonCAdapter.SetStructMemberType](commoncadapter-setstructmembertype.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-getstructnames.html language=enus -->
## TOPIC 00357: CommonCAdapter.GetStructNames

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-getstructnames.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-getstructnames.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.GetStructNames Return Value String Array Purpose Returns a list of TestStand type names to use to pass to C struct parameters. The list contains all the currently loaded TestStand types you can pass to structure parameters. See Also Type Properties dialog box

### CommonCAdapter.GetStructNames

#### Syntax

[CommonCAdapter](commoncadapter.html).GetStructNames

#### Return Value

[String Array](data-types-for-teststand.html)

#### Purpose

Returns a list of TestStand type names to use to pass to C struct parameters. The list contains all the currently loaded TestStand types you can pass to structure parameters.

#### See Also

[Type Properties dialog box](../tsref/c-struct-passing-tab-type-properties-dialog-b.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-getstructpacking.html language=enus -->
## TOPIC 00358: CommonCAdapter.GetStructPacking

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-getstructpacking.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-getstructpacking.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.GetStructPacking( typeDefinition) Return Value StructPassingOptions Use the following constants with this data type: StructPassing_AdapterDefault –(Value: 0x0) Specifies to use the default TestStand setting to store structure and union members. You can change the default TestSt

### CommonCAdapter.GetStructPacking

#### Syntax

[CommonCAdapter](commoncadapter.html).GetStructPacking( typeDefinition)

#### Return Value

[StructPassingOptions](structpassingoptions.html)

Use the following constants with this data type:

- StructPassing_AdapterDefault 
 –(Value: 0x0) Specifies to use the default TestStand setting to store structure and union members. You can change the default TestStand setting by modifying the
 CommonCAdapter.DefaultStructPacking 
 property or by configuring it in the
 C/C++ DLL Adapter Configuration 
 or
 LabWindows/CVI Adapter Configuration 
 dialog boxes. Do not pass
 StructPassing_AdapterDefault 
 to the
 CommonCAdapter.DefaultStructPacking 
 property itself.
- StructPassing_EightByte 
 –(Value: 0x8) Specifies to store structure and union members on an 8-byte boundary.
- StructPassing_FourByte 
 –(Value: 0x4) Specifies to store structure and union members on a 4-byte boundary.
- StructPassing_OneByte 
 –(Value: 0x1) Specifies to store structure and union members on a 1-byte boundary.
- StructPassing_SixteenByte 
 –(Value: 0x16) Specifies to store structure and union members on a 16-byte boundary.
- StructPassing_TwoByte 
 –(Value: 0x2) Specifies to store structure and union members on a 2-byte boundary.

Indicates the structure passing for the specific type definition.

#### Purpose

Returns the manner in which an adapter packs the structure parameters it passes to a corresponding module. The packing options must match the structure packing for the struct in the code module.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the PropertyObject is not a type definition.

#### See Also

[C/C++ DLL Adapter Configuration](../tsref/c-c-dll-adapter-configuration-dialog-box.html)

[CommonCAdapter.DefaultStructPacking](commoncadapter-defaultstructpacking.html)

[CommonCAdapter.SetStructPacking](commoncadapter-setstructpacking.html)

[LabWindows/CVI Adapter Configuration dialog box](../tsref/labwindows-cvi-adapter-configuration-dialog-b.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-setallowstructpassing.html language=enus -->
## TOPIC 00359: CommonCAdapter.SetAllowStructPassing

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-setallowstructpassing.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-setallowstructpassing.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.SetAllowStructPassing( typeDefinition, allowStructPassing) Purpose Specifies whether a type definition allows the adapter to pass instances of the type as structures to the corresponding module. Parameters typeDefinition As PropertyObject [In] Specifies the type definition. Thi

### CommonCAdapter.SetAllowStructPassing

#### Syntax

[CommonCAdapter](commoncadapter.html).SetAllowStructPassing( typeDefinition, allowStructPassing)

#### Purpose

Specifies whether a type definition allows the adapter to pass instances of the type as structures to the corresponding module.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the PropertyObject is not a type definition.

allowStructPassing
 As
 [Boolean](data-types-for-teststand.html)

[In] If this parameter is
 True
 , structure passing is enabled. Otherwise, structure passing is disabled.

#### See Also

[CommonCAdapter.GetAllowStructPassing](commoncadapter-getallowstructpassing.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-setexcludefromstruct.html language=enus -->
## TOPIC 00360: CommonCAdapter.SetExcludeFromStruct

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-setexcludefromstruct.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-setexcludefromstruct.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.SetExcludeFromStruct( typeDefinition, propertyLookupString, excludeFromStruct) Purpose Specifies whether the specified type definition property is excluded when converting instances of the type definition into structures to pass as parameters to the corresponding code module. P

### CommonCAdapter.SetExcludeFromStruct

#### Syntax

[CommonCAdapter](commoncadapter.html).SetExcludeFromStruct( typeDefinition, propertyLookupString, excludeFromStruct)

#### Purpose

Specifies whether the specified type definition property is excluded when converting instances of the type definition into structures to pass as parameters to the corresponding code module.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the PropertyObject is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

excludeFromStruct
 As
 [Boolean](data-types-for-teststand.html)

[In] Set this parameter to
 True
 to exclude the corresponding property. Otherwise, set this parameter to
 False
 .

#### See Also

[CommonCAdapter.GetExcludeFromStruct](commoncadapter-getexcludefromstruct.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-setstructmemberarraystorage.html language=enus -->
## TOPIC 00361: CommonCAdapter.SetStructMemberArrayStorage

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-setstructmemberarraystorage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-setstructmemberarraystorage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.SetStructMemberArrayStorage( typeDefinition, propertyLookupString, structMemberArrayStorage) Purpose Specifies the kind of array storage used for the type definition property that the corresponding location specifies. Parameters typeDefinition As PropertyObject [In] Specifies t

### CommonCAdapter.SetStructMemberArrayStorage

#### Syntax

[CommonCAdapter](commoncadapter.html).SetStructMemberArrayStorage( typeDefinition, propertyLookupString, structMemberArrayStorage)

#### Purpose

Specifies the kind of array storage used for the type definition property that the corresponding location specifies.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the PropertyObject is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

structMemberArrayStorage
 As
 [StructMemberArrayStorageOptions](structmemberarraystorageoptions.html)

[In] Specifies the kind of array storage of the specific property in the corresponding
 typeDefinition
 parameter.

#### See Also

[CommonCAdapter.GetStructMemberArrayStorage](commoncadapter-getstructmemberarraystorage.html)

[PropertyObject](propertyobject.html)

[StructMemberArrayStorageOptions](structmemberarraystorageoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-setstructmemberstorage.html language=enus -->
## TOPIC 00362: CommonCAdapter.SetStructMemberStorage

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-setstructmemberstorage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-setstructmemberstorage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.SetStructMemberStorage( typeDefinition, propertyLookupString, structMemberStorage) Purpose Specifies the kind of storage used for the type definition that the corresponding location stores. Parameters typeDefinition As PropertyObject [In] Specifies the type definition. This met

### CommonCAdapter.SetStructMemberStorage

#### Syntax

[CommonCAdapter](commoncadapter.html).SetStructMemberStorage( typeDefinition, propertyLookupString, structMemberStorage)

#### Purpose

Specifies the kind of storage used for the type definition that the corresponding location stores.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the PropertyObject is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

structMemberStorage
 As
 [StructMemberStorageOptions](structmemberstorageoptions.html)

[In] Specifies the kind of storage of the specific property in the corresponding
 typeDefinition
 parameter.

#### See Also

[CommonCAdapter.GetStructMemberStorage](commoncadapter-getstructmemberstorage.html)

[PropertyObject](propertyobject.html)

[StructMemberArrayStorageOptions](structmemberarraystorageoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-setstructmemberstringbuffersiz.html language=enus -->
## TOPIC 00363: CommonCAdapter.SetStructMemberStringBufferSize

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-setstructmemberstringbuffersiz.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-setstructmemberstringbuffersiz.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.SetStructMemberStringBufferSize( typeDefinition, propertyLookupString, structMemberStringBufferSize) Purpose Specifies the string buffer size corresponding to the property that the corresponding location specifies. Parameters typeDefinition As PropertyObject [In] Specifies the

### CommonCAdapter.SetStructMemberStringBufferSize

#### Syntax

[CommonCAdapter](commoncadapter.html).SetStructMemberStringBufferSize( typeDefinition, propertyLookupString, structMemberStringBufferSize)

#### Purpose

Specifies the string buffer size corresponding to the property that the corresponding location specifies.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the PropertyObject is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

structMemberStringBufferSize
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the string buffer size for the corresponding property.

#### See Also

[CommonCAdapter.GetStructMemberStringBufferSize](commoncadapter-getstructmemberstringbuffersiz.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-setstructmembertype.html language=enus -->
## TOPIC 00364: CommonCAdapter.SetStructMemberType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-setstructmembertype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-setstructmembertype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.SetStructMemberType( typeDefinition, propertyLookupString, structMemberType) Purpose Specifies the type of the type definition property that the corresponding location specifies. Parameters typeDefinition As PropertyObject [In] Specifies the type definition. This method returns

### CommonCAdapter.SetStructMemberType

#### Syntax

[CommonCAdapter](commoncadapter.html).SetStructMemberType( typeDefinition, propertyLookupString, structMemberType)

#### Purpose

Specifies the type of the type definition property that the corresponding location specifies.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the PropertyObject is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

structMemberType
 As
 [StructMemberTypes](structmembertypes.html)

[In] Specifies the type of specific property in the corresponding
 typeDefinition
 parameter.

#### See Also

[CommonCAdapter.GetStructMemberType](commoncadapter-getstructmembertype.html)

[PropertyObject](propertyobject.html)

[StructMemberTypes](structmembertypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter-setstructpacking.html language=enus -->
## TOPIC 00365: CommonCAdapter.SetStructPacking

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter-setstructpacking.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter-setstructpacking.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCAdapter.SetStructPacking( typeDefinition, structPackingOption) Purpose Specifies how a type definition allows the adapter to pack the structure parameters it passes to a corresponding module. Set the packing options to match structure packing for the struct in the code module. Paramete

### CommonCAdapter.SetStructPacking

#### Syntax

[CommonCAdapter](commoncadapter.html).SetStructPacking( typeDefinition, structPackingOption)

#### Purpose

Specifies how a type definition allows the adapter to pack the structure parameters it passes to a corresponding module. Set the packing options to match structure packing for the struct in the code module.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the PropertyObject is not a type definition.

structPackingOption
 As
 [StructPassingOptions](structpassingoptions.html)

[In] Specifies the structure passing for the specific type definition.

#### See Also

[CommonCAdapter.DefaultStructPacking](commoncadapter-defaultstructpacking.html)

[CommonCAdapter.GetStructPacking](commoncadapter-getstructpacking.html)

[PropertyObject](propertyobject.html)

[StructPassingOptions](structpassingoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncadapter.html language=enus -->
## TOPIC 00366: CommonCAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the CommonCAdapter class to configure and obtain common information about the LabWindows/CVI and C/C++ DLL Adapters. To access the properties and methods of the Adapter class, use the CommonCAdapter.AsAdapter method to obtain an object. To access the properties and methods of a spec

### CommonCAdapter

Use objects from the CommonCAdapter class to configure and obtain common information about the LabWindows/CVI and C/C++ DLL Adapters.

To access the properties and methods of the Adapter class, use the
 [CommonCAdapter.AsAdapter](commoncadapter-asadapter.html)
 method to obtain an object.

To access the properties and methods of a specific adapter class, query the CommonCAdapter object for the interface of the adapter-specific interface you want.

#### Property

| DefaultStructPacking |
| --- |

#### Methods

| AsAdapter |
| --- |
| GetAllowStructPassing |
| GetDllFunctions |
| GetEnumerationNames |
| GetExcludeFromStruct |
| GetStructMemberArrayStorage |
| GetStructMemberStorage |
| GetStructMemberStringBufferSize |
| GetStructMemberType |
| GetStructNames |
| GetStructPacking |
| SetAllowStructPassing |
| SetExcludeFromStruct |
| SetStructMemberArrayStorage |
| SetStructMemberStorage |
| SetStructMemberStringBufferSize |
| SetStructMemberType |
| SetStructPacking |

#### See Also

[Adapter](adapter.html)

[CVIAdapter](cviadapter.html)

[DllAdapter](dlladapter.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncmodule-acceptfunctioncall.html language=enus -->
## TOPIC 00367: CommonCModule.AcceptFunctionCall

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncmodule-acceptfunctioncall.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncmodule-acceptfunctioncall.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCModule.AcceptFunctionCall( evaluationContext, funcCall, allowEditingPrototype, prototypeModified, cancelled) Return Value Boolean Returns True if this method modifies the module. Purpose This method updates the function name, parameters, and parameter values on the module to match the

### CommonCModule.AcceptFunctionCall

#### Syntax

[CommonCModule](commoncmodule.html).AcceptFunctionCall( evaluationContext, funcCall, allowEditingPrototype, prototypeModified, cancelled)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if this method modifies the module.

#### Purpose

This method updates the function name, parameters, and parameter values on the module to match the function call you pass as the
 funcCall
 parameter. If the function call you pass modifies the prototype of the function, this method prompts the user to accept the changes to the prototype.

#### Remarks

Use the
 [CommonCModule.FunctionCall](commoncmodule-functioncall.html)
 property to obtain a string that represents the current function call using syntax for calling an expression function.

#### Parameters

evaluationContext
 As
 
 [PropertyObject](propertyobject.html)

[In] This method uses this object to locate variables the
 funcCall
 parameter specifies.

funcCall
 As
 [String](data-types-for-teststand.html)

[In] Specifies a string for the function call that uses the syntax for calling an expression function.

allowEditingPrototype
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to allow this method to update the prototype of the currently loaded parameters from the
 funcCall
 parameter. Pass
 False
 to allow this method to only update the function name and parameter values.

prototypeModified
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns
 True
 if this method added, removed, or changed the type of a parameter in the function call.

cancelled
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns
 True
 if the user cancels accepting the changes to the prototype.

#### See Also

[CommonCModule.FunctionCall](commoncmodule-functioncall.html)

[CommonCModule.FunctionName](commoncmodule-functionname.html)

[CVIModule.Parameters](cvimodule-parameters.html)

[DllModule.Parameters](dllmodule-parameters.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncmodule-asmodule.html language=enus -->
## TOPIC 00368: CommonCModule.AsModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncmodule-asmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncmodule-asmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCModule.AsModule Return Value Module Purpose Returns the underlying module object that represents the CommonCModule. Remarks Use the Module object to access properties and methods common to all modules. See Also CVIModule DllModule Module

### CommonCModule.AsModule

#### Syntax

[CommonCModule](commoncmodule.html).AsModule

#### Return Value

[Module](module.html)

#### Purpose

Returns the underlying module object that represents the CommonCModule.

#### Remarks

Use the Module object to access properties and methods common to all modules.

#### See Also

[CVIModule](cvimodule.html)

[DllModule](dllmodule.html)

[Module](module.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncmodule-codetemplatename.html language=enus -->
## TOPIC 00369: CommonCModule.CodeTemplateName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncmodule-codetemplatename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncmodule-codetemplatename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCModule.CodeTemplateName Data Type String Purpose Specifies a code template associated with this module. Remarks The Module.CreateCode and CommonCModule.LoadPrototypeFromCodeTemplate methods use the code template this property specifies. If this property is empty, the Module.CreateCode

### CommonCModule.CodeTemplateName

#### Syntax

[CommonCModule](commoncmodule.html).CodeTemplateName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies a code template associated with this module.

#### Remarks

The
 [Module.CreateCode](module-createcode.html)
 and
 [CommonCModule.LoadPrototypeFromCodeTemplate](commoncmodule-loadprototypefromcodetemplate.html)
 methods use the code template this property specifies. If this property is empty, the
 Module.CreateCode
 method does not use a code template and the
 CommonCModule.LoadPrototypeFromCodeTemplate
 method does nothing. You can acquire a list of code template names using the collection the
 [StepType.CodeTemplates](steptype-codetemplates.html)
 property returns.

#### See Also

[CommonCModule.LoadPrototypeFromCodeTemplate](commoncmodule-loadprototypefromcodetemplate.html)

[Module.CreateCode](module-createcode.html)

[StepType.CodeTemplates](steptype-codetemplates.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncmodule-functioncall.html language=enus -->
## TOPIC 00370: CommonCModule.FunctionCall

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncmodule-functioncall.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncmodule-functioncall.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCModule.FunctionCall Data Type String Purpose Returns the function call using the syntax for calling an expression function. Remarks Use the CommonCModule.AcceptFunctionCall method to update the function name, parameters, and parameter values for the module using a string with syntax fo

### CommonCModule.FunctionCall

#### Syntax

[CommonCModule](commoncmodule.html).FunctionCall

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the function call using the syntax for calling an expression function.

#### Remarks

Use the
 [CommonCModule.AcceptFunctionCall](commoncmodule-acceptfunctioncall.html)
 method to update the function name, parameters, and parameter values for the module using a string with syntax for calling an expression function.

#### See Also

[CommonCModule.AcceptFunctionCall](commoncmodule-acceptfunctioncall.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncmodule-functionname.html language=enus -->
## TOPIC 00371: CommonCModule.FunctionName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncmodule-functionname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncmodule-functionname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCModule.FunctionName Data Type String Purpose Specifies the function in the code module the step calls. See Also CommonCModule.ModulePath CVIModule.ModuleType

### CommonCModule.FunctionName

#### Syntax

[CommonCModule](commoncmodule.html).FunctionName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the function in the code module the step calls.

#### See Also

[CommonCModule.ModulePath](commoncmodule-modulepath.html)

[CVIModule.ModuleType](cvimodule-moduletype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncmodule-loadprototype.html language=enus -->
## TOPIC 00372: CommonCModule.LoadPrototype

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncmodule-loadprototype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncmodule-loadprototype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCModule.LoadPrototype( discardParameterValues = False) Return Value Boolean Returns a value that indicates whether the prototype was loaded. This method usually returns True . Purpose This method is obsolete. Use the Module.LoadPrototype method instead. Remarks At any time, you can requ

### CommonCModule.LoadPrototype

#### Syntax

[CommonCModule](commoncmodule.html).LoadPrototype( discardParameterValues = False)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns a value that indicates whether the prototype was loaded. This method usually returns
 True
 .

#### Purpose

Note

Module.LoadPrototype

#### Remarks

At any time, you can request the LabWindows/CVI or C/C++ DLL Adapter to query the type library or read the DLL export table for the currently selected function by calling this method. If the module file does not have prototype information, this method returns
 False
 . Otherwise, this method returns
 True
 .

If the module contains prototype information, all the information is updated in the internal structure of the module configuration every time you call this method.

#### Parameters

discardParameterValues
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether to discard the values assigned to the current parameters once the prototype information is updated.

This parameter has a default value of
 False
 .

#### See Also

[CommonCModule.FunctionName](commoncmodule-functionname.html)

[CommonCModule.LoadPrototypeFromCodeTemplate](commoncmodule-loadprototypefromcodetemplate.html)

[CommonCModule.ModulePath](commoncmodule-modulepath.html)

[CommonCModule.UpdatePrototypeFromSource](commoncmodule-updateprototypefromsource.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Obsolete CommonCModule Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncmodule-loadprototypefromcodetemplate.html language=enus -->
## TOPIC 00373: CommonCModule.LoadPrototypeFromCodeTemplate

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncmodule-loadprototypefromcodetemplate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncmodule-loadprototypefromcodetemplate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCModule.LoadPrototypeFromCodeTemplate Return Value Boolean Returns True if this method modifies the step. Purpose Updates the parameters of the module to match the prototype and parameter values of the code template the CommonCModule.CodeTemplateName property specifies. Remarks This met

### CommonCModule.LoadPrototypeFromCodeTemplate

#### Syntax

[CommonCModule](commoncmodule.html).LoadPrototypeFromCodeTemplate

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if this method modifies the step.

#### Purpose

Updates the parameters of the module to match the prototype and parameter values of the code template the
 [CommonCModule.CodeTemplateName](commoncmodule-codetemplatename.html)
 property specifies.

#### Remarks

This method does nothing if the
 CommonCModule.CodeTemplateName
 property is empty.

For adapters that use Microsoft Visual Studio, calling this method can result in prompts to the user if any of the following conditions exist:

- Multiple versions of Visual Studio exist on the computer and you select the
 Always Prompt for Version 
 option from the Version of Visual Studio to Use for Create and Edit Code ring control in the
 Adapter Configuration 
 dialog box.
- Multiple versions of Visual Studio exist on the computer and you select the
 Use the Version that Matches the Project File 
 option from the Version of Visual Studio to Use for Create and Edit Code ring control in the Adapter Configuration dialog box, and TestStand cannot match the version of the file.

#### See Also

[Adapter Configuration dialog box](../tsref/adapter-configuration-dialog-box.html)

[CommonCModule.CodeTemplateName](commoncmodule-codetemplatename.html)

[CVIModule.Parameters](cvimodule-parameters.html)

[DllModule.Parameters](dllmodule-parameters.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncmodule-modulepath.html language=enus -->
## TOPIC 00374: CommonCModule.ModulePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncmodule-modulepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncmodule-modulepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCModule.ModulePath Data Type String Purpose Specifies the pathname of the code module file that contains the function the step calls. You can specify an absolute or relative pathname for the module file. Relative pathnames are relative to the TestStand search directory paths . See Also

### CommonCModule.ModulePath

#### Syntax

[CommonCModule](commoncmodule.html).ModulePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the pathname of the code module file that contains the function the step calls. You can specify an absolute or relative pathname for the module file. Relative pathnames are relative to the TestStand
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### See Also

[CommonCModule.FunctionName](commoncmodule-functionname.html)

[CVIModule.ModuleType](cvimodule-moduletype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncmodule-projectfilepath.html language=enus -->
## TOPIC 00375: CommonCModule.ProjectFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncmodule-projectfilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncmodule-projectfilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCModule.ProjectFilePath Data Type String Purpose Specifies the name of the Microsoft Visual Studio or LabWindows/CVI project used to create the code module. Remarks TestStand uses this property when you create or edit source code for this module using the Module.CreateCode or Module.Edi

### CommonCModule.ProjectFilePath

#### Syntax

[CommonCModule](commoncmodule.html).ProjectFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the name of the Microsoft Visual Studio or LabWindows/CVI project used to create the code module.

#### Remarks

TestStand uses this property when you create or edit source code for this module using the
 [Module.CreateCode](module-createcode.html)
 or
 [Module.EditCode](module-editcode.html)
 methods.

#### See Also

[CommonCModule.ModulePath](commoncmodule-modulepath.html)

[CommonCModule.SourceFilePath](commoncmodule-sourcefilepath.html)

[CommonCModule.WorkspaceFilePath](commoncmodule-workspacefilepath.html)

[Module.CreateCode](module-createcode.html)

[Module.EditCode](module-editcode.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncmodule-sourcefilepath.html language=enus -->
## TOPIC 00376: CommonCModule.SourceFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncmodule-sourcefilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncmodule-sourcefilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCModule.SourceFilePath Data Type String Purpose Specifies the pathname of the source file. If you want to create a new source file, you must enter an absolute pathname. If you are using an existing source file, you can enter an absolute or relative pathname. Relative pathnames are relat

### CommonCModule.SourceFilePath

#### Syntax

[CommonCModule](commoncmodule.html).SourceFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the pathname of the source file. If you want to create a new source file, you must enter an absolute pathname. If you are using an existing source file, you can enter an absolute or relative pathname. Relative pathnames are relative to the TestStand
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### Remarks

You can specify the source file to generate the source code for the function, edit the source code, and resolve differences between the parameter list in the source code and the parameter information. You do not have to specify the source file for TestStand to call the step code module.

#### See Also

[CommonCModule.ProjectFilePath](commoncmodule-projectfilepath.html)

[CommonCModule.WorkspaceFilePath](commoncmodule-workspacefilepath.html)

[Module.CreateCode](module-createcode.html)

[Module.EditCode](module-editcode.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncmodule-updateprototypefromsource.html language=enus -->
## TOPIC 00377: CommonCModule.UpdatePrototypeFromSource

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncmodule-updateprototypefromsource.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncmodule-updateprototypefromsource.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCModule.UpdatePrototypeFromSource( keepParameterValues) Purpose Call this method to update the current parameters prototype from the source code. Remarks If you update the prototype from the source code, TestStand deletes any parameters not present in the source code prototype. Paramete

### CommonCModule.UpdatePrototypeFromSource

#### Syntax

[CommonCModule](commoncmodule.html).UpdatePrototypeFromSource( keepParameterValues)

#### Purpose

Call this method to update the current parameters prototype from the source code.

#### Remarks

If you update the prototype from the source code, TestStand deletes any parameters not present in the source code prototype.

#### Parameters

keepParameterValues
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to keep the parameter values after updating the prototype from the source file.

#### See Also

[CommonCModule.VerifyPrototype](commoncmodule-verifyprototype.html)

[CommonCModule.VerifyPrototypeFromSource](commoncmodule-verifyprototypefromsource.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncmodule-verifyprototype.html language=enus -->
## TOPIC 00378: CommonCModule.VerifyPrototype

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncmodule-verifyprototype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncmodule-verifyprototype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCModule.VerifyPrototype( result) Return Value Boolean Returns True if this method modifies the module. Purpose This method checks if the prototype the source code specifies matches the currently loaded parameters. If they do not match, this method prompts you to modify the module or sou

### CommonCModule.VerifyPrototype

#### Syntax

[CommonCModule](commoncmodule.html).VerifyPrototype( result)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if this method modifies the module.

#### Purpose

This method checks if the prototype the source code specifies matches the currently loaded parameters. If they do not match, this method prompts you to modify the module or source code so that the prototypes match.

#### Parameters

result
 As
 [CommonCVerifyPrototypeResults](commoncverifyprototyperesults.html)

[Out] Returns a value that specifies the results of this method.

#### See Also

[CommonCModule.UpdatePrototypeFromSource](commoncmodule-updateprototypefromsource.html)

[CommonCModule.VerifyPrototypeFromSource](commoncmodule-verifyprototypefromsource.html)

[CommonCVerifyPrototypeResults](commoncverifyprototyperesults.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncmodule-verifyprototypefromsource.html language=enus -->
## TOPIC 00379: CommonCModule.VerifyPrototypeFromSource

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncmodule-verifyprototypefromsource.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncmodule-verifyprototypefromsource.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCModule.VerifyPrototypeFromSource Return Value Boolean Indicates that there are no conflicts. Purpose Call this method to check for conflicts between the source code and the currently loaded parameter information. This method does not prompt the user if a conflict exists See Also Common

### CommonCModule.VerifyPrototypeFromSource

#### Syntax

[CommonCModule](commoncmodule.html).VerifyPrototypeFromSource

#### Return Value

[Boolean](data-types-for-teststand.html)

Indicates that there are no conflicts.

#### Purpose

Call this method to check for conflicts between the source code and the currently loaded parameter information. This method does not prompt the user if a conflict exists

#### See Also

[CommonCModule.UpdatePrototypeFromSource](commoncmodule-updateprototypefromsource.html)

[CommonCModule.VerifyPrototype](commoncmodule-verifyprototype.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncmodule-workspacefilepath.html language=enus -->
## TOPIC 00380: CommonCModule.WorkspaceFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncmodule-workspacefilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncmodule-workspacefilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCModule.WorkspaceFilePath Data Type String Purpose Specifies the pathname of the LabWindows/CVI workspace file or Microsoft Visual Studio solution file used to create source code for this module. Remarks TestStand uses this property when you create or edit source code for this module us

### CommonCModule.WorkspaceFilePath

#### Syntax

[CommonCModule](commoncmodule.html).WorkspaceFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the pathname of the LabWindows/CVI workspace file or Microsoft Visual Studio solution file used to create source code for this module.

#### Remarks

TestStand uses this property when you create or edit source code for this module using the
 [Module.CreateCode](module-createcode.html)
 or
 [Module.EditCode](module-editcode.html)
 methods. If you do not specify a workspace file for this module, TestStand uses a default workspace.

#### See Also

[CommonCModule.ModulePath](commoncmodule-modulepath.html)

[CommonCModule.ProjectFilePath](commoncmodule-projectfilepath.html)

[CommonCModule.SourceFilePath](commoncmodule-sourcefilepath.html)

[Module.CreateCode](module-createcode.html)

[Module.EditCode](module-editcode.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncmodule.html language=enus -->
## TOPIC 00381: CommonCModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the CommonCModule class to specify and obtain common information for the LabWindows/CVI and C/C++ DLL code modules that steps or step type substeps execute. Use the Step.Module property to obtain a reference to a CommonCModule object. To access the properties and methods of a specif

### CommonCModule

Use objects from the CommonCModule class to specify and obtain common information for the LabWindows/CVI and C/C++ DLL code modules that steps or step type substeps execute. Use the
 
 [Step.Module](step-module.html)
 property to obtain a reference to a CommonCModule object. To access the properties and methods of a specific module class, query the Module object for the interface of the module-specific interface you want to acquire.

Typically, you use this class only when you are writing a sequence editor.

To access the properties and methods of the Module class, use the
 [CommonCModule.AsModule](commoncmodule-asmodule.html)
 method to obtain an object. To access the properties and methods of a specific module class, query the CommonCModule object for the interface of the module-specific interface you want to acquire.

You can use the
 
 [Module.LoadPrototype](module-loadprototype.html)
 method to load the prototype for the module the step specifies.

#### Properties

| CodeTemplateName |
| --- |
| FunctionCall (Read Only) |
| FunctionName |
| ModulePath |
| ProjectFilePath |
| SourceFilePath |
| WorkspaceFilePath |

#### Methods

| AcceptFunctionCall |
| --- |
| AsModule |
| LoadPrototypeFromCodeTemplate |
| UpdatePrototypeFromSource |
| VerifyPrototype |
| VerifyPrototypeFromSource |

#### See Also

[CVIModule](cvimodule.html)

[DllModule](dllmodule.html)

[Module](module.html)

[Module.LoadPrototype](module-loadprototype.html)

[Step.Module](step-module.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-arraydimensions.html language=enus -->
## TOPIC 00382: CommonCParameter.ArrayDimensions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-arraydimensions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-arraydimensions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.ArrayDimensions Data Type Long Purpose Specifies the number of dimensions for array parameters. See Also CommonCParameter.GetArrayDimensionSizeExpr CommonCParameter.SetArrayDimensionSizeExpr

### CommonCParameter.ArrayDimensions

#### Syntax

[CommonCParameter](commoncparameter.html).ArrayDimensions

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the number of dimensions for array parameters.

#### See Also

[CommonCParameter.GetArrayDimensionSizeExpr](commoncparameter-getarraydimensionsizeexpr.html)

[CommonCParameter.SetArrayDimensionSizeExpr](commoncparameter-setarraydimensionsizeexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-aspropertyobject.html language=enus -->
## TOPIC 00383: CommonCParameter.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the adapter. Remarks Use the PropertyObject to edit, add, or remove custom properties of the adapter. See Also PropertyObject

### CommonCParameter.AsPropertyObject

#### Syntax

[CommonCParameter](commoncparameter.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the adapter.

#### Remarks

Use the PropertyObject to edit, add, or remove custom properties of the adapter.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-displaycreatecustomdatatyped.html language=enus -->
## TOPIC 00384: CommonCParameter.DisplayCreateCustomDataTypeDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-displaycreatecustomdatatyped.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-displaycreatecustomdatatyped.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.DisplayCreateCustomDataTypeDialog( sequenceContext) Return Value Boolean Parameters sequenceContext As SequenceContext [In]

### CommonCParameter.DisplayCreateCustomDataTypeDialog

#### Syntax

[CommonCParameter](commoncparameter.html).DisplayCreateCustomDataTypeDialog( sequenceContext)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Parameters

sequenceContext
 As
 
 [SequenceContext](sequencecontext.html)

[In]

Parent topic:

Obsolete CommonCParameter Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-displayvalueexpr.html language=enus -->
## TOPIC 00385: CommonCParameter.DisplayValueExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-displayvalueexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-displayvalueexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.DisplayValueExpr Data Type String Purpose Returns the text to display for the CommonCParameter.ValueExpr property. Remarks The text of this property differs from the text of the CommonCParameter.ValueExpr property when the expression contains an enumeration constant. If you s

### CommonCParameter.DisplayValueExpr

#### Syntax

[CommonCParameter](commoncparameter.html).DisplayValueExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the text to display for the
 [CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)
 property.

#### Remarks

The text of this property differs from the text of the
 CommonCParameter.ValueExpr
 property when the expression contains an enumeration constant. If you set the
 CommonCParameter.ValueExpr
 property to an expression that contains an enumeration constant, this property is set to the expression with the constant, and the
 CommonCParameter.ValueExpr
 property is set to an expression that contains the value of the constant.

#### See Also

[CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-enumtypename.html language=enus -->
## TOPIC 00386: CommonCParameter.EnumTypeName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-enumtypename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-enumtypename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.EnumTypeName Data Type String Purpose Returns the name of the enumeration type for a parameter that is an enumeration. See Also CommonCParameter.GetEnumValues

### CommonCParameter.EnumTypeName

#### Syntax

[CommonCParameter](commoncparameter.html).EnumTypeName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the enumeration type for a parameter that is an enumeration.

#### See Also

[CommonCParameter.GetEnumValues](commoncparameter-getenumvalues.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-enumtypeparamiscompatible.html language=enus -->
## TOPIC 00387: CommonCParameter.EnumTypeParamIsCompatible

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-enumtypeparamiscompatible.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-enumtypeparamiscompatible.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.EnumTypeParamIsCompatible( enumTypeName, reasonNotCompatible) Return Value Boolean Parameters enumTypeName As String [In] reasonNotCompatible As String [Out]

### CommonCParameter.EnumTypeParamIsCompatible

#### Syntax

[CommonCParameter](commoncparameter.html).EnumTypeParamIsCompatible( enumTypeName, reasonNotCompatible)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Parameters

enumTypeName
 As
 [String](data-types-for-teststand.html)

[In]

reasonNotCompatible
 As
 [String](data-types-for-teststand.html)

[Out]

Parent topic:

Obsolete CommonCParameter Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-flags.html language=enus -->
## TOPIC 00388: CommonCParameter.Flags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-flags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-flags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.Flags Data Type Long Purpose Specifies certain attributes for the parameter, such as whether TestStand sets the Error.Code property of the step to the return value or parameter value the argument returns. Refer to CommonCParameterFlags for all the possible values. See Also Co

### CommonCParameter.Flags

#### Syntax

[CommonCParameter](commoncparameter.html).Flags

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies certain attributes for the parameter, such as whether TestStand sets the
 Error.Code
 property of the step to the return value or parameter value the argument returns. Refer to
 [CommonCParameterFlags](commoncparameterflags.html)
 for all the possible values.

#### See Also

[CommonCParameter.ResultAction](commoncparameter-resultaction.html)

[CommonCParameterFlags](commoncparameterflags.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-getarraydimensionsize.html language=enus -->
## TOPIC 00389: CommonCParameter.GetArrayDimensionSize

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-getarraydimensionsize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-getarraydimensionsize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.GetArrayDimensionSize( dimension) Return Value Long Purpose This property is obsolete. Use the CommonCParameter.GetArrayDimensionSizeExpr method instead. Remarks Returns the value of the CommonCParameter.GetArrayDimensionSizeExpr method if the expression is a numeric value; o

### CommonCParameter.GetArrayDimensionSize

#### Syntax

[CommonCParameter](commoncparameter.html).GetArrayDimensionSize( dimension)

#### Return Value

[Long](data-types-for-teststand.html)

#### Purpose

Note

CommonCParameter.GetArrayDimensionSizeExpr

#### Remarks

Returns the value of the
 CommonCParameter.GetArrayDimensionSizeExpr
 method if the expression is a numeric value; otherwise TestStand throws an exception.

#### Parameters

dimension
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index corresponding to one of the array dimensions.

#### See Also

[CommonCParameter.GetArrayDimensionSizeExpr](commoncparameter-getarraydimensionsizeexpr.html)

[CommonCParameter.SetArrayDimensionSize](commoncparameter-setarraydimensionsize.html)

[CVIParameter.Category](cviparameter-category.html)

[DllParameter.Category](dllparameter-category.html)

Parent topic:

Obsolete CommonCParameter Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-getarraydimensionsizeexpr.html language=enus -->
## TOPIC 00390: CommonCParameter.GetArrayDimensionSizeExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-getarraydimensionsizeexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-getarraydimensionsizeexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.GetArrayDimensionSizeExpr( dimension) Return Value String Purpose Returns an expression that determines the size of the array corresponding to the zero-based index passed as input. Parameters dimension As Long [In] Specifies the zero-based index corresponding to one of the ar

### CommonCParameter.GetArrayDimensionSizeExpr

#### Syntax

[CommonCParameter](commoncparameter.html).GetArrayDimensionSizeExpr( dimension)

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns an expression that determines the size of the array corresponding to the zero-based index passed as input.

#### Parameters

dimension
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index corresponding to one of the array dimensions.

#### See Also

[CommonCParameter.SetArrayDimensionSizeExpr](commoncparameter-setarraydimensionsizeexpr.html)

[CVIParameter.Category](cviparameter-category.html)

[DllParameter.Category](dllparameter-category.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-getdescription.html language=enus -->
## TOPIC 00391: CommonCParameter.GetDescription

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-getdescription.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-getdescription.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.GetDescription Return Value String Purpose Returns the parameter description. Remarks This property corresponds to the short description of the parameter type using C++ syntax. See Also CommonCParameter.ParameterName

### CommonCParameter.GetDescription

#### Syntax

[CommonCParameter](commoncparameter.html).GetDescription

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns the parameter description.

#### Remarks

This property corresponds to the short description of the parameter type using C++ syntax.

#### See Also

[CommonCParameter.ParameterName](commoncparameter-parametername.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-getdllinfotype.html language=enus -->
## TOPIC 00392: CommonCParameter.GetDllInfoType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-getdllinfotype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-getdllinfotype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.GetDllInfoType Return Value DllInfoTypes Use the following constants with this data type: DllInfoType_Enumeration –(Value: 1) DllInfoType_None –(Value: 0) DllInfoType_Struct –(Value: 2)

### CommonCParameter.GetDllInfoType

#### Syntax

[CommonCParameter](commoncparameter.html).GetDllInfoType

#### Return Value

[DllInfoTypes](dllinfotypes.html)

Use the following constants with this data type:

- DllInfoType_Enumeration 
 –(Value: 1)
- DllInfoType_None 
 –(Value: 0)
- DllInfoType_Struct 
 –(Value: 2)

Parent topic:

Obsolete CommonCParameter Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-getenumvalues.html language=enus -->
## TOPIC 00393: CommonCParameter.GetEnumValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-getenumvalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-getenumvalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.GetEnumValues Return Value Object Array Returns an array of property objects where each property object represents an enumeration value. Purpose Returns the enumeration constants for a parameter that is an enumeration. Remarks The property objects in the array this method ret

### CommonCParameter.GetEnumValues

#### Syntax

[CommonCParameter](commoncparameter.html).GetEnumValues

#### Return Value

[Object Array](data-types-for-teststand.html)

Returns an array of property objects where each property object represents an enumeration value.

#### Purpose

Returns the enumeration constants for a parameter that is an enumeration.

#### Remarks

The property objects in the array this method returns have a name and value that corresponds to the name and value of the enumeration constant.

Pass the return value of this method as the
 additionalConstants
 parameter of
 [Expression.ValidateEvaluationType](expression-validateevaluationtype.html)
 when checking the
 [CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)
 property for errors.

If you are using an ExpressionEdit control to specify the
 CommonCParameter.ValueExpr
 property, pass the return value of this method to
 
 [ExpressionEdit.SetAdditionalEvaluationConstants](../tsuiref/expressionedit-setadditionalevaluationconstan.html)
 to direct the ExpressionEdit control to recognize the enumeration constants.

#### See Also

[CommonCParameter.EnumTypeName](commoncparameter-enumtypename.html)

[CommonCParameter.ValidEvaluationTypes](commoncparameter-validevaluationtypes.html)

[CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[ExpressionEdit.SetAdditionalEvaluationConstants](../tsuiref/expressionedit-setadditionalevaluationconstan.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-numerictypeparamiscompatible.html language=enus -->
## TOPIC 00394: CommonCParameter.NumericTypeParamIsCompatible

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-numerictypeparamiscompatible.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-numerictypeparamiscompatible.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.NumericTypeParamIsCompatible( numericTypeName, reasonNotCompatible) Return Value Boolean Parameters numericTypeName As String [In] reasonNotCompatible As String [Out]

### CommonCParameter.NumericTypeParamIsCompatible

#### Syntax

[CommonCParameter](commoncparameter.html).NumericTypeParamIsCompatible( numericTypeName, reasonNotCompatible)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Parameters

numericTypeName
 As
 [String](data-types-for-teststand.html)

[In]

reasonNotCompatible
 As
 [String](data-types-for-teststand.html)

[Out]

Parent topic:

Obsolete CommonCParameter Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-parametername.html language=enus -->
## TOPIC 00395: CommonCParameter.ParameterName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-parametername.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-parametername.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.ParameterName Data Type String Purpose Returns the symbolic name for the parameter. See Also CommonCParameter.ValueExpr

### CommonCParameter.ParameterName

#### Syntax

[CommonCParameter](commoncparameter.html).ParameterName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the symbolic name for the parameter.

#### See Also

[CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-pass.html language=enus -->
## TOPIC 00396: CommonCParameter.Pass

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-pass.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-pass.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.Pass Data Type CommonCParameterPassOptions Use the following constants with this data type: CParamPass_ByConstPointer –(Value: 0x41) Passes a pointer to a constant value. CParamPass_ByConstReference –(Value: 0x50) Passes a reference to a constant value. CParamPass_ByPointer –

### CommonCParameter.Pass

#### Syntax

[CommonCParameter](commoncparameter.html).Pass

#### Data Type

[CommonCParameterPassOptions](commoncparameterpassoptions.html)

Use the following constants with this data type:

- CParamPass_ByConstPointer 
 –(Value: 0x41) Passes a pointer to a constant value.
- CParamPass_ByConstReference 
 –(Value: 0x50) Passes a reference to a constant value.
- CParamPass_ByPointer 
 –(Value: 1) Passes a pointer to a modifiable value.
- CParamPass_ByReference 
 –(Value: 0x10) Passes a reference to a modifiable value.
- CParamPass_ByVal 
 –(Value: 0) Passes a copy of the value.

#### Purpose

Specifies how to pass the value specified in the argument expression property,
 [CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)
 , to the specific function. Use the
 [CommonCParameter.PassArrayElementBy](commoncparameter-passarrayelementby.html)
 property to specify how to pass structure elements of an array parameter.

#### Remarks

This option is not used for string or array parameters.

The
 CParamPass_ByConstPointer
 and
 CParamPass_ByConstReference
 values are valid only for parameters that have the Category set to one of the
 [C++ classes](../tsref/c-class-parameters-c-c-dll-call-parameters.html)

The
 CParamPass_ByReference
 value is valid only for C/C++ DLL module parameters.

#### See Also

[C++ classes](../tsref/c-class-parameters-c-c-dll-call-parameters.html)

[CommonCParameter.PassArrayElementBy](commoncparameter-passarrayelementby.html)

[CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-passarrayelementby.html language=enus -->
## TOPIC 00397: CommonCParameter.PassArrayElementBy

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-passarrayelementby.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-passarrayelementby.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.PassArrayElementBy Data Type CommonCParameterPassOptions Use the following constants with this data type: CParamPass_ByConstPointer –(Value: 0x41) Passes a pointer to a constant value. CParamPass_ByConstReference –(Value: 0x50) Passes a reference to a constant value. CParamPa

### CommonCParameter.PassArrayElementBy

#### Syntax

[CommonCParameter](commoncparameter.html).PassArrayElementBy

#### Data Type

[CommonCParameterPassOptions](commoncparameterpassoptions.html)

Use the following constants with this data type:

- CParamPass_ByConstPointer 
 –(Value: 0x41) Passes a pointer to a constant value.
- CParamPass_ByConstReference 
 –(Value: 0x50) Passes a reference to a constant value.
- CParamPass_ByPointer 
 –(Value: 1) Passes a pointer to a modifiable value.
- CParamPass_ByReference 
 –(Value: 0x10) Passes a reference to a modifiable value.
- CParamPass_ByVal 
 –(Value: 0) Passes a copy of the value.

#### Purpose

Specifies how to pass structures in arrays. Valid values are
 CParamPass_ByPointer
 and
 CParamPass_ByVal
 .

#### See Also

[CommonCParameter.Pass](commoncparameter-pass.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-resultaction.html language=enus -->
## TOPIC 00398: CommonCParameter.ResultAction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-resultaction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-resultaction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.ResultAction Data Type CommonCParameterResultActions Use the following constants with this data type: CParamResult_NoAction –(Value: 0) Specifies to ignore the return value. CParamResult_SetErrorIfNegative –(Value: 1) Specifies to set the error state of the step if the return

### CommonCParameter.ResultAction

#### Syntax

[CommonCParameter](commoncparameter.html).ResultAction

#### Data Type

[CommonCParameterResultActions](commoncparameterresultactions.html)

Use the following constants with this data type:

- CParamResult_NoAction 
 –(Value: 0) Specifies to ignore the return value.
- CParamResult_SetErrorIfNegative 
 –(Value: 1) Specifies to set the error state of the step if the return value is less than zero.
- CParamResult_SetErrorIfNotZero 
 –(Value: 4) Specifies to set the error state of the step if the return value is not zero.
- CParamResult_SetErrorIfPositive 
 –(Value: 2) Specifies to set the error state of the step if the return value is greater than zero.
- CParamResult_SetErrorIfZero 
 –(Value: 3) Specifies to set the error state of the step if the return value is equal to zero.

#### Purpose

Specifies whether TestStand sets the
 Error.Occurred
 property of the step to
 True
 when the return value or parameter value after the call is greater than zero, less than zero, equal to zero, or not equal to zero.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-setarraydimensionsize.html language=enus -->
## TOPIC 00399: CommonCParameter.SetArrayDimensionSize

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-setarraydimensionsize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-setarraydimensionsize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.SetArrayDimensionSize( dimension, arrayDimensionSize) Purpose This property is obsolete. Use the CommonCParameter.SetArrayDimensionSizeExpr method instead. Remarks Specifies the size of the array corresponding to the zero-based index passed as an input. TestStand assigns this

### CommonCParameter.SetArrayDimensionSize

#### Syntax

[CommonCParameter](commoncparameter.html).SetArrayDimensionSize( dimension, arrayDimensionSize)

#### Purpose

Note

CommonCParameter.SetArrayDimensionSizeExpr

#### Remarks

Specifies the size of the array corresponding to the zero-based index passed as an input. TestStand assigns this value to the
 CommonCParameter.SetArrayDimensionSizeExpr
 property.

#### Parameters

dimension
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index corresponding to one of the array dimensions.

arrayDimensionSize
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the dimension size.

#### See Also

[CommonCParameter.GetArrayDimensionSize](commoncparameter-getarraydimensionsize.html)

[CommonCParameter.SetArrayDimensionSizeExpr](commoncparameter-setarraydimensionsizeexpr.html)

Parent topic:

Obsolete CommonCParameter Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-setarraydimensionsizeexpr.html language=enus -->
## TOPIC 00400: CommonCParameter.SetArrayDimensionSizeExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-setarraydimensionsizeexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-setarraydimensionsizeexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.SetArrayDimensionSizeExpr( dimension, arrayDimensionSizeExpr) Purpose Specifies an expression that determines the size of the array corresponding to the zero-based index passed as an input. Parameters dimension As Long [In] Specifies the zero-based index corresponding to one

### CommonCParameter.SetArrayDimensionSizeExpr

#### Syntax

[CommonCParameter](commoncparameter.html).SetArrayDimensionSizeExpr( dimension, arrayDimensionSizeExpr)

#### Purpose

Specifies an expression that determines the size of the array corresponding to the zero-based index passed as an input.

#### Parameters

dimension
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index corresponding to one of the array dimensions.

arrayDimensionSizeExpr
 As
 [String](data-types-for-teststand.html)

[In] Specifies the dimension size.

#### See Also

[CVIParameter.Category](cviparameter-category.html)

[DllParameter.Category](dllparameter-category.html)

[GetArrayDimensionSizeExpr](commoncparameter-getarraydimensionsizeexpr.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-stringbuffersize.html language=enus -->
## TOPIC 00401: CommonCParameter.StringBufferSize

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-stringbuffersize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-stringbuffersize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.StringBufferSize Data Type Long Purpose This property is obsolete. Use the CommonCParameter.StringBufferSizeExpr property instead. Remarks Specifies the buffer size for a string parameter. TestStand assigns this value to the CommonCParameter.StringBufferSizeExpr property. Whe

### CommonCParameter.StringBufferSize

#### Syntax

[CommonCParameter](commoncparameter.html).StringBufferSize

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Note

CommonCParameter.StringBufferSizeExpr

#### Remarks

Specifies the buffer size for a string parameter. TestStand assigns this value to the
 CommonCParameter.StringBufferSizeExpr
 property. When you use this property, TestStand returns the value stored in the
 CommonCParameter.StringBufferSizeExpr
 property if the expression is a numeric value; otherwise TestStand throws an exception.

#### See Also

[CommonCParameter.StringBufferSizeExpr](commoncparameter-stringbuffersizeexpr.html)

Parent topic:

Obsolete CommonCParameter Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-stringbuffersizeexpr.html language=enus -->
## TOPIC 00402: CommonCParameter.StringBufferSizeExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-stringbuffersizeexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-stringbuffersizeexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.StringBufferSizeExpr Data Type String Purpose Specifies an expression that determines the buffer size for a string parameter. When you specify one of the string buffer types as the parameter type, the adapter copies the contents of the string argument and a trailing zero elem

### CommonCParameter.StringBufferSizeExpr

#### Syntax

[CommonCParameter](commoncparameter.html).StringBufferSizeExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an expression that determines the buffer size for a string parameter. When you specify one of the string buffer types as the parameter type, the adapter copies the contents of the string argument and a trailing zero element into a temporary buffer before calling the function. Specify the minimum size of the temporary buffer using this property.

#### Remarks

If the string value is longer than the buffer size you specify, the adapter resizes the temporary buffer so it is large enough to hold the contents of the string argument and the trailing zero element. After the function returns, TestStand copies the value the function writes into the temporary buffer back to the string argument.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-structtype.html language=enus -->
## TOPIC 00403: CommonCParameter.StructType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-structtype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-structtype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.StructType Data Type String Purpose Specifies the name of the type used when the category of a parameter is a C structure argument or a TestStand object. Remarks If you specify DllParamCategory_CStruct or DllParamCategory_CStructArray for the DllParameter.Category property or

### CommonCParameter.StructType

#### Syntax

[CommonCParameter](commoncparameter.html).StructType

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the name of the type used when the category of a parameter is a C structure argument or a TestStand object.

#### Remarks

If you specify
 DllParamCategory_CStruct
 or
 DllParamCategory_CStructArray
 for the
 [DllParameter.Category](dllparameter-category.html)
 property or
 CVIParamCategory_CStruct
 or
 CVIParamCategory_CStructArray
 for the
 [CVIParameter.Category](cviparameter-category.html)
 property, you can pass variables and properties you create with named data types to function parameters that accept structures. When you create or edit a data type, specify if the type can be a C structure argument and how the type represents itself in memory when you pass it to a structure parameter.

If you specify
 DllParamCategory_TSObject
 for the
 [DllParameter.Category](dllparameter-category.html)
 property, you can pass objects from the TestStand ActiveX API to function parameters that accept object references.

#### See Also

[CVIParameter.Category](cviparameter-category.html)

[CVIParameter.Type](cviparameter-type.html)

[DllParameter.Category](dllparameter-category.html)

[DllParameter.Type](dllparameter-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-unknowninfo.html language=enus -->
## TOPIC 00404: CommonCParameter.UnknownInfo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-unknowninfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-unknowninfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.UnknownInfo Data Type CommonCParameterUnknownInfoFlags Purpose Specifies what part of the parameter information is unknown based on the category and type. Remarks You can have unknown information when you load a prototype from a module that does not contain enough information

### CommonCParameter.UnknownInfo

#### Syntax

[CommonCParameter](commoncparameter.html).UnknownInfo

#### Data Type

[CommonCParameterUnknownInfoFlags](commoncparameterunknowninfoflags.html)

#### Purpose

Specifies what part of the parameter information is unknown based on the category and type.

#### Remarks

You can have unknown information when you load a prototype from a module that does not contain enough information to determine the exact category and type of the specific parameter.

#### See Also

[CommonCParameterUnknownInfoFlags](commoncparameterunknowninfoflags.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-userdata.html language=enus -->
## TOPIC 00405: CommonCParameter.UserData

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-userdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-userdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.UserData Data Type PropertyObject Purpose Holds a data item you associate with the parameter object. Remarks Typically, you do not use this property. See Also PropertyObject

### CommonCParameter.UserData

#### Syntax

[CommonCParameter](commoncparameter.html).UserData

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

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-validevaluationtypes.html language=enus -->
## TOPIC 00406: CommonCParameter.ValidEvaluationTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-validevaluationtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-validevaluationtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.ValidEvaluationTypes Data Type EvaluationTypes Purpose Returns the valid types to which this parameter can evaluate. Remarks You can pass the value of this property to the validEvaluationTypes parameter of the Expression.ValidateEvaluationType method to determine whether the

### CommonCParameter.ValidEvaluationTypes

#### Syntax

[CommonCParameter](commoncparameter.html).ValidEvaluationTypes

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
 [CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)
 property contains errors.

If you are using an ExpressionEdit control to display the value of the
 CommonCParameter.ValueExpr
 property, pass the value of this property to the
 
 [ExpressionEdit.SetValidEvaluationTypes](../tsuiref/expressionedit-setvalidevaluationtypes.html)
 method.

#### See Also

[CommonCParameter.GetEnumValues](commoncparameter-getenumvalues.html)

[CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)

[EvaluationTypes](evaluationtypes.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[ExpressionEdit.GetValidEvaluationTypes](../tsuiref/expressionedit-getvalidevaluationtypes.html)

[ExpressionEdit.SetValidEvaluationTypes](../tsuiref/expressionedit-setvalidevaluationtypes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-valueexpr.html language=enus -->
## TOPIC 00407: CommonCParameter.ValueExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-valueexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-valueexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.ValueExpr Data Type String Purpose Specifies the argument expression. Remarks If the parameter is an input, this expression corresponds to the value to pass. If the parameter is an output, this expression specifies where to store the result value. See Also CommonCParameter.Pa

### CommonCParameter.ValueExpr

#### Syntax

[CommonCParameter](commoncparameter.html).ValueExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the argument expression.

#### Remarks

If the parameter is an input, this expression corresponds to the value to pass. If the parameter is an output, this expression specifies where to store the result value.

#### See Also

[CommonCParameter.ParameterName](commoncparameter-parametername.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-valueexprisignored.html language=enus -->
## TOPIC 00408: CommonCParameter.ValueExprIsIgnored

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-valueexprisignored.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-valueexprisignored.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.ValueExprIsIgnored Data Type Boolean Purpose Use this property to determine whether the adapter ignores the argument value expression when it calls the module. The LabWindows/CVI and C/C++ DLL Adapters ignore the value expression for the parameter that corresponds to the retu

### CommonCParameter.ValueExprIsIgnored

#### Syntax

[CommonCParameter](commoncparameter.html).ValueExprIsIgnored

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Use this property to determine whether the adapter ignores the argument value expression when it calls the module. The LabWindows/CVI and C/C++ DLL Adapters ignore the value expression for the parameter that corresponds to the return value of a void function.

#### See Also

[CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)

[CommonCParameter.ValueExprIsOptional](commoncparameter-valueexprisoptional.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter-valueexprisoptional.html language=enus -->
## TOPIC 00409: CommonCParameter.ValueExprIsOptional

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter-valueexprisoptional.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter-valueexprisoptional.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommonCParameter.ValueExprIsOptional Data Type Boolean Purpose Use this property to determine whether the argument value expression is optional. You do not have to specify an optional value expression to call the module successfully. Value expressions for return values are optional. See Also

### CommonCParameter.ValueExprIsOptional

#### Syntax

[CommonCParameter](commoncparameter.html).ValueExprIsOptional

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Use this property to determine whether the argument value expression is optional. You do not have to specify an optional value expression to call the module successfully. Value expressions for return values are optional.

#### See Also

[CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)

[CommonCParameter.ValueExprIsIgnored](commoncparameter-valueexprisignored.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameter.html language=enus -->
## TOPIC 00410: CommonCParameter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the CommonCParameter class to configure and obtain common parameter information for a CVIParameter or DllParameter object. To access the properties and methods of a specific parameter class, query the CommonCParameter object for the interface of the parameter-specific interface you

### CommonCParameter

Use objects from the CommonCParameter class to configure and obtain common parameter information for a CVIParameter or DllParameter object.

To access the properties and methods of a specific parameter class, query the CommonCParameter object for the interface of the parameter-specific interface you want.

#### Properties

| ArrayDimensions |
| --- |
| DisplayValueExpr (Read Only) |
| EnumTypeName (Read Only) |
| Flags |
| ParameterName |
| Pass |
| PassArrayElementBy |
| ResultAction |
| StringBufferSizeExpr |
| StructType |
| UnknownInfo |
| UserData (Read Only) |
| ValidEvaluationTypes (Read Only) |
| ValueExpr |
| ValueExprIsIgnored (Read Only) |
| ValueExprIsOptional (Read Only) |

#### Methods

| AsPropertyObject |
| --- |
| GetArrayDimensionSizeExpr |
| GetDescription |
| GetEnumValues |
| SetArrayDimensionSizeExpr |

#### See Also

[CVIParameter](cviparameter.html)

[DllParameter](dllparameter.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameterflags.html language=enus -->
## TOPIC 00411: CommonCParameterFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameterflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameterflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following constant with the CommonCParameter.Flags property to specify what action to take when the code module returns a value. A value of zero indicates that no flags are set. CParamFlags_SetErrorCodeToReturnValue –(Value: 1) Specifies to assign the return value of the parameter to the Err

### CommonCParameterFlags

Use the following constant with the
 [CommonCParameter.Flags](commoncparameter-flags.html)
 property to specify what action to take when the code module returns a value. A value of zero indicates that no flags are set.

- CParamFlags_SetErrorCodeToReturnValue 
 –(Value: 1) Specifies to assign the return value of the parameter to the
 Error.Code 
 property of the currently executing step. This flag is valid only for return values and numeric parameters passed by pointer or reference.

#### See Also

[CommonCParameter.Flags](commoncparameter-flags.html)

[CommonCParameter.ResultAction](commoncparameter-resultaction.html)

Parent topic:

Adapter API-Related Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameterpassoptions.html language=enus -->
## TOPIC 00412: CommonCParameterPassOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameterpassoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameterpassoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the CommonCParameter.Pass property and the paramPass parameter of CVIParameters.New and DllParameters.New methods to specify how to pass the parameter. CParamPass_ByConstPointer –(Value: 0x41) Passes a pointer to a constant value. CParamPass_ByConstReference –(Value: 0x50) P

### CommonCParameterPassOptions

Use these constants with the
 [CommonCParameter.Pass](commoncparameter-pass.html)
 property and the
 paramPass
 parameter of
 [CVIParameters.New](cviparameters-new.html)
 and
 [DllParameters.New](dllparameters-new.html)
 methods to specify how to pass the parameter.

- CParamPass_ByConstPointer 
 –(Value: 0x41) Passes a pointer to a constant value.
- CParamPass_ByConstReference 
 –(Value: 0x50) Passes a reference to a constant value.
- CParamPass_ByPointer 
 –(Value: 1) Passes a pointer to a modifiable value.
- CParamPass_ByReference 
 –(Value: 0x10) Passes a reference to a modifiable value.
- CParamPass_ByVal 
 –(Value: 0) Passes a copy of the value.

#### See Also

[CommonCParameter.Pass](commoncparameter-pass.html)

[CVIParameters.New](cviparameters-new.html)

[DllParameters.New](dllparameters-new.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameterresultactions.html language=enus -->
## TOPIC 00413: CommonCParameterResultActions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameterresultactions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameterresultactions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following constants with the CommonCParameter.ResultAction property to specify what action to take when the code module returns a value. This property is valid only for return values and numeric parameters you pass by pointer. CParamResult_NoAction –(Value: 0) Specifies to ignore the return

### CommonCParameterResultActions

Use the following constants with the
 [CommonCParameter.ResultAction](commoncparameter-resultaction.html)
 property to specify what action to take when the code module returns a value. This property is valid only for return values and numeric parameters you pass by pointer.

- CParamResult_NoAction 
 –(Value: 0) Specifies to ignore the return value.
- CParamResult_SetErrorIfNegative 
 –(Value: 1) Specifies to set the error state of the step if the return value is less than zero.
- CParamResult_SetErrorIfNotZero 
 –(Value: 4) Specifies to set the error state of the step if the return value is not zero.
- CParamResult_SetErrorIfPositive 
 –(Value: 2) Specifies to set the error state of the step if the return value is greater than zero.
- CParamResult_SetErrorIfZero 
 –(Value: 3) Specifies to set the error state of the step if the return value is equal to zero.

#### See Also

[CommonCParameter.ResultAction](commoncparameter-resultaction.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparametertypes.html language=enus -->
## TOPIC 00414: CommonCParameterTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparametertypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparametertypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following constants with the CVIParameter.Type and DllParameter.Type properties to specify the parameters data type, or as the parameterType parameter of the CVIParameters.New and DllParameters.New methods. When you get or set the parameter data type, also get or set the category with the CV

### CommonCParameterTypes

Use the following constants with the
 [CVIParameter.Type](cviparameter-type.html)
 and
 [DllParameter.Type](dllparameter-type.html)
 properties to specify the parameters data type, or as the
 parameterType
 parameter of the
 [CVIParameters.New](cviparameters-new.html)
 and
 [DllParameters.New](dllparameters-new.html)
 methods. When you get or set the parameter data type, also get or set the category with the
 [CVIParameter.Category](cviparameter-category.html)
 or
 [DllParameter.Category](dllparameter-category.html)
 properties, or set the
 parameterCategory
 parameter of the
 CVIParameters.New
 and
 DllParameters.New
 methods.

- CParamType_CString 
 –(Value: 0x20) Specifies that the parameter is a C-style string, such as a pointer to an array of single-byte characters. Ensure the code module does not modify the value of a string parameter of this type.
- CParamType_CStringBuffer 
 –(Value: 0x22) Specifies that the parameter is a C-style string buffer, such as a pointer to a modifiable array of single-byte characters. The code module can also modify the value of a string parameter of this type.
- CParamType_CVIHandle 
 –(Value: 0x41) Specifies that the parameter is an ActiveX reference passed as a CVI CAObjHandle.
- CParamType_Float32 
 –(Value: 6) Specifies that the parameter is a 32-bit floating-point number.
- CParamType_Float64 
 –(Value: 7) Specifies that the parameter is a 64-bit floating-point number.
- CParamType_IDispatch 
 –(Value: 0x40) Specifies that the parameter is a pointer to an ActiveX dispatch interface.
- CParamType_Int16 
 –(Value: 2) Specifies that the parameter is a 16-bit integer.
- CParamType_Int32 
 –(Value: 4) Specifies that the parameter is a 32-bit integer.
- CParamType_Int64 
 –(Value: 8) Specifies that the parameter is a 64-bit integer.
- CParamType_Int8 
 –(Value: 0) Specifies that the parameter is an 8-bit integer.
- CParamType_IUnknown 
 –(Value: 0x42) Specifies that the parameter is a pointer to an ActiveX IUnknown interface.
- CParamType_NotUsed 
 –(Value: 200) Specifies that no data type is associated with the category of the parameter. Refer to
 CVIParameterCategories 
 and
 DllParameterCategories 
 for more information about category descriptions.
- CParamType_UInt16 
 –(Value: 3) Specifies that the parameter is a 16-bit unsigned integer.
- CParamType_UInt32 
 –(Value: 5) Specifies that the parameter is a 32-bit unsigned integer.
- CParamType_UInt64 
 –(Value: 9) Specifies that the parameter is a 64-bit unsigned integer.
- CParamType_UInt8 
 –(Value: 1) Specifies that the parameter is an 8-bit unsigned integer.
- CParamType_UnicodeString 
 –(Value: 0x21) Specifies that the parameter is a C-style, wide character string buffer, such as a pointer to an array of double-byte characters. Ensure the code module does not modify the value of a string parameter of this type.
- CParamType_UnicodeStringBuffer 
 –(Value: 0x23) Specifies that the parameter is a C-style, wide character string buffer, such as a pointer to a modifiable array of dual-byte characters. The code module can also modify the value of a string parameter of this type.

#### See Also

[CVIParameterCategories](cviparametercategories.html)

[CVIParameter.Category](cviparameter-category.html)

[CVIParameter.Type](cviparameter-type.html)

[CVIParameters.New](cviparameters-new.html)

[DllParameterCategories](dllparametercategories.html)

[DllParameter.Category](dllparameter-category.html)

[DllParameter.Type](dllparameter-type.html)

[DllParameters.New](dllparameters-new.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncparameterunknowninfoflags.html language=enus -->
## TOPIC 00415: CommonCParameterUnknownInfoFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncparameterunknowninfoflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncparameterunknowninfoflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The CommonCParameter.UnknownInfo property returns one or more of the following constants to indicate how much information TestStand was able to acquire about the parameter when reading the module information from a DLL exports table or a type library: CParamInfo_DontKnowFirstDimensionSize –(Value: 3

### CommonCParameterUnknownInfoFlags

The
 [CommonCParameter.UnknownInfo](commoncparameter-unknowninfo.html)
 property returns one or more of the following constants to indicate how much information TestStand was able to acquire about the parameter when reading the module information from a DLL exports table or a type library:

- CParamInfo_DontKnowFirstDimensionSize 
 –(Value: 3) Indicates that TestStand could not determine how large the first dimension was for an array parameter.
- CParamInfo_DontKnowIfArrayOrPointer 
 –(Value: 2) Indicates that TestStand could not determine whether the parameter was an array or pointer.
- CParamInfo_DontKnowNumElements 
 –(Value: 1) Indicates that TestStand could not determine the number of elements in the array parameter.
- CParamInfo_EveryThingKnown 
 –(Value: 0) Indicates that TestStand could determine the required information about the parameter.

#### See Also

[CommonCParameter.UnknownInfo](commoncparameter-unknowninfo.html)

Parent topic:

Adapter API-Related Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commoncverifyprototyperesults.html language=enus -->
## TOPIC 00416: CommonCVerifyPrototypeResults

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commoncverifyprototyperesults.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commoncverifyprototyperesults.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the result parameter the CommonCModule.VerifyPrototype method returns. CommonCVerifyPrototypeResult_ModuleUpdated –(Value: 1) Specifies that the CommonCModule.VerifyPrototype method modified the currently loaded parameters to match the prototype the source code specifies. Co

### CommonCVerifyPrototypeResults

Use these constants with the
 result
 parameter the
 [CommonCModule.VerifyPrototype](commoncmodule-verifyprototype.html)
 method returns.

- CommonCVerifyPrototypeResult_ModuleUpdated 
 –(Value: 1) Specifies that the
 CommonCModule.VerifyPrototype 
 method modified the currently loaded parameters to match the prototype the source code specifies.
- CommonCVerifyPrototypeResult_PrototypesMatch 
 –(Value: 0) Specifies that the prototype the source code specifies matches the currently loaded parameters.
- CommonCVerifyPrototypeResult_SourceUpdated 
 –(Value: 2) Specifies that the
 CommonCModule.VerifyPrototype 
 method modified the source code to match the prototype the currently loaded parameters specify.
- CommonCVerifyPrototypeResult_UserCancelled 
 –(Value: 3) Specifies that the
 CommonCModule.VerifyPrototype 
 method prompted the user to update the module or source code, but the user cancelled the dialog box.

#### See Also

[CommonCModule.VerifyPrototype](commoncmodule-verifyprototype.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/commondialogoptions.html language=enus -->
## TOPIC 00417: CommonDialogOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/commondialogoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/commondialogoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the values you can use with the dlgOptions parameter of several methods that display dialog boxes. Use the bitwise-OR operator to specify more than one option. CommonDlgOption_DisableGotoLocation –(Value: 0x80000) Use this option to specify that if the error message contain

### CommonDialogOptions

These constants represent the values you can use with the
 dlgOptions
 parameter of several methods that display dialog boxes. Use the bitwise-OR operator to specify more than one option.

- CommonDlgOption_DisableGotoLocation 
 –(Value: 0x80000) Use this option to specify that if the error message contains location information, the dialog does not offer the user the option to go to the location.
- CommonDlgOption_ModalToAppMainWind 
 –(Value: 0x10000) By default, the dialog box is modal to the last active window of the calling thread, or if none exists, to the last active window from AppMainHwnd. If you enable this option, the dialog box is modal with respect to the window handle the
 Engine.AppMainHwnd 
 property returns. Typically, you do not need to set this option.
- CommonDlgOption_NoOptions 
 –(Value: 0x0) No options.
- CommonDlgOption_ReadOnly 
 –(Value: 0x20000) Use this option to create a read-only version of the dialog box.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/copylocationsoptions.html language=enus -->
## TOPIC 00418: CopyLocationsOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/copylocationsoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/copylocationsoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the Locations.AddLocations method. CopyLocationsOption_DeepCopy –(Value: 2) Specifies that the Locations.AddLocations method adds a copy of the locations you pass to the collection. CopyLocationsOption_ShallowCopy –(Value: 1) Specifies that the Locations.AddLocations method

### CopyLocationsOptions

Use these constants with the
 [Locations.AddLocations](locations-addlocations.html)
 method.

- CopyLocationsOption_DeepCopy 
 –(Value: 2) Specifies that the
 Locations.AddLocations 
 method adds a copy of the locations you pass to the collection.
- CopyLocationsOption_ShallowCopy 
 –(Value: 1) Specifies that the
 Locations.AddLocations 
 method adds the locations you pass to the collection without making a copy of the locations.

#### See Also

[Locations.AddLocations](locations-addlocations.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/core-api-constants.html language=enus -->
## TOPIC 00419: Core API Constants

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/core-api-constants.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/core-api-constants.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains information about each TestStand core API constant.

### Core API Constants

This book contains information about each TestStand core API constant.

Parent topic:

API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/core-api-enumerations.html language=enus -->
## TOPIC 00420: Core API Enumerations

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/core-api-enumerations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/core-api-enumerations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains information about each TestStand core API enumeration.

### Core API Enumerations

This book contains information about each TestStand core API enumeration.

Parent topic:

API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cpuaffinityfornewthreadoptions.html language=enus -->
## TOPIC 00421: CPUAffinityForNewThreadOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cpuaffinityfornewthreadoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cpuaffinityfornewthreadoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this enumeration to specify the CPUs on which a new thread executes. CPUAffinityForNewThreadOption_UseAffinityOfCaller –(Value: 1) Specifies to use the CPU affinity of the calling sequence as the CPU affinity of the new thread. CPUAffinityForNewThreadOption_UseAllCPUs –(Value: 2) Specifies to us

### CPUAffinityForNewThreadOptions

Use this enumeration to specify the CPUs on which a new thread executes.

- CPUAffinityForNewThreadOption_UseAffinityOfCaller 
 –(Value: 1) Specifies to use the CPU affinity of the calling sequence as the CPU affinity of the new thread.
- CPUAffinityForNewThreadOption_UseAllCPUs 
 –(Value: 2) Specifies to use all CPUs available to the process as the CPU affinity of the new thread.
- CPUAffinityForNewThreadOption_UseCustomAffinity 
 –(Value: 3) Specifies to use an expression to determine the CPU affinity of the new thread.
- CPUAffinityForNewThreadOption_UseStationOption 
 –(Value: 0) Specifies to use the
 StationOptions.DefaultCPUAffinityForThreadsEx 
 property as the CPU affinity of the new thread.

#### See Also

[SequenceCallModule.CPUAffinityForNewThreadOption](sequencecallmodule-cpuaffinityfornewthreadopt.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/crashcallbackoptions.html language=enus -->
## TOPIC 00422: CrashCallbackOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/crashcallbackoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/crashcallbackoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options for the Engine.RegisterSequenceToExecuteOnCrash method. CrashCallbackOption_NoOptions –(Value: 0x0) No options. CrashCallbackOption_PreloadFile –(Value: 0x1) Load the sequence file while registering for crash recovery callback. See Also Engine.RegisterSequenceTo

### CrashCallbackOptions

These constants represent the options for the
 Engine.RegisterSequenceToExecuteOnCrash
 method.

- CrashCallbackOption_NoOptions 
 –(Value: 0x0) No options.
- CrashCallbackOption_PreloadFile 
 –(Value: 0x1) Load the sequence file while registering for crash recovery callback.

#### See Also

[Engine.RegisterSequenceToExecuteOnCrash](engine-registersequencetoexecuteoncrash.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/createundoitemoptions.html language=enus -->
## TOPIC 00423: CreateUndoItemOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/createundoitemoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/createundoitemoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the UndoItemCreator.CreateAndPostUndoItem method. CreateUndoItemOption_CreateOnly –(Value: 0x1): Use this option to prevent the UndoItemCreator.CreateAndPostUndoItem method from sending the created undo item to the sequence editor. CreateUndoItemOption_NoOptions –(Value: 0x0

### CreateUndoItemOptions

Use these constants with the
 [UndoItemCreator.CreateAndPostUndoItem](undoitemcreator-createandpostundoitem.html)
 method.

- CreateUndoItemOption_CreateOnly 
 –(Value: 0x1): Use this option to prevent the
 UndoItemCreator.CreateAndPostUndoItem 
 method from sending the created undo item to the sequence editor.
- CreateUndoItemOption_NoOptions 
 –(Value: 0x0): No options.

#### See Also

[UndoItemCreator.CreateAndPostUndoItem](undoitemcreator-createandpostundoitem.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileinputrecordstream-close.html language=enus -->
## TOPIC 00424: CsvFileInputRecordStream.Close

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileinputrecordstream-close.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileinputrecordstream-close.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileInputRecordStream.Close Purpose Close this InputRecordStream . Implements InputRecordStream.Close . See Also InputRecordStream.Close

### CsvFileInputRecordStream.Close

#### Syntax

[CsvFileInputRecordStream](csvfileinputrecordstream.html).Close

#### Purpose

Close this
 InputRecordStream
 . Implements
 [InputRecordStream.Close](inputrecordstream-close.html)
 .

#### See Also

[InputRecordStream.Close](inputrecordstream-close.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileinputrecordstream-fieldmapping.html language=enus -->
## TOPIC 00425: CsvFileInputRecordStream.FieldMapping

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileinputrecordstream-fieldmapping.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileinputrecordstream-fieldmapping.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileInputRecordStream.FieldMapping Data Type String Specifies which fields to read from the InputRecordStream . Purpose Specifies which fields to read from the InputRecordStream . Implements InputRecordStream.FieldMapping .

### CsvFileInputRecordStream.FieldMapping

#### Syntax

[CsvFileInputRecordStream](csvfileinputrecordstream.html).FieldMapping

#### Data Type

[String](data-types-for-teststand.html)

Specifies which fields to read from the
 InputRecordStream
 .

#### Purpose

Specifies which fields to read from the
 InputRecordStream
 . Implements
 [InputRecordStream.FieldMapping](inputrecordstream-fieldmapping.html)
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileinputrecordstream-getrecordprototype.html language=enus -->
## TOPIC 00426: CsvFileInputRecordStream.GetRecordPrototype

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileinputrecordstream-getrecordprototype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileinputrecordstream-getrecordprototype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileInputRecordStream.GetRecordPrototype( prototype, options = 0) Return Value Boolean True if there is a record prototype associated with this CsvFileInputRecordStream. Otherwise, returns false. Purpose Get the prototype associated with this CsvFileInputRecordStream . Parameters prototype

### CsvFileInputRecordStream.GetRecordPrototype

#### Syntax

[CsvFileInputRecordStream](csvfileinputrecordstream.html).GetRecordPrototype( prototype, options = 0)

#### Return Value

[Boolean](data-types-for-teststand.html)

True if there is a record prototype associated with this CsvFileInputRecordStream. Otherwise, returns false.

#### Purpose

Get the prototype associated with this
 CsvFileInputRecordStream
 .

#### Parameters

prototype
 As
 [PropertyObject](propertyobject.html)

[In/Out] A container defining the prototype for this stream. The name and type of each subproperty correspond to the name and type of the column in the CSV file with the same index as the subproperty.

options
 As
 [Long](data-types-for-teststand.html)

[In] This parameter is reserved for future use.

This parameter has a default value of
 0
 .

#### See Also

[SetRecordPrototype](csvfileinputrecordstream-setrecordprototype.html)

[ReadRecordPrototype](csvfileinputrecordstream-readrecordprototype.html)

[Record Prototypes](../tsref/record-prototypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileinputrecordstream-open.html language=enus -->
## TOPIC 00427: CsvFileInputRecordStream.Open

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileinputrecordstream-open.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileinputrecordstream-open.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileInputRecordStream.Open( absolutePath) Purpose Open the file specified by the absolutePath argument, associating it with this CsvFileInputRecordStream . Remarks You will not normally need to call this method, as Engine.NewCsvFileInputRecordStream returns a stream already associated with

### CsvFileInputRecordStream.Open

#### Syntax

[CsvFileInputRecordStream](csvfileinputrecordstream.html).Open( absolutePath)

#### Purpose

Open the file specified by the absolutePath argument, associating it with this
 CsvFileInputRecordStream
 .

#### Remarks

You will not normally need to call this method, as
 Engine.NewCsvFileInputRecordStream
 returns a stream already associated with an open file. When a
 CsvFileInputRecordStream
 is no longer needed, it should be closed by calling
 CsvFileInputRecordStream.Close
 . If it is not closed already, the stream will close automatically when the last reference to it is removed.

#### Parameters

absolutePath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute path to the CSV file.

#### See Also

[InputRecordStream.Close](inputrecordstream-close.html)

[Engine.NewCsvFileInputRecordStream](engine-newcsvfileinputrecordstream.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileinputrecordstream-path.html language=enus -->
## TOPIC 00428: CsvFileInputRecordStream.Path

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileinputrecordstream-path.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileinputrecordstream-path.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileInputRecordStream.Path Data Type String The path of the CSV file associated with this stream. Purpose Get the absolute path of the CSV file associated with this CsvFileInputRecordStream . Remarks An empty string is returned if this stream is not currently associated with an open file.

### CsvFileInputRecordStream.Path

#### Syntax

[CsvFileInputRecordStream](csvfileinputrecordstream.html).Path

#### Data Type

[String](data-types-for-teststand.html)

The path of the CSV file associated with this stream.

#### Purpose

Get the absolute path of the CSV file associated with this
 CsvFileInputRecordStream
 .

#### Remarks

An empty string is returned if this stream is not currently associated with an open file. Path is set implicitly by calling
 CsvFileInputRecordStream.Open
 and cleared by calling
 CsvFileInputRecordStream.Close
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileinputrecordstream-readline.html language=enus -->
## TOPIC 00429: CsvFileInputRecordStream.ReadLine

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileinputrecordstream-readline.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileinputrecordstream-readline.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileInputRecordStream.ReadLine( lineString) Return Value Long Returns 0 if a line of text was successfully read. Returns non-zero if end of file is encountered. Purpose Read the next line of text from the underlying file. Remarks CsvFileInputRecordStream.ReadLine provides a lower level int

### CsvFileInputRecordStream.ReadLine

#### Syntax

[CsvFileInputRecordStream](csvfileinputrecordstream.html).ReadLine( lineString)

#### Return Value

[Long](data-types-for-teststand.html)

Returns
 0
 if a line of text was successfully read. Returns non-zero if end of file is encountered.

#### Purpose

Read the next line of text from the underlying file.

#### Remarks

CsvFileInputRecordStream.ReadLine
 provides a lower level interface to the underlying file than
 ReadRecord
 . The next line of text from the file is stored directly to the lineString parameter with no additional processing.

Note

CsvFileInputRecordStream.ReadLine

CsvFileInputRecordStream.ReadRecord

#### Parameters

lineString
 As
 [String](data-types-for-teststand.html)

[Out] Outputs the next line from the CSV file.

#### See Also

[CsvFileInputRecordStream.SkipLines](csvfileinputrecordstream-skiplines.html)

[CsvFileOutputRecordStream.WriteLine](csvfileoutputrecordstream-writeline.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileinputrecordstream-readrecord.html language=enus -->
## TOPIC 00430: CsvFileInputRecordStream.ReadRecord

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileinputrecordstream-readrecord.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileinputrecordstream-readrecord.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileInputRecordStream.ReadRecord( record, mapping = "") Return Value Long Returns 0 if a record was successfully read. Returns -1 if end of file was encountered before reading a record. Returns 1 if the end of a table was encountered before reading a record. Purpose Reads the next record f

### CsvFileInputRecordStream.ReadRecord

#### Syntax

[CsvFileInputRecordStream](csvfileinputrecordstream.html).ReadRecord( record, mapping = "")

#### Return Value

[Long](data-types-for-teststand.html)

Returns 0 if a record was successfully read. Returns -1 if end of file was encountered before reading a record. Returns 1 if the end of a table was encountered before reading a record.

#### Purpose

Reads the next record from the stream. Implements
 [InputRecordStream.ReadRecord](inputrecordstream-readrecord.html)
 .

#### Remarks

CsvFileInputRecordStream
 is designed to work with CSV files that contain multiple tables. Strictly speaking, such files are not compliant with RFC 4180, but many common spreadsheet applications support them regardless.

If
 CsvFileInputRecordStream.ReadRecord
 encounters an empty line or a line with nothing but separator characters, it returns
 1
 to indicate it has reached the end of the current table.
 CsvFileInputRecordStream.ReadRecord
 returns
 -1
 to indicate it has reached the end of the underlying file.

Note

CsvFileInputRecordStream

Applications that only need to read the current table do not have to be aware of end-of-table vs. end-of-file distinction, as
 InputRecordStream.ReadRecord
 defines end of file to be any non-zero return value. However, applications that are aware they are reading a
 CsvFileInputRecordStream
 can distinguish between having reached the end of the current table and the actual end of the file by checking if the return value is
 +1
 or
 -1
 .

Note

InputRecordStream

CsvFileInputRecordStream
 instances without record prototypes store data to fields in the order specified by the mapping parameter.

When the stream has a prototype, columns in the CSV file are mapped by name to fields in the record. As such, the record must be of a type that supports named fields: either a container or PropertyObject array. If the record is a container, the prototype field name determines the name of the subproperty the value in its column is stored to. If the record is an array, the prototype specifies the name of the array element(s) the value in its column is stored to. The record parameter cannot be a string or other type of array, as these types do not support named fields. Specifying a field mapping when a prototype is present results in a run-time error.

#### Parameters

record
 As
 [PropertyObject](propertyobject.html)

[In/Out] Specifies where to store the incoming record. Refer to
 InputRecordStream.ReadRecord
 for more information.

Note

mapping
 As
 [String](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies the mapping to elements (subproperties or array elements) in the record parameter from fields in the CSV file. Refer to
 InputRecordStream.ReadRecord
 for more information. Passing a non-empty field mapping to a stream that has a record prototype results in a run-time error.

#### See Also

[InputRecordStream.ReadRecord](inputrecordstream-readrecord.html)

[CsvFileInputRecordStream.SetRecordPrototype](csvfileinputrecordstream-setrecordprototype.html)

[CsvFileInputRecordStream.GetRecordPrototype](csvfileinputrecordstream-getrecordprototype.html)

[CsvFileInputRecordStream.ReadRecordPrototype](csvfileinputrecordstream-readrecordprototype.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileinputrecordstream-readrecordprototype.html language=enus -->
## TOPIC 00431: CsvFileInputRecordStream.ReadRecordPrototype

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileinputrecordstream-readrecordprototype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileinputrecordstream-readrecordprototype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileInputRecordStream.ReadRecordPrototype( prototype, options = 0) Purpose Read the record prototype from the CSV file, and set it. Parameters prototype As PropertyObject [In/Out] A container defining the prototype for this stream. The name and type of each subproperty correspond to the na

### CsvFileInputRecordStream.ReadRecordPrototype

#### Syntax

[CsvFileInputRecordStream](csvfileinputrecordstream.html).ReadRecordPrototype( prototype, options = 0)

#### Purpose

Read the record prototype from the CSV file, and set it.

#### Parameters

prototype
 As
 [PropertyObject](propertyobject.html)

[In/Out] A container defining the prototype for this stream. The name and type of each subproperty correspond to the name and type of the column in the CSV file with the same index as the subproperty.

options
 As
 [Long](data-types-for-teststand.html)

[In] This parameter is reserved for future use.

This parameter has a default value of
 0
 .

#### See Also

[SetRecordPrototype](csvfileinputrecordstream-setrecordprototype.html)

[GetRecordPrototype](csvfileinputrecordstream-getrecordprototype.html)

[Record Prototypes](../tsref/record-prototypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileinputrecordstream-readrecordto.html language=enus -->
## TOPIC 00432: CsvFileInputRecordStream.ReadRecordTo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileinputrecordstream-readrecordto.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileinputrecordstream-readrecordto.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileInputRecordStream.ReadRecordTo( context, record) Return Value Long Returns 0 if a record was successfully read. Returns -1 if end of file was encountered before reading a record. Returns 1 if the end of a table was encountered before reading a record. Purpose Read the next record from

### CsvFileInputRecordStream.ReadRecordTo

#### Syntax

[CsvFileInputRecordStream](csvfileinputrecordstream.html).ReadRecordTo( context, record)

#### Return Value

[Long](data-types-for-teststand.html)

Returns
 0
 if a record was successfully read. Returns
 -1
 if end of file was encountered before reading a record. Returns
 1
 if the end of a table was encountered before reading a record.

#### Purpose

Read the next record from this stream. Implements
 [InputRecordStream.ReadRecordTo](inputrecordstream-readrecordto.html)
 .

#### Remarks

CsvFileInputRecordStream
 is designed to work with CSV files that may contain multiple tables. Strictly speaking, such files are not compliant with RFC 4180, but many common spreadsheet applications support them regardless.

If
 CsvFileInputRecordStream.ReadRecordTo
 encounters an empty line or a line with nothing but separator characters, it returns
 1
 to indicate it has reached the end of the current table.
 CsvFileInputRecordStream.ReadRecordTo
 returns
 -1
 to indicate it has reached the end of the underlying file.

Note

CsvFileInputRecordStream

Applications that only need to read the current table do not have to be aware of end-of-table vs end-of-file distinction, as
 InputRecordStream.ReadRecordTo
 defines end of file to be any non-zero return value. However, applications that are aware they are reading a
 CsvFileInputRecordStream
 can distinguish between having reached the end of the current table and the actual end of the file by checking if the return value is
 +1
 or
 -1
 .

#### Parameters

context
 As
 [SequenceContext](sequencecontext.html)

[In] Specifies the
 SequenceContext
 against which to evaluate the lookup strings specified by the record parameter. Refer to
 [InputRecordStream.ReadRecordTo](inputrecordstream-readrecordto.html)
 for more information.

record
 As
 [String Array](data-types-for-teststand.html)

[In/Out] An array of lookup strings specifying where to store the fields from the incoming record. The lookup strings are evaluated relative to the
 SequenceContext
 specified by the context parameter. Refer to
 [InputRecordStream.ReadRecordTo](inputrecordstream-readrecordto.html)
 for more information.

#### See Also

[InputRecordStream.ReadRecordTo](inputrecordstream-readrecordto.html)

[CsvFileInputRecordStream.ReadRecord](csvfileinputrecordstream-readrecord.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileinputrecordstream-scanfortag.html language=enus -->
## TOPIC 00433: CsvFileInputRecordStream.ScanForTag

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileinputrecordstream-scanfortag.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileinputrecordstream-scanfortag.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileInputRecordStream.ScanForTag( tag, ignoreCase) Return Value Long Returns 0 if the tag was found. Returns non-zero if end of file was encountered without finding the tag. Purpose Search forward through the file for the line beginning with the specified string. Reading begins from the ne

### CsvFileInputRecordStream.ScanForTag

#### Syntax

[CsvFileInputRecordStream](csvfileinputrecordstream.html).ScanForTag( tag, ignoreCase)

#### Return Value

[Long](data-types-for-teststand.html)

Returns
 0
 if the tag was found. Returns non-zero if end of file was encountered without finding the tag.

#### Purpose

Search forward through the file for the line beginning with the specified string. Reading begins from the next line.

#### Remarks

Use
 CsvFileInputRecordStream.ScanForTag
 to search through a CSV file for a known string that indicates the location of the records you wish to read.

#### Parameters

tag
 As
 [String](data-types-for-teststand.html)

[In] The tag to search for.

ignoreCase
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether to perform case-sensitive or case-insensitive matching. Specify true to ignore case, or false to perform case-sensitive matching.

#### See Also

[CsvFileInputRecordStream.SkipLines](csvfileinputrecordstream-skiplines.html)

[CsvFileInputRecordStream.ReadLine](csvfileinputrecordstream-readline.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileinputrecordstream-separatorchar.html language=enus -->
## TOPIC 00434: CsvFileInputRecordStream.SeparatorChar

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileinputrecordstream-separatorchar.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileinputrecordstream-separatorchar.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileInputRecordStream.SeparatorChar Data Type String The separator character for the CSV file. Purpose Get or set the separator character associated with this CsvFileInputRecordStream . By default, the separator character is a "," (comma). Remarks The only separator compliant with RFC 4180

### CsvFileInputRecordStream.SeparatorChar

#### Syntax

[CsvFileInputRecordStream](csvfileinputrecordstream.html).SeparatorChar

#### Data Type

[String](data-types-for-teststand.html)

The separator character for the CSV file.

#### Purpose

Get or set the separator character associated with this
 CsvFileInputRecordStream
 . By default, the separator character is a "," (comma).

#### Remarks

Note

CsvFileInputRecordStream

Note

#### See Also

[CsvFileOutputRecordStream.SeparatorChar](csvfileoutputrecordstream-separatorchar.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileinputrecordstream-setrecordprototype.html language=enus -->
## TOPIC 00435: CsvFileInputRecordStream.SetRecordPrototype

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileinputrecordstream-setrecordprototype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileinputrecordstream-setrecordprototype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileInputRecordStream.SetRecordPrototype( prototype, mapping = "") Purpose Set the prototype associated with this CsvFileInputRecordStream . Parameters prototype As PropertyObject [In] A container defining the prototype for this stream. The name and type of each subproperty correspond to t

### CsvFileInputRecordStream.SetRecordPrototype

#### Syntax

[CsvFileInputRecordStream](csvfileinputrecordstream.html).SetRecordPrototype( prototype, mapping = "")

#### Purpose

Set the prototype associated with this
 CsvFileInputRecordStream
 .

#### Parameters

prototype
 As
 [PropertyObject](propertyobject.html)

[In] A container defining the prototype for this stream. The name and type of each subproperty correspond to the name and type of the column in the CSV file with the same index as the subproperty.

mapping
 As
 [String](data-types-for-teststand.html)

[In] Specifies the mapping from subproperties in the prototype parameter to columns in the CSV file. The mapping is a comma-separated list of index ranges. For example, "0, 3-5, 8-7" specifies that subproperties 0, 3, 4, 5, 8, and 7 of the container correspond to columns 0-5 of the CSV file. The final range in the list may be open-ended. For example, "2, 3-" indicates that subproperties 2, 3, and all subproperties beyond 3 map to columns 0, 1, 2, etc. of the CSV file. The range list may also include individual subproperty names. For example, "Temperature, Pressure, 0-1" specifies that the subproperties "Temperature" and "Pressure", then subproperties 0 and 1 define columns 0-3 of the CSV file. For convenience, you can specify an empty string to specify all subproperties of the container define the columns in order. That is, an empty string is equivalent to "0-".

This parameter has a default value of
 ""
 .

#### See Also

[GetRecordPrototype](csvfileinputrecordstream-getrecordprototype.html)

[ReadRecordPrototype](csvfileinputrecordstream-readrecordprototype.html)

[Record Prototypes](../tsref/record-prototypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileinputrecordstream-skiplines.html language=enus -->
## TOPIC 00436: CsvFileInputRecordStream.SkipLines

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileinputrecordstream-skiplines.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileinputrecordstream-skiplines.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileInputRecordStream.SkipLines( numLines) Return Value Long Returns 0 if numLines were successfully skipped. Returns non-zero if end of file is encountered before numLines could be skipped. Purpose Skip the specified number of lines. Remarks This method provides a lower level interface to

### CsvFileInputRecordStream.SkipLines

#### Syntax

[CsvFileInputRecordStream](csvfileinputrecordstream.html).SkipLines( numLines)

#### Return Value

[Long](data-types-for-teststand.html)

Returns
 0
 if numLines were successfully skipped. Returns non-zero if end of file is encountered before numLines could be skipped.

#### Purpose

Skip the specified number of lines.

#### Remarks

This method provides a lower level interface to the underlying file than
 InputRecordStream.SkipRecords
 . Lines are read from the file and discarded immediately without further processing. Unlike
 InputRecordStream.SkipRecords
 ,
 InputRecordStream.SkipLines
 has no special behavior for end of table.

#### Parameters

numLines
 As
 [Long](data-types-for-teststand.html)

[In] The number of lines to skip. A value of 0 indicates to return successfully without skipping any lines. A negative value causes a run-time error.

#### See Also

[InputRecordStream.SkipRecords](inputrecordstream-skiprecords.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileinputrecordstream-skiprecords.html language=enus -->
## TOPIC 00437: CsvFileInputRecordStream.SkipRecords

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileinputrecordstream-skiprecords.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileinputrecordstream-skiprecords.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileInputRecordStream.SkipRecords( numRecords) Return Value Long Returns 0 if numRecords were successfully skipped. Returns - 1 if end of file was encountered before numRecords were skipped. Returns 1 if the end of a table was encountered before numRecords were skipped. Purpose Skip the sp

### CsvFileInputRecordStream.SkipRecords

#### Syntax

[CsvFileInputRecordStream](csvfileinputrecordstream.html).SkipRecords( numRecords)

#### Return Value

[Long](data-types-for-teststand.html)

Returns
 0
 if
 numRecords
 were successfully skipped. Returns -
 1
 if end of file was encountered before
 numRecords
 were skipped. Returns
 1
 if the end of a table was encountered before
 numRecords
 were skipped.

#### Purpose

Skip the specified number of records. Implements
 [InputRecordStream.SkipRecords](inputrecordstream-skiprecords.html)
 .

#### Remarks

CsvFileInputRecordStream
 is designed to work with CSV files that may contain multiple tables. Strictly speaking, such files are not compliant with RFC 4180, but many common spreadsheet applications support them regardless.

If
 CsvFileInputRecordStream.SkipRecords
 encounters an empty line or a line with nothing but separator characters, it returns
 1
 to indicate it has reached the end of the current table.
 CsvFileInputRecordStream.ReadRecordTo
 returns
 -1
 to indicate it has reached the end of the underlying file.

Note

CsvFileInputRecordStream

Applications that only need to read the current table do not have to be aware of end-of-table vs end-of-file distinction, as
 InputRecordStream.SkipRecords
 defines end of file to be any non-zero return value. However, applications that are aware they are reading a
 CsvFileInputRecordStream
 can distinguish between having reached the end of the current table and the actual end of the file by checking if the return value is
 +1
 or
 -1
 .

#### Parameters

numRecords
 As
 [Long](data-types-for-teststand.html)

[In] The number of records to skip. Refer to
 [InputRecordStream.SkipRecords](inputrecordstream-skiprecords.html)
 for more information.

#### See Also

[InputRecordStream.SkipRecords](inputrecordstream-skiprecords.html)

[CsvFileInputRecordStream.SkipLines](csvfileinputrecordstream-skiplines.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileinputrecordstream.html language=enus -->
## TOPIC 00438: CsvFileInputRecordStream

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileinputrecordstream.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileinputrecordstream.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Properties FieldMapping Path (Read Only) SeparatorChar Methods Close GetRecordPrototype Open ReadLine ReadRecord ReadRecordPrototype ReadRecordTo ScanForTag SetRecordPrototype SkipLines SkipRecords

### CsvFileInputRecordStream

#### Properties

| FieldMapping |
| --- |
| Path (Read Only) |
| SeparatorChar |

#### Methods

| Close |
| --- |
| GetRecordPrototype |
| Open |
| ReadLine |
| ReadRecord |
| ReadRecordPrototype |
| ReadRecordTo |
| ScanForTag |
| SetRecordPrototype |
| SkipLines |
| SkipRecords |

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileoutputrecordstream-autoflush.html language=enus -->
## TOPIC 00439: CsvFileOutputRecordStream.AutoFlush

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileoutputrecordstream-autoflush.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileoutputrecordstream-autoflush.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileOutputRecordStream.AutoFlush Data Type Boolean True makes all write operations flush immediately. False allows this stream to buffer write operations for better performance. Purpose Set or retrieve the automatic flushing behavior of this CsvFileOutputRecordStream . Remarks If AutoFlush

### CsvFileOutputRecordStream.AutoFlush

#### Syntax

[CsvFileOutputRecordStream](csvfileoutputrecordstream.html).AutoFlush

#### Data Type

[Boolean](data-types-for-teststand.html)

True
 makes all write operations flush immediately.
 False
 allows this stream to buffer write operations for better performance.

#### Purpose

Set or retrieve the automatic flushing behavior of this
 CsvFileOutputRecordStream
 .

#### Remarks

If AutoFlush is
 false
 , this
 CsvFileOutputRecordStream
 is free to buffer data to improve performance. If AutoFlush is
 true
 , write operations (
 CsvFileOutputRecordStream.WriteRecord
 ,
 CsvFileOutputRecordStream.WriteRecordFrom
 , and
 CsvFileOutputRecordStream.WriteLine
 ) automatically flush before returning, reducing the risk of data loss in the event of a crash or other failure.

Set AutoFlush to
 true
 when it is critical that no data be lost in the event of an unexpected crash or internal error. Set AutoFlush to
 false
 to achieve better performance. By default AutoFlush is
 false
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileoutputrecordstream-close.html language=enus -->
## TOPIC 00440: CsvFileOutputRecordStream.Close

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileoutputrecordstream-close.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileoutputrecordstream-close.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileOutputRecordStream.Close Purpose Flush buffered data to the underlying device, and close the stream. Implements OutputRecordStream.Close . See Also OutputRecordStream.Close CsvFileOutputRecordStream.Flush

### CsvFileOutputRecordStream.Close

#### Syntax

[CsvFileOutputRecordStream](csvfileoutputrecordstream.html).Close

#### Purpose

Flush buffered data to the underlying device, and close the stream. Implements
 [OutputRecordStream.Close](outputrecordstream-close.html)
 .

#### See Also

[OutputRecordStream.Close](outputrecordstream-close.html)

[CsvFileOutputRecordStream.Flush](outputrecordstream-flush.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileoutputrecordstream-getstreaminfo.html language=enus -->
## TOPIC 00441: CsvFileOutputRecordStream.GetStreamInfo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileoutputrecordstream-getstreaminfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileoutputrecordstream-getstreaminfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileOutputRecordStream.GetStreamInfo( streamDescription) Return Value String The absolute path of the file associated with this CsvFileOutputRecordStream . Purpose Get descriptive information about this stream useful for displaying to the user. Implements OutputRecordStream.GetStreamInfo .

### CsvFileOutputRecordStream.GetStreamInfo

#### Syntax

[CsvFileOutputRecordStream](csvfileoutputrecordstream.html).GetStreamInfo( streamDescription)

#### Return Value

[String](data-types-for-teststand.html)

The absolute path of the file associated with this
 CsvFileOutputRecordStream
 .

#### Purpose

Get descriptive information about this stream useful for displaying to the user. Implements
 [OutputRecordStream.GetStreamInfo](outputrecordstream-getstreaminfo.html)
 .

#### Parameters

streamDescription
 As
 [String](data-types-for-teststand.html)

[Out] Outputs "CSV File Output Record Stream".

#### See Also

[OutputRecordStream.GetStreamInfo](outputrecordstream-getstreaminfo.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileoutputrecordstream-open.html language=enus -->
## TOPIC 00442: CsvFileOutputRecordStream.Open

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileoutputrecordstream-open.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileoutputrecordstream-open.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileOutputRecordStream.Open( absolutePath, openMode) Purpose Open the file specified by the absolutePath argument, associating it with this CsvFileOutputRecordStream . Remarks You will not normally need to call this method, as Engine.NewCsvFileOutputRecordStream returns a stream already as

### CsvFileOutputRecordStream.Open

#### Syntax

[CsvFileOutputRecordStream](csvfileoutputrecordstream.html).Open( absolutePath, openMode)

#### Purpose

Open the file specified by the absolutePath argument, associating it with this
 CsvFileOutputRecordStream
 .

#### Remarks

You will not normally need to call this method, as
 Engine.NewCsvFileOutputRecordStream
 returns a stream already associated with an open file. When a
 CsvFileOutputRecordStream
 is no longer needed, it should be closed by calling
 CsvFileOutputRecordStream.Close
 . If it is not closed already, the stream will close automatically when the last reference to it is removed.

#### Parameters

absolutePath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute path to the CSV file.

openMode
 As
 [Long](data-types-for-teststand.html)

[In] Specifies how to open the CSV file. Supported options include:

- FileOpenMode_NoOptions 
 - Create the file if it does not exist. Fail with a run-time error if the file exists.
- FileOpenMode_Truncate 
 - If the file exists, overwrite it deleting the previous contents. Create a new file if it does not exist.
- FileOpenMode_Append 
 - If the file exists, append to the end of it, preserving the existing contents. Create a new file if it does not exist.
- FileOpenMode_Uniquify 
 - Create a new file if it does not exist. If a file with the specified path exists, attempt to make the file name unique by appending "_" (underscore) plus a numeric suffix to the file name. For example, if "AlreadyExists.csv" already exists, "AlreadyExists_2.csv" is tried, then "AlreadyExists_3.csv", etc. until a unique name has been found. If a unique name is not found after 10000 attempts, the method fails and throws a runtime error.

#### See Also

[FileOpenModes](fileopenmodes.html)

[Engine.NewCsvFileOutputRecordStream](engine-newcsvfileoutputrecordstream.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileoutputrecordstream-path.html language=enus -->
## TOPIC 00443: CsvFileOutputRecordStream.Path

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileoutputrecordstream-path.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileoutputrecordstream-path.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileOutputRecordStream.Path Data Type String The path of the CSV file associated with this stream. Purpose Get the absolute path of the CSV file associated with this CsvFileOutputRecordStream . Remarks An empty string is returned if this stream is not currently associated with an open file

### CsvFileOutputRecordStream.Path

#### Syntax

[CsvFileOutputRecordStream](csvfileoutputrecordstream.html).Path

#### Data Type

[String](data-types-for-teststand.html)

The path of the CSV file associated with this stream.

#### Purpose

Get the absolute path of the CSV file associated with this
 CsvFileOutputRecordStream
 .

#### Remarks

An empty string is returned if this stream is not currently associated with an open file. Path is set implicitly by calling
 CsvFileOutputRecordStream.Open
 and cleared by calling
 CsvFileOutputRecordStream.Close
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileoutputrecordstream-separatorchar.html language=enus -->
## TOPIC 00444: CsvFileOutputRecordStream.SeparatorChar

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileoutputrecordstream-separatorchar.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileoutputrecordstream-separatorchar.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileOutputRecordStream.SeparatorChar Data Type String The separator character for the CSV file. Purpose Get or set the separator character associated with this CsvFileInputRecordStream . By default, the separator character is a "," (comma). Remarks CsvFileOutputRecordStream supports any si

### CsvFileOutputRecordStream.SeparatorChar

#### Syntax

[CsvFileOutputRecordStream](csvfileoutputrecordstream.html).SeparatorChar

#### Data Type

[String](data-types-for-teststand.html)

The separator character for the CSV file.

#### Purpose

Get or set the separator character associated with this
 CsvFileInputRecordStream
 . By default, the separator character is a "," (comma).

#### Remarks

CsvFileOutputRecordStream
 supports any single character besides '"' (double quote), as well as null (empty string) for the separator. However,
 CsvFileInputRecordStream
 does not support carriage return, new line, or null separator characters. While it is possible to write files using these separator characters with
 CsvFileOutputRecordStream
 ,
 CsvFileInputRecordStream
 cannot parse them. Attempting to set
 SeparatorChar
 to a string of two or more characters results in a run-time error.

Note

Note

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileoutputrecordstream-writefieldheaders.html language=enus -->
## TOPIC 00445: CsvFileOutputRecordStream.WriteFieldHeaders

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileoutputrecordstream-writefieldheaders.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileoutputrecordstream-writefieldheaders.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileOutputRecordStream.WriteFieldHeaders( fields, mapping = "") Purpose Write the field headers (i.e. column names) for your data to the underlying CSV file. Remarks WriteFieldHeaders is very similar to CsvFileOutputRecordStream.WriteRecord . The only difference is that if the specified re

### CsvFileOutputRecordStream.WriteFieldHeaders

#### Syntax

[CsvFileOutputRecordStream](csvfileoutputrecordstream.html).WriteFieldHeaders( fields, mapping = "")

#### Purpose

Write the field headers (i.e. column names) for your data to the underlying CSV file.

#### Remarks

WriteFieldHeaders is very similar to
 CsvFileOutputRecordStream.WriteRecord
 . The only difference is that if the specified record is a container, the names of the subproperties are written to the CSV file instead of the values. This makes it straightforward to completely specify records with a container.
 WriteFieldHeaders
 will also accept an array, but in this case the behavior is identical to
 CsvFileOutputRecordStream.WriteRecord
 . The values in the array specify the field headers.

#### Parameters

fields
 As
 [PropertyObject](propertyobject.html)

[In] A container or array specifying the field headers. If a container is specified, names of the subproperties specify the field headers. If an array is specified, the values of the array elements coerced to strings define the field headers.

mapping
 As
 [String](data-types-for-teststand.html)

[In] Specifies the mapping from elements (either subproperties or array elements) in the
 fields
 parameter to fields in the stream. The mapping is a comma-separated list of index ranges. For example, "
 0, 3-5, 8-7
 " specifies that elements 0, 3, 4, 5, 8, and 7 define the field headers. The final range in the list may be open-ended. For example, "
 2, 3-
 " indicates that elements 2, 3, and all elements beyond 3 define the field headers. For convenience, you may specify an empty string to specify all elements be written in order. That is, an empty string is equivalent to
 0-
 . The default value is an empty string.

This parameter has a default value of
 ""
 .

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileoutputrecordstream-writeline.html language=enus -->
## TOPIC 00446: CsvFileOutputRecordStream.WriteLine

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileoutputrecordstream-writeline.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileoutputrecordstream-writeline.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileOutputRecordStream.WriteLine( lineString) Purpose Write a line of text to the file. A line feed is appended automatically. Remarks WriteLine provides a lower level interface to the underlying file than OutputRecordStream.WriteRecord . The specified string plus a linefeed is written dir

### CsvFileOutputRecordStream.WriteLine

#### Syntax

[CsvFileOutputRecordStream](csvfileoutputrecordstream.html).WriteLine( lineString)

#### Purpose

Write a line of text to the file. A line feed is appended automatically.

#### Remarks

WriteLine
 provides a lower level interface to the underlying file than
 OutputRecordStream.WriteRecord
 . The specified string plus a linefeed is written directly to the file without further processing or escaping. Use this method to add formatting or other non-record data to the CSV file.

#### Parameters

lineString
 As
 [String](data-types-for-teststand.html)

[In] The string to write.

#### See Also

[OutputRecordStream.WriteRecord](outputrecordstream-writerecord.html)

[CsvFileInputRecordStream.ReadLine](csvfileinputrecordstream-readline.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileoutputrecordstream-writerecord.html language=enus -->
## TOPIC 00447: CsvFileOutputRecordStream.WriteRecord

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileoutputrecordstream-writerecord.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileoutputrecordstream-writerecord.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileOutputRecordStream.WriteRecord( record, mapping = "") Purpose Write a record to the CSV file. Implements OutputRecordStream.WriteRecord . Parameters record As PropertyObject [In] The record to write. Refer to OutputRecordStream.WriteRecord for more information. mapping As String [In] [

### CsvFileOutputRecordStream.WriteRecord

#### Syntax

[CsvFileOutputRecordStream](csvfileoutputrecordstream.html).WriteRecord( record, mapping = "")

#### Purpose

Write a record to the CSV file. Implements
 [OutputRecordStream.WriteRecord](outputrecordstream-writerecord.html)
 .

#### Parameters

record
 As
 [PropertyObject](propertyobject.html)

[In] The record to write. Refer to
 [OutputRecordStream.WriteRecord](outputrecordstream-writerecord.html)
 for more information.

mapping
 As
 [String](data-types-for-teststand.html)

[In] [Optional] Specifies the mapping from elements (either subproperties or array elements) in the record parameter to fields in the file. Refer to
 [OutputRecordStream.WriteRecord](outputrecordstream-writerecord.html)
 for more information.

#### See Also

[OutputRecordStream.WriteRecord](outputrecordstream-writerecord.html)

[CsvFileOutputRecordStream.WriteRecordFrom](csvfileoutputrecordstream-writerecordfrom.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileoutputrecordstream-writerecordfrom.html language=enus -->
## TOPIC 00448: CsvFileOutputRecordStream.WriteRecordFrom

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileoutputrecordstream-writerecordfrom.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileoutputrecordstream-writerecordfrom.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileOutputRecordStream.WriteRecordFrom( context, record) Purpose Write a record to the CSV file. Implements OutputRecordStream.WriteRecordFrom . Parameters context As SequenceContext [In] Specifies the SequenceContext against which to evaluate the lookup strings specified by the record par

### CsvFileOutputRecordStream.WriteRecordFrom

#### Syntax

[CsvFileOutputRecordStream](csvfileoutputrecordstream.html).WriteRecordFrom( context, record)

#### Purpose

Write a record to the CSV file. Implements
 [OutputRecordStream.WriteRecordFrom](outputrecordstream-writerecordfrom.html)
 .

#### Parameters

context
 As
 [SequenceContext](sequencecontext.html)

[In] Specifies the
 SequenceContext
 against which to evaluate the lookup strings specified by the
 record
 parameter.

record
 As
 [String Array](data-types-for-teststand.html)

[In] An array of lookup strings specifying the fields to write to the stream. The lookup strings are evaluated relative to the
 SequenceContext
 specified by the
 context
 parameter.

#### See Also

[OutputRecordStream.WriteRecord](outputrecordstream-writerecord.html)

[InputRecordStream.ReadRecordTo](inputrecordstream-readrecordto.html)

[CsvFileOutputRecordStream.WriteRecord](csvfileoutputrecordstream-writerecord.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileoutputrecordstream-writerecordprototyp.html language=enus -->
## TOPIC 00449: CsvFileOutputRecordStream.WriteRecordPrototype

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileoutputrecordstream-writerecordprototyp.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileoutputrecordstream-writerecordprototyp.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CsvFileOutputRecordStream.WriteRecordPrototype( prototype, mapping = "") Purpose Write the specified prototype to the CSV file. Parameters prototype As PropertyObject [In] A container or PropertyObject array defining the prototype for this stream. The name and type of each subproperty or arra

### CsvFileOutputRecordStream.WriteRecordPrototype

#### Syntax

[CsvFileOutputRecordStream](csvfileoutputrecordstream.html).WriteRecordPrototype( prototype, mapping = "")

#### Purpose

Write the specified prototype to the CSV file.

#### Parameters

prototype
 As
 [PropertyObject](propertyobject.html)

[In] A container or
 PropertyObject
 array defining the prototype for this stream. The name and type of each subproperty or array element define to the name and type of the column in the CSV file with the corresponding index.

mapping
 As
 [String](data-types-for-teststand.html)

[In] Specifies the mapping from fields in the prototype parameter to columns in the CSV file. The mapping is a comma-separated list of index ranges. For example, "0, 3-5, 8-7" specifies that fields 0, 3, 4, 5, 8, and 7 of the container correspond to columns 0-5 of the CSV file. The final range in the list may be open-ended. For example, "2, 3-" indicates that fields 2, 3, and all fields beyond 3 map to columns 0, 1, 2, etc. of the CSV file. The range list may also include individual subproperty or array element names. For example, "Temperature, Pressure, 0-1" specifies that the subproperties or array elements named "Temperature" and "Pressure", followed by those with indices 0 and 1 define columns 0-3 of the CSV file. For convenience, you can specify an empty string to specify all fields from the prototype parameter define the columns in order. That is, an empty string is equivalent to "0-".

This parameter has a default value of
 ""
 .

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/csvfileoutputrecordstream.html language=enus -->
## TOPIC 00450: CsvFileOutputRecordStream

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/csvfileoutputrecordstream.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/csvfileoutputrecordstream.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Properties AutoFlush Path (Read Only) SeparatorChar Methods Close Flush GetStreamInfo Open WriteFieldHeaders WriteLine WriteRecord WriteRecordFrom WriteRecordPrototype

### CsvFileOutputRecordStream

#### Properties

| AutoFlush |
| --- |
| Path (Read Only) |
| SeparatorChar |

#### Methods

| Close |
| --- |
| Flush |
| GetStreamInfo |
| Open |
| WriteFieldHeaders |
| WriteLine |
| WriteRecord |
| WriteRecordFrom |
| WriteRecordPrototype |

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/custompoststepuimsgoptions.html language=enus -->
## TOPIC 00451: CustomPostStepUIMsgOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/custompoststepuimsgoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/custompoststepuimsgoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the values you can use with the CustomUIMessageOptions parameter of the Execution.AddPostStepCustomUIMessage method. Use the bitwise-OR operator to specify more than one option. CustomUIMsgOptions_AppliesToAllThreads –(Value: 2) Use this flag to send custom user interface m

### CustomPostStepUIMsgOptions

These constants represent the values you can use with the
 CustomUIMessageOptions
 parameter of the
 [Execution.AddPostStepCustomUIMessage](execution-addpoststepcustomuimessage.html)
 method. Use the bitwise-OR operator to specify more than one option.

- CustomUIMsgOptions_AppliesToAllThreads 
 –(Value: 2) Use this flag to send custom user interface message to all threads this execution creates. Otherwise, only the foreground thread of the execution sends this message.
- CustomUIMsgOptions_NoOptions 
 –(Value: 0) No options.
- CustomUIMsgOptions_SuppressIfTraceSent 
 –(Value: 1) When this flag is set, TestStand does not send a user interface message if a
 UIMsg_Trace 
 message is sent. Do not use this option if you want the UIMessage sent even when tracing is disabled.

#### See Also

[Execution.AddPostStepCustomUIMessage](execution-addpoststepcustomuimessage.html)

[Execution.RemovePostStepCustomUIMessage](execution-removepoststepcustomuimessage.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviadapter-asadapter.html language=enus -->
## TOPIC 00452: CVIAdapter.AsAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviadapter-asadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviadapter-asadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIAdapter.AsAdapter Return Value Adapter Purpose Returns the underlying module Adapter object that represents the LabWindows/CVI Adapter. Remarks Use the adapter to access properties and methods common to all adapters. See Also Adapter CVIAdapter.AsCommonCAdapter

### CVIAdapter.AsAdapter

#### Syntax

[CVIAdapter](cviadapter.html).AsAdapter

#### Return Value

[Adapter](adapter.html)

#### Purpose

Returns the underlying module Adapter object that represents the LabWindows/CVI Adapter.

#### Remarks

Use the adapter to access properties and methods common to all adapters.

#### See Also

[Adapter](adapter.html)

[CVIAdapter.AsCommonCAdapter](cviadapter-ascommoncadapter.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviadapter-ascommoncadapter.html language=enus -->
## TOPIC 00453: CVIAdapter.AsCommonCAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviadapter-ascommoncadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviadapter-ascommoncadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIAdapter.AsCommonCAdapter Return Value CommonCAdapter Purpose Returns the underlying CommonCAdapter object that represents the LabWindows/CVI Adapter. Remarks Use the CommonCAdapter object to access properties and methods common to all adapters derived from this class. See Also CommonCAdapt

### CVIAdapter.AsCommonCAdapter

#### Syntax

[CVIAdapter](cviadapter.html).AsCommonCAdapter

#### Return Value

[CommonCAdapter](commoncadapter.html)

#### Purpose

Returns the underlying CommonCAdapter object that represents the LabWindows/CVI Adapter.

#### Remarks

Use the CommonCAdapter object to access properties and methods common to all adapters derived from this class.

#### See Also

[CommonCAdapter](commoncadapter.html)

[CVIAdapter.AsAdapter](cviadapter-asadapter.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviadapter-codetemplatepolicy.html language=enus -->
## TOPIC 00454: CVIAdapter.CodeTemplatePolicy

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviadapter-codetemplatepolicy.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviadapter-codetemplatepolicy.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIAdapter.CodeTemplatePolicy Data Type AdapterCodeTemplatePolicies Use the following constants with this data type: AdapterCodeTemplatePolicy_UseNewAndLegacy –(Value: 2) Specifies that the adapter searches for new and legacy code templates. AdapterCodeTemplatePolicy_UseOnlyLegacy –(Value: 1)

### CVIAdapter.CodeTemplatePolicy

#### Syntax

[CVIAdapter](cviadapter.html).CodeTemplatePolicy

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

Specifies which code templates to use during code creation. You can choose to use new templates, legacy templates, or both new and legacy templates.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviadapter-executestepsinexternalinstance.html language=enus -->
## TOPIC 00455: CVIAdapter.ExecuteStepsInExternalInstance

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviadapter-executestepsinexternalinstance.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviadapter-executestepsinexternalinstance.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIAdapter.ExecuteStepsInExternalInstance Data Type Boolean Purpose You can specify the test execution mode as in-process or out-of-process for the LabWindows/CVI Adapter. When the adapter runs tests in-process, it executes them in the same process as the sequence editor or the user interface

### CVIAdapter.ExecuteStepsInExternalInstance

#### Syntax

[CVIAdapter](cviadapter.html).ExecuteStepsInExternalInstance

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

You can specify the test execution mode as in-process or out-of-process for the LabWindows/CVI Adapter. When the adapter runs tests in-process, it executes them in the same process as the sequence editor or the user interface you are running. When the adapter runs tests out-of-process, it executes them in an external instance of the LabWindows/CVI development environment.

If this property is
 True
 , the tests run out-of-process. If the property is
 False
 , the tests run in-process.

#### Remarks

When you execute code modules in the same process as the sequence editor or user interface, the adapter loads and runs code modules directly without using the LabWindows/CVI development environment.

#### See Also

[CVIAdapter.ExecutionServerProjectPathName](cviadapter-executionserverprojectpathname.html)

[CVIModule.AlwaysRunInProcess](cvimodule-alwaysruninprocess.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviadapter-executionserverprojectpathname.html language=enus -->
## TOPIC 00456: CVIAdapter.ExecutionServerProjectPathName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviadapter-executionserverprojectpathname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviadapter-executionserverprojectpathname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIAdapter.ExecutionServerProjectPathName Data Type String Purpose The LabWindows/CVI Adapter can launch two different copies of LabWindows/CVI. The adapter uses one copy to execute test modules. By default, the adapter opens <TestStand> \AdapterSupport\CVI\tscvirun.prj in the copy of LabWind

### CVIAdapter.ExecutionServerProjectPathName

#### Syntax

[CVIAdapter](cviadapter.html).ExecutionServerProjectPathName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

The LabWindows/CVI Adapter can launch two different copies of LabWindows/CVI.

The adapter uses one copy to execute test modules. By default, the adapter opens
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \AdapterSupport\CVI\tscvirun.prj
 in the copy of LabWindows/CVI that is executing the code modules. You can use the
 [LabWindows/CVI Adapter Configuration](../tsref/labwindows-cvi-adapter-configuration-dialog-b.html)
 dialog box to change which project the adapter uses to run code modules.

The adapter uses the other copy of LabWindows/CVI to allow you to edit the projects you use to create DLLs, static libraries, and object files.

#### Remarks

When you execute code modules in the same process as the sequence editor or user interface, the adapter loads and runs code modules directly without using the LabWindows/CVI development environment.

#### See Also

[CVIAdapter.ExecuteStepsInExternalInstance](cviadapter-executestepsinexternalinstance.html)

[LabWindows/CVI Adapter Configuration dialog box](../tsref/labwindows-cvi-adapter-configuration-dialog-b.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviadapter-newmodule.html language=enus -->
## TOPIC 00457: CVIAdapter.NewModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviadapter-newmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviadapter-newmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIAdapter.NewModule Return Value CVIModule Purpose Creates and returns a new CVIModule object. Use this method to create a CVIModule object that you can execute without using a step, sequence, or execution. See Also CVIModule CVIModule.Execute CVIParameters.NewArguments

### CVIAdapter.NewModule

#### Syntax

[CVIAdapter](cviadapter.html).NewModule

#### Return Value

[CVIModule](cvimodule.html)

#### Purpose

Creates and returns a new
 [CVIModule](cvimodule.html)
 object. Use this method to create a
 CVIModule
 object that you can execute without using a step, sequence, or execution.

#### See Also

[CVIModule](cvimodule.html)

[CVIModule.Execute](cvimodule-execute.html)

[CVIParameters.NewArguments](cviparameters-newarguments.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviadapter.html language=enus -->
## TOPIC 00458: CVIAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the CVIAdapter class to configure and obtain LabWindows/CVI Adapter-specific information about the module adapter. Call the Engine.GetAdapter or Engine.GetAdapterByKeyName method to obtain a reference to the adapter object. To access the properties and methods of the Adapter class,

### CVIAdapter

Use objects from the CVIAdapter class to configure and obtain LabWindows/CVI Adapter-specific information about the module adapter. Call the
 
 [Engine.GetAdapter](engine-getadapter.html)
 or
 
 [Engine.GetAdapterByKeyName](engine-getadapterbykeyname.html)
 method to obtain a reference to the adapter object.

To access the properties and methods of the Adapter class, use the
 [CVIAdapter.AsAdapter](cviadapter-asadapter.html)
 method to obtain an object.

#### Properties

| CodeTemplatePolicy |
| --- |
| ExecuteStepsInExternalInstance |
| ExecutionServerProjectPathName |

#### Methods

| AsAdapter |
| --- |
| AsCommonCAdapter |
| NewModule |

#### See Also

[Adapter](adapter.html)

[CommonCAdapter](commoncadapter.html)

[Engine.GetAdapter](engine-getadapter.html)

[Engine.GetAdapterByKeyName](engine-getadapterbykeyname.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviargument-value.html language=enus -->
## TOPIC 00459: CVIArgument.Value

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviargument-value.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviargument-value.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIArgument.Value Data Type PropertyObject Purpose Specifies the argument value to pass for the corresponding parameter. Remarks When you pass a CVIArguments collection to the CVIModule.Execute function, the adapter passes this property to the function instead of evaluating the CommonCParamet

### CVIArgument.Value

#### Syntax

[CVIArgument](cviargument.html).Value

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Specifies the argument value to pass for the corresponding parameter.

#### Remarks

When you pass a
 [CVIArguments](cviarguments.html)
 collection to the
 [CVIModule.Execute](cvimodule-execute.html)
 function, the adapter passes this property to the function instead of evaluating the
 [CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)
 expression.

#### See Also

[CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)

[CVIArguments](cviarguments.html)

[CVIModule.Execute](cvimodule-execute.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviargument.html language=enus -->
## TOPIC 00460: CVIArgument

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviargument.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviargument.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the CVIArgument class to set the argument value to pass to a LabWindows/CVI module function using the CVIModule.Execute method. Property Value See Also CVIArguments CVIModule.Execute

### CVIArgument

Use objects from the
 CVIArgument
 class to set the argument value to pass to a LabWindows/CVI module function using the
 [CVIModule.Execute](cvimodule-execute.html)
 method.

#### Property

| Value |
| --- |

#### See Also

[CVIArguments](cviarguments.html)

[CVIModule.Execute](cvimodule-execute.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviarguments-count.html language=enus -->
## TOPIC 00461: CVIArguments.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviarguments-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviarguments-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIArguments.Count Data Type Long Purpose Returns the number of items in the collection.

### CVIArguments.Count

#### Syntax

[CVIArguments](cviarguments.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviarguments-item.html language=enus -->
## TOPIC 00462: CVIArguments.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviarguments-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviarguments-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIArguments.Item( index) Data Type CVIArgument Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the item to retrieve. An argument at a specific index in the CVIArguments collection corresponds

### CVIArguments.Item

#### Syntax

[CVIArguments](cviarguments.html).Item( index)

#### Data Type

[CVIArgument](cviargument.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve. An argument at a specific index in the
 [CVIArguments](cviarguments.html)
 collection corresponds to the parameter at the same index in the
 [CVIParameters](cviparameters.html)
 collection that you used to create the
 CVIArguments
 collection.

#### See Also

[CVIArgument](cviargument.html)

[CVIArguments](cviarguments.html)

[CVIParameters](cviparameters.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviarguments.html language=enus -->
## TOPIC 00463: CVIArguments

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviarguments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviarguments.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the CVIArguments class to pass specific argument values to a LabWindows/CVI module function using the CVIModule.Execute method. Use the CVIParameters.NewArguments method to create a new arguments collection. Properties Count (Read Only) Item (Read Only) See Also CVIModule.Execute CV

### CVIArguments

Use objects from the
 CVIArguments
 class to pass specific argument values to a LabWindows/CVI module function using the
 [CVIModule.Execute](cvimodule-execute.html)
 method. Use the
 [CVIParameters.NewArguments](cviparameters-newarguments.html)
 method to create a new arguments collection.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[CVIModule.Execute](cvimodule-execute.html)

[CVIParameters.NewArguments](cviparameters-newarguments.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cvimodule-allowprojectfilewhenselectingmodule.html language=enus -->
## TOPIC 00464: CVIModule.AllowProjectFileWhenSelectingModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cvimodule-allowprojectfilewhenselectingmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cvimodule-allowprojectfilewhenselectingmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIModule.AllowProjectFileWhenSelectingModule Return Value Boolean Returns True if the active version of LabWindows/CVI provides support for CVIModule.GetModulePathFromProject . Otherwise, returns False . Purpose Checks if the active version of LabWindows/CVI provides support for CVIModule.Ge

### CVIModule.AllowProjectFileWhenSelectingModule

#### Syntax

[CVIModule](cvimodule.html).AllowProjectFileWhenSelectingModule

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the active version of LabWindows/CVI provides support for
 CVIModule.GetModulePathFromProject
 . Otherwise, returns
 False
 .

#### Purpose

Checks if the active version of LabWindows/CVI provides support for
 CVIModule.GetModulePathFromProject
 .

#### Remarks

This method requires LabWindows/CVI 2017 SP1 or later.

#### See Also

[CVIModule.GetModulePathFromProject](cvimodule-getmodulepathfromproject.html)

[CVIModule.GetProjectFilePathFromDll](cvimodule-getprojectfilepathfromdll.html)

[CVIModule.GetSourceFilePathFromDll](cvimodule-getsourcefilepathfromdll.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cvimodule-alwaysruninprocess.html language=enus -->
## TOPIC 00465: CVIModule.AlwaysRunInProcess

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cvimodule-alwaysruninprocess.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cvimodule-alwaysruninprocess.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIModule.AlwaysRunInProcess Data Type Boolean Purpose If the value of this property is True , the step always runs in-process even when the LabWindows/CVI Adapter is configured to run out-of-process. See Also CVIAdapter.ExecuteStepsInExternalInstance

### CVIModule.AlwaysRunInProcess

#### Syntax

[CVIModule](cvimodule.html).AlwaysRunInProcess

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

If the value of this property is
 True
 , the step always runs in-process even when the LabWindows/CVI Adapter is configured to run out-of-process.

#### See Also

[CVIAdapter.ExecuteStepsInExternalInstance](cviadapter-executestepsinexternalinstance.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cvimodule-ascommoncmodule.html language=enus -->
## TOPIC 00466: CVIModule.AsCommonCModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cvimodule-ascommoncmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cvimodule-ascommoncmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIModule.AsCommonCModule Return Value CommonCModule Purpose Returns the underlying CommonCModule that represents the CVIModule. Remarks Use the CommonCModule object to access properties and methods common to all modules derived from this class. See Also CommonCModule Module

### CVIModule.AsCommonCModule

#### Syntax

[CVIModule](cvimodule.html).AsCommonCModule

#### Return Value

[CommonCModule](commoncmodule.html)

#### Purpose

Returns the underlying CommonCModule that represents the CVIModule.

#### Remarks

Use the CommonCModule object to access properties and methods common to all modules derived from this class.

#### See Also

[CommonCModule](commoncmodule.html)

[Module](module.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cvimodule-execute.html language=enus -->
## TOPIC 00467: CVIModule.Execute

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cvimodule-execute.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cvimodule-execute.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIModule.Execute( sequenceContextParam, argumentsParam) Purpose Use this method to call a LabWindows/CVI module function directly without using a step, sequence, or execution. Remarks When you call a LabWindows/CVI module function using this method you can evaluate the parameter expressions

### CVIModule.Execute

#### Syntax

[CVIModule](cvimodule.html).Execute( sequenceContextParam, argumentsParam)

#### Purpose

Use this method to call a LabWindows/CVI module function directly without using a step, sequence, or execution.

#### Remarks

When you call a LabWindows/CVI module function using this method you can evaluate the parameter expressions to determine the argument values or specify the argument values directly using a
 [CVIArguments](cviarguments.html)
 collection.

To use the parameter value expressions, pass a valid
 [SequenceContext](sequencecontext.html)
 object to the
 sequenceContextParam
 to use to evaluate the
 [CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)
 expressions.

To pass specific argument values, use the
 [CVIParameters.NewArguments](cviparameters-newarguments.html)
 method to create a collection of
 [CVIArgument](cviargument.html)
 objects and set the
 [CVIArgument.Value](cviargument-value.html)
 property on each item in the collection.

#### Parameters

sequenceContextParam
 As
 
 [SequenceContext](sequencecontext.html)

[In] Specifies the
 SequenceContext
 object that this method uses to evaluate each of the
 CommonCParameter.ValueExpr
 expressions in the module parameters. Pass
 NULL
 for this parameter if you pass a
 CVIArguments
 collection to the
 argumentsParam
 parameter.

argumentsParam
 As
 [CVIArguments](cviarguments.html)

[In] Specifies the argument collection that contains the argument values to pass to the function. Pass
 NULL
 for this parameter to pass the values obtained from evaluating each of the
 CommonCParameter.ValueExpr
 expressions in the module parameters.

#### See Also

[CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)

[CVIArgument](cviargument.html)

[CVIArgument.Value](cviargument-value.html)

[CVIArguments](cviarguments.html)

[CVIParameters.NewArguments](cviparameters-newarguments.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cvimodule-getmodulepathfromproject.html language=enus -->
## TOPIC 00468: CVIModule.GetModulePathFromProject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cvimodule-getmodulepathfromproject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cvimodule-getmodulepathfromproject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIModule.GetModulePathFromProject( projectPathParam, options, modulePathParam) Return Value Boolean Returns True upon success. Otherwise, returns False . Purpose Returns the absolute path of the code module built by the specified LabWindows/CVI project. Remarks This method requires LabWindow

### CVIModule.GetModulePathFromProject

#### Syntax

[CVIModule](cvimodule.html).GetModulePathFromProject( projectPathParam, options, modulePathParam)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 upon success. Otherwise, returns
 False
 .

#### Purpose

Returns the absolute path of the code module built by the specified LabWindows/CVI project.

#### Remarks

This method requires LabWindows/CVI 2017 SP1 or later.

#### Parameters

projectPathParam
 As
 [String](data-types-for-teststand.html)

[In] The absolute path of the LabWindows/CVI project (
 .prj
 ) file.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies
 GetModuleFromProjectOptions
 :

- GetModuleFromProjectOption_NoOptions 
 –(Value: 0x0) No options.
- GetModuleFromProjectOption_NoPrompts 
 –(Value: 0x1) Suppress prompts.

modulePathParam
 As
 [String](data-types-for-teststand.html)

[Out] The absolute path of the target file (usually a DLL) for the specified project.

#### See Also

[CVIModule.AllowProjectFileWhenSelectingModule](cvimodule-allowprojectfilewhenselectingmodule.html)

[CVIModule.GetProjectFilePathFromDll](cvimodule-getprojectfilepathfromdll.html)

[CVIModule.GetSourceFilePathFromDll](cvimodule-getsourcefilepathfromdll.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cvimodule-getprojectfilepathfromdll.html language=enus -->
## TOPIC 00469: CVIModule.GetProjectFilePathFromDll

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cvimodule-getprojectfilepathfromdll.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cvimodule-getprojectfilepathfromdll.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIModule.GetProjectFilePathFromDll( dllPath, projectPathParam) Return Value Boolean Returns True upon success. Otherwise, returns False . Purpose Returns the path of the LabWindows/CVI project file ( .prj ) that created the specified DLL. Remarks This method requires LabWindows/CVI 2017 SP1

### CVIModule.GetProjectFilePathFromDll

#### Syntax

[CVIModule](cvimodule.html).GetProjectFilePathFromDll( dllPath, projectPathParam)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 upon success. Otherwise, returns
 False
 .

#### Purpose

Returns the path of the LabWindows/CVI project file (
 .prj
 ) that created the specified DLL.

#### Remarks

This method requires LabWindows/CVI 2017 SP1 or later.

#### Parameters

dllPath
 As
 [String](data-types-for-teststand.html)

[In] The absolute path of the DLL.

projectPathParam
 As
 [String](data-types-for-teststand.html)

[Out] The path of the LabWindows/CVI project (
 .prj
 ) file.

#### See Also

[CVIModule.AllowProjectFileWhenSelectingModule](cvimodule-allowprojectfilewhenselectingmodule.html)

[CVIModule.GetModulePathFromProject](cvimodule-getmodulepathfromproject.html)

[CVIModule.GetSourceFilePathFromDll](cvimodule-getsourcefilepathfromdll.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cvimodule-getsourcefilepathfromdll.html language=enus -->
## TOPIC 00470: CVIModule.GetSourceFilePathFromDll

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cvimodule-getsourcefilepathfromdll.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cvimodule-getsourcefilepathfromdll.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIModule.GetSourceFilePathFromDll( dllPath, function, sourcePath) Return Value Boolean Returns True upon success. Otherwise, returns False . Purpose Returns the path of the C source file containing the definition of the specified function. Remarks This method requires LabWindows/CVI 2017 SP1

### CVIModule.GetSourceFilePathFromDll

#### Syntax

[CVIModule](cvimodule.html).GetSourceFilePathFromDll( dllPath, function, sourcePath)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 upon success. Otherwise, returns
 False
 .

#### Purpose

Returns the path of the C source file containing the definition of the specified function.

#### Remarks

This method requires LabWindows/CVI 2017 SP1 or later.

#### Parameters

dllPath
 As
 [String](data-types-for-teststand.html)

[In] The absolute path of the DLL.

function
 As
 [String](data-types-for-teststand.html)

[In] The function name.

sourcePath
 As
 [String](data-types-for-teststand.html)

[Out] The path of the C source file.

#### See Also

[CVIModule.AllowProjectFileWhenSelectingModule](cvimodule-allowprojectfilewhenselectingmodule.html)

[CVIModule.GetModulePathFromProject](cvimodule-getmodulepathfromproject.html)

[CVIModule.GetProjectFilePathFromDll](cvimodule-getprojectfilepathfromdll.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cvimodule-moduletype.html language=enus -->
## TOPIC 00471: CVIModule.ModuleType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cvimodule-moduletype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cvimodule-moduletype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIModule.ModuleType Data Type CVIModuleTypes Use the following constants with this data type: CVIModuleType_DLL –(Value: 2) Specifies that the module is a DLL. CVIModuleType_Lib –(Value: 3) This constant is obsolete. Specifies that the module is a static library. CVIModuleType_Obj –(Value: 0

### CVIModule.ModuleType

#### Syntax

[CVIModule](cvimodule.html).ModuleType

#### Data Type

[CVIModuleTypes](cvimoduletypes.html)

Use the following constants with this data type:

- CVIModuleType_DLL 
 –(Value: 2) Specifies that the module is a DLL.
- CVIModuleType_Lib 
 –(Value: 3) This constant is obsolete. Specifies that the module is a static library.
- CVIModuleType_Obj 
 –(Value: 0) This constant is obsolete. Specifies that the module is an object file.
- CVIModuleType_Source 
 –(Value: 1) This constant is obsolete. Specifies that the module is a source file.

#### Purpose

Specifies the type of code module the step calls.

#### Remarks

The LabWindows/CVI Adapter supports calling functions in DLL files.

#### See Also

[CommonCModule.FunctionName](commoncmodule-functionname.html)

[CommonCModule.ModulePath](commoncmodule-modulepath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cvimodule-parameters.html language=enus -->
## TOPIC 00472: CVIModule.Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cvimodule-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cvimodule-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIModule.Parameters Data Type CVIParameters Purpose Returns the CVIParameters collection that contains a list of the current parameters used as inputs and outputs of the corresponding module. Remarks If you need to add or modify a parameter, you must first obtain the parameters collection. S

### CVIModule.Parameters

#### Syntax

[CVIModule](cvimodule.html).Parameters

#### Data Type

[CVIParameters](cviparameters.html)

#### Purpose

Returns the CVIParameters collection that contains a list of the current parameters used as inputs and outputs of the corresponding module.

#### Remarks

If you need to add or modify a parameter, you must first obtain the parameters collection.

#### See Also

[CVIParameters](cviparameters.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cvimodule.html language=enus -->
## TOPIC 00473: CVIModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cvimodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cvimodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the CVIModule class to specify and obtain LabWindows/CVI Adapter-specific information about the code module that steps or step type substeps execute. Use the Step.Module property to obtain a reference to a CVIModule object. To access the properties and methods of a specific module c

### CVIModule

Use objects from the CVIModule class to specify and obtain LabWindows/CVI Adapter-specific information about the code module that steps or step type substeps execute. Use the
 
 [Step.Module](step-module.html)
 property to obtain a reference to a CVIModule object. To access the properties and methods of a specific module class, query the Module object for the interface of the module-specific interface you want to acquire.

Typically, you use this class only when you are writing a sequence editor.

To access the properties and methods of the CommonCModule class, use the
 [CVIModule.AsCommonCModule](cvimodule-ascommoncmodule.html)
 method to obtain an object.

You can use the
 
 [Module.LoadPrototype](module-loadprototype.html)
 method to load the prototype for the module the step specifies.

#### Properties

| AlwaysRunInProcess |
| --- |
| ModuleType |
| Parameters (Read Only) |

#### Methods

| AllowProjectFileWhenSelectingModule |
| --- |
| AsCommonCModule |
| Execute |
| GetModulePathFromProject |
| GetProjectFilePathFromDll |
| GetSourceFilePathFromDll |

#### See Also

[CommonCModule](commoncmodule.html)

[Module](module.html)

[Module.LoadPrototype](module-loadprototype.html)

[Step.Module](step-module.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cvimoduletypes.html language=enus -->
## TOPIC 00474: CVIModuleTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cvimoduletypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cvimoduletypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the CVIModule.ModuleType property to specify what type of executable the module runs. CVIModuleType_DLL –(Value: 2) Specifies that the module is a DLL. CVIModuleType_Lib –(Value: 3) This constant is obsolete. Specifies that the module is a static library. CVIModuleType_Obj –

### CVIModuleTypes

Use these constants with the
 [CVIModule.ModuleType](cvimodule-moduletype.html)
 property to specify what type of executable the module runs.

- CVIModuleType_DLL 
 –(Value: 2) Specifies that the module is a DLL.
- CVIModuleType_Lib 
 –(Value: 3) This constant is obsolete. Specifies that the module is a static library.
- CVIModuleType_Obj 
 –(Value: 0) This constant is obsolete. Specifies that the module is an object file.
- CVIModuleType_Source 
 –(Value: 1) This constant is obsolete. Specifies that the module is a source file.

#### See Also

[CVIModule.ModuleType](cvimodule-moduletype.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviparameter-ascommoncparameter.html language=enus -->
## TOPIC 00475: CVIParameter.AsCommonCParameter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviparameter-ascommoncparameter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviparameter-ascommoncparameter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIParameter.AsCommonCParameter Return Value CommonCParameter Purpose Returns the underlying CommonCParameter that represents the CVIParameter. Remarks Use the CommonCParameter object to access properties and methods common to all parameters derived from this class. See Also CommonCParameter

### CVIParameter.AsCommonCParameter

#### Syntax

[CVIParameter](cviparameter.html).AsCommonCParameter

#### Return Value

[CommonCParameter](commoncparameter.html)

#### Purpose

Returns the underlying CommonCParameter that represents the CVIParameter.

#### Remarks

Use the CommonCParameter object to access properties and methods common to all parameters derived from this class.

#### See Also

[CommonCParameter](commoncparameter.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviparameter-category.html language=enus -->
## TOPIC 00476: CVIParameter.Category

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviparameter-category.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviparameter-category.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIParameter.Category Data Type CVIParameterCategories Use the following constants with this data type: CVIParamCategory_CStruct –(Value: 5) Specifies that the parameter is a C-style struct. This category does not have any associated data types. However, you can use the CommonCParameter.Struc

### CVIParameter.Category

#### Syntax

[CVIParameter](cviparameter.html).Category

#### Data Type

[CVIParameterCategories](cviparametercategories.html)

Use the following constants with this data type:

- CVIParamCategory_CStruct 
 –(Value: 5) Specifies that the parameter is a C-style struct. This category does not have any associated data types. However, you can use the
 CommonCParameter.StructType 
 property to specify the name of the TestStand type the parameter represents.
- CVIParamCategory_CStructArray 
 –(Value: 8) Specifies that the parameter is an array of C-style structs. This category does not have any associated data types. However, you can use the
 CommonCParameter.StructType 
 property to specify the name of the TestStand type that the parameter represents.
- CVIParamCategory_Enum 
 –(Value: 10) Specifies that the parameter is an enumeration data type. Valid data types for this category include
 CParamType_Float32 
 ,
 CParamType_Float64 
 ,
 CParamType_Int16 
 ,
 CParamType_Int32 
 ,
 CParamType_Int8 
 ,
 CParamType_UInt16 
 ,
 CParamType_UInt32 
 ,
 CParamType_UInt8 
 ,
 CParamType_UInt64 
 , and
 CParamType_Int64 
 . You can use the CommonCParameter.StructType property to specify the name of the TestStand type that the parameter represents.
- CVIParamCategory_EnumArray 
 –(Value: 11) Specifies that the parameter is an array of C-style structs. Valid data types for this category include
 CParamType_Float32 
 ,
 CParamType_Float64 
 ,
 CParamType_Int16 
 ,
 CParamType_Int32 
 ,
 CParamType_Int8 
 ,
 CParamType_UInt16 
 ,
 CParamType_UInt32 
 ,
 CParamType_UInt8 
 ,
 CParamType_UInt64 
 , and
 CParamType_Int64 
 . You can use the CommonCParameter.StructType property to specify the name of the TestStand type that the parameter represents.
- CVIParamCategory_Numeric 
 –(Value: 0) Specifies that the parameter is a numeric data type. Valid data types for this category include
 CParamType_Float32 
 ,
 CParamType_Float64 
 ,
 CParamType_Int16 
 ,
 CParamType_Int32 
 ,
 CParamType_Int8 
 ,
 CParamType_UInt16 
 ,
 CParamType_UInt32 
 ,
 CParamType_UInt8 
 ,
 CParamType_UInt64 
 , and
 CParamType_Int64 
 .
- CVIParamCategory_NumericArray 
 –(Value: 1) Specifies that the parameter is an array of numbers. Valid data types for this category include
 CParamType_Float32 
 ,
 CParamType_Float64 
 ,
 CParamType_Int16 
 ,
 CParamType_Int32 
 ,
 CParamType_Int8 
 ,
 CParamType_UInt16 
 ,
 CParamType_UInt32 
 ,
 CParamType_UInt8 
 ,
 CParamType_UInt64 
 , and
 CParamType_Int64 
 .
- CVIParamCategory_Object 
 –(Value: 4) Specifies that the parameter is an ActiveX object reference. Valid data types for this category include
 CParamType_CVIHandle 
 ,
 CParamType_IDispatch 
 , and
 CParamType_IUnknown 
 .
- CVIParamCategory_ObjectArray 
 –(Value: 7) Specifies that the parameter is an array of ActiveX object references. Valid data types for this category include
 CParamType_CVIHandle 
 ,
 CParamType_IDispatch 
 , and
 CParamType_IUnknown 
 .
- CVIParamCategory_Pointer 
 –(Value: 9)
- CVIParamCategory_String 
 –(Value: 2) Specifies that the parameter is a string. Valid data types for this category include
 CParamType_CString 
 ,
 CParamType_CStringBuffer 
 ,
 CParamType_UnicodeString 
 , and
 CParamType_UnicodeStringBuffer 
 .
- CVIParamCategory_StringArray 
 –(Value: 6) Specifies that the parameter is an array of strings. Valid data types for this category include
 CParamType_CString 
 ,
 CParamType_CStringBuffer 
 ,
 CParamType_UnicodeString 
 , and
 CParamType_UnicodeStringBuffer 
 .
- CVIParamCategory_TestData 
 –(Value: 100) Specifies that the parameter is a legacy LabWindows/CVI tTestData struct. This category does not have any associated data types.
- CVIParamCategory_TestError 
 –(Value: 101) Specifies that the parameter is a legacy LabWindows/CVI tTestError struct. This category does not have any associated data types.
- CVIParamCategory_Void 
 –(Value: 3) Specifies that the parameter is a void parameter, meaning it has no value. This category applies only to return values.

#### Purpose

Returns the category of the parameter.

#### See Also

[CommonCParameter.GetArrayDimensionSizeExpr](commoncparameter-getarraydimensionsizeexpr.html)

[CommonCParameter.SetArrayDimensionSizeExpr](commoncparameter-setarraydimensionsizeexpr.html)

[CommonCParameter.StringBufferSizeExpr](commoncparameter-stringbuffersizeexpr.html)

[CommonCParameter.StructType](commoncparameter-structtype.html)

[CVIParameter.Type](cviparameter-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviparameter-type.html language=enus -->
## TOPIC 00477: CVIParameter.Type

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviparameter-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviparameter-type.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIParameter.Type Data Type CommonCParameterTypes Purpose Specifies the type of parameter. Remarks The parameter category depends on the parameter type. Before you choose the type, ensure you select the correct category. See Also CommonCParameter.StringBufferSizeExpr CommonCParameter.StructTy

### CVIParameter.Type

#### Syntax

[CVIParameter](cviparameter.html).Type

#### Data Type

[CommonCParameterTypes](commoncparametertypes.html)

#### Purpose

Specifies the type of parameter.

#### Remarks

The parameter category depends on the parameter type. Before you choose the type, ensure you select the correct category.

#### See Also

[CommonCParameter.StringBufferSizeExpr](commoncparameter-stringbuffersizeexpr.html)

[CommonCParameter.StructType](commoncparameter-structtype.html)

[CommonCParameterTypes](commoncparametertypes.html)

[CVIParameter.Category](cviparameter-category.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviparameter.html language=enus -->
## TOPIC 00478: CVIParameter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviparameter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviparameter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the CVIParameters class to configure and obtain LabWindows/CVI parameter-specific information for an item in the CVIParameter collection class. To access the properties and methods of the CommonCParameter class, use the CVIParameter.AsCommonCParameter method to obtain an object. Pro

### CVIParameter

Use objects from the CVIParameters class to configure and obtain LabWindows/CVI parameter-specific information for an item in the CVIParameter collection class.

To access the properties and methods of the CommonCParameter class, use the
 [CVIParameter.AsCommonCParameter](cviparameter-ascommoncparameter.html)
 method to obtain an object.

#### Properties

| Category |
| --- |
| Type |

#### Method

| AsCommonCParameter |
| --- |

#### See Also

[CommonCParameter](commoncparameter.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviparametercategories.html language=enus -->
## TOPIC 00479: CVIParameterCategories

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviparametercategories.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviparametercategories.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following constants with the CVIParameter.Category property and the parameterCategory parameter of CVIParameters.New method to specify the group of data types to which the parameter belongs. When you get or set the category of the parameter, also get or set the data type with the CVIParamete

### CVIParameterCategories

Use the following constants with the
 [CVIParameter.Category](cviparameter-category.html)
 property and the
 parameterCategory
 parameter of
 [CVIParameters.New](cviparameters-new.html)
 method to specify the group of data types to which the parameter belongs. When you get or set the category of the parameter, also get or set the data type with the
 [CVIParameter.Type](cviparameter-type.html)
 property or set the
 parameterType
 parameter of the
 CVIParameters.New
 method. Some categories do not have an associated data type. For these categories, the only valid value for
 CVIParameter.Type
 is
 [ParamType_NotUsed](commoncparametertypes.html)
 .

- CVIParamCategory_CStruct 
 –(Value: 5) Specifies that the parameter is a C-style struct. This category does not have any associated data types. However, you can use the
 CommonCParameter.StructType 
 property to specify the name of the TestStand type the parameter represents.
- CVIParamCategory_CStructArray 
 –(Value: 8) Specifies that the parameter is an array of C-style structs. This category does not have any associated data types. However, you can use the
 CommonCParameter.StructType 
 property to specify the name of the TestStand type that the parameter represents.
- CVIParamCategory_Enum 
 –(Value: 10) Specifies that the parameter is an enumeration data type. Valid data types for this category include
 CParamType_Float32 
 ,
 CParamType_Float64 
 ,
 CParamType_Int16 
 ,
 CParamType_Int32 
 ,
 CParamType_Int8 
 ,
 CParamType_UInt16 
 ,
 CParamType_UInt32 
 ,
 CParamType_UInt8 
 ,
 CParamType_UInt64 
 , and
 CParamType_Int64 
 . You can use the CommonCParameter.StructType property to specify the name of the TestStand type that the parameter represents.
- CVIParamCategory_EnumArray 
 –(Value: 11) Specifies that the parameter is an array of C-style structs. Valid data types for this category include
 CParamType_Float32 
 ,
 CParamType_Float64 
 ,
 CParamType_Int16 
 ,
 CParamType_Int32 
 ,
 CParamType_Int8 
 ,
 CParamType_UInt16 
 ,
 CParamType_UInt32 
 ,
 CParamType_UInt8 
 ,
 CParamType_UInt64 
 , and
 CParamType_Int64 
 . You can use the CommonCParameter.StructType property to specify the name of the TestStand type that the parameter represents.
- CVIParamCategory_Numeric 
 –(Value: 0) Specifies that the parameter is a numeric data type. Valid data types for this category include
 CParamType_Float32 
 ,
 CParamType_Float64 
 ,
 CParamType_Int16 
 ,
 CParamType_Int32 
 ,
 CParamType_Int8 
 ,
 CParamType_UInt16 
 ,
 CParamType_UInt32 
 ,
 CParamType_UInt8 
 ,
 CParamType_UInt64 
 , and
 CParamType_Int64 
 .
- CVIParamCategory_NumericArray 
 –(Value: 1) Specifies that the parameter is an array of numbers. Valid data types for this category include
 CParamType_Float32 
 ,
 CParamType_Float64 
 ,
 CParamType_Int16 
 ,
 CParamType_Int32 
 ,
 CParamType_Int8 
 ,
 CParamType_UInt16 
 ,
 CParamType_UInt32 
 ,
 CParamType_UInt8 
 ,
 CParamType_UInt64 
 , and
 CParamType_Int64 
 .
- CVIParamCategory_Object 
 –(Value: 4) Specifies that the parameter is an ActiveX object reference. Valid data types for this category include
 CParamType_CVIHandle 
 ,
 CParamType_IDispatch 
 , and
 CParamType_IUnknown 
 .
- CVIParamCategory_ObjectArray 
 –(Value: 7) Specifies that the parameter is an array of ActiveX object references. Valid data types for this category include
 CParamType_CVIHandle 
 ,
 CParamType_IDispatch 
 , and
 CParamType_IUnknown 
 .
- CVIParamCategory_Pointer 
 –(Value: 9)
- CVIParamCategory_String 
 –(Value: 2) Specifies that the parameter is a string. Valid data types for this category include
 CParamType_CString 
 ,
 CParamType_CStringBuffer 
 ,
 CParamType_UnicodeString 
 , and
 CParamType_UnicodeStringBuffer 
 .
- CVIParamCategory_StringArray 
 –(Value: 6) Specifies that the parameter is an array of strings. Valid data types for this category include
 CParamType_CString 
 ,
 CParamType_CStringBuffer 
 ,
 CParamType_UnicodeString 
 , and
 CParamType_UnicodeStringBuffer 
 .
- CVIParamCategory_TestData 
 –(Value: 100) Specifies that the parameter is a legacy LabWindows/CVI tTestData struct. This category does not have any associated data types.
- CVIParamCategory_TestError 
 –(Value: 101) Specifies that the parameter is a legacy LabWindows/CVI tTestError struct. This category does not have any associated data types.
- CVIParamCategory_Void 
 –(Value: 3) Specifies that the parameter is a void parameter, meaning it has no value. This category applies only to return values.

#### See Also

[CommonCParameter.SetArrayDimensionSizeExpr](commoncparameter-setarraydimensionsizeexpr.html)

[CommonCParameter.StringBufferSizeExpr](commoncparameter-stringbuffersizeexpr.html)

[CommonCParameter.StructType](commoncparameter-structtype.html)

[CommonCParameterTypes](commoncparametertypes.html)

[CVIParameter.Category](cviparameter-category.html)

[CVIParameter.Type](cviparameter-type.html)

[CVIParameters.New](cviparameters-new.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviparameters-count.html language=enus -->
## TOPIC 00480: CVIParameters.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviparameters-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviparameters-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIParameters.Count Data Type Long Purpose Returns the number of items in the collection.

### CVIParameters.Count

#### Syntax

[CVIParameters](cviparameters.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviparameters-delete.html language=enus -->
## TOPIC 00481: CVIParameters.Delete

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviparameters-delete.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviparameters-delete.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIParameters.Delete( index) Purpose Removes the parameter located at the specific index. Parameters index As Long [In] Specifies the zero-based index of the parameter to delete.

### CVIParameters.Delete

#### Syntax

[CVIParameters](cviparameters.html).Delete( index)

#### Purpose

Removes the parameter located at the specific index.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the parameter to delete.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviparameters-item.html language=enus -->
## TOPIC 00482: CVIParameters.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviparameters-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviparameters-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIParameters.Item( index) Data Type CVIParameter Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the parameter to retrieve. See Also CVIParameter

### CVIParameters.Item

#### Syntax

[CVIParameters](cviparameters.html).Item( index)

#### Data Type

[CVIParameter](cviparameter.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the parameter to retrieve.

#### See Also

[CVIParameter](cviparameter.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviparameters-move.html language=enus -->
## TOPIC 00483: CVIParameters.Move

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviparameters-move.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviparameters-move.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIParameters.Move( index, newIndex) Purpose Moves a parameter within the collection. Parameters index As Long [In] Specifies the zero-based index indicating the current position of the parameter to move. newIndex As Long [In] Specifies the zero-based index indicating the new position of the

### CVIParameters.Move

#### Syntax

[CVIParameters](cviparameters.html).Move( index, newIndex)

#### Purpose

Moves a parameter within the collection.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index indicating the current position of the parameter to move.

newIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index indicating the new position of the parameter.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviparameters-new.html language=enus -->
## TOPIC 00484: CVIParameters.New

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviparameters-new.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviparameters-new.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIParameters.New( index, parameterName, parameterValueExpr, parameterCategory, parameterPass, parameterType) Purpose Adds a new parameter to the collection. Parameters index As Long [In] Specifies the zero-based index of where to insert the parameter. parameterName As String [In] Specifies t

### CVIParameters.New

#### Syntax

[CVIParameters](cviparameters.html).New( index, parameterName, parameterValueExpr, parameterCategory, parameterPass, parameterType)

#### Purpose

Adds a new parameter to the collection.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of where to insert the parameter.

parameterName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name assigned to the new parameter.

parameterValueExpr
 As
 [String](data-types-for-teststand.html)

[In] Specifies the argument expression.

If the parameter is an input, this expression corresponds to the value to pass. If the parameter is an output, this expression specifies where to store the result value.

parameterCategory
 As
 [CVIParameterCategories](cviparametercategories.html)

[In] Specifies the parameter category.

parameterPass
 As
 [CommonCParameterPassOptions](commoncparameterpassoptions.html)

[In] Specifies how to pass the value specified in the argument expression property,
 [CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)
 , to the specific function and sets the
 [CommonCParameter.Pass](commoncparameter-pass.html)
 property.

parameterType
 As
 [CommonCParameterTypes](commoncparametertypes.html)

[In] Specifies the parameter type.

#### See Also

[CommonCParameter.Pass](commoncparameter-pass.html)

[CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)

[CommonCParameterPassOptions](commoncparameterpassoptions.html)

[CommonCParameterTypes](commoncparametertypes.html)

[CVIParameterCategories](cviparametercategories.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviparameters-newarguments.html language=enus -->
## TOPIC 00485: CVIParameters.NewArguments

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviparameters-newarguments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviparameters-newarguments.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CVIParameters.NewArguments Return Value CVIArguments Purpose Creates and returns a new CVIArguments collection. Use this collection to pass argument values to a LabWindows/CVI module function using the CVIModule.Execute method. Remarks The new collection contains the same number of items as t

### CVIParameters.NewArguments

#### Syntax

[CVIParameters](cviparameters.html).NewArguments

#### Return Value

[CVIArguments](cviarguments.html)

#### Purpose

Creates and returns a new
 [CVIArguments](cviarguments.html)
 collection. Use this collection to pass argument values to a LabWindows/CVI module function using the
 [CVIModule.Execute](cvimodule-execute.html)
 method.

#### Remarks

The new collection contains the same number of items as the
 [CVIParameters](cviparameters.html)
 collection. To pass an argument value to a function parameter, set the
 [CVIArgument.Value](cviargument-value.html)
 property on the item in the
 CVIArguments
 collection that has the same index as the parameter in the
 CVIParameters
 collection.

#### See Also

[CVIArgument.Value](cviargument-value.html)

[CVIArguments](cviarguments.html)

[CVIModule.Execute](cvimodule-execute.html)

[CVIParameters](cviparameters.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cviparameters.html language=enus -->
## TOPIC 00486: CVIParameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cviparameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cviparameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the CVIParameters class to configure and obtain parameters for a module that uses the LabWindows/CVI Adapter. Use the CVIModule.Parameters property to obtain the collection of parameters for a module. Properties Count (Read Only) Item (Read Only) Methods Delete Move New NewArguments

### CVIParameters

Use objects from the CVIParameters class to configure and obtain parameters for a module that uses the LabWindows/CVI Adapter. Use the
 [CVIModule.Parameters](cvimodule-parameters.html)
 property to obtain the collection of parameters for a module.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Delete |
| --- |
| Move |
| New |
| NewArguments |

#### See Also

[CVIModule.Parameters](cvimodule-parameters.html)

[CVIParameter](cviparameter.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/cvistepadditions.html language=enus -->
## TOPIC 00487: CVIStepAdditions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/cvistepadditions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/cvistepadditions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Do not use these constants to access the adapter-specific properties of a step. Use the CVIModule interface for the Module object for the step. Use the Step.Module property to acquire a reference to a Module object. In TestStand 3.0 or later, these string constants are obsolete. These string constan

### CVIStepAdditions

Note

CVIModule

Step.Module

In TestStand 3.0 or later, these string constants are obsolete.

These string constants were previously used to create
 [lookup strings](/csh?context=ts_tsapiref_api_lookupstring)
 to access the adapter-specific properties of a LabWindows/CVI step. The following example code sets the module pathname property of a LabWindows/CVI step:

TS_PropertySetValString(propObj, &errorInfo,
 [Step_TSInfoProp](stepproperties.html)
 "."
 [TSInfo_StepAdditions](stepproperties.html)
 "." CVIStep_ModulePathProp, 0, testFilePath);

- CVIStep_FunctionNameProp 
 –(Value: "FuncName") This constant is obsolete.
- CVIStep_FunctionPrototypeProp 
 –(Value: "FuncProto") This constant is obsolete.
- CVIStep_ModulePathProp 
 –(Value: "ModulePath") This constant is obsolete.
- CVIStep_ModulePrjPathProp 
 –(Value: "ModulePrjPath") This constant is obsolete.
- CVIStep_ModuleSrcPathProp 
 –(Value: "ModuleSrcPath") This constant is obsolete.
- CVIStep_ModuleTypeProp 
 –(Value: "ModuleType") This constant is obsolete.
- CVIStep_ParamsStringProp 
 –(Value: "ExtProtoParams") This constant is obsolete.
- CVIStep_SeqContextPassProp 
 –(Value: "SeqContextType") This constant is obsolete.

#### See Also

[Lookup Strings](/csh?context=ts_tsapiref_api_lookupstring)

[Step](step.html)

[Step.Module](step-module.html)

[StepProperties](stepproperties.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/data-types-for-teststand.html language=enus -->
## TOPIC 00488: Data Types for TestStand

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/data-types-for-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/data-types-for-teststand.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Type OLE Automation Type Description Boolean VARIANT_BOOL Has the value True ( -1 ) or False ( 0 ). Byte Array SAFEARRAY(unsigned char) An array of bytes. Color OLE_COLOR A color. Many containers treat colors as 32-bit integers. Date DATE DATE is a variant time that is stored as an 8-byte real value

### Data Types for TestStand

| Type | OLE Automation Type | Description |
| --- | --- | --- |
| Boolean | VARIANT_BOOL | Has the value True ( -1 ) or False ( 0 ). |
| Byte Array | SAFEARRAY(unsigned char) | An array of bytes. |
| Color | OLE_COLOR | A color. Many containers treat colors as 32-bit integers. |
| Date | DATE | DATE is a variant time that is stored as an 8-byte real value (double) and represents a date between January 1, 100 and December 31, 9999, inclusive. The value 0 represents December 30, 1899. Adding 1 to the value increments the date by a day. The fractional part of the value represents the time of day. Negative numbers represent the dates before December 30, 1899. LabWindows/CVI users can use the VariantTimeToSystemTime Microsoft Windows Software Development Kit (SDK) function to convert the variant date to a system time value and then use the GetDateFormat and GetTimeFormat Windows SDK functions to generate display strings. LabVIEW automatically converts the DATE data type to a timestamp. |
| Double | double | 64-bit floating point number. |
| Float | float | 32-bit floating point number. |
| Font | IFontDisp | An Object Linking and Embedding (OLE) Automation Interface to a font . |
| Integer | short | 16-bit signed integer. |
| IUnknown | IUnknown | A generic OLE interface. |
| long | OLE_YPOS_PIXELS | Position on the Y-axis in pixels. |
| Long | Long | 32-bit signed integer. |
| long | OLE_XPOS_PIXELS | Position on the X-axis in pixels. |
| Long | LCID | A locale identifier. |
| Long Array | SAFEARRAY(long) | An array of longs. |
| long long | LONGLONG | 64-bit signed integer. |
| Object | IDispatch | A generic OLE Automation interface. |
| Object Array | SAFEARRAY | An array of objects. |
| Picture | IPicture | An OLE Automation Interface to a Picture object or image. |
| Picture | IPictureDisp | An OLE Automation Interface to a Picture object or image. |
| String | BSTR | A string. |
| String Array | SAFEARRAY(BSTR) | An array of strings. |
| SynchronizationStates |  |  |
| unsigned long long | ULONGLONG | 64-bit unsigned integer. |
| Variant | VARIANT | A variant. |
| VARTYPE | VARTYPE | An enumeration type used to describe a data type of a VARIANT or safearray value. Refer to VARTYPE for more information about VARTYPE enumeration values. |
| WIDESTR(OLD_CONFIG_FILE_HEADER_TYPE) |  |  |

Parent topic:

API Classes, Properties, and Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/debugoptions.html language=enus -->
## TOPIC 00489: DebugOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/debugoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/debugoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the type of debug operations TestStand performs. DebugOptions_BufferChecking –(Value: 0x2) The LabWindows/CVI and C/C++ DLL Adapters verify that the code module does not modify the memory that surrounds the buffer parameters passed to code modules. The adapters also ve

### DebugOptions

Use these constants to specify the type of debug operations TestStand performs.

- DebugOptions_BufferChecking 
 –(Value: 0x2) The LabWindows/CVI and C/C++ DLL Adapters verify that the code module does not modify the memory that surrounds the buffer parameters passed to code modules. The adapters also verify that code modules do not modify const string parameters.
- DebugOptions_None 
 –(Value: 0x0) Disables all debugging features.
- DebugOptions_ReportKnownOSandComponentProblems 
 –(Value: 0x10) During shut down of the TestStand Engine, TestStand launches a dialog box that contains a list of any operating system issues or component-related issues that can cause leaks in memory, Graphics Device Interface, and User object resources in TestStand.
- DebugOptions_ReportObjectLeaks 
 –(Value: 0x4) During shutdown of the engine, TestStand launches a dialog box that contains a list of any top-level Property Objects with unreleased references.
- DebugOptions_SendOutputMessagesToDebugger 
 –(Value: 0x8) Instructs TestStand to send output messages to the debugger when you call the
 OutputMessage.Post 
 method.
- DebugOptions_StackChecking 
 –(Value: 0x1) The LabWindows/CVI (in-process), C/C++ DLL, and ActiveX Adapters verify that the content of a thread stack does not change while calling code modules.

#### See Also

[OutputMessage.Post](outputmessage-post.html)

[StationOptions.DebugOptions](stationoptions-debugoptions.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/decimalpointlocalizationoptions.html language=enus -->
## TOPIC 00490: DecimalPointLocalizationOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/decimalpointlocalizationoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/decimalpointlocalizationoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the decimalPointOption parameter of the Engine.LocalizeExpression , Engine.DelocalizeExpression , and Engine.GetLocalizedDecimalPoint methods. The decimalPointOption parameter specifies how TestStand determines which character it uses as the localized decimal point cha

### DecimalPointLocalizationOptions

Use these constants to specify the
 decimalPointOption
 parameter of the
 [Engine.LocalizeExpression](engine-localizeexpression.html)
 ,
 [Engine.DelocalizeExpression](engine-delocalizeexpression.html)
 , and
 [Engine.GetLocalizedDecimalPoint](engine-getlocalizeddecimalpoint.html)
 methods. The
 decimalPointOption
 parameter specifies how TestStand determines which character it uses as the localized decimal point character.

- DecimalPoint_UseComma 
 –(Value: 4) Use the comma character.
- DecimalPoint_UsePeriod 
 –(Value: 3) Use the period character.
- DecimalPoint_UsePreference 
 –(Value: 1) Use the Station Options localization preferences to determine whether to use the operating system setting.
- DecimalPoint_UseSystemSetting 
 –(Value: 2) Use the operating system setting.

#### See Also

[Engine.DelocalizeExpression](engine-delocalizeexpression.html)

[Engine.GetLocalizedDecimalPoint](engine-getlocalizeddecimalpoint.html)

[Engine.LocalizeExpression](engine-localizeexpression.html)

[Engine.StationOptions](engine-stationoptions.html)

[StationOptions.UseLocalizedDecimalPoint](stationoptions-uselocalizeddecimalpoint.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/defaultmodelcallbacks.html language=enus -->
## TOPIC 00491: DefaultModelCallbacks

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/defaultmodelcallbacks.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/defaultmodelcallbacks.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these string constants to specify the callbackName parameter of the SequenceFile.CreateCallbackOverrideSequence method. DefModCback_DatabaseOptions –(Value: "DatabaseOptions") DefModCback_GetReportFilePath –(Value: "GetReportFilePath") DefModCback_LogToDatabase –(Value: "LogToDatabase") DefModCb

### DefaultModelCallbacks

Use these string constants to specify the
 callbackName
 parameter of the
 [SequenceFile.CreateCallbackOverrideSequence](sequencefile-createcallbackoverridesequence.html)
 method.

- DefModCback_DatabaseOptions 
 –(Value: "DatabaseOptions")
- DefModCback_GetReportFilePath 
 –(Value: "GetReportFilePath")
- DefModCback_LogToDatabase 
 –(Value: "LogToDatabase")
- DefModCback_ModelOptions 
 –(Value: "ModelOptions")
- DefModCback_ModelPluginConfiguration 
 –(Value: "ModelPluginConfiguration")
- DefModCback_ModelPluginOptions 
 –(Value: "ModelPluginOptions")
- DefModCback_ModifyReportEntry 
 –(Value: "ModifyReportEntry")
- DefModCback_ModifyReportFooter 
 –(Value: "ModifyReportFooter")
- DefModCback_ModifyReportHeader 
 –(Value: "ModifyReportHeader")
- DefModCback_ModifyRptEntry 
 –(Value: "ModifyReportEntry")
- DefModCback_PostMainSequence 
 –(Value: "PostMainSequence")
- DefModCback_PostUUT 
 –(Value: "PostUUT")
- DefModCback_PostUUTLoop 
 –(Value: "PostUUTLoop")
- DefModCback_PreMainSequence 
 –(Value: "PreMainSequence")
- DefModCback_PreUUT 
 –(Value: "PreUUT")
- DefModCback_PreUUTLoop 
 –(Value: "PreUUTLoop")
- DefModCback_ProcessCleanup 
 –(Value: "ProcessCleanup")
- DefModCback_ProcessSetup 
 –(Value: "ProcessSetup")
- DefModCback_ReportOptions 
 –(Value: "ReportOptions")
- DefModCback_TestReport 
 –(Value: "TestReport")

#### See Also

[FrontEndCallbacks](frontendcallbacks.html)

[SeqFileCallbacks](seqfilecallbacks.html)

[SequenceFile.CreateCallbackOverrideSequence](sequencefile-createcallbackoverridesequence.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/deployprojectlibraryoptions.html language=enus -->
## TOPIC 00492: DeployProjectLibraryOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/deployprojectlibraryoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/deployprojectlibraryoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following constants with the LabVIEWAdapter.DeployProjectLibrary method to specify whether to deploy or undeploy a LabVIEW project library file: DeployProjectLibraryOption_Deploy –(Value: 0) Specifies to deploy the LabVIEW project library file. DeployProjectLibraryOption_Undeploy –(Value: 1)

### DeployProjectLibraryOptions

Use the following constants with the
 [LabVIEWAdapter.DeployProjectLibrary](labviewadapter-deployprojectlibrary.html)
 method to specify whether to deploy or undeploy a LabVIEW project library file:

- DeployProjectLibraryOption_Deploy 
 –(Value: 0) Specifies to deploy the LabVIEW project library file.
- DeployProjectLibraryOption_Undeploy 
 –(Value: 1) Specifies to undeploy the LabVIEW project library file.

#### See Also

[Deploying Network-Published Shared Variables](/csh?context=ts_tslabview_variable)

[LabVIEWAdapter.DeployProjectLibrary](labviewadapter-deployprojectlibrary.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dlladapter-asadapter.html language=enus -->
## TOPIC 00493: DllAdapter.AsAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dlladapter-asadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dlladapter-asadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllAdapter.AsAdapter Return Value Adapter Purpose Returns the underlying module Adapter object that represents the C/C++ DLL Adapter. Remarks Use the adapter to access properties and methods common to all adapters. See Also Adapter DllAdapter.AsCommonCAdapter

### DllAdapter.AsAdapter

#### Syntax

[DllAdapter](dlladapter.html).AsAdapter

#### Return Value

[Adapter](adapter.html)

#### Purpose

Returns the underlying module Adapter object that represents the C/C++ DLL Adapter.

#### Remarks

Use the adapter to access properties and methods common to all adapters.

#### See Also

[Adapter](adapter.html)

[DllAdapter.AsCommonCAdapter](dlladapter-ascommoncadapter.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dlladapter-ascommoncadapter.html language=enus -->
## TOPIC 00494: DllAdapter.AsCommonCAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dlladapter-ascommoncadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dlladapter-ascommoncadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllAdapter.AsCommonCAdapter Return Value CommonCAdapter Purpose Returns the underlying CommonCAdapter object that represents the C/C++ DLL Adapter. Remarks Use the CommonCAdapter object to access properties and methods common to all adapters derived from this class. See Also AsAdapter CommonC

### DllAdapter.AsCommonCAdapter

#### Syntax

[DllAdapter](dlladapter.html).AsCommonCAdapter

#### Return Value

[CommonCAdapter](commoncadapter.html)

#### Purpose

Returns the underlying CommonCAdapter object that represents the C/C++ DLL Adapter.

#### Remarks

Use the CommonCAdapter object to access properties and methods common to all adapters derived from this class.

#### See Also

[AsAdapter](dlladapter-asadapter.html)

[CommonCAdapter](commoncadapter.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dlladapter-newmodule.html language=enus -->
## TOPIC 00495: DllAdapter.NewModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dlladapter-newmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dlladapter-newmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllAdapter.NewModule Return Value DllModule Purpose Creates and returns a new DllModule object. Use this method to create a DllModule object that you can execute without using a step, sequence, or execution. See Also DllModule DllModule.Execute DllParameters.NewArguments

### DllAdapter.NewModule

#### Syntax

[DllAdapter](dlladapter.html).NewModule

#### Return Value

[DllModule](dllmodule.html)

#### Purpose

Creates and returns a new
 [DllModule](dllmodule.html)
 object. Use this method to create a
 DllModule
 object that you can execute without using a step, sequence, or execution.

#### See Also

[DllModule](dllmodule.html)

[DllModule.Execute](dllmodule-execute.html)

[DllParameters.NewArguments](dllparameters-newarguments.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dlladapter-visualstudiodteversionfordebugging.html language=enus -->
## TOPIC 00496: DllAdapter.VisualStudioDTEVersionForDebugging

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dlladapter-visualstudiodteversionfordebugging.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dlladapter-visualstudiodteversionfordebugging.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllAdapter.VisualStudioDTEVersionForDebugging Data Type String Purpose Specifies the Microsoft Visual Studio development environment (DTE) version the C/C++ DLL Adapter uses when debugging into code modules when more than one version of Visual Studio is installed. Remarks If you have only one

### DllAdapter.VisualStudioDTEVersionForDebugging

#### Syntax

[DllAdapter](dlladapter.html).VisualStudioDTEVersionForDebugging

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the Microsoft Visual Studio development environment (DTE) version the C/C++ DLL Adapter uses when debugging into code modules when more than one version of Visual Studio is installed.

#### Remarks

If you have only one version of Visual Studio installed, the C/C++ DLL Adapter always uses that version for debugging.

You can set this property to a supported value of the
 [VisualStudioDTEVersions](visualstudiodteversions.html)
 constants or to the programmatic identifier of the DTE version you want to use.

Note

VisualStudioDTEVersion_MatchProject

#### See Also

[VisualStudioDTEVersions](visualstudiodteversions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dlladapter-visualstudiodteversionforediting.html language=enus -->
## TOPIC 00497: DllAdapter.VisualStudioDTEVersionForEditing

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dlladapter-visualstudiodteversionforediting.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dlladapter-visualstudiodteversionforediting.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllAdapter.VisualStudioDTEVersionForEditing Data Type String Purpose Specifies the Microsoft Visual Studio development environment (DTE) version the C/C++ DLL Adapter uses when creating and editing code when more than one version of Visual Studio is installed. Remarks If you have only one ver

### DllAdapter.VisualStudioDTEVersionForEditing

#### Syntax

[DllAdapter](dlladapter.html).VisualStudioDTEVersionForEditing

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the Microsoft Visual Studio development environment (DTE) version the C/C++ DLL Adapter uses when creating and editing code when more than one version of Visual Studio is installed.

#### Remarks

If you have only one version of Visual Studio installed, the C/C++ DLL Adapter always uses that version for debugging.

You can set this property to a supported value of the
 [VisualStudioDTEVersions](visualstudiodteversions.html)
 constants or to the programmatic identifier of the DTE version you want to use.

#### See Also

[VisualStudioDTEVersions](visualstudiodteversions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dlladapter.html language=enus -->
## TOPIC 00498: DllAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dlladapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dlladapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the DllAdapter class to configure and obtain C/C++ DLL Adapter-specific information about the module adapter. Call the Engine.GetAdapter or Engine.GetAdapterByKeyName method to obtain a reference to the adapter object. To access the properties and methods of the Adapter class, use t

### DllAdapter

Use objects from the DllAdapter class to configure and obtain C/C++ DLL Adapter-specific information about the module adapter. Call the
 
 [Engine.GetAdapter](engine-getadapter.html)
 or
 
 [Engine.GetAdapterByKeyName](engine-getadapterbykeyname.html)
 method to obtain a reference to the adapter object.

To access the properties and methods of the Adapter class, use the
 [DllAdapter.AsAdapter](dlladapter-asadapter.html)
 method to obtain an object.

#### Properties

| VisualStudioDTEVersionForDebugging |
| --- |
| VisualStudioDTEVersionForEditing |

#### Methods

| AsAdapter |
| --- |
| AsCommonCAdapter |
| NewModule |

#### See Also

[Adapter](adapter.html)

[CommonCAdapter](commoncadapter.html)

[DllAdapter.AsAdapter](dlladapter-asadapter.html)

[Engine.GetAdapter](engine-getadapter.html)

[Engine.GetAdapterByKeyName](engine-getadapterbykeyname.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllargument-imaginarypartvalue.html language=enus -->
## TOPIC 00499: DllArgument.ImaginaryPartValue

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllargument-imaginarypartvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllargument-imaginarypartvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllArgument.ImaginaryPartValue Data Type PropertyObject Purpose Specifies the argument value for to pass for the imaginary part of a DllParamCategory_CNiComplex or DllParamCategory_CNiComplexVector parameter. See Also DllArgument.Value DllParameter.ImaginaryPartValueExpr DllParameterCategorie

### DllArgument.ImaginaryPartValue

#### Syntax

[DllArgument](dllargument.html).ImaginaryPartValue

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Specifies the argument value for to pass for the imaginary part of a
 [DllParamCategory_CNiComplex](dllparametercategories.html)
 or
 [DllParamCategory_CNiComplexVector](dllparametercategories.html)
 parameter.

#### See Also

[DllArgument.Value](dllargument-value.html)

[DllParameter.ImaginaryPartValueExpr](dllparameter-imaginarypartvalueexpr.html)

[DllParameterCategories](dllparametercategories.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllargument-value.html language=enus -->
## TOPIC 00500: DllArgument.Value

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllargument-value.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllargument-value.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllArgument.Value Data Type PropertyObject Purpose Specifies the argument value to pass for the corresponding parameter. Remarks When you pass a DllArguments collection to the DllModule.Execute function, the adapter passes this property to the function instead of evaluating the CommonCParamet

### DllArgument.Value

#### Syntax

[DllArgument](dllargument.html).Value

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Specifies the argument value to pass for the corresponding parameter.

#### Remarks

When you pass a
 [DllArguments](dllarguments.html)
 collection to the
 [DllModule.Execute](dllmodule-execute.html)
 function, the adapter passes this property to the function instead of evaluating the
 [CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)
 expression.

#### See Also

[CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)

[DllArguments](dllarguments.html)

[DllModule.Execute](dllmodule-execute.html)

Parent topic:

Properties
