# JAVA OPENAPI: SecurityPackage (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/security/SecurityPackage.html
- source_path: `com/nomagic/magicdraw/security/SecurityPackage.html`
- source_sha256: `3c0cfdeba2590729e77ad72eab9f0b9bfd477d68c5c14346bc1e03aacf2d99a1`
- captured_utc: `2026-07-14T16:58:01.657578+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.security](package-summary.html)

## Interface SecurityPackage

All Superinterfaces:
`org.eclipse.emf.ecore.EModelElement`, `org.eclipse.emf.ecore.ENamedElement`, `org.eclipse.emf.ecore.EObject`, `org.eclipse.emf.ecore.EPackage`, `org.eclipse.emf.common.notify.Notifier`

public interfaceSecurityPackageextends org.eclipse.emf.ecore.EPackage

begin-user-doc 
 The **Package** for the model.
 It contains accessors for the meta objects to represent
 each class,
each feature of each class,
each operation of each class,
each enum,
and each data type
 end-user-doc

See Also:
[`SecurityFactory`](SecurityFactory.html)
Model:
kind="package"
Generated:

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Interface
Description
`static interface`
`[SecurityPackage.Literals](SecurityPackage.Literals.html)`
Defines literals for the meta objects that represent
 
 each class,
 each feature of each class,
 each operation of each class,
 each enum,
 and each data type
 
 end-user-doc
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[ACTION](#ACTION)`
The meta object id for the '[`*Action*`](Action.html)' enum.
`static final int`
`[APPLICATION](#APPLICATION)`
The meta object id for the '[`*Application*`](Application.html)' enum.
`static final [SecurityPackage](SecurityPackage.html)`
`[eINSTANCE](#eINSTANCE)`
The singleton instance of the package.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[eNAME](#eNAME)`
The package name.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[eNS_PREFIX](#eNS_PREFIX)`
The package namespace name.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[eNS_URI](#eNS_URI)`
The package namespace URI.
`static final int`
`[EVERYONE_PRINCIPAL](#EVERYONE_PRINCIPAL)`
The meta object id for the '`*Everyone Principal*`' class.
`static final int`
`[EVERYONE_PRINCIPAL___IS_SAME__PRINCIPAL](#EVERYONE_PRINCIPAL___IS_SAME__PRINCIPAL)`
The operation id for the '*Is Same*' operation.
`static final int`
`[EVERYONE_PRINCIPAL__NAME](#EVERYONE_PRINCIPAL__NAME)`
The feature id for the '***Name***' attribute.
`static final int`
`[EVERYONE_PRINCIPAL__PACKAGE_PERMISSIONS](#EVERYONE_PRINCIPAL__PACKAGE_PERMISSIONS)`
The feature id for the '***Package Permissions***' reference list.
`static final int`
`[EVERYONE_PRINCIPAL_FEATURE_COUNT](#EVERYONE_PRINCIPAL_FEATURE_COUNT)`
The number of structural features of the '*Everyone Principal*' class.
`static final int`
`[EVERYONE_PRINCIPAL_OPERATION_COUNT](#EVERYONE_PRINCIPAL_OPERATION_COUNT)`
The number of operations of the '*Everyone Principal*' class.
`static final int`
`[GROUP_PRINCIPAL](#GROUP_PRINCIPAL)`
The meta object id for the '`*Group Principal*`' class.
`static final int`
`[GROUP_PRINCIPAL___IS_SAME__PRINCIPAL](#GROUP_PRINCIPAL___IS_SAME__PRINCIPAL)`
The operation id for the '*Is Same*' operation.
`static final int`
`[GROUP_PRINCIPAL__NAME](#GROUP_PRINCIPAL__NAME)`
The feature id for the '***Name***' attribute.
`static final int`
`[GROUP_PRINCIPAL__PACKAGE_PERMISSIONS](#GROUP_PRINCIPAL__PACKAGE_PERMISSIONS)`
The feature id for the '***Package Permissions***' reference list.
`static final int`
`[GROUP_PRINCIPAL_FEATURE_COUNT](#GROUP_PRINCIPAL_FEATURE_COUNT)`
The number of structural features of the '*Group Principal*' class.
`static final int`
`[GROUP_PRINCIPAL_OPERATION_COUNT](#GROUP_PRINCIPAL_OPERATION_COUNT)`
The number of operations of the '*Group Principal*' class.
`static final int`
`[PACKAGE_ACCESS_PERMISSION](#PACKAGE_ACCESS_PERMISSION)`
The meta object id for the '`*Package Access Permission*`' class.
`static final int`
`[PACKAGE_ACCESS_PERMISSION___IS_SAME__PACKAGEACCESSPERMISSION](#PACKAGE_ACCESS_PERMISSION___IS_SAME__PACKAGEACCESSPERMISSION)`
The operation id for the '*Is Same*' operation.
`static final int`
`[PACKAGE_ACCESS_PERMISSION__ACTION](#PACKAGE_ACCESS_PERMISSION__ACTION)`
The feature id for the '***Action***' attribute.
`static final int`
`[PACKAGE_ACCESS_PERMISSION__APPLICATION](#PACKAGE_ACCESS_PERMISSION__APPLICATION)`
The feature id for the '***Application***' attribute.
`static final int`
`[PACKAGE_ACCESS_PERMISSION__PRINCIPAL](#PACKAGE_ACCESS_PERMISSION__PRINCIPAL)`
The feature id for the '***Principal***' reference.
`static final int`
`[PACKAGE_ACCESS_PERMISSION_FEATURE_COUNT](#PACKAGE_ACCESS_PERMISSION_FEATURE_COUNT)`
The number of structural features of the '*Package Access Permission*' class.
`static final int`
`[PACKAGE_ACCESS_PERMISSION_OPERATION_COUNT](#PACKAGE_ACCESS_PERMISSION_OPERATION_COUNT)`
The number of operations of the '*Package Access Permission*' class.
`static final int`
`[PACKAGE_PERMISSIONS](#PACKAGE_PERMISSIONS)`
The meta object id for the '`*Package Permissions*`' class.
`static final int`
`[PACKAGE_PERMISSIONS___IS_SAME__PACKAGEPERMISSIONS](#PACKAGE_PERMISSIONS___IS_SAME__PACKAGEPERMISSIONS)`
The operation id for the '*Is Same*' operation.
`static final int`
`[PACKAGE_PERMISSIONS__ACCESS_PERMISSIONS](#PACKAGE_PERMISSIONS__ACCESS_PERMISSIONS)`
The feature id for the '***Access Permissions***' containment reference list.
`static final int`
`[PACKAGE_PERMISSIONS__USE_PARENT_PERMISSIONS](#PACKAGE_PERMISSIONS__USE_PARENT_PERMISSIONS)`
The feature id for the '***Use Parent Permissions***' attribute.
`static final int`
`[PACKAGE_PERMISSIONS_FEATURE_COUNT](#PACKAGE_PERMISSIONS_FEATURE_COUNT)`
The number of structural features of the '*Package Permissions*' class.
`static final int`
`[PACKAGE_PERMISSIONS_OPERATION_COUNT](#PACKAGE_PERMISSIONS_OPERATION_COUNT)`
The number of operations of the '*Package Permissions*' class.
`static final int`
`[PRINCIPAL](#PRINCIPAL)`
The meta object id for the '`*Principal*`' class.
`static final int`
`[PRINCIPAL___IS_SAME__PRINCIPAL](#PRINCIPAL___IS_SAME__PRINCIPAL)`
The operation id for the '*Is Same*' operation.
`static final int`
`[PRINCIPAL__NAME](#PRINCIPAL__NAME)`
The feature id for the '***Name***' attribute.
`static final int`
`[PRINCIPAL__PACKAGE_PERMISSIONS](#PRINCIPAL__PACKAGE_PERMISSIONS)`
The feature id for the '***Package Permissions***' reference list.
`static final int`
`[PRINCIPAL_FEATURE_COUNT](#PRINCIPAL_FEATURE_COUNT)`
The number of structural features of the '*Principal*' class.
`static final int`
`[PRINCIPAL_OPERATION_COUNT](#PRINCIPAL_OPERATION_COUNT)`
The number of operations of the '*Principal*' class.
`static final int`
`[PROJECT_SECURITY](#PROJECT_SECURITY)`
The meta object id for the '`*Project Security*`' class.
`static final int`
`[PROJECT_SECURITY___IS_EMPTY](#PROJECT_SECURITY___IS_EMPTY)`
The operation id for the '*Is Empty*' operation.
`static final int`
`[PROJECT_SECURITY__PACKAGE_PERMISSIONS](#PROJECT_SECURITY__PACKAGE_PERMISSIONS)`
The feature id for the '***Package Permissions***' map.
`static final int`
`[PROJECT_SECURITY__PRINCIPALS](#PROJECT_SECURITY__PRINCIPALS)`
The feature id for the '***Principals***' containment reference list.
`static final int`
`[PROJECT_SECURITY_FEATURE_COUNT](#PROJECT_SECURITY_FEATURE_COUNT)`
The number of structural features of the '*Project Security*' class.
`static final int`
`[PROJECT_SECURITY_OPERATION_COUNT](#PROJECT_SECURITY_OPERATION_COUNT)`
The number of operations of the '*Project Security*' class.
`static final int`
`[ROLE_PRINCIPAL](#ROLE_PRINCIPAL)`
The meta object id for the '`*Role Principal*`' class.
`static final int`
`[ROLE_PRINCIPAL___IS_SAME__PRINCIPAL](#ROLE_PRINCIPAL___IS_SAME__PRINCIPAL)`
The operation id for the '*Is Same*' operation.
`static final int`
`[ROLE_PRINCIPAL__NAME](#ROLE_PRINCIPAL__NAME)`
The feature id for the '***Name***' attribute.
`static final int`
`[ROLE_PRINCIPAL__PACKAGE_PERMISSIONS](#ROLE_PRINCIPAL__PACKAGE_PERMISSIONS)`
The feature id for the '***Package Permissions***' reference list.
`static final int`
`[ROLE_PRINCIPAL_FEATURE_COUNT](#ROLE_PRINCIPAL_FEATURE_COUNT)`
The number of structural features of the '*Role Principal*' class.
`static final int`
`[ROLE_PRINCIPAL_OPERATION_COUNT](#ROLE_PRINCIPAL_OPERATION_COUNT)`
The number of operations of the '*Role Principal*' class.
`static final int`
`[STRING_TO_PACKAGE_PERMISSIONS_MAP](#STRING_TO_PACKAGE_PERMISSIONS_MAP)`
The meta object id for the '`*String To Package Permissions Map*`' class.
`static final int`
`[STRING_TO_PACKAGE_PERMISSIONS_MAP__KEY](#STRING_TO_PACKAGE_PERMISSIONS_MAP__KEY)`
The feature id for the '***Key***' attribute.
`static final int`
`[STRING_TO_PACKAGE_PERMISSIONS_MAP__VALUE](#STRING_TO_PACKAGE_PERMISSIONS_MAP__VALUE)`
The feature id for the '***Value***' containment reference.
`static final int`
`[STRING_TO_PACKAGE_PERMISSIONS_MAP_FEATURE_COUNT](#STRING_TO_PACKAGE_PERMISSIONS_MAP_FEATURE_COUNT)`
The number of structural features of the '*String To Package Permissions Map*' class.
`static final int`
`[STRING_TO_PACKAGE_PERMISSIONS_MAP_OPERATION_COUNT](#STRING_TO_PACKAGE_PERMISSIONS_MAP_OPERATION_COUNT)`
The number of operations of the '*String To Package Permissions Map*' class.
`static final int`
`[USER_PRINCIPAL](#USER_PRINCIPAL)`
The meta object id for the '`*User Principal*`' class.
`static final int`
`[USER_PRINCIPAL___IS_SAME__PRINCIPAL](#USER_PRINCIPAL___IS_SAME__PRINCIPAL)`
The operation id for the '*Is Same*' operation.
`static final int`
`[USER_PRINCIPAL__NAME](#USER_PRINCIPAL__NAME)`
The feature id for the '***Name***' attribute.
`static final int`
`[USER_PRINCIPAL__PACKAGE_PERMISSIONS](#USER_PRINCIPAL__PACKAGE_PERMISSIONS)`
The feature id for the '***Package Permissions***' reference list.
`static final int`
`[USER_PRINCIPAL_FEATURE_COUNT](#USER_PRINCIPAL_FEATURE_COUNT)`
The number of structural features of the '*User Principal*' class.
`static final int`
`[USER_PRINCIPAL_OPERATION_COUNT](#USER_PRINCIPAL_OPERATION_COUNT)`
The number of operations of the '*User Principal*' class.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`org.eclipse.emf.ecore.EEnum`
`[getAction](#getAction())()`
Returns the meta object for enum '[`*Action*`](Action.html)'.
`org.eclipse.emf.ecore.EEnum`
`[getApplication](#getApplication())()`
Returns the meta object for enum '[`*Application*`](Application.html)'.
`org.eclipse.emf.ecore.EClass`
`[getEveryonePrincipal](#getEveryonePrincipal())()`
Returns the meta object for class '[`*Everyone Principal*`](EveryonePrincipal.html)'.
`org.eclipse.emf.ecore.EClass`
`[getGroupPrincipal](#getGroupPrincipal())()`
Returns the meta object for class '[`*Group Principal*`](GroupPrincipal.html)'.
`org.eclipse.emf.ecore.EClass`
`[getPackageAccessPermission](#getPackageAccessPermission())()`
Returns the meta object for class '[`*Package Access Permission*`](PackageAccessPermission.html)'.
`org.eclipse.emf.ecore.EOperation`
`[getPackageAccessPermission__IsSame__PackageAccessPermission](#getPackageAccessPermission__IsSame__PackageAccessPermission())()`
Returns the meta object for the '[`*Is Same*`](PackageAccessPermission.html#isSame(com.nomagic.magicdraw.security.PackageAccessPermission))' operation.
`org.eclipse.emf.ecore.EAttribute`
`[getPackageAccessPermission_Action](#getPackageAccessPermission_Action())()`
Returns the meta object for the attribute '[`*Action*`](PackageAccessPermission.html#getAction())'.
`org.eclipse.emf.ecore.EAttribute`
`[getPackageAccessPermission_Application](#getPackageAccessPermission_Application())()`
Returns the meta object for the attribute '[`*Application*`](PackageAccessPermission.html#getApplication())'.
`org.eclipse.emf.ecore.EReference`
`[getPackageAccessPermission_Principal](#getPackageAccessPermission_Principal())()`
Returns the meta object for the reference '[`*Principal*`](PackageAccessPermission.html#getPrincipal())'.
`org.eclipse.emf.ecore.EClass`
`[getPackagePermissions](#getPackagePermissions())()`
Returns the meta object for class '[`*Package Permissions*`](PackagePermissions.html)'.
`org.eclipse.emf.ecore.EOperation`
`[getPackagePermissions__IsSame__PackagePermissions](#getPackagePermissions__IsSame__PackagePermissions())()`
Returns the meta object for the '[`*Is Same*`](PackagePermissions.html#isSame(com.nomagic.magicdraw.security.PackagePermissions))' operation.
`org.eclipse.emf.ecore.EReference`
`[getPackagePermissions_AccessPermissions](#getPackagePermissions_AccessPermissions())()`
Returns the meta object for the containment reference list '[`*Access Permissions*`](PackagePermissions.html#getAccessPermissions())'.
`org.eclipse.emf.ecore.EAttribute`
`[getPackagePermissions_UseParentPermissions](#getPackagePermissions_UseParentPermissions())()`
Returns the meta object for the attribute '[`*Use Parent Permissions*`](PackagePermissions.html#isUseParentPermissions())'.
`org.eclipse.emf.ecore.EClass`
`[getPrincipal](#getPrincipal())()`
Returns the meta object for class '[`*Principal*`](Principal.html)'.
`org.eclipse.emf.ecore.EOperation`
`[getPrincipal__IsSame__Principal](#getPrincipal__IsSame__Principal())()`
Returns the meta object for the '[`*Is Same*`](Principal.html#isSame(com.nomagic.magicdraw.security.Principal))' operation.
`org.eclipse.emf.ecore.EAttribute`
`[getPrincipal_Name](#getPrincipal_Name())()`
Returns the meta object for the attribute '[`*Name*`](Principal.html#getName())'.
`org.eclipse.emf.ecore.EReference`
`[getPrincipal_PackagePermissions](#getPrincipal_PackagePermissions())()`
Returns the meta object for the reference list '[`*Package Permissions*`](Principal.html#getPackagePermissions())'.
`org.eclipse.emf.ecore.EClass`
`[getProjectSecurity](#getProjectSecurity())()`
Returns the meta object for class '[`*Project Security*`](ProjectSecurity.html)'.
`org.eclipse.emf.ecore.EOperation`
`[getProjectSecurity__IsEmpty](#getProjectSecurity__IsEmpty())()`
Returns the meta object for the '[`*Is Empty*`](ProjectSecurity.html#isEmpty())' operation.
`org.eclipse.emf.ecore.EReference`
`[getProjectSecurity_PackagePermissions](#getProjectSecurity_PackagePermissions())()`
Returns the meta object for the map '[`*Package Permissions*`](ProjectSecurity.html#getPackagePermissions())'.
`org.eclipse.emf.ecore.EReference`
`[getProjectSecurity_Principals](#getProjectSecurity_Principals())()`
Returns the meta object for the containment reference list '[`*Principals*`](ProjectSecurity.html#getPrincipals())'.
`org.eclipse.emf.ecore.EClass`
`[getRolePrincipal](#getRolePrincipal())()`
Returns the meta object for class '[`*Role Principal*`](RolePrincipal.html)'.
`[SecurityFactory](SecurityFactory.html)`
`[getSecurityFactory](#getSecurityFactory())()`
Returns the factory that creates the instances of the model.
`org.eclipse.emf.ecore.EClass`
`[getStringToPackagePermissionsMap](#getStringToPackagePermissionsMap())()`
Returns the meta object for class '[`*String To Package Permissions Map*`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.Entry.html)'.
`org.eclipse.emf.ecore.EAttribute`
`[getStringToPackagePermissionsMap_Key](#getStringToPackagePermissionsMap_Key())()`
Returns the meta object for the attribute '[`*Key*`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.Entry.html)'.
`org.eclipse.emf.ecore.EReference`
`[getStringToPackagePermissionsMap_Value](#getStringToPackagePermissionsMap_Value())()`
Returns the meta object for the containment reference '[`*Value*`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.Entry.html)'.
`org.eclipse.emf.ecore.EClass`
`[getUserPrincipal](#getUserPrincipal())()`
Returns the meta object for class '[`*User Principal*`](UserPrincipal.html)'.
Methods inherited from interface org.eclipse.emf.ecore.EModelElement
`getEAnnotation, getEAnnotations`
Methods inherited from interface org.eclipse.emf.ecore.ENamedElement
`getName, setName`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface org.eclipse.emf.ecore.EPackage
`getEClassifier, getEClassifiers, getEFactoryInstance, getESubpackages, getESuperPackage, getNsPrefix, getNsURI, setEFactoryInstance, setNsPrefix, setNsURI`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`

============ FIELD DETAIL =========== 
Field Details
eNAME
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) eNAME
The package name.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.eNAME)
Generated:
eNS_URI
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) eNS_URI
The package namespace URI.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.eNS_URI)
Generated:
eNS_PREFIX
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) eNS_PREFIX
The package namespace name.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.eNS_PREFIX)
Generated:
eINSTANCE
static final [SecurityPackage](SecurityPackage.html) eINSTANCE
The singleton instance of the package.
 begin-user-doc 
 end-user-doc
Generated:
PROJECT_SECURITY
static final int PROJECT_SECURITY
The meta object id for the '`*Project Security*`' class.
 begin-user-doc 
 end-user-doc
See Also:
`ProjectSecurityImpl`
`SecurityPackageImpl.getProjectSecurity()`
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PROJECT_SECURITY)
Generated:
PROJECT_SECURITY__PACKAGE_PERMISSIONS
static final int PROJECT_SECURITY__PACKAGE_PERMISSIONS
The feature id for the '***Package Permissions***' map.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PROJECT_SECURITY__PACKAGE_PERMISSIONS)
Generated:
PROJECT_SECURITY__PRINCIPALS
static final int PROJECT_SECURITY__PRINCIPALS
The feature id for the '***Principals***' containment reference list.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PROJECT_SECURITY__PRINCIPALS)
Generated:
PROJECT_SECURITY_FEATURE_COUNT
static final int PROJECT_SECURITY_FEATURE_COUNT
The number of structural features of the '*Project Security*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PROJECT_SECURITY_FEATURE_COUNT)
Generated:
PROJECT_SECURITY___IS_EMPTY
static final int PROJECT_SECURITY___IS_EMPTY
The operation id for the '*Is Empty*' operation.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PROJECT_SECURITY___IS_EMPTY)
Generated:
PROJECT_SECURITY_OPERATION_COUNT
static final int PROJECT_SECURITY_OPERATION_COUNT
The number of operations of the '*Project Security*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PROJECT_SECURITY_OPERATION_COUNT)
Generated:
PACKAGE_ACCESS_PERMISSION
static final int PACKAGE_ACCESS_PERMISSION
The meta object id for the '`*Package Access Permission*`' class.
 begin-user-doc 
 end-user-doc
See Also:
`PackageAccessPermissionImpl`
`SecurityPackageImpl.getPackageAccessPermission()`
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_ACCESS_PERMISSION)
Generated:
PACKAGE_ACCESS_PERMISSION__ACTION
static final int PACKAGE_ACCESS_PERMISSION__ACTION
The feature id for the '***Action***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_ACCESS_PERMISSION__ACTION)
Generated:
PACKAGE_ACCESS_PERMISSION__APPLICATION
static final int PACKAGE_ACCESS_PERMISSION__APPLICATION
The feature id for the '***Application***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_ACCESS_PERMISSION__APPLICATION)
Generated:
PACKAGE_ACCESS_PERMISSION__PRINCIPAL
static final int PACKAGE_ACCESS_PERMISSION__PRINCIPAL
The feature id for the '***Principal***' reference.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_ACCESS_PERMISSION__PRINCIPAL)
Generated:
PACKAGE_ACCESS_PERMISSION_FEATURE_COUNT
static final int PACKAGE_ACCESS_PERMISSION_FEATURE_COUNT
The number of structural features of the '*Package Access Permission*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_ACCESS_PERMISSION_FEATURE_COUNT)
Generated:
PACKAGE_ACCESS_PERMISSION___IS_SAME__PACKAGEACCESSPERMISSION
static final int PACKAGE_ACCESS_PERMISSION___IS_SAME__PACKAGEACCESSPERMISSION
The operation id for the '*Is Same*' operation.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_ACCESS_PERMISSION___IS_SAME__PACKAGEACCESSPERMISSION)
Generated:
PACKAGE_ACCESS_PERMISSION_OPERATION_COUNT
static final int PACKAGE_ACCESS_PERMISSION_OPERATION_COUNT
The number of operations of the '*Package Access Permission*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_ACCESS_PERMISSION_OPERATION_COUNT)
Generated:
STRING_TO_PACKAGE_PERMISSIONS_MAP
static final int STRING_TO_PACKAGE_PERMISSIONS_MAP
The meta object id for the '`*String To Package Permissions Map*`' class.
 begin-user-doc 
 end-user-doc
See Also:
`StringToPackagePermissionsMapImpl`
`SecurityPackageImpl.getStringToPackagePermissionsMap()`
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.STRING_TO_PACKAGE_PERMISSIONS_MAP)
Generated:
STRING_TO_PACKAGE_PERMISSIONS_MAP__KEY
static final int STRING_TO_PACKAGE_PERMISSIONS_MAP__KEY
The feature id for the '***Key***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.STRING_TO_PACKAGE_PERMISSIONS_MAP__KEY)
Generated:
STRING_TO_PACKAGE_PERMISSIONS_MAP__VALUE
static final int STRING_TO_PACKAGE_PERMISSIONS_MAP__VALUE
The feature id for the '***Value***' containment reference.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.STRING_TO_PACKAGE_PERMISSIONS_MAP__VALUE)
Generated:
STRING_TO_PACKAGE_PERMISSIONS_MAP_FEATURE_COUNT
static final int STRING_TO_PACKAGE_PERMISSIONS_MAP_FEATURE_COUNT
The number of structural features of the '*String To Package Permissions Map*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.STRING_TO_PACKAGE_PERMISSIONS_MAP_FEATURE_COUNT)
Generated:
STRING_TO_PACKAGE_PERMISSIONS_MAP_OPERATION_COUNT
static final int STRING_TO_PACKAGE_PERMISSIONS_MAP_OPERATION_COUNT
The number of operations of the '*String To Package Permissions Map*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.STRING_TO_PACKAGE_PERMISSIONS_MAP_OPERATION_COUNT)
Generated:
PACKAGE_PERMISSIONS
static final int PACKAGE_PERMISSIONS
The meta object id for the '`*Package Permissions*`' class.
 begin-user-doc 
 end-user-doc
See Also:
`PackagePermissionsImpl`
`SecurityPackageImpl.getPackagePermissions()`
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_PERMISSIONS)
Generated:
PACKAGE_PERMISSIONS__ACCESS_PERMISSIONS
static final int PACKAGE_PERMISSIONS__ACCESS_PERMISSIONS
The feature id for the '***Access Permissions***' containment reference list.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_PERMISSIONS__ACCESS_PERMISSIONS)
Generated:
PACKAGE_PERMISSIONS__USE_PARENT_PERMISSIONS
static final int PACKAGE_PERMISSIONS__USE_PARENT_PERMISSIONS
The feature id for the '***Use Parent Permissions***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_PERMISSIONS__USE_PARENT_PERMISSIONS)
Generated:
PACKAGE_PERMISSIONS_FEATURE_COUNT
static final int PACKAGE_PERMISSIONS_FEATURE_COUNT
The number of structural features of the '*Package Permissions*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_PERMISSIONS_FEATURE_COUNT)
Generated:
PACKAGE_PERMISSIONS___IS_SAME__PACKAGEPERMISSIONS
static final int PACKAGE_PERMISSIONS___IS_SAME__PACKAGEPERMISSIONS
The operation id for the '*Is Same*' operation.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_PERMISSIONS___IS_SAME__PACKAGEPERMISSIONS)
Generated:
PACKAGE_PERMISSIONS_OPERATION_COUNT
static final int PACKAGE_PERMISSIONS_OPERATION_COUNT
The number of operations of the '*Package Permissions*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_PERMISSIONS_OPERATION_COUNT)
Generated:
PRINCIPAL
static final int PRINCIPAL
The meta object id for the '`*Principal*`' class.
 begin-user-doc 
 end-user-doc
See Also:
`PrincipalImpl`
`SecurityPackageImpl.getPrincipal()`
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PRINCIPAL)
Generated:
PRINCIPAL__NAME
static final int PRINCIPAL__NAME
The feature id for the '***Name***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PRINCIPAL__NAME)
Generated:
PRINCIPAL__PACKAGE_PERMISSIONS
static final int PRINCIPAL__PACKAGE_PERMISSIONS
The feature id for the '***Package Permissions***' reference list.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PRINCIPAL__PACKAGE_PERMISSIONS)
Generated:
PRINCIPAL_FEATURE_COUNT
static final int PRINCIPAL_FEATURE_COUNT
The number of structural features of the '*Principal*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PRINCIPAL_FEATURE_COUNT)
Generated:
PRINCIPAL___IS_SAME__PRINCIPAL
static final int PRINCIPAL___IS_SAME__PRINCIPAL
The operation id for the '*Is Same*' operation.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PRINCIPAL___IS_SAME__PRINCIPAL)
Generated:
PRINCIPAL_OPERATION_COUNT
static final int PRINCIPAL_OPERATION_COUNT
The number of operations of the '*Principal*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PRINCIPAL_OPERATION_COUNT)
Generated:
USER_PRINCIPAL
static final int USER_PRINCIPAL
The meta object id for the '`*User Principal*`' class.
 begin-user-doc 
 end-user-doc
See Also:
`UserPrincipalImpl`
`SecurityPackageImpl.getUserPrincipal()`
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.USER_PRINCIPAL)
Generated:
USER_PRINCIPAL__NAME
static final int USER_PRINCIPAL__NAME
The feature id for the '***Name***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.USER_PRINCIPAL__NAME)
Generated:
USER_PRINCIPAL__PACKAGE_PERMISSIONS
static final int USER_PRINCIPAL__PACKAGE_PERMISSIONS
The feature id for the '***Package Permissions***' reference list.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.USER_PRINCIPAL__PACKAGE_PERMISSIONS)
Generated:
USER_PRINCIPAL_FEATURE_COUNT
static final int USER_PRINCIPAL_FEATURE_COUNT
The number of structural features of the '*User Principal*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.USER_PRINCIPAL_FEATURE_COUNT)
Generated:
USER_PRINCIPAL___IS_SAME__PRINCIPAL
static final int USER_PRINCIPAL___IS_SAME__PRINCIPAL
The operation id for the '*Is Same*' operation.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.USER_PRINCIPAL___IS_SAME__PRINCIPAL)
Generated:
USER_PRINCIPAL_OPERATION_COUNT
static final int USER_PRINCIPAL_OPERATION_COUNT
The number of operations of the '*User Principal*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.USER_PRINCIPAL_OPERATION_COUNT)
Generated:
GROUP_PRINCIPAL
static final int GROUP_PRINCIPAL
The meta object id for the '`*Group Principal*`' class.
 begin-user-doc 
 end-user-doc
See Also:
`GroupPrincipalImpl`
`SecurityPackageImpl.getGroupPrincipal()`
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.GROUP_PRINCIPAL)
Generated:
GROUP_PRINCIPAL__NAME
static final int GROUP_PRINCIPAL__NAME
The feature id for the '***Name***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.GROUP_PRINCIPAL__NAME)
Generated:
GROUP_PRINCIPAL__PACKAGE_PERMISSIONS
static final int GROUP_PRINCIPAL__PACKAGE_PERMISSIONS
The feature id for the '***Package Permissions***' reference list.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.GROUP_PRINCIPAL__PACKAGE_PERMISSIONS)
Generated:
GROUP_PRINCIPAL_FEATURE_COUNT
static final int GROUP_PRINCIPAL_FEATURE_COUNT
The number of structural features of the '*Group Principal*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.GROUP_PRINCIPAL_FEATURE_COUNT)
Generated:
GROUP_PRINCIPAL___IS_SAME__PRINCIPAL
static final int GROUP_PRINCIPAL___IS_SAME__PRINCIPAL
The operation id for the '*Is Same*' operation.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.GROUP_PRINCIPAL___IS_SAME__PRINCIPAL)
Generated:
GROUP_PRINCIPAL_OPERATION_COUNT
static final int GROUP_PRINCIPAL_OPERATION_COUNT
The number of operations of the '*Group Principal*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.GROUP_PRINCIPAL_OPERATION_COUNT)
Generated:
ROLE_PRINCIPAL
static final int ROLE_PRINCIPAL
The meta object id for the '`*Role Principal*`' class.
 begin-user-doc 
 end-user-doc
See Also:
`RolePrincipalImpl`
`SecurityPackageImpl.getRolePrincipal()`
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.ROLE_PRINCIPAL)
Generated:
ROLE_PRINCIPAL__NAME
static final int ROLE_PRINCIPAL__NAME
The feature id for the '***Name***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.ROLE_PRINCIPAL__NAME)
Generated:
ROLE_PRINCIPAL__PACKAGE_PERMISSIONS
static final int ROLE_PRINCIPAL__PACKAGE_PERMISSIONS
The feature id for the '***Package Permissions***' reference list.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.ROLE_PRINCIPAL__PACKAGE_PERMISSIONS)
Generated:
ROLE_PRINCIPAL_FEATURE_COUNT
static final int ROLE_PRINCIPAL_FEATURE_COUNT
The number of structural features of the '*Role Principal*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.ROLE_PRINCIPAL_FEATURE_COUNT)
Generated:
ROLE_PRINCIPAL___IS_SAME__PRINCIPAL
static final int ROLE_PRINCIPAL___IS_SAME__PRINCIPAL
The operation id for the '*Is Same*' operation.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.ROLE_PRINCIPAL___IS_SAME__PRINCIPAL)
Generated:
ROLE_PRINCIPAL_OPERATION_COUNT
static final int ROLE_PRINCIPAL_OPERATION_COUNT
The number of operations of the '*Role Principal*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.ROLE_PRINCIPAL_OPERATION_COUNT)
Generated:
EVERYONE_PRINCIPAL
static final int EVERYONE_PRINCIPAL
The meta object id for the '`*Everyone Principal*`' class.
 begin-user-doc 
 end-user-doc
See Also:
`EveryonePrincipalImpl`
`SecurityPackageImpl.getEveryonePrincipal()`
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.EVERYONE_PRINCIPAL)
Generated:
EVERYONE_PRINCIPAL__NAME
static final int EVERYONE_PRINCIPAL__NAME
The feature id for the '***Name***' attribute.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.EVERYONE_PRINCIPAL__NAME)
Generated:
EVERYONE_PRINCIPAL__PACKAGE_PERMISSIONS
static final int EVERYONE_PRINCIPAL__PACKAGE_PERMISSIONS
The feature id for the '***Package Permissions***' reference list.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.EVERYONE_PRINCIPAL__PACKAGE_PERMISSIONS)
Generated:
EVERYONE_PRINCIPAL_FEATURE_COUNT
static final int EVERYONE_PRINCIPAL_FEATURE_COUNT
The number of structural features of the '*Everyone Principal*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.EVERYONE_PRINCIPAL_FEATURE_COUNT)
Generated:
EVERYONE_PRINCIPAL___IS_SAME__PRINCIPAL
static final int EVERYONE_PRINCIPAL___IS_SAME__PRINCIPAL
The operation id for the '*Is Same*' operation.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.EVERYONE_PRINCIPAL___IS_SAME__PRINCIPAL)
Generated:
EVERYONE_PRINCIPAL_OPERATION_COUNT
static final int EVERYONE_PRINCIPAL_OPERATION_COUNT
The number of operations of the '*Everyone Principal*' class.
 begin-user-doc 
 end-user-doc
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.EVERYONE_PRINCIPAL_OPERATION_COUNT)
Generated:
ACTION
static final int ACTION
The meta object id for the '[`*Action*`](Action.html)' enum.
 begin-user-doc 
 end-user-doc
See Also:
[`Action`](Action.html)
`SecurityPackageImpl.getAction()`
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.ACTION)
Generated:
APPLICATION
static final int APPLICATION
The meta object id for the '[`*Application*`](Application.html)' enum.
 begin-user-doc 
 end-user-doc
See Also:
[`Application`](Application.html)
`SecurityPackageImpl.getApplication()`
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.APPLICATION)
Generated:
 ============ METHOD DETAIL ========== 
Method Details
getProjectSecurity
org.eclipse.emf.ecore.EClass getProjectSecurity()
Returns the meta object for class '[`*Project Security*`](ProjectSecurity.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for class '*Project Security*'.
See Also:
[`ProjectSecurity`](ProjectSecurity.html)
Generated:
getProjectSecurity_PackagePermissions
org.eclipse.emf.ecore.EReference getProjectSecurity_PackagePermissions()
Returns the meta object for the map '[`*Package Permissions*`](ProjectSecurity.html#getPackagePermissions())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the map '*Package Permissions*'.
See Also:
[`ProjectSecurity.getPackagePermissions()`](ProjectSecurity.html#getPackagePermissions())
[`getProjectSecurity()`](#getProjectSecurity())
Generated:
getProjectSecurity_Principals
org.eclipse.emf.ecore.EReference getProjectSecurity_Principals()
Returns the meta object for the containment reference list '[`*Principals*`](ProjectSecurity.html#getPrincipals())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the containment reference list '*Principals*'.
See Also:
[`ProjectSecurity.getPrincipals()`](ProjectSecurity.html#getPrincipals())
[`getProjectSecurity()`](#getProjectSecurity())
Generated:
getProjectSecurity__IsEmpty
org.eclipse.emf.ecore.EOperation getProjectSecurity__IsEmpty()
Returns the meta object for the '[`*Is Empty*`](ProjectSecurity.html#isEmpty())' operation.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the '*Is Empty*' operation.
See Also:
[`ProjectSecurity.isEmpty()`](ProjectSecurity.html#isEmpty())
Generated:
getPackageAccessPermission
org.eclipse.emf.ecore.EClass getPackageAccessPermission()
Returns the meta object for class '[`*Package Access Permission*`](PackageAccessPermission.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for class '*Package Access Permission*'.
See Also:
[`PackageAccessPermission`](PackageAccessPermission.html)
Generated:
getPackageAccessPermission_Action
org.eclipse.emf.ecore.EAttribute getPackageAccessPermission_Action()
Returns the meta object for the attribute '[`*Action*`](PackageAccessPermission.html#getAction())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*Action*'.
See Also:
[`PackageAccessPermission.getAction()`](PackageAccessPermission.html#getAction())
[`getPackageAccessPermission()`](#getPackageAccessPermission())
Generated:
getPackageAccessPermission_Application
org.eclipse.emf.ecore.EAttribute getPackageAccessPermission_Application()
Returns the meta object for the attribute '[`*Application*`](PackageAccessPermission.html#getApplication())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*Application*'.
See Also:
[`PackageAccessPermission.getApplication()`](PackageAccessPermission.html#getApplication())
[`getPackageAccessPermission()`](#getPackageAccessPermission())
Generated:
getPackageAccessPermission_Principal
org.eclipse.emf.ecore.EReference getPackageAccessPermission_Principal()
Returns the meta object for the reference '[`*Principal*`](PackageAccessPermission.html#getPrincipal())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the reference '*Principal*'.
See Also:
[`PackageAccessPermission.getPrincipal()`](PackageAccessPermission.html#getPrincipal())
[`getPackageAccessPermission()`](#getPackageAccessPermission())
Generated:
getPackageAccessPermission__IsSame__PackageAccessPermission
org.eclipse.emf.ecore.EOperation getPackageAccessPermission__IsSame__PackageAccessPermission()
Returns the meta object for the '[`*Is Same*`](PackageAccessPermission.html#isSame(com.nomagic.magicdraw.security.PackageAccessPermission))' operation.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the '*Is Same*' operation.
See Also:
[`PackageAccessPermission.isSame(com.nomagic.magicdraw.security.PackageAccessPermission)`](PackageAccessPermission.html#isSame(com.nomagic.magicdraw.security.PackageAccessPermission))
Generated:
getStringToPackagePermissionsMap
org.eclipse.emf.ecore.EClass getStringToPackagePermissionsMap()
Returns the meta object for class '[`*String To Package Permissions Map*`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.Entry.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for class '*String To Package Permissions Map*'.
See Also:
[`Map.Entry`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.Entry.html)
Model:
keyDataType="org.eclipse.emf.ecore.EString"
 valueType="com.nomagic.magicdraw.security.PackagePermissions" valueContainment="true" valueResolveProxies="true"
Generated:
getStringToPackagePermissionsMap_Key
org.eclipse.emf.ecore.EAttribute getStringToPackagePermissionsMap_Key()
Returns the meta object for the attribute '[`*Key*`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.Entry.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*Key*'.
See Also:
[`Map.Entry`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.Entry.html)
[`getStringToPackagePermissionsMap()`](#getStringToPackagePermissionsMap())
Generated:
getStringToPackagePermissionsMap_Value
org.eclipse.emf.ecore.EReference getStringToPackagePermissionsMap_Value()
Returns the meta object for the containment reference '[`*Value*`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.Entry.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the containment reference '*Value*'.
See Also:
[`Map.Entry`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.Entry.html)
[`getStringToPackagePermissionsMap()`](#getStringToPackagePermissionsMap())
Generated:
getPackagePermissions
org.eclipse.emf.ecore.EClass getPackagePermissions()
Returns the meta object for class '[`*Package Permissions*`](PackagePermissions.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for class '*Package Permissions*'.
See Also:
[`PackagePermissions`](PackagePermissions.html)
Generated:
getPackagePermissions_AccessPermissions
org.eclipse.emf.ecore.EReference getPackagePermissions_AccessPermissions()
Returns the meta object for the containment reference list '[`*Access Permissions*`](PackagePermissions.html#getAccessPermissions())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the containment reference list '*Access Permissions*'.
See Also:
[`PackagePermissions.getAccessPermissions()`](PackagePermissions.html#getAccessPermissions())
[`getPackagePermissions()`](#getPackagePermissions())
Generated:
getPackagePermissions_UseParentPermissions
org.eclipse.emf.ecore.EAttribute getPackagePermissions_UseParentPermissions()
Returns the meta object for the attribute '[`*Use Parent Permissions*`](PackagePermissions.html#isUseParentPermissions())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*Use Parent Permissions*'.
See Also:
[`PackagePermissions.isUseParentPermissions()`](PackagePermissions.html#isUseParentPermissions())
[`getPackagePermissions()`](#getPackagePermissions())
Generated:
getPackagePermissions__IsSame__PackagePermissions
org.eclipse.emf.ecore.EOperation getPackagePermissions__IsSame__PackagePermissions()
Returns the meta object for the '[`*Is Same*`](PackagePermissions.html#isSame(com.nomagic.magicdraw.security.PackagePermissions))' operation.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the '*Is Same*' operation.
See Also:
[`PackagePermissions.isSame(com.nomagic.magicdraw.security.PackagePermissions)`](PackagePermissions.html#isSame(com.nomagic.magicdraw.security.PackagePermissions))
Generated:
getPrincipal
org.eclipse.emf.ecore.EClass getPrincipal()
Returns the meta object for class '[`*Principal*`](Principal.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for class '*Principal*'.
See Also:
[`Principal`](Principal.html)
Generated:
getPrincipal_Name
org.eclipse.emf.ecore.EAttribute getPrincipal_Name()
Returns the meta object for the attribute '[`*Name*`](Principal.html#getName())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the attribute '*Name*'.
See Also:
[`Principal.getName()`](Principal.html#getName())
[`getPrincipal()`](#getPrincipal())
Generated:
getPrincipal_PackagePermissions
org.eclipse.emf.ecore.EReference getPrincipal_PackagePermissions()
Returns the meta object for the reference list '[`*Package Permissions*`](Principal.html#getPackagePermissions())'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the reference list '*Package Permissions*'.
See Also:
[`Principal.getPackagePermissions()`](Principal.html#getPackagePermissions())
[`getPrincipal()`](#getPrincipal())
Generated:
getPrincipal__IsSame__Principal
org.eclipse.emf.ecore.EOperation getPrincipal__IsSame__Principal()
Returns the meta object for the '[`*Is Same*`](Principal.html#isSame(com.nomagic.magicdraw.security.Principal))' operation.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for the '*Is Same*' operation.
See Also:
[`Principal.isSame(com.nomagic.magicdraw.security.Principal)`](Principal.html#isSame(com.nomagic.magicdraw.security.Principal))
Generated:
getUserPrincipal
org.eclipse.emf.ecore.EClass getUserPrincipal()
Returns the meta object for class '[`*User Principal*`](UserPrincipal.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for class '*User Principal*'.
See Also:
[`UserPrincipal`](UserPrincipal.html)
Generated:
getGroupPrincipal
org.eclipse.emf.ecore.EClass getGroupPrincipal()
Returns the meta object for class '[`*Group Principal*`](GroupPrincipal.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for class '*Group Principal*'.
See Also:
[`GroupPrincipal`](GroupPrincipal.html)
Generated:
getRolePrincipal
org.eclipse.emf.ecore.EClass getRolePrincipal()
Returns the meta object for class '[`*Role Principal*`](RolePrincipal.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for class '*Role Principal*'.
See Also:
[`RolePrincipal`](RolePrincipal.html)
Generated:
getEveryonePrincipal
org.eclipse.emf.ecore.EClass getEveryonePrincipal()
Returns the meta object for class '[`*Everyone Principal*`](EveryonePrincipal.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for class '*Everyone Principal*'.
See Also:
[`EveryonePrincipal`](EveryonePrincipal.html)
Generated:
getAction
org.eclipse.emf.ecore.EEnum getAction()
Returns the meta object for enum '[`*Action*`](Action.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for enum '*Action*'.
See Also:
[`Action`](Action.html)
Generated:
getApplication
org.eclipse.emf.ecore.EEnum getApplication()
Returns the meta object for enum '[`*Application*`](Application.html)'.
 begin-user-doc 
 end-user-doc
Returns:
the meta object for enum '*Application*'.
See Also:
[`Application`](Application.html)
Generated:
getSecurityFactory
[SecurityFactory](SecurityFactory.html) getSecurityFactory()
Returns the factory that creates the instances of the model.
 begin-user-doc 
 end-user-doc
Returns:
the factory that creates the instances of the model.
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.security</a></div>
<h1 class="title" title="Interface SecurityPackage">Interface SecurityPackage</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>org.eclipse.emf.ecore.EModelElement</code>, <code>org.eclipse.emf.ecore.ENamedElement</code>, <code>org.eclipse.emf.ecore.EObject</code>, <code>org.eclipse.emf.ecore.EPackage</code>, <code>org.eclipse.emf.common.notify.Notifier</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">SecurityPackage</span><span class="extends-implements">
extends org.eclipse.emf.ecore.EPackage</span></div>
<div class="block"><!-- begin-user-doc -->
 The <b>Package</b> for the model.
 It contains accessors for the meta objects to represent
 <ul>
<li>each class,</li>
<li>each feature of each class,</li>
<li>each operation of each class,</li>
<li>each enum,</li>
<li>and each data type</li>
</ul>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="SecurityFactory.html" title="interface in com.nomagic.magicdraw.security"><code>SecurityFactory</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>kind="package"</dd>
<dt>Generated:</dt>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Interface</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SecurityPackage.Literals.html" title="interface in com.nomagic.magicdraw.security">SecurityPackage.Literals</a></code></div>
<div class="col-last even-row-color">
<div class="block">Defines literals for the meta objects that represent
 
 each class,
 each feature of each class,
 each operation of each class,
 each enum,
 and each data type
 
 <!-- end-user-doc --></div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ACTION">ACTION</a></code></div>
<div class="col-last even-row-color">
<div class="block">The meta object id for the '<a href="Action.html" title="enum class in com.nomagic.magicdraw.security"><code><em>Action</em></code></a>' enum.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#APPLICATION">APPLICATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The meta object id for the '<a href="Application.html" title="enum class in com.nomagic.magicdraw.security"><code><em>Application</em></code></a>' enum.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="SecurityPackage.html" title="interface in com.nomagic.magicdraw.security">SecurityPackage</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#eINSTANCE">eINSTANCE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The singleton instance of the package.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#eNAME">eNAME</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The package name.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#eNS_PREFIX">eNS_PREFIX</a></code></div>
<div class="col-last even-row-color">
<div class="block">The package namespace name.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#eNS_URI">eNS_URI</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The package namespace URI.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EVERYONE_PRINCIPAL">EVERYONE_PRINCIPAL</a></code></div>
<div class="col-last even-row-color">
<div class="block">The meta object id for the '<code><em>Everyone Principal</em></code>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EVERYONE_PRINCIPAL___IS_SAME__PRINCIPAL">EVERYONE_PRINCIPAL___IS_SAME__PRINCIPAL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The operation id for the '<em>Is Same</em>' operation.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EVERYONE_PRINCIPAL__NAME">EVERYONE_PRINCIPAL__NAME</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>Name</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EVERYONE_PRINCIPAL__PACKAGE_PERMISSIONS">EVERYONE_PRINCIPAL__PACKAGE_PERMISSIONS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Package Permissions</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EVERYONE_PRINCIPAL_FEATURE_COUNT">EVERYONE_PRINCIPAL_FEATURE_COUNT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The number of structural features of the '<em>Everyone Principal</em>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EVERYONE_PRINCIPAL_OPERATION_COUNT">EVERYONE_PRINCIPAL_OPERATION_COUNT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The number of operations of the '<em>Everyone Principal</em>' class.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#GROUP_PRINCIPAL">GROUP_PRINCIPAL</a></code></div>
<div class="col-last even-row-color">
<div class="block">The meta object id for the '<code><em>Group Principal</em></code>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#GROUP_PRINCIPAL___IS_SAME__PRINCIPAL">GROUP_PRINCIPAL___IS_SAME__PRINCIPAL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The operation id for the '<em>Is Same</em>' operation.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#GROUP_PRINCIPAL__NAME">GROUP_PRINCIPAL__NAME</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>Name</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#GROUP_PRINCIPAL__PACKAGE_PERMISSIONS">GROUP_PRINCIPAL__PACKAGE_PERMISSIONS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Package Permissions</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#GROUP_PRINCIPAL_FEATURE_COUNT">GROUP_PRINCIPAL_FEATURE_COUNT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The number of structural features of the '<em>Group Principal</em>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#GROUP_PRINCIPAL_OPERATION_COUNT">GROUP_PRINCIPAL_OPERATION_COUNT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The number of operations of the '<em>Group Principal</em>' class.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PACKAGE_ACCESS_PERMISSION">PACKAGE_ACCESS_PERMISSION</a></code></div>
<div class="col-last even-row-color">
<div class="block">The meta object id for the '<code><em>Package Access Permission</em></code>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PACKAGE_ACCESS_PERMISSION___IS_SAME__PACKAGEACCESSPERMISSION">PACKAGE_ACCESS_PERMISSION___IS_SAME__PACKAGEACCESSPERMISSION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The operation id for the '<em>Is Same</em>' operation.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PACKAGE_ACCESS_PERMISSION__ACTION">PACKAGE_ACCESS_PERMISSION__ACTION</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>Action</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PACKAGE_ACCESS_PERMISSION__APPLICATION">PACKAGE_ACCESS_PERMISSION__APPLICATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Application</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PACKAGE_ACCESS_PERMISSION__PRINCIPAL">PACKAGE_ACCESS_PERMISSION__PRINCIPAL</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>Principal</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PACKAGE_ACCESS_PERMISSION_FEATURE_COUNT">PACKAGE_ACCESS_PERMISSION_FEATURE_COUNT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The number of structural features of the '<em>Package Access Permission</em>' class.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PACKAGE_ACCESS_PERMISSION_OPERATION_COUNT">PACKAGE_ACCESS_PERMISSION_OPERATION_COUNT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The number of operations of the '<em>Package Access Permission</em>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PACKAGE_PERMISSIONS">PACKAGE_PERMISSIONS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The meta object id for the '<code><em>Package Permissions</em></code>' class.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PACKAGE_PERMISSIONS___IS_SAME__PACKAGEPERMISSIONS">PACKAGE_PERMISSIONS___IS_SAME__PACKAGEPERMISSIONS</a></code></div>
<div class="col-last even-row-color">
<div class="block">The operation id for the '<em>Is Same</em>' operation.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PACKAGE_PERMISSIONS__ACCESS_PERMISSIONS">PACKAGE_PERMISSIONS__ACCESS_PERMISSIONS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Access Permissions</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PACKAGE_PERMISSIONS__USE_PARENT_PERMISSIONS">PACKAGE_PERMISSIONS__USE_PARENT_PERMISSIONS</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>Use Parent Permissions</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PACKAGE_PERMISSIONS_FEATURE_COUNT">PACKAGE_PERMISSIONS_FEATURE_COUNT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The number of structural features of the '<em>Package Permissions</em>' class.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PACKAGE_PERMISSIONS_OPERATION_COUNT">PACKAGE_PERMISSIONS_OPERATION_COUNT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The number of operations of the '<em>Package Permissions</em>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PRINCIPAL">PRINCIPAL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The meta object id for the '<code><em>Principal</em></code>' class.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PRINCIPAL___IS_SAME__PRINCIPAL">PRINCIPAL___IS_SAME__PRINCIPAL</a></code></div>
<div class="col-last even-row-color">
<div class="block">The operation id for the '<em>Is Same</em>' operation.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PRINCIPAL__NAME">PRINCIPAL__NAME</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Name</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PRINCIPAL__PACKAGE_PERMISSIONS">PRINCIPAL__PACKAGE_PERMISSIONS</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>Package Permissions</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PRINCIPAL_FEATURE_COUNT">PRINCIPAL_FEATURE_COUNT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The number of structural features of the '<em>Principal</em>' class.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PRINCIPAL_OPERATION_COUNT">PRINCIPAL_OPERATION_COUNT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The number of operations of the '<em>Principal</em>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROJECT_SECURITY">PROJECT_SECURITY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The meta object id for the '<code><em>Project Security</em></code>' class.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROJECT_SECURITY___IS_EMPTY">PROJECT_SECURITY___IS_EMPTY</a></code></div>
<div class="col-last even-row-color">
<div class="block">The operation id for the '<em>Is Empty</em>' operation.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROJECT_SECURITY__PACKAGE_PERMISSIONS">PROJECT_SECURITY__PACKAGE_PERMISSIONS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Package Permissions</b></em>' map.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROJECT_SECURITY__PRINCIPALS">PROJECT_SECURITY__PRINCIPALS</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>Principals</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROJECT_SECURITY_FEATURE_COUNT">PROJECT_SECURITY_FEATURE_COUNT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The number of structural features of the '<em>Project Security</em>' class.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROJECT_SECURITY_OPERATION_COUNT">PROJECT_SECURITY_OPERATION_COUNT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The number of operations of the '<em>Project Security</em>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ROLE_PRINCIPAL">ROLE_PRINCIPAL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The meta object id for the '<code><em>Role Principal</em></code>' class.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ROLE_PRINCIPAL___IS_SAME__PRINCIPAL">ROLE_PRINCIPAL___IS_SAME__PRINCIPAL</a></code></div>
<div class="col-last even-row-color">
<div class="block">The operation id for the '<em>Is Same</em>' operation.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ROLE_PRINCIPAL__NAME">ROLE_PRINCIPAL__NAME</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Name</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ROLE_PRINCIPAL__PACKAGE_PERMISSIONS">ROLE_PRINCIPAL__PACKAGE_PERMISSIONS</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>Package Permissions</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ROLE_PRINCIPAL_FEATURE_COUNT">ROLE_PRINCIPAL_FEATURE_COUNT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The number of structural features of the '<em>Role Principal</em>' class.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ROLE_PRINCIPAL_OPERATION_COUNT">ROLE_PRINCIPAL_OPERATION_COUNT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The number of operations of the '<em>Role Principal</em>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STRING_TO_PACKAGE_PERMISSIONS_MAP">STRING_TO_PACKAGE_PERMISSIONS_MAP</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The meta object id for the '<code><em>String To Package Permissions Map</em></code>' class.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STRING_TO_PACKAGE_PERMISSIONS_MAP__KEY">STRING_TO_PACKAGE_PERMISSIONS_MAP__KEY</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>Key</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STRING_TO_PACKAGE_PERMISSIONS_MAP__VALUE">STRING_TO_PACKAGE_PERMISSIONS_MAP__VALUE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Value</b></em>' containment reference.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STRING_TO_PACKAGE_PERMISSIONS_MAP_FEATURE_COUNT">STRING_TO_PACKAGE_PERMISSIONS_MAP_FEATURE_COUNT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The number of structural features of the '<em>String To Package Permissions Map</em>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STRING_TO_PACKAGE_PERMISSIONS_MAP_OPERATION_COUNT">STRING_TO_PACKAGE_PERMISSIONS_MAP_OPERATION_COUNT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The number of operations of the '<em>String To Package Permissions Map</em>' class.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#USER_PRINCIPAL">USER_PRINCIPAL</a></code></div>
<div class="col-last even-row-color">
<div class="block">The meta object id for the '<code><em>User Principal</em></code>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#USER_PRINCIPAL___IS_SAME__PRINCIPAL">USER_PRINCIPAL___IS_SAME__PRINCIPAL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The operation id for the '<em>Is Same</em>' operation.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#USER_PRINCIPAL__NAME">USER_PRINCIPAL__NAME</a></code></div>
<div class="col-last even-row-color">
<div class="block">The feature id for the '<em><b>Name</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#USER_PRINCIPAL__PACKAGE_PERMISSIONS">USER_PRINCIPAL__PACKAGE_PERMISSIONS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The feature id for the '<em><b>Package Permissions</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#USER_PRINCIPAL_FEATURE_COUNT">USER_PRINCIPAL_FEATURE_COUNT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The number of structural features of the '<em>User Principal</em>' class.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#USER_PRINCIPAL_OPERATION_COUNT">USER_PRINCIPAL_OPERATION_COUNT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The number of operations of the '<em>User Principal</em>' class.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EEnum</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAction()">getAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for enum '<a href="Action.html" title="enum class in com.nomagic.magicdraw.security"><code><em>Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EEnum</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getApplication()">getApplication</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for enum '<a href="Application.html" title="enum class in com.nomagic.magicdraw.security"><code><em>Application</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EClass</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEveryonePrincipal()">getEveryonePrincipal</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for class '<a href="EveryonePrincipal.html" title="interface in com.nomagic.magicdraw.security"><code><em>Everyone Principal</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EClass</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getGroupPrincipal()">getGroupPrincipal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for class '<a href="GroupPrincipal.html" title="interface in com.nomagic.magicdraw.security"><code><em>Group Principal</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EClass</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPackageAccessPermission()">getPackageAccessPermission</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for class '<a href="PackageAccessPermission.html" title="interface in com.nomagic.magicdraw.security"><code><em>Package Access Permission</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EOperation</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPackageAccessPermission__IsSame__PackageAccessPermission()">getPackageAccessPermission__IsSame__PackageAccessPermission</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the '<a href="PackageAccessPermission.html#isSame(com.nomagic.magicdraw.security.PackageAccessPermission)"><code><em>Is Same</em></code></a>' operation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPackageAccessPermission_Action()">getPackageAccessPermission_Action</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a href="PackageAccessPermission.html#getAction()"><code><em>Action</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPackageAccessPermission_Application()">getPackageAccessPermission_Application</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a href="PackageAccessPermission.html#getApplication()"><code><em>Application</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EReference</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPackageAccessPermission_Principal()">getPackageAccessPermission_Principal</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the reference '<a href="PackageAccessPermission.html#getPrincipal()"><code><em>Principal</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EClass</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPackagePermissions()">getPackagePermissions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for class '<a href="PackagePermissions.html" title="interface in com.nomagic.magicdraw.security"><code><em>Package Permissions</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EOperation</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPackagePermissions__IsSame__PackagePermissions()">getPackagePermissions__IsSame__PackagePermissions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the '<a href="PackagePermissions.html#isSame(com.nomagic.magicdraw.security.PackagePermissions)"><code><em>Is Same</em></code></a>' operation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EReference</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPackagePermissions_AccessPermissions()">getPackagePermissions_AccessPermissions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the containment reference list '<a href="PackagePermissions.html#getAccessPermissions()"><code><em>Access Permissions</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPackagePermissions_UseParentPermissions()">getPackagePermissions_UseParentPermissions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a href="PackagePermissions.html#isUseParentPermissions()"><code><em>Use Parent Permissions</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EClass</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPrincipal()">getPrincipal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for class '<a href="Principal.html" title="interface in com.nomagic.magicdraw.security"><code><em>Principal</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EOperation</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPrincipal__IsSame__Principal()">getPrincipal__IsSame__Principal</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the '<a href="Principal.html#isSame(com.nomagic.magicdraw.security.Principal)"><code><em>Is Same</em></code></a>' operation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPrincipal_Name()">getPrincipal_Name</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a href="Principal.html#getName()"><code><em>Name</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EReference</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPrincipal_PackagePermissions()">getPrincipal_PackagePermissions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the reference list '<a href="Principal.html#getPackagePermissions()"><code><em>Package Permissions</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EClass</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProjectSecurity()">getProjectSecurity</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for class '<a href="ProjectSecurity.html" title="interface in com.nomagic.magicdraw.security"><code><em>Project Security</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EOperation</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProjectSecurity__IsEmpty()">getProjectSecurity__IsEmpty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the '<a href="ProjectSecurity.html#isEmpty()"><code><em>Is Empty</em></code></a>' operation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EReference</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProjectSecurity_PackagePermissions()">getProjectSecurity_PackagePermissions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the map '<a href="ProjectSecurity.html#getPackagePermissions()"><code><em>Package Permissions</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EReference</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProjectSecurity_Principals()">getProjectSecurity_Principals</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the containment reference list '<a href="ProjectSecurity.html#getPrincipals()"><code><em>Principals</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EClass</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRolePrincipal()">getRolePrincipal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for class '<a href="RolePrincipal.html" title="interface in com.nomagic.magicdraw.security"><code><em>Role Principal</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="SecurityFactory.html" title="interface in com.nomagic.magicdraw.security">SecurityFactory</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSecurityFactory()">getSecurityFactory</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the factory that creates the instances of the model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EClass</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getStringToPackagePermissionsMap()">getStringToPackagePermissionsMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for class '<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.Entry.html" title="class or interface in java.util"><code><em>String To Package Permissions Map</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EAttribute</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getStringToPackagePermissionsMap_Key()">getStringToPackagePermissionsMap_Key</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the attribute '<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.Entry.html" title="class or interface in java.util"><code><em>Key</em></code></a>'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EReference</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getStringToPackagePermissionsMap_Value()">getStringToPackagePermissionsMap_Value</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for the containment reference '<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.Entry.html" title="class or interface in java.util"><code><em>Value</em></code></a>'.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.ecore.EClass</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUserPrincipal()">getUserPrincipal</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the meta object for class '<a href="UserPrincipal.html" title="interface in com.nomagic.magicdraw.security"><code><em>User Principal</em></code></a>'.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EModelElement">Methods inherited from interface org.eclipse.emf.ecore.EModelElement</h3>
<code>getEAnnotation, getEAnnotations</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.ENamedElement">Methods inherited from interface org.eclipse.emf.ecore.ENamedElement</h3>
<code>getName, setName</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EPackage">Methods inherited from interface org.eclipse.emf.ecore.EPackage</h3>
<code>getEClassifier, getEClassifiers, getEFactoryInstance, getESubpackages, getESuperPackage, getNsPrefix, getNsURI, setEFactoryInstance, setNsPrefix, setNsURI</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="eNAME">
<h3>eNAME</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">eNAME</span></div>
<div class="block">The package name.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.eNAME">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="eNS_URI">
<h3>eNS_URI</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">eNS_URI</span></div>
<div class="block">The package namespace URI.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.eNS_URI">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="eNS_PREFIX">
<h3>eNS_PREFIX</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">eNS_PREFIX</span></div>
<div class="block">The package namespace name.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.eNS_PREFIX">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="eINSTANCE">
<h3>eINSTANCE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a href="SecurityPackage.html" title="interface in com.nomagic.magicdraw.security">SecurityPackage</a></span> <span class="element-name">eINSTANCE</span></div>
<div class="block">The singleton instance of the package.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROJECT_SECURITY">
<h3>PROJECT_SECURITY</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PROJECT_SECURITY</span></div>
<div class="block">The meta object id for the '<code><em>Project Security</em></code>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><code>ProjectSecurityImpl</code></li>
<li><code>SecurityPackageImpl.getProjectSecurity()</code></li>
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PROJECT_SECURITY">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROJECT_SECURITY__PACKAGE_PERMISSIONS">
<h3>PROJECT_SECURITY__PACKAGE_PERMISSIONS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PROJECT_SECURITY__PACKAGE_PERMISSIONS</span></div>
<div class="block">The feature id for the '<em><b>Package Permissions</b></em>' map.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PROJECT_SECURITY__PACKAGE_PERMISSIONS">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROJECT_SECURITY__PRINCIPALS">
<h3>PROJECT_SECURITY__PRINCIPALS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PROJECT_SECURITY__PRINCIPALS</span></div>
<div class="block">The feature id for the '<em><b>Principals</b></em>' containment reference list.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PROJECT_SECURITY__PRINCIPALS">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROJECT_SECURITY_FEATURE_COUNT">
<h3>PROJECT_SECURITY_FEATURE_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PROJECT_SECURITY_FEATURE_COUNT</span></div>
<div class="block">The number of structural features of the '<em>Project Security</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PROJECT_SECURITY_FEATURE_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROJECT_SECURITY___IS_EMPTY">
<h3>PROJECT_SECURITY___IS_EMPTY</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PROJECT_SECURITY___IS_EMPTY</span></div>
<div class="block">The operation id for the '<em>Is Empty</em>' operation.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PROJECT_SECURITY___IS_EMPTY">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROJECT_SECURITY_OPERATION_COUNT">
<h3>PROJECT_SECURITY_OPERATION_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PROJECT_SECURITY_OPERATION_COUNT</span></div>
<div class="block">The number of operations of the '<em>Project Security</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PROJECT_SECURITY_OPERATION_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PACKAGE_ACCESS_PERMISSION">
<h3>PACKAGE_ACCESS_PERMISSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PACKAGE_ACCESS_PERMISSION</span></div>
<div class="block">The meta object id for the '<code><em>Package Access Permission</em></code>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><code>PackageAccessPermissionImpl</code></li>
<li><code>SecurityPackageImpl.getPackageAccessPermission()</code></li>
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_ACCESS_PERMISSION">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PACKAGE_ACCESS_PERMISSION__ACTION">
<h3>PACKAGE_ACCESS_PERMISSION__ACTION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PACKAGE_ACCESS_PERMISSION__ACTION</span></div>
<div class="block">The feature id for the '<em><b>Action</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_ACCESS_PERMISSION__ACTION">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PACKAGE_ACCESS_PERMISSION__APPLICATION">
<h3>PACKAGE_ACCESS_PERMISSION__APPLICATION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PACKAGE_ACCESS_PERMISSION__APPLICATION</span></div>
<div class="block">The feature id for the '<em><b>Application</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_ACCESS_PERMISSION__APPLICATION">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PACKAGE_ACCESS_PERMISSION__PRINCIPAL">
<h3>PACKAGE_ACCESS_PERMISSION__PRINCIPAL</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PACKAGE_ACCESS_PERMISSION__PRINCIPAL</span></div>
<div class="block">The feature id for the '<em><b>Principal</b></em>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_ACCESS_PERMISSION__PRINCIPAL">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PACKAGE_ACCESS_PERMISSION_FEATURE_COUNT">
<h3>PACKAGE_ACCESS_PERMISSION_FEATURE_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PACKAGE_ACCESS_PERMISSION_FEATURE_COUNT</span></div>
<div class="block">The number of structural features of the '<em>Package Access Permission</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_ACCESS_PERMISSION_FEATURE_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PACKAGE_ACCESS_PERMISSION___IS_SAME__PACKAGEACCESSPERMISSION">
<h3>PACKAGE_ACCESS_PERMISSION___IS_SAME__PACKAGEACCESSPERMISSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PACKAGE_ACCESS_PERMISSION___IS_SAME__PACKAGEACCESSPERMISSION</span></div>
<div class="block">The operation id for the '<em>Is Same</em>' operation.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_ACCESS_PERMISSION___IS_SAME__PACKAGEACCESSPERMISSION">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PACKAGE_ACCESS_PERMISSION_OPERATION_COUNT">
<h3>PACKAGE_ACCESS_PERMISSION_OPERATION_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PACKAGE_ACCESS_PERMISSION_OPERATION_COUNT</span></div>
<div class="block">The number of operations of the '<em>Package Access Permission</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_ACCESS_PERMISSION_OPERATION_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="STRING_TO_PACKAGE_PERMISSIONS_MAP">
<h3>STRING_TO_PACKAGE_PERMISSIONS_MAP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STRING_TO_PACKAGE_PERMISSIONS_MAP</span></div>
<div class="block">The meta object id for the '<code><em>String To Package Permissions Map</em></code>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><code>StringToPackagePermissionsMapImpl</code></li>
<li><code>SecurityPackageImpl.getStringToPackagePermissionsMap()</code></li>
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.STRING_TO_PACKAGE_PERMISSIONS_MAP">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="STRING_TO_PACKAGE_PERMISSIONS_MAP__KEY">
<h3>STRING_TO_PACKAGE_PERMISSIONS_MAP__KEY</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STRING_TO_PACKAGE_PERMISSIONS_MAP__KEY</span></div>
<div class="block">The feature id for the '<em><b>Key</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.STRING_TO_PACKAGE_PERMISSIONS_MAP__KEY">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="STRING_TO_PACKAGE_PERMISSIONS_MAP__VALUE">
<h3>STRING_TO_PACKAGE_PERMISSIONS_MAP__VALUE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STRING_TO_PACKAGE_PERMISSIONS_MAP__VALUE</span></div>
<div class="block">The feature id for the '<em><b>Value</b></em>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.STRING_TO_PACKAGE_PERMISSIONS_MAP__VALUE">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="STRING_TO_PACKAGE_PERMISSIONS_MAP_FEATURE_COUNT">
<h3>STRING_TO_PACKAGE_PERMISSIONS_MAP_FEATURE_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STRING_TO_PACKAGE_PERMISSIONS_MAP_FEATURE_COUNT</span></div>
<div class="block">The number of structural features of the '<em>String To Package Permissions Map</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.STRING_TO_PACKAGE_PERMISSIONS_MAP_FEATURE_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="STRING_TO_PACKAGE_PERMISSIONS_MAP_OPERATION_COUNT">
<h3>STRING_TO_PACKAGE_PERMISSIONS_MAP_OPERATION_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STRING_TO_PACKAGE_PERMISSIONS_MAP_OPERATION_COUNT</span></div>
<div class="block">The number of operations of the '<em>String To Package Permissions Map</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.STRING_TO_PACKAGE_PERMISSIONS_MAP_OPERATION_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PACKAGE_PERMISSIONS">
<h3>PACKAGE_PERMISSIONS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PACKAGE_PERMISSIONS</span></div>
<div class="block">The meta object id for the '<code><em>Package Permissions</em></code>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><code>PackagePermissionsImpl</code></li>
<li><code>SecurityPackageImpl.getPackagePermissions()</code></li>
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_PERMISSIONS">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PACKAGE_PERMISSIONS__ACCESS_PERMISSIONS">
<h3>PACKAGE_PERMISSIONS__ACCESS_PERMISSIONS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PACKAGE_PERMISSIONS__ACCESS_PERMISSIONS</span></div>
<div class="block">The feature id for the '<em><b>Access Permissions</b></em>' containment reference list.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_PERMISSIONS__ACCESS_PERMISSIONS">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PACKAGE_PERMISSIONS__USE_PARENT_PERMISSIONS">
<h3>PACKAGE_PERMISSIONS__USE_PARENT_PERMISSIONS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PACKAGE_PERMISSIONS__USE_PARENT_PERMISSIONS</span></div>
<div class="block">The feature id for the '<em><b>Use Parent Permissions</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_PERMISSIONS__USE_PARENT_PERMISSIONS">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PACKAGE_PERMISSIONS_FEATURE_COUNT">
<h3>PACKAGE_PERMISSIONS_FEATURE_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PACKAGE_PERMISSIONS_FEATURE_COUNT</span></div>
<div class="block">The number of structural features of the '<em>Package Permissions</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_PERMISSIONS_FEATURE_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PACKAGE_PERMISSIONS___IS_SAME__PACKAGEPERMISSIONS">
<h3>PACKAGE_PERMISSIONS___IS_SAME__PACKAGEPERMISSIONS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PACKAGE_PERMISSIONS___IS_SAME__PACKAGEPERMISSIONS</span></div>
<div class="block">The operation id for the '<em>Is Same</em>' operation.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_PERMISSIONS___IS_SAME__PACKAGEPERMISSIONS">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PACKAGE_PERMISSIONS_OPERATION_COUNT">
<h3>PACKAGE_PERMISSIONS_OPERATION_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PACKAGE_PERMISSIONS_OPERATION_COUNT</span></div>
<div class="block">The number of operations of the '<em>Package Permissions</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PACKAGE_PERMISSIONS_OPERATION_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PRINCIPAL">
<h3>PRINCIPAL</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PRINCIPAL</span></div>
<div class="block">The meta object id for the '<code><em>Principal</em></code>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><code>PrincipalImpl</code></li>
<li><code>SecurityPackageImpl.getPrincipal()</code></li>
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PRINCIPAL">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PRINCIPAL__NAME">
<h3>PRINCIPAL__NAME</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PRINCIPAL__NAME</span></div>
<div class="block">The feature id for the '<em><b>Name</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PRINCIPAL__NAME">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PRINCIPAL__PACKAGE_PERMISSIONS">
<h3>PRINCIPAL__PACKAGE_PERMISSIONS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PRINCIPAL__PACKAGE_PERMISSIONS</span></div>
<div class="block">The feature id for the '<em><b>Package Permissions</b></em>' reference list.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PRINCIPAL__PACKAGE_PERMISSIONS">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PRINCIPAL_FEATURE_COUNT">
<h3>PRINCIPAL_FEATURE_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PRINCIPAL_FEATURE_COUNT</span></div>
<div class="block">The number of structural features of the '<em>Principal</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PRINCIPAL_FEATURE_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PRINCIPAL___IS_SAME__PRINCIPAL">
<h3>PRINCIPAL___IS_SAME__PRINCIPAL</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PRINCIPAL___IS_SAME__PRINCIPAL</span></div>
<div class="block">The operation id for the '<em>Is Same</em>' operation.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PRINCIPAL___IS_SAME__PRINCIPAL">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="PRINCIPAL_OPERATION_COUNT">
<h3>PRINCIPAL_OPERATION_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PRINCIPAL_OPERATION_COUNT</span></div>
<div class="block">The number of operations of the '<em>Principal</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.PRINCIPAL_OPERATION_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="USER_PRINCIPAL">
<h3>USER_PRINCIPAL</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">USER_PRINCIPAL</span></div>
<div class="block">The meta object id for the '<code><em>User Principal</em></code>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><code>UserPrincipalImpl</code></li>
<li><code>SecurityPackageImpl.getUserPrincipal()</code></li>
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.USER_PRINCIPAL">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="USER_PRINCIPAL__NAME">
<h3>USER_PRINCIPAL__NAME</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">USER_PRINCIPAL__NAME</span></div>
<div class="block">The feature id for the '<em><b>Name</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.USER_PRINCIPAL__NAME">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="USER_PRINCIPAL__PACKAGE_PERMISSIONS">
<h3>USER_PRINCIPAL__PACKAGE_PERMISSIONS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">USER_PRINCIPAL__PACKAGE_PERMISSIONS</span></div>
<div class="block">The feature id for the '<em><b>Package Permissions</b></em>' reference list.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.USER_PRINCIPAL__PACKAGE_PERMISSIONS">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="USER_PRINCIPAL_FEATURE_COUNT">
<h3>USER_PRINCIPAL_FEATURE_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">USER_PRINCIPAL_FEATURE_COUNT</span></div>
<div class="block">The number of structural features of the '<em>User Principal</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.USER_PRINCIPAL_FEATURE_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="USER_PRINCIPAL___IS_SAME__PRINCIPAL">
<h3>USER_PRINCIPAL___IS_SAME__PRINCIPAL</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">USER_PRINCIPAL___IS_SAME__PRINCIPAL</span></div>
<div class="block">The operation id for the '<em>Is Same</em>' operation.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.USER_PRINCIPAL___IS_SAME__PRINCIPAL">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="USER_PRINCIPAL_OPERATION_COUNT">
<h3>USER_PRINCIPAL_OPERATION_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">USER_PRINCIPAL_OPERATION_COUNT</span></div>
<div class="block">The number of operations of the '<em>User Principal</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.USER_PRINCIPAL_OPERATION_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="GROUP_PRINCIPAL">
<h3>GROUP_PRINCIPAL</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">GROUP_PRINCIPAL</span></div>
<div class="block">The meta object id for the '<code><em>Group Principal</em></code>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><code>GroupPrincipalImpl</code></li>
<li><code>SecurityPackageImpl.getGroupPrincipal()</code></li>
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.GROUP_PRINCIPAL">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="GROUP_PRINCIPAL__NAME">
<h3>GROUP_PRINCIPAL__NAME</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">GROUP_PRINCIPAL__NAME</span></div>
<div class="block">The feature id for the '<em><b>Name</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.GROUP_PRINCIPAL__NAME">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="GROUP_PRINCIPAL__PACKAGE_PERMISSIONS">
<h3>GROUP_PRINCIPAL__PACKAGE_PERMISSIONS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">GROUP_PRINCIPAL__PACKAGE_PERMISSIONS</span></div>
<div class="block">The feature id for the '<em><b>Package Permissions</b></em>' reference list.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.GROUP_PRINCIPAL__PACKAGE_PERMISSIONS">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="GROUP_PRINCIPAL_FEATURE_COUNT">
<h3>GROUP_PRINCIPAL_FEATURE_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">GROUP_PRINCIPAL_FEATURE_COUNT</span></div>
<div class="block">The number of structural features of the '<em>Group Principal</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.GROUP_PRINCIPAL_FEATURE_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="GROUP_PRINCIPAL___IS_SAME__PRINCIPAL">
<h3>GROUP_PRINCIPAL___IS_SAME__PRINCIPAL</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">GROUP_PRINCIPAL___IS_SAME__PRINCIPAL</span></div>
<div class="block">The operation id for the '<em>Is Same</em>' operation.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.GROUP_PRINCIPAL___IS_SAME__PRINCIPAL">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="GROUP_PRINCIPAL_OPERATION_COUNT">
<h3>GROUP_PRINCIPAL_OPERATION_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">GROUP_PRINCIPAL_OPERATION_COUNT</span></div>
<div class="block">The number of operations of the '<em>Group Principal</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.GROUP_PRINCIPAL_OPERATION_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ROLE_PRINCIPAL">
<h3>ROLE_PRINCIPAL</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ROLE_PRINCIPAL</span></div>
<div class="block">The meta object id for the '<code><em>Role Principal</em></code>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><code>RolePrincipalImpl</code></li>
<li><code>SecurityPackageImpl.getRolePrincipal()</code></li>
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.ROLE_PRINCIPAL">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ROLE_PRINCIPAL__NAME">
<h3>ROLE_PRINCIPAL__NAME</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ROLE_PRINCIPAL__NAME</span></div>
<div class="block">The feature id for the '<em><b>Name</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.ROLE_PRINCIPAL__NAME">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ROLE_PRINCIPAL__PACKAGE_PERMISSIONS">
<h3>ROLE_PRINCIPAL__PACKAGE_PERMISSIONS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ROLE_PRINCIPAL__PACKAGE_PERMISSIONS</span></div>
<div class="block">The feature id for the '<em><b>Package Permissions</b></em>' reference list.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.ROLE_PRINCIPAL__PACKAGE_PERMISSIONS">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ROLE_PRINCIPAL_FEATURE_COUNT">
<h3>ROLE_PRINCIPAL_FEATURE_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ROLE_PRINCIPAL_FEATURE_COUNT</span></div>
<div class="block">The number of structural features of the '<em>Role Principal</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.ROLE_PRINCIPAL_FEATURE_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ROLE_PRINCIPAL___IS_SAME__PRINCIPAL">
<h3>ROLE_PRINCIPAL___IS_SAME__PRINCIPAL</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ROLE_PRINCIPAL___IS_SAME__PRINCIPAL</span></div>
<div class="block">The operation id for the '<em>Is Same</em>' operation.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.ROLE_PRINCIPAL___IS_SAME__PRINCIPAL">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ROLE_PRINCIPAL_OPERATION_COUNT">
<h3>ROLE_PRINCIPAL_OPERATION_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ROLE_PRINCIPAL_OPERATION_COUNT</span></div>
<div class="block">The number of operations of the '<em>Role Principal</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.ROLE_PRINCIPAL_OPERATION_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="EVERYONE_PRINCIPAL">
<h3>EVERYONE_PRINCIPAL</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">EVERYONE_PRINCIPAL</span></div>
<div class="block">The meta object id for the '<code><em>Everyone Principal</em></code>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><code>EveryonePrincipalImpl</code></li>
<li><code>SecurityPackageImpl.getEveryonePrincipal()</code></li>
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.EVERYONE_PRINCIPAL">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="EVERYONE_PRINCIPAL__NAME">
<h3>EVERYONE_PRINCIPAL__NAME</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">EVERYONE_PRINCIPAL__NAME</span></div>
<div class="block">The feature id for the '<em><b>Name</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.EVERYONE_PRINCIPAL__NAME">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="EVERYONE_PRINCIPAL__PACKAGE_PERMISSIONS">
<h3>EVERYONE_PRINCIPAL__PACKAGE_PERMISSIONS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">EVERYONE_PRINCIPAL__PACKAGE_PERMISSIONS</span></div>
<div class="block">The feature id for the '<em><b>Package Permissions</b></em>' reference list.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.EVERYONE_PRINCIPAL__PACKAGE_PERMISSIONS">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="EVERYONE_PRINCIPAL_FEATURE_COUNT">
<h3>EVERYONE_PRINCIPAL_FEATURE_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">EVERYONE_PRINCIPAL_FEATURE_COUNT</span></div>
<div class="block">The number of structural features of the '<em>Everyone Principal</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.EVERYONE_PRINCIPAL_FEATURE_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="EVERYONE_PRINCIPAL___IS_SAME__PRINCIPAL">
<h3>EVERYONE_PRINCIPAL___IS_SAME__PRINCIPAL</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">EVERYONE_PRINCIPAL___IS_SAME__PRINCIPAL</span></div>
<div class="block">The operation id for the '<em>Is Same</em>' operation.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.EVERYONE_PRINCIPAL___IS_SAME__PRINCIPAL">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="EVERYONE_PRINCIPAL_OPERATION_COUNT">
<h3>EVERYONE_PRINCIPAL_OPERATION_COUNT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">EVERYONE_PRINCIPAL_OPERATION_COUNT</span></div>
<div class="block">The number of operations of the '<em>Everyone Principal</em>' class.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.EVERYONE_PRINCIPAL_OPERATION_COUNT">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="ACTION">
<h3>ACTION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ACTION</span></div>
<div class="block">The meta object id for the '<a href="Action.html" title="enum class in com.nomagic.magicdraw.security"><code><em>Action</em></code></a>' enum.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="Action.html" title="enum class in com.nomagic.magicdraw.security"><code>Action</code></a></li>
<li><code>SecurityPackageImpl.getAction()</code></li>
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.ACTION">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="APPLICATION">
<h3>APPLICATION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">APPLICATION</span></div>
<div class="block">The meta object id for the '<a href="Application.html" title="enum class in com.nomagic.magicdraw.security"><code><em>Application</em></code></a>' enum.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="Application.html" title="enum class in com.nomagic.magicdraw.security"><code>Application</code></a></li>
<li><code>SecurityPackageImpl.getApplication()</code></li>
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.security.SecurityPackage.APPLICATION">Constant Field Values</a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
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
<section class="detail" id="getProjectSecurity()">
<h3>getProjectSecurity</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EClass</span> <span class="element-name">getProjectSecurity</span>()</div>
<div class="block">Returns the meta object for class '<a href="ProjectSecurity.html" title="interface in com.nomagic.magicdraw.security"><code><em>Project Security</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for class '<em>Project Security</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="ProjectSecurity.html" title="interface in com.nomagic.magicdraw.security"><code>ProjectSecurity</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectSecurity_PackagePermissions()">
<h3>getProjectSecurity_PackagePermissions</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EReference</span> <span class="element-name">getProjectSecurity_PackagePermissions</span>()</div>
<div class="block">Returns the meta object for the map '<a href="ProjectSecurity.html#getPackagePermissions()"><code><em>Package Permissions</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the map '<em>Package Permissions</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ProjectSecurity.html#getPackagePermissions()"><code>ProjectSecurity.getPackagePermissions()</code></a></li>
<li><a href="#getProjectSecurity()"><code>getProjectSecurity()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectSecurity_Principals()">
<h3>getProjectSecurity_Principals</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EReference</span> <span class="element-name">getProjectSecurity_Principals</span>()</div>
<div class="block">Returns the meta object for the containment reference list '<a href="ProjectSecurity.html#getPrincipals()"><code><em>Principals</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the containment reference list '<em>Principals</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ProjectSecurity.html#getPrincipals()"><code>ProjectSecurity.getPrincipals()</code></a></li>
<li><a href="#getProjectSecurity()"><code>getProjectSecurity()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectSecurity__IsEmpty()">
<h3>getProjectSecurity__IsEmpty</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EOperation</span> <span class="element-name">getProjectSecurity__IsEmpty</span>()</div>
<div class="block">Returns the meta object for the '<a href="ProjectSecurity.html#isEmpty()"><code><em>Is Empty</em></code></a>' operation.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the '<em>Is Empty</em>' operation.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="ProjectSecurity.html#isEmpty()"><code>ProjectSecurity.isEmpty()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackageAccessPermission()">
<h3>getPackageAccessPermission</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EClass</span> <span class="element-name">getPackageAccessPermission</span>()</div>
<div class="block">Returns the meta object for class '<a href="PackageAccessPermission.html" title="interface in com.nomagic.magicdraw.security"><code><em>Package Access Permission</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for class '<em>Package Access Permission</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="PackageAccessPermission.html" title="interface in com.nomagic.magicdraw.security"><code>PackageAccessPermission</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackageAccessPermission_Action()">
<h3>getPackageAccessPermission_Action</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getPackageAccessPermission_Action</span>()</div>
<div class="block">Returns the meta object for the attribute '<a href="PackageAccessPermission.html#getAction()"><code><em>Action</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="PackageAccessPermission.html#getAction()"><code>PackageAccessPermission.getAction()</code></a></li>
<li><a href="#getPackageAccessPermission()"><code>getPackageAccessPermission()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackageAccessPermission_Application()">
<h3>getPackageAccessPermission_Application</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getPackageAccessPermission_Application</span>()</div>
<div class="block">Returns the meta object for the attribute '<a href="PackageAccessPermission.html#getApplication()"><code><em>Application</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>Application</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="PackageAccessPermission.html#getApplication()"><code>PackageAccessPermission.getApplication()</code></a></li>
<li><a href="#getPackageAccessPermission()"><code>getPackageAccessPermission()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackageAccessPermission_Principal()">
<h3>getPackageAccessPermission_Principal</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EReference</span> <span class="element-name">getPackageAccessPermission_Principal</span>()</div>
<div class="block">Returns the meta object for the reference '<a href="PackageAccessPermission.html#getPrincipal()"><code><em>Principal</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the reference '<em>Principal</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="PackageAccessPermission.html#getPrincipal()"><code>PackageAccessPermission.getPrincipal()</code></a></li>
<li><a href="#getPackageAccessPermission()"><code>getPackageAccessPermission()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackageAccessPermission__IsSame__PackageAccessPermission()">
<h3>getPackageAccessPermission__IsSame__PackageAccessPermission</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EOperation</span> <span class="element-name">getPackageAccessPermission__IsSame__PackageAccessPermission</span>()</div>
<div class="block">Returns the meta object for the '<a href="PackageAccessPermission.html#isSame(com.nomagic.magicdraw.security.PackageAccessPermission)"><code><em>Is Same</em></code></a>' operation.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the '<em>Is Same</em>' operation.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="PackageAccessPermission.html#isSame(com.nomagic.magicdraw.security.PackageAccessPermission)"><code>PackageAccessPermission.isSame(com.nomagic.magicdraw.security.PackageAccessPermission)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStringToPackagePermissionsMap()">
<h3>getStringToPackagePermissionsMap</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EClass</span> <span class="element-name">getStringToPackagePermissionsMap</span>()</div>
<div class="block">Returns the meta object for class '<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.Entry.html" title="class or interface in java.util"><code><em>String To Package Permissions Map</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for class '<em>String To Package Permissions Map</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.Entry.html" title="class or interface in java.util"><code>Map.Entry</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>keyDataType="org.eclipse.emf.ecore.EString"
        valueType="com.nomagic.magicdraw.security.PackagePermissions" valueContainment="true" valueResolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStringToPackagePermissionsMap_Key()">
<h3>getStringToPackagePermissionsMap_Key</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getStringToPackagePermissionsMap_Key</span>()</div>
<div class="block">Returns the meta object for the attribute '<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.Entry.html" title="class or interface in java.util"><code><em>Key</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>Key</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.Entry.html" title="class or interface in java.util"><code>Map.Entry</code></a></li>
<li><a href="#getStringToPackagePermissionsMap()"><code>getStringToPackagePermissionsMap()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStringToPackagePermissionsMap_Value()">
<h3>getStringToPackagePermissionsMap_Value</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EReference</span> <span class="element-name">getStringToPackagePermissionsMap_Value</span>()</div>
<div class="block">Returns the meta object for the containment reference '<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.Entry.html" title="class or interface in java.util"><code><em>Value</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the containment reference '<em>Value</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.Entry.html" title="class or interface in java.util"><code>Map.Entry</code></a></li>
<li><a href="#getStringToPackagePermissionsMap()"><code>getStringToPackagePermissionsMap()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackagePermissions()">
<h3>getPackagePermissions</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EClass</span> <span class="element-name">getPackagePermissions</span>()</div>
<div class="block">Returns the meta object for class '<a href="PackagePermissions.html" title="interface in com.nomagic.magicdraw.security"><code><em>Package Permissions</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for class '<em>Package Permissions</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="PackagePermissions.html" title="interface in com.nomagic.magicdraw.security"><code>PackagePermissions</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackagePermissions_AccessPermissions()">
<h3>getPackagePermissions_AccessPermissions</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EReference</span> <span class="element-name">getPackagePermissions_AccessPermissions</span>()</div>
<div class="block">Returns the meta object for the containment reference list '<a href="PackagePermissions.html#getAccessPermissions()"><code><em>Access Permissions</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the containment reference list '<em>Access Permissions</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="PackagePermissions.html#getAccessPermissions()"><code>PackagePermissions.getAccessPermissions()</code></a></li>
<li><a href="#getPackagePermissions()"><code>getPackagePermissions()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackagePermissions_UseParentPermissions()">
<h3>getPackagePermissions_UseParentPermissions</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getPackagePermissions_UseParentPermissions</span>()</div>
<div class="block">Returns the meta object for the attribute '<a href="PackagePermissions.html#isUseParentPermissions()"><code><em>Use Parent Permissions</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>Use Parent Permissions</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="PackagePermissions.html#isUseParentPermissions()"><code>PackagePermissions.isUseParentPermissions()</code></a></li>
<li><a href="#getPackagePermissions()"><code>getPackagePermissions()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackagePermissions__IsSame__PackagePermissions()">
<h3>getPackagePermissions__IsSame__PackagePermissions</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EOperation</span> <span class="element-name">getPackagePermissions__IsSame__PackagePermissions</span>()</div>
<div class="block">Returns the meta object for the '<a href="PackagePermissions.html#isSame(com.nomagic.magicdraw.security.PackagePermissions)"><code><em>Is Same</em></code></a>' operation.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the '<em>Is Same</em>' operation.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="PackagePermissions.html#isSame(com.nomagic.magicdraw.security.PackagePermissions)"><code>PackagePermissions.isSame(com.nomagic.magicdraw.security.PackagePermissions)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrincipal()">
<h3>getPrincipal</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EClass</span> <span class="element-name">getPrincipal</span>()</div>
<div class="block">Returns the meta object for class '<a href="Principal.html" title="interface in com.nomagic.magicdraw.security"><code><em>Principal</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for class '<em>Principal</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="Principal.html" title="interface in com.nomagic.magicdraw.security"><code>Principal</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrincipal_Name()">
<h3>getPrincipal_Name</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EAttribute</span> <span class="element-name">getPrincipal_Name</span>()</div>
<div class="block">Returns the meta object for the attribute '<a href="Principal.html#getName()"><code><em>Name</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the attribute '<em>Name</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="Principal.html#getName()"><code>Principal.getName()</code></a></li>
<li><a href="#getPrincipal()"><code>getPrincipal()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrincipal_PackagePermissions()">
<h3>getPrincipal_PackagePermissions</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EReference</span> <span class="element-name">getPrincipal_PackagePermissions</span>()</div>
<div class="block">Returns the meta object for the reference list '<a href="Principal.html#getPackagePermissions()"><code><em>Package Permissions</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the reference list '<em>Package Permissions</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="Principal.html#getPackagePermissions()"><code>Principal.getPackagePermissions()</code></a></li>
<li><a href="#getPrincipal()"><code>getPrincipal()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrincipal__IsSame__Principal()">
<h3>getPrincipal__IsSame__Principal</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EOperation</span> <span class="element-name">getPrincipal__IsSame__Principal</span>()</div>
<div class="block">Returns the meta object for the '<a href="Principal.html#isSame(com.nomagic.magicdraw.security.Principal)"><code><em>Is Same</em></code></a>' operation.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for the '<em>Is Same</em>' operation.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="Principal.html#isSame(com.nomagic.magicdraw.security.Principal)"><code>Principal.isSame(com.nomagic.magicdraw.security.Principal)</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUserPrincipal()">
<h3>getUserPrincipal</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EClass</span> <span class="element-name">getUserPrincipal</span>()</div>
<div class="block">Returns the meta object for class '<a href="UserPrincipal.html" title="interface in com.nomagic.magicdraw.security"><code><em>User Principal</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for class '<em>User Principal</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="UserPrincipal.html" title="interface in com.nomagic.magicdraw.security"><code>UserPrincipal</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGroupPrincipal()">
<h3>getGroupPrincipal</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EClass</span> <span class="element-name">getGroupPrincipal</span>()</div>
<div class="block">Returns the meta object for class '<a href="GroupPrincipal.html" title="interface in com.nomagic.magicdraw.security"><code><em>Group Principal</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for class '<em>Group Principal</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="GroupPrincipal.html" title="interface in com.nomagic.magicdraw.security"><code>GroupPrincipal</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRolePrincipal()">
<h3>getRolePrincipal</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EClass</span> <span class="element-name">getRolePrincipal</span>()</div>
<div class="block">Returns the meta object for class '<a href="RolePrincipal.html" title="interface in com.nomagic.magicdraw.security"><code><em>Role Principal</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for class '<em>Role Principal</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="RolePrincipal.html" title="interface in com.nomagic.magicdraw.security"><code>RolePrincipal</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEveryonePrincipal()">
<h3>getEveryonePrincipal</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EClass</span> <span class="element-name">getEveryonePrincipal</span>()</div>
<div class="block">Returns the meta object for class '<a href="EveryonePrincipal.html" title="interface in com.nomagic.magicdraw.security"><code><em>Everyone Principal</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for class '<em>Everyone Principal</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="EveryonePrincipal.html" title="interface in com.nomagic.magicdraw.security"><code>EveryonePrincipal</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAction()">
<h3>getAction</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EEnum</span> <span class="element-name">getAction</span>()</div>
<div class="block">Returns the meta object for enum '<a href="Action.html" title="enum class in com.nomagic.magicdraw.security"><code><em>Action</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for enum '<em>Action</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="Action.html" title="enum class in com.nomagic.magicdraw.security"><code>Action</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getApplication()">
<h3>getApplication</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.ecore.EEnum</span> <span class="element-name">getApplication</span>()</div>
<div class="block">Returns the meta object for enum '<a href="Application.html" title="enum class in com.nomagic.magicdraw.security"><code><em>Application</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the meta object for enum '<em>Application</em>'.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="Application.html" title="enum class in com.nomagic.magicdraw.security"><code>Application</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSecurityFactory()">
<h3>getSecurityFactory</h3>
<div class="member-signature"><span class="return-type"><a href="SecurityFactory.html" title="interface in com.nomagic.magicdraw.security">SecurityFactory</a></span> <span class="element-name">getSecurityFactory</span>()</div>
<div class="block">Returns the factory that creates the instances of the model.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the factory that creates the instances of the model.</dd>
<dt>Generated:</dt>
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
