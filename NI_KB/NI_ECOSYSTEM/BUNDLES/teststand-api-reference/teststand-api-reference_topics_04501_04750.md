# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=4501 end=4750 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/methods_5.html language=enus -->
## TOPIC 04501: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/methods_5.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/methods_5.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

Queue

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/methods_6.html language=enus -->
## TOPIC 04502: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/methods_6.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/methods_6.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

Rendezvous

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/methods_7.html language=enus -->
## TOPIC 04503: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/methods_7.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/methods_7.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

Semaphore

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/methods_8.html language=enus -->
## TOPIC 04504: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/methods_8.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/methods_8.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

SyncManager

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/mutex-earlyunlockmutex.html language=enus -->
## TOPIC 04505: Mutex.EarlyUnlockMutex

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/mutex-earlyunlockmutex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/mutex-earlyunlockmutex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Mutex.EarlyUnlockMutex( threadId) Purpose This method is obsolete. Use the Mutex.EarlyUnlockMutexEx method instead. Remarks Performs an AutoReleaser.EarlyRelease on the most recent AutoReleaser object the Mutex.LockMutex method or the Mutex.LockMutexGroup method returns for the current thread

### Mutex.EarlyUnlockMutex

#### Syntax

[Mutex](mutex.html).EarlyUnlockMutex( threadId)

#### Purpose

Note

Mutex.EarlyUnlockMutexEx

#### Remarks

Performs an
 [AutoReleaser.EarlyRelease](autoreleaser-earlyrelease.html)
 on the most recent
 [AutoReleaser](autoreleaser.html)
 object the
 [Mutex.LockMutex](mutex-lockmutex.html)
 method or the
 [Mutex.LockMutexGroup](mutex-lockmutexgroup.html)
 method returns for the current thread.

Note

#### Parameters

threadId
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a globally unique thread ID (GUID) for the thread that performs the operation. When you call this method from a TestStand execution, specify the value of the
 
 [Thread.UniqueThreadId](../tsapiref/thread-uniquethreadid.html)
 property for this parameter. Because the TestStand Synchronization Manager permits sharing of mutexes among computers, you must use an ID more unique than just the current operating system thread ID of the current thread on the current computer. When you plan to use mutexes across computers, use a GUID or some other way of creating a thread ID that is unique across all computers. The
 Thread.UniqueThreadId
 property is a GUID.

#### See Also

[AutoReleaser](autoreleaser.html)

[AutoReleaser.EarlyRelease](autoreleaser-earlyrelease.html)

[Mutex.EarlyUnlockMutexEx](mutex-earlyunlockmutexex.html)

[Mutex.LockMutex](mutex-lockmutex.html)

[Mutex.LockMutexGroup](mutex-lockmutexgroup.html)

[Sequence Context](../tsapiref/sequencecontext.html)

[Thread.UniqueThreadId](../tsapiref/thread-uniquethreadid.html)

Parent topic:

Obsolete Mutex Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/mutex-earlyunlockmutexex.html language=enus -->
## TOPIC 04506: Mutex.EarlyUnlockMutexEx

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/mutex-earlyunlockmutexex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/mutex-earlyunlockmutexex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Mutex.EarlyUnlockMutexEx( sequenceContextObj, threadId) Purpose Performs an AutoReleaser.EarlyReleaseEx on the most recent AutoReleaser object the Mutex.LockMutex method or the Mutex.LockMutexGroup method returns for the current thread. This method does not necessarily release ownership of th

### Mutex.EarlyUnlockMutexEx

#### Syntax

[Mutex](mutex.html).EarlyUnlockMutexEx( sequenceContextObj, threadId)

#### Purpose

Performs an
 [AutoReleaser.EarlyReleaseEx](autoreleaser-earlyreleaseex.html)
 on the most recent
 [AutoReleaser](autoreleaser.html)
 object the
 [Mutex.LockMutex](mutex-lockmutex.html)
 method or the
 [Mutex.LockMutexGroup](mutex-lockmutexgroup.html)
 method returns for the current thread.

Note

#### Parameters

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 when you call this method from within a step of an execution. You must use the sequence context of the sequence in which you are calling this method. Pass a
 NULL
 reference when you do not call this method from an execution.

threadId
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a globally unique thread ID (GUID) for the thread that performs the operation. When you call this method from a TestStand execution, specify the value of the
 
 [Thread.UniqueThreadId](../tsapiref/thread-uniquethreadid.html)
 property for this parameter. Because the TestStand Synchronization Manager permits sharing of mutexes among computers, you must use an ID more unique than just the current operating system thread ID of the current thread on the current computer. When you plan to use mutexes across computers, use a GUID or some other way of creating a thread ID that is unique across all computers. The
 Thread.UniqueThreadId
 property is a GUID.

#### See Also

[AutoReleaser.EarlyReleaseEx](autoreleaser-earlyreleaseex.html)

[Mutex.LockMutex](mutex-lockmutex.html)

[Mutex.LockMutexGroup](mutex-lockmutexgroup.html)

[Thread.UniqueThreadId](../tsapiref/thread-uniquethreadid.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/mutex-finalizeforgrouplock.html language=enus -->
## TOPIC 04507: Mutex.FinalizeForGroupLock

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/mutex-finalizeforgrouplock.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/mutex-finalizeforgrouplock.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Mutex.FinalizeForGroupLock( homeSyncMgr) Purpose This method is obsolete. Remarks Do not call this method. This method is for internal use only to implement the Mutex.LockMutexGroup method. Parameters homeSyncMgr As SyncManager [In] Specifies the local version of the TestStand Synchronization

### Mutex.FinalizeForGroupLock

#### Syntax

[Mutex](mutex.html).FinalizeForGroupLock( homeSyncMgr)

#### Purpose

Note

#### Remarks

Do not call this method. This method is for internal use only to implement the
 [Mutex.LockMutexGroup](mutex-lockmutexgroup.html)
 method.

#### Parameters

homeSyncMgr
 As
 [SyncManager](syncmanager.html)

[In] Specifies the local version of the TestStand Synchronization Manager. When you use the
 
 [TestStand Engine](../tsapiref/engine.html)
 , National Instruments recommends that you call the method on a local version of the TestStand Engine to obtain the value to pass for this parameter. This parameter is used for deadlock detection purposes.

Notice

NULL

#### See Also

[Engine.GetSyncManager](../tsapiref/engine-getsyncmanager.html)

[Mutex.LockMutexGroup](mutex-lockmutexgroup.html)

[TestStand Engine](../tsapiref/engine.html)

Parent topic:

Obsolete Mutex Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/mutex-getinfo.html language=enus -->
## TOPIC 04508: Mutex.GetInfo

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/mutex-getinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/mutex-getinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Mutex.GetInfo( numThreadsWaitingToLock) Purpose Obtains information about the current state of the mutex. Parameters numThreadsWaitingToLock As Long [Out] Returns the number of threads waiting to lock the mutex.

### Mutex.GetInfo

#### Syntax

[Mutex](mutex.html).GetInfo( numThreadsWaitingToLock)

#### Purpose

Obtains information about the current state of the mutex.

#### Parameters

numThreadsWaitingToLock
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[Out] Returns the number of threads waiting to lock the mutex.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/mutex-getinfoex.html language=enus -->
## TOPIC 04509: Mutex.GetInfoEx

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/mutex-getinfoex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/mutex-getinfoex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Mutex.GetInfoEx( numThreadsWaitingToLock, threadId, threadDisplayName) Purpose Obtains information about the current state of the mutex. Parameters numThreadsWaitingToLock As Long [Out] Returns the number of threads waiting to lock the mutex. threadId As String [Out] Returns the thread ID of

### Mutex.GetInfoEx

#### Syntax

[Mutex](mutex.html).GetInfoEx( numThreadsWaitingToLock, threadId, threadDisplayName)

#### Purpose

Obtains information about the current state of the mutex.

#### Parameters

numThreadsWaitingToLock
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[Out] Returns the number of threads waiting to lock the mutex.

threadId
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[Out] Returns the thread ID of the current owner of the mutex or an empty string when no owner exists.

threadDisplayName
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[Out] Returns the display name of the current owner of the mutex or an empty string when no owner exists.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/mutex-getsavedownerinfo.html language=enus -->
## TOPIC 04510: Mutex.GetSavedOwnerInfo

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/mutex-getsavedownerinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/mutex-getsavedownerinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Mutex.GetSavedOwnerInfo( threadId, threadDisplayName, homeSyncMgr) Purpose This method is obsolete. Remarks Do not call this method. This method is for internal use only to implement deadlock reporting. This method is unsafe to call externally and can crash the application. This method access

### Mutex.GetSavedOwnerInfo

#### Syntax

[Mutex](mutex.html).GetSavedOwnerInfo( threadId, threadDisplayName, homeSyncMgr)

#### Purpose

Note

#### Remarks

Do not call this method. This method is for internal use only to implement deadlock reporting.

Notice

#### Parameters

threadId
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[Out] Returns a globally unique thread ID (GUID) for the thread that performs the operation.

threadDisplayName
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[Out] Returns a display name to identify the current thread.

homeSyncMgr
 As
 [SyncManager](syncmanager.html)

[Out] Returns the local version of the TestStand Synchronization Manager. When you use the
 
 [TestStand Engine](../tsapiref/engine.html)
 , National Instruments recommends that you call the
 
 [Engine.GetSyncManager](../tsapiref/engine-getsyncmanager.html)
 method on a local version of the TestStand Engine to obtain the value to pass for this parameter. This parameter is used for deadlock detection purposes.

Notice

NULL

#### See Also

[Engine.GetSyncManager](../tsapiref/engine-getsyncmanager.html)

[TestStand Engine](../tsapiref/engine.html)

[Thread.UniqueThreadId](../tsapiref/thread-uniquethreadid.html)

Parent topic:

Obsolete Mutex Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/mutex-lockmutex.html language=enus -->
## TOPIC 04511: Mutex.LockMutex

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/mutex-lockmutex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/mutex-lockmutex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Mutex.LockMutex( threadId, threadDisplayName, homeSyncMgr, timeoutInSeconds, sequenceContextObj, processMsgs, isPartOfGroupLock, waitRes, deadlockElabMsg) Return Value AutoReleaser An object that automatically unlocks the mutex when you release the last reference to the AutoReleaser object. P

### Mutex.LockMutex

#### Syntax

[Mutex](mutex.html).LockMutex( threadId, threadDisplayName, homeSyncMgr, timeoutInSeconds, sequenceContextObj, processMsgs, isPartOfGroupLock, waitRes, deadlockElabMsg)

#### Return Value

[AutoReleaser](autoreleaser.html)

An object that automatically unlocks the mutex when you release the last reference to the
 AutoReleaser
 object.

#### Purpose

Performs a Lock operation on the mutex.

#### Parameters

threadId
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a globally unique thread ID (GUID) for the thread that performs the operation. When you call this method from a TestStand execution, specify the value of the
 
 [Thread.UniqueThreadId](../tsapiref/thread-uniquethreadid.html)
 property for this parameter. Because the TestStand Synchronization Manager permits sharing of mutexes among computers, you must use an ID more unique than just the current operating system thread ID of the current thread on the current computer. When you plan to use mutexes across computers, use a GUID or some other way of creating a thread ID that is unique across all computers. The
 Thread.UniqueThreadId
 property is a GUID.

threadDisplayName
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a display name to identify the current thread. This name reports a deadlock condition, when one occurs, involving this thread.

homeSyncMgr
 As
 [SyncManager](syncmanager.html)

[In] Specifies the local version of the TestStand Synchronization Manager. When you use the
 
 [TestStand Engine](../tsapiref/engine.html)
 , National Instruments recommends that you call the
 
 [Engine.GetSyncManager](../tsapiref/engine-getsyncmanager.html)
 method on a local version of the TestStand Engine to obtain the value to pass for this parameter. Use this parameter for deadlock detection purposes.

Notice

NULL

timeoutInSeconds
 As
 [Double](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a timeout in seconds. Pass a negative number to specify that you do not want a timeout.

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 when you call this method from within a step of an execution. You must use the sequence context of the sequence in which you are calling this method. Pass a
 NULL
 reference when you do not call this method from an execution. This method uses the sequence context to improve the behavior of the execution when it is blocked while waiting on this method.

processMsgs
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to process Microsoft Windows messages while waiting. When you call this method from an execution, pass
 True
 for this parameter. Otherwise, pass
 False
 .

isPartOfGroupLock
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] This parameter is used internally to implement the
 [Mutex.LockMutexGroup](mutex-lockmutexgroup.html)
 method. Always pass
 False
 for this parameter.

waitRes
 As
 [WaitResult](waitresult.html)

[Out] Returns the
 [status](waitresult.html)
 of the operation.

deadlockElabMsg
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[Out] When the
 waitRes
 parameter returns the
 WaitResult_DeadlockDetected
 enumeration, this parameter returns a description of why the deadlock occurred.

#### See Also

[AutoReleaser](autoreleaser.html)

[Engine.GetSyncManager](../tsapiref/engine-getsyncmanager.html)

[Mutex.LockMutexGroup](mutex-lockmutexgroup.html)

[Sequence Context](../tsapiref/sequencecontext.html)

[TestStand Engine](../tsapiref/engine.html)

[Thread.UniqueThreadId](../tsapiref/thread-uniquethreadid.html)

[WaitResult](waitresult.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/mutex-lockmutexgroup.html language=enus -->
## TOPIC 04512: Mutex.LockMutexGroup

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/mutex-lockmutexgroup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/mutex-lockmutexgroup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Mutex.LockMutexGroup( mutexArray, threadId, threadDisplayName, homeSyncMgr, timeoutInSeconds, sequenceContextObj, processMsgs, waitRes, deadlockElabMsg) Return Value Object Array An array of objects that automatically unlocks the mutexes when you release the last reference to the AutoReleaser

### Mutex.LockMutexGroup

#### Syntax

[Mutex](mutex.html).LockMutexGroup( mutexArray, threadId, threadDisplayName, homeSyncMgr, timeoutInSeconds, sequenceContextObj, processMsgs, waitRes, deadlockElabMsg)

#### Return Value

[Object Array](data-types-for-teststand-synchronization-serv.html)

An array of objects that automatically unlocks the mutexes when you release the last reference to the
 [AutoReleaser](autoreleaser.html)
 objects.

#### Purpose

Performs a Lock operation on a group of mutexes. This operation attempts to lock all the locks you specify. When the operation cannot lock all the locks, it unlocks the successful locks and tries again after a random delay. This behavior continues until the operation succeeds in locking all the locks or the timeout you specify occurs. When you use this method to lock all the locks a thread requires, you avoid the possibility of deadlock. However, you lose the guarantee of first in, first out (FIFO) ordering of which thread can lock a particular lock first.

Note

mutexArray

#### Parameters

mutexArray
 As
 [Object Array](data-types-for-teststand-synchronization-serv.html)

[In] Specifies an array of Mutex objects to lock.

threadId
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a globally unique thread ID (GUID) for the thread that performs the operation. When you call this method from a TestStand execution, specify the value of the
 
 [Thread.UniqueThreadId](../tsapiref/thread-uniquethreadid.html)
 property for this parameter. Because the TestStand Synchronization Manager permits sharing of mutexes among computers, you must use an ID more unique than just the current operating system thread ID of the current thread on the current computer. When you plan to use mutexes across computers, use a GUID or some other way of creating a thread ID that is unique across all computers. The
 Thread.UniqueThreadId
 property is a GUID.

threadDisplayName
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a display name to identify the current thread. Use this name to report a deadlock condition, when one occurs, involving this thread.

homeSyncMgr
 As
 [SyncManager](syncmanager.html)

[In] Specifies the local version of the TestStand Synchronization Manager. When you use the
 
 [TestStand Engine](../tsapiref/engine.html)
 , National Instruments recommends that you call the method on a local version of the TestStand Engine to obtain the value to pass for this parameter. Use this parameter for deadlock detection purposes.

Notice

NULL

timeoutInSeconds
 As
 [Double](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a timeout in seconds. Pass a negative number to specify that you do not want a timeout.

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 when you call this method from within a step of an execution. You must use the sequence context of the sequence in which you are calling this method. Pass a
 NULL
 reference when you do not call this method from an execution. This method uses the sequence context to improve the behavior of the execution when it is blocked while waiting on this method.

processMsgs
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to process Microsoft Windows messages while waiting. When you call this method from an execution, pass
 True
 for this parameter. Otherwise, pass
 False
 .

waitRes
 As
 [WaitResult](waitresult.html)

[Out] Returns the
 [status](waitresult.html)
 of the operation.

deadlockElabMsg
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[Out] When the
 waitRes
 parameter returns
 WaitResult_DeadlockDetected
 , this parameter returns a description of why the deadlock occurred.

#### See Also

[AutoReleaser](autoreleaser.html)

[Engine.GetSyncManager](../tsapiref/engine-getsyncmanager.html)

[Sequence Context](../tsapiref/sequencecontext.html)

[TestStand Engine](../tsapiref/engine.html)

[Thread.UniqueThreadId](../tsapiref/thread-uniquethreadid.html)

[WaitResult](waitresult.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/mutex-name.html language=enus -->
## TOPIC 04513: Mutex.Name

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/mutex-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/mutex-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Mutex.Name Data Type String Purpose Returns the name of the mutex.

### Mutex.Name

#### Syntax

[Mutex](mutex.html).Name

#### Data Type

[String](data-types-for-teststand-synchronization-serv.html)

#### Purpose

Returns the name of the mutex.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/mutex.html language=enus -->
## TOPIC 04514: Mutex

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/mutex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/mutex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This class implements the Lock synchronization primitive. Use these properties and methods to implement the Lock step type. Property Name (Read Only) Methods EarlyUnlockMutexEx GetInfo GetInfoEx LockMutex LockMutexGroup See Also Lock step type Synchronization Step Types

### Mutex

This class implements the Lock synchronization primitive. Use these properties and methods to implement the
 [Lock](../tsref/lock-step.html)
 step type.

#### Property

| Name (Read Only) |
| --- |

#### Methods

| EarlyUnlockMutexEx |
| --- |
| GetInfo |
| GetInfoEx |
| LockMutex |
| LockMutexGroup |

#### See Also

[Lock step type](../tsref/lock-step.html)

[Synchronization Step Types](../tsref/synchronization-step-types.html)

Parent topic:

TestStand Synchronization Server

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/ni-teststand-synchronization-server-api-refer.html language=enus -->
## TOPIC 04515: NI TestStand Synchronization Server API Reference Help

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/ni-teststand-synchronization-server-api-refer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/ni-teststand-synchronization-server-api-refer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This help file contains detailed information about the properties, methods, events, constants, and enumerations of the TestStand Synchronization Server API. If you open help files directly from the <TestStand> \Doc\Help directory, National Instruments recommends that you open TSHelp.chm first becaus

### NI TestStand Synchronization Server API Reference Help

Note

<TestStand>

TSHelp.chm

To navigate this help file, use the
 Contents
 ,
 Index
 , and
 Search
 tabs to the left of this window.

Refer to the
 [National Instruments website](http://digital.ni.com/express.nsf/bycode/feedback)
 to comment on National Instruments documentation.

Copyright © National Instruments Corporation. All rights reserved.

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/notification-beginwaitformultiwait.html language=enus -->
## TOPIC 04516: Notification.BeginWaitForMultiWait

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/notification-beginwaitformultiwait.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/notification-beginwaitformultiwait.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Notification.BeginWaitForMultiWait( eventName, operationId, waitId) Purpose This method is obsolete. Remarks Do not call this method. This method is for internal use only to implement the Notification.WaitMultiple method. Parameters eventName As String [Out] Returns an event name the object u

### Notification.BeginWaitForMultiWait

#### Syntax

[Notification](notification.html).BeginWaitForMultiWait( eventName, operationId, waitId)

#### Purpose

Note

#### Remarks

Do not call this method. This method is for internal use only to implement the
 [Notification.WaitMultiple](notification-waitmultiple.html)
 method.

#### Parameters

eventName
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[Out] Returns an event name the object uses internally.

operationId
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[Out] Returns an internal value the server uses to wait on multiple Notification objects.

waitId
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[Out] Returns an internal value the server uses to wait on multiple Notification objects.

#### See Also

[Notification.WaitMultiple](notification-waitmultiple.html)

Parent topic:

Obsolete Notification Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/notification-clear.html language=enus -->
## TOPIC 04517: Notification.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/notification-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/notification-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Notification.Clear Purpose This method is obsolete. Use the Notification.ClearEx method instead. Remarks Clears the state of a notification so subsequent Wait operations block until the next Set operation.

### Notification.Clear

#### Syntax

[Notification](notification.html).Clear

#### Purpose

Note

Notification.ClearEx

#### Remarks

Clears the state of a notification so subsequent Wait operations block until the next Set operation.

Parent topic:

Obsolete Notification Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/notification-clearex.html language=enus -->
## TOPIC 04518: Notification.ClearEx

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/notification-clearex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/notification-clearex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Notification.ClearEx( sequenceContextObj) Purpose Clears the state of a notification so subsequent Wait operations block until the next Set operation. Parameters sequenceContextObj As Object [In] Specifies a sequence context when you call this method from within a step of an execution. You mu

### Notification.ClearEx

#### Syntax

[Notification](notification.html).ClearEx( sequenceContextObj)

#### Purpose

Clears the state of a notification so subsequent Wait operations block until the next Set operation.

#### Parameters

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 when you call this method from within a step of an execution. You must use the sequence context of the sequence in which you are calling this method. Pass a
 NULL
 reference when you do not call this method from an execution.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/notification-dowaitformultiwait.html language=enus -->
## TOPIC 04519: Notification.DoWaitForMultiWait

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/notification-dowaitformultiwait.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/notification-dowaitformultiwait.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Notification.DoWaitForMultiWait( sequenceContextObj, destinationPropObj, operationId, waitId, keepWaitingParam) Purpose This method is obsolete. Remarks Do not call this method. This method is for internal use only to implement the Notification.WaitMultiple method. Parameters sequenceContextO

### Notification.DoWaitForMultiWait

#### Syntax

[Notification](notification.html).DoWaitForMultiWait( sequenceContextObj, destinationPropObj, operationId, waitId, keepWaitingParam)

#### Purpose

Note

#### Remarks

Do not call this method. This method is for internal use only to implement the
 [Notification.WaitMultiple](notification-waitmultiple.html)
 method.

#### Parameters

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 when you call this method from within a step of an execution. You must use the sequence context of the sequence in which you are calling this method. Pass a
 NULL
 reference when you do not call this method from an execution. This method uses the sequence context to improve the behavior of the execution when it is blocked while waiting on this method.

destinationPropObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the
 
 [PropertyObject](../tsapiref/propertyobject.html)
 in which to store the notification data. You can pass a
 NULL
 reference when you do not want to store the data. The type of the destination
 PropertyObject
 must be compatible with the data the notification sends. The
 [Wait Behaviors for Data Set or Pulsed by Value](../tsref/wait-operation-notification-step-configuratio.html)
 and
 [Wait Behaviors for Data Set or Pulsed by Reference](../tsref/wait-operation-notification-step-configuratio.html)
 tables illustrate the wait outcome depending on the type of the data and the data type of the storage location. In these tables, Simple Type refers to a number, string, Boolean, or array of any type, and Structured Type refers to an instance of a user-defined type where the root property is a container.

operationId
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[In] Specifies an internal value the server uses to wait on multiple Notification objects.

waitId
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[In] Specifies an internal value the server uses to wait on multiple Notification objects.

keepWaitingParam
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[Out] Returns
 True
 when the caller should call this method again to retry the operation.

#### See Also

[PropertyObject](../tsapiref/propertyobject.html)

[Sequence Context](../tsapiref/sequencecontext.html)

[Wait Behaviors for Data Set or Pulsed by Reference](../tsref/wait-operation-notification-step-configuratio.html)

[Wait Behaviors for Data Set or Pulsed by Value](../tsref/wait-operation-notification-step-configuratio.html)

[WaitMultiple](notification-waitmultiple.html)

Parent topic:

Obsolete Notification Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/notification-endwaitformultiwait.html language=enus -->
## TOPIC 04520: Notification.EndWaitForMultiWait

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/notification-endwaitformultiwait.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/notification-endwaitformultiwait.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Notification.EndWaitForMultiWait( operationId, waitId) Purpose This method is obsolete. Remarks Do not call this method. This method is for internal use only and is used to implement the Notification.WaitMultiple method. Parameters operationId As Long [In] Specifies an internal value the serv

### Notification.EndWaitForMultiWait

#### Syntax

[Notification](notification.html).EndWaitForMultiWait( operationId, waitId)

#### Purpose

Note

#### Remarks

Do not call this method. This method is for internal use only and is used to implement the
 [Notification.WaitMultiple](notification-waitmultiple.html)
 method.

#### Parameters

operationId
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[In] Specifies an internal value the server uses to wait on multiple Notification objects.

waitId
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[In] Specifies an internal value the server uses to wait on multiple Notification objects.

#### See Also

[Notification.WaitMultiple](notification-waitmultiple.html)

Parent topic:

Obsolete Notification Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/notification-getinfo.html language=enus -->
## TOPIC 04521: Notification.GetInfo

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/notification-getinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/notification-getinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Notification.GetInfo( sequenceContextObj, destinationPropObj, numThreadsWaiting, isSet, isAutoClear) Purpose Obtains information about the notification. Parameters sequenceContextObj As Object [In] Specifies a sequence context . You can pass NULL for this parameter, but when you want to use t

### Notification.GetInfo

#### Syntax

[Notification](notification.html).GetInfo( sequenceContextObj, destinationPropObj, numThreadsWaiting, isSet, isAutoClear)

#### Purpose

Obtains information about the notification.

#### Parameters

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 . You can pass
 NULL
 for this parameter, but when you want to use the
 destinationPropObj
 parameter to retrieve data from a notification a different process put there, you must pass a valid sequence context.

destinationPropObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the
 
 [PropertyObject](../tsapiref/propertyobject.html)
 in which to store the notification data. You can pass a
 NULL
 reference when you do not want to store the data. The type of the destination
 PropertyObject
 must be compatible with the data the notification sends. The
 [Wait Behaviors for Data Set or Pulsed by Value](../tsref/wait-operation-notification-step-configuratio.html)
 and
 [Wait Behaviors for Data Set or Pulsed by Reference](../tsref/wait-operation-notification-step-configuratio.html)
 tables illustrate the wait outcome depending on the type of the data and the data type of the storage location. In these tables, Simple Type refers to a number, string, Boolean, or array of any type, and Structured Type refers to an instance of a user-defined type where the root property is a container.

numThreadsWaiting
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[Out] Returns the number of threads waiting on the notification. You can pass
 NULL
 for this parameter.

isSet
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[Out] Returns
 True
 when the notification is in a set state. You can pass
 NULL
 for this parameter.

isAutoClear
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[Out] Returns
 True
 when the notification is configured to automatically clear itself after one thread waits on the notification. You can pass
 NULL
 for this parameter.

#### See Also

[Notification.Wait](notification-wait.html)

[PropertyObject](../tsapiref/propertyobject.html)

[Sequence Context](../tsapiref/sequencecontext.html)

[Wait Behaviors for Data Set or Pulsed by Reference](../tsref/wait-operation-notification-step-configuratio.html)

[Wait Behaviors for Data Set or Pulsed by Value](../tsref/wait-operation-notification-step-configuratio.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/notification-name.html language=enus -->
## TOPIC 04522: Notification.Name

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/notification-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/notification-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Notification.Name Data Type String Purpose Returns the name of the notification.

### Notification.Name

#### Syntax

[Notification](notification.html).Name

#### Data Type

[String](data-types-for-teststand-synchronization-serv.html)

#### Purpose

Returns the name of the notification.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/notification-pulse.html language=enus -->
## TOPIC 04523: Notification.Pulse

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/notification-pulse.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/notification-pulse.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Notification.Pulse( dataPropObj, byRef, applyToAllWaiters) Purpose This method is obsolete. Use the Notification.PulseEx method instead. Remarks Notifies one or all currently waiting threads. This method differs from the Notification.Set method because this method notifies only those threads

### Notification.Pulse

#### Syntax

[Notification](notification.html).Pulse( dataPropObj, byRef, applyToAllWaiters)

#### Purpose

Note

Notification.PulseEx

#### Remarks

Notifies one or all currently waiting threads. This method differs from the
 [Notification.Set](notification-set.html)
 method because this method notifies only those threads already waiting when the Pulse operation occurs. Threads that wait on the notification after a Pulse operation occurs block until you send the Set or Pulse notification again. A Pulse operation places the notification in a Cleared state, even when the notification was in a Set state before the Pulse operation.

#### Parameters

dataPropObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies an optional
 
 [PropertyObject](../tsapiref/propertyobject.html)
 data element to store with the Set state of the notification. Threads that wait on the notification can then optionally retrieve this data. You can use data of any type, including a number, string, Boolean, object reference, structured type (container), or arrays of these types. When you later wait on the notification, you must store the element in a
 PropertyObject
 with the appropriate type. You can pass
 NULL
 for this parameter.

byRef
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] When you pass
 False
 , the notification stores a copy of the data you specify in the
 dataPropObj
 parameter. When you pass
 True
 , the notification stores an object reference to the data value.

applyToAllWaiters
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to notify all currently waiting threads. Pass
 False
 to notify just the first waiting thread.

#### See Also

[Notification.Clear](notification-clear.html)

[Notification.PulseEx](notification-pulseex.html)

[Notification.Set](notification-set.html)

[Notification.Wait](notification-wait.html)

[PropertyObject](../tsapiref/propertyobject.html)

Parent topic:

Obsolete Notification Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/notification-pulseex.html language=enus -->
## TOPIC 04524: Notification.PulseEx

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/notification-pulseex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/notification-pulseex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Notification.PulseEx( sequenceContextObj, dataPropObj, byRef, applyToAllWaiters) Purpose Notifies one or all currently waiting threads. This method differs from the Notification.SetEx method because this method notifies only those threads already waiting when the Pulse operation occurs. Threa

### Notification.PulseEx

#### Syntax

[Notification](notification.html).PulseEx( sequenceContextObj, dataPropObj, byRef, applyToAllWaiters)

#### Purpose

Notifies one or all currently waiting threads. This method differs from the
 [Notification.SetEx](notification-setex.html)
 method because this method notifies only those threads already waiting when the Pulse operation occurs. Threads that wait on the notification after a Pulse operation occurs block until you send the Set or Pulse notification again. A Pulse operation places the notification in a Cleared state, even when the notification was in a Set state before the Pulse operation.

#### Parameters

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 when you call this method from within a step of an execution. You must use the sequence context of the sequence in which you are calling this method. Pass a
 NULL
 reference when you do not call this method from an execution.

dataPropObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies an optional
 
 [PropertyObject](../tsapiref/propertyobject.html)
 data element to store with the Set state of the notification. Threads that wait on the notification can then optionally retrieve this data. You can use data of any type, including a number, string, Boolean, object reference, structured type (container), or arrays of these types. Subsequent wait operations must store the element in a
 PropertyObject
 with the appropriate type. You can pass
 NULL
 for this parameter.

byRef
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] When you pass
 False
 , the notification stores a copy of the data you specify in the
 dataPropObj
 parameter. When you pass
 True
 , the notification stores an object reference to the data value.

applyToAllWaiters
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to notify all currently waiting threads. Pass
 False
 to notify just the first waiting thread.

#### See Also

[Notification.ClearEx](notification-clearex.html)

[Notification.SetEx](notification-setex.html)

[Notification.Wait](notification-wait.html)

[PropertyObject](../tsapiref/propertyobject.html)

[Sequence Context](../tsapiref/sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/notification-set.html language=enus -->
## TOPIC 04525: Notification.Set

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/notification-set.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/notification-set.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Notification.Set( dataPropObj, byRef, autoClear) Purpose This method is obsolete. Use the Notification.SetEx method instead. Remarks Notifies one or more threads that an event has occurred or a condition has been met. When the notification is in a Set state, Wait operations on the notificatio

### Notification.Set

#### Syntax

[Notification](notification.html).Set( dataPropObj, byRef, autoClear)

#### Purpose

Note

Notification.SetEx

#### Remarks

Notifies one or more threads that an event has occurred or a condition has been met. When the notification is in a Set state, Wait operations on the notification succeed immediately.

#### Parameters

dataPropObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies an optional
 
 [PropertyObject](../tsapiref/propertyobject.html)
 data element to store with the Set state of the notification. Threads that wait on the notification can then optionally retrieve this data. You can use data of any type, including a number, string, Boolean, object reference, structured type (container), or arrays of these types. When you later wait on the notification, you must store the element in a
 PropertyObject
 with the appropriate type. You can pass
 NULL
 for this parameter.

byRef
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] When you pass
 False
 , the notification stores a copy of the data you specify in the
 dataPropObj
 parameter. When you pass
 True
 , the notification stores an object reference to the data value.

autoClear
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Specifies to clear the state of the notification after one thread receives the notification. Once you clear the state of a notification, subsequent Wait operations block until you perform another Set operation.

#### See Also

[Notification.Clear](notification-clear.html)

[Notification.Pulse](notification-pulse.html)

[Notification.SetEx](notification-setex.html)

[Notification.Wait](notification-wait.html)

[PropertyObject](../tsapiref/propertyobject.html)

Parent topic:

Obsolete Notification Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/notification-setex.html language=enus -->
## TOPIC 04526: Notification.SetEx

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/notification-setex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/notification-setex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Notification.SetEx( sequenceContextObj, dataPropObj, byRef, autoClear) Purpose Notifies one or more threads that an event has occurred or a condition has been met. When the notification is in a Set state, Wait operations on the notification succeed immediately. Parameters sequenceContextObj A

### Notification.SetEx

#### Syntax

[Notification](notification.html).SetEx( sequenceContextObj, dataPropObj, byRef, autoClear)

#### Purpose

Notifies one or more threads that an event has occurred or a condition has been met. When the notification is in a Set state, Wait operations on the notification succeed immediately.

#### Parameters

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 when you call this method from within a step of an execution. You must use the sequence context of the sequence in which you are calling this method. Pass a
 NULL
 reference when you do not call this method from an execution.

dataPropObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies an optional
 
 [PropertyObject](../tsapiref/propertyobject.html)
 data element to store with the Set state of the notification. Threads that wait on the notification can then optionally retrieve this data. You can use data of any type, including a number, string, Boolean, object reference, structured type (container), or arrays of these types. Subsequent wait operations must store the element in a
 PropertyObject
 with the appropriate type. You can pass
 NULL
 for this parameter.

byRef
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] When you pass
 False
 , the notification stores a copy of the data you specify in the
 dataPropObj
 parameter. When you pass
 True
 , the notification stores an object reference to the data value.

autoClear
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Specifies to clear the state of the notification after one thread receives the notification. Once you clear the state of a notification, subsequent Wait operations block until you perform another Set operation.

#### See Also

[Notification.ClearEx](notification-clearex.html)

[Notification.PulseEx](notification-pulseex.html)

[Notification.Wait](notification-wait.html)

[PropertyObject](../tsapiref/propertyobject.html)

[Sequence Context](../tsapiref/sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/notification-wait.html language=enus -->
## TOPIC 04527: Notification.Wait

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/notification-wait.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/notification-wait.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Notification.Wait( destinationPropObj, timeoutInSeconds, sequenceContextObj, processMsgs, waitRes) Purpose Waits until you Set or Pulse the notification. When the notification is already in a Set state, the Wait operation completes immediately. Parameters destinationPropObj As Object [In] Spe

### Notification.Wait

#### Syntax

[Notification](notification.html).Wait( destinationPropObj, timeoutInSeconds, sequenceContextObj, processMsgs, waitRes)

#### Purpose

Waits until you Set or Pulse the notification. When the notification is already in a Set state, the Wait operation completes immediately.

#### Parameters

destinationPropObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the
 
 [PropertyObject](../tsapiref/propertyobject.html)
 in which to store the notification data. You can pass a
 NULL
 reference when you do not want to store the data. The type of the destination
 PropertyObject
 must be compatible with the data the notification sends. The
 [Wait Behaviors for Data Set or Pulsed by Value](../tsref/wait-operation-notification-step-configuratio.html)
 and
 [Wait Behaviors for Data Set or Pulsed by Reference](../tsref/wait-operation-notification-step-configuratio.html)
 tables illustrate the wait outcome depending on the type of the data and the data type of the storage location. In these tables, Simple Type refers to a number, string, Boolean, or array of any type, and Structured Type refers to an instance of a user-defined type where the root property is a container.

timeoutInSeconds
 As
 [Double](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a timeout in seconds. Pass a negative number to specify that you do not want a timeout.

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 when you call this method from within a step of an execution. You must use the sequence context of the sequence in which you are calling this method. Pass a
 NULL
 reference when you do not call this method from an execution. This method uses the sequence context to improve the behavior of the execution when it is blocked while waiting on this method.

processMsgs
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to process Microsoft Windows messages while waiting. When you call this method from an execution, pass
 True
 for this parameter. Otherwise, pass
 False
 .

waitRes
 As
 [WaitResult](waitresult.html)

[Out] Returns the
 [status](waitresult.html)
 of the operation.

#### See Also

[Notification.PulseEx](notification-pulseex.html)

[Notification.SetEx](notification-setex.html)

[PropertyObject](../tsapiref/propertyobject.html)

[Sequence Context](../tsapiref/sequencecontext.html)

[Wait Behaviors for Data Set or Pulsed by Reference](../tsref/wait-operation-notification-step-configuratio.html)

[Wait Behaviors for Data Set or Pulsed by Value](../tsref/wait-operation-notification-step-configuratio.html)

[WaitResult](waitresult.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/notification-waitmultiple.html language=enus -->
## TOPIC 04528: Notification.WaitMultiple

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/notification-waitmultiple.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/notification-waitmultiple.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Notification.WaitMultiple( notificationArray, destinationPropObj, timeoutInSeconds, sequenceContextObj, processMsgs, waitRes, whichNotification, whichNotificationOffset) Purpose Waits on multiple notifications. This method waits until you Set or Pulse any of the notifications in the array. Wh

### Notification.WaitMultiple

#### Syntax

[Notification](notification.html).WaitMultiple( notificationArray, destinationPropObj, timeoutInSeconds, sequenceContextObj, processMsgs, waitRes, whichNotification, whichNotificationOffset)

#### Purpose

Waits on multiple notifications. This method waits until you Set or Pulse any of the notifications in the array. When you Set or Pulse more than one of the notifications, this method responds to the notification that appears first in the array. You can determine which notification the method responds to by checking the value of the
 whichNotification
 or
 whichNotificationOffset
 output parameter.

Note

notificationArray

#### Parameters

notificationArray
 As
 [Object Array](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the notifications on which to wait.

destinationPropObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the
 
 [PropertyObject](../tsapiref/propertyobject.html)
 in which to store the notification data. You can pass a
 NULL
 reference when you do not want to store the data. The type of the destination
 PropertyObject
 must be compatible with the data the notification sends. The
 [Wait Behaviors for Data Set or Pulsed by Value](../tsref/wait-operation-notification-step-configuratio.html)
 and
 [Wait Behaviors for Data Set or Pulsed by Reference](../tsref/wait-operation-notification-step-configuratio.html)
 tables illustrate the wait outcome depending on the type of the data and the data type of the storage location. In these tables, Simple Type refers to a number, string, Boolean, or array of any type, and Structured Type refers to an instance of a user-defined type where the root property is a container.

timeoutInSeconds
 As
 [Double](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a timeout in seconds. Pass a negative number to specify that you do not want a timeout.

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 when you call this method from within a step of an execution. You must use the sequence context of the sequence in which you are calling this method. Pass a
 NULL
 reference when you do not call this method from an execution. This method uses the sequence context to improve the behavior of the execution when it is blocked while waiting on this method.

processMsgs
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to process Microsoft Windows messages while waiting. When you call this method from an execution, pass
 True
 for this parameter. Otherwise, pass
 False
 .

waitRes
 As
 [WaitResult](waitresult.html)

[Out] Returns the
 [status](waitresult.html)
 of the operation.

whichNotification
 As
 [Notification](notification.html)

[Out] Returns a reference to the Notification object that awakens this thread.

whichNotificationOffset
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[Out] Returns the array offset within the
 notificationArray
 parameter of the Notification object that awakens this thread.

#### See Also

[PropertyObject](../tsapiref/propertyobject.html)

[Sequence Context](../tsapiref/sequencecontext.html)

[Wait Behaviors for Data Set or Pulsed by Reference](../tsref/wait-operation-notification-step-configuratio.html)

[Wait Behaviors for Data Set or Pulsed by Value](../tsref/wait-operation-notification-step-configuratio.html)

[WaitResult](waitresult.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/notification.html language=enus -->
## TOPIC 04529: Notification

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/notification.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/notification.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This class implements the Notification synchronization primitive. Use these properties and methods to implement the Notification step type. Property Name (Read Only) Methods ClearEx GetInfo PulseEx SetEx Wait WaitMultiple See Also Notification step type Synchronization Step Types

### Notification

This class implements the Notification synchronization primitive. Use these properties and methods to implement the
 [Notification](../tsref/notification-step.html)
 step type.

#### Property

| Name (Read Only) |
| --- |

#### Methods

| ClearEx |
| --- |
| GetInfo |
| PulseEx |
| SetEx |
| Wait |
| WaitMultiple |

#### See Also

[Notification step type](../tsref/notification-step.html)

[Synchronization Step Types](../tsref/synchronization-step-types.html)

Parent topic:

TestStand Synchronization Server

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/obsolete-autoreleaser-methods.html language=enus -->
## TOPIC 04530: Obsolete AutoReleaser Methods

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/obsolete-autoreleaser-methods.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/obsolete-autoreleaser-methods.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following methods are now obsolete. National Instruments supports these methods but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand. Obsolete Method Preferred Property or Method EarlyRelease AutoReleaser.EarlyReleaseEx method

### Obsolete AutoReleaser Methods

The following methods are now obsolete. National Instruments supports these methods but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand.

| Obsolete Method | Preferred Property or Method |
| --- | --- |
| EarlyRelease | AutoReleaser.EarlyReleaseEx method |

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/obsolete-batch-methods.html language=enus -->
## TOPIC 04531: Obsolete Batch Methods

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/obsolete-batch-methods.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/obsolete-batch-methods.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following methods are now obsolete. National Instruments supports these methods but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand. Obsolete Method Preferred Property or Method ReportRTEOccurred N/A

### Obsolete Batch Methods

The following methods are now obsolete. National Instruments supports these methods but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand.

| Obsolete Method | Preferred Property or Method |
| --- | --- |
| ReportRTEOccurred | N/A |

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/obsolete-mutex-methods.html language=enus -->
## TOPIC 04532: Obsolete Mutex Methods

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/obsolete-mutex-methods.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/obsolete-mutex-methods.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following methods are now obsolete. National Instruments supports these methods but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand. Obsolete Method Preferred Property or Method EarlyUnlockMutex Mutex.EarlyUnlockMutexEx method F

### Obsolete Mutex Methods

The following methods are now obsolete. National Instruments supports these methods but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand.

| Obsolete Method | Preferred Property or Method |
| --- | --- |
| EarlyUnlockMutex | Mutex.EarlyUnlockMutexEx method |
| FinalizeForGroupLock | N/A |
| GetSavedOwnerInfo | N/A |

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/obsolete-notification-methods.html language=enus -->
## TOPIC 04533: Obsolete Notification Methods

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/obsolete-notification-methods.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/obsolete-notification-methods.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following methods are now obsolete. National Instruments supports these methods but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand. Obsolete Method Preferred Property or Method BeginWaitForMultiWait N/A Clear Notification.Clear

### Obsolete Notification Methods

The following methods are now obsolete. National Instruments supports these methods but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand.

| Obsolete Method | Preferred Property or Method |
| --- | --- |
| BeginWaitForMultiWait | N/A |
| Clear | Notification.ClearEx method |
| DoWaitForMultiWait | N/A |
| EndWaitForMultiWait | N/A |
| Pulse | Notification.PulseEx method |
| Set | Notification.SetEx method |

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/obsolete-queue-methods.html language=enus -->
## TOPIC 04534: Obsolete Queue Methods

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/obsolete-queue-methods.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/obsolete-queue-methods.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following methods are now obsolete. National Instruments supports these methods but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand. Obsolete Method Preferred Property or Method BeginDequeueForMultiDequeue N/A DoDequeueForMultiD

### Obsolete Queue Methods

The following methods are now obsolete. National Instruments supports these methods but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand.

| Obsolete Method | Preferred Property or Method |
| --- | --- |
| BeginDequeueForMultiDequeue | N/A |
| DoDequeueForMultiDequeue | N/A |
| EndDequeueForMultiDequeue | N/A |

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/obsolete-semaphore-methods.html language=enus -->
## TOPIC 04535: Obsolete Semaphore Methods

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/obsolete-semaphore-methods.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/obsolete-semaphore-methods.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following method is now obsolete. National Instruments supports these methods but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand. Obsolete Method Preferred Property or Method ReleaseSemaphore Semaphore.ReleaseSemaphoreEx method

### Obsolete Semaphore Methods

The following method is now obsolete. National Instruments supports these methods but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand.

| Obsolete Method | Preferred Property or Method |
| --- | --- |
| ReleaseSemaphore | Semaphore.ReleaseSemaphoreEx method |

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/obsolete-syncmanager-methods.html language=enus -->
## TOPIC 04536: Obsolete SyncManager Methods

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/obsolete-syncmanager-methods.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/obsolete-syncmanager-methods.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following methods are now obsolete. National Instruments supports these methods but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand. Obsolete Method Preferred Property or Method GetLockMutexThreadIsWaitingFor N/A GetMutexOwnerIn

### Obsolete SyncManager Methods

The following methods are now obsolete. National Instruments supports these methods but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand.

| Obsolete Method | Preferred Property or Method |
| --- | --- |
| GetLockMutexThreadIsWaitingFor | N/A |
| GetMutexOwnerInfo | N/A |
| RecordThreadNolongerWaitingForLockMutex | N/A |
| RecordThreadWaitingForLockMutex | N/A |
| ReleaseServerOnDestruct | N/A |

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/obsolete-syncmanager-properties.html language=enus -->
## TOPIC 04537: Obsolete SyncManager Properties

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/obsolete-syncmanager-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/obsolete-syncmanager-properties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following properties are now obsolete. National Instruments supports these properties but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand. Obsolete Property Preferred Property or Method MachineID N/A ProcessID N/A

### Obsolete SyncManager Properties

The following properties are now obsolete. National Instruments supports these properties but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand.

| Obsolete Property | Preferred Property or Method |
| --- | --- |
| MachineID | N/A |
| ProcessID | N/A |

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/properties.html language=enus -->
## TOPIC 04538: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/properties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

Batch

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/properties_2.html language=enus -->
## TOPIC 04539: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/properties_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/properties_2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

Mutex

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/properties_3.html language=enus -->
## TOPIC 04540: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/properties_3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/properties_3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

Notification

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/properties_4.html language=enus -->
## TOPIC 04541: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/properties_4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/properties_4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

Queue

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/properties_5.html language=enus -->
## TOPIC 04542: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/properties_5.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/properties_5.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

Rendezvous

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/properties_6.html language=enus -->
## TOPIC 04543: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/properties_6.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/properties_6.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

Semaphore

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/properties_7.html language=enus -->
## TOPIC 04544: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/properties_7.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/properties_7.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

SyncManager

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/queue-begindequeueformultidequeue.html language=enus -->
## TOPIC 04545: Queue.BeginDequeueForMultiDequeue

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/queue-begindequeueformultidequeue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/queue-begindequeueformultidequeue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Queue.BeginDequeueForMultiDequeue( eventName, operationId) Purpose This method is obsolete. Remarks Do not call this method. This method is for internal use only to implement the Queue.DequeueMultiple method. Parameters eventName As String [Out] Returns an event name the object uses internall

### Queue.BeginDequeueForMultiDequeue

#### Syntax

[Queue](queue.html).BeginDequeueForMultiDequeue( eventName, operationId)

#### Purpose

Note

#### Remarks

Do not call this method. This method is for internal use only to implement the
 [Queue.DequeueMultiple](queue-dequeuemultiple.html)
 method.

#### Parameters

eventName
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[Out] Returns an event name the object uses internally.

operationId
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[Out] Returns an internal value the server uses to wait on multiple Queue objects.

#### See Also

[Queue.DequeueMultiple](queue-dequeuemultiple.html)

Parent topic:

Obsolete Queue Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/queue-dequeue.html language=enus -->
## TOPIC 04546: Queue.Dequeue

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/queue-dequeue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/queue-dequeue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Queue.Dequeue( removeElement, atFront, destinationPropObj, timeoutInSeconds, sequenceContextObj, processMsgs, waitRes) Purpose Dequeues data from the queue. Parameters removeElement As Boolean [In] Pass True to remove the element from the queue. Pass False to retrieve the data for the element

### Queue.Dequeue

#### Syntax

[Queue](queue.html).Dequeue( removeElement, atFront, destinationPropObj, timeoutInSeconds, sequenceContextObj, processMsgs, waitRes)

#### Purpose

Dequeues data from the queue.

#### Parameters

removeElement
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to remove the element from the queue. Pass
 False
 to retrieve the data for the element but leave it in the queue.

atFront
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to retrieve the item at the front of the queue. Pass
 False
 to retrieve the item at the end.

destinationPropObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the
 
 [PropertyObject](../tsapiref/propertyobject.html)
 in which to store the queue element. You can pass a
 NULL
 reference when you do not want to store the data. The type of the destination
 PropertyObject
 must be compatible with the data the element stores. The
 [Dequeue Behaviors for Data You Enqueue by Value](../tsref/dequeue-operation-queue-step-configuration-di.html)
 and
 [Dequeue Behaviors for Data You Enqueue by Reference](../tsref/dequeue-operation-queue-step-configuration-di.html)
 tables illustrate the outcomes depending on the type of the data in the queue and the data type of the destination
 PropertyObject
 . In these tables, Simple Type refers to a number, string, Boolean, or array of any type, and Structured Type refers to an instance of a user-defined type where the root property is a container.

timeoutInSeconds
 As
 [Double](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a timeout in seconds. Pass a negative number to specify you do not want a timeout.

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 when you call this method from within a step of an execution. You must use the sequence context of the sequence in which you are calling this method. Pass a
 NULL
 reference when you do not call this method from an execution. This method uses the sequence context to improve the behavior of the execution when it is blocked while waiting on this method.

processMsgs
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to process Microsoft Windows messages while waiting. When you call this method from an execution, pass
 True
 for this parameter. Otherwise, pass
 False
 .

waitRes
 As
 [WaitResult](waitresult.html)

[Out] Returns the
 [status](waitresult.html)
 of the operation.

#### See Also

[Dequeue Behaviors for Data You Enqueue by Reference](../tsref/dequeue-operation-queue-step-configuration-di.html)

[Dequeue Behaviors for Data You Enqueue by Value](../tsref/dequeue-operation-queue-step-configuration-di.html)

[PropertyObject](../tsapiref/propertyobject.html)

[Sequence Context](../tsapiref/sequencecontext.html)

[WaitResult](waitresult.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/queue-dequeuemultiple.html language=enus -->
## TOPIC 04547: Queue.DequeueMultiple

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/queue-dequeuemultiple.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/queue-dequeuemultiple.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Queue.DequeueMultiple( queueArray, removeElement, atFront, destinationPropObj, timeoutInSeconds, sequenceContextObj, processMsgs, waitRes, whichQueue, whichQueueOffset) Purpose Dequeues data from multiple queues. This method dequeues an element from the first queue you specify that has an ele

### Queue.DequeueMultiple

#### Syntax

[Queue](queue.html).DequeueMultiple( queueArray, removeElement, atFront, destinationPropObj, timeoutInSeconds, sequenceContextObj, processMsgs, waitRes, whichQueue, whichQueueOffset)

#### Purpose

Dequeues data from multiple queues. This method dequeues an element from the first queue you specify that has an element available. You can determine which queues the method dequeues from by checking the value of the
 whichQueue
 or
 whichQueueOffset
 output parameter.

#### Parameters

queueArray
 As
 [Object Array](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the queues from which to dequeue an element.

removeElement
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to remove the element from the queue. Pass
 False
 to retrieve the data for the element but leave it in the queue.

atFront
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to retrieve the item at the front of the queue. Pass
 False
 to retrieve the item at the end.

destinationPropObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the
 
 [PropertyObject](../tsapiref/propertyobject.html)
 in which to store the queue element. You can pass a
 NULL
 reference when you do not want to store the data. The type of the destination
 PropertyObject
 must be compatible with the data the element stores. The
 [Dequeue Behaviors for Data You Enqueue by Value](../tsref/dequeue-operation-queue-step-configuration-di.html)
 and
 [Dequeue Behaviors for Data You Enqueue by Reference](../tsref/dequeue-operation-queue-step-configuration-di.html)
 tables illustrate the outcomes depending on the type of the data in the queue and the data type of the destination
 PropertyObject
 . In these tables, Simple Type refers to a number, string, Boolean, or array of any type, and Structured Type refers to an instance of a user-defined type where the root property is a container.

timeoutInSeconds
 As
 [Double](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a timeout in seconds. Pass a negative number to specify that you do not want a timeout.

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 when you call this method from within a step of an execution. You must use the sequence context of the sequence in which you are calling this method. Pass a
 NULL
 reference when you do not call this method from an execution. This method uses the sequence context to improve the behavior of the execution when it is blocked while waiting on this method.

processMsgs
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to process Microsoft Windows messages while waiting. When you call this method from an execution, pass
 True
 for this parameter. Otherwise, pass
 False
 .

waitRes
 As
 [WaitResult](waitresult.html)

[Out] Returns the
 [status](waitresult.html)
 of the operation.

whichQueue
 As
 [Queue](queue.html)

[Out] Returns a reference to the Queue object from which the element was dequeued.

whichQueueOffset
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[Out] Returns the array offset within the
 queueArray
 parameter of the queue from which the element was dequeued.

#### See Also

[Dequeue Behaviors for Data You Enqueue by Reference](../tsref/dequeue-operation-queue-step-configuration-di.html)

[Dequeue Behaviors for Data You Enqueue by Value](../tsref/dequeue-operation-queue-step-configuration-di.html)

[PropertyObject](../tsapiref/propertyobject.html)

[Sequence Context](../tsapiref/sequencecontext.html)

[WaitResult](waitresult.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/queue-dodequeueformultidequeue.html language=enus -->
## TOPIC 04548: Queue.DoDequeueForMultiDequeue

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/queue-dodequeueformultidequeue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/queue-dodequeueformultidequeue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Queue.DoDequeueForMultiDequeue( sequenceContextObj, removeElement, atFront, destinationPropObj, operationId, keepWaitingParam) Purpose This method is obsolete. Remarks Do not call this method. This method is for internal use only to implement the Queue.DequeueMultiple method. Parameters seque

### Queue.DoDequeueForMultiDequeue

#### Syntax

[Queue](queue.html).DoDequeueForMultiDequeue( sequenceContextObj, removeElement, atFront, destinationPropObj, operationId, keepWaitingParam)

#### Purpose

Note

#### Remarks

Do not call this method. This method is for internal use only to implement the
 [Queue.DequeueMultiple](queue-dequeuemultiple.html)
 method.

#### Parameters

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 when you call this method from within a step of an execution. You must use the sequence context of the sequence in which you are calling this method. Pass a
 NULL
 reference when you do not call this method from an execution. This method uses the sequence context to improve the behavior of the execution when it is blocked while waiting on this method.

removeElement
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to remove the element from the queue. Pass
 False
 to retrieve the data for the element but leave it in the queue.

atFront
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to retrieve the item at the front of the queue. Pass
 False
 to retrieve the item at the end.

destinationPropObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the
 
 [PropertyObject](../tsapiref/propertyobject.html)
 in which to store the queue element. You can pass a
 NULL
 reference when you do not want to store the data. The type of the destination
 PropertyObject
 must be compatible with the data the element stores. The
 [Dequeue Behaviors for Data You Enqueue by Value](../tsref/dequeue-operation-queue-step-configuration-di.html)
 and
 [Dequeue Behaviors for Data You Enqueue by Reference](../tsref/dequeue-operation-queue-step-configuration-di.html)
 tables illustrate the outcomes depending on the type of the data in the queue and the data type of the destination
 PropertyObject
 . In these tables, Simple Type refers to a number, string, Boolean, or array of any type, and Structured Type refers to an instance of a user-defined type where the root property is a container.

operationId
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[In] Specifies an internal value the server uses to dequeue from multiple Queue objects.

keepWaitingParam
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[Out] Returns
 True
 when the caller should call this method again to retry the operation.

#### See Also

[Dequeue Behaviors for Data You Enqueue by Reference](../tsref/dequeue-operation-queue-step-configuration-di.html)

[Dequeue Behaviors for Data You Enqueue by Value](../tsref/dequeue-operation-queue-step-configuration-di.html)

[PropertyObject](../tsapiref/propertyobject.html)

[Queue.DequeueMultiple](queue-dequeuemultiple.html)

[Sequence Context](../tsapiref/sequencecontext.html)

Parent topic:

Obsolete Queue Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/queue-enddequeueformultidequeue.html language=enus -->
## TOPIC 04549: Queue.EndDequeueForMultiDequeue

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/queue-enddequeueformultidequeue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/queue-enddequeueformultidequeue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Queue.EndDequeueForMultiDequeue( operationId) Purpose This method is obsolete. Remarks Do not call this method. This method is for internal use only to implement the Queue.DequeueMultiple method. Parameters operationId As Long [In] Specifies an internal value the server uses to dequeue from m

### Queue.EndDequeueForMultiDequeue

#### Syntax

[Queue](queue.html).EndDequeueForMultiDequeue( operationId)

#### Purpose

Note

#### Remarks

Do not call this method. This method is for internal use only to implement the
 [Queue.DequeueMultiple](queue-dequeuemultiple.html)
 method.

#### Parameters

operationId
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[In] Specifies an internal value the server uses to dequeue from multiple Queue objects.

#### See Also

[Queue.DequeueMultiple](queue-dequeuemultiple.html)

Parent topic:

Obsolete Queue Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/queue-enqueue.html language=enus -->
## TOPIC 04550: Queue.Enqueue

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/queue-enqueue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/queue-enqueue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Queue.Enqueue( atFront, fqOption, newElementPropObj, byRef, timeoutInSeconds, sequenceContextObj, processMsgs, waitRes, enqueueRes) Purpose Enqueues data into the queue. Parameters atFront As Boolean [In] Pass True to insert the new item at the front of the queue. Pass False to insert the new

### Queue.Enqueue

#### Syntax

[Queue](queue.html).Enqueue( atFront, fqOption, newElementPropObj, byRef, timeoutInSeconds, sequenceContextObj, processMsgs, waitRes, enqueueRes)

#### Purpose

Enqueues data into the queue.

#### Parameters

atFront
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to insert the new item at the front of the queue. Pass
 False
 to insert the new item at the end.

fqOption
 As
 [FullQueueOption](fullqueueoption.html)

[In] Specifies what to do when the queue is full. Refer to the
 [FullQueueOption](fullqueueoption.html)
 enumeration for more information about values for this parameter.

newElementPropObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [PropertyObject](../tsapiref/propertyobject.html)
 that is the item or contains the value of the item to insert into the queue. You can use data of any type, including a number, string, Boolean, object reference, structured type (container), or arrays of these types. When you dequeue the element you must specify a destination
 PropertyObject
 with the appropriate type.

byRef
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] When you pass
 False
 , the queue stores a copy of the data you enqueue. When you pass
 True
 , the Enqueue operation stores an object reference to the data value.

timeoutInSeconds
 As
 [Double](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the timeout, in seconds. Pass a negative number to specify that you do not want a timeout.

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 when you call this method from within a step of an execution. You must use the sequence context of the sequence in which you are calling this method. Pass a
 NULL
 reference when you do not call this method from an execution. This method uses the sequence context to improve the behavior of the execution when it is blocked while waiting on this method.

processMsgs
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to process Microsoft Windows messages while waiting. When you call this method from an execution, pass
 True
 for this parameter. Otherwise, pass
 False
 .

waitRes
 As
 [WaitResult](waitresult.html)

[Out] Returns the
 [status](waitresult.html)
 of the Enqueue operation.

enqueueRes
 As
 [EnqueueResult](enqueueresult.html)

[Out] Returns the
 [result of the Enqueue operation](enqueueresult.html)
 .

#### See Also

[EnqueueResult](enqueueresult.html)

[FullQueueOption](fullqueueoption.html)

[PropertyObject](../tsapiref/propertyobject.html)

[Sequence Context](../tsapiref/sequencecontext.html)

[WaitResult](waitresult.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/queue-flush.html language=enus -->
## TOPIC 04551: Queue.Flush

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/queue-flush.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/queue-flush.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Queue.Flush( sequenceContextObj, destQueueElementsArrayPropObj) Purpose Empties the queue and optionally retrieves all its elements. Parameters sequenceContextObj As Object [In] Specifies a sequence context . You can pass NULL for this parameter, but when you want to retrieve the elements, yo

### Queue.Flush

#### Syntax

[Queue](queue.html).Flush( sequenceContextObj, destQueueElementsArrayPropObj)

#### Purpose

Empties the queue and optionally retrieves all its elements.

#### Parameters

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 . You can pass
 NULL
 for this parameter, but when you want to retrieve the elements, you must pass a valid sequence context.

destQueueElementsArrayPropObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies an array
 
 [PropertyObject](../tsapiref/propertyobject.html)
 in which to store the elements of the queue. All queue elements must be of the same data type as the array you specify and no queue element can be an array. You can pass
 NULL
 for this parameter.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/queue-getinfo.html language=enus -->
## TOPIC 04552: Queue.GetInfo

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/queue-getinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/queue-getinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Queue.GetInfo( sequenceContextObj, destQueueElementsArrayPropObj, numThreadsWaitingToEnqueue, numThreadsWaitingToDequeue, sizeLimit, numElements) Purpose Obtains information about the queue and optionally retrieves all its elements. Parameters sequenceContextObj As Object [In] Specifies a seq

### Queue.GetInfo

#### Syntax

[Queue](queue.html).GetInfo( sequenceContextObj, destQueueElementsArrayPropObj, numThreadsWaitingToEnqueue, numThreadsWaitingToDequeue, sizeLimit, numElements)

#### Purpose

Obtains information about the queue and optionally retrieves all its elements.

#### Parameters

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 . You can pass
 NULL
 for this parameter, but to retrieve the elements, you must pass a valid sequence context.

destQueueElementsArrayPropObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies an array
 
 [PropertyObject](../tsapiref/propertyobject.html)
 in which to store the elements of the queue. All queue elements must be of the same data type as the array you specify and no queue element can be an array. You can pass
 NULL
 for this parameter.

numThreadsWaitingToEnqueue
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[Out] Returns the number of threads waiting to perform an Enqueue operation. You can pass
 NULL
 for this parameter.

numThreadsWaitingToDequeue
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[Out] Returns the number of threads waiting to perform a Dequeue operation. You can pass
 NULL
 for this parameter.

sizeLimit
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[Out] Returns the size limit of the queue. A value less than or equal to zero indicates that the queue does not have a maximum size. You can pass
 NULL
 for this parameter.

numElements
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[Out] Returns the number of elements in the queue. You can pass
 NULL
 for this parameter.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/queue-name.html language=enus -->
## TOPIC 04553: Queue.Name

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/queue-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/queue-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Queue.Name Data Type String Purpose Returns the name of the queue.

### Queue.Name

#### Syntax

[Queue](queue.html).Name

#### Data Type

[String](data-types-for-teststand-synchronization-serv.html)

#### Purpose

Returns the name of the queue.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/queue.html language=enus -->
## TOPIC 04554: Queue

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/queue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/queue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This class implements the Queue synchronization primitive. Use these properties and methods to implement the Queue step type. Property Name (Read Only) Methods Dequeue DequeueMultiple Enqueue Flush GetInfo See Also Queue step type Synchronization Step Types

### Queue

This class implements the Queue synchronization primitive. Use these properties and methods to implement the
 [Queue](../tsref/queue-step.html)
 step type.

#### Property

| Name (Read Only) |
| --- |

#### Methods

| Dequeue |
| --- |
| DequeueMultiple |
| Enqueue |
| Flush |
| GetInfo |

#### See Also

[Queue step type](../tsref/queue-step.html)

[Synchronization Step Types](../tsref/synchronization-step-types.html)

Parent topic:

TestStand Synchronization Server

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/rendezvous-getinfo.html language=enus -->
## TOPIC 04555: Rendezvous.GetInfo

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/rendezvous-getinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/rendezvous-getinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Rendezvous.GetInfo( numThreadsWaiting, rendezvousCount) Purpose Obtains information about the current state of the rendezvous. Parameters numThreadsWaiting As Long [Out] Returns the number of threads waiting for the rendezvous condition. rendezvousCount As Long [Out] Returns the number of thr

### Rendezvous.GetInfo

#### Syntax

[Rendezvous](rendezvous.html).GetInfo( numThreadsWaiting, rendezvousCount)

#### Purpose

Obtains information about the current state of the rendezvous.

#### Parameters

numThreadsWaiting
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[Out] Returns the number of threads waiting for the rendezvous condition.

rendezvousCount
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[Out] Returns the number of threads that must call the
 [Rendezvous.Rendezvous](rendezvous-rendezvous.html)
 method to satisfy the rendezvous condition.

#### See Also

[Rendezvous.Rendezvous](rendezvous-rendezvous.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/rendezvous-name.html language=enus -->
## TOPIC 04556: Rendezvous.Name

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/rendezvous-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/rendezvous-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Rendezvous.Name Data Type String Purpose Returns the name of the rendezvous.

### Rendezvous.Name

#### Syntax

[Rendezvous](rendezvous.html).Name

#### Data Type

[String](data-types-for-teststand-synchronization-serv.html)

#### Purpose

Returns the name of the rendezvous.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/rendezvous-rendezvous.html language=enus -->
## TOPIC 04557: Rendezvous.Rendezvous

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/rendezvous-rendezvous.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/rendezvous-rendezvous.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Rendezvous.Rendezvous( timeoutInSeconds, sequenceContextObj, processMsgs, waitRes) Purpose Waits for the rendezvous condition to occur. The rendezvous condition occurs when all the threads the rendezvous requires call this method. Parameters timeoutInSeconds As Double [In] Specifies a timeout

### Rendezvous.Rendezvous

#### Syntax

[Rendezvous](rendezvous.html).Rendezvous( timeoutInSeconds, sequenceContextObj, processMsgs, waitRes)

#### Purpose

Waits for the rendezvous condition to occur. The rendezvous condition occurs when all the threads the rendezvous requires call this method.

#### Parameters

timeoutInSeconds
 As
 [Double](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a timeout, in seconds. Pass a negative number to specify that you do not want a timeout.

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 when you call this method from within a step of an execution. You must use the sequence context of the sequence in which you are calling this method. Pass a
 NULL
 reference when you do not call this method from an execution. This method uses the sequence context to improve the behavior of the execution when it is blocked while waiting on this method.

processMsgs
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to process Microsoft Windows messages while waiting. When you call this method from an execution, pass
 True
 for this parameter. Otherwise, pass
 False
 .

waitRes
 As
 [WaitResult](waitresult.html)

[Out] Returns the
 [status](waitresult.html)
 of the operation.

#### See Also

[Sequence Context](../tsapiref/sequencecontext.html)

[WaitResult](waitresult.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/rendezvous.html language=enus -->
## TOPIC 04558: Rendezvous

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/rendezvous.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/rendezvous.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This class implements the Rendezvous synchronization primitive. Use these properties and methods to implement the Rendezvous step type. Property Name (Read Only) Methods GetInfo Rendezvous See Also Rendezvous step type Synchronization Step Types

### Rendezvous

This class implements the Rendezvous synchronization primitive. Use these properties and methods to implement the
 [Rendezvous](../tsref/rendezvous-step.html)
 step type.

#### Property

| Name (Read Only) |
| --- |

#### Methods

| GetInfo |
| --- |
| Rendezvous |

#### See Also

[Rendezvous step type](../tsref/rendezvous-step.html)

[Synchronization Step Types](../tsref/synchronization-step-types.html)

Parent topic:

TestStand Synchronization Server

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/resourceusageoutputmessagesubproperties.html language=enus -->
## TOPIC 04559: ResourceUsageOutputMessageSubProperties

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/resourceusageoutputmessagesubproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/resourceusageoutputmessagesubproperties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify subproperty names for additional OutputMessage information stored in resource usage output messages. OutputMessageSubProperty_BatchType –(Value: "ResourceUsage.BatchType") This numeric property exists only for batch synchronization operations. The value is the numeric

### ResourceUsageOutputMessageSubProperties

Use these constants to specify subproperty names for additional
 
 [OutputMessage](../tsapiref/outputmessage.html)
 information stored in resource usage output messages.

- OutputMessageSubProperty_BatchType 
 –(Value: "ResourceUsage.BatchType") This numeric property exists only for batch synchronization operations. The value is the numeric value of the
 BatchSyncType 
 enumeration that identifies the section type.
- OutputMessageSubProperty_ExecutionDisplayName 
 –(Value: "ResourceUsage.ExecutionDisplayName") When this string property exists, it indicates the display name of the execution that initiated the synchronization operation.
- OutputMessageSubProperty_ExecutionId 
 –(Value: "ResourceUsage.ExecutionId") When this numeric property exists, it indicates the ID of the execution that initiated the synchronization operation.
- OutputMessageSubProperty_FromProcessModel 
 –(Value: "ResourceUsage.FromProcessModel") When the
 
 OutputMessage 
 describes a resource usage synchronization state that occurs in a process model file, this Boolean subproperty is
 True 
 . Otherwise, this subproperty does not exist. This property does not necessarily exist for
 SyncState_Completed 
 synchronization states that occur in process models.
- OutputMessageSubProperty_Operation 
 –(Value: "ResourceUsage.Operation") This string property identifies the synchronization operation that generated the
 OutputMessage 
 .
- OutputMessageSubProperty_ResourceAlternativeIndex 
 –(Value: "ResourceUsage.ResourceAlternativeIndex") When the
 OutputMessage 
 describes a resource usage synchronization state of
 SyncState_InUse 
 for a
 Use Auto Scheduled Resource 
 step and the step is configured for multiple resource alternatives, this numeric property indicates the zero-based index of the acquired resource alternative. This string property does not exist for all other resource usage synchronization states.
- OutputMessageSubProperty_ResourceName 
 –(Value: "ResourceUsage.ResourceName") The string subproperty in which the
 SyncManager.LogAction 
 method stores the name of the resource.
- OutputMessageSubProperty_SocketCount 
 –(Value: "ResourceUsage.TestSockets.Count") The numeric subproperty in which the
 SyncManager.LogAction 
 method stores the number of test sockets.
- OutputMessageSubProperty_SocketIndex 
 –(Value: "ResourceUsage.TestSockets.MyIndex") The numeric subproperty in which the
 SyncManager.LogAction 
 method stores the Test Socket index of the thread that performs the resource action.
- OutputMessageSubProperty_SynchronizationMechanism 
 –(Value: "SynchronizationMechanism") This string property identifies the synchronization mechanism that generated the
 OutputMessage 
 .
- OutputMessageSubProperty_SynchronizationState 
 –(Value: "ResourceUsage.SynchronizationState") The numeric subproperty in which the
 SyncManager.LogAction 
 method stores the synchronization state type.
- OutputMessageSubProperty_ThreadDisplayName 
 –(Value: "ResourceUsage.ThreadDisplayName") When this string property exists, it indicates the display name of the thread that initiated the synchronization operation.
- OutputMessageSubProperty_ThreadId 
 –(Value: "ResourceUsage.ThreadId") Stores a string that contains the unique thread ID string for the thread that initiated the synchronization action.
- OutputMessageSubProperty_TimeoutPeriod 
 –(Value: "ResourceUsage.TimeoutPeriod") The numeric subproperty in which the
 SyncManager.LogAction 
 method stores the timeout period for a synchronization state of
 SyncState_Blocked 
 . For other synchronization state types, this subproperty does not exist.
- OutputMessageSubProperty_UseResourceStepDescription 
 –(Value: "ResourceUsage.UseResourceStepDescription") When the
 OutputMessage 
 describes a resource usage action of the
 SyncState_InUse 
 type for a Use Auto Scheduled Resource step, this string subproperty indicates the display description of the step.

#### See Also

[BatchSyncType](batchsynctype.html)

[SyncStates](syncstates.html)

[SyncManager.LogAction](syncmanager-logaction.html)

[OutputMessage](../tsapiref/outputmessage.html)

Parent topic:

API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/semaphore-acquiresemaphore.html language=enus -->
## TOPIC 04560: Semaphore.AcquireSemaphore

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/semaphore-acquiresemaphore.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/semaphore-acquiresemaphore.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Semaphore.AcquireSemaphore( timeoutInSeconds, sequenceContextObj, processMsgs, waitRes) Purpose Performs an Acquire (decrement) operation on the semaphore. Parameters timeoutInSeconds As Double [In] Specifies a timeout in seconds. Pass a negative number to specify that you do not want a time

### Semaphore.AcquireSemaphore

#### Syntax

[Semaphore](semaphore.html).AcquireSemaphore( timeoutInSeconds, sequenceContextObj, processMsgs, waitRes)

#### Purpose

Performs an Acquire (decrement) operation on the semaphore.

#### Parameters

timeoutInSeconds
 As
 [Double](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a timeout in seconds. Pass a negative number to specify that you do not want a time out.

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 when you call this method from within a step of an execution. You must use the sequence context of the sequence in which you are calling this method. Pass a
 NULL
 reference when you do not call this method from an execution. The semaphore uses the sequence context to improve the behavior of the execution when it is blocked while waiting on the semaphore.

processMsgs
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to process Microsoft Windows messages while waiting to acquire the semaphore. When you call this method from an execution, pass
 True
 for this parameter. Otherwise, pass
 False
 .

waitRes
 As
 [WaitResult](waitresult.html)

[Out] Returns the
 [status](waitresult.html)
 of the Acquire operation.

#### See Also

[Sequence Context](../tsapiref/sequencecontext.html)

[WaitResult](waitresult.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/semaphore-acquiresemaphorewithautoreleaser.html language=enus -->
## TOPIC 04561: Semaphore.AcquireSemaphoreWithAutoReleaser

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/semaphore-acquiresemaphorewithautoreleaser.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/semaphore-acquiresemaphorewithautoreleaser.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Semaphore.AcquireSemaphoreWithAutoReleaser( timeoutInSeconds, sequenceContextObj, processMsgs, waitRes) Return Value AutoReleaser An object that automatically calls the Semaphore.ReleaseSemaphoreEx method on the semaphore when you release the last reference to the AutoReleaser object. Purpose

### Semaphore.AcquireSemaphoreWithAutoReleaser

#### Syntax

[Semaphore](semaphore.html).AcquireSemaphoreWithAutoReleaser( timeoutInSeconds, sequenceContextObj, processMsgs, waitRes)

#### Return Value

[AutoReleaser](autoreleaser.html)

An object that automatically calls the
 [Semaphore.ReleaseSemaphoreEx](semaphore-releasesemaphoreex.html)
 method on the semaphore when you release the last reference to the
 AutoReleaser
 object.

#### Purpose

Performs an Acquire (decrement) operation on the semaphore and returns an
 AutoReleaser
 object that automatically calls the
 [Semaphore.ReleaseSemaphoreEx](semaphore-releasesemaphoreex.html)
 method when you release the last reference to the
 [AutoReleaser](autoreleaser.html)
 object. This is useful for controlling the lifetime of the Acquire operation.

#### Parameters

timeoutInSeconds
 As
 [Double](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a timeout in seconds. Pass a negative number to specify that you do not want a timeout.

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 when you call this method from within a step of an execution. You must use the sequence context of the sequence in which you are calling this method. Pass a
 NULL
 reference when you do not call this method from an execution. This method uses the sequence context to improve the behavior of the execution when it is blocked while waiting on this method.

processMsgs
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to process Microsoft Windows messages while waiting. When you call this method from an execution, pass
 True
 for this parameter. Otherwise, pass
 False
 .

waitRes
 As
 [WaitResult](waitresult.html)

[Out] Returns the
 [status](waitresult.html)
 of the Acquire operation.

#### See Also

[AutoReleaser](autoreleaser.html)

[Semaphore.ReleaseSemaphore](semaphore-releasesemaphore.html)

[Semaphore.ReleaseSemaphoreEx](semaphore-releasesemaphoreex.html)

[Sequence Context](../tsapiref/sequencecontext.html)

[WaitResult](waitresult.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/semaphore-getinfo.html language=enus -->
## TOPIC 04562: Semaphore.GetInfo

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/semaphore-getinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/semaphore-getinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Semaphore.GetInfo( numThreadsWaitingToAcquire, currentCount, initialCount, maxCount) Purpose Obtains information about the current state of the semaphore. Parameters numThreadsWaitingToAcquire As Long [Out] Returns the number of threads waiting to acquire the semaphore. currentCount As Long [

### Semaphore.GetInfo

#### Syntax

[Semaphore](semaphore.html).GetInfo( numThreadsWaitingToAcquire, currentCount, initialCount, maxCount)

#### Purpose

Obtains information about the current state of the semaphore.

#### Parameters

numThreadsWaitingToAcquire
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[Out] Returns the number of threads waiting to acquire the semaphore.

currentCount
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[Out] Returns the current count for the semaphore.

initialCount
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[Out] Returns the value of the
 initialCount
 parameter when the
 [SyncManager.CreateSemaphore](syncmanager-createsemaphore.html)
 method creates the object.

maxCount
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[Out] Returns the value of the
 maxCount
 parameter when the
 SyncManager.CreateSemaphore
 method creates the object.

#### See Also

[SyncManager.CreateSemaphore](syncmanager-createsemaphore.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/semaphore-name.html language=enus -->
## TOPIC 04563: Semaphore.Name

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/semaphore-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/semaphore-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Semaphore.Name Data Type String Purpose Returns the name of the semaphore.

### Semaphore.Name

#### Syntax

[Semaphore](semaphore.html).Name

#### Data Type

[String](data-types-for-teststand-synchronization-serv.html)

#### Purpose

Returns the name of the semaphore.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/semaphore-releasesemaphore.html language=enus -->
## TOPIC 04564: Semaphore.ReleaseSemaphore

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/semaphore-releasesemaphore.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/semaphore-releasesemaphore.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Semaphore.ReleaseSemaphore Purpose This method is obsolete. Use the Semaphore.ReleaseSemaphoreEx method instead. Remarks Performs a Release (increment) operation on the semaphore. Use this method when you want direct control over the count of the semaphore or when you use semaphores in a way

### Semaphore.ReleaseSemaphore

#### Syntax

[Semaphore](semaphore.html).ReleaseSemaphore

#### Purpose

Note

Semaphore.ReleaseSemaphoreEx

#### Remarks

Performs a Release (increment) operation on the semaphore. Use this method when you want direct control over the count of the semaphore or when you use semaphores in a way that requires unmatched increments and decrements. When you use the
 [Semaphore.AcquireSemaphoreWithAutoReleaser](semaphore-acquiresemaphorewithautoreleaser.html)
 method, releasing the last reference to the
 [AutoReleaser](autoreleaser.html)
 object calls this method automatically.

#### See Also

[AutoReleaser](autoreleaser.html)

[Semaphore.AcquireSemaphoreWithAutoReleaser](semaphore-acquiresemaphorewithautoreleaser.html)

Parent topic:

Obsolete Semaphore Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/semaphore-releasesemaphoreex.html language=enus -->
## TOPIC 04565: Semaphore.ReleaseSemaphoreEx

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/semaphore-releasesemaphoreex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/semaphore-releasesemaphoreex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Semaphore.ReleaseSemaphoreEx( sequenceContextObj, threadId) Purpose Performs a Release (increment) operation on the semaphore. Use this method when you want direct control over the count of the semaphore or when you use semaphores in a way that requires unmatched increments and decrements. Wh

### Semaphore.ReleaseSemaphoreEx

#### Syntax

[Semaphore](semaphore.html).ReleaseSemaphoreEx( sequenceContextObj, threadId)

#### Purpose

Performs a Release (increment) operation on the semaphore. Use this method when you want direct control over the count of the semaphore or when you use semaphores in a way that requires unmatched increments and decrements. When you use the
 [Semaphore.AcquireSemaphoreWithAutoReleaser](semaphore-acquiresemaphorewithautoreleaser.html)
 method, releasing the last reference to the
 [AutoReleaser](autoreleaser.html)
 object calls this method automatically.

#### Parameters

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a
 
 [sequence context](../tsapiref/sequencecontext.html)
 when you call this method from within a step of an execution. You must use the sequence context of the sequence in which you are calling this method. Pass a
 NULL
 reference when you do not call this method from an execution.

threadId
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the thread ID of the thread that releases the semaphore. You can pass
 NULL
 or an empty string for this parameter when you already are passing in the sequence context or when you do not want the
 [Resource Usage Profiler](/csh?context=ts_9920)
 to account for this operation.

#### See Also

[AutoReleaser](autoreleaser.html)

[Resource Usage Profiler](/csh?context=ts_9920)

[Semaphore.AcquireSemaphoreWithAutoReleaser](semaphore-acquiresemaphorewithautoreleaser.html)

[Sequence Context](../tsapiref/sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/semaphore.html language=enus -->
## TOPIC 04566: Semaphore

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/semaphore.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/semaphore.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This class implements the Semaphore synchronization primitive. Use these properties and methods to implement the Semaphore step type. Property Name (Read Only) Methods AcquireSemaphore AcquireSemaphoreWithAutoReleaser GetInfo ReleaseSemaphoreEx See Also Semaphore step type Synchronization Step Types

### Semaphore

This class implements the Semaphore synchronization primitive. Use these properties and methods to implement the
 [Semaphore](../tsref/semaphore-step.html)
 step type.

#### Property

| Name (Read Only) |
| --- |

#### Methods

| AcquireSemaphore |
| --- |
| AcquireSemaphoreWithAutoReleaser |
| GetInfo |
| ReleaseSemaphoreEx |

#### See Also

[Semaphore step type](../tsref/semaphore-step.html)

[Synchronization Step Types](../tsref/synchronization-step-types.html)

Parent topic:

TestStand Synchronization Server

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/synchronizationmechanism.html language=enus -->
## TOPIC 04567: SynchronizationMechanism

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/synchronizationmechanism.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/synchronizationmechanism.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants identify the different synchronization mechanisms TestStand provides. SynchronizationMechanism_AutoSchedule –(Value: "AutoSchedule") SynchronizationMechanism_Batch –(Value: "Batch") SynchronizationMechanism_Lock –(Value: "Lock") SynchronizationMechanism_Notification –(Value: "Notific

### SynchronizationMechanism

These constants identify the different synchronization mechanisms TestStand provides.

- SynchronizationMechanism_AutoSchedule 
 –(Value: "AutoSchedule")
- SynchronizationMechanism_Batch 
 –(Value: "Batch")
- SynchronizationMechanism_Lock 
 –(Value: "Lock")
- SynchronizationMechanism_Notification 
 –(Value: "Notification")
- SynchronizationMechanism_Queue 
 –(Value: "Queue")
- SynchronizationMechanism_Rendezvous 
 –(Value: "Rendezvous")
- SynchronizationMechanism_Semaphore 
 –(Value: "Semaphore")
- SynchronizationMechanism_Wait 
 –(Value: "Wait")

Parent topic:

API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-beginlogging.html language=enus -->
## TOPIC 04568: SyncManager.BeginLogging

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-beginlogging.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-beginlogging.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.BeginLogging Return Value Long Returns the number of unbalanced calls to this method. Purpose Sets the value of the SyncManager.LoggingEnabled property to True . You must balance each call to this method with a call to the SyncManager.EndLogging method. See Also SyncManager.EndLog

### SyncManager.BeginLogging

#### Syntax

[SyncManager](syncmanager.html).BeginLogging

#### Return Value

[Long](data-types-for-teststand-synchronization-serv.html)

Returns the number of unbalanced calls to this method.

#### Purpose

Sets the value of the
 [SyncManager.LoggingEnabled](syncmanager-loggingenabled.html)
 property to
 True
 . You must balance each call to this method with a call to the
 [SyncManager.EndLogging](syncmanager-endlogging.html)
 method.

#### See Also

[SyncManager.EndLogging](syncmanager-endlogging.html)

[SyncManager.LoggingEnabled](syncmanager-loggingenabled.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-createbatch.html language=enus -->
## TOPIC 04569: SyncManager.CreateBatch

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-createbatch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-createbatch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.CreateBatch( name, alreadyExists) Return Value Batch Purpose Creates or retrieves a Batch object with the name and settings you specify. Parameters name As String [In] Specifies a unique name for the Synchronization object. When the Synchronization object name begins with an aster

### SyncManager.CreateBatch

#### Syntax

[SyncManager](syncmanager.html).CreateBatch( name, alreadyExists)

#### Return Value

[Batch](batch.html)

#### Purpose

Creates or retrieves a
 [Batch](batch.html)
 object with the name and settings you specify.

#### Parameters

name
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a unique name for the Synchronization object. When the Synchronization object name begins with an asterisk,
 *
 , such as
 *syncobjectname
 , processes can share the object.

When the Synchronization object name begins with a computer name, such as
 \\computername\syncobjectname
 , you can share the object among computers, but the object resides on the computer for which you specify a name.

When the Synchronization object name begins with an asterisk or computer name, you can use a
 32
 or
 64
 prefix to specify using 32- or 64-bit TestStand to host the out-of-process Synchronization object. For example, the name
 64*syncobj
 specifies a Synchronization object called
 *syncobj
 in the 64-bit TestStand host process, even when used from 32-bit TestStand. Use the prefix to share Synchronization objects between 32-bit TestStand and 64-bit TestStand in the same host process. If you do not use the prefix, 32-bit TestStand hosts out-of-process Synchronization objects in a 32-bit process, and 64-bit TestStand hosts out-of-process Synchronization objects in a 64-bit process.

alreadyExists
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[Out] Returns
 True
 when the Synchronization object for which you specify a name already exists.

When the object already exists, this method returns the existing object rather than creating a new object.

#### See Also

[Batch](batch.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-createmutex.html language=enus -->
## TOPIC 04570: SyncManager.CreateMutex

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-createmutex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-createmutex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.CreateMutex( name, alreadyExists) Return Value Mutex Purpose Creates or retrieves a Mutex object with the name and settings you specify. Parameters name As String [In] Specifies a unique name for the Synchronization object. When the Synchronization object name begins with an aster

### SyncManager.CreateMutex

#### Syntax

[SyncManager](syncmanager.html).CreateMutex( name, alreadyExists)

#### Return Value

[Mutex](mutex.html)

#### Purpose

Creates or retrieves a
 [Mutex](mutex.html)
 object with the name and settings you specify.

#### Parameters

name
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a unique name for the Synchronization object. When the Synchronization object name begins with an asterisk,
 *
 , such as
 *syncobjectname
 , processes can share the object.

When the Synchronization object name begins with a computer name, such as
 \\computername\syncobjectname
 , you can share the object among computers, but the object resides on the computer for which you specify a name.

When the Synchronization object name begins with an asterisk or computer name, you can use a
 32
 or
 64
 prefix to specify using 32- or 64-bit TestStand to host the out-of-process Synchronization object. For example, the name
 64*syncobj
 specifies a Synchronization object called
 *syncobj
 in the 64-bit TestStand host process, even when used from 32-bit TestStand. Use the prefix to share Synchronization objects between 32-bit TestStand and 64-bit TestStand in the same host process. If you do not use the prefix, 32-bit TestStand hosts out-of-process Synchronization objects in a 32-bit process, and 64-bit TestStand hosts out-of-process Synchronization objects in a 64-bit process.

alreadyExists
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[Out] Returns
 True
 when the Synchronization object for which you specify a name already exists.

When the object already exists, this method returns the existing object rather than creating a new object.

#### See Also

[Mutex](mutex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-createnotification.html language=enus -->
## TOPIC 04571: SyncManager.CreateNotification

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-createnotification.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-createnotification.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.CreateNotification( name, alreadyExists) Return Value Notification Purpose Creates or retrieves a Notification object with the name and settings you specify. Parameters name As String [In] Specifies a unique name for the Synchronization object. When the Synchronization object name

### SyncManager.CreateNotification

#### Syntax

[SyncManager](syncmanager.html).CreateNotification( name, alreadyExists)

#### Return Value

[Notification](notification.html)

#### Purpose

Creates or retrieves a
 [Notification](notification.html)
 object with the name and settings you specify.

#### Parameters

name
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a unique name for the Synchronization object. When the Synchronization object name begins with an asterisk,
 *
 , such as
 *syncobjectname
 , processes can share the object.

When the Synchronization object name begins with a computer name, such as
 \\computername\syncobjectname
 , you can share the object among computers, but the object resides on the computer for which you specify a name.

When the Synchronization object name begins with an asterisk or computer name, you can use a
 32
 or
 64
 prefix to specify using 32- or 64-bit TestStand to host the out-of-process Synchronization object. For example, the name
 64*syncobj
 specifies a Synchronization object called
 *syncobj
 in the 64-bit TestStand host process, even when used from 32-bit TestStand. Use the prefix to share Synchronization objects between 32-bit TestStand and 64-bit TestStand in the same host process. If you do not use the prefix, 32-bit TestStand hosts out-of-process Synchronization objects in a 32-bit process, and 64-bit TestStand hosts out-of-process Synchronization objects in a 64-bit process.

alreadyExists
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[Out] Returns
 True
 when the Synchronization object for which you specify a name already exists.

When the object already exists, this method returns the existing object rather than creating a new object.

#### See Also

[Notification](notification.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-createqueue.html language=enus -->
## TOPIC 04572: SyncManager.CreateQueue

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-createqueue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-createqueue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.CreateQueue( name, sizeLimit, alreadyExists) Return Value Queue Purpose Creates or retrieves a Queue object with the name and settings you specify. Parameters name As String [In] Specifies a unique name for the Synchronization object. When the Synchronization object name begins wi

### SyncManager.CreateQueue

#### Syntax

[SyncManager](syncmanager.html).CreateQueue( name, sizeLimit, alreadyExists)

#### Return Value

[Queue](queue.html)

#### Purpose

Creates or retrieves a
 [Queue](queue.html)
 object with the name and settings you specify.

#### Parameters

name
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a unique name for the Synchronization object. When the Synchronization object name begins with an asterisk,
 *
 , such as
 *syncobjectname
 , processes can share the object.

When the Synchronization object name begins with a computer name, such as
 \\computername\syncobjectname
 , you can share the object among computers, but the object resides on the computer for which you specify a name.

When the Synchronization object name begins with an asterisk or computer name, you can use a
 32
 or
 64
 prefix to specify using 32- or 64-bit TestStand to host the out-of-process Synchronization object. For example, the name
 64*syncobj
 specifies a Synchronization object called
 *syncobj
 in the 64-bit TestStand host process, even when used from 32-bit TestStand. Use the prefix to share Synchronization objects between 32-bit TestStand and 64-bit TestStand in the same host process. If you do not use the prefix, 32-bit TestStand hosts out-of-process Synchronization objects in a 32-bit process, and 64-bit TestStand hosts out-of-process Synchronization objects in a 64-bit process.

sizeLimit
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the maximum number of items the queue can store. A value less than or equal to zero specifies that the queue does not have a maximum number of elements.

When the
 alreadyExists
 parameter returns
 True
 to indicate a queue already exists, TestStand ignores this value.

alreadyExists
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[Out] Returns
 True
 when the Synchronization object for which you specify a name already exists.

When the object already exists, this method returns the existing object rather than creating a new object.

#### See Also

[Queue](queue.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-createrendezvous.html language=enus -->
## TOPIC 04573: SyncManager.CreateRendezvous

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-createrendezvous.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-createrendezvous.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.CreateRendezvous( name, rendezvousCount, alreadyExists) Return Value Rendezvous Purpose Creates or retrieves a Rendezvous object with the name and settings you specify. Parameters name As String [In] Specifies a unique name for the Synchronization object. When the Synchronization

### SyncManager.CreateRendezvous

#### Syntax

[SyncManager](syncmanager.html).CreateRendezvous( name, rendezvousCount, alreadyExists)

#### Return Value

[Rendezvous](rendezvous.html)

#### Purpose

Creates or retrieves a
 [Rendezvous](rendezvous.html)
 object with the name and settings you specify.

#### Parameters

name
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a unique name for the Synchronization object. When the Synchronization object name begins with an asterisk,
 *
 , such as
 *syncobjectname
 , processes can share the object.

When the Synchronization object name begins with a computer name, such as
 \\computername\syncobjectname
 , you can share the object among computers, but the object resides on the computer for which you specify a name.

When the Synchronization object name begins with an asterisk or computer name, you can use a
 32
 or
 64
 prefix to specify using 32- or 64-bit TestStand to host the out-of-process Synchronization object. For example, the name
 64*syncobj
 specifies a Synchronization object called
 *syncobj
 in the 64-bit TestStand host process, even when used from 32-bit TestStand. Use the prefix to share Synchronization objects between 32-bit TestStand and 64-bit TestStand in the same host process. If you do not use the prefix, 32-bit TestStand hosts out-of-process Synchronization objects in a 32-bit process, and 64-bit TestStand hosts out-of-process Synchronization objects in a 64-bit process.

rendezvousCount
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the number of threads that must rendezvous before the Synchronization object unblocks those threads. This value must be greater than zero.

When the
 alreadyExists
 parameter returns
 True
 to indicate a rendezvous already exists, TestStand ignores this value.

alreadyExists
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[Out] Returns
 True
 when the Synchronization object for which you specify a name already exists.

When the object already exists, this method returns the existing object rather than creating a new object.

#### See Also

[Rendezvous](rendezvous.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-createsemaphore.html language=enus -->
## TOPIC 04574: SyncManager.CreateSemaphore

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-createsemaphore.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-createsemaphore.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.CreateSemaphore( name, initialCount, maxCount, alreadyExists) Return Value Semaphore Purpose Creates or retrieves a Semaphore object with the name and settings you specify. Parameters name As String [In] Specifies a unique name for the Synchronization object. When the Synchronizat

### SyncManager.CreateSemaphore

#### Syntax

[SyncManager](syncmanager.html).CreateSemaphore( name, initialCount, maxCount, alreadyExists)

#### Return Value

[Semaphore](semaphore.html)

#### Purpose

Creates or retrieves a
 [Semaphore](semaphore.html)
 object with the name and settings you specify.

#### Parameters

name
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a unique name for the Synchronization object. When the Synchronization object name begins with an asterisk,
 *
 , such as
 *syncobjectname
 , processes can share the object.

When the Synchronization object name begins with a computer name, such as
 \\computername\syncobjectname
 , you can share the object among computers, but the object resides on the computer for which you specify a name.

When the Synchronization object name begins with an asterisk or computer name, you can use a
 32
 or
 64
 prefix to specify using 32- or 64-bit TestStand to host the out-of-process Synchronization object. For example, the name
 64*syncobj
 specifies a Synchronization object called
 *syncobj
 in the 64-bit TestStand host process, even when used from 32-bit TestStand. Use the prefix to share Synchronization objects between 32-bit TestStand and 64-bit TestStand in the same host process. If you do not use the prefix, 32-bit TestStand hosts out-of-process Synchronization objects in a 32-bit process, and 64-bit TestStand hosts out-of-process Synchronization objects in a 64-bit process.

initialCount
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the initial value for the count. This value must be greater than or equal to 0.

When the
 alreadyExists
 parameter returns
 True
 to indicate a semaphore already exists, TestStand ignores this value.

maxCount
 As
 [Long](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the max count allowed for the semaphore. Release operations that result in a count greater than the max count return an error. Normally, you pass
 0x80000000
 as the value for this parameter.

When the
 alreadyExists
 parameter returns
 True
 to indicate a semaphore already exists, this value is ignored.

alreadyExists
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[Out] Returns
 True
 when the Synchronization object for which you specify a name already exists.

When the object already exists, this method returns the existing object rather than creating a new object.

#### See Also

[Semaphore](semaphore.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-endlogging.html language=enus -->
## TOPIC 04575: SyncManager.EndLogging

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-endlogging.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-endlogging.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.EndLogging Return Value Long Returns the number of unbalanced calls to the SyncManager.BeginLogging method. Purpose Balances a preceding call to the SyncManager.BeginLogging method. When all calls to SyncManager.BeginLogging are balanced, the value of the SyncManager.LoggingEnable

### SyncManager.EndLogging

#### Syntax

[SyncManager](syncmanager.html).EndLogging

#### Return Value

[Long](data-types-for-teststand-synchronization-serv.html)

Returns the number of unbalanced calls to the
 [SyncManager.BeginLogging](syncmanager-beginlogging.html)
 method.

#### Purpose

Balances a preceding call to the
 SyncManager.BeginLogging
 method. When all calls to
 SyncManager.BeginLogging
 are balanced, the value of the
 [SyncManager.LoggingEnabled](syncmanager-loggingenabled.html)
 property is
 False
 .

#### See Also

[SyncManager.BeginLogging](syncmanager-beginlogging.html)

[SyncManager.LoggingEnabled](syncmanager-loggingenabled.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-getbatch.html language=enus -->
## TOPIC 04576: SyncManager.GetBatch

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-getbatch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-getbatch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.GetBatch( name) Return Value Batch Purpose Returns a reference to the Synchronization object for which you specify a name or returns NULL when no such object exists. When a Synchronization object with the name you specify exists but is of the wrong type, this method returns an err

### SyncManager.GetBatch

#### Syntax

[SyncManager](syncmanager.html).GetBatch( name)

#### Return Value

[Batch](batch.html)

#### Purpose

Returns a reference to the Synchronization object for which you specify a name or returns
 NULL
 when no such object exists. When a Synchronization object with the name you specify exists but is of the wrong type, this method returns an error.

#### Parameters

name
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a unique name for the Synchronization object. When the Synchronization object name begins with an asterisk,
 *
 , such as
 *syncobjectname
 , processes can share the object.

When the Synchronization object name begins with a computer name, such as
 \\computername\syncobjectname
 , you can share the object among computers, but the object resides on the computer for which you specify a name.

When the Synchronization object name begins with an asterisk or computer name, you can use a
 32
 or
 64
 prefix to specify using 32- or 64-bit TestStand to host the out-of-process Synchronization object. For example, the name
 64*syncobj
 specifies a Synchronization object called
 *syncobj
 in the 64-bit TestStand host process, even when used from 32-bit TestStand. Use the prefix to share Synchronization objects between 32-bit TestStand and 64-bit TestStand in the same host process. If you do not use the prefix, 32-bit TestStand hosts out-of-process Synchronization objects in a 32-bit process, and 64-bit TestStand hosts out-of-process Synchronization objects in a 64-bit process.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-getlockmutexthreadiswaitingfor.html language=enus -->
## TOPIC 04577: SyncManager.GetLockMutexThreadIsWaitingFor

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-getlockmutexthreadiswaitingfor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-getlockmutexthreadiswaitingfor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.GetLockMutexThreadIsWaitingFor( threadId, mutexName, mutexSyncMgr) Purpose This method is obsolete. Remarks Do not call this method. This method is for internal use only and is used to implement deadlock detection for mutex Synchronization objects. Parameters threadId As String [I

### SyncManager.GetLockMutexThreadIsWaitingFor

#### Syntax

[SyncManager](syncmanager.html).GetLockMutexThreadIsWaitingFor( threadId, mutexName, mutexSyncMgr)

#### Purpose

Note

#### Remarks

Do not call this method. This method is for internal use only and is used to implement deadlock detection for mutex Synchronization objects.

#### Parameters

threadId
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a globally unique thread ID (GUID) for the thread that performs the operation. When you call this method from a TestStand execution, specify the value of the
 
 [Thread.UniqueThreadId](../tsapiref/thread-uniquethreadid.html)
 property for this parameter. Because the TestStand Synchronization Manager permits sharing of mutexes between computers, you must use an ID more unique than just the current operating system thread ID of the current thread on the current computer. When you plan to use mutexes across computers, use a GUID or some other way of creating a thread ID that is unique across all computers. The
 Thread.UniqueThreadId
 property is a GUID.

mutexName
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[Out] Returns the unique name for the Synchronization object.

mutexSyncMgr
 As
 [SyncManager](syncmanager.html)

[Out] Returns the TestStand Synchronization Manager associated with the mutex.

#### See Also

[Thread.UniqueThreadId](../tsapiref/thread-uniquethreadid.html)

Parent topic:

Obsolete SyncManager Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-getmutex.html language=enus -->
## TOPIC 04578: SyncManager.GetMutex

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-getmutex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-getmutex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.GetMutex( name) Return Value Mutex Purpose Returns a reference to the Synchronization object for which you specify a name or returns NULL when no such object exists. When a Synchronization object with the name you specify exists but is of the wrong type, this method returns an err

### SyncManager.GetMutex

#### Syntax

[SyncManager](syncmanager.html).GetMutex( name)

#### Return Value

[Mutex](mutex.html)

#### Purpose

Returns a reference to the Synchronization object for which you specify a name or returns
 NULL
 when no such object exists. When a Synchronization object with the name you specify exists but is of the wrong type, this method returns an error.

#### Parameters

name
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a unique name for the Synchronization object. When the Synchronization object name begins with an asterisk,
 *
 , such as
 *syncobjectname
 , processes can share the object.

When the Synchronization object name begins with a computer name, such as
 \\computername\syncobjectname
 , you can share the object among computers, but the object resides on the computer for which you specify a name.

When the Synchronization object name begins with an asterisk or computer name, you can use a
 32
 or
 64
 prefix to specify using 32- or 64-bit TestStand to host the out-of-process Synchronization object. For example, the name
 64*syncobj
 specifies a Synchronization object called
 *syncobj
 in the 64-bit TestStand host process, even when used from 32-bit TestStand. Use the prefix to share Synchronization objects between 32-bit TestStand and 64-bit TestStand in the same host process. If you do not use the prefix, 32-bit TestStand hosts out-of-process Synchronization objects in a 32-bit process, and 64-bit TestStand hosts out-of-process Synchronization objects in a 64-bit process.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-getmutexownerinfo.html language=enus -->
## TOPIC 04579: SyncManager.GetMutexOwnerInfo

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-getmutexownerinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-getmutexownerinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.GetMutexOwnerInfo( mutexName, threadId, threadDisplayName, homeSyncMgr) Purpose This method is obsolete. Remarks Do not call this method. This method is for internal use only to implement deadlock detection for mutex Synchronization objects. Parameters mutexName As String [In] Spe

### SyncManager.GetMutexOwnerInfo

#### Syntax

[SyncManager](syncmanager.html).GetMutexOwnerInfo( mutexName, threadId, threadDisplayName, homeSyncMgr)

#### Purpose

Note

#### Remarks

Do not call this method. This method is for internal use only to implement deadlock detection for mutex Synchronization objects.

#### Parameters

mutexName
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a unique name for the Synchronization object. When the Synchronization object name begins with an asterisk,
 *
 , such as
 *syncobjectname
 , processes can share the object.

When the Synchronization object name begins with a computer name, such as
 \\computername\syncobjectname
 , you can share the object among computers, but the object resides on the computer for which you specify a name.

When the Synchronization object name begins with an asterisk or computer name, you can use a
 32
 or
 64
 prefix to specify using 32- or 64-bit TestStand to host the out-of-process Synchronization object. For example, the name
 64*syncobj
 specifies a Synchronization object called
 *syncobj
 in the 64-bit TestStand host process, even when used from 32-bit TestStand. Use the prefix to share Synchronization objects between 32-bit TestStand and 64-bit TestStand in the same host process. If you do not use the prefix, 32-bit TestStand hosts out-of-process Synchronization objects in a 32-bit process, and 64-bit TestStand hosts out-of-process Synchronization objects in a 64-bit process.

threadId
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[Out] Returns a globally unique thread ID (GUID) for the thread performing the operation. When you call this method from a TestStand execution, specify the value of the
 
 [Thread.UniqueThreadId](../tsapiref/thread-uniquethreadid.html)
 property for this parameter. Because the TestStand Synchronization Manager permits sharing of mutexes between computers, you must use an ID more unique than just the current operating system thread ID of the current thread on the current computer. When you plan to use mutexes across computers, use a GUID or some other way of creating a thread ID that is unique across all computers. The
 Thread.UniqueThreadId
 property is a GUID.

threadDisplayName
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[Out] Returns a display name to identify the current thread. This name is used to report a deadlock condition, when one occurs, that involves this thread.

homeSyncMgr
 As
 [SyncManager](syncmanager.html)

[Out] Returns the local version of the TestStand Synchronization Manager. When you use the
 
 [TestStand Engine](../tsapiref/engine.html)
 , National Instruments recommends that you call the
 
 [Engine.GetSyncManager](../tsapiref/engine-getsyncmanager.html)
 method on a local version of the TestStand Engine to obtain the value to pass for this parameter. This parameter is used for deadlock detection purposes.

Notice

NULL

#### See Also

[Engine.GetSyncManager](../tsapiref/engine-getsyncmanager.html)

[Thread.UniqueThreadId](../tsapiref/thread-uniquethreadid.html)

Parent topic:

Obsolete SyncManager Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-getnotification.html language=enus -->
## TOPIC 04580: SyncManager.GetNotification

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-getnotification.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-getnotification.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.GetNotification( name) Return Value Notification Purpose Returns a reference to the Synchronization object for which you specify a name or returns NULL when no such object exists. When a Synchronization object with the name you specify exists but is of the wrong type, this method

### SyncManager.GetNotification

#### Syntax

[SyncManager](syncmanager.html).GetNotification( name)

#### Return Value

[Notification](notification.html)

#### Purpose

Returns a reference to the Synchronization object for which you specify a name or returns
 NULL
 when no such object exists. When a Synchronization object with the name you specify exists but is of the wrong type, this method returns an error.

#### Parameters

name
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a unique name for the Synchronization object. When the Synchronization object name begins with an asterisk,
 *
 , such as
 *syncobjectname
 , processes can share the object.

When the Synchronization object name begins with a computer name, such as
 \\computername\syncobjectname
 , you can share the object among computers, but the object resides on the computer for which you specify a name.

When the Synchronization object name begins with an asterisk or computer name, you can use a
 32
 or
 64
 prefix to specify using 32- or 64-bit TestStand to host the out-of-process Synchronization object. For example, the name
 64*syncobj
 specifies a Synchronization object called
 *syncobj
 in the 64-bit TestStand host process, even when used from 32-bit TestStand. Use the prefix to share Synchronization objects between 32-bit TestStand and 64-bit TestStand in the same host process. If you do not use the prefix, 32-bit TestStand hosts out-of-process Synchronization objects in a 32-bit process, and 64-bit TestStand hosts out-of-process Synchronization objects in a 64-bit process.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-getqueue.html language=enus -->
## TOPIC 04581: SyncManager.GetQueue

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-getqueue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-getqueue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.GetQueue( name) Return Value Queue Purpose Returns a reference to the Synchronization object for which you specify a name or returns NULL when no such object exists. When a Synchronization object with the name you specify exists but is of the wrong type, this method returns an err

### SyncManager.GetQueue

#### Syntax

[SyncManager](syncmanager.html).GetQueue( name)

#### Return Value

[Queue](queue.html)

#### Purpose

Returns a reference to the Synchronization object for which you specify a name or returns
 NULL
 when no such object exists. When a Synchronization object with the name you specify exists but is of the wrong type, this method returns an error.

#### Parameters

name
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a unique name for the Synchronization object. When the Synchronization object name begins with an asterisk,
 *
 , such as
 *syncobjectname
 , processes can share the object.

When the Synchronization object name begins with a computer name, such as
 \\computername\syncobjectname
 , you can share the object among computers, but the object resides on the computer for which you specify a name.

When the Synchronization object name begins with an asterisk or computer name, you can use a
 32
 or
 64
 prefix to specify using 32- or 64-bit TestStand to host the out-of-process Synchronization object. For example, the name
 64*syncobj
 specifies a Synchronization object called
 *syncobj
 in the 64-bit TestStand host process, even when used from 32-bit TestStand. Use the prefix to share Synchronization objects between 32-bit TestStand and 64-bit TestStand in the same host process. If you do not use the prefix, 32-bit TestStand hosts out-of-process Synchronization objects in a 32-bit process, and 64-bit TestStand hosts out-of-process Synchronization objects in a 64-bit process.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-getrendezvous.html language=enus -->
## TOPIC 04582: SyncManager.GetRendezvous

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-getrendezvous.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-getrendezvous.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.GetRendezvous( name) Return Value Rendezvous Purpose Returns a reference to the Synchronization object for which you specify a name or returns NULL when no such object exists. When a Synchronization object with the name you specify exists but is of the wrong type, this method retu

### SyncManager.GetRendezvous

#### Syntax

[SyncManager](syncmanager.html).GetRendezvous( name)

#### Return Value

[Rendezvous](rendezvous.html)

#### Purpose

Returns a reference to the Synchronization object for which you specify a name or returns
 NULL
 when no such object exists. When a Synchronization object with the name you specify exists but is of the wrong type, this method returns an error.

#### Parameters

name
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a unique name for the Synchronization object. When the Synchronization object name begins with an asterisk,
 *
 , such as
 *syncobjectname
 , the object can be shared between processes.

When the Synchronization object name begins with a computer name, such as
 \\computername\syncobjectname
 , the object can be shared among computers and resides on the computer for which you specify a name.

When the Synchronization object name begins with an asterisk or computer name, you can use a
 32
 or
 64
 prefix to specify using 32- or 64-bit TestStand to host the out-of-process Synchronization object. For example, the name
 64*syncobj
 specifies a Synchronization object called
 *syncobj
 in the 64-bit TestStand host process, even when used from 32-bit TestStand. Use the prefix to share Synchronization objects between 32-bit TestStand and 64-bit TestStand in the same host process. If you do not use the prefix, 32-bit TestStand hosts out-of-process Synchronization objects in a 32-bit process, and 64-bit TestStand hosts out-of-process Synchronization objects in a 64-bit process.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-getsemaphore.html language=enus -->
## TOPIC 04583: SyncManager.GetSemaphore

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-getsemaphore.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-getsemaphore.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.GetSemaphore( name) Return Value Semaphore Purpose Returns a reference to the Synchronization object for which you specify a name or returns NULL when no such object exists. When a Synchronization object with the name you specify exists but is of the wrong type, this method return

### SyncManager.GetSemaphore

#### Syntax

[SyncManager](syncmanager.html).GetSemaphore( name)

#### Return Value

[Semaphore](semaphore.html)

#### Purpose

Returns a reference to the Synchronization object for which you specify a name or returns
 NULL
 when no such object exists. When a Synchronization object with the name you specify exists but is of the wrong type, this method returns an error.

#### Parameters

name
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a unique name for the Synchronization object. When the Synchronization object name begins with an asterisk,
 *
 , such as
 *syncobjectname
 , processes can share the object.

When the Synchronization object name begins with a computer name, such as
 \\computername\syncobjectname
 , you can share the object among computers, but the object resides on the computer for which you specify a name.

When the Synchronization object name begins with an asterisk or computer name, you can use a
 32
 or
 64
 prefix to specify using 32- or 64-bit TestStand to host the out-of-process Synchronization object. For example, the name
 64*syncobj
 specifies a Synchronization object called
 *syncobj
 in the 64-bit TestStand host process, even when used from 32-bit TestStand. Use the prefix to share Synchronization objects between 32-bit TestStand and 64-bit TestStand in the same host process. If you do not use the prefix, 32-bit TestStand hosts out-of-process Synchronization objects in a 32-bit process, and 64-bit TestStand hosts out-of-process Synchronization objects in a 64-bit process.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-getsyncobject.html language=enus -->
## TOPIC 04584: SyncManager.GetSyncObject

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-getsyncobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-getsyncobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.GetSyncObject( name, syncObjType) Return Value IUnknown Purpose Returns a reference to the Synchronization object for which you specify a name or returns NULL when no such object exists. When a Synchronization object with the name you specify exists but is of the wrong type, this

### SyncManager.GetSyncObject

#### Syntax

[SyncManager](syncmanager.html).GetSyncObject( name, syncObjType)

#### Return Value

[IUnknown](data-types-for-teststand-synchronization-serv.html)

#### Purpose

Returns a reference to the Synchronization object for which you specify a name or returns
 NULL
 when no such object exists. When a Synchronization object with the name you specify exists but is of the wrong type, this method returns an error.

#### Parameters

name
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a unique name for the Synchronization object. When the Synchronization object name begins with an asterisk,
 *
 , such as
 *syncobjectname
 , processes can share the object.

When the Synchronization object name begins with a computer name, such as
 \\computername\syncobjectname
 , you can share the object among computers but the object resides on the computer for which you specify a name.

When the Synchronization object name begins with an asterisk or computer name, you can use a
 32
 or
 64
 prefix to specify using 32- or 64-bit TestStand to host the out-of-process Synchronization object. For example, the name
 64*syncobj
 specifies a Synchronization object called
 *syncobj
 in the 64-bit TestStand host process, even when used from 32-bit TestStand. Use the prefix to share Synchronization objects between 32-bit TestStand and 64-bit TestStand in the same host process. If you do not use the prefix, 32-bit TestStand hosts out-of-process Synchronization objects in a 32-bit process, and 64-bit TestStand hosts out-of-process Synchronization objects in a 64-bit process.

syncObjType
 As
 [SyncObjTypes](syncobjtypes.html)

[In] Specifies the type of Synchronization object.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-isalive.html language=enus -->
## TOPIC 04585: SyncManager.IsAlive

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-isalive.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-isalive.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.IsAlive Return Value Boolean Purpose Pings the TestStand Synchronization Manager COM server to ensure that the process is active. When the process is active, this method returns True . When the process is not active, a COM error occurs.

### SyncManager.IsAlive

#### Syntax

[SyncManager](syncmanager.html).IsAlive

#### Return Value

[Boolean](data-types-for-teststand-synchronization-serv.html)

#### Purpose

Pings the TestStand Synchronization Manager COM server to ensure that the process is active. When the process is active, this method returns
 True
 . When the process is not active, a COM error occurs.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-logaction.html language=enus -->
## TOPIC 04586: SyncManager.LogAction

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-logaction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-logaction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.LogAction( synchronizationMechanism, sequenceContextObj, threadId, threadDisplayName, name, syncState, operation, timeout, postMessage, reserved) Return Value Object Purpose When the SyncManager.LoggingEnabled property is True , this method posts or returns an OutputMessage with a

### SyncManager.LogAction

#### Syntax

[SyncManager](syncmanager.html).LogAction( synchronizationMechanism, sequenceContextObj, threadId, threadDisplayName, name, syncState, operation, timeout, postMessage, reserved)

#### Return Value

[Object](data-types-for-teststand-synchronization-serv.html)

#### Purpose

When the
 [SyncManager.LoggingEnabled](syncmanager-loggingenabled.html)
 property is
 True
 , this method posts or returns an
 
 [OutputMessage](../tsapiref/outputmessage.html)
 with a category of
 Resource Usage
 that records the specified action. When the
 [SyncManager.LoggingEnabled](syncmanager-loggingenabled.html)
 property is
 False
 , this method does nothing and returns
 NULL
 .

Note

Use Auto Scheduled Resource

#### Parameters

synchronizationMechanism
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the synchronization mechanism that generated the action to log. When the mechanism is a TestStand synchronization mechanism, pass the appropriate
 [SynchronizationMechanism](synchronizationmechanism.html)
 constant.

sequenceContextObj
 As
 [Object](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the
 
 [SequenceContext](../tsapiref/sequencecontext.html)
 object that identifies the step that performs the resource action to log. This parameter might be
 NULL
 when the synchronization state is
 [SyncState_Completed](syncstates.html)
 .

threadId
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the TestStand thread ID of the thread that performs the resource action to log. This parameter might be an empty string when the synchronization state is
 SyncState_Completed
 .

threadDisplayName
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the display name of the TestStand thread that performs the resource action to log. This parameter might be an empty string when the synchronization state is
 SyncState_Completed
 .

name
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the name of the resource to which the action applies.

syncState
 As
 [SyncStates](syncstates.html)

[In] Specifies the type of synchronization state to log.

operation
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies the synchronization operation that generated the action to log.

timeout
 As
 [Double](data-types-for-teststand-synchronization-serv.html)

[In] When the synchronization state is
 [SyncState_Blocked](syncstates.html)
 , pass the timeout period for the wait or pass
 -1
 when no timeout exists. For other synchronization state types, pass
 0
 .

postMessage
 As
 [Boolean](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 True
 to force this method to post the OutputMessage it creates before it returns. Pass
 False
 when you want to add subproperties to the OutputMessage before posting it. Posting the OutputMessage after you add subproperties ensures that the additional properties are added before the OutputMessage is received.

reserved
 As
 [IUnknown](data-types-for-teststand-synchronization-serv.html)

[In] Pass
 NULL
 to this reserved parameter.

#### See Also

[OutputMessage](../tsapiref/outputmessage.html)

[SequenceContext](../tsapiref/sequencecontext.html)

[SynchronizationMechanism](synchronizationmechanism.html)

[SyncManager.LoggingEnabled](syncmanager-loggingenabled.html)

[SyncStates](syncstates.html)

[Use Auto Scheduled Resource steps](../tsref/use-auto-scheduled-resource-step.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-loggingenabled.html language=enus -->
## TOPIC 04587: SyncManager.LoggingEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-loggingenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-loggingenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.LoggingEnabled Data Type Boolean Purpose Returns a value that indicates whether calls to the SyncManager.LogAction method generate OutputMessages . See Also OutputMessage SyncManager.LogAction

### SyncManager.LoggingEnabled

#### Syntax

[SyncManager](syncmanager.html).LoggingEnabled

#### Data Type

[Boolean](data-types-for-teststand-synchronization-serv.html)

#### Purpose

Returns a value that indicates whether calls to the
 [SyncManager.LogAction](syncmanager-logaction.html)
 method generate
 
 [OutputMessages](../tsapiref/outputmessage.html)
 .

#### See Also

[OutputMessage](../tsapiref/outputmessage.html)

[SyncManager.LogAction](syncmanager-logaction.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-loggingoutputmessagecategoryname.html language=enus -->
## TOPIC 04588: SyncManager.LoggingOutputMessageCategoryName

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-loggingoutputmessagecategoryname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-loggingoutputmessagecategoryname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.LoggingOutputMessageCategoryName Data Type String Purpose Returns the localized category name the SyncManager.LogAction method assigns to the OutputMessage it creates. You can use this category name to determine whether the Synchronization Manager created a particular OutputMessag

### SyncManager.LoggingOutputMessageCategoryName

#### Syntax

[SyncManager](syncmanager.html).LoggingOutputMessageCategoryName

#### Data Type

[String](data-types-for-teststand-synchronization-serv.html)

#### Purpose

Returns the localized category name the
 [SyncManager.LogAction](syncmanager-logaction.html)
 method assigns to the
 
 [OutputMessage](../tsapiref/outputmessage.html)
 it creates. You can use this category name to determine whether the Synchronization Manager created a particular OutputMessage.

#### See Also

[OutputMessage](../tsapiref/outputmessage.html)

[SyncManager.LogAction](syncmanager-logaction.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-machineid.html language=enus -->
## TOPIC 04589: SyncManager.MachineID

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-machineid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-machineid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.MachineID Data Type String Purpose This property is obsolete. Remarks Do not call this property. This property is for internal use only to implement deadlock detection for mutex Synchronization objects.

### SyncManager.MachineID

#### Syntax

[SyncManager](syncmanager.html).MachineID

#### Data Type

[String](data-types-for-teststand-synchronization-serv.html)

#### Purpose

Note

#### Remarks

Do not call this property. This property is for internal use only to implement deadlock detection for mutex Synchronization objects.

Parent topic:

Obsolete SyncManager Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-processid.html language=enus -->
## TOPIC 04590: SyncManager.ProcessID

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-processid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-processid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.ProcessID Data Type Long Purpose This property is obsolete. Remarks Do not call this property. This property is for internal use only to implement deadlock detection for mutex Synchronization objects.

### SyncManager.ProcessID

#### Syntax

[SyncManager](syncmanager.html).ProcessID

#### Data Type

[Long](data-types-for-teststand-synchronization-serv.html)

#### Purpose

Note

#### Remarks

Do not call this property. This property is for internal use only to implement deadlock detection for mutex Synchronization objects.

Parent topic:

Obsolete SyncManager Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-recordthreadnolongerwaitingforloc.html language=enus -->
## TOPIC 04591: SyncManager.RecordThreadNolongerWaitingForLockMutex

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-recordthreadnolongerwaitingforloc.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-recordthreadnolongerwaitingforloc.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.RecordThreadNolongerWaitingForLockMutex( threadId) Purpose This method is obsolete. Remarks Do not call this method. This method is for internal use only to implement deadlock detection for mutex Synchronization objects. Parameters threadId As String [In] Specifies a globally uniq

### SyncManager.RecordThreadNolongerWaitingForLockMutex

#### Syntax

[SyncManager](syncmanager.html).RecordThreadNolongerWaitingForLockMutex( threadId)

#### Purpose

Note

#### Remarks

Do not call this method. This method is for internal use only to implement deadlock detection for mutex Synchronization objects.

#### Parameters

threadId
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a globally unique thread ID (GUID) for the thread performing the operation. When you call method from a TestStand execution, specify the value of the
 
 [Thread.UniqueThreadId](../tsapiref/thread-uniquethreadid.html)
 property for this parameter. Because the TestStand Synchronization Manager permits sharing of mutexes between computers, you must use an ID more unique than just the current operating system thread ID of the current thread on the current computer. When you plan to use mutexes across computers, use a GUID or some other way of creating a thread ID that is unique across all computers. The
 Thread.UniqueThreadId
 property is a GUID.

#### See Also

[Thread.UniqueThreadId](../tsapiref/thread-uniquethreadid.html)

Parent topic:

Obsolete SyncManager Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-recordthreadwaitingforlockmutex.html language=enus -->
## TOPIC 04592: SyncManager.RecordThreadWaitingForLockMutex

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-recordthreadwaitingforlockmutex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-recordthreadwaitingforlockmutex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.RecordThreadWaitingForLockMutex( threadId, threadDisplayName, mutexName, mutexSyncMgr) Purpose This method is obsolete. Remarks Do not call this method. This method is for internal use only to implement deadlock detection for mutex Synchronization objects. Parameters threadId As S

### SyncManager.RecordThreadWaitingForLockMutex

#### Syntax

[SyncManager](syncmanager.html).RecordThreadWaitingForLockMutex( threadId, threadDisplayName, mutexName, mutexSyncMgr)

#### Purpose

Note

#### Remarks

Do not call this method. This method is for internal use only to implement deadlock detection for mutex Synchronization objects.

#### Parameters

threadId
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a globally unique thread ID (GUID) for the thread performing the operation. When you call this method from a TestStand execution, specify the value of the
 
 [Thread.UniqueThreadId](../tsapiref/thread-uniquethreadid.html)
 property for this parameter. Because the TestStand Synchronization Manager permits sharing of mutexes between computers, you must use an ID more unique than just the current operating system thread ID of the current thread on the current computer. When you plan to use mutexes across computers, use a GUID or some other way of creating a thread ID that is unique across all computers. The
 Thread.UniqueThreadId
 property is a GUID.

threadDisplayName
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a display name to identify the current thread. This name is used to report any deadlock conditions that involve this thread.

mutexName
 As
 [String](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a unique name for the Synchronization object. When the Synchronization object name begins with an asterisk,
 *
 , such as
 *syncobjectname
 , processes can share the object.

When the Synchronization object name begins with a computer name, such as
 \\computername\syncobjectname
 , you can share the object among computers, but the object resides on the computer for which you specify a name.

When the Synchronization object name begins with an asterisk or computer name, you can use a
 32
 or
 64
 prefix to specify using 32- or 64-bit TestStand to host the out-of-process Synchronization object. For example, the name
 64*syncobj
 specifies a Synchronization object called
 *syncobj
 in the 64-bit TestStand host process, even when used from 32-bit TestStand. Use the prefix to share Synchronization objects between 32-bit TestStand and 64-bit TestStand in the same host process. If you do not use the prefix, 32-bit TestStand hosts out-of-process Synchronization objects in a 32-bit process, and 64-bit TestStand hosts out-of-process Synchronization objects in a 64-bit process.

mutexSyncMgr
 As
 [SyncManager](syncmanager.html)

[In] Specifies the TestStand Synchronization Manager associated with the mutex name.

#### See Also

[Thread.UniqueThreadId](../tsapiref/thread-uniquethreadid.html)

Parent topic:

Obsolete SyncManager Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager-releaseserverondestruct.html language=enus -->
## TOPIC 04593: SyncManager.ReleaseServerOnDestruct

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager-releaseserverondestruct.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager-releaseserverondestruct.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SyncManager.ReleaseServerOnDestruct( serverToRelease) Purpose This method is obsolete. Remarks Do not call this method. This method is only for internal use. Parameters serverToRelease As IUnknown [In] Specifies a reference to an object the TestStand Synchronization Manager releases when dest

### SyncManager.ReleaseServerOnDestruct

#### Syntax

[SyncManager](syncmanager.html).ReleaseServerOnDestruct( serverToRelease)

#### Purpose

Note

#### Remarks

Do not call this method. This method is only for internal use.

#### Parameters

serverToRelease
 As
 [IUnknown](data-types-for-teststand-synchronization-serv.html)

[In] Specifies a reference to an object the TestStand Synchronization Manager releases when destroyed.

Parent topic:

Obsolete SyncManager Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncmanager.html language=enus -->
## TOPIC 04594: SyncManager

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncmanager.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncmanager.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The SyncManager class is the main class for all Synchronization objects . This class helps manage the creation and sharing of the different Synchronization objects between threads. You must create all Synchronization objects using this class. To obtain the appropriate instance of the TestStand Synch

### SyncManager

The
 SyncManager
 class is the main class for all
 [Synchronization objects](../tsref/synchronization-step-types.html)
 . This class helps manage the creation and sharing of the different Synchronization objects between threads. You must create all Synchronization objects using this class. To obtain the appropriate instance of the TestStand Synchronization Manager to use for any particular Synchronization object, call the
 
 [Engine.GetSyncManager](../tsapiref/engine-getsyncmanager.html)
 method. The
 Engine.GetSyncManager
 method returns the TestStand Synchronization Manager for the appropriate computer or process based on the name of the Synchronization object.

#### Properties

| LoggingEnabled (Read Only) |
| --- |
| LoggingOutputMessageCategoryName (Read Only) |

#### Methods

| BeginLogging |
| --- |
| CreateBatch |
| CreateMutex |
| CreateNotification |
| CreateQueue |
| CreateRendezvous |
| CreateSemaphore |
| EndLogging |
| GetBatch |
| GetMutex |
| GetNotification |
| GetQueue |
| GetRendezvous |
| GetSemaphore |
| GetSyncObject |
| IsAlive |
| LogAction |

#### See Also

[Engine.GetSyncManager](../tsapiref/engine-getsyncmanager.html)

[Synchronization Step Types](../tsref/synchronization-step-types.html)

Parent topic:

TestStand Synchronization Server

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncobjtypes.html language=enus -->
## TOPIC 04595: SyncObjTypes

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncobjtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncobjtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the syncObjectType parameter of the SyncManager.GetSyncObject method. The syncObjectType parameter specifies the type of Synchronization object to return. SyncObjType_Batch –(Value: 6) Specifies a Batch Synchronization object. SyncObjType_Mutex –(Value: 2) Specifies a

### SyncObjTypes

Use these constants to specify the
 syncObjectType
 parameter of the
 [SyncManager.GetSyncObject](syncmanager-getsyncobject.html)
 method. The
 syncObjectType
 parameter specifies the type of Synchronization object to return.

- SyncObjType_Batch 
 –(Value: 6) Specifies a Batch Synchronization object.
- SyncObjType_Mutex 
 –(Value: 2) Specifies a Mutex Synchronization object.
- SyncObjType_NotASyncObj 
 –(Value: 0) Not a valid Synchronization object.
- SyncObjType_Notification 
 –(Value: 5) Specifies a Notification Synchronization object.
- SyncObjType_Queue 
 –(Value: 4) Specifies a Queue Synchronization object.
- SyncObjType_Rendezvous 
 –Value: 3) Specifies a Rendezvous Synchronization object.
- SyncObjType_Semaphore 
 –(Value: 1) Specifies a Semaphore Synchronization object.

#### See Also

[SyncManager.GetSyncObject](syncmanager-getsyncobject.html)

Parent topic:

API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/syncstates.html language=enus -->
## TOPIC 04596: SyncStates

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/syncstates.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/syncstates.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the type of synchronization state the SyncManager.LogAction method records in the OutputMessageSubProperty_SynchronizationState property object subproperty of the OutputMessage it creates. SyncState_Aborted –(Value: 3) Indicates that a thread has abandoned an attempt t

### SyncStates

Use these constants to specify the type of synchronization state the
 [SyncManager.LogAction](syncmanager-logaction.html)
 method records in the
 [OutputMessageSubProperty_SynchronizationState](resourceusageoutputmessagesubproperties.html)
 property object subproperty of the
 
 [OutputMessage](../tsapiref/outputmessage.html)
 it creates.

- SyncState_Aborted 
 –(Value: 3) Indicates that a thread has abandoned an attempt to perform a synchronization operation. For example, for a lock, this value can indicate that a thread terminated or aborted while waiting to acquire the lock.
- SyncState_Blocked 
 –(Value: 1) Indicates that a thread has begun waiting in the process of performing a synchronization operation. For example, for a lock, this value indicates that a thread has blocked trying to acquire the lock.
- SyncState_Completed 
 –(Value: 5) Indicates that a thread has completed a synchronization operation. For example, for a lock, this value indicates that a thread has released a resource it had previously acquired.
- SyncState_InUse 
 –(Value: 2) Indicates that a thread has obtained access to a synchronization object. For example, for a lock, this value indicates that a thread has acquired the lock.
- SyncState_None 
 –(Value: 0) Not a valid synchronization state.
- SyncState_TimedOut 
 –(Value: 4) Indicates that the timeout period you specified expired while waiting to access a synchronization object. For example, for a lock, this value indicates that the timeout period expired while a thread was waiting to acquire the lock.

#### See Also

[OutputMessage](../tsapiref/outputmessage.html)

[ResourceUsageOutputMessageSubProperties](resourceusageoutputmessagesubproperties.html)

[SyncManager.LogAction](syncmanager-logaction.html)

Parent topic:

API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/teststand-synchronization-server.html language=enus -->
## TOPIC 04597: TestStand Synchronization Server

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/teststand-synchronization-server.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/teststand-synchronization-server.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Object and Description AutoReleaser Use the AutoReleaser class to hold a reference with a lifetime that corresponds to a semaphore Acquire operation or a mutex Lock operation. When you release the final reference to the AutoReleaser object, one of the following operations complete: When the AutoRele

### TestStand Synchronization Server

| Object and Description |
| --- |
| AutoReleaser |
| Use the AutoReleaser class to hold a reference with a lifetime that corresponds to a semaphore Acquire operation or a mutex Lock operation. When you release the final reference to the AutoReleaser object, one of the following operations complete: When the AutoReleaser is from the Semaphore.AcquireSemaphoreWithAutoReleaser method, a Release operation on the semaphore completes. When the AutoReleaser is from the Mutex.LockMutex method, an Unlock operation on the mutex completes. |
| Batch |
| This class implements the Batch synchronization primitive. Use these properties and methods to implement the Batch Specification and Batch Synchronization step types. |
| Mutex |
| This class implements the Lock synchronization primitive. Use these properties and methods to implement the Lock step type. |
| Notification |
| This class implements the Notification synchronization primitive. Use these properties and methods to implement the Notification step type. |
| Queue |
| This class implements the Queue synchronization primitive. Use these properties and methods to implement the Queue step type. |
| Rendezvous |
| This class implements the Rendezvous synchronization primitive. Use these properties and methods to implement the Rendezvous step type. |
| Semaphore |
| This class implements the Semaphore synchronization primitive. Use these properties and methods to implement the Semaphore step type. |
| SyncManager |
| The SyncManager class is the main class for all Synchronization objects . This class helps manage the creation and sharing of the different Synchronization objects between threads. You must create all Synchronization objects using this class. To obtain the appropriate instance of the TestStand Synchronization Manager to use for any particular Synchronization object, call the Engine.GetSyncManager method. The Engine.GetSyncManager method returns the TestStand Synchronization Manager for the appropriate computer or process based on the name of the Synchronization object. |

Parent topic:

NI TestStand Synchronization Server API Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tssyncserver/waitresult.html language=enus -->
## TOPIC 04598: WaitResult

- bundle_id: `teststand-api-reference`
- source_path: `tssyncserver/waitresult.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tssyncserver/waitresult.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to determine the value of the waitRes parameter of the following methods: Semaphore.AcquireSemaphore Semaphore.AcquireSemaphoreWithAutoReleaser Mutex.LockMutex Mutex.LockMutexGroup Rendezvous.Rendezvous Queue.Enqueue Queue.Dequeue Queue.DequeueMultiple Notification.Wait Notificat

### WaitResult

Use these constants to determine the value of the
 waitRes
 parameter of the following methods:

[Semaphore.AcquireSemaphore](semaphore-acquiresemaphore.html)

[Semaphore.AcquireSemaphoreWithAutoReleaser](semaphore-acquiresemaphorewithautoreleaser.html)

[Mutex.LockMutex](mutex-lockmutex.html)

[Mutex.LockMutexGroup](mutex-lockmutexgroup.html)

[Rendezvous.Rendezvous](rendezvous-rendezvous.html)

[Queue.Enqueue](queue-enqueue.html)

[Queue.Dequeue](queue-dequeue.html)

[Queue.DequeueMultiple](queue-dequeuemultiple.html)

[Notification.Wait](notification-wait.html)

[Notification.WaitMultiple](notification-waitmultiple.html)

[Batch.EnterSynchronizedSection](batch-entersynchronizedsection.html)

[Batch.ExitSynchronizedSection](batch-exitsynchronizedsection.html)

[Batch.ExitAllSynchronizedSectionsInCurrentSequence](batch-exitallsynchronizedsectionsincurrentseq.html)

- WaitResult_DeadlockDetected 
 –(Value: 3) A deadlock condition was detected.
 Note 
 This enumeration element applies only to the
 [Mutex.LockMutex](mutex-lockmutex.html)
 method.
- WaitResult_Success 
 –(Value: 0) The operation was successful.
- WaitResult_TerminateOrAbortOccurred 
 –(Value: 2) The execution was terminated or aborted.
- WaitResult_TimeoutOccurred 
 –(Value: 1) The specified timeout occurred before the operation completed.

Parent topic:

API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/adapterlistconnection.html language=enus -->
## TOPIC 04599: AdapterListConnection

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/adapterlistconnection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/adapterlistconnection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a connection from an Application Manager control to a control that displays the list of adapters. Use the connected control to select an adapter to which to set the Engine.DefaultAdapter property. This class currently contains no properties or methods. Properties or methods might be added

### AdapterListConnection

Represents a connection from an
 [Application Manager](applicationmgr.html)
 control to a control that displays the list of adapters. Use the connected control to select an adapter to which to set the
 
 [Engine.DefaultAdapter](../tsapiref/engine-defaultadapter.html)
 property.

Note

#### See Also

[Application Manager](applicationmgr.html)

[AdapterListConnections](adapterlistconnections.html)

[Engine.DefaultAdapter](../tsapiref/engine-defaultadapter.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/adapterlistconnections-add.html language=enus -->
## TOPIC 04600: AdapterListConnections.Add

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/adapterlistconnections-add.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/adapterlistconnections-add.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdapterListConnections.Add( uiObj) Return Value AdapterListConnection The AdapterListConnection this method creates. Purpose Creates and adds a new AdapterListConnection to the collection. Parameters uiObj As Object [In] Specifies the user interface object to connect. See Also AdapterListConn

### AdapterListConnections.Add

#### Syntax

[AdapterListConnections](adapterlistconnections.html).Add( uiObj)

#### Return Value

[AdapterListConnection](adapterlistconnection.html)

The AdapterListConnection this method creates.

#### Purpose

Creates and adds a new AdapterListConnection to the collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to connect.

#### See Also

[AdapterListConnection](adapterlistconnection.html)

[AdapterListConnections.Remove](adapterlistconnections-remove.html)

[ApplicationMgr.ConnectAdapterList](applicationmgr-connectadapterlist.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/adapterlistconnections-clear.html language=enus -->
## TOPIC 04601: AdapterListConnections.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/adapterlistconnections-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/adapterlistconnections-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdapterListConnections.Clear Purpose Removes all items from the collection. See Also AdapterListConnections.Remove

### AdapterListConnections.Clear

#### Syntax

[AdapterListConnections](adapterlistconnections.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[AdapterListConnections.Remove](adapterlistconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/adapterlistconnections-count.html language=enus -->
## TOPIC 04602: AdapterListConnections.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/adapterlistconnections-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/adapterlistconnections-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdapterListConnections.Count Data Type Long Purpose Returns the number of items in the collection.

### AdapterListConnections.Count

#### Syntax

[AdapterListConnections](adapterlistconnections.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/adapterlistconnections-fromcontrol.html language=enus -->
## TOPIC 04603: AdapterListConnections.FromControl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/adapterlistconnections-fromcontrol.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/adapterlistconnections-fromcontrol.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdapterListConnections.FromControl( uiObj) Return Value AdapterListConnection Purpose Returns the AdapterListConnection connected to the uiObj parameter. When no AdapterListConnection is connected to the user interface object the parameter specifies, this method returns NULL . Parameters uiOb

### AdapterListConnections.FromControl

#### Syntax

[AdapterListConnections](adapterlistconnections.html).FromControl( uiObj)

#### Return Value

[AdapterListConnection](adapterlistconnection.html)

#### Purpose

Returns the AdapterListConnection connected to the
 uiObj
 parameter. When no AdapterListConnection is connected to the user interface object the parameter specifies, this method returns
 NULL
 .

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies a connected user interface object.

#### See Also

[AdapterListConnection](adapterlistconnection.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/adapterlistconnections-item.html language=enus -->
## TOPIC 04604: AdapterListConnections.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/adapterlistconnections-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/adapterlistconnections-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdapterListConnections.Item( itemIndex) Data Type AdapterListConnection Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIndex As Long [In] Specifies the zero-based index of the item to retrieve. See Also AdapterListConnection AdapterListConnecti

### AdapterListConnections.Item

#### Syntax

[AdapterListConnections](adapterlistconnections.html).Item( itemIndex)

#### Data Type

[AdapterListConnection](adapterlistconnection.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index of the item to retrieve.

#### See Also

[AdapterListConnection](adapterlistconnection.html)

[AdapterListConnections.Count](adapterlistconnections-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/adapterlistconnections-remove.html language=enus -->
## TOPIC 04605: AdapterListConnections.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/adapterlistconnections-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/adapterlistconnections-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AdapterListConnections.Remove( uiObj) Return Value Boolean Returns True when the AdapterListConnection is removed. Returns False when the AdapterListConnection is not found. Purpose Removes the specified item from this collection, if it exists. Parameters uiObj As Object [In] Specifies the us

### AdapterListConnections.Remove

#### Syntax

[AdapterListConnections](adapterlistconnections.html).Remove( uiObj)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when the AdapterListConnection is removed. Returns
 False
 when the AdapterListConnection is not found.

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to disconnect.

#### See Also

[AdapterListConnection](adapterlistconnection.html)

[AdapterListConnections.Add](adapterlistconnections-add.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/adapterlistconnections.html language=enus -->
## TOPIC 04606: AdapterListConnections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/adapterlistconnections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/adapterlistconnections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of AdapterListConnection objects. Properties Count (Read Only) Item (Read Only) Methods Add Clear FromControl Remove See Also AdapterListConnection

### AdapterListConnections

A collection of
 [AdapterListConnection](adapterlistconnection.html)
 objects.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Add |
| --- |
| Clear |
| FromControl |
| Remove |

#### See Also

[AdapterListConnection](adapterlistconnection.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/alignmentstyles.html language=enus -->
## TOPIC 04607: AlignmentStyles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/alignmentstyles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/alignmentstyles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the text alignment of the Label and StatusBarPane controls. AlignmentStyle_Center –(Value: 2) Text is centered. AlignmentStyle_LeftJustify –(Value: 0) Text is left-aligned. AlignmentStyle_RightJustify –(Value: 1) Text is right-aligned. See Also Label StatusBarPane

### AlignmentStyles

Use these constants to specify the text alignment of the
 [Label](label.html)
 and
 [StatusBarPane](statusbarpane.html)
 controls.

- AlignmentStyle_Center 
 –(Value: 2) Text is centered.
- AlignmentStyle_LeftJustify 
 –(Value: 0) Text is left-aligned.
- AlignmentStyle_RightJustify 
 –(Value: 1) Text is right-aligned.

#### See Also

[Label](label.html)

[StatusBarPane](statusbarpane.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-addcommandlineargumentshelp.html language=enus -->
## TOPIC 04608: ApplicationMgr.AddCommandLineArgumentsHelp

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-addcommandlineargumentshelp.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-addcommandlineargumentshelp.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.AddCommandLineArgumentsHelp( usage, parameterHelp, notes) Purpose Use this method to document command-line arguments you define. Remarks The Application Manager control displays help for command-line arguments when you pass the /? switch to the application. Parameters usage As

### ApplicationMgr.AddCommandLineArgumentsHelp

#### Syntax

[ApplicationMgr](applicationmgr.html).AddCommandLineArgumentsHelp( usage, parameterHelp, notes)

#### Purpose

Use this method to document command-line arguments you define.

#### Remarks

The Application Manager control displays help for command-line arguments when you pass the
 /?
 switch to the application.

#### Parameters

usage
 As
 [String](data-types-for-teststand-user-interface.html)

[In] The Application Manager control adds this string to the usage section in the command-line help dialog box.

parameterHelp
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies a string for the Application Manager control to add to the section of the command-line help dialog box that explains parameters to command-line arguments.

notes
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies a string for the Application Manager control to add to the end of the command-line help dialog box.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-afteruimessageevent.html language=enus -->
## TOPIC 04609: ApplicationMgr.AfterUIMessageEvent

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-afteruimessageevent.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-afteruimessageevent.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_AfterUIMessageEvent( uiMsg) Applies To ApplicationMgr Purpose Forwards TestStand Engine events after the manager controls process them. Remarks Use this event to handle messages after the manager controls handle them. The Application Manager control automatically calls the UIMessa

### ApplicationMgr.AfterUIMessageEvent

#### Syntax

ControlName_AfterUIMessageEvent( uiMsg)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Forwards TestStand Engine events after the manager controls process them.

#### Remarks

Use this event to handle messages after the manager controls handle them.

The Application Manager control automatically calls the
 
 [UIMessage.Acknowledge](../tsapiref/uimessage-acknowledge.html)
 method when this event completes. Therefore, you do not have to directly call the
 UIMessage.Acknowledge
 method from within this event.

#### Parameters

uiMsg
 As
 
 [UIMessage](../tsapiref/uimessage.html)

[In] A TestStand user interface message.

#### See Also

[ApplicationMgr.UIMessageEvent](applicationmgr-uimessageevent.html)

[ApplicationMgr.UserMessage](applicationmgr-usermessage.html)

[UIMessage](../tsapiref/uimessage.html)

[UIMessage.Acknowledge](../tsapiref/uimessage-acknowledge.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-applicationwillexitonstart.html language=enus -->
## TOPIC 04610: ApplicationMgr.ApplicationWillExitOnStart

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-applicationwillexitonstart.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-applicationwillexitonstart.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.ApplicationWillExitOnStart Data Type Boolean Purpose Returns True when the application exits on start as a result of using the command-line switch /? or /useExisting . Check this property before you call the ApplicationMgr.Start method. When this property is True , do not launc

### ApplicationMgr.ApplicationWillExitOnStart

#### Syntax

[ApplicationMgr](applicationmgr.html).ApplicationWillExitOnStart

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Returns
 True
 when the application exits on start as a result of using the command-line switch
 /?
 or
 /useExisting
 . Check this property before you call the
 [ApplicationMgr.Start](applicationmgr-start.html)
 method. When this property is
 True
 , do not launch a splash screen or do any unnecessary time-consuming tasks.

#### See Also

[ApplicationMgr.ProcessCommandLine](applicationmgr-processcommandline.html)

[ApplicationMgr.Start](applicationmgr-start.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-automaticallyreloadmodifiedfil.html language=enus -->
## TOPIC 04611: ApplicationMgr.AutomaticallyReloadModifiedFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-automaticallyreloadmodifiedfil.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-automaticallyreloadmodifiedfil.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.AutomaticallyReloadModifiedFiles Data Type AutomaticallyReloadModifiedFilesOptions Use the following constants with this data type: AutomaticallyReloadModifiedFilesOption_DoNotReload –(Value: 1) Specifies that the Application Manager control never calls the ApplicationMgr.Reloa

### ApplicationMgr.AutomaticallyReloadModifiedFiles

#### Syntax

[ApplicationMgr](applicationmgr.html).AutomaticallyReloadModifiedFiles

#### Data Type

[AutomaticallyReloadModifiedFilesOptions](automaticallyreloadmodifiedfilesoptions.html)

Use the following constants with this data type:

- AutomaticallyReloadModifiedFilesOption_DoNotReload 
 –(Value: 1) Specifies that the Application Manager control never calls the
 ApplicationMgr.ReloadModifiedSequenceFilesEx 
 method. You must call the
 ApplicationMgr.ReloadModifiedSequenceFilesEx 
 method to reload modified sequence files.
- AutomaticallyReloadModifiedFilesOption_OnActivateApplication 
 –(Value: 3) Specifies that the Application Manager control calls the
 ApplicationMgr.ReloadModifiedSequenceFilesEx 
 method when you activate the application.
- AutomaticallyReloadModifiedFilesOption_OnTimer 
 –(Value: 2) Specifies that the Application Manager control calls the
 ApplicationMgr.ReloadModifiedSequenceFilesEx 
 method at the interval you specify with the
 ApplicationMgr.ReloadModifiedFilesInterval 
 property.

#### Purpose

Specifies when the Application Manager control reloads sequence files that you modified on disk.

#### Remarks

The Application Manager control generates the
 [ApplicationMgr.QueryReloadSequenceFile](applicationmgr-queryreloadsequencefile.html)
 event when the Application Manager control wants to reload the sequence file.

#### See Also

[ApplicationMgr.QueryReloadSequenceFile](applicationmgr-queryreloadsequencefile.html)

[ApplicationMgr.ReloadModifiedFilesInterval](applicationmgr-reloadmodifiedfilesinterval.html)

[ApplicationMgr.ReloadModifiedSequenceFiles](applicationmgr-reloadmodifiedsequencefiles.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-beginedit.html language=enus -->
## TOPIC 04612: ApplicationMgr.BeginEdit

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-beginedit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-beginedit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_BeginEdit( editedFile, editKind, objectsToEdit, cancel, editDenialReasons) Applies To ApplicationMgr Purpose Occurs before an editing action initiates or when you explicitly call the ApplicationMgr.BeginEdit method. Parameters editedFile As PropertyObjectFile [In] Specifies the fi

### ApplicationMgr.BeginEdit

#### Syntax

ControlName_BeginEdit( editedFile, editKind, objectsToEdit, cancel, editDenialReasons)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs before an editing action initiates or when you explicitly call the
 [ApplicationMgr.BeginEdit](applicationmgr-beginedit2.html)
 method.

#### Parameters

editedFile
 As
 
 [PropertyObjectFile](../tsapiref/propertyobjectfile.html)

[In] Specifies the file being edited.

editKind
 As
 
 [EditKinds](../tsapiref/editkinds.html)

[In] Specifies the type of editing action.

objectsToEdit
 As
 
 [PropertyObject](../tsapiref/propertyobject.html)

[In] Specifies the objects to edit. The
 objectsToEdit
 parameter is passed as a one-dimensional array of containers where each array element is an object to edit. You can call the
 
 [PropertyObject.GetNumElements](../tsapiref/propertyobject-getnumelements.html)
 method to obtain the length of the array and the
 
 [PropertyObject.GetPropertyObjectByOffset](../tsapiref/propertyobject-getpropertyobjectbyoffset.html)
 method to access array elements.

cancel
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In/Out] Pass
 True
 to prevent the edit from occurring.

editDenialReasons
 As
 [Long](data-types-for-teststand-user-interface.html)

[In/Out] Specifies a set of
 [EditingDenialReasons](editingdenialreasons.html)
 flags. When this parameter is non-zero, the flags in this parameter specify reasons why the edit cannot proceed. The application can clear these flags to allow the edit to proceed. For example, when the application integrates with source control systems and the
 EditingDenialReason_IsReadOnly
 flag is set, you could attempt to check out the selected file from source control to make it writable and then clear the
 EditingDenialReason_IsReadOnly
 flag if the checkout succeeds.

Note

EditingDenialReason_IsNotEditor

#### See Also

[ApplicationMgr.BeginEdit method](applicationmgr-beginedit2.html)

[ApplicationMgr.CanEdit event](applicationmgr-canedit.html)

[ApplicationMgr.EndEdit event](applicationmgr-endedit.html)

[EditingDenialReasons](editingdenialreasons.html)

[PropertyObject.GetNumElements](../tsapiref/propertyobject-getnumelements.html)

[PropertyObject.GetPropertyObjectByOffset](../tsapiref/propertyobject-getpropertyobjectbyoffset.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-beginedit2.html language=enus -->
## TOPIC 04613: ApplicationMgr.BeginEdit

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-beginedit2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-beginedit2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.BeginEdit( editedFile, editKind, objectsToEdit) Return Value Boolean Returns True when the application cancels the edit operation. When the application cancels the edit operation, do not modify the objectsToEdit parameter. Purpose Call this method before using the TestStand API

### ApplicationMgr.BeginEdit

#### Syntax

[ApplicationMgr](applicationmgr.html).BeginEdit( editedFile, editKind, objectsToEdit)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when the application cancels the edit operation. When the application cancels the edit operation, do not modify the
 objectsToEdit
 parameter.

#### Purpose

Call this method before using the TestStand API to edit files the
 [Application Manager](applicationmgr.html)
 and
 [SequenceFileView Manager](sequencefileviewmgr.html)
 controls display. This method generates an
 [ApplicationMgr.BeginEdit](applicationmgr-beginedit.html)
 event to notify the application about the edit.

#### Remarks

Always make a corresponding call to the
 [ApplicationMgr.EndEdit](applicationmgr-endedit2.html)
 method after you modify the
 objectsToEdit
 parameter. Call the
 ApplicationMgr.EndEdit
 method even when the application cancels the edit. Do not call the
 ApplicationMgr.BeginEdit
 or
 ApplicationMgr.EndEdit
 methods when you execute a
 [Command](command.html)
 object to perform an edit. The Command object automatically calls the
 ApplicationMgr.BeginEdit
 and
 ApplicationMgr.EndEdit
 methods.

#### Parameters

editedFile
 As
 
 [PropertyObjectFile](../tsapiref/propertyobjectfile.html)

[In] Specifies the file you are editing.

editKind
 As
 
 [EditKinds](../tsapiref/editkinds.html)

[In] Specifies the kind of edit you are making.

objectsToEdit
 As
 [Object Array](data-types-for-teststand-user-interface.html)

[In] Specifies the objects you are modifying.

#### See Also

[ApplicationMgr](applicationmgr.html)

[ApplicationMgr.BeginEdit event](applicationmgr-beginedit.html)

[ApplicationMgr.CanEdit](applicationmgr-canedit2.html)

[ApplicationMgr.EndEdit](applicationmgr-endedit2.html)

[Command](command.html)

[Command.Execute](command-execute.html)

[SequenceFileViewMgr](sequencefileviewmgr.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-break.html language=enus -->
## TOPIC 04614: ApplicationMgr.Break

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-break.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-break.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_Break( exec) Applies To ApplicationMgr Purpose Occurs when any execution breaks. Remarks An ApplicationMgr.DisplayExecution event follows this event. Parameters exec As Execution [In] Specifies a paused execution. See Also ApplicationMgr.DisplayExecution UIMsg_Break

### ApplicationMgr.Break

#### Syntax

ControlName_Break( exec)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when any execution breaks.

#### Remarks

An
 [ApplicationMgr.DisplayExecution](applicationmgr-displayexecution.html)
 event follows this event.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies a paused execution.

#### See Also

[ApplicationMgr.DisplayExecution](applicationmgr-displayexecution.html)

[UIMsg_Break](../tsapiref/uimessagecodes.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-breakonfirststep.html language=enus -->
## TOPIC 04615: ApplicationMgr.BreakOnFirstStep

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-breakonfirststep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-breakonfirststep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.BreakOnFirstStep Data Type Boolean Purpose When this property is True , all new executions break on the first step. Remarks The value of this property persists in the configuration file the ApplicationMgr.ConfigFilePath property specifies. See Also ApplicationMgr.BreakOnSequenc

### ApplicationMgr.BreakOnFirstStep

#### Syntax

[ApplicationMgr](applicationmgr.html).BreakOnFirstStep

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 , all new executions break on the first step.

#### Remarks

The value of this property persists in the configuration file the
 [ApplicationMgr.ConfigFilePath](applicationmgr-configfilepath.html)
 property specifies.

#### See Also

[ApplicationMgr.BreakOnSequenceFailure](applicationmgr-breakonsequencefailure.html)

[ApplicationMgr.BreakOnStepFailure](applicationmgr-breakonstepfailure.html)

[ApplicationMgr.ConfigFilePath](applicationmgr-configfilepath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-breakonruntimeerror.html language=enus -->
## TOPIC 04616: ApplicationMgr.BreakOnRunTimeError

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-breakonruntimeerror.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-breakonruntimeerror.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_BreakOnRunTimeError( exec, initiatingThread, showDialog, breakExecution) Applies To ApplicationMgr Purpose Occurs when TestStand sends the UIMsg_BreakOnRunTimeErrorMessage message. Remarks Use this event to launch a custom run-time error dialog box or to specify whether the Applic

### ApplicationMgr.BreakOnRunTimeError

#### Syntax

ControlName_BreakOnRunTimeError( exec, initiatingThread, showDialog, breakExecution)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when TestStand sends the
 UIMsg_BreakOnRunTimeErrorMessage
 message.

#### Remarks

Use this event to launch a custom run-time error dialog box or to specify whether the Application Manager control launches a
 [Run-Time Error](../tsref/run-time-error-dialog-box.html)
 dialog box or suspends the execution. You can change the
 
 [Execution.RTEOptionForThisExecution](../tsapiref/execution-rteoptionforthisexecution.html)
 property for the execution in this event before the Application Manager control handles it.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the execution to which the event applies.

initiatingThread
 As
 
 [Thread](../tsapiref/thread.html)

[In] Specifies the thread that sent the run-time error notification.

showDialog
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In/Out] The Application Manager control launches a Run-Time Error dialog box when the
 Execution.RTEOptionForThisExecution
 property is set to
 RTEOption_ShowDialog
 . Set this parameter to
 False
 when you do not want the Application Manager control to launch the Run-Time Error dialog box. Do not set this parameter to
 False
 to replace the default run-time error dialog box. Instead, handle the
 [ApplicationMgr.DisplayCustomRunTimeErrorDialog](applicationmgr-displaycustomruntimeerrordialo.html)
 event.

By default, this parameter is
 True
 .

breakExecution
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In/Out] Set this parameter to
 True
 to pause the current execution.

By default, this parameter is
 False
 .

#### See Also

[Execution.RTEOptionForThisExecution](../tsapiref/execution-rteoptionforthisexecution.html)

[Run-Time Error dialog box](../tsref/run-time-error-dialog-box.html)

[StationOptions.RTEOption](../tsapiref/stationoptions-rteoption.html)

[UIMsg_BreakOnRunTimeError](../tsapiref/uimessagecodes.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-breakonsequencefailure.html language=enus -->
## TOPIC 04617: ApplicationMgr.BreakOnSequenceFailure

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-breakonsequencefailure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-breakonsequencefailure.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.BreakOnSequenceFailure Data Type Boolean Purpose When this property is True , TestStand suspends an execution on sequence failure. When this property is False , TestStand suspends execution based on whether the ExecTypeMask_BreakOnSequenceFailure option is enabled in the Execut

### ApplicationMgr.BreakOnSequenceFailure

#### Syntax

[ApplicationMgr](applicationmgr.html).BreakOnSequenceFailure

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 , TestStand suspends an execution on sequence failure. When this property is
 False
 , TestStand suspends execution based on whether the
 
 [ExecTypeMask_BreakOnSequenceFailure](../tsapiref/executiontypemask.html)
 option is enabled in the
 
 [Execution.TypeMask](../tsapiref/execution-typemask.html)
 property for the execution.

#### Remarks

The value of this property is the same as the
 
 [StationOptions.BreakOnSequenceFailure](../tsapiref/stationoptions-breakonsequencefailure.html)
 property.

#### See Also

[ApplicationMgr.BreakOnFirstStep](applicationmgr-breakonfirststep.html)

[ApplicationMgr.BreakOnStepFailure](applicationmgr-breakonstepfailure.html)

[Execution.TypeMask](../tsapiref/execution-typemask.html)

[ExecutionTypeMask](../tsapiref/executiontypemask.html)

[StationOptions.BreakOnSequenceFailure](../tsapiref/stationoptions-breakonsequencefailure.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-breakonstepfailure.html language=enus -->
## TOPIC 04618: ApplicationMgr.BreakOnStepFailure

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-breakonstepfailure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-breakonstepfailure.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.BreakOnStepFailure Data Type Boolean Purpose When this property is True , TestStand suspends an execution for any step that fails. When this property is False , TestStand suspends execution based on whether the ExecTypeMask_BreakOnStepFailure option is enabled in the Execution.

### ApplicationMgr.BreakOnStepFailure

#### Syntax

[ApplicationMgr](applicationmgr.html).BreakOnStepFailure

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 , TestStand suspends an execution for any step that fails. When this property is
 False
 , TestStand suspends execution based on whether the
 
 [ExecTypeMask_BreakOnStepFailure](../tsapiref/executiontypemask.html)
 option is enabled in the
 
 [Execution.TypeMask](../tsapiref/execution-typemask.html)
 property for that execution.

#### Remarks

The value of this property is the same as the
 
 [StationOptions.BreakOnStepFailure](../tsapiref/stationoptions-breakonstepfailure.html)
 property.

#### See Also

[ApplicationMgr.BreakOnFirstStep](applicationmgr-breakonfirststep.html)

[ApplicationMgr.BreakOnSequenceFailure](applicationmgr-breakonsequencefailure.html)

[Execution.TypeMask](../tsapiref/execution-typemask.html)

[ExecutionTypeMask](../tsapiref/executiontypemask.html)

[StationOptions.BreakOnStepFailure](../tsapiref/stationoptions-breakonstepfailure.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-canedit.html language=enus -->
## TOPIC 04619: ApplicationMgr.CanEdit

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-canedit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-canedit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_CanEdit( editedFile, editKind, canEditValue, editDenialReasons) Applies To ApplicationMgr Purpose Occurs when an editing action determines the enabled state or when you explicitly call the ApplicationMgr.CanEdit method. Remarks The application can handle this event to modify the c

### ApplicationMgr.CanEdit

#### Syntax

ControlName_CanEdit( editedFile, editKind, canEditValue, editDenialReasons)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when an editing action determines the enabled state or when you explicitly call the
 [ApplicationMgr.CanEdit](applicationmgr-canedit2.html)
 method.

#### Remarks

The application can handle this event to modify the conditions that determine when to allow editing actions.

#### Parameters

editedFile
 As
 
 [PropertyObjectFile](../tsapiref/propertyobjectfile.html)

[In] Specifies the file being edited.

editKind
 As
 
 [EditKinds](../tsapiref/editkinds.html)

[In] Specifies the type of editing action.

canEditValue
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In/Out] Pass
 False
 to disable the editing action.

editDenialReasons
 As
 [Long](data-types-for-teststand-user-interface.html)

[In/Out] Specifies a set of
 [EditingDenialReasons](editingdenialreasons.html)
 flags. When this parameter is non-zero, the flags in this parameter specify reasons why the edit cannot proceed. The application can clear these flags to allow the edit to proceed. For example, when the application integrates with source control systems and the
 EditingDenialReason_IsReadOnly
 flag is set, you could attempt to check out the selected file from source control to make it writable and then clear the
 EditingDenialReason_IsReadOnly
 flag if the checkout succeeds.

Note

EditingDenialReason_IsNotEditor

#### See Also

[ApplicationMgr.BeginEdit event](applicationmgr-beginedit.html)

[ApplicationMgr.CanEdit method](applicationmgr-canedit2.html)

[ApplicationMgr.EndEdit event](applicationmgr-endedit.html)

[EditingDenialReasons](editingdenialreasons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-canedit2.html language=enus -->
## TOPIC 04620: ApplicationMgr.CanEdit

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-canedit2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-canedit2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.CanEdit( editedFile, editKind) Return Value Boolean Returns a Boolean value that indicates whether the application allows or denies permission to perform the edit. Purpose Call this method to query whether the application gives permission to use the TestStand API to edit the se

### ApplicationMgr.CanEdit

#### Syntax

[ApplicationMgr](applicationmgr.html).CanEdit( editedFile, editKind)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns a Boolean value that indicates whether the application allows or denies permission to perform the edit.

#### Purpose

Call this method to query whether the application gives permission to use the TestStand API to edit the sequence file the Application Manager control displays. This method generates an
 [ApplicationMgr.CanEdit](applicationmgr-canedit.html)
 event to notify the application about the edit.

#### Remarks

When the application implements custom editing actions on the selected sequence file using the TestStand API, call this method to determine whether to enable or disable the user interface element such as a menu or button that invokes the editing action. The application might not grant permission to edit based on a number of factors, such as the read-only state of the file, whether the file is executing, or other conditions the application considers when it responds to the
 ApplicationMgr.CanEdit
 event. Do not call this method to determine whether to enable a user interface element that invokes a
 [Command](command.html)
 object. Instead, obtain the value from the
 [Command.Enabled](command-enabled.html)
 property, which checks conditions specific to the command in addition to calling this method. When you connect a command to a button or when you connect a command to a menu item using the appropriate TestStand utility methods, the connection automatically queries the
 Command.Enabled
 property to enable or disable the button or menu item.

#### Parameters

editedFile
 As
 
 [PropertyObjectFile](../tsapiref/propertyobjectfile.html)

[In] Specifies the file you are editing.

editKind
 As
 
 [EditKinds](../tsapiref/editkinds.html)

[In] Specifies the kind of edit you are making.

#### See Also

[ApplicationMgr.BeginEdit](applicationmgr-beginedit2.html)

[ApplicationMgr.CanEdit event](applicationmgr-canedit.html)

[ApplicationMgr.EndEdit](applicationmgr-endedit2.html)

[Command.Enabled](command-enabled.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-closeallexecutions.html language=enus -->
## TOPIC 04621: ApplicationMgr.CloseAllExecutions

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-closeallexecutions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-closeallexecutions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.CloseAllExecutions Purpose Closes and releases all references to all executions. Remarks The Application Manager control attempts to close all executions by generating a QueryCloseExecution event for each execution in the Executions collection. The ApplicationMgr.QueryCloseExec

### ApplicationMgr.CloseAllExecutions

#### Syntax

[ApplicationMgr](applicationmgr.html).CloseAllExecutions

#### Purpose

Closes and releases all references to all executions.

#### Remarks

The Application Manager control attempts to close all executions by generating a
 [QueryCloseExecution](applicationmgr-querycloseexecution.html)
 event for each execution in the
 [Executions](executions.html)
 collection. The
 ApplicationMgr.QueryCloseExecution
 event determines whether to cancel the closing of an execution or take additional actions when the execution is running. This method does not wait for running or terminating executions to complete.

#### See Also

[ApplicationMgr.CloseExecution](applicationmgr-closeexecution.html)

[ApplicationMgr.QueryCloseExecution](applicationmgr-querycloseexecution.html)

[Executions](executions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-closeallsequencefiles.html language=enus -->
## TOPIC 04622: ApplicationMgr.CloseAllSequenceFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-closeallsequencefiles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-closeallsequencefiles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.CloseAllSequenceFiles Purpose Closes all open sequence files. Remarks The Application Manager control attempts to close all sequence files by generating a QueryCloseSequenceFile event for each sequence file in the SequenceFiles collection. The ApplicationMgr.QueryCloseSequenceF

### ApplicationMgr.CloseAllSequenceFiles

#### Syntax

[ApplicationMgr](applicationmgr.html).CloseAllSequenceFiles

#### Purpose

Closes all open sequence files.

#### Remarks

The Application Manager control attempts to close all sequence files by generating a
 [QueryCloseSequenceFile](applicationmgr-queryclosesequencefile.html)
 event for each sequence file in the
 [SequenceFiles](sequencefiles.html)
 collection. The
 ApplicationMgr.QueryCloseSequenceFile
 event confirms whether to release the file and remove the file from the
 SequenceFiles
 collection. When a sequence file is running in an execution or when other references to the sequence file exist, TestStand does not immediately unload the sequence file from memory.

#### See Also

[ApplicationMgr.CloseSequenceFile](applicationmgr-closesequencefile.html)

[ApplicationMgr.QueryCloseSequenceFile](applicationmgr-queryclosesequencefile.html)

[ApplicationMgr.SequenceFileClosing](applicationmgr-sequencefileclosing.html)

[SequenceFiles](sequencefiles.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-closeexecution.html language=enus -->
## TOPIC 04623: ApplicationMgr.CloseExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-closeexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-closeexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.CloseExecution( exec) Return Value Boolean Returns True if the execution was closed. Purpose Releases all references to the execution. Remarks The Application Manager control attempts to close the execution by generating a QueryCloseExecution event. The ApplicationMgr.QueryClos

### ApplicationMgr.CloseExecution

#### Syntax

[ApplicationMgr](applicationmgr.html).CloseExecution( exec)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 if the execution was closed.

#### Purpose

Releases all references to the execution.

#### Remarks

The Application Manager control attempts to close the execution by generating a
 [QueryCloseExecution](applicationmgr-querycloseexecution.html)
 event. The
 ApplicationMgr.QueryCloseExecution
 event determines whether to cancel the closing of an execution or take additional actions when the execution is running. This method does not wait for running or terminating executions to complete.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the execution to close.

#### See Also

[ApplicationMgr.CloseAllExecutions](applicationmgr-closeallexecutions.html)

[ApplicationMgr.QueryCloseExecution](applicationmgr-querycloseexecution.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-closesequencefile.html language=enus -->
## TOPIC 04624: ApplicationMgr.CloseSequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-closesequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-closesequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.CloseSequenceFile( file) Return Value Boolean Returns True if the sequence file was closed. Purpose Closes a sequence file. Remarks The Application Manager control attempts to close the sequence file by generating a QueryCloseSequenceFile event. The ApplicationMgr.QueryCloseSeq

### ApplicationMgr.CloseSequenceFile

#### Syntax

[ApplicationMgr](applicationmgr.html).CloseSequenceFile( file)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 if the sequence file was closed.

#### Purpose

Closes a sequence file.

#### Remarks

The Application Manager control attempts to close the sequence file by generating a
 [QueryCloseSequenceFile](applicationmgr-queryclosesequencefile.html)
 event. The
 ApplicationMgr.QueryCloseSequenceFile
 event confirms whether to release the file and remove the file from the
 [SequenceFiles](sequencefiles.html)
 collection. When the sequence file is running in an execution or when other references to the sequence file exist, TestStand does not immediately unload the file from memory.

#### Parameters

file
 As
 
 [SequenceFile](../tsapiref/sequencefile.html)

[In] Specifies the sequence file to close.

#### See Also

[ApplicationMgr.QueryCloseSequenceFile](applicationmgr-queryclosesequencefile.html)

[ApplicationMgr.SequenceFileClosing](applicationmgr-sequencefileclosing.html)

[SequenceFiles](sequencefiles.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-commandlinearguments.html language=enus -->
## TOPIC 04625: ApplicationMgr.CommandLineArguments

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-commandlinearguments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-commandlinearguments.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.CommandLineArguments Data Type Strings Purpose Returns the collection of command-line arguments to the application. The following are switches on the command line: /run <sequence> <sequencefile> —Runs the sequence in the sequence file. /runEntryPoint <entryPointName> <SequenceF

### ApplicationMgr.CommandLineArguments

#### Syntax

[ApplicationMgr](applicationmgr.html).CommandLineArguments

#### Data Type

[Strings](strings.html)

#### Purpose

Returns the collection of command-line arguments to the application. The following are switches on the command line:

- /run <sequence> <sequencefile> 
 —Runs the sequence in the sequence file.
- /runEntryPoint <entryPointName> <SequenceFile> 
 —Runs the entry point on the sequence file.
- /quit 
 —Exits the application once all executions complete.
- /setCurrentDir 
 —Sets the current directory to the first directory in the directory history list in the File dialog box. The current directory is the directory the File dialog box initially displays when you open a file. Use this option to set the directory the File dialog box displays to the directory the File dialog box displayed the last time you ran the application. The application sets the current directory after processing the other command-line options.
- /? 
 —Launches a help dialog box, which contains a list of valid command-line arguments, and then immediately closes.
- /useExisting 
 —Prevents a second instance of the application from running and forwards all command-line arguments to the application that is already running.
- /goto <location> 
 —Instructs the application to display the item the <location> property object path specifies, such as
 TestExec.exe C:\example.seq /goto "Seq[\"MainSequence\"].Main[\"Power On\"]" 
 TestExec.exe C:\example.seq /goto "Seq[\"MainSequence\"].Main[\"ID#:JifH4ODTf0y1z7bJne0G7D\"]" 
 TestExec.exe C:\example.seq /goto "Seq[1].Main[4].TS.LoadOpt"
- /editor 
 —Enables the application to create and edit sequence files. You must have activated a
 
 license 
 that supports creating and editing sequence files.
- /operatorInterface 
 —Prevents the application from creating and editing sequence files.
 Note 
 You can use
 /
 or
 -
 to specify a switch. Quotation marks are required for arguments that contain a space, such as
 "Test UUTs"
 and
 "C:\My Documents\Test Sequence.seq"
 .

#### Remarks

The collection is created by splitting up the command line used to start the application, using white space as a delimiter.

Note

/useExisting

ApplicationMgr.ProcessUserCommandLineArguments

#### See Also

[ApplicationMgr.ProcessCommandLine](applicationmgr-processcommandline.html)

[ApplicationMgr.ProcessUserCommandLineArguments](applicationmgr-processusercommandlineargument.html)

[TestStand Licensing Options](/csh?context=ts_9050)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-commandlinecanchangeeditmode.html language=enus -->
## TOPIC 04626: ApplicationMgr.CommandLineCanChangeEditMode

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-commandlinecanchangeeditmode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-commandlinecanchangeeditmode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.CommandLineCanChangeEditMode Data Type Boolean Purpose Set this property to False to prevent users from changing the edit mode of the application by passing /operatorInterface or /editor on the command line. Remarks Requests to launch an application in Editor Mode might prompt

### ApplicationMgr.CommandLineCanChangeEditMode

#### Syntax

[ApplicationMgr](applicationmgr.html).CommandLineCanChangeEditMode

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Set this property to
 False
 to prevent users from changing the edit mode of the application by passing
 /operatorInterface
 or
 /editor
 on the command line.

#### Remarks

Requests to launch an application in Editor Mode might prompt a user to activate a
 
 [license](/csh?context=ts_9050)
 when the Application Manager control cannot acquire the appropriate license to edit and save sequence files.

#### See Also

[ApplicationMgr.EditModeShortcutKey](applicationmgr-editmodeshortcutkey.html)

[ApplicationMgr.EditModeShortcutModifier](applicationmgr-editmodeshortcutmodifier.html)

[ApplicationMgr.IsEditor](applicationmgr-iseditor.html)

[ApplicationMgr.Start](applicationmgr-start.html)

[TestStand Licensing Options](/csh?context=ts_9050)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-configfile.html language=enus -->
## TOPIC 04627: ApplicationMgr.ConfigFile

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-configfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-configfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.ConfigFile Data Type PropertyObjectFile Purpose Returns the PropertyObjectFile object that represents the configuration information that persists between sessions of the application. Remarks The ApplicationMgr.ConfigFilePath property specifies the property object filename. See

### ApplicationMgr.ConfigFile

#### Syntax

[ApplicationMgr](applicationmgr.html).ConfigFile

#### Data Type

[PropertyObjectFile](../tsapiref/propertyobjectfile.html)

#### Purpose

Returns the PropertyObjectFile object that represents the configuration information that persists between sessions of the application.

#### Remarks

The
 [ApplicationMgr.ConfigFilePath](applicationmgr-configfilepath.html)
 property specifies the property object filename.

#### See Also

[ApplicationMgr.ConfigFilePath](applicationmgr-configfilepath.html)

[ApplicationMgr.MakeStepNamesUnique](applicationmgr-makestepnamesunique.html)

[ApplicationMgr.PromptForOverwrite](applicationmgr-promptforoverwrite.html)

[ApplicationMgr.ReloadConfigFile](applicationmgr-reloadconfigfile.html)

[ApplicationMgr.SaveOnClose](applicationmgr-saveonclose.html)

[PropertyObjectFile](../tsapiref/propertyobjectfile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-configfilepath.html language=enus -->
## TOPIC 04628: ApplicationMgr.ConfigFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-configfilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-configfilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.ConfigFilePath Data Type String Purpose Specifies the path of the configuration file. Remarks Once the file has been loaded and you have called the ApplicationMgr.Start method, the path cannot be changed. The default pathname is %TestStandLocalAppData%\UserInterface.xml . This

### ApplicationMgr.ConfigFilePath

#### Syntax

[ApplicationMgr](applicationmgr.html).ConfigFilePath

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the path of the configuration file.

#### Remarks

Once the file has been loaded and you have called the
 [ApplicationMgr.Start](applicationmgr-start.html)
 method, the path cannot be changed. The default pathname is
 %TestStandLocalAppData%\UserInterface.xml
 .

Note

%TSVer%

%TestStandConfig%

%TestStandLocalAppData%

%TSVer%

%TestStandConfig%

Engine.GetTestStandPath

TestStandPath_Config

%TestStandLocalAppData%

Engine.GetTestStandPath

TestStandPath_LocalAppData

#### See Also

[ApplicationMgr.ConfigFile](applicationmgr-configfile.html)

[ApplicationMgr.Start](applicationmgr-start.html)

[Engine.GetTestStandPath](../tsapiref/engine-getteststandpath.html)

[TestStandPaths](../tsapiref/teststandpaths.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-configurationentrypoints.html language=enus -->
## TOPIC 04629: ApplicationMgr.ConfigurationEntryPoints

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-configurationentrypoints.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-configurationentrypoints.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.ConfigurationEntryPoints Data Type EntryPoints Purpose Returns the set of Configuration entry points that the station model sequence file defines. Remarks This collection can change when the station model sequence file changes. See Also ApplicationMgr.ExecutionEntryPoints Engin

### ApplicationMgr.ConfigurationEntryPoints

#### Syntax

[ApplicationMgr](applicationmgr.html).ConfigurationEntryPoints

#### Data Type

[EntryPoints](entrypoints.html)

#### Purpose

Returns the set of Configuration entry points that the station model sequence file defines.

#### Remarks

This collection can change when the station model sequence file changes.

#### See Also

[ApplicationMgr.ExecutionEntryPoints](applicationmgr-executionentrypoints.html)

[Engine.GetStationModelSequenceFile](../tsapiref/engine-getstationmodelsequencefile.html)

[EntryPoints](entrypoints.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-connectadapterlist.html language=enus -->
## TOPIC 04630: ApplicationMgr.ConnectAdapterList

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-connectadapterlist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-connectadapterlist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.ConnectAdapterList( uiObj) Return Value AdapterListConnection Purpose Connects the list of adapters to a ComboBox , ListBarPage , or ListBox control. The connected control shows the adapters and allows the user to select an adapter as the default adapter of the TestStand Engine

### ApplicationMgr.ConnectAdapterList

#### Syntax

[ApplicationMgr](applicationmgr.html).ConnectAdapterList( uiObj)

#### Return Value

[AdapterListConnection](adapterlistconnection.html)

#### Purpose

Connects the list of adapters to a
 [ComboBox](combobox.html)
 ,
 [ListBarPage](listbarpage.html)
 , or
 [ListBox](listbox.html)
 control. The connected control shows the adapters and allows the user to select an adapter as the default adapter of the TestStand Engine.

#### Remarks

To disconnect an existing connection, you must first obtain the
 [ApplicationMgrConnections](applicationmgrconnections.html)
 object from the
 [ApplicationMgr.Connections](applicationmgr-connections.html)
 property. Then, access the
 [ApplicationMgrConnections.AdapterList](applicationmgrconnections-adapterlist.html)
 property to obtain the
 [AdapterListConnections](adapterlistconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the visible control or element of a visible control to display the list of adapters. Pass a ComboBox, ListBarPage, or ListBox.

#### See Also

[AdapterListConnections](adapterlistconnections.html)

[ApplicationMgr.Connections](applicationmgr-connections.html)

[ApplicationMgrConnections](applicationmgrconnections.html)

[ApplicationMgrConnections.AdapterList](applicationmgrconnections-adapterlist.html)

[ComboBox](combobox.html)

[Engine.DefaultAdapter](../tsapiref/engine-defaultadapter.html)

[Engine.DefaultAdapterIndex](../tsapiref/engine-defaultadapterindex.html)

[ListBarPage](listbarpage.html)

[ListBox](listbox.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-connectcaption.html language=enus -->
## TOPIC 04631: ApplicationMgr.ConnectCaption

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-connectcaption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-connectcaption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.ConnectCaption( uiObj, captionSource, longName) Return Value CaptionConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected with this type of connection, the existing c

### ApplicationMgr.ConnectCaption

#### Syntax

[ApplicationMgr](applicationmgr.html).ConnectCaption( uiObj, captionSource, longName)

#### Return Value

[CaptionConnection](captionconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected with this type of connection, the existing connection is returned.

#### Purpose

Connects a caption source in the Application Manager control to a visible control or an element of a visible control. The connection automatically updates the visible control with the text that describes an aspect of the application state.

#### Remarks

You can use this method to display a caption in a
 [Label](label.html)
 ,
 [ExpressionEdit](expressionedit.html)
 or
 [StatusBarPane](statusbarpane.html)
 control.

To disconnect an existing connection, you must first obtain the
 [ApplicationMgrConnections](applicationmgrconnections.html)
 object from the
 [ApplicationMgr.Connections](applicationmgr-connections.html)
 property. Then, access the
 [ApplicationMgrConnections.Caption](applicationmgrconnections-caption.html)
 property to obtain the
 [CaptionConnections](captionconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the visible control, or element of a visible control to which the caption source connects. Pass a
 [Label](label.html)
 ,
 [ExpressionEdit](expressionedit.html)
 , or
 [StatusBarPane](statusbarpane.html)
 .

captionSource
 As
 [CaptionSources](captionsources.html)

[In] Specifies the type of caption source to connect.

longName
 As
 [Boolean](data-types-for-teststand-user-interface.html)

For certain caption sources, this parameter specifies whether the connection displays the long or short version of the caption text. Refer to the
 [CaptionSources](captionsources.html)
 enumeration for more information about the difference between the long and short versions of the text and to determine when this option affects a caption source.

#### See Also

[ApplicationMgr.Connections](applicationmgr-connections.html)

[ApplicationMgr.GetCaptionText](applicationmgr-getcaptiontext.html)

[ApplicationMgrConnections](applicationmgrconnections.html)

[ApplicationMgrConnections.Caption](applicationmgrconnections-caption.html)

[CaptionConnection](captionconnection.html)

[CaptionConnections](captionconnections.html)

[CaptionSources](captionsources.html)

[ExecutionViewMgr.ConnectCaption](executionviewmgr-connectcaption.html)

[ExpressionEdit](expressionedit.html)

[Label](label.html)

[SequenceFileViewMgr.ConnectCaption](sequencefileviewmgr-connectcaption.html)

[StatusBarPane](statusbarpane.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-connectcommand.html language=enus -->
## TOPIC 04632: ApplicationMgr.ConnectCommand

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-connectcommand.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-connectcommand.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.ConnectCommand( uiObj, cmdKind, index = 0, opts = 0) Return Value CommandConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected with this type of connection, the exist

### ApplicationMgr.ConnectCommand

#### Syntax

[ApplicationMgr](applicationmgr.html).ConnectCommand( uiObj, cmdKind, index = 0, opts = 0)

#### Return Value

[CommandConnection](commandconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected with this type of connection, the existing connection is returned.

#### Purpose

Connects a control to the Application Manager control to make the connected control function as a command.

#### Remarks

You can connect TestStand User Interface buttons and checkboxes using this method.

To disconnect an existing connection, you must first obtain the
 [ApplicationMgrConnections](applicationmgrconnections.html)
 object from the
 [ApplicationMgr.Connections](applicationmgr-connections.html)
 property. Then, access the
 [ApplicationMgrConnections.Command](applicationmgrconnections-command.html)
 property to obtain the
 [CommandConnections](commandconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the button or checkbox control to which the command connects.

cmdKind
 As
 [CommandKinds](commandkinds.html)

[In] Specifies the type of command to connect.

Note

CommandKinds

index
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies an index into command sets. For example, when you connect to
 CommandKind_EntryPointSet
 , this parameter specifies the index of the entry point to use.

This parameter has a default value of
 0
 .

opts
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies a bitwise-OR combination of the
 [CommandConnectionOptions](commandconnectionoptions.html)
 constants.

This parameter has a default value of
 0
 .

#### See Also

[ApplicationMgr.Connections](applicationmgr-connections.html)

[ApplicationMgr.GetCommand](applicationmgr-getcommand.html)

[ApplicationMgrConnections](applicationmgrconnections.html)

[ApplicationMgrConnections.Command](applicationmgrconnections-command.html)

[Button](button.html)

[CommandConnection](commandconnection.html)

[CommandConnections](commandconnections.html)

[CommandConnectionOptions](commandconnectionoptions.html)

[CommandKinds](commandkinds.html)

[ExecutionViewMgr.ConnectCommand](executionviewmgr-connectcommand.html)

[SequenceFileViewMgr.ConnectCommand](sequencefileviewmgr-connectcommand.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-connections.html language=enus -->
## TOPIC 04633: ApplicationMgr.Connections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-connections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-connections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.Connections Data Type ApplicationMgrConnections Purpose Returns the ApplicationMgrConnections object, which contains the collection of the connections made to the Application Manager control. Remarks Typically, you do not need to use this object. To make connections to the Appl

### ApplicationMgr.Connections

#### Syntax

[ApplicationMgr](applicationmgr.html).Connections

#### Data Type

[ApplicationMgrConnections](applicationmgrconnections.html)

#### Purpose

Returns the
 [ApplicationMgrConnections](applicationmgrconnections.html)
 object, which contains the collection of the connections made to the Application Manager control.

#### Remarks

Typically, you do not need to use this object.

To make connections to the Application Manager control, use the
 [ApplicationMgr.ConnectCaption](applicationmgr-connectcaption.html)
 and the
 [ApplicationMgr.ConnectCommand](applicationmgr-connectcommand.html)
 methods.

#### See Also

[ApplicationMgr.ExecutionEntryPoints](applicationmgr-executionentrypoints.html)

[ApplicationMgr.ConnectCaption](applicationmgr-connectcaption.html)

[ApplicationMgr.ExecutionEntryPoints](applicationmgr-executionentrypoints.html)

[ApplicationMgr.ConnectCommand](applicationmgr-connectcommand.html)

[ApplicationMgrConnections](applicationmgrconnections.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-createemptysequencefileonstart.html language=enus -->
## TOPIC 04634: ApplicationMgr.CreateEmptySequenceFileOnStart

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-createemptysequencefileonstart.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-createemptysequencefileonstart.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.CreateEmptySequenceFileOnStart Data Type Boolean Purpose Specifies that the Application Manager control creates a new, empty sequence file at startup when the application is in edit mode, no initially opened sequences files exist, and a user logs in with the privilege to edit s

### ApplicationMgr.CreateEmptySequenceFileOnStart

#### Syntax

[ApplicationMgr](applicationmgr.html).CreateEmptySequenceFileOnStart

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies that the Application Manager control creates a new, empty sequence file at startup when the application is in edit mode, no initially opened sequences files exist, and a user logs in with the privilege to edit sequence files. When users open or create another file before making any changes to the empty automatically created file, the automatically created file closes.

#### Remarks

If you do not want the Application Manager control to create an empty file for the user, set this property to
 False
 in the designer or in the application before you call the
 [ApplicationMgr.Start](applicationmgr-start.html)
 method.

#### See Also

[ApplicationMgr.IsEditor](applicationmgr-iseditor.html)

[ApplicationMgr.ReloadSequenceFilesOnStart](applicationmgr-reloadsequencefilesonstart.html)

[ApplicationMgr.Start](applicationmgr-start.html)

[Priv_EditSequenceFiles](../tsapiref/userprivileges.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-currentuimessage.html language=enus -->
## TOPIC 04635: ApplicationMgr.CurrentUIMessage

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-currentuimessage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-currentuimessage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.CurrentUIMessage Data Type UIMessage Purpose Accesses the current message being processed. Remarks This property returns the current TestStand user interface message object when you need more information while handling an event. See Also Engine.UIMessageEvent ExecutionViewMgr.U

### ApplicationMgr.CurrentUIMessage

#### Syntax

[ApplicationMgr](applicationmgr.html).CurrentUIMessage

#### Data Type

[UIMessage](../tsapiref/uimessage.html)

#### Purpose

Accesses the current message being processed.

#### Remarks

This property returns the current TestStand user interface message object when you need more information while handling an event.

#### See Also

[Engine.UIMessageEvent](../tsapiref/engine-uimessageevent.html)

[ExecutionViewMgr.UserMessage](executionviewmgr-usermessage.html)

[UIMessage](../tsapiref/uimessage.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-displaycustomruntimeerrordialo.html language=enus -->
## TOPIC 04636: ApplicationMgr.DisplayCustomRunTimeErrorDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-displaycustomruntimeerrordialo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-displaycustomruntimeerrordialo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_DisplayCustomRunTimeErrorDialog( ctxt, breakExec, doNotShowAgainForExecution, doNotShowAgainForBatch, rteOption, showDefaultDialog) Applies To ApplicationMgr Purpose Occurs before TestStand launches the default run-time error dialog box. You can use this event to launch a custom r

### ApplicationMgr.DisplayCustomRunTimeErrorDialog

#### Syntax

ControlName_DisplayCustomRunTimeErrorDialog( ctxt, breakExec, doNotShowAgainForExecution, doNotShowAgainForBatch, rteOption, showDefaultDialog)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs before TestStand launches the default run-time error dialog box. You can use this event to launch a custom run-time error dialog box.

#### Parameters

ctxt
 As
 
 [SequenceContext](../tsapiref/sequencecontext.html)

[In] Specifies the SequenceContext in which the run-time error occurred.

breakExec
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In/Out] Set this parameter to
 True
 to pause the current execution.

doNotShowAgainForExecution
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In/Out] Set this parameter to
 True
 to set the
 
 [Execution.RTEOptionForThisExecution](../tsapiref/execution-rteoptionforthisexecution.html)
 property to the value of the
 rteOption
 parameter.

doNotShowAgainForBatch
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In/Out] Set this parameter to
 True
 to set the
 
 [Thread.SetBatchRTEOption](../tsapiref/thread-setbatchrteoption.html)
 method to the value of the
 rteOption
 parameter.

rteOption
 As
 [Long](data-types-for-teststand-user-interface.html)

[In/Out] Use the
 
 [RTEOptions constants](../tsapiref/rteoptions.html)
 to specify how TestStand handles the run-time error.

showDefaultDialog
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In/Out] Set this parameter to
 True
 to launch the default run-time error dialog box.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-displayexecution.html language=enus -->
## TOPIC 04637: ApplicationMgr.DisplayExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-displayexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-displayexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_DisplayExecution( exec, reason) Applies To ApplicationMgr Purpose Occurs when a visible execution starts, when an execution breaks, or in response to a UIMsg_OpenWindow or a UIMsg_GotoLocation user interface message. Use the reason parameter to find out why this event was called.

### ApplicationMgr.DisplayExecution

#### Syntax

ControlName_DisplayExecution( exec, reason)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when a visible execution starts, when an execution breaks, or in response to a
 UIMsg_OpenWindow
 or a
 UIMsg_GotoLocation
 user interface message. Use the
 reason
 parameter to find out why this event was called.

#### Remarks

Use this event to display the execution in a window by setting the
 [ExecutionViewMgr.Execution](executionviewmgr-execution.html)
 property on the ExecutionView Manager control for the window.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the execution to display.

reason
 As
 [ExecutionDisplayReasons](executiondisplayreasons.html)

[In] Specifies the reason why the event was generated. Refer to the
 [ExecutionDisplayReasons](executiondisplayreasons.html)
 enumeration for more information about reasons for execution actions.

#### See Also

[ApplicationMgr.CurrentUIMessage](applicationmgr-currentuimessage.html)

[ApplicationMgr.GetVisible](applicationmgr-getvisible.html)

[ApplicationMgr.SetVisible](applicationmgr-setvisible.html)

[ExecutionDisplayReasons](executiondisplayreasons.html)

[ExecutionViewMgr.Execution](executionviewmgr-execution.html)

[UIMsg_OpenWindow](../tsapiref/uimessagecodes.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-displayreport.html language=enus -->
## TOPIC 04638: ApplicationMgr.DisplayReport

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-displayreport.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-displayreport.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_DisplayReport( exec) Applies To ApplicationMgr Purpose Occurs when the UIMsg_DisplayReport user interface message is received. Remarks Use this event to show the window that displays the report. Parameters exec As Execution [In] Specifies the execution that contains the report to

### ApplicationMgr.DisplayReport

#### Syntax

ControlName_DisplayReport( exec)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when the
 UIMsg_DisplayReport
 user interface message is received.

#### Remarks

Use this event to show the window that displays the report.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the execution that contains the report to display.

#### See Also

[UIMessageCodes](../tsapiref/uimessagecodes.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-displaysequencefile.html language=enus -->
## TOPIC 04639: ApplicationMgr.DisplaySequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-displaysequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-displaysequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_DisplaySequenceFile( file, reason) Applies To ApplicationMgr Purpose Occurs when a sequence file is opened directly or in response to a UIMsg_OpenWindows event TestStand sends. Remarks Use this event to display the sequence file in a Sequence File window by setting the SequenceFil

### ApplicationMgr.DisplaySequenceFile

#### Syntax

ControlName_DisplaySequenceFile( file, reason)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when a sequence file is opened directly or in response to a
 UIMsg_OpenWindows
 event TestStand sends.

#### Remarks

Use this event to display the sequence file in a Sequence File window by setting the
 [SequenceFileViewMgr.SequenceFile](sequencefileviewmgr-sequencefile.html)
 property on the SequenceFileView Manager control for the window.

#### Parameters

file
 As
 
 [SequenceFile](../tsapiref/sequencefile.html)

[In] Specifies the sequence file to display.

reason
 As
 [SequenceFileDisplayReasons](sequencefiledisplayreasons.html)

[In] Specifies the reason why the event was generated. Refer to the
 [SequenceFileDisplayReasons](sequencefiledisplayreasons.html)
 enumeration for more information about reasons for sequence file actions.

#### See Also

[SequenceFileDisplayReasons](sequencefiledisplayreasons.html)

[SequenceFileViewMgr.SequenceFile](sequencefileviewmgr-sequencefile.html)

[UIMsg_OpenWindows](../tsapiref/uimessagecodes.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-dropfile.html language=enus -->
## TOPIC 04640: ApplicationMgr.DropFile

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-dropfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-dropfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_DropFile( file, handled) Applies To ApplicationMgr Purpose Occurs when you drop a file onto a TestStand User Interface (UI) Control that supports drag and drop. When you drop multiple files at once, the Application Manager control generates this event once for each file dropped. R

### ApplicationMgr.DropFile

#### Syntax

ControlName_DropFile( file, handled)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when you drop a file onto a TestStand User Interface (UI) Control that supports drag and drop. When you drop multiple files at once, the Application Manager control generates this event once for each file dropped.

#### Remarks

This event is useful for supporting drag and drop of files that are not sequence files and must be handled differently. You can customize TestStand to natively support opening custom file formats and
 [translating](/csh?context=ts_tsfundamentals_translators)
 them into sequence files.

When you drop a file onto a
 SequenceView
 control and the file is a valid TestStand code module file, the control inserts a step with its code module configured to call the file. Before the
 SequenceView
 control inserts the step, the Application Manager control generates the
 DropFile
 event for the dropped file. If your application handles the
 DropFile
 event, the
 SequenceView
 control does not insert the step.

#### Parameters

file
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the absolute pathname of the file you dropped.

handled
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In/Out] Set this parameter to
 True
 when you programmatically open the file in the event handler and do not want the Application Manager to try to open the file. When you do not set this parameter to
 True
 , the Application Manager control opens the file as a sequence file or, if the file is a valid code module file and the file was dropped on a
 SequenceView
 control, the
 SequenceView
 control inserts a step configured to call the code module file.

#### See Also

[Translating custom file format into sequence files](/csh?context=ts_tsfundamentals_translators)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-editmodechanged.html language=enus -->
## TOPIC 04641: ApplicationMgr.EditModeChanged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-editmodechanged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-editmodechanged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_EditModeChanged Applies To ApplicationMgr Purpose Occurs when the ApplicationMgr.IsEditor property changes when directly set or when processing command-line arguments. See Also ApplicationMgr.IsEditor

### ApplicationMgr.EditModeChanged

#### Syntax

ControlName_EditModeChanged

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when the
 [ApplicationMgr.IsEditor](applicationmgr-iseditor.html)
 property changes when directly set or when processing command-line arguments.

#### See Also

[ApplicationMgr.IsEditor](applicationmgr-iseditor.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-editmodeshortcutkey.html language=enus -->
## TOPIC 04642: ApplicationMgr.EditModeShortcutKey

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-editmodeshortcutkey.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-editmodeshortcutkey.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.EditModeShortcutKey Data Type ShortcutKeys Purpose Specifies a key users can press to toggle the ApplicationMgr.IsEditor property. To prevent users from toggling the edit mode with a keystroke, set this property to ShortcutKey_VK_NOT_A_KEY . Remarks Requests to switch an applic

### ApplicationMgr.EditModeShortcutKey

#### Syntax

[ApplicationMgr](applicationmgr.html).EditModeShortcutKey

#### Data Type

[ShortcutKeys](shortcutkeys.html)

#### Purpose

Specifies a key users can press to toggle the
 [ApplicationMgr.IsEditor](applicationmgr-iseditor.html)
 property. To prevent users from toggling the edit mode with a keystroke, set this property to
 ShortcutKey_VK_NOT_A_KEY
 .

#### Remarks

Requests to switch an application to Editor Mode might prompt a user to activate a
 
 [license](/csh?context=ts_9050)
 when the Application Manager control cannot acquire the appropriate license to edit and save sequence files.

#### See Also

[ApplicationMgr.CommandLineCanChangeEditMode](applicationmgr-commandlinecanchangeeditmode.html)

[ApplicationMgr.EditModeShortcutModifier](applicationmgr-editmodeshortcutmodifier.html)

[ApplicationMgr.IsEditor](applicationmgr-iseditor.html)

[ApplicationMgr.Start](applicationmgr-start.html)

[ShortcutKeys](shortcutkeys.html)

[TestStand Licensing Options](/csh?context=ts_9050)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-editmodeshortcutmodifier.html language=enus -->
## TOPIC 04643: ApplicationMgr.EditModeShortcutModifier

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-editmodeshortcutmodifier.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-editmodeshortcutmodifier.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.EditModeShortcutModifier Data Type Long Purpose Specifies a modifier for the key users can press to toggle the ApplicationMgr.IsEditor property. Use any combination of the ShortcutModifiers constants. See Also ApplicationMgr.CommandLineCanChangeEditMode ApplicationMgr.EditModeS

### ApplicationMgr.EditModeShortcutModifier

#### Syntax

[ApplicationMgr](applicationmgr.html).EditModeShortcutModifier

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies a modifier for the key users can press to toggle the
 [ApplicationMgr.IsEditor](applicationmgr-iseditor.html)
 property. Use any combination of the
 [ShortcutModifiers](shortcutmodifiers.html)
 constants.

#### See Also

[ApplicationMgr.CommandLineCanChangeEditMode](applicationmgr-commandlinecanchangeeditmode.html)

[ApplicationMgr.EditModeShortcutKey](applicationmgr-editmodeshortcutkey.html)

[ApplicationMgr.IsEditor](applicationmgr-iseditor.html)

[ApplicationMgr.Start](applicationmgr-start.html)

[ShortcutModifiers](shortcutmodifiers.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-editreadonlyfiles.html language=enus -->
## TOPIC 04644: ApplicationMgr.EditReadOnlyFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-editreadonlyfiles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-editreadonlyfiles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.EditReadOnlyFiles Data Type Boolean Purpose Specifies whether the TestStand User Interface (UI) Controls allow editing of read-only files. Remarks The value of this property persists in the application configuration file. See Also ApplicationMgr.ConfigFile ApplicationMgr.IsEdit

### ApplicationMgr.EditReadOnlyFiles

#### Syntax

[ApplicationMgr](applicationmgr.html).EditReadOnlyFiles

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the TestStand User Interface (UI) Controls allow editing of read-only files.

#### Remarks

The value of this property persists in the application configuration file.

#### See Also

[ApplicationMgr.ConfigFile](applicationmgr-configfile.html)

[ApplicationMgr.IsEditor](applicationmgr-iseditor.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-endedit.html language=enus -->
## TOPIC 04645: ApplicationMgr.EndEdit

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-endedit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-endedit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_EndEdit( editedFile, editKind, editedObjects, cancelled) Applies To ApplicationMgr Purpose Occurs after an editing action completes or when you explicitly call the ApplicationMgr.EndEdit method. Remarks For each ApplicationMgr.BeginEdit event the application receives, the applicat

### ApplicationMgr.EndEdit

#### Syntax

ControlName_EndEdit( editedFile, editKind, editedObjects, cancelled)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs after an editing action completes or when you explicitly call the
 [ApplicationMgr.EndEdit](applicationmgr-endedit2.html)
 method.

#### Remarks

For each
 [ApplicationMgr.BeginEdit](applicationmgr-beginedit.html)
 event the application receives, the application also receives a corresponding EndEdit event.

#### Parameters

editedFile
 As
 
 [PropertyObjectFile](../tsapiref/propertyobjectfile.html)

[In] Specifies the file being edited.

editKind
 As
 
 [EditKinds](../tsapiref/editkinds.html)

[In] Specifies the type of editing action.

editedObjects
 As
 
 [PropertyObject](../tsapiref/propertyobject.html)

[In] Specifies the edited objects.

cancelled
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] Specifies whether the editing action was cancelled.

#### See Also

[ApplicationMgr.BeginEdit event](applicationmgr-beginedit.html)

[ApplicationMgr.CanEdit event](applicationmgr-canedit.html)

[ApplicationMgr.EndEdit method](applicationmgr-endedit2.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-endedit2.html language=enus -->
## TOPIC 04646: ApplicationMgr.EndEdit

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-endedit2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-endedit2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.EndEdit( editedFile, editKind, editedObjects, cancelled) Purpose Call this method to generate an ApplicationMgr.EndEdit event that notifies the application an edit operation has completed. Call this method once for each call you make to the ApplicationMgr.BeginEdit method. Para

### ApplicationMgr.EndEdit

#### Syntax

[ApplicationMgr](applicationmgr.html).EndEdit( editedFile, editKind, editedObjects, cancelled)

#### Purpose

Call this method to generate an
 [ApplicationMgr.EndEdit](applicationmgr-endedit.html)
 event that notifies the application an edit operation has completed. Call this method once for each call you make to the
 [ApplicationMgr.BeginEdit](applicationmgr-beginedit2.html)
 method.

#### Parameters

editedFile
 As
 
 [PropertyObjectFile](../tsapiref/propertyobjectfile.html)

[In] Specifies the file you are editing.

editKind
 As
 
 [EditKinds](../tsapiref/editkinds.html)

[In] Specifies the kind of edit. Pass the same value you pass to the
 ApplicationMgr.BeginEdit
 method.

editedObjects
 As
 [Object Array](data-types-for-teststand-user-interface.html)

[In] Specifies the edited objects. Pass the same objects you pass to the
 ApplicationMgr.BeginEdit
 method.

cancelled
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] Specifies whether the edit was cancelled. Pass the value you receive from the
 ApplicationMgr.BeginEdit
 method.

#### See Also

[ApplicationMgr.BeginEdit](applicationmgr-beginedit2.html)

[ApplicationMgr.EndEdit event](applicationmgr-endedit.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-endexecution.html language=enus -->
## TOPIC 04647: ApplicationMgr.EndExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-endexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-endexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_EndExecution( exec) Applies To ApplicationMgr Purpose Occurs when an execution ends and the TestStand Engine sends a UIMsg_EndExecution message. Parameters exec As Execution [In] Specifies the execution that has ended. See Also ApplicationMgr.ExecutionClosed ApplicationMgr.StartEx

### ApplicationMgr.EndExecution

#### Syntax

ControlName_EndExecution( exec)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when an execution ends and the TestStand Engine sends a
 UIMsg_EndExecution
 message.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the execution that has ended.

#### See Also

[ApplicationMgr.ExecutionClosed](applicationmgr-executionclosed.html)

[ApplicationMgr.StartExecution](applicationmgr-startexecution.html)

UIMsg_End
 [Execution](../tsapiref/execution.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-executing.html language=enus -->
## TOPIC 04648: ApplicationMgr.Executing

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-executing.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-executing.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.Executing Data Type Boolean Purpose Returns True when an execution is running. See Also ApplicationMgr.Executions Executions

### ApplicationMgr.Executing

#### Syntax

[ApplicationMgr](applicationmgr.html).Executing

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Returns
 True
 when an execution is running.

#### See Also

[ApplicationMgr.Executions](applicationmgr-executions.html)

[Executions](executions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-executionclosed.html language=enus -->
## TOPIC 04649: ApplicationMgr.ExecutionClosed

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-executionclosed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-executionclosed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ExecutionClosed( exec) Applies To ApplicationMgr Purpose Occurs when the Application Manager control closes an execution. Parameters exec As Execution [In] Specifies the execution that has been closed. See Also ApplicationMgr ApplicationMgr.EndExecution

### ApplicationMgr.ExecutionClosed

#### Syntax

ControlName_ExecutionClosed( exec)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when the Application Manager control closes an execution.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the execution that has been closed.

#### See Also

[ApplicationMgr](applicationmgr.html)

[ApplicationMgr.EndExecution](applicationmgr-endexecution.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-executionentrypoints.html language=enus -->
## TOPIC 04650: ApplicationMgr.ExecutionEntryPoints

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-executionentrypoints.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-executionentrypoints.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.ExecutionEntryPoints Data Type EntryPoints Purpose Returns the set of Execution entry points that the station model sequence file defines. The collection includes only entry points that set the Sequence.ShowEntryPointForAllWindows property. Remarks This collection can change wh

### ApplicationMgr.ExecutionEntryPoints

#### Syntax

[ApplicationMgr](applicationmgr.html).ExecutionEntryPoints

#### Data Type

[EntryPoints](entrypoints.html)

#### Purpose

Returns the set of Execution entry points that the station model sequence file defines. The collection includes only entry points that set the
 
 [Sequence.ShowEntryPointForAllWindows](../tsapiref/sequence-showentrypointforallwindows.html)
 property.

#### Remarks

This collection can change when the station model sequence file changes.

#### See Also

[ConfigurationEntryPoints](applicationmgr-configurationentrypoints.html)

[Engine.GetStationModelSequenceFile](../tsapiref/engine-getstationmodelsequencefile.html)

[EntryPoints](entrypoints.html)

[ExecutionViewMgr.ExecutionEntryPoints](executionviewmgr-executionentrypoints.html)

[Sequence.ShowEntryPointForAllWindows](../tsapiref/sequence-showentrypointforallwindows.html)

[SequenceFileViewMgr.ExecutionEntryPoints](sequencefileviewmgr-executionentrypoints.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-executions.html language=enus -->
## TOPIC 04651: ApplicationMgr.Executions

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-executions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-executions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.Executions Data Type Executions Purpose Returns the collection of executions the application creates. Remarks This property eliminates the need to keep an array of open executions. The Application Manager control automatically adds new executions to the collection and removes c

### ApplicationMgr.Executions

#### Syntax

[ApplicationMgr](applicationmgr.html).Executions

#### Data Type

[Executions](executions.html)

#### Purpose

Returns the collection of executions the application creates.

#### Remarks

This property eliminates the need to keep an array of open executions. The Application Manager control automatically adds new executions to the collection and removes closed executions.

#### See Also

[ApplicationMgr.Executing](applicationmgr-executing.html)

[Executions](executions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-exitapplication.html language=enus -->
## TOPIC 04652: ApplicationMgr.ExitApplication

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-exitapplication.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-exitapplication.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ExitApplication Applies To ApplicationMgr Purpose Occurs when the application has completed the shutdown process. Remarks The application responds to this event by exiting. Refer to the ApplicationMgr.Shutdown method for more information about exiting. See Also ApplicationMgr.Shut

### ApplicationMgr.ExitApplication

#### Syntax

ControlName_ExitApplication

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when the application has completed the shutdown process.

#### Remarks

The application responds to this event by exiting. Refer to the
 [ApplicationMgr.Shutdown](applicationmgr-shutdown.html)
 method for more information about exiting.

#### See Also

[ApplicationMgr.Shutdown](applicationmgr-shutdown.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-exitcode.html language=enus -->
## TOPIC 04653: ApplicationMgr.ExitCode

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-exitcode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-exitcode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.ExitCode Data Type Long Purpose Specifies the exit code of a user interface. Remarks The Application Manager control sets the value of this property based on the status of executions and uses the following exit codes to indicate the specified status: Status Exit Code Run-time E

### ApplicationMgr.ExitCode

#### Syntax

[ApplicationMgr](applicationmgr.html).ExitCode

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the exit code of a user interface.

#### Remarks

The Application Manager control sets the value of this property based on the status of executions and uses the following exit codes to indicate the specified status:

| Status | Exit Code |
| --- | --- |
| Run-time Error | the error code of the run-time error |
| Normal Exit | 0 |
| Command-line Error | 1 |
| Sequence Failed | 2 |
| Sequence Terminated | 3 |
| Sequence Aborted | 4 |
| Killed Threads | 5 |

If a run-time error with a non-negative error code occurs, the exit code is -17009 (
 TS_Err_ConvertedErrorCode
 ).

As a user interface developer, set the exit code of the application to this property. The development environment you use determines how you return an exit code in an application. LabVIEW does not support returning exit codes.

If you use a command line to run the user interface, you must use the
 start /wait
 command to obtain the exit code from a user interface, as follows:

start /wait TestExec -Quit -Run MainSequence SequenceFile1.seq

Use the
 –OutputToStdIO
 command-line flag to send additional status information for completed executions to standard output.

#### See Also

[ApplicationMgr.ProcessCommandLine](applicationmgr-processcommandline.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-getautocloseexecution.html language=enus -->
## TOPIC 04654: ApplicationMgr.GetAutoCloseExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-getautocloseexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-getautocloseexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.GetAutoCloseExecution( exec) Return Value Boolean When this method returns True , the execution closes automatically when complete. When this method returns False , the execution does not close automatically. Purpose Returns a Boolean value that indicates whether an execution c

### ApplicationMgr.GetAutoCloseExecution

#### Syntax

[ApplicationMgr](applicationmgr.html).GetAutoCloseExecution( exec)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

When this method returns
 True
 , the execution closes automatically when complete. When this method returns
 False
 , the execution does not close automatically.

#### Purpose

Returns a Boolean value that indicates whether an execution closes automatically when complete.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the execution to obtain the setting from.

#### See Also

[ApplicationMgr.SetAutoCloseExecution](applicationmgr-setautocloseexecution.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-getcaptiontext.html language=enus -->
## TOPIC 04655: ApplicationMgr.GetCaptionText

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-getcaptiontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-getcaptiontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.GetCaptionText( captionSource, longName, formatExpression = "") Return Value String The current text for the caption source you specify. Purpose Returns the current caption text for a caption source in the Application Manager control. Parameters captionSource As CaptionSources

### ApplicationMgr.GetCaptionText

#### Syntax

[ApplicationMgr](applicationmgr.html).GetCaptionText( captionSource, longName, formatExpression = "")

#### Return Value

[String](data-types-for-teststand-user-interface.html)

The current text for the caption source you specify.

#### Purpose

Returns the current caption text for a caption source in the Application Manager control.

#### Parameters

captionSource
 As
 [CaptionSources](captionsources.html)

[In] Specifies the type of caption source to obtain the text from.

longName
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] Specifies whether to return a long or short version of the caption text for certain caption sources. Refer to the
 [CaptionSources](captionsources.html)
 enumeration for more information about determining when this option affects the text and for more information about the difference between the long and short versions of the text.

formatExpression
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies a format expression to evaluate when generating the caption text. For the
 [CaptionSource_MacroExpression](captionsources.html)
 caption source, specify a format expression that evaluates to a string value that contains macros that specify other caption sources. For all other caption sources, specify an expression that evaluates to a string value that contains the characters
 %1
 . The method replaces the
 %1
 characters with the text from the caption source. Pass an empty string to use the default format string for the caption source.

This parameter has a default value of
 ""
 .

#### See Also

[CaptionSources](captionsources.html)

[ExecutionViewMgr.GetCaptionText](executionviewmgr-getcaptiontext.html)

[SequenceFileViewMgr.GetCaptionText](sequencefileviewmgr-getcaptiontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-getcommand.html language=enus -->
## TOPIC 04656: ApplicationMgr.GetCommand

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-getcommand.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-getcommand.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.GetCommand( cmdKind, commandIndex = 0) Return Value Command Command object that represents the command. Purpose Creates a Command object. Parameters cmdKind As CommandKinds [In] Specifies the type of Command object to create. commandIndex As Long [In] Specifies which command in

### ApplicationMgr.GetCommand

#### Syntax

[ApplicationMgr](applicationmgr.html).GetCommand( cmdKind, commandIndex = 0)

#### Return Value

[Command](command.html)

Command object that represents the command.

#### Purpose

Creates a
 [Command](command.html)
 object.

#### Parameters

cmdKind
 As
 [CommandKinds](commandkinds.html)

[In] Specifies the type of Command object to create.

commandIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies which command in the set to return. Use this on sets of commands.

This parameter has a default value of
 0
 .

#### See Also

[ApplicationMgr.NewCommands](applicationmgr-newcommands.html)

[Command](command.html)

[Commands](commands.html)

[ExecutionViewMgr.GetCommand](executionviewmgr-getcommand.html)

[SequenceFileViewMgr.GetCommand](sequencefileviewmgr-getcommand.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-getengine.html language=enus -->
## TOPIC 04657: ApplicationMgr.GetEngine

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-getengine.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-getengine.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.GetEngine Return Value Engine Purpose Returns a reference to the TestStand Engine.

### ApplicationMgr.GetEngine

#### Syntax

[ApplicationMgr](applicationmgr.html).GetEngine

#### Return Value

[Engine](../tsapiref/engine.html)

#### Purpose

Returns a reference to the TestStand Engine.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-getexecutionviewmgr.html language=enus -->
## TOPIC 04658: ApplicationMgr.GetExecutionViewMgr

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-getexecutionviewmgr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-getexecutionviewmgr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.GetExecutionViewMgr( exec) Return Value Object The ExecutionView Manager control that is displaying the execution that is passed in. This method returns NULL when it cannot find an ExecutionView Manager control that displays the specified execution. Purpose Finds the ExecutionV

### ApplicationMgr.GetExecutionViewMgr

#### Syntax

[ApplicationMgr](applicationmgr.html).GetExecutionViewMgr( exec)

#### Return Value

[Object](data-types-for-teststand-user-interface.html)

The ExecutionView Manager control that is displaying the execution that is passed in. This method returns
 NULL
 when it cannot find an ExecutionView Manager control that displays the specified execution.

#### Purpose

Finds the ExecutionView Manager control displaying a particular execution.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the execution with the ExecutionView Manager control you want returned.

#### See Also

[ApplicationMgr.GetSequenceFileViewMgr](applicationmgr-getsequencefileviewmgr.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-getimagename.html language=enus -->
## TOPIC 04659: ApplicationMgr.GetImageName

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-getimagename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-getimagename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.GetImageName( imageSource) Return Value String The current image name for the image source you specify. Purpose Returns the current image name for an image source in the Application Manager control. Use the Images.FindImage method to acquire a reference to the image. Parameters

### ApplicationMgr.GetImageName

#### Syntax

[ApplicationMgr](applicationmgr.html).GetImageName( imageSource)

#### Return Value

[String](data-types-for-teststand-user-interface.html)

The current image name for the image source you specify.

#### Purpose

Returns the current image name for an image source in the Application Manager control. Use the
 
 [Images.FindImage](../tsapiref/images-findimage.html)
 method to acquire a reference to the image.

#### Parameters

imageSource
 As
 [ImageSources](imagesources.html)

[In] Specifies the type of image source from which to obtain an image name.

#### See Also

[Engine.Images](../tsapiref/engine-images.html)

[ExecutionViewMgr.GetImageName](executionviewmgr-getimagename.html)

[Images.FindImage](../tsapiref/images-findimage.html)

[SequenceFileViewMgr.GetImageName](sequencefileviewmgr-getimagename.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-getmodelfile.html language=enus -->
## TOPIC 04660: ApplicationMgr.GetModelFile

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-getmodelfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-getmodelfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.GetModelFile( clientFile, loadIfNotAlreadyLoaded) Return Value SequenceFile Purpose This method returns the process model sequence file the Application Manager control loads for a specified sequence file. Parameters clientFile As SequenceFile [In] Specifies the sequence file wi

### ApplicationMgr.GetModelFile

#### Syntax

[ApplicationMgr](applicationmgr.html).GetModelFile( clientFile, loadIfNotAlreadyLoaded)

#### Return Value

[SequenceFile](../tsapiref/sequencefile.html)

#### Purpose

This method returns the process model sequence file the Application Manager control loads for a specified sequence file.

#### Parameters

clientFile
 As
 
 [SequenceFile](../tsapiref/sequencefile.html)

[In] Specifies the sequence file with the associated process model sequence file you want. When you pass
 NULL
 , this method returns the station model file.

loadIfNotAlreadyLoaded
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] Pass
 True
 to force the Application Manager control to load the model file if the Application Manager control has not already done so. When you pass
 False
 and the Application Manager control has not already loaded the model file, this method returns
 NULL
 .

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-getrunstate.html language=enus -->
## TOPIC 04661: ApplicationMgr.GetRunState

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-getrunstate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-getrunstate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.GetRunState( exec) Return Value ExecutionRunStates Use the following constants with this data type: ExecRunState_Paused –(Value: 2) The execution is suspended. ExecRunState_Running –(Value: 1) The execution is running. ExecRunState_Stopped –(Value: 3) The execution has finished

### ApplicationMgr.GetRunState

#### Syntax

[ApplicationMgr](applicationmgr.html).GetRunState( exec)

#### Return Value

[ExecutionRunStates](../tsapiref/executionrunstates.html)

Use the following constants with this data type:

- ExecRunState_Paused 
 –(Value: 2) The execution is suspended.
- ExecRunState_Running 
 –(Value: 1) The execution is running.
- ExecRunState_Stopped 
 –(Value: 3) The execution has finished executing.

#### Purpose

Returns the run state of an execution.

#### Remarks

The value obtained from this method does not necessarily correspond to the value obtained from the
 
 [Execution.GetStates](../tsapiref/execution-getstates.html)
 method. The
 Execution.GetStates
 method returns the instantaneous state of the execution. This method returns the current state the TestStand User Interface (UI) Controls display.

Note

ExecutionViewMgr.RunState

Execution.GetStates

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the execution on which to operate.

#### See Also

[ApplicationMgr.GetTerminationState](applicationmgr-getterminationstate.html)

[Execution.GetStates](../tsapiref/execution-getstates.html)

[ExecutionViewMgr.RunState](executionviewmgr-runstate.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-getsequencefileviewmgr.html language=enus -->
## TOPIC 04662: ApplicationMgr.GetSequenceFileViewMgr

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-getsequencefileviewmgr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-getsequencefileviewmgr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.GetSequenceFileViewMgr( file) Return Value Object IDispatch pointer to a SequenceFileView Manager control. When a sequence file is not selected in a SequenceFileView Manager control, the return value is NULL . Purpose Finds a SequenceFileView Manager control that has a particul

### ApplicationMgr.GetSequenceFileViewMgr

#### Syntax

[ApplicationMgr](applicationmgr.html).GetSequenceFileViewMgr( file)

#### Return Value

[Object](data-types-for-teststand-user-interface.html)

IDispatch pointer to a SequenceFileView Manager control. When a sequence file is not selected in a SequenceFileView Manager control, the return value is
 NULL
 .

#### Purpose

Finds a SequenceFileView Manager control that has a particular sequence file selected.

#### Parameters

file
 As
 
 [SequenceFile](../tsapiref/sequencefile.html)

[In] Specifies the Sequence file with the SequenceFileView Manager control you want returned.

#### See Also

[ApplicationMgr.GetExecutionViewMgr](applicationmgr-getexecutionviewmgr.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-getterminationstate.html language=enus -->
## TOPIC 04663: ApplicationMgr.GetTerminationState

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-getterminationstate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-getterminationstate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.GetTerminationState( exec) Return Value ExecutionTerminationStates Use the following constants with this data type: ExecTermState_Aborting –(Value: 4) TestStand is aborting the running execution. ExecTermState_KillingThreads –(Value: 5) TestStand is ending the threads in the ex

### ApplicationMgr.GetTerminationState

#### Syntax

[ApplicationMgr](applicationmgr.html).GetTerminationState( exec)

#### Return Value

[ExecutionTerminationStates](../tsapiref/executionterminationstates.html)

Use the following constants with this data type:

- ExecTermState_Aborting 
 –(Value: 4) TestStand is aborting the running execution.
- ExecTermState_KillingThreads 
 –(Value: 5) TestStand is ending the threads in the execution.
- ExecTermState_Normal 
 –(Value: 1) The execution is not terminating.
- ExecTermState_Terminating 
 –(Value: 2) TestStand is terminating the running execution.
- ExecTermState_TerminatingInteractive 
 –(Value: 3) TestStand is terminating the running interactive execution.

#### Purpose

Returns the termination state of an execution.

#### Remarks

The value obtained from this method does not necessarily correspond to the value obtained from the
 
 [Execution.GetStates](../tsapiref/execution-getstates.html)
 method. The
 Execution.GetStates
 method returns the instantaneous state of the execution. This method returns the current state that the TestStand User Interface (UI) Controls display.

Note

ExecutionViewMgr.TerminationState

Execution.GetStates

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the execution on which to operate.

#### See Also

[ApplicationMgr.GetRunState](applicationmgr-getrunstate.html)

[Execution.GetStates](../tsapiref/execution-getstates.html)

[ExecutionViewMgr.TerminationState](executionviewmgr-terminationstate.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-getvisible.html language=enus -->
## TOPIC 04664: ApplicationMgr.GetVisible

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-getvisible.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-getvisible.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.GetVisible( exec) Return Value Boolean Purpose Returns True when the execution is not hidden in the user interface. Hidden executions are not included in an execution list connection you establish to an ExecutionView Manager control unless you set the ExecutionListConnection.Sh

### ApplicationMgr.GetVisible

#### Syntax

[ApplicationMgr](applicationmgr.html).GetVisible( exec)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Returns
 True
 when the execution is not hidden in the user interface. Hidden executions are not included in an execution list connection you establish to an ExecutionView Manager control unless you set the
 [ExecutionListConnection.ShowHiddenExecutions](executionlistconnection-showhiddenexecutions.html)
 property to
 True
 .

#### Remarks

Hidden executions are created using the
 ExecTypeMask_InitiallyHidden
 flag.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the execution to determine whether it is visible.

#### See Also

[ApplicationMgr.SetVisible](applicationmgr-setvisible.html)

[ExecutionListConnection](executionlistconnection.html)

[ExecutionListConnection.ShowHiddenExecutions](executionlistconnection-showhiddenexecutions.html)

[ExecutionTypeMask](../tsapiref/executiontypemask.html)

[ExecutionViewMgr.Connections](executionviewmgr-connections.html)

[ExecutionViewMgrConnections.ExecutionList](executionviewmgrconnections-executionlist.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-iseditor.html language=enus -->
## TOPIC 04665: ApplicationMgr.IsEditor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-iseditor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-iseditor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.IsEditor Data Type Boolean Purpose Specifies whether the TestStand User Interface (UI) Controls allow the user to create and edit sequence files. Set this property to False for a non-editing user interface application. Set this property to True for an application that edits and

### ApplicationMgr.IsEditor

#### Syntax

[ApplicationMgr](applicationmgr.html).IsEditor

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the TestStand User Interface (UI) Controls allow the user to create and edit sequence files. Set this property to
 False
 for a non-editing user interface application. Set this property to
 True
 for an application that edits and saves sequence files.

#### Remarks

When you set this property to
 True
 and you do not have an activated
 
 [license](/csh?context=ts_9050)
 that allows editing, TestStand generates a prompt to activate a license. When you do not have an appropriate license, TestStand generates an error. You can set or clear this property with the
 /editor
 or
 /operatorinterface
 command-line flags. To avoid overriding a value you specify on the command line, set this property to a default value for the application before the application evaluates the command-line arguments. The application evaluates command-line arguments when you call the
 [ApplicationMgr.Start](applicationmgr-start.html)
 method. Use the
 [ApplicationMgr.CommandLineCanChangeEditMode](applicationmgr-commandlinecanchangeeditmode.html)
 property to control whether the application evaluates the
 /editor
 or
 /operatorinterface
 command-line flags.

When you set this property in the designer or set it before you call the
 ApplicationMgr.Start
 method, TestStand verifies the value when you call the
 ApplicationMgr.Start
 method, which returns an error when this property is
 True
 and cannot obtain a license that permits editing. When you set this property after calling the
 ApplicationMgr.Start
 method, the Application Manager control might prompt to activate a license.

#### See Also

[Activating Your Software with the NI License Manager](../tshelp/activating-your-software.html)

[ApplicationMgr.CommandLineCanChangeEditMode](applicationmgr-commandlinecanchangeeditmode.html)

[ApplicationMgr.EditModeShortcutKey](applicationmgr-editmodeshortcutkey.html)

[ApplicationMgr.ProcessCommandLine](applicationmgr-processcommandline.html)

[ApplicationMgr.Start](applicationmgr-start.html)

[TestStand Licensing Options](/csh?context=ts_9050)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-isshuttingdown.html language=enus -->
## TOPIC 04666: ApplicationMgr.IsShuttingDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-isshuttingdown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-isshuttingdown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.IsShuttingDown Data Type Boolean Purpose Returns True when the Application Manager control is shutting down. The Application Manager control shuts down between the time when the ApplicationMgr.Shutdown method is called until the ApplicationMgr.ExitApplication or ApplicationMgr.

### ApplicationMgr.IsShuttingDown

#### Syntax

[ApplicationMgr](applicationmgr.html).IsShuttingDown

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Returns
 True
 when the Application Manager control is shutting down. The Application Manager control shuts down between the time when the
 [ApplicationMgr.Shutdown](applicationmgr-shutdown.html)
 method is called until the
 [ApplicationMgr.ExitApplication](applicationmgr-exitapplication.html)
 or
 [ApplicationMgr.ShutDownCancelled](applicationmgr-shutdowncancelled.html)
 event is called.

#### See Also

[ApplicationMgr.ExitApplication](applicationmgr-exitapplication.html)

[ApplicationMgr.Shutdown](applicationmgr-shutdown.html)

[ApplicationMgr.ShutDownCancelled](applicationmgr-shutdowncancelled.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-isstarted.html language=enus -->
## TOPIC 04667: ApplicationMgr.IsStarted

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-isstarted.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-isstarted.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.IsStarted Data Type Boolean Purpose Returns True when the ApplicationMgr.Start method has been called. Returns False when the Application Manager control has been shutdown. See Also ApplicationMgr.Shutdown ApplicationMgr.Start

### ApplicationMgr.IsStarted

#### Syntax

[ApplicationMgr](applicationmgr.html).IsStarted

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Returns
 True
 when the
 [ApplicationMgr.Start](applicationmgr-start.html)
 method has been called. Returns
 False
 when the Application Manager control has been shutdown.

#### See Also

[ApplicationMgr.Shutdown](applicationmgr-shutdown.html)

[ApplicationMgr.Start](applicationmgr-start.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-localizeallcontrols.html language=enus -->
## TOPIC 04668: ApplicationMgr.LocalizeAllControls

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-localizeallcontrols.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-localizeallcontrols.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.LocalizeAllControls( sectionName) Purpose Calls the Localize method on all loaded TestStand User Interface Controls using a given section name. For each user visible control text string, this method searches for a tag with the same string value in the specified section. When th

### ApplicationMgr.LocalizeAllControls

#### Syntax

[ApplicationMgr](applicationmgr.html).LocalizeAllControls( sectionName)

#### Purpose

Calls the
 Localize
 method on all loaded TestStand User Interface Controls using a given section name.

For each user visible control text string, this method searches for a tag with the same string value in the specified section. When this method finds a control text string that is a tag in the language file, the method replaces the control text string with the value of the tag for the current language.

#### Remarks

Call this control to localize all the controls once they are loaded.

#### Parameters

sectionName
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the name of the section in the language files to use.

#### See Also

[Button.Localize](button-localize.html)

[Label.Localize](label-localize.html)

[ListBar.Localize](listbar-localize.html)

[SequenceView.Localize](sequenceview-localize.html)

[StatusBar.Localize](statusbar-localize.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-login.html language=enus -->
## TOPIC 04669: ApplicationMgr.Login

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-login.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-login.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.Login Purpose Logs in the user by running the LoginLogout Front-End callback sequence. This method does not wait for the callback to execute. Use the ApplicationMgr.UserChanged event to determine whether the login was successful. See Also ApplicationMgr.LoginLogoutRunning Appli

### ApplicationMgr.Login

#### Syntax

[ApplicationMgr](applicationmgr.html).Login

#### Purpose

Logs in the user by running the LoginLogout Front-End callback sequence. This method does not wait for the callback to execute. Use the
 [ApplicationMgr.UserChanged](applicationmgr-userchanged.html)
 event to determine whether the login was successful.

#### See Also

[ApplicationMgr.LoginLogoutRunning](applicationmgr-loginlogoutrunning.html)

[ApplicationMgr.LoginOnStart](applicationmgr-loginonstart.html)

[ApplicationMgr.Logout](applicationmgr-logout.html)

[ApplicationMgr.UserChanged](applicationmgr-userchanged.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-loginlogoutrunning.html language=enus -->
## TOPIC 04670: ApplicationMgr.LoginLogoutRunning

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-loginlogoutrunning.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-loginlogoutrunning.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.LoginLogoutRunning Data Type Boolean Purpose Returns True when the Application Manager control is running a LoginLogout Front-End callback sequence for a user to log in or log out. See Also ApplicationMgr.Login ApplicationMgr.LoginOnStart ApplicationMgr.Logout

### ApplicationMgr.LoginLogoutRunning

#### Syntax

[ApplicationMgr](applicationmgr.html).LoginLogoutRunning

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Returns
 True
 when the Application Manager control is running a LoginLogout Front-End callback sequence for a user to log in or log out.

#### See Also

[ApplicationMgr.Login](applicationmgr-login.html)

[ApplicationMgr.LoginOnStart](applicationmgr-loginonstart.html)

[ApplicationMgr.Logout](applicationmgr-logout.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-loginonstart.html language=enus -->
## TOPIC 04671: ApplicationMgr.LoginOnStart

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-loginonstart.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-loginonstart.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.LoginOnStart Data Type Boolean Purpose When this property is True and the StationOptions.LoginOnStart property is True , the LoginLogout Front-End callback sequence runs when you call the ApplicationMgr.Start method. See Also ApplicationMgr.LoginLogoutRunning ApplicationMgr.Log

### ApplicationMgr.LoginOnStart

#### Syntax

[ApplicationMgr](applicationmgr.html).LoginOnStart

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 and the
 
 [StationOptions.LoginOnStart](../tsapiref/stationoptions-loginonstart.html)
 property is
 True
 , the LoginLogout Front-End callback sequence runs when you call the
 [ApplicationMgr.Start](applicationmgr-start.html)
 method.

#### See Also

[ApplicationMgr.LoginLogoutRunning](applicationmgr-loginlogoutrunning.html)

[ApplicationMgr.LoginOnStart](applicationmgr-loginonstart.html)

[ApplicationMgr.Start](applicationmgr-start.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-loginrunning.html language=enus -->
## TOPIC 04672: ApplicationMgr.LoginRunning

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-loginrunning.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-loginrunning.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.LoginRunning Data Type Boolean Purpose Returns True when the Application Manager control is running the LoginLogout Front-End callback sequence to log in a user. See Also ApplicationMgr.LogoutRunning

### ApplicationMgr.LoginRunning

#### Syntax

[ApplicationMgr](applicationmgr.html).LoginRunning

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Returns
 True
 when the Application Manager control is running the LoginLogout Front-End callback sequence to log in a user.

#### See Also

[ApplicationMgr.LogoutRunning](applicationmgr-logoutrunning.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-logout.html language=enus -->
## TOPIC 04673: ApplicationMgr.Logout

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-logout.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-logout.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.Logout Purpose Logs out the current user by running the LoginLogout Front-End callback sequence. This method does not wait for the callback to execute. Use the ApplicationMgr.UserChanged event to determine whether the logout was successful. See Also ApplicationMgr.Login Applica

### ApplicationMgr.Logout

#### Syntax

[ApplicationMgr](applicationmgr.html).Logout

#### Purpose

Logs out the current user by running the LoginLogout Front-End callback sequence. This method does not wait for the callback to execute. Use the
 [ApplicationMgr.UserChanged](applicationmgr-userchanged.html)
 event to determine whether the logout was successful.

#### See Also

[ApplicationMgr.Login](applicationmgr-login.html)

[ApplicationMgr.LoginLogoutRunning](applicationmgr-loginlogoutrunning.html)

[ApplicationMgr.UserChanged](applicationmgr-userchanged.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-logoutclosesseqfilesandexecs.html language=enus -->
## TOPIC 04674: ApplicationMgr.LogoutClosesSeqFilesAndExecs

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-logoutclosesseqfilesandexecs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-logoutclosesseqfilesandexecs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.LogoutClosesSeqFilesAndExecs Data Type Boolean Purpose When this property is True , the ApplicationMgr.Logout method closes all sequence files and executions before running the LoginLogout Front-End callback. When this property is False , the ApplicationMgr.Logout method does n

### ApplicationMgr.LogoutClosesSeqFilesAndExecs

#### Syntax

[ApplicationMgr](applicationmgr.html).LogoutClosesSeqFilesAndExecs

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 , the
 [ApplicationMgr.Logout](applicationmgr-logout.html)
 method closes all sequence files and executions before running the LoginLogout Front-End callback. When this property is
 False
 , the
 ApplicationMgr.Logout
 method does not close any open sequence files or executions.

#### See Also

[ApplicationMgr.Logout](applicationmgr-logout.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-logoutrunning.html language=enus -->
## TOPIC 04675: ApplicationMgr.LogoutRunning

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-logoutrunning.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-logoutrunning.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.LogoutRunning Data Type Boolean Purpose Returns True when the Application Manager control is running LoginLogout Front-End callback sequence to log out a user. See Also ApplicationMgr.LoginRunning

### ApplicationMgr.LogoutRunning

#### Syntax

[ApplicationMgr](applicationmgr.html).LogoutRunning

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Returns
 True
 when the Application Manager control is running LoginLogout Front-End callback sequence to log out a user.

#### See Also

[ApplicationMgr.LoginRunning](applicationmgr-loginrunning.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-makestepnamesunique.html language=enus -->
## TOPIC 04676: ApplicationMgr.MakeStepNamesUnique

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-makestepnamesunique.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-makestepnamesunique.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.MakeStepNamesUnique Data Type Boolean Purpose When this property is True , the TestStand User Interface Controls ensure that steps you insert into a sequence have names that are unique within the sequence. Remarks The value of this property persists in the application configura

### ApplicationMgr.MakeStepNamesUnique

#### Syntax

[ApplicationMgr](applicationmgr.html).MakeStepNamesUnique

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 , the TestStand User Interface Controls ensure that steps you insert into a sequence have names that are unique within the sequence.

#### Remarks

The value of this property persists in the application configuration file.

#### See Also

[ApplicationMgr.ConfigFile](applicationmgr-configfile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-mrufiles.html language=enus -->
## TOPIC 04677: ApplicationMgr.MRUFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-mrufiles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-mrufiles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.MRUFiles Data Type MRUFiles Purpose Returns a collection of the most recently used (MRU) sequence filenames in the application. See Also MRUFiles

### ApplicationMgr.MRUFiles

#### Syntax

[ApplicationMgr](applicationmgr.html).MRUFiles

#### Data Type

[MRUFiles](mrufiles.html)

#### Purpose

Returns a collection of the most recently used (MRU) sequence filenames in the application.

#### See Also

[MRUFiles](mrufiles.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-newcommands.html language=enus -->
## TOPIC 04678: ApplicationMgr.NewCommands

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-newcommands.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-newcommands.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.NewCommands Return Value Commands A reference to a Commands object. Release this reference when you are finished with it. Purpose Creates an empty Commands collection. Refer to the Command object for more information about Command objects. See Also Command Commands

### ApplicationMgr.NewCommands

#### Syntax

[ApplicationMgr](applicationmgr.html).NewCommands

#### Return Value

[Commands](commands.html)

A reference to a Commands object. Release this reference when you are finished with it.

#### Purpose

Creates an empty
 [Commands](commands.html)
 collection. Refer to the
 [Command](command.html)
 object for more information about Command objects.

#### See Also

[Command](command.html)

[Commands](commands.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-opensequencefile.html language=enus -->
## TOPIC 04679: ApplicationMgr.OpenSequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-opensequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-opensequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.OpenSequenceFile( sequenceFilePath) Return Value SequenceFile Returns the opened sequence file, when successful. When a type conflict occurs when loading the file and the conflict prevents TestStand from opening the file, this method returns NULL . When an error occurs while op

### ApplicationMgr.OpenSequenceFile

#### Syntax

[ApplicationMgr](applicationmgr.html).OpenSequenceFile( sequenceFilePath)

#### Return Value

[SequenceFile](../tsapiref/sequencefile.html)

Returns the opened sequence file, when successful. When a type conflict occurs when loading the file and the conflict prevents TestStand from opening the file, this method returns
 NULL
 . When an error occurs while opening the file, this method throws an exception.

#### Purpose

Opens a sequence file.

#### Remarks

This method adds the sequence file to the
 [SequenceFiles](sequencefiles.html)
 collection and generates the
 [ApplicationMgr.SequenceFileOpened](applicationmgr-sequencefileopened.html)
 and
 [ApplicationMgr.DisplaySequenceFile](applicationmgr-displaysequencefile.html)
 events.

#### Parameters

sequenceFilePath
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the path of the sequence file to load. When you do not pass an absolute path, this method searches for the file using the TestStand
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### See Also

[ApplicationMgr.CloseSequenceFile](applicationmgr-closesequencefile.html)

[ApplicationMgr.DisplaySequenceFile](applicationmgr-displaysequencefile.html)

[ApplicationMgr.OpenSequenceFileDialog](applicationmgr-opensequencefiledialog.html)

[ApplicationMgr.OpenSequenceFilesDialog](applicationmgr-opensequencefilesdialog.html)

[ApplicationMgr.SequenceFileOpened](applicationmgr-sequencefileopened.html)

[SequenceFiles](sequencefiles.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-opensequencefiledialog.html language=enus -->
## TOPIC 04680: ApplicationMgr.OpenSequenceFileDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-opensequencefiledialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-opensequencefiledialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.OpenSequenceFileDialog Return Value SequenceFile Returns the opened sequence file if you open a file. This method returns NULL if you cancel the Open File dialog box. Purpose Launches the Open File dialog box. Remarks This method adds the sequence file to the SequenceFiles coll

### ApplicationMgr.OpenSequenceFileDialog

#### Syntax

[ApplicationMgr](applicationmgr.html).OpenSequenceFileDialog

#### Return Value

[SequenceFile](../tsapiref/sequencefile.html)

Returns the opened sequence file if you open a file. This method returns
 NULL
 if you cancel the Open File dialog box.

#### Purpose

Launches the
 [Open File](../tsref/open-file-dialog-box.html)
 dialog box.

#### Remarks

This method adds the sequence file to the
 [SequenceFiles](sequencefiles.html)
 collection and generates the
 [ApplicationMgr.SequenceFileOpened](applicationmgr-sequencefileopened.html)
 and
 [ApplicationMgr.DisplaySequenceFile](applicationmgr-displaysequencefile.html)
 events.

#### See Also

[ApplicationMgr.CloseSequenceFile](applicationmgr-closesequencefile.html)

[ApplicationMgr.DisplaySequenceFile](applicationmgr-displaysequencefile.html)

[ApplicationMgr.OpenSequenceFile](applicationmgr-opensequencefile.html)

[ApplicationMgr.OpenSequenceFilesDialog](applicationmgr-opensequencefilesdialog.html)

[ApplicationMgr.SequenceFileOpened](applicationmgr-sequencefileopened.html)

[Open File dialog box](../tsref/open-file-dialog-box.html)

[SequenceFiles](sequencefiles.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-opensequencefilesdialog.html language=enus -->
## TOPIC 04681: ApplicationMgr.OpenSequenceFilesDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-opensequencefilesdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-opensequencefilesdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.OpenSequenceFilesDialog Return Value SequenceFiles A collection of the opened sequence files. Purpose Launches an Open File dialog box, in which you can select more than one sequence file. Remarks This method adds the opened sequence files to the SequenceFiles collection and ge

### ApplicationMgr.OpenSequenceFilesDialog

#### Syntax

[ApplicationMgr](applicationmgr.html).OpenSequenceFilesDialog

#### Return Value

[SequenceFiles](sequencefiles.html)

A collection of the opened sequence files.

#### Purpose

Launches an
 [Open File](../tsref/open-file-dialog-box.html)
 dialog box, in which you can select more than one sequence file.

#### Remarks

This method adds the opened sequence files to the
 [SequenceFiles](sequencefiles.html)
 collection and generates the
 [ApplicationMgr.SequenceFileOpened](applicationmgr-sequencefileopened.html)
 event for each opened file and generates the
 [ApplicationMgr.DisplaySequenceFile](applicationmgr-displaysequencefile.html)
 event for the first file opened.

#### See Also

[ApplicationMgr.CloseSequenceFile](applicationmgr-closesequencefile.html)

[ApplicationMgr.DisplaySequenceFile](applicationmgr-displaysequencefile.html)

[ApplicationMgr.OpenSequenceFile](applicationmgr-opensequencefile.html)

[ApplicationMgr.OpenSequenceFileDialog](applicationmgr-opensequencefiledialog.html)

[ApplicationMgr.SequenceFileOpened](applicationmgr-sequencefileopened.html)

[Open File dialog box](../tsref/open-file-dialog-box.html)

[SequenceFiles](sequencefiles.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-postcommandexecute.html language=enus -->
## TOPIC 04682: ApplicationMgr.PostCommandExecute

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-postcommandexecute.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-postcommandexecute.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_PostCommandExecute( command) Applies To ApplicationMgr Purpose Occurs when a caller invokes the Command.Execute method. The event occurs after the Command object performs an action. Parameters command As Command [In] Specifies the command that executed. See Also ApplicationMgr.Pre

### ApplicationMgr.PostCommandExecute

#### Syntax

ControlName_PostCommandExecute( command)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when a caller invokes the
 [Command.Execute](command-execute.html)
 method. The event occurs after the Command object performs an action.

#### Parameters

command
 As
 [Command](command.html)

[In] Specifies the command that executed.

#### See Also

[ApplicationMgr.PreCommandExecute](applicationmgr-precommandexecute.html)

[Command.Execute](command-execute.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-precommandexecute.html language=enus -->
## TOPIC 04683: ApplicationMgr.PreCommandExecute

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-precommandexecute.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-precommandexecute.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_PreCommandExecute( command, cancel) Applies To ApplicationMgr Purpose Occurs when a caller invokes the Command.Execute method. When you return False through the cancel parameter, the Command.Execute method does not perform an action and the ApplicationMgr.PostCommandExecute event

### ApplicationMgr.PreCommandExecute

#### Syntax

ControlName_PreCommandExecute( command, cancel)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when a caller invokes the
 [Command.Execute](command-execute.html)
 method. When you return
 False
 through the
 cancel
 parameter, the
 Command.Execute
 method does not perform an action and the
 [ApplicationMgr.PostCommandExecute](applicationmgr-postcommandexecute.html)
 event does not occur.

#### Parameters

command
 As
 [Command](command.html)

[In] Specifies the command about to execute.

cancel
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In/Out] Set this parameter to
 False
 to prevent the command from executing. When you cancel the command execution, you do not receive an
 [ApplicationMgr.PostCommandExecute](applicationmgr-postcommandexecute.html)
 event.

#### See Also

[ApplicationMgr.PostCommandExecute](applicationmgr-postcommandexecute.html)

[Command.Execute](command-execute.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-processcommandline.html language=enus -->
## TOPIC 04684: ApplicationMgr.ProcessCommandLine

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-processcommandline.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-processcommandline.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.ProcessCommandLine Data Type Boolean Purpose When this property is True , the Application Manager control processes the following switches on the command line: /editor —Enables the application to create and edit sequence files. You must have activated a license that supports cr

### ApplicationMgr.ProcessCommandLine

#### Syntax

[ApplicationMgr](applicationmgr.html).ProcessCommandLine

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 , the Application Manager control processes the following switches on the command line:

- /editor 
 —Enables the application to create and edit sequence files. You must have activated a
 
 license 
 that supports creating and editing sequence files.
- /goto <location> 
 —Instructs the application to display the item the
 <location> 
 property object path specifies, such as
 TestExec.exe C:\example.seq /goto "Seq[\"MainSequence\"].Main[\"Power On\"]" 
 TestExec.exe C:\example.seq /goto "Seq[\"MainSequence\"].Main[\"ID#:JifH4ODTf0y1z7bJne0G7D\"]" 
 TestExec.exe C:\example.seq /goto "Seq[1].Main[4].TS.LoadOpt"
- /operatorinterface 
 —Prevents the application from creating and editing sequence files.
 Note 
 You can use
 /
 or
 -
 to specify a switch. Quotation marks are required for arguments that contain a space, such as
 "Test UUTs"
 and
 "C:\My Documents\Test Sequence.seq"
 .
- /outputToStdIO 
 —Writes the status of completed executions to standard output. When you run a user interface from the command line, the console window displays the text written to standard output.
- /quit 
 —Exits the application once all executions complete.
- /run <sequence> <sequencefile> 
 —Runs the sequence in the sequence file.
- /runEntryPoint <entryPointName> <SequenceFile> 
 —Runs the entry point on the sequence file.
- /setCurrentDir 
 —Sets the current directory to the first directory in the directory history list in the File dialog box. The current directory is the directory the File dialog box initially displays when you open a file. Use this option to set the directory the File dialog box displays to the directory the File dialog box displayed the last time you ran the application. The application sets the current directory after processing the other command-line options.
- /useExisting 
 —Prevents a second instance of the application from running and forwards all command-line arguments to the application that is already running.
- /? 
 —Launches a help dialog box, which contains a list of valid command-line arguments, and then immediately closes.

In addition to the switches, you can provide on the command line sequence filenames to load into the application.

#### Remarks

The
 [ApplicationMgr.ReportError](applicationmgr-reporterror.html)
 event reports errors that might occur while processing the command-line arguments.

Use the
 [ApplicationMgr.ProcessUserCommandLineArguments](applicationmgr-processusercommandlineargument.html)
 event to process command-line arguments the Application Manager control does not recognize as custom command-line arguments.

#### See Also

[ApplicationMgr.CommandLineArguments](applicationmgr-commandlinearguments.html)

[ApplicationMgr.ProcessUserCommandLineArguments](applicationmgr-processusercommandlineargument.html)

[ApplicationMgr.ReportError](applicationmgr-reporterror.html)

[TestStand Licensing Options](/csh?context=ts_9050)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-processusercommandlineargument.html language=enus -->
## TOPIC 04685: ApplicationMgr.ProcessUserCommandLineArguments

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-processusercommandlineargument.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-processusercommandlineargument.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ProcessUserCommandLineArguments( processCommand, arguments, currentArgument, errorProcessing, errorMessage) Applies To ApplicationMgr Purpose Use this event to validate and process command-line arguments you define. Remarks The Application Manager control generates this event whil

### ApplicationMgr.ProcessUserCommandLineArguments

#### Syntax

ControlName_ProcessUserCommandLineArguments( processCommand, arguments, currentArgument, errorProcessing, errorMessage)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Use this event to validate and process command-line arguments you define.

#### Remarks

The Application Manager control generates this event while validating and processing command-line arguments. When the Application Manager control validates the command line, the Application Manager control generates this event for command-line arguments that it does not recognize. For these events, you must validate the unrecognized command-line arguments. In addition, when the Application Manager control processes the command line, the Application Manager control generates this event again for command-line arguments that it does not recognize. For these events, you must perform the action that the arguments require. Use the
 processCommand
 parameter of this event to determine whether you must perform the action that the arguments requires.

#### Parameters

processCommand
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] The Application Manager control passes
 False
 to this parameter when the control is only validating and not actually processing the command line. When this parameter is
 False
 , handle this event the same as when this parameter is
 True
 , without performing the action the command-line specifies.

arguments
 As
 
 [Strings](strings.html)

[In] Specifies the command-line arguments passed to the application.

currentArgument
 As
 [Long](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the index into arguments of the command-line argument the Application Manager control does not recognize. Increment this parameter for every argument you process. The Application Manager control continues processing the command-line arguments at this parameter when this event returns.

errorProcessing
 As
 [ProcessCommandLineErrors](processcommandlineerrors.html)

[In/Out] The Application Manager control initializes this parameter to
 ProcessCommandLineError_None
 . Set this parameter to
 ProcessCommandLineError_UnrecognizedArgumentError
 when you do not recognize the command-line argument. Set this parameter to
 ProcessCommandLineError_CustomError
 when you encounter any other error processing the command line. The Application Manager control stops processing the command line and generates the
 [ReportError](applicationmgr-reporterror.html)
 event when an error occurs while processing the command line.

errorMessage
 As
 [String](data-types-for-teststand-user-interface.html)

[In/Out] When you set the
 errorProcessing
 parameter to
 ProcessCommandLineError_CustomError
 , set this parameter to a custom error message.

#### See Also

[ApplicationMgr.AddCommandLineArgumentsHelp](applicationmgr-addcommandlineargumentshelp.html)

[ApplicationMgr.ProcessCommandLine](applicationmgr-processcommandline.html)

[ApplicationMgr.ReportError](applicationmgr-reporterror.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-processusercommands.html language=enus -->
## TOPIC 04686: ApplicationMgr.ProcessUserCommands

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-processusercommands.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-processusercommands.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ProcessUserCommands( cmds) Applies To ApplicationMgr Purpose This event is obsolete. Use the ApplicationMgr.ProcessUserCommandLineArguments event instead. Remarks Use this event to process custom command-line arguments. This event occurs when the ApplicationMgr.Start method is cal

### ApplicationMgr.ProcessUserCommands

#### Syntax

ControlName_ProcessUserCommands( cmds)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Note

ApplicationMgr.ProcessUserCommandLineArguments

#### Remarks

Use this event to process custom command-line arguments. This event occurs when the
 [ApplicationMgr.Start](applicationmgr-start.html)
 method is called and when another instance of the application is executed with the
 /useExisting
 command-line switch. This event occurs before the Application Manager control processes any command-line arguments.

#### Parameters

cmds
 As
 
 [Strings](strings.html)

[In] Specifies the user command-line arguments. This collection is created by splitting up the command line used to start the application using white space as a delimiter. When the
 [ApplicationMgr.ProcessCommandLine](applicationmgr-processcommandline.html)
 property is
 True
 , the first argument the Application Manager control does not recognize marks the start of the user arguments. When the
 ApplicationMgr.ProcessCommandLine
 property is
 False
 , all arguments are user arguments.

#### See Also

[ApplicationMgr.ProcessCommandLine](applicationmgr-processcommandline.html)

[ApplicationMgr.ProcessUserCommandLineArguments](applicationmgr-processusercommandlineargument.html)

[ApplicationMgr.Start](applicationmgr-start.html)

Parent topic:

Obsolete ApplicationMgr Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-promptforoverwrite.html language=enus -->
## TOPIC 04687: ApplicationMgr.PromptForOverwrite

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-promptforoverwrite.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-promptforoverwrite.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.PromptForOverwrite Data Type PerformActionOptions Use the following constants with this data type: PerformActionOption_No –(Value: 1) Specifies to not perform an action. PerformActionOption_Prompt –(Value: 2) Specifies to prompt the user to determine whether to perform an actio

### ApplicationMgr.PromptForOverwrite

#### Syntax

[ApplicationMgr](applicationmgr.html).PromptForOverwrite

#### Data Type

[PerformActionOptions](../tsapiref/performactionoptions.html)

Use the following constants with this data type:

- PerformActionOption_No 
 –(Value: 1) Specifies to not perform an action.
- PerformActionOption_Prompt 
 –(Value: 2) Specifies to prompt the user to determine whether to perform an action.
- PerformActionOption_Yes 
 –(Value: 0) Specifies to perform an action without prompting the user.

#### Purpose

Specifies whether the Application Manager control makes a backup of a file when you save a sequence file over an existing file that has an older or newer format. When this property is
 PerformActionOption_Yes
 , the Application Manager control backs up the existing file before saving it. When this property is
 PerformActionOption_No
 , the Application Manager control saves over the existing file without backing it up. When this property is
 PerformActionOption_Prompt
 , the Application Manager control prompts you to choose whether to back up the existing file.

#### Remarks

The value of this property persists in the application configuration file.

#### See Also

[ApplicationMgr.ConfigFile](applicationmgr-configfile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-querycloseexecution.html language=enus -->
## TOPIC 04688: ApplicationMgr.QueryCloseExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-querycloseexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-querycloseexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_QueryCloseExecution( exec, runState, opt) Applies To ApplicationMgr Purpose Occurs when the Application Manager control is attempting to close an execution. Remarks Calls to the ApplicationMgr.Shutdown , ApplicationMgr.CloseExecution , and ApplicationMgr.CloseAllExecutions methods

### ApplicationMgr.QueryCloseExecution

#### Syntax

ControlName_QueryCloseExecution( exec, runState, opt)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when the Application Manager control is attempting to close an execution.

#### Remarks

Calls to the
 [ApplicationMgr.Shutdown](applicationmgr-shutdown.html)
 ,
 [ApplicationMgr.CloseExecution](applicationmgr-closeexecution.html)
 , and
 [ApplicationMgr.CloseAllExecutions](applicationmgr-closeallexecutions.html)
 methods result in closing executions and calling this event.

You can use this event to inform the user that an execution is closing and to allow the user to confirm that this is the desired action.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the execution about to be closed.

runState
 As
 
 [ExecutionRunStates](../tsapiref/executionrunstates.html)

[In] Specifies the run state of the execution.

opt
 As
 [QueryCloseExecutionOptions](querycloseexecutionoptions.html)

[In/Out] Specifies to cancel the closing of the execution; automatically close, abort, or terminate the running execution; or prompt the user for action. Refer to the
 [QueryCloseExecutionOptions](querycloseexecutionoptions.html)
 enumeration for more information about options for closing executions.

#### See Also

[ApplicationMgr.CloseAllExecutions](applicationmgr-closeallexecutions.html)

[ApplicationMgr.CloseExecution](applicationmgr-closeexecution.html)

[ApplicationMgr.Shutdown](applicationmgr-shutdown.html)

[QueryCloseExecutionOptions](querycloseexecutionoptions.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-queryclosesequencefile.html language=enus -->
## TOPIC 04689: ApplicationMgr.QueryCloseSequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-queryclosesequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-queryclosesequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_QueryCloseSequenceFile( file, cancel) Applies To ApplicationMgr Purpose Occurs before a sequence file is closed. Remarks Use this event to prompt the user for confirmation on closing the sequence file or to stop the sequence file from closing. Parameters file As SequenceFile [In]

### ApplicationMgr.QueryCloseSequenceFile

#### Syntax

ControlName_QueryCloseSequenceFile( file, cancel)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs before a sequence file is closed.

#### Remarks

Use this event to prompt the user for confirmation on closing the sequence file or to stop the sequence file from closing.

#### Parameters

file
 As
 
 [SequenceFile](../tsapiref/sequencefile.html)

[In] Specifies the sequence file that is closing.

cancel
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In/Out] Set this parameter to
 True
 when you want to stop the sequence file from closing.

#### See Also

[ApplicationMgr.CloseAllSequenceFiles](applicationmgr-closeallsequencefiles.html)

[ApplicationMgr.CloseSequenceFile](applicationmgr-closesequencefile.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-queryreloadsequencefile.html language=enus -->
## TOPIC 04690: ApplicationMgr.QueryReloadSequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-queryreloadsequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-queryreloadsequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_QueryReloadSequenceFile( file, opt) Applies To ApplicationMgr Purpose Occurs when the Application Manager control wants to reload a modified sequence file because you called the ApplicationMgr.ReloadModifiedSequenceFiles method or because the Application Manager control detected a

### ApplicationMgr.QueryReloadSequenceFile

#### Syntax

ControlName_QueryReloadSequenceFile( file, opt)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when the Application Manager control wants to reload a modified sequence file because you called the
 [ApplicationMgr.ReloadModifiedSequenceFiles](applicationmgr-reloadmodifiedsequencefiles.html)
 method or because the Application Manager control detected a modified sequence file.

#### Remarks

Use this event to customize how the application prompts the user to reload the modified sequence file or to reload or ignore modified sequence files without prompting the user.

#### Parameters

file
 As
 
 [SequenceFile](../tsapiref/sequencefile.html)

[In] Specifies the sequence file to reload.

opt
 As
 [QueryReloadSequenceFileOptions](queryreloadsequencefileoptions.html)

[In/Out] Use
 [QueryReloadSequenceFileOptions](queryreloadsequencefileoptions.html)
 with this parameter. This parameter is initialized to
 QueryReloadSequenceFile_Prompt
 . You can change the value of this parameter to make the Application Manager control reload or discard the modified file without prompting the user.

#### See Also

[ApplicationMgr.AutomaticallyReloadModifiedFiles](applicationmgr-automaticallyreloadmodifiedfil.html)

[ApplicationMgr.ReloadModifiedFilesInterval](applicationmgr-reloadmodifiedfilesinterval.html)

[ApplicationMgr.ReloadModifiedSequenceFilesEx](applicationmgr-reloadmodifiedsequencefilesex.html)

[QueryReloadSequenceFileOptions](queryreloadsequencefileoptions.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-queryshutdown.html language=enus -->
## TOPIC 04691: ApplicationMgr.QueryShutdown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-queryshutdown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-queryshutdown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_QueryShutdown( opt) Applies To ApplicationMgr Purpose Occurs before the Application Manager control initiates a shutdown. Parameters opt As QueryShutdownOptions [In/Out] Refer to the QueryShutdownOptions enumeration for more information about constants with this parameter. See Als

### ApplicationMgr.QueryShutdown

#### Syntax

ControlName_QueryShutdown( opt)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs before the Application Manager control initiates a shutdown.

#### Parameters

opt
 As
 [QueryShutdownOptions](queryshutdownoptions.html)

[In/Out] Refer to the
 [QueryShutdownOptions](queryshutdownoptions.html)
 enumeration for more information about constants with this parameter.

#### See Also

[ApplicationMgr.Shutdown](applicationmgr-shutdown.html)

[QueryShutdownOptions](queryshutdownoptions.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-raiseerror.html language=enus -->
## TOPIC 04692: ApplicationMgr.RaiseError

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-raiseerror.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-raiseerror.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.RaiseError( errorCode, errorMessage) Purpose Generates an ApplicationMgr.ReportError event. Remarks Typically, an application handles the ReportError event to display or log errors that occur during the operation of the TestStand User Interface Controls. An application can reus

### ApplicationMgr.RaiseError

#### Syntax

[ApplicationMgr](applicationmgr.html).RaiseError( errorCode, errorMessage)

#### Purpose

Generates an
 [ApplicationMgr.ReportError](applicationmgr-reporterror.html)
 event.

#### Remarks

Typically, an application handles the
 [ReportError](applicationmgr-reporterror.html)
 event to display or log errors that occur during the operation of the TestStand User Interface Controls. An application can reuse this event handler to report other errors by calling this method.

#### Parameters

errorCode
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the integer error code.

errorMessage
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the descriptive error string.

#### See Also

[ApplicationMgr.ReportError](applicationmgr-reporterror.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-refresh.html language=enus -->
## TOPIC 04693: ApplicationMgr.Refresh

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-refresh.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-refresh.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.Refresh( opts = RefreshOption_All) Purpose Refreshes the specified connected controls. Parameters opts As Long [In] Specifies any combination of RefreshOptions . This parameter has a default value of RefreshOption_All . See Also ApplicationMgr.RefreshAllViewMgrs ExecutionViewMg

### ApplicationMgr.Refresh

#### Syntax

[ApplicationMgr](applicationmgr.html).Refresh( opts = RefreshOption_All)

#### Purpose

Refreshes the specified connected controls.

#### Parameters

opts
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies any combination of
 [RefreshOptions](refreshoptions.html)
 .

This parameter has a default value of
 RefreshOption_All
 .

#### See Also

[ApplicationMgr.RefreshAllViewMgrs](applicationmgr-refreshallviewmgrs.html)

[ExecutionViewMgr.Refresh](executionviewmgr-refresh.html)

[RefreshOptions](refreshoptions.html)

[SequenceFileViewMgr.Refresh](sequencefileviewmgr-refresh.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-refreshallviewmgrs.html language=enus -->
## TOPIC 04694: ApplicationMgr.RefreshAllViewMgrs

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-refreshallviewmgrs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-refreshallviewmgrs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.RefreshAllViewMgrs Purpose Refreshes all connected controls for all manager controls. See Also ApplicationMgr.Refresh ExecutionViewMgr.Refresh SequenceFileViewMgr.Refresh

### ApplicationMgr.RefreshAllViewMgrs

#### Syntax

[ApplicationMgr](applicationmgr.html).RefreshAllViewMgrs

#### Purpose

Refreshes all connected controls for all manager controls.

#### See Also

[ApplicationMgr.Refresh](applicationmgr-refresh.html)

[ExecutionViewMgr.Refresh](executionviewmgr-refresh.html)

[SequenceFileViewMgr.Refresh](sequencefileviewmgr-refresh.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-refreshfile.html language=enus -->
## TOPIC 04695: ApplicationMgr.RefreshFile

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-refreshfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-refreshfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.RefreshFile( file, opts = RefreshOption_All) Purpose Performs a refresh operation on every SequenceFileView Manager control that currently displays the specified file. Remarks Parameters file As PropertyObjectFile [In] Specifies the PropertyObjectFile reference for a TestStand

### ApplicationMgr.RefreshFile

#### Syntax

[ApplicationMgr](applicationmgr.html).RefreshFile( file, opts = RefreshOption_All)

#### Purpose

Performs a refresh operation on every
 [SequenceFileView Manager](sequencefileviewmgr.html)
 control that currently displays the specified file.

#### Remarks

#### Parameters

file
 As
 
 [PropertyObjectFile](../tsapiref/propertyobjectfile.html)

[In] Specifies the
 
 [PropertyObjectFile](../tsapiref/propertyobjectfile.html)
 reference for a TestStand sequence file.

opts
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Do not pass a value or pass
 RefreshOption_All (0xFFFFFFFF)
 to this reserved parameter.

This parameter has a default value of
 RefreshOption_All
 .

#### See Also

[PropertyObjectFile](../tsapiref/propertyobjectfile.html)

[SequenceFileViewMgr](sequencefileviewmgr.html)

[SequenceFileViewMgr.Refresh](sequencefileviewmgr-refresh.html)

[SequenceFileViewMgr.SequenceFile](sequencefileviewmgr-sequencefile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-refreshwindows.html language=enus -->
## TOPIC 04696: ApplicationMgr.RefreshWindows

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-refreshwindows.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-refreshwindows.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_RefreshWindows( activeXData) Applies To ApplicationMgr Purpose Occurs when a UIMsg_RefreshWindows UIMessage posts. Handle this event to refresh custom controls as needed. Remarks A step or callback sequence typically posts the UIMsg_RefreshWindows UIMessage to force a refresh, suc

### ApplicationMgr.RefreshWindows

#### Syntax

ControlName_RefreshWindows( activeXData)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when a
 UIMsg_RefreshWindows
 UIMessage posts. Handle this event to refresh custom controls as needed.

#### Remarks

A step or callback sequence typically posts the
 UIMsg_RefreshWindows
 UIMessage to force a refresh, such as updating the status of a step in the Execution view when TestStand does not normally update it.

#### Parameters

activeXData
 As
 [IUnknown](data-types-for-teststand-user-interface.html)

[In] Specifies the ActiveXData of the UIMessage object. Specify
 NULL
 to refresh data for all files and executions. Specify a
 
 [PropertyObjectFile](../tsapiref/propertyobjectfile.html)
 to refresh the data of a specific file. Specify a
 
 [SequenceContext](../tsapiref/sequencecontext.html)
 to refresh the SequenceContext of an execution. You can also specify an Object Reference Array that contains multiple values.

#### See Also

[ExecutionViewMgr.RefreshWindow](executionviewmgr-refreshwindow.html)

[PropertyObjectFile](../tsapiref/propertyobjectfile.html)

[SequenceContext](../tsapiref/sequencecontext.html)

[SequenceFileViewMgr.RefreshWindow](sequencefileviewmgr-refreshwindow.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-reloadconfigfile.html language=enus -->
## TOPIC 04697: ApplicationMgr.ReloadConfigFile

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-reloadconfigfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-reloadconfigfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.ReloadConfigFile Purpose Reloads the application configuration file from disk. Remarks Unlike sequences files, the application configuration file does not automatically reload when an external application, such as a source control system, modifies the file. You can call this me

### ApplicationMgr.ReloadConfigFile

#### Syntax

[ApplicationMgr](applicationmgr.html).ReloadConfigFile

#### Purpose

Reloads the application configuration file from disk.

#### Remarks

Unlike sequences files, the application configuration file does not automatically reload when an external application, such as a source control system, modifies the file. You can call this method to force the configuration file to reload.

#### See Also

[ApplicationMgr.ConfigFile](applicationmgr-configfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-reloadfile.html language=enus -->
## TOPIC 04698: ApplicationMgr.ReloadFile

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-reloadfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-reloadfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.ReloadFile( file, options = 0) Return Value Boolean Returns True when the file was reloaded. This method returns False when the TestStand Engine cannot unload the file, when an ApplicationMgr.QueryReloadSequenceFile event cancels the operation, or when TestStand prompts the use

### ApplicationMgr.ReloadFile

#### Syntax

[ApplicationMgr](applicationmgr.html).ReloadFile( file, options = 0)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when the file was reloaded. This method returns
 False
 when the TestStand Engine cannot unload the file, when an
 [ApplicationMgr.QueryReloadSequenceFile](applicationmgr-queryreloadsequencefile.html)
 event cancels the operation, or when TestStand prompts the user and the user cancels the operation.

#### Purpose

Reloads the specified file.

When the file is reloaded, this method returns a reference to the newly loaded version of the file in the file parameter. This method supports only sequence files the Application Manager control opens. For all other files, this method returns
 False
 .

#### Remarks

TestStand generates an
 [ApplicationMgr.QueryReloadSequenceFile](applicationmgr-queryreloadsequencefile.html)
 event to allow the application to cancel the reload operation or specify to prompt the user to reload the file.

When you specify
 [ReloadFileOption_NoOptions](reloadfileoptions.html)
 for the
 options
 parameter for this method and an
 ApplicationMgr.QueryReloadSequenceFile
 event does not alter the
 opt
 parameter of the event, TestStand does not prompt to reload the file.

When you specify
 [ReloadFileOption_OnlyIfModifiedInMemory](reloadfileoptions.html)
 or
 [ReloadFileOption_OnlyIfModifiedOnDisk](reloadfileoptions.html)
 for the
 options
 parameter to this method and an
 ApplicationMgr.QueryReloadSequenceFile
 event does not alter the
 opt
 parameter of the event, TestStand prompts the user to reload the file.

#### Parameters

file
 As
 
 [PropertyObjectFile](../tsapiref/propertyobjectfile.html)

[In/Out] Specifies a reference to the file you want to reload. The reference changes to the reloaded version of the file when TestStand reloads the file.

options
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies one or more
 [ReloadFileOptions](reloadfileoptions.html)
 constants. Use the bitwise-OR operator to specify multiple options. Pass
 0
 to reload the file unconditionally.

This parameter has a default value of
 0
 .

#### See Also

[ApplicationMgr.QueryReloadSequenceFile event](applicationmgr-queryreloadsequencefile.html)

[ApplicationMgr.AutomaticallyReloadModifiedFiles](applicationmgr-automaticallyreloadmodifiedfil.html)

[ApplicationMgr.ReloadModifiedSequenceFilesEx](applicationmgr-reloadmodifiedsequencefilesex.html)

[ReloadFileOptions](reloadfileoptions.html)

[SequenceFile.CanUnload](../tsapiref/sequencefile-canunload.html)

[SequenceFile.IsExecuting](../tsapiref/sequencefile-isexecuting.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-reloadmodifiedfilesinterval.html language=enus -->
## TOPIC 04699: ApplicationMgr.ReloadModifiedFilesInterval

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-reloadmodifiedfilesinterval.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-reloadmodifiedfilesinterval.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.ReloadModifiedFilesInterval Data Type Long Purpose Specifies the interval, in seconds, at which the Application Manager control calls the ApplicationMgr.ReloadModifiedSequenceFilesEx method. When the value is 0 , the Application Manager control does not reload any modified sequ

### ApplicationMgr.ReloadModifiedFilesInterval

#### Syntax

[ApplicationMgr](applicationmgr.html).ReloadModifiedFilesInterval

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the interval, in seconds, at which the Application Manager control calls the
 [ApplicationMgr.ReloadModifiedSequenceFilesEx](applicationmgr-reloadmodifiedsequencefilesex.html)
 method. When the value is
 0
 , the Application Manager control does not reload any modified sequence files.

#### Remarks

The default value is 3 seconds.

#### See Also

[ApplicationMgr.AutomaticallyReloadModifiedFiles](applicationmgr-automaticallyreloadmodifiedfil.html)

[ApplicationMgr.QueryReloadSequenceFile](applicationmgr-queryreloadsequencefile.html)

[ApplicationMgr.ReloadModifiedSequenceFilesEx](applicationmgr-reloadmodifiedsequencefilesex.html)

[QueryReloadSequenceFileOptions](queryreloadsequencefileoptions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-reloadmodifiedsequencefiles.html language=enus -->
## TOPIC 04700: ApplicationMgr.ReloadModifiedSequenceFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-reloadmodifiedsequencefiles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-reloadmodifiedsequencefiles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.ReloadModifiedSequenceFiles Purpose This method is obsolete. Use the ReloadModifiedSequenceFilesEx method instead. Remarks Determines whether loaded sequence files have been modified on disk and generates an ApplicationMgr.QueryReloadSequenceFile event to determine whether to p

### ApplicationMgr.ReloadModifiedSequenceFiles

#### Syntax

[ApplicationMgr](applicationmgr.html).ReloadModifiedSequenceFiles

#### Purpose

Note

ReloadModifiedSequenceFilesEx

#### Remarks

Determines whether loaded sequence files have been modified on disk and generates an
 [ApplicationMgr.QueryReloadSequenceFile](applicationmgr-queryreloadsequencefile.html)
 event to determine whether to prompt you to reload any modified files.

This method also refreshes the read-only state of open sequence files and updates the
 [ApplicationMgr.ConfigurationEntryPoints](applicationmgr-configurationentrypoints.html)
 and
 [ApplicationMgr.ExecutionEntryPoints](applicationmgr-executionentrypoints.html)
 properties. Use the
 [ApplicationMgr.ReloadFile](applicationmgr-reloadfile.html)
 method to reload a specific file.

#### See Also

[ApplicationMgr.AutomaticallyReloadModifiedFiles](applicationmgr-automaticallyreloadmodifiedfil.html)

[ApplicationMgr.ConfigurationEntryPoints](applicationmgr-configurationentrypoints.html)

[ApplicationMgr.ExecutionEntryPoints](applicationmgr-executionentrypoints.html)

[ApplicationMgr.QueryReloadSequenceFile](applicationmgr-queryreloadsequencefile.html)

[ApplicationMgr.ReloadFile](applicationmgr-reloadfile.html)

[ApplicationMgr.ReloadModifiedFilesInterval](applicationmgr-reloadmodifiedfilesinterval.html)

Parent topic:

Obsolete ApplicationMgr Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-reloadmodifiedsequencefilesex.html language=enus -->
## TOPIC 04701: ApplicationMgr.ReloadModifiedSequenceFilesEx

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-reloadmodifiedsequencefilesex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-reloadmodifiedsequencefilesex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.ReloadModifiedSequenceFilesEx Return Value Boolean Returns True if this method reloads a sequence file. Purpose Determines whether loaded sequence files have been modified on disk and generates an ApplicationMgr.QueryReloadSequenceFile event to determine whether to prompt you t

### ApplicationMgr.ReloadModifiedSequenceFilesEx

#### Syntax

[ApplicationMgr](applicationmgr.html).ReloadModifiedSequenceFilesEx

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 if this method reloads a sequence file.

#### Purpose

Determines whether loaded sequence files have been modified on disk and generates an
 [ApplicationMgr.QueryReloadSequenceFile](applicationmgr-queryreloadsequencefile.html)
 event to determine whether to prompt you to reload any modified files.

#### Remarks

This method also refreshes the read-only state of open sequence files and updates the
 [ApplicationMgr.ConfigurationEntryPoints](applicationmgr-configurationentrypoints.html)
 and
 [ApplicationMgr.ExecutionEntryPoints](applicationmgr-executionentrypoints.html)
 properties. Use the
 [ApplicationMgr.ReloadFile](applicationmgr-reloadfile.html)
 method to reload a specific file.

#### See Also

[ApplicationMgr.AutomaticallyReloadModifiedFiles](applicationmgr-automaticallyreloadmodifiedfil.html)

[ApplicationMgr.ConfigurationEntryPoints](applicationmgr-configurationentrypoints.html)

[ApplicationMgr.ExecutionEntryPoints](applicationmgr-executionentrypoints.html)

[ApplicationMgr.QueryReloadSequenceFile](applicationmgr-queryreloadsequencefile.html)

[ApplicationMgr.ReloadFile](applicationmgr-reloadfile.html)

[ApplicationMgr.ReloadModifiedFilesInterval](applicationmgr-reloadmodifiedfilesinterval.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-reloadsequencefilesonstart.html language=enus -->
## TOPIC 04702: ApplicationMgr.ReloadSequenceFilesOnStart

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-reloadsequencefilesonstart.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-reloadsequencefilesonstart.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.ReloadSequenceFilesOnStart Data Type ReloadFiles Use the following constants with this data type: ReloadFile_All –(Value: 2) Reloads all files. ReloadFile_None –(Value: 0) Does not reload any files. ReloadFile_Selected –(Value: 1) Reloads any file selected in a SequenceFileView

### ApplicationMgr.ReloadSequenceFilesOnStart

#### Syntax

[ApplicationMgr](applicationmgr.html).ReloadSequenceFilesOnStart

#### Data Type

[ReloadFiles](reloadfiles.html)

Use the following constants with this data type:

- ReloadFile_All 
 –(Value: 2) Reloads all files.
- ReloadFile_None 
 –(Value: 0) Does not reload any files.
- ReloadFile_Selected 
 –(Value: 1) Reloads any file selected in a
 SequenceFileView Manager 
 control.

#### Purpose

Specifies which files to reload when the application starts.

#### Remarks

A value of
 ReloadFile_None
 results in nothing being reloaded on start. A value of
 ReloadFile_Selected
 makes the
 [ApplicationMgr.Start](applicationmgr-start.html)
 method reload all files selected in any SequenceFileView Manager controls the last time the
 [ApplicationMgr.Shutdown](applicationmgr-shutdown.html)
 method was called. A value of
 ReloadFile_All
 makes the
 ApplicationMgr.Start
 method reload all files that were open when the
 ApplicationMgr.Shutdown
 method was last called.

The files load after the first time a user logs in.

#### See Also

[ApplicationMgr.LoginOnStart](applicationmgr-loginonstart.html)

[ApplicationMgr.ReloadFile](applicationmgr-reloadfile.html)

[ApplicationMgr.Shutdown](applicationmgr-shutdown.html)

[ApplicationMgr.Start](applicationmgr-start.html)

[SequenceFileViewMgr](sequencefileviewmgr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-reporterror.html language=enus -->
## TOPIC 04703: ApplicationMgr.ReportError

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-reporterror.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-reporterror.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ReportError( errorCode, errorMessage) Applies To ApplicationMgr Purpose Occurs when an error is reported. This event notifies the application of errors that occur while the user operates connected controls. This event is also called when the ApplicationMgr.RaiseError method is cal

### ApplicationMgr.ReportError

#### Syntax

ControlName_ReportError( errorCode, errorMessage)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when an error is reported. This event notifies the application of errors that occur while the user operates connected controls. This event is also called when the
 [ApplicationMgr.RaiseError](applicationmgr-raiseerror.html)
 method is called.

#### Remarks

Use this event to display an error message to the user of the user interface.

#### Parameters

errorCode
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the error code for the error that caused the event.

errorMessage
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the descriptive error string.

#### See Also

[ApplicationMgr.RaiseError](applicationmgr-raiseerror.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-saveonclose.html language=enus -->
## TOPIC 04704: ApplicationMgr.SaveOnClose

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-saveonclose.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-saveonclose.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.SaveOnClose Data Type PerformActionOptions Use the following constants with this data type: PerformActionOption_No –(Value: 1) Specifies to not perform an action. PerformActionOption_Prompt –(Value: 2) Specifies to prompt the user to determine whether to perform an action. Perf

### ApplicationMgr.SaveOnClose

#### Syntax

[ApplicationMgr](applicationmgr.html).SaveOnClose

#### Data Type

[PerformActionOptions](../tsapiref/performactionoptions.html)

Use the following constants with this data type:

- PerformActionOption_No 
 –(Value: 1) Specifies to not perform an action.
- PerformActionOption_Prompt 
 –(Value: 2) Specifies to prompt the user to determine whether to perform an action.
- PerformActionOption_Yes 
 –(Value: 0) Specifies to perform an action without prompting the user.

#### Purpose

Specifies whether the Application Manager control saves a modified file when you close the modified file. When this property is
 PerformActionOption_Yes
 , the Application Manager control saves the file. When this property is
 PerformActionOption_No
 , the Application Manager control discards the file without saving the file. When this property is
 PerformActionOption_Prompt
 , the Application Manager control prompts you to choose whether to save the file.

#### Remarks

The value of this property persists in the application configuration file.

#### See Also

[ApplicationMgr.ConfigFile](applicationmgr-configfile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-sequencefileclosed.html language=enus -->
## TOPIC 04705: ApplicationMgr.SequenceFileClosed

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-sequencefileclosed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-sequencefileclosed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_SequenceFileClosed( pathName) Applies To ApplicationMgr Purpose This event is obsolete. Use the ApplicationMgr.SequenceFileClosing event instead. Remarks Occurs when the application has closed a sequence file. You can use this event, but unsaved sequence files always pass in an em

### ApplicationMgr.SequenceFileClosed

#### Syntax

ControlName_SequenceFileClosed( pathName)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Note

ApplicationMgr.SequenceFileClosing

#### Remarks

Occurs when the application has closed a sequence file. You can use this event, but unsaved sequence files always pass in an empty string for the
 pathName
 parameter so no method exists for distinguishing the files.

#### Parameters

pathName
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the path of the closed sequence file.

#### See Also

[ApplicationMgr.CloseAllSequenceFiles](applicationmgr-closeallsequencefiles.html)

[ApplicationMgr.CloseSequenceFile](applicationmgr-closesequencefile.html)

[ApplicationMgr.QueryCloseSequenceFile](applicationmgr-queryclosesequencefile.html)

[ApplicationMgr.SequenceFileClosing](applicationmgr-sequencefileclosing.html)

Parent topic:

Obsolete ApplicationMgr Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-sequencefileclosing.html language=enus -->
## TOPIC 04706: ApplicationMgr.SequenceFileClosing

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-sequencefileclosing.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-sequencefileclosing.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_SequenceFileClosing( file) Applies To ApplicationMgr Purpose Use this event when you need to perform cleanup or otherwise require a notification when the Application Manager control closes a sequence file. This event is generated immediately before the Application Manager control

### ApplicationMgr.SequenceFileClosing

#### Syntax

ControlName_SequenceFileClosing( file)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Use this event when you need to perform cleanup or otherwise require a notification when the Application Manager control closes a sequence file. This event is generated immediately before the Application Manager control closes the file. The event handler for this event cannot cancel closing the file. Use the
 [ApplicationMgr.QueryCloseSequenceFile](applicationmgr-queryclosesequencefile.html)
 event when you want an opportunity to cancel the closing of sequence files.

#### Parameters

file
 As
 
 [SequenceFile](../tsapiref/sequencefile.html)

[In] Specifies a reference to the sequence file about to be closed.

#### See Also

[ApplicationMgr.QueryCloseSequenceFile](applicationmgr-queryclosesequencefile.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-sequencefileopened.html language=enus -->
## TOPIC 04707: ApplicationMgr.SequenceFileOpened

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-sequencefileopened.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-sequencefileopened.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_SequenceFileOpened( file, alreadyLoaded) Applies To ApplicationMgr Purpose Occurs when a sequence file is opened. Parameters file As SequenceFile [In] Specifies the sequence file that opened. alreadyLoaded As Boolean [In] If this parameter is True , the sequence file was already o

### ApplicationMgr.SequenceFileOpened

#### Syntax

ControlName_SequenceFileOpened( file, alreadyLoaded)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when a sequence file is opened.

#### Parameters

file
 As
 
 [SequenceFile](../tsapiref/sequencefile.html)

[In] Specifies the sequence file that opened.

alreadyLoaded
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] If this parameter is
 True
 , the sequence file was already opened.

#### See Also

[ApplicationMgr.DisplaySequenceFile](applicationmgr-displaysequencefile.html)

[ApplicationMgr.OpenSequenceFile](applicationmgr-opensequencefile.html)

[ApplicationMgr.OpenSequenceFileDialog](applicationmgr-opensequencefiledialog.html)

[ApplicationMgr.OpenSequenceFilesDialog](applicationmgr-opensequencefilesdialog.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-sequencefiles.html language=enus -->
## TOPIC 04708: ApplicationMgr.SequenceFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-sequencefiles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-sequencefiles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.SequenceFiles Data Type SequenceFiles Purpose Returns the collection of sequence files the application opens. Remarks This property eliminates the need to keep an array of open sequence files. Use the ApplicationMgr.OpenSequenceFile method to add files to the collection and the

### ApplicationMgr.SequenceFiles

#### Syntax

[ApplicationMgr](applicationmgr.html).SequenceFiles

#### Data Type

[SequenceFiles](sequencefiles.html)

#### Purpose

Returns the collection of sequence files the application opens.

#### Remarks

This property eliminates the need to keep an array of open sequence files. Use the
 [ApplicationMgr.OpenSequenceFile](applicationmgr-opensequencefile.html)
 method to add files to the collection and the
 [ApplicationMgr.CloseSequenceFile](applicationmgr-closesequencefile.html)
 method to remove files from the collection.

#### See Also

[ApplicationMgr.CloseSequenceFile](applicationmgr-closesequencefile.html)

[ApplicationMgr.OpenSequenceFile](applicationmgr-opensequencefile.html)

[SequenceFiles](sequencefiles.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-setautocloseexecution.html language=enus -->
## TOPIC 04709: ApplicationMgr.SetAutoCloseExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-setautocloseexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-setautocloseexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.SetAutoCloseExecution( exec, val) Purpose Sets an execution to automatically close when complete. Parameters exec As Execution [In] Specifies the execution you want to close automatically. val As Boolean [In] Pass True for the execution to close when complete. When this paramet

### ApplicationMgr.SetAutoCloseExecution

#### Syntax

[ApplicationMgr](applicationmgr.html).SetAutoCloseExecution( exec, val)

#### Purpose

Sets an execution to automatically close when complete.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the execution you want to close automatically.

val
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] Pass
 True
 for the execution to close when complete. When this parameter is
 False
 , the execution does not close automatically.

#### See Also

[ApplicationMgr.GetAutoCloseExecution](applicationmgr-getautocloseexecution.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-setvisible.html language=enus -->
## TOPIC 04710: ApplicationMgr.SetVisible

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-setvisible.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-setvisible.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.SetVisible( exec, val) Purpose Specify False to hide the execution in the user interface. Hidden executions are not included in an execution list connection you establish to an ExecutionView Manager control unless you set the ExecutionListConnection.ShowHiddenExecutions propert

### ApplicationMgr.SetVisible

#### Syntax

[ApplicationMgr](applicationmgr.html).SetVisible( exec, val)

#### Purpose

Specify
 False
 to hide the execution in the user interface. Hidden executions are not included in an execution list connection you establish to an ExecutionView Manager control unless you set the
 [ExecutionListConnection.ShowHiddenExecutions](executionlistconnection-showhiddenexecutions.html)
 property to
 True
 .

#### Remarks

Invisible executions are created when an execution is created with
 ExecTypeMask_InitiallyHidden
 .

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the execution to make visible or hidden.

val
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] Pass
 True
 to make the execution visible. Pass
 False
 to make the execution hidden.

#### See Also

[ApplicationMgr.GetVisible](applicationmgr-getvisible.html)

[ExecutionListConnection](executionlistconnection.html)

[ExecutionListConnection.ShowHiddenExecutions](executionlistconnection-showhiddenexecutions.html)

[ExecutionTypeMask](../tsapiref/executiontypemask.html)

[ExecutionViewMgr.Connections](executionviewmgr-connections.html)

[ExecutionViewMgrConnections.ExecutionList](executionviewmgrconnections-executionlist.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-shutdown.html language=enus -->
## TOPIC 04711: ApplicationMgr.Shutdown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-shutdown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-shutdown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.Shutdown Return Value Boolean Purpose Closes opened sequence files and executions. This method also releases the TestStand Engine. Remarks Call this method before the parent window of the Application Manager control is destroyed. When this method returns True , it is safe to de

### ApplicationMgr.Shutdown

#### Syntax

[ApplicationMgr](applicationmgr.html).Shutdown

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Closes opened sequence files and executions. This method also releases the TestStand Engine.

#### Remarks

Call this method before the parent window of the Application Manager control is destroyed. When this method returns
 True
 , it is safe to destroy the parent window. When this method returns
 False
 , do not destroy the window until the Application Manager control generates an
 [ApplicationMgrExitApplication](applicationmgr-exitapplication.html)
 event. When you cancel the TestStand Engine shutdown procedure, the Application Manager control generates the
 [ApplicationMgrShutDownCancelled](applicationmgr-shutdowncancelled.html)
 event.

#### See Also

[ApplicationMgr.ExitApplication](applicationmgr-exitapplication.html)

[ApplicationMgr.QueryShutdown](applicationmgr-queryshutdown.html)

[ApplicationMgr.ShutDownCancelled](applicationmgr-shutdowncancelled.html)

[ApplicationMgr.Start](applicationmgr-start.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-shutdowncancelled.html language=enus -->
## TOPIC 04712: ApplicationMgr.ShutDownCancelled

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-shutdowncancelled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-shutdowncancelled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ShutDownCancelled Applies To ApplicationMgr Purpose Occurs when the Engine.ShutDown method is cancelled. See Also ApplicationMgr.QueryShutdown ApplicationMgr.Shutdown ApplicationMgr.ShutDownCompleted Engine.ShutDown UIMsg_ShutDownCancelled

### ApplicationMgr.ShutDownCancelled

#### Syntax

ControlName_ShutDownCancelled

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when the
 
 [Engine.ShutDown](../tsapiref/engine-shutdown.html)
 method is cancelled.

#### See Also

[ApplicationMgr.QueryShutdown](applicationmgr-queryshutdown.html)

[ApplicationMgr.Shutdown](applicationmgr-shutdown.html)

[ApplicationMgr.ShutDownCompleted](applicationmgr-shutdowncompleted.html)

[Engine.ShutDown](../tsapiref/engine-shutdown.html)

[UIMsg_ShutDownCancelled](../tsapiref/uimessagecodes.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-shutdowncompleted.html language=enus -->
## TOPIC 04713: ApplicationMgr.ShutDownCompleted

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-shutdowncompleted.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-shutdowncompleted.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ShutDownCompleted Applies To ApplicationMgr Purpose Occurs when the TestStand Engine sends the UIMsg_ShutDownComplete message. Use the ApplicationMgr.Shutdown method to initiate the shutdown process. See Also ApplicationMgr.ExitApplication ApplicationMgr.Shutdown ApplicationMgr.Sh

### ApplicationMgr.ShutDownCompleted

#### Syntax

ControlName_ShutDownCompleted

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when the TestStand Engine sends the
 UIMsg_ShutDownComplete
 message. Use the
 [ApplicationMgr.Shutdown](applicationmgr-shutdown.html)
 method to initiate the shutdown process.

#### See Also

[ApplicationMgr.ExitApplication](applicationmgr-exitapplication.html)

[ApplicationMgr.Shutdown](applicationmgr-shutdown.html)

[ApplicationMgr.ShutDownCancelled](applicationmgr-shutdowncancelled.html)

[UIMsg_ShutDownComplete](../tsapiref/uimessagecodes.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-start.html language=enus -->
## TOPIC 04714: ApplicationMgr.Start

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-start.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-start.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.Start Purpose Initializes the user interface, acquires the necessary license , and runs the LoginLogout Front-End callback sequence, if the ApplicationMgr.LoginOnStart property is True . Remarks Call this method after you create the user interface window. If the application edi

### ApplicationMgr.Start

#### Syntax

[ApplicationMgr](applicationmgr.html).Start

#### Purpose

Initializes the user interface, acquires the necessary
 
 [license](/csh?context=ts_9050)
 , and runs the LoginLogout Front-End callback sequence, if the
 [ApplicationMgr.LoginOnStart](applicationmgr-loginonstart.html)
 property is
 True
 .

#### Remarks

Call this method after you create the user interface window. If the application edits sequence files, set the
 [ApplicationMgr.IsEditor](applicationmgr-iseditor.html)
 property before calling this method. This method calls the
 
 [Engine.AcquireLicense](../tsapiref/engine-acquirelicense.html)
 method to request the proper license for the application to start.

Note

#### See Also

[ApplicationMgr.IsEditor](applicationmgr-iseditor.html)

[ApplicationMgr.IsStarted](applicationmgr-isstarted.html)

[ApplicationMgr.LoginOnStart](applicationmgr-loginonstart.html)

[ApplicationMgr.Shutdown](applicationmgr-shutdown.html)

[Engine.AcquireLicense](../tsapiref/engine-acquirelicense.html)

[TestStand Licensing Options](/csh?context=ts_9050)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-startexecution.html language=enus -->
## TOPIC 04715: ApplicationMgr.StartExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-startexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-startexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_StartExecution( exec, thrd, initiallyHidden) Applies To ApplicationMgr Purpose Occurs when an execution starts. Parameters exec As Execution [In] Specifies the newly started execution. thrd As Thread [In] Specifies the thread of the execution. initiallyHidden As Boolean [In] Speci

### ApplicationMgr.StartExecution

#### Syntax

ControlName_StartExecution( exec, thrd, initiallyHidden)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when an execution starts.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the newly started execution.

thrd
 As
 
 [Thread](../tsapiref/thread.html)

[In] Specifies the thread of the execution.

initiallyHidden
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] Specifies whether the execution is initially hidden.

#### See Also

[ApplicationMgr.EndExecution](applicationmgr-endexecution.html)

[ApplicationMgr.ExecutionClosed](applicationmgr-executionclosed.html)

[UIMsg_ExecutionCreated](../tsapiref/uimessagecodes.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-uimessageevent.html language=enus -->
## TOPIC 04716: ApplicationMgr.UIMessageEvent

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-uimessageevent.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-uimessageevent.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_UIMessageEvent( uiMsg, cancel) Applies To ApplicationMgr Purpose Forwards TestStand Engine events before the manager controls process them. Remarks Use this event to handle messages before the manager controls handle them. The Application Manager control automatically calls the UI

### ApplicationMgr.UIMessageEvent

#### Syntax

ControlName_UIMessageEvent( uiMsg, cancel)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Forwards TestStand Engine events before the manager controls process them.

#### Remarks

Use this event to handle messages before the manager controls handle them.

The Application Manager control automatically calls the
 
 [UIMessage.Acknowledge](../tsapiref/uimessage-acknowledge.html)
 method when this event completes. Therefore, you do not have to directly call the
 UIMessage.Acknowledge
 method from within this event.

#### Parameters

uiMsg
 As
 
 [UIMessage](../tsapiref/uimessage.html)

[In] Specifies a TestStand User Interface message.

cancel
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In/Out] Set this parameter to
 True
 when you do not want the manager controls to handle this event. Setting this parameter to
 True
 can improve performance in some cases by preventing TestStand from storing user interface message data in the internal cache.

Note

#### See Also

[ApplicationMgr.AfterUIMessageEvent](applicationmgr-afteruimessageevent.html)

[ApplicationMgr.UserMessage](applicationmgr-usermessage.html)

[UIMessage](../tsapiref/uimessage.html)

[UIMessage.Acknowledge](../tsapiref/uimessage-acknowledge.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-undostack.html language=enus -->
## TOPIC 04717: ApplicationMgr.UndoStack

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-undostack.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-undostack.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.UndoStack Data Type UndoStack Purpose Assign an UndoStack to this property to provide an UndoStack for CommandKind_Edit_Undo and CommandKind_Edit_Redo commands you connect to the Application Manager control. Remarks This property is useful for creating undo and redo commands fo

### ApplicationMgr.UndoStack

#### Syntax

[ApplicationMgr](applicationmgr.html).UndoStack

#### Data Type

[UndoStack](../tsapiref/undostack.html)

#### Purpose

Assign an
 
 [UndoStack](../tsapiref/undostack.html)
 to this property to provide an UndoStack for
 CommandKind_Edit_Undo
 and
 CommandKind_Edit_Redo
 commands you connect to the Application Manager control.

#### Remarks

This property is useful for creating undo and redo commands for TestStand files that are not sequence files such the station globals file and the users file.

#### See Also

[CommandKinds](commandkinds.html)

Engine.New
 [UndoStack](../tsapiref/undostack.html)

[SequenceFileViewMgr.UndoStack](sequencefileviewmgr-undostack.html)

[UndoStack](../tsapiref/undostack.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-userchanged.html language=enus -->
## TOPIC 04718: ApplicationMgr.UserChanged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-userchanged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-userchanged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_UserChanged( user) Applies To ApplicationMgr Purpose Occurs when the current user logged in changes. Remarks Use this event to update the parts of the user interface that depend on user permissions when the current user logged in changes. Parameters user As User [In] Specifies the

### ApplicationMgr.UserChanged

#### Syntax

ControlName_UserChanged( user)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when the current user logged in changes.

#### Remarks

Use this event to update the parts of the user interface that depend on user permissions when the current user logged in changes.

#### Parameters

user
 As
 
 [User](../tsapiref/user.html)

[In] Specifies the current user. When this parameter is
 NULL
 , no user is logged in.

#### See Also

[ApplicationMgr.Login](applicationmgr-login.html)

[ApplicationMgr.Logout](applicationmgr-logout.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-userdata.html language=enus -->
## TOPIC 04719: ApplicationMgr.UserData

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-userdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-userdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.UserData Data Type Variant Purpose Stores user-specific data. Remarks User data is cleared when the application shuts down.

### ApplicationMgr.UserData

#### Syntax

[ApplicationMgr](applicationmgr.html).UserData

#### Data Type

[Variant](data-types-for-teststand-user-interface.html)

#### Purpose

Stores user-specific data.

#### Remarks

User data is cleared when the application shuts down.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-usermessage.html language=enus -->
## TOPIC 04720: ApplicationMgr.UserMessage

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-usermessage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-usermessage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_UserMessage( uiMsg) Applies To ApplicationMgr Purpose Occurs when an application component posts a user-defined UIMessage . A user-defined user interface message has an event code value that is equal to or greater than UIMsg_UserMessageBase (value: 10000) . Remarks The Application

### ApplicationMgr.UserMessage

#### Syntax

ControlName_UserMessage( uiMsg)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when an application component posts a user-defined
 
 [UIMessage](../tsapiref/uimessage.html)
 . A user-defined user interface message has an event code value that is equal to or greater than
 UIMsg_UserMessageBase (value: 10000)
 .

#### Remarks

The Application Manager control automatically acknowledges the user message when this event completes. Therefore, you do not have to directly call the
 
 [UIMessage.Acknowledge](../tsapiref/uimessage-acknowledge.html)
 method from within this event.

Messages the
 
 Engine.Register
 [UIMessage](../tsapiref/uimessage.html)
 method defines do not generate an
 ApplicationMgr.UserMessage
 event, but TestStand does send the message to
 [ApplicationMgr.UIMessageEvent](applicationmgr-uimessageevent.html)
 .

#### Parameters

uiMsg
 As
 
 [UIMessage](../tsapiref/uimessage.html)

[In] Specifies the user-defined UIMessage object.

#### See Also

[ApplicationMgr.UIMessageEvent](applicationmgr-uimessageevent.html)

Engine.Register
 [UIMessage](../tsapiref/uimessage.html)

Engine.Post
 [UIMessage](../tsapiref/uimessage.html)

[UIMessage](../tsapiref/uimessage.html)

[UIMessage.Acknowledge](../tsapiref/uimessage-acknowledge.html)

[UIMsg_UserMessage](../tsapiref/uimessagecodes.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-usesteplistconfigurations.html language=enus -->
## TOPIC 04721: ApplicationMgr.UseStepListConfigurations

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-usesteplistconfigurations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-usesteplistconfigurations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgr.UseStepListConfigurations Data Type Boolean Purpose Specifies whether the Application Manager control uses the selected step list configurations specified in the Edit Step List Configurations dialog box that set the non-border properties of connected SequenceView controls. When

### ApplicationMgr.UseStepListConfigurations

#### Syntax

[ApplicationMgr](applicationmgr.html).UseStepListConfigurations

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the Application Manager control uses the selected step list configurations specified in the
 [Edit Step List Configurations](../tsref/edit-step-list-configurations-dialog-box.html)
 dialog box that set the non-border properties of connected SequenceView controls.

When this property is
 True
 , the Application Manager control enables commands that select or configure step list configuration. In addition, the non-border SequenceView properties you specify at edit time on the SequenceView property pages apply only when no applicable step list configurations exist in the application configuration file.

When this property is
 False
 , the Application Manager control hides commands that select or configure step list configurations, and the Application Manager control uses the non-border SequenceView properties you specify at edit time on the SequenceView property pages.

#### See Also

[Edit Step List Configurations dialog box](../tsref/edit-step-list-configurations-dialog-box.html)

[SequenceView Appearance Property Page](sequenceview-appearance-property-page.html)

[SequenceView Columns Property Page](sequenceview-columns-property-page.html)

[SequenceView Fonts and Colors Property Page](sequenceview-fonts-and-colors-property-page.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr-wait.html language=enus -->
## TOPIC 04722: ApplicationMgr.Wait

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr-wait.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr-wait.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_Wait( showWait) Applies To ApplicationMgr Purpose Occurs when the application is performing lengthy tasks. Remarks Use this event to display or remove a wait cursor or other indicator to show when the application is busy. Parameters showWait As Boolean [In] When this parameter is

### ApplicationMgr.Wait

#### Syntax

ControlName_Wait( showWait)

#### Applies To

[ApplicationMgr](applicationmgr.html)

#### Purpose

Occurs when the application is performing lengthy tasks.

#### Remarks

Use this event to display or remove a wait cursor or other indicator to show when the application is busy.

#### Parameters

showWait
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] When this parameter is
 True
 , the application has started a long operation. When this parameter is
 False
 , the application has finished the long operation.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgr.html language=enus -->
## TOPIC 04723: ApplicationMgr

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Application Manager control performs the following basic operations, which facilitate using the TestStand Engine in an application: Processes command-line arguments. Maintains an application configuration file. Initializes and shuts down the TestStand Engine. Logs users in and out. Loads and unl

### ApplicationMgr

The Application Manager control performs the following basic operations, which facilitate using the TestStand Engine in an application:

- Processes command-line arguments.
- Maintains an application configuration file.
- Initializes and shuts down the TestStand Engine.
- Logs users in and out.
- Loads and unloads files.
- Launches executions.
- Tracks existing sequence files and executions.
- Manages licensing.

An application that uses the TestStand User Interface Controls must have a single Application Manager control that exists for the duration of the application.

#### Properties

| ApplicationWillExitOnStart (Read Only) |
| --- |
| AutomaticallyReloadModifiedFiles |
| BreakOnFirstStep |
| BreakOnSequenceFailure |
| BreakOnStepFailure |
| CommandLineArguments (Read Only) |
| CommandLineCanChangeEditMode |
| ConfigFile (Read Only) |
| ConfigFilePath |
| ConfigurationEntryPoints (Read Only) |
| Connections (Read Only) |
| CreateEmptySequenceFileOnStart |
| CurrentUIMessage (Read Only) |
| EditModeShortcutKey |
| EditModeShortcutModifier |
| EditReadOnlyFiles |
| Executing (Read Only) |
| ExecutionEntryPoints (Read Only) |
| Executions (Read Only) |
| ExitCode |
| IsEditor |
| IsShuttingDown (Read Only) |
| IsStarted (Read Only) |
| LoginLogoutRunning (Read Only) |
| LoginOnStart |
| LoginRunning (Read Only) |
| LogoutClosesSeqFilesAndExecs |
| LogoutRunning (Read Only) |
| MakeStepNamesUnique |
| MRUFiles (Read Only) |
| ProcessCommandLine |
| PromptForOverwrite |
| ReloadModifiedFilesInterval |
| ReloadSequenceFilesOnStart |
| SaveOnClose |
| SequenceFiles (Read Only) |
| UndoStack |
| UserData |
| UseStepListConfigurations |

#### Methods

| AddCommandLineArgumentsHelp |
| --- |
| BeginEdit |
| CanEdit |
| CloseAllExecutions |
| CloseAllSequenceFiles |
| CloseExecution |
| CloseSequenceFile |
| ConnectAdapterList |
| ConnectCaption |
| ConnectCommand |
| EndEdit |
| GetAutoCloseExecution |
| GetCaptionText |
| GetCommand |
| GetEngine |
| GetExecutionViewMgr |
| GetImageName |
| GetModelFile |
| GetRunState |
| GetSequenceFileViewMgr |
| GetTerminationState |
| GetVisible |
| LocalizeAllControls |
| Login |
| Logout |
| NewCommands |
| OpenSequenceFile |
| OpenSequenceFileDialog |
| OpenSequenceFilesDialog |
| RaiseError |
| Refresh |
| RefreshAllViewMgrs |
| RefreshFile |
| ReloadConfigFile |
| ReloadFile |
| ReloadModifiedSequenceFilesEx |
| SetAutoCloseExecution |
| SetVisible |
| Shutdown |
| Start |

#### Events

| AfterUIMessageEvent |
| --- |
| BeginEdit |
| Break |
| BreakOnRunTimeError |
| CanEdit |
| DisplayCustomRunTimeErrorDialog |
| DisplayExecution |
| DisplayReport |
| DisplaySequenceFile |
| DropFile |
| EditModeChanged |
| EndEdit |
| EndExecution |
| ExecutionClosed |
| ExitApplication |
| PostCommandExecute |
| PreCommandExecute |
| ProcessUserCommandLineArguments |
| QueryCloseExecution |
| QueryCloseSequenceFile |
| QueryReloadSequenceFile |
| QueryShutdown |
| RefreshWindows |
| ReportError |
| SequenceFileClosing |
| SequenceFileOpened |
| ShutDownCancelled |
| ShutDownCompleted |
| StartExecution |
| UIMessageEvent |
| UserChanged |
| UserMessage |
| Wait |

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgrconnections-adapterlist.html language=enus -->
## TOPIC 04724: ApplicationMgrConnections.AdapterList

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgrconnections-adapterlist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgrconnections-adapterlist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgrConnections.AdapterList Data Type AdapterListConnections Purpose Collection of AdapterListConnection objects. See Also AdapterListConnection AdapterListConnections ApplicationMgr.ConnectAdapterList

### ApplicationMgrConnections.AdapterList

#### Syntax

[ApplicationMgrConnections](applicationmgrconnections.html).AdapterList

#### Data Type

[AdapterListConnections](adapterlistconnections.html)

#### Purpose

Collection of
 [AdapterListConnection](adapterlistconnection.html)
 objects.

#### See Also

[AdapterListConnection](adapterlistconnection.html)

[AdapterListConnections](adapterlistconnections.html)

[ApplicationMgr.ConnectAdapterList](applicationmgr-connectadapterlist.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgrconnections-caption.html language=enus -->
## TOPIC 04725: ApplicationMgrConnections.Caption

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgrconnections-caption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgrconnections-caption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgrConnections.Caption Data Type CaptionConnections Purpose Collection of CaptionConnection objects. See Also ApplicationMgr.ConnectCaption CaptionConnection CaptionConnections

### ApplicationMgrConnections.Caption

#### Syntax

[ApplicationMgrConnections](applicationmgrconnections.html).Caption

#### Data Type

[CaptionConnections](captionconnections.html)

#### Purpose

Collection of CaptionConnection objects.

#### See Also

[ApplicationMgr.ConnectCaption](applicationmgr-connectcaption.html)

[CaptionConnection](captionconnection.html)

[CaptionConnections](captionconnections.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgrconnections-command.html language=enus -->
## TOPIC 04726: ApplicationMgrConnections.Command

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgrconnections-command.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgrconnections-command.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ApplicationMgrConnections.Command Data Type CommandConnections Purpose Collection of CommandConnection objects. See Also ApplicationMgr.ConnectCommand CommandConnection CommandConnections

### ApplicationMgrConnections.Command

#### Syntax

[ApplicationMgrConnections](applicationmgrconnections.html).Command

#### Data Type

[CommandConnections](commandconnections.html)

#### Purpose

Collection of CommandConnection objects.

#### See Also

[ApplicationMgr.ConnectCommand](applicationmgr-connectcommand.html)

[CommandConnection](commandconnection.html)

[CommandConnections](commandconnections.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/applicationmgrconnections.html language=enus -->
## TOPIC 04727: ApplicationMgrConnections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/applicationmgrconnections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/applicationmgrconnections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the connections for an Application Manager control. Use the ApplicationMgr.Connections property to obtain a collection of ApplicationMgrConnections objects. Properties AdapterList (Read Only) Caption (Read Only) Command (Read Only) See Also Application Manager ApplicationMgr.Connections Exe

### ApplicationMgrConnections

Contains the connections for an
 [Application Manager](applicationmgr.html)
 control. Use the
 [ApplicationMgr.Connections](applicationmgr-connections.html)
 property to obtain a collection of ApplicationMgrConnections objects.

#### Properties

| AdapterList (Read Only) |
| --- |
| Caption (Read Only) |
| Command (Read Only) |

#### See Also

[Application Manager](applicationmgr.html)

[ApplicationMgr.Connections](applicationmgr-connections.html)

[ExecutionViewMgrConnections](executionviewmgrconnections.html)

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/automaticallyreloadmodifiedfilesoptions.html language=enus -->
## TOPIC 04728: AutomaticallyReloadModifiedFilesOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/automaticallyreloadmodifiedfilesoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/automaticallyreloadmodifiedfilesoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the ApplicationMgr.AutomaticallyReloadModifiedFiles property. AutomaticallyReloadModifiedFilesOption_DoNotReload –(Value: 1) Specifies that the Application Manager control never calls the ApplicationMgr.ReloadModifiedSequenceFilesEx method. You must call the ApplicationMgr.R

### AutomaticallyReloadModifiedFilesOptions

Use these constants with the
 [ApplicationMgr.AutomaticallyReloadModifiedFiles](applicationmgr-automaticallyreloadmodifiedfil.html)
 property.

- AutomaticallyReloadModifiedFilesOption_DoNotReload 
 –(Value: 1) Specifies that the Application Manager control never calls the
 ApplicationMgr.ReloadModifiedSequenceFilesEx 
 method. You must call the
 ApplicationMgr.ReloadModifiedSequenceFilesEx 
 method to reload modified sequence files.
- AutomaticallyReloadModifiedFilesOption_OnActivateApplication 
 –(Value: 3) Specifies that the Application Manager control calls the
 ApplicationMgr.ReloadModifiedSequenceFilesEx 
 method when you activate the application.
- AutomaticallyReloadModifiedFilesOption_OnTimer 
 –(Value: 2) Specifies that the Application Manager control calls the
 ApplicationMgr.ReloadModifiedSequenceFilesEx 
 method at the interval you specify with the
 ApplicationMgr.ReloadModifiedFilesInterval 
 property.

#### See Also

[ApplicationMgr.AutomaticallyReloadModifiedFiles](applicationmgr-automaticallyreloadmodifiedfil.html)

[ApplicationMgr.ReloadModifiedFilesInterval](applicationmgr-reloadmodifiedfilesinterval.html)

[ApplicationMgr.ReloadModifiedSequenceFilesEx](applicationmgr-reloadmodifiedsequencefilesex.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/autosizingoptions.html language=enus -->
## TOPIC 04729: AutoSizingOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/autosizingoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/autosizingoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the SeqViewColumn.Autosizing and ListBoxColumn.Autosizing properties. AutoSizingOption_None –(Value: 0) The item does not automatically resize itself. AutoSizingOption_Proportional –(Value: 1) The item resizes when the container resizes. The item determines the amount to res

### AutoSizingOptions

Use these constants with the
 [SeqViewColumn.Autosizing](seqviewcolumn-autosizing.html)
 and
 [ListBoxColumn.Autosizing](listboxcolumn-autosizing.html)
 properties.

- AutoSizingOption_None 
 –(Value: 0) The item does not automatically resize itself.
- AutoSizingOption_Proportional 
 –(Value: 1) The item resizes when the container resizes. The item determines the amount to resize from the proportion that the current size occupies of the total size of all resizable items in the same container.

#### See Also

[ListBoxColumn.Autosizing](listboxcolumn-autosizing.html)

[SeqViewColumn.Autosizing](seqviewcolumn-autosizing.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/blockdisplayoptions.html language=enus -->
## TOPIC 04730: BlockDisplayOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/blockdisplayoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/blockdisplayoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the SequenceView.BlockDisplayOptions property. BlockDisplayOption_BoldStepFont –(Value: 0x10) Displays the step name in bold for steps that define or operate according to the block structure of the sequence. BlockDisplayOption_DottedLines –(Value: 0x4) Draws the vertical bar

### BlockDisplayOptions

Use these constants with the
 [SequenceView.BlockDisplayOptions](sequenceview-blockdisplayoptions.html)
 property.

- BlockDisplayOption_BoldStepFont 
 –(Value: 0x10) Displays the step name in bold for steps that define or operate according to the block structure of the sequence.
- BlockDisplayOption_DottedLines 
 –(Value: 0x4) Draws the vertical bar to the left of the block with a dotted line.
- BlockDisplayOption_HighlightMismatchErrors 
 –(Value: 0x20) Draws the step name in red for steps that start blocks that do not have an End step and for block ending steps that do not match with a block starting step. Also draws the vertical block bar red for blocks that do not have an ending step.
- BlockDisplayOption_Indent 
 –(Value: 0x1) Indents the steps within a block.
- BlockDisplayOption_None 
 –(Value: 0x0) No options.
- BlockDisplayOption_ShowGroupLines 
 –(Value: 0x40) Draws a vertical bar to the left of the steps in a step group.
- BlockDisplayOption_ShowLines 
 –(Value: 0x2) Draws a vertical bar to the left of the steps in a block.
- BlockDisplayOption_ShowStepIcons 
 –(Value: 0x8) Displays icons for steps that define or operate according to the block structure of the sequence.

#### See Also

[SequenceView.BlockDisplayOptions](sequenceview-blockdisplayoptions.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/booleanorpreference.html language=enus -->
## TOPIC 04731: BooleanOrPreference

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/booleanorpreference.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/booleanorpreference.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the ExpressionEdit.WantReturn and ExpressionEdit.WordWrap properties. BooleanOrPreference_False –(Value: 0) Specifies a value of False . BooleanOrPreference_True –(Value: 1) Specifies a value of True . BooleanOrPreference_UsePreference –(Value: 3) Use the corresponding prefe

### BooleanOrPreference

Use these constants with the
 [ExpressionEdit.WantReturn](expressionedit-wantreturn.html)
 and
 [ExpressionEdit.WordWrap](expressionedit-wordwrap.html)
 properties.

- BooleanOrPreference_False 
 –(Value: 0) Specifies a value of
 False 
 .
- BooleanOrPreference_True 
 –(Value: 1) Specifies a value of
 True 
 .
- BooleanOrPreference_UsePreference 
 –(Value: 3) Use the corresponding preference option in the
 Expression Editing Options 
 dialog box.

#### See Also

[Expression Editing Options dialog box](../tsref/expression-editing-options-dialog-box.html)

[ExpressionEdit.WantReturn](expressionedit-wantreturn.html)

[ExpressionEdit.WordWrap](expressionedit-wordwrap.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/borders-borderdraggedeventenabled.html language=enus -->
## TOPIC 04732: Borders.BorderDraggedEventEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/borders-borderdraggedeventenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/borders-borderdraggedeventenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Borders.BorderDraggedEventEnabled Data Type Boolean Purpose When this property is True , the control displays a resizing cursor over the draggable borders, and the control generates BorderDragged events when the user drags a draggable border with the mouse.

### Borders.BorderDraggedEventEnabled

#### Syntax

[Borders](borders.html).BorderDraggedEventEnabled

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 , the control displays a resizing cursor over the draggable borders, and the control generates
 BorderDragged
 events when the user drags a draggable border with the mouse.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/borders-borderedgestyle.html language=enus -->
## TOPIC 04733: Borders.BorderEdgeStyle

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/borders-borderedgestyle.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/borders-borderedgestyle.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Borders.BorderEdgeStyle Data Type EdgeStyles Use the following constants with this data type: EdgeStyle_ControlEdge –(Value: 3) The edge has the appearance of a control edge. The appearance can vary depending on the Microsoft Windows appearance settings and on the specific property to which y

### Borders.BorderEdgeStyle

#### Syntax

[Borders](borders.html).BorderEdgeStyle

#### Data Type

[EdgeStyles](edgestyles.html)

Use the following constants with this data type:

- EdgeStyle_ControlEdge 
 –(Value: 3) The edge has the appearance of a control edge. The appearance can vary depending on the Microsoft Windows appearance settings and on the specific property to which you apply this value.
- EdgeStyle_FixedSingle 
 –(Value: 2) The edge is a black line, one pixel thick.
- EdgeStyle_Flat 
 –(Value: 1) The edge appears flat.
- EdgeStyle_Inset 
 –(Value: 5) The edge has a sunken three-dimensional appearance.
- EdgeStyle_Raised 
 –(Value: 4) The edge has a raised three-dimensional appearance.
- EdgeStyle_UI 
 –(Value: 6) The edge uses the color from the property
 Borders.FrameEdgeUIStyleColor 
 .

#### Purpose

Specifies the appearance of the draggable borders the control displays.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/borders-borderwidth.html language=enus -->
## TOPIC 04734: Borders.BorderWidth

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/borders-borderwidth.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/borders-borderwidth.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Borders.BorderWidth Data Type Long Purpose Specifies the width of the draggable borders the control displays.

### Borders.BorderWidth

#### Syntax

[Borders](borders.html).BorderWidth

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the width of the draggable borders the control displays.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/borders-frameedgestyle.html language=enus -->
## TOPIC 04735: Borders.FrameEdgeStyle

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/borders-frameedgestyle.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/borders-frameedgestyle.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Borders.FrameEdgeStyle Data Type EdgeStyles Use the following constants with this data type: EdgeStyle_ControlEdge –(Value: 3) The edge has the appearance of a control edge. The appearance can vary depending on the Microsoft Windows appearance settings and on the specific property to which yo

### Borders.FrameEdgeStyle

#### Syntax

[Borders](borders.html).FrameEdgeStyle

#### Data Type

[EdgeStyles](edgestyles.html)

Use the following constants with this data type:

- EdgeStyle_ControlEdge 
 –(Value: 3) The edge has the appearance of a control edge. The appearance can vary depending on the Microsoft Windows appearance settings and on the specific property to which you apply this value.
- EdgeStyle_FixedSingle 
 –(Value: 2) The edge is a black line, one pixel thick.
- EdgeStyle_Flat 
 –(Value: 1) The edge appears flat.
- EdgeStyle_Inset 
 –(Value: 5) The edge has a sunken three-dimensional appearance.
- EdgeStyle_Raised 
 –(Value: 4) The edge has a raised three-dimensional appearance.
- EdgeStyle_UI 
 –(Value: 6) The edge uses the color from the property
 Borders.FrameEdgeUIStyleColor 
 .

#### Purpose

Specifies the appearance of the frame the control displays.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/borders-frameedgeuistylecolor.html language=enus -->
## TOPIC 04736: Borders.FrameEdgeUIStyleColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/borders-frameedgeuistylecolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/borders-frameedgeuistylecolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Borders.FrameEdgeUIStyleColor Data Type Color Purpose Specifies the color to use for the frame and draggable borders when using the option EdgeStyles.EdgeStyle_UI . The default color is COLOR_3DFACE .

### Borders.FrameEdgeUIStyleColor

#### Syntax

[Borders](borders.html).FrameEdgeUIStyleColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the color to use for the frame and draggable borders when using the option
 EdgeStyles.EdgeStyle_UI
 . The default color is
 COLOR_3DFACE
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/borders-frameinsideborders.html language=enus -->
## TOPIC 04737: Borders.FrameInsideBorders

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/borders-frameinsideborders.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/borders-frameinsideborders.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Borders.FrameInsideBorders Data Type Boolean Purpose When this property is True , the control displays the frame within the draggable borders. When this property is False , the control displays the frame around the draggable borders.

### Borders.FrameInsideBorders

#### Syntax

[Borders](borders.html).FrameInsideBorders

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 , the control displays the frame
 within
 the draggable borders. When this property is
 False
 , the control displays the frame
 around
 the draggable borders.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/borders-framevisible.html language=enus -->
## TOPIC 04738: Borders.FrameVisible

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/borders-framevisible.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/borders-framevisible.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Borders.FrameVisible Data Type Boolean Purpose When this property is True , the control displays a thin rectangular frame that surrounds the control.

### Borders.FrameVisible

#### Syntax

[Borders](borders.html).FrameVisible

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 , the control displays a thin rectangular frame that surrounds the control.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/borders-getframethickness.html language=enus -->
## TOPIC 04739: Borders.GetFrameThickness

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/borders-getframethickness.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/borders-getframethickness.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Borders.GetFrameThickness( verticalThickness, horizontalThickness) Purpose Returns the vertical and horizontal thickness of the frame around the control. The values returned are based on the frame visibility and style. Parameters verticalThickness As Long [Out] Returns the thickness, in pixel

### Borders.GetFrameThickness

#### Syntax

[Borders](borders.html).GetFrameThickness( verticalThickness, horizontalThickness)

#### Purpose

Returns the vertical and horizontal thickness of the frame around the control. The values returned are based on the frame visibility and style.

#### Parameters

verticalThickness
 As
 [Long](data-types-for-teststand-user-interface.html)

[Out] Returns the thickness, in pixels, of the vertical portion of the frame.

horizontalThickness
 As
 [Long](data-types-for-teststand-user-interface.html)

[Out] Returns the thickness, in pixels, of the horizontal portion of the frame.

#### See Also

[Borders.FrameEdgeStyle](borders-frameedgestyle.html)

[Borders.FrameVisible](borders-framevisible.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/borders-visibleborders.html language=enus -->
## TOPIC 04740: Borders.VisibleBorders

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/borders-visibleborders.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/borders-visibleborders.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Borders.VisibleBorders Data Type Long Purpose Specifies which draggable borders the control displays. Remarks Use any combination of the WhichBorders constants. Use the bitwise-OR operator to specify more than one value. See Also WhichBorders

### Borders.VisibleBorders

#### Syntax

[Borders](borders.html).VisibleBorders

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies which draggable borders the control displays.

#### Remarks

Use any combination of the
 [WhichBorders](whichborders.html)
 constants. Use the bitwise-OR operator to specify more than one value.

#### See Also

[WhichBorders](whichborders.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/borders.html language=enus -->
## TOPIC 04741: Borders

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/borders.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/borders.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A Borders object specifies the frame and draggable borders that surround a control. A frame is a thin rectangle that surrounds a control on all sides. A draggable border is a rectangular strip of configurable thickness you can place on any combination of the edges of a control. When the application

### Borders

A Borders object specifies the frame and draggable borders that surround a control. A frame is a thin rectangle that surrounds a control on all sides. A draggable border is a rectangular strip of configurable thickness you can place on any combination of the edges of a control. When the application handles the
 BorderDragged
 event for the control, users can drag the borders to resize or move the control.

When a control fills a rectangular view area of an application window, you can enable the draggable borders to implement splitter bars that resize the view. Although you can implement splitter bars in some environments without using draggable borders, some environments do not provide any other way to create a splitter bar. For other environments, creating a resizable view using draggable borders is sometimes simpler than using a separate splitter bar. You can also disable the
 BorderDragged
 event for a control to use borders for their cosmetic effect only.

#### Properties

| BorderDraggedEventEnabled |
| --- |
| BorderEdgeStyle |
| BorderWidth |
| FrameEdgeStyle |
| FrameEdgeUIStyleColor |
| FrameInsideBorders |
| FrameVisible |
| VisibleBorders |

#### Method

| GetFrameThickness |
| --- |

#### See Also

[ExpressionEdit.Borders](expressionedit-borders.html)

[ListBar.Borders](listbar-borders.html)

[ListBox.Borders](listbox-borders.html)

[ReportView.Borders](reportview-borders.html)

[SequenceView.Borders](sequenceview-borders.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/borderstyles.html language=enus -->
## TOPIC 04742: BorderStyles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/borderstyles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/borderstyles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with Label.BorderStyle to specify the border style of the control. BorderStyle_Fixed3D –(Value: 1) Specifies that the control draws a three-dimensional border. BorderStyle_FixedSingle –(Value: 2) Specifies that the control draws a single-line border. BorderStyle_NoBorder –(Value:

### BorderStyles

Use these constants with
 [Label.BorderStyle](label-borderstyle.html)
 to specify the border style of the control.

- BorderStyle_Fixed3D 
 –(Value: 1) Specifies that the control draws a three-dimensional border.
- BorderStyle_FixedSingle 
 –(Value: 2) Specifies that the control draws a single-line border.
- BorderStyle_NoBorder 
 –(Value: 0) Specifies that the control does not draw a border.

#### See Also

[Label.BorderStyle](label-borderstyle.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-actionstyle.html language=enus -->
## TOPIC 04743: Button.ActionStyle

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-actionstyle.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-actionstyle.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.ActionStyle Data Type ButtonActionStyles Use the following constants with this data type: ButtonActionStyle_PushButton –(Value: 0) Specifies that the button changes to a pressed state only when you click it. ButtonActionStyle_ToggleButton –(Value: 1) Specifies that the button changes t

### Button.ActionStyle

#### Syntax

[Button](button.html).ActionStyle

#### Data Type

[ButtonActionStyles](buttonactionstyles.html)

Use the following constants with this data type:

- ButtonActionStyle_PushButton 
 –(Value: 0) Specifies that the button changes to a pressed state only when you click it.
- ButtonActionStyle_ToggleButton 
 –(Value: 1) Specifies that the button changes to a pressed state when you set the
 Button.Value 
 property to
 True 
 and changes to a normal state when you set the value to
 False 
 .

#### Purpose

Specifies how the button behaves when you click it.

#### See Also

[Button.Style](button-style.html)

[Button.Value](button-value.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-autosizing.html language=enus -->
## TOPIC 04744: Button.AutoSizing

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-autosizing.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-autosizing.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.AutoSizing Data Type ButtonSizing Use the following constants with this data type: ButtonSizing_AlwaysAutoSize –(Value: 0) Always resize the Button control to fit the text. ButtonSizing_GrowOnly –(Value: 1) Resize the Button control only when the text does not fit in the control. Butto

### Button.AutoSizing

#### Syntax

[Button](button.html).AutoSizing

#### Data Type

[ButtonSizing](buttonsizing.html)

Use the following constants with this data type:

- ButtonSizing_AlwaysAutoSize 
 –(Value: 0) Always resize the Button control to fit the text.
- ButtonSizing_GrowOnly 
 –(Value: 1) Resize the Button control only when the text does not fit in the control.
- ButtonSizing_NeverAutoSize 
 –(Value: 3) Never resize the Button control.
- ButtonSizing_ShrinkOnly 
 –(Value: 2) Resize the Button control only when the text is smaller than the button.

#### Purpose

Specifies whether the control automatically resizes when the text of the control changes.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-backcolor.html language=enus -->
## TOPIC 04745: Button.BackColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-backcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-backcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.BackColor Data Type Color Purpose Specifies the background color for the Button control. Remarks When you set the Button.Style property to ButtonStyle_ToolBar , this setting applies to the face and border of the button. When you set the Button.Style property to ButtonStyle_Standard , t

### Button.BackColor

#### Syntax

[Button](button.html).BackColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the background color for the Button control.

#### Remarks

When you set the
 [Button.Style](button-style.html)
 property to
 [ButtonStyle_ToolBar](buttonstyles.html)
 , this setting applies to the face and border of the button. When you set the
 Button.Style
 property to
 [ButtonStyle_Standard](buttonstyles.html)
 , the button face adheres to the system settings, and this setting affects only the border of the button.

#### See Also

[Button.ForeColor](button-forecolor.html)

[Button.Style](button-style.html)

[ButtonStyles](buttonstyles.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-caption.html language=enus -->
## TOPIC 04746: Button.Caption

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-caption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-caption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.Caption Data Type String Purpose Specifies the text the control displays. Remarks In the caption, include an ampersand ( & ) immediately before the character, if any, you want to designate as an accelerator character. The character displays as underlined. Press <Alt> and the underlined

### Button.Caption

#### Syntax

[Button](button.html).Caption

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the text the control displays.

#### Remarks

In the caption, include an ampersand (
 &
 ) immediately before the character, if any, you want to designate as an accelerator character. The character displays as underlined. Press <Alt> and the underlined character to move the focus to the control. To include an ampersand character in a caption without creating an accelerator character, include two consecutive ampersands. A single ampersand displays in the caption and no characters display as underlined.

When you connect this control to a manager control, the manager control sets this property automatically.

#### See Also

[Button.UseMnemonic](button-usemnemonic.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-click.html language=enus -->
## TOPIC 04747: Button.Click

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-click.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-click.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_Click Applies To Button Purpose Occurs when you press and release the mouse on the control, or when the Button.Value property of the control changes. See Also Button.DoClick Button.MouseDown Button.MouseMove Button.MouseUp Button.Value

### Button.Click

#### Syntax

ControlName_Click

#### Applies To

[Button](button.html)

#### Purpose

Occurs when you press and release the mouse on the control, or when the
 [Button.Value](button-value.html)
 property of the control changes.

#### See Also

[Button.DoClick](button-doclick.html)

[Button.MouseDown](button-mousedown.html)

[Button.MouseMove](button-mousemove.html)

[Button.MouseUp](button-mouseup.html)

[Button.Value](button-value.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-connectionactivity.html language=enus -->
## TOPIC 04748: Button.ConnectionActivity

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-connectionactivity.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-connectionactivity.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ConnectionActivity( activity) Applies To Button Purpose Occurs after the connection to a manager control makes a change to a user interface control. Parameters activity As ConnectionActivityTypes [In] Specifies the type of change.

### Button.ConnectionActivity

#### Syntax

ControlName_ConnectionActivity( activity)

#### Applies To

[Button](button.html)

#### Purpose

Occurs after the connection to a manager control makes a change to a user interface control.

#### Parameters

activity
 As
 [ConnectionActivityTypes](connectionactivitytypes.html)

[In] Specifies the type of change.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-doclick.html language=enus -->
## TOPIC 04749: Button.DoClick

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-doclick.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-doclick.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.DoClick Purpose Call this method to simulate a button click. See Also Button.Click Button.Value

### Button.DoClick

#### Syntax

[Button](button.html).DoClick

#### Purpose

Call this method to simulate a button click.

#### See Also

[Button.Click](button-click.html)

[Button.Value](button-value.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-enabled.html language=enus -->
## TOPIC 04750: Button.Enabled

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-enabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-enabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.Enabled Data Type Boolean Purpose The control responds to user-generated events only when this property is True . Remarks When you connect this control to a manager control, the manager control sets this property automatically.

### Button.Enabled

#### Syntax

[Button](button.html).Enabled

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

The control responds to user-generated events only when this property is
 True
 .

#### Remarks

When you connect this control to a manager control, the manager control sets this property automatically.

Parent topic:

Properties
