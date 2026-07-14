# NI PYTHON API DIGEST: nitsm-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/nitsm-python commit=334552e02b324bf5663e96a4fc31399570c3138a -->

<!--NI_PYTHON_API repo=nitsm-python path=src/nitsm/__init__.py -->
## PYTHON MODULE: src/nitsm/__init__.py

### MODULE DOCSTRING

NI TestStand Semiconductor Module Python API

<!--NI_PYTHON_API repo=nitsm-python path=src/nitsm/_pinmapinterfaces.py -->
## PYTHON MODULE: src/nitsm/_pinmapinterfaces.py

### MODULE DOCSTRING

NI TestStand 2020 Semiconductor Module Pin Map Interfaces

- `CLSID = IID('{AC54E909-CA87-48AB-9935-A908E5DCB97B}')`

- `LCID = 0`

### `class constants()`

### `class IMeasurementPublisher(DispatchBaseClass)`

#### `def GetInputDataBoolean(self, siteNumberParam=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, inputDataId=defaultNamedNotOptArg)`

#### `def GetInputDataDouble(self, siteNumberParam=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, inputDataId=defaultNamedNotOptArg)`

#### `def GetInputDataString(self, siteNumberParam=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, inputDataId=defaultNamedNotOptArg)`

#### `def PublishBool(self, siteNumberParam=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg)`

#### `def PublishBoolToTestStandVariable(self, siteNumber=defaultNamedNotOptArg, expression=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg)`

#### `def PublishDouble(self, siteNumberParam=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg)`

#### `def PublishDoubleToTestStandVariable(self, siteNumber=defaultNamedNotOptArg, expression=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg)`

#### `def PublishString(self, siteNumberParam=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg)`

#### `def PublishStringToTestStandVariable(self, siteNumber=defaultNamedNotOptArg, expression=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg)`

#### `def __iter__(self)`

Return a Python iterator for this object

### `class IModelBasedInstrumentInstanceData(DispatchBaseClass)`

#### `def __iter__(self)`

Return a Python iterator for this object

### `class IModelBasedInstrumentProperty(DispatchBaseClass)`

#### `def __iter__(self)`

Return a Python iterator for this object

### `class IModelBasedInstrumentPropertyList(DispatchBaseClass)`

#### `def __iter__(self)`

Return a Python iterator for this object

### `class IModelBasedInstrumentResourcePropertyList(DispatchBaseClass)`

#### `def __iter__(self)`

Return a Python iterator for this object

### `class ISemiconductorModuleContext(DispatchBaseClass)`

NI TestStand Semiconductor Module Pin Map

#### `def CreateMultisiteDataForAnalogOutput(self, perPinWaveform=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, idleValue=defaultNamedNotOptArg, numberOfChannelsInTask=pythoncom.Missing)`

#### `def CreateMultisiteDataForAnalogOutput_2(self, perPinWaveform=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, idleValue=defaultNamedNotOptArg, numberOfChannelsInTask=pythoncom.Missing)`

#### `def CreatePerSiteMultisiteDataForAnalogOutput(self, sitePinWaveforms=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, idleValue=defaultNamedNotOptArg, numberOfChannelsInTask=pythoncom.Missing)`

#### `def CreatePerSiteMultisiteDataForAnalogOutput_2(self, sitePinWaveforms=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, idleValue=defaultNamedNotOptArg, numberOfChannelsInTask=pythoncom.Missing)`

#### `def ExtractPinData(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, pin=defaultNamedNotOptArg)`

#### `def ExtractPinData_2(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, pin=defaultNamedNotOptArg)`

#### `def ExtractPinData_3(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, pin=defaultNamedNotOptArg)`

#### `def ExtractPinData_4(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, pin=defaultNamedNotOptArg)`

#### `def FilterPinsByInstrumentType(self, pins=defaultNamedNotOptArg, instrumentTypeId=defaultNamedNotOptArg, capability=defaultNamedNotOptArg)`

#### `def GetAllInstrumentDefinitions(self, instrumentTypeId=defaultNamedNotOptArg, instrumentNames=pythoncom.Missing, channelGroupIds=pythoncom.Missing, channelLists=pythoncom.Missing)`

#### `def GetAllSessionData(self, instrumentTypeId=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelGroupIds=pythoncom.Missing, channelLists=pythoncom.Missing)`

#### `def GetChannelGroupAndChannelIndex(self, pins=defaultNamedNotOptArg, numberOfPinsPerChannelGroup=pythoncom.Missing, channelGroupIndices=pythoncom.Missing, channelIndices=pythoncom.Missing)`

#### `def GetChannelGroupAndChannelIndex_2(self, pinsInLookup=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, siteNumber=defaultNamedNotOptArg, channelGroupIndex=pythoncom.Missing, channelIndex=pythoncom.Missing)`

#### `def GetDAQmxAnalogOutputDataIndexesForMultipleTasksWithDifferentDataForEachSite(self, pinNames=defaultNamedNotOptArg, samplesPerSiteArrayLength=defaultNamedNotOptArg, samplesPerPinArrayLength=defaultNamedNotOptArg, parameterName=defaultNamedNotOptArg, perTaskChannelSiteIndexes=pythoncom.Missing, perTaskChannelPinIndexes=pythoncom.Missing, numberOfChannelsPerTask=pythoncom.Missing)`

#### `def GetDAQmxAnalogOutputDataIndexesForMultipleTasksWithSameDataForAllSites(self, pinNames=defaultNamedNotOptArg, samplesPerPinArrayLength=defaultNamedNotOptArg, parameterName=defaultNamedNotOptArg, perTaskChannelPinIndexes=pythoncom.Missing, numberOfChannelsPerTask=pythoncom.Missing)`

#### `def GetDAQmxAnalogOutputDataIndexesForSingleTaskWithDifferentDataForEachSite(self, pinNames=defaultNamedNotOptArg, samplesPerSiteArrayLength=defaultNamedNotOptArg, samplesPerPinArrayLength=defaultNamedNotOptArg, parameterName=defaultNamedNotOptArg, channelSiteIndexes=pythoncom.Missing, channelPinIndexes=pythoncom.Missing)`

#### `def GetDAQmxAnalogOutputDataIndexesForSingleTaskWithSameDataForAllSites(self, pinNames=defaultNamedNotOptArg, samplesPerPinArrayLength=defaultNamedNotOptArg, parameterName=defaultNamedNotOptArg, channelPinIndexes=pythoncom.Missing)`

#### `def GetDigitalPatternProjectCaptureWaveformFilePaths(self)`

#### `def GetDigitalPatternProjectLevelsFilePaths(self)`

#### `def GetDigitalPatternProjectPatternFilePaths(self)`

#### `def GetDigitalPatternProjectSourceWaveformFilePaths(self)`

#### `def GetDigitalPatternProjectSpecificationsFilePaths(self)`

#### `def GetDigitalPatternProjectTimingFilePaths(self)`

#### `def GetFPGAInstrumentNames(self, instrumentNames=pythoncom.Missing, fpgaFilePaths=pythoncom.Missing)`

#### `def GetFPGAVIReference(self, pin=defaultNamedNotOptArg)`

#### `def GetFPGAVIReferences(self, pin=defaultNamedNotOptArg)`

#### `def GetFPGAVIReferences_2(self)`

#### `def GetGlobalData(self, dataId=defaultNamedNotOptArg)`

#### `def GetInputDataBoolean(self, pin=defaultNamedNotOptArg, inputDataId=defaultNamedNotOptArg)`

#### `def GetInputDataDouble(self, pin=defaultNamedNotOptArg, inputDataId=defaultNamedNotOptArg)`

#### `def GetInputDataString(self, pin=defaultNamedNotOptArg, inputDataId=defaultNamedNotOptArg)`

#### `def GetInstrumentNameAndChannelForPinOnSingleSite(self, pinName=defaultNamedNotOptArg, instrumentName=pythoncom.Missing, channelOrPort=pythoncom.Missing)`

#### `def GetModelBasedInstrumentNames(self, category=defaultNamedNotOptArg, subcategory=defaultNamedNotOptArg)`

#### `def GetModelBasedInstrumentProperties(self, instrumentName=defaultNamedNotOptArg)`

#### `def GetModelBasedInstrumentResourceNames(self, instrumentName=defaultNamedNotOptArg)`

#### `def GetModelBasedInstrumentResourceProperties(self, instrumentName=defaultNamedNotOptArg)`

#### `def GetNI5530RFPortModuleNames(self, ni5530RFPortModuleNames=pythoncom.Missing, calibrationFilePaths=pythoncom.Missing)`

#### `def GetNI5530RFPortModuleSessions(self, ni5530RFPortModuleSessions=pythoncom.Missing, calibrationSessions=pythoncom.Missing)`

#### `def GetNI5530RFPortModuleSessions_2(self, pin=defaultNamedNotOptArg, semiconductorModuleContexts=pythoncom.Missing, ni5530RFPortModuleSessions=pythoncom.Missing, calibrationSessions=pythoncom.Missing, ni5530Channel1=pythoncom.Missing, ni5530Channel2=pythoncom.Missing)`

#### `def GetNI5530RFPortModuleSessions_3(self, pins=defaultNamedNotOptArg, semiconductorModuleContexts=pythoncom.Missing, ni5530RFPortModuleSessions=pythoncom.Missing, calibrationSessions=pythoncom.Missing, ni5530Channel1=pythoncom.Missing, ni5530Channel2=pythoncom.Missing)`

#### `def GetNIDAQmxTask(self, pin=defaultNamedNotOptArg, task=pythoncom.Missing, channelList=pythoncom.Missing)`

#### `def GetNIDAQmxTaskNames(self, taskType=defaultNamedNotOptArg, channelLists=pythoncom.Missing)`

#### `def GetNIDAQmxTask_2(self, pins=defaultNamedNotOptArg, task=pythoncom.Missing, channelList=pythoncom.Missing)`

#### `def GetNIDAQmxTasks(self, taskType=defaultNamedNotOptArg)`

#### `def GetNIDAQmxTasks_2(self, pin=defaultNamedNotOptArg, tasks=pythoncom.Missing, channelLists=pythoncom.Missing)`

#### `def GetNIDAQmxTasks_3(self, pins=defaultNamedNotOptArg, tasks=pythoncom.Missing, channelLists=pythoncom.Missing)`

#### `def GetNIDCPowerAlarmSession(self, session=defaultNamedNotOptArg)`

#### `def GetNIDCPowerInstrumentNames(self, channelLists=pythoncom.Missing)`

#### `def GetNIDCPowerResourceStrings(self)`

#### `def GetNIDCPowerSession(self, pin=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing)`

#### `def GetNIDCPowerSession_2(self, pins=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing)`

#### `def GetNIDCPowerSessions(self)`

#### `def GetNIDCPowerSessions_2(self, pin=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing)`

#### `def GetNIDCPowerSessions_3(self, pins=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing)`

#### `def GetNIDigitalPatternInstrumentNames(self)`

#### `def GetNIDigitalPatternSession(self, pinNames=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing, siteList=pythoncom.Missing)`

#### `def GetNIDigitalPatternSession_2(self, pinName=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing, siteList=pythoncom.Missing)`

#### `def GetNIDigitalPatternSessions(self)`

#### `def GetNIDigitalPatternSessions_2(self, pinNames=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing, siteLists=pythoncom.Missing)`

#### `def GetNIDigitalPatternSessions_3(self, pinName=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing, siteLists=pythoncom.Missing)`

#### `def GetNIDmmInstrumentNames(self)`

#### `def GetNIDmmSession(self, pin=defaultNamedNotOptArg)`

#### `def GetNIDmmSessions(self)`

#### `def GetNIDmmSessions_2(self, pin=defaultNamedNotOptArg)`

#### `def GetNIDmmSessions_3(self, pins=defaultNamedNotOptArg)`

#### `def GetNIFGenInstrumentNames(self)`

#### `def GetNIFGenSession(self, pin=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing)`

#### `def GetNIFGenSession_2(self, pins=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing)`

#### `def GetNIFGenSessions(self)`

#### `def GetNIFGenSessions_2(self, pin=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing)`

#### `def GetNIFGenSessions_3(self, pins=defaultNamedNotOptArg, session=pythoncom.Missing, channelLists=pythoncom.Missing)`

#### `def GetNIHSDIOChannelMasks(self, pins=defaultNamedNotOptArg, masks=pythoncom.Missing)`

#### `def GetNIHSDIOChannelMasks_2(self, pins=defaultNamedNotOptArg, masks=pythoncom.Missing)`

#### `def GetNIHSDIOInstrumentNames(self)`

#### `def GetNIHSDIOSession(self, pin=defaultNamedNotOptArg, acquisitionSession=pythoncom.Missing, generationSession=pythoncom.Missing, channelList=pythoncom.Missing)`

#### `def GetNIHSDIOSession_2(self, pins=defaultNamedNotOptArg, acquisitionSession=pythoncom.Missing, generationSession=pythoncom.Missing, channelList=pythoncom.Missing)`

#### `def GetNIHSDIOSessions(self, acquisitionSessions=pythoncom.Missing, generationSessions=pythoncom.Missing)`

#### `def GetNIHSDIOSessions_2(self, pin=defaultNamedNotOptArg, acquisitionSessions=pythoncom.Missing, generationSessions=pythoncom.Missing, channelLists=pythoncom.Missing)`

#### `def GetNIHSDIOSessions_3(self, pins=defaultNamedNotOptArg, acquisitionSessions=pythoncom.Missing, generationSessions=pythoncom.Missing, channelLists=pythoncom.Missing)`

#### `def GetNIRFPMDeembeddingDataForDutPins(self, sessions=pythoncom.Missing, portLists=pythoncom.Missing, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing)`

#### `def GetNIRFPMDeembeddingDataForSystemPins(self, sessions=pythoncom.Missing, portLists=pythoncom.Missing, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing)`

#### `def GetNIRFPMInstrumentNames(self, instrumentNames=pythoncom.Missing, calibrationFilePaths=pythoncom.Missing, iviSwitchNames=pythoncom.Missing, fpgaFilePaths=pythoncom.Missing)`

#### `def GetNIRFPMSession(self, systemPin=defaultNamedNotOptArg, session=pythoncom.Missing, port=pythoncom.Missing, deembeddingFilePath=pythoncom.Missing, deembeddingOrientation=pythoncom.Missing)`

#### `def GetNIRFPMSessions(self)`

#### `def GetNIRFPMSessions_2(self, pin=defaultNamedNotOptArg, semiconductorModuleContexts=pythoncom.Missing, sessions=pythoncom.Missing, portList=pythoncom.Missing, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing)`

#### `def GetNIRFPMSessions_3(self, pin1=defaultNamedNotOptArg, pin2=defaultNamedNotOptArg, semiconductorModuleContexts=pythoncom.Missing, sessions=pythoncom.Missing, portLists1=pythoncom.Missing, portLists2=pythoncom.Missing, deembeddingFilePaths1=pythoncom.Missing, deembeddingFilePaths2=pythoncom.Missing, deembeddingOrientations1=pythoncom.Missing, deembeddingOrientations2=pythoncom.Missing)`

#### `def GetNIRFPMSessions_4(self, pins=defaultNamedNotOptArg, semiconductorModuleContexts=pythoncom.Missing, sessions=pythoncom.Missing, portLists=pythoncom.Missing, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing)`

#### `def GetNIRFPMSessions_5(self, systemPins=defaultNamedNotOptArg, sessions=pythoncom.Missing, portList=pythoncom.Missing, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing)`

#### `def GetNIRFSADeembeddingData(self, pin=defaultNamedNotOptArg, deembeddingFilePath=pythoncom.Missing, deembeddingOrientation=pythoncom.Missing)`

#### `def GetNIRFSADeembeddingData_2(self, pin=defaultNamedNotOptArg, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing)`

#### `def GetNIRFSAInstrumentNames(self)`

#### `def GetNIRFSASession(self, pin=defaultNamedNotOptArg)`

#### `def GetNIRFSASession_2(self, pin=defaultNamedNotOptArg, port=pythoncom.Missing)`

#### `def GetNIRFSASessions(self)`

#### `def GetNIRFSASessions_2(self, pin=defaultNamedNotOptArg)`

#### `def GetNIRFSASessions_3(self, pin=defaultNamedNotOptArg, ports=pythoncom.Missing)`

#### `def GetNIRFSGDeembeddingData(self, pin=defaultNamedNotOptArg, deembeddingFilePath=pythoncom.Missing, deembeddingOrientation=pythoncom.Missing)`

#### `def GetNIRFSGDeembeddingData_2(self, pin=defaultNamedNotOptArg, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing)`

#### `def GetNIRFSGInstrumentNames(self)`

#### `def GetNIRFSGSession(self, pin=defaultNamedNotOptArg)`

#### `def GetNIRFSGSession_2(self, pin=defaultNamedNotOptArg, port=pythoncom.Missing)`

#### `def GetNIRFSGSessions(self)`

#### `def GetNIRFSGSessions_2(self, pin=defaultNamedNotOptArg)`

#### `def GetNIRFSGSessions_3(self, pin=defaultNamedNotOptArg, ports=pythoncom.Missing)`

#### `def GetNIRFmxDeembeddingData(self, pin=defaultNamedNotOptArg, deembeddingFilePath=pythoncom.Missing, deembeddingOrientation=pythoncom.Missing)`

#### `def GetNIRFmxDeembeddingData_2(self, pin=defaultNamedNotOptArg, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing)`

#### `def GetNIRFmxInstrumentNames(self)`

#### `def GetNIRFmxSession(self, pin=defaultNamedNotOptArg)`

#### `def GetNIRFmxSession_2(self, pin=defaultNamedNotOptArg, port=pythoncom.Missing)`

#### `def GetNIRFmxSessions(self)`

#### `def GetNIRFmxSessions_2(self, pin=defaultNamedNotOptArg)`

#### `def GetNIRFmxSessions_3(self, pin=defaultNamedNotOptArg, ports=pythoncom.Missing)`

#### `def GetNIRelayDriverModuleNames(self)`

#### `def GetNIRelayDriverSession(self, relay=defaultNamedNotOptArg, niSwitchSession=pythoncom.Missing, niSwitchRelayNames=pythoncom.Missing)`

#### `def GetNIRelayDriverSession_2(self, relays=defaultNamedNotOptArg, niSwitchSession=pythoncom.Missing, niSwitchRelayNames=pythoncom.Missing)`

#### `def GetNIRelayDriverSessions(self)`

#### `def GetNIRelayDriverSessions_2(self, relay=defaultNamedNotOptArg, niSwitchSessions=pythoncom.Missing, niSwitchRelayNames=pythoncom.Missing)`

#### `def GetNIRelayDriverSessions_3(self, relays=defaultNamedNotOptArg, niSwitchSessions=pythoncom.Missing, niSwitchRelayNames=pythoncom.Missing)`

#### `def GetNIScopeInstrumentNames(self)`

#### `def GetNIScopeSession(self, pin=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing)`

#### `def GetNIScopeSession_2(self, pins=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing)`

#### `def GetNIScopeSessions(self)`

#### `def GetNIScopeSessions_2(self, pin=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing)`

#### `def GetNIScopeSessions_3(self, pins=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing)`

#### `def GetPinNames(self, instrumentTypeId=defaultNamedNotOptArg, capability=defaultNamedNotOptArg, dutPinNames=pythoncom.Missing, systemPinNames=pythoncom.Missing)`

#### `def GetRelayDriverSessionsFromRelayConfiguration(self, configurationName=defaultNamedNotOptArg, sessionsForRelaysInOpenState=pythoncom.Missing, niSwitchRelayNamesForRelaysInOpenState=pythoncom.Missing, sessionsForRelaysInClosedState=pythoncom.Missing, niSwitchRelayNamesForRelaysInClosedState=pythoncom.Missing)`

#### `def GetRelayDriverSessionsFromRelays(self, relayNames=defaultNamedNotOptArg, switchRelayActionsAsIntegerArray=defaultNamedNotOptArg, sessionsForRelaysInOpenState=pythoncom.Missing, niSwitchRelayNamesForRelaysInOpenState=pythoncom.Missing, sessionsForRelaysInClosedState=pythoncom.Missing, niSwitchRelayNamesForRelaysInClosedState=pythoncom.Missing)`

#### `def GetRelayNames(self, siteRelayNames=pythoncom.Missing, systemRelayNames=pythoncom.Missing)`

#### `def GetRelaysInRelayGroups(self, relayGroups=defaultNamedNotOptArg)`

#### `def GetSemiconductorModuleContextWithSites(self, SiteNumbers=defaultNamedNotOptArg)`

#### `def GetSessionData(self, instrumentTypeId=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, sessionData=pythoncom.Missing, channelGroupIds=pythoncom.Missing, channelLists=pythoncom.Missing)`

#### `def GetSessionData_2(self, instrumentTypeId=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, sessionData=pythoncom.Missing, channelGroupId=pythoncom.Missing, channelList=pythoncom.Missing)`

#### `def GetSiteData(self, dataId=defaultNamedNotOptArg)`

#### `def GetSiteSemiconductorModuleContexts(self)`

#### `def GetSpecValue(self, symbol=defaultNamedNotOptArg)`

#### `def GetSpecValues(self, symbols=defaultNamedNotOptArg)`

#### `def GetSupportedAlarmNames(self, resourceString=defaultNamedNotOptArg)`

#### `def GetSwitchNames(self, switchTypeId=defaultNamedNotOptArg)`

#### `def GetSwitchSessions(self, switchTypeId=defaultNamedNotOptArg)`

#### `def GetSwitchSessions_2(self, switchTypeId=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, semiconductorModuleContexts=pythoncom.Missing, switchSessions=pythoncom.Missing, switchRoute=pythoncom.Missing)`

#### `def GlobalDataExists(self, dataId=defaultNamedNotOptArg)`

#### `def PerInstrumentToPerSiteData(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg)`

#### `def PerInstrumentToPerSiteData2D(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg)`

#### `def PerInstrumentToPerSiteData2D_2(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg)`

#### `def PerInstrumentToPerSiteData_2(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg)`

#### `def PerInstrumentToPerSitePatternResults(self, pins=defaultNamedNotOptArg, patternResults=defaultNamedNotOptArg)`

#### `def PerInstrumentToPerSiteWaveforms(self, pins=defaultNamedNotOptArg, instrumentWaveforms=defaultNamedNotOptArg)`

#### `def PerSiteToPerInstrumentWaveforms(self, pins=defaultNamedNotOptArg, perSiteWaveforms=defaultNamedNotOptArg)`

#### `def Publish(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg)`

#### `def PublishHistoryRamCycleInformation(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, sessionIndex=defaultNamedNotOptArg, siteIndex=defaultNamedNotOptArg, patternName=defaultNamedNotOptArg, timeSetName=defaultNamedNotOptArg, vectorNumber=defaultNamedNotOptArg, cycleNumber=defaultNamedNotOptArg, expectedPinStates=defaultNamedNotOptArg, actualPinStates=defaultNamedNotOptArg, perPinPassFail=defaultNamedNotOptArg)`

#### `def PublishPatternResults(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, patternResults=defaultNamedNotOptArg)`

#### `def PublishPatternResults_2(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, patternResults=defaultNamedNotOptArg)`

#### `def PublishPerSite(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg)`

#### `def PublishPerSite_2(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg)`

#### `def PublishPerSite_3(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg)`

#### `def PublishPerSite_4(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg)`

#### `def PublishPerSite_5(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg)`

#### `def PublishPerSite_6(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg)`

#### `def PublishPinNamesForHistoryRamCycleInformation(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, pinNames=defaultNamedNotOptArg)`

#### `def PublishToTestStandVariablePerSite(self, expression=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg)`

#### `def PublishToTestStandVariablePerSite_2(self, expression=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg)`

#### `def PublishToTestStandVariablePerSite_3(self, expression=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg)`

#### `def PublishToTestStandVariablePerSite_4(self, expression=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg)`

#### `def PublishToTestStandVariablePerSite_5(self, expression=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg)`

#### `def PublishToTestStandVariablePerSite_6(self, expression=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg)`

#### `def Publish_10(self, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg)`

#### `def Publish_11(self, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg)`

#### `def Publish_2(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg)`

#### `def Publish_3(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg)`

#### `def Publish_4(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg)`

#### `def Publish_5(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg)`

#### `def Publish_6(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg)`

#### `def Publish_7(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg)`

#### `def Publish_8(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg)`

#### `def Publish_9(self, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg)`

#### `def ReportError(self, errorCode=defaultNamedNotOptArg, parameters=defaultNamedNotOptArg)`

#### `def ReportIncompatibleArrayLengths(self, arrayParameterName1=defaultNamedNotOptArg, arrayParameterName2=defaultNamedNotOptArg)`

#### `def ReportInvalidArray(self, parameterName=defaultNamedNotOptArg, elementType=defaultNamedNotOptArg)`

#### `def ReportInvalidTimeToWait(self, parameterName=defaultNamedNotOptArg)`

#### `def ReportMissingDriver(self, driverName=defaultNamedNotOptArg)`

#### `def ReportUnsupportedCapability(self, capability=defaultNamedNotOptArg)`

#### `def SetFPGAVIReference(self, instrumentName=defaultNamedNotOptArg, fpgaVIReference=defaultNamedNotOptArg)`

#### `def SetGlobalData(self, dataId=defaultNamedNotOptArg, data=defaultNamedNotOptArg)`

#### `def SetNI5530RFPortModuleSession(self, ni5530RFPortModuleName=defaultNamedNotOptArg, ni5530RFPortModuleSession=defaultNamedNotOptArg, calibrationSession=defaultNamedNotOptArg)`

#### `def SetNIDAQmxTask(self, taskName=defaultNamedNotOptArg, task=defaultNamedNotOptArg)`

#### `def SetNIDCPowerSession(self, instrumentName=defaultNamedNotOptArg, channelId=defaultNamedNotOptArg, session=defaultNamedNotOptArg)`

#### `def SetNIDCPowerSession_2(self, resourceString=defaultNamedNotOptArg, session=defaultNamedNotOptArg, alarmNames=defaultNamedNotOptArg, alarmSession=defaultNamedNotOptArg)`

#### `def SetNIDCPowerSession_3(self, instrumentName=defaultNamedNotOptArg, channelId=defaultNamedNotOptArg, session=defaultNamedNotOptArg, alarmNames=defaultNamedNotOptArg, alarmSession=defaultNamedNotOptArg)`

#### `def SetNIDigitalPatternSession(self, instrumentName=defaultNamedNotOptArg, session=defaultNamedNotOptArg)`

#### `def SetNIDmmSession(self, instrumentName=defaultNamedNotOptArg, instrumentSession=defaultNamedNotOptArg)`

#### `def SetNIFGenSession(self, instrumentName=defaultNamedNotOptArg, session=defaultNamedNotOptArg)`

#### `def SetNIHSDIOSessions(self, instrumentName=defaultNamedNotOptArg, acquisitionSession=defaultNamedNotOptArg, generationSession=defaultNamedNotOptArg)`

#### `def SetNIRFPMSession(self, instrumentName=defaultNamedNotOptArg, instrumentSession=defaultNamedNotOptArg)`

#### `def SetNIRFSASession(self, instrumentName=defaultNamedNotOptArg, instrumentSession=defaultNamedNotOptArg)`

#### `def SetNIRFSGSession(self, instrumentName=defaultNamedNotOptArg, instrumentSession=defaultNamedNotOptArg)`

#### `def SetNIRFmxSession(self, instrumentName=defaultNamedNotOptArg, instrumentSession=defaultNamedNotOptArg)`

#### `def SetNIRelayDriverSession(self, relayDriverName=defaultNamedNotOptArg, niSwitchSession=defaultNamedNotOptArg)`

#### `def SetNIScopeSession(self, instrumentName=defaultNamedNotOptArg, session=defaultNamedNotOptArg)`

#### `def SetSessionData(self, instrumentTypeId=defaultNamedNotOptArg, instrumentName=defaultNamedNotOptArg, channelGroupId=defaultNamedNotOptArg, sessionData=defaultNamedNotOptArg)`

#### `def SetSiteData(self, dataId=defaultNamedNotOptArg, data=defaultNamedNotOptArg)`

#### `def SetSiteData_2(self, dataId=defaultNamedNotOptArg, data=defaultNamedNotOptArg)`

#### `def SetSwitchSession(self, switchTypeId=defaultNamedNotOptArg, switchName=defaultNamedNotOptArg, switchSession=defaultNamedNotOptArg)`

#### `def SiteDataExists(self, dataId=defaultNamedNotOptArg)`

#### `def __iter__(self)`

Return a Python iterator for this object

<!--NI_PYTHON_API repo=nitsm-python path=src/nitsm/codemoduleapi.py -->
## PYTHON MODULE: src/nitsm/codemoduleapi.py

### MODULE DOCSTRING

Code Module API

- `__all__ = ['SemiconductorModuleContext', 'Capability', 'InstrumentTypeIdConstants', 'code_module']`

### `class code_module()`

This function decorator wraps the ISemiconductorModuleContext
    win32com.client.dynamic.CDispatch object passed from the Semiconductor Multi Test step into a
    nitsm.codemoduleapi.SemiconductorModuleContext object prior to calling the decorated function.
    

#### `def __init__(self, func)`

Converts a function into a TSM code module.

        The Semiconductor Multi Test step must pass the Step.SemiconductorModuleContext property to
        the code module as the first positional argument.
        

#### `def __get__(self, instance, owner)`

Binds the code module to an object or class.

#### `def __call__(self, *args, **kwargs)`

Calls the code module.

<!--NI_PYTHON_API repo=nitsm-python path=src/nitsm/debug.py -->
## PYTHON MODULE: src/nitsm/debug.py

### MODULE DOCSTRING

Code Module Debugging Utilities

### `def prompt_attach_debugger() -> None`

Pauses the Python interpreter and displays the process ID (PID). The PID can be used by an
    IDE such as PyCharm to attach to the process for debugging. This is useful for stepping into
    nitsm code modules from TestStand.

    Instructions for use with PyCharm:
        1. Call this function from the code module you want to debug. Placing it at the beginning
            of the code module is recommended.
        2. Add a breakpoint at the location where you want to start debugging. Make sure this
            breakpoint will be reached after this function is called.
        3. In TestStand, execute a sequence that calls into the code module.
        4. A dialog box will appear displaying the PID of the current process. Before clicking
            "Okay" on the dialog, select Run -> Attach To Process... from the PyCharm menu.
        5. PyCharm will display a window of discovered processes. Click the process with the
            matching PID.
        6. PyCharm will open a debug terminal and attach to the process. Wait for PyCharm to
            indicate it has successfully attached.
        6. Once PyCharm is attached, click "Okay" on the dialog to continue execution. If these
            steps were performed correctly, PyCharm will break at the first breakpoint it reaches in
            the code.
    

<!--NI_PYTHON_API repo=nitsm-python path=src/nitsm/enums.py -->
## PYTHON MODULE: src/nitsm/enums.py

### MODULE DOCSTRING

Enumerations

- `__all__ = ['Capability', 'InstrumentTypeIdConstants']`

### `class Capability(enum.Enum)`

Differentiates between pins in the same instrument with different capabilities, such as
    NI-HSDIO Dynamic DIO channels and PFI lines.
    

### `class InstrumentTypeIdConstants(enum.Enum)`

The type IDs for non-custom instruments in the pin map file.

<!--NI_PYTHON_API repo=nitsm-python path=src/nitsm/pinquerycontexts.py -->
## PYTHON MODULE: src/nitsm/pinquerycontexts.py

### MODULE DOCSTRING

Pin Query Contexts

- `__all__ = ['PinQueryContext', 'DigitalPatternPinQueryContext']`

### `def _pad_jagged_sequence(seq)`

Pads a 2D jagged sequence with the default value of the element type to make it rectangular.

    The type of each sequence (tuple, list, etc) is maintained.
    

### `class PinQueryContext()`

Provides the base class for a pin query context, which is an object a pin query method
    returns to track the sessions and channels associated with the pins for one or more sites.
    

#### `def __init__(self, tsm_context, pins)`

Not for public use.

#### `def get_session_and_channel_index(self, site_number: int, pin: str)`

Returns the index of the session and channel that corresponds to a pin query. Use this
        method to access an individual pin on a specific site when you take a measurement across
        multiple instruments. When you call a pin query method, such as
        pins_to_nidigital_sessions_for_ppmu, the method returns a tuple of sessions and a tuple of
        channel lists. Use this method to identify which session and which channel refers to the pin
        from the pin query and the site number you specify.

        Args:
            site_number: The site number of the pin to obtain the session and channel index in a
                previous pin query. For a system pin, pass any valid site number.
            pin: The name of the pin to obtain the session and channel index in a previous pin
                query.

        Returns:
            session_index: Returns the index of the session for a measurement taken on the pin and
                site number you specify.
            channel_index: Returns the index of the channel within the channel list for a
                measurement taken on the pin and site number you specify.
        

#### `def publish(self, data: '_PublishDataArg', published_data_id='')`

Publishes the measurement data for one or more pins to the Semiconductor Multi Test step
        for all sites in the PinQueryContext.

        Args:
            data: The measurement data from one or more pins connected to one or more instruments.
                The values can be bools, ints, or floats, and each value represents a measurement
                made for a single instrument channel. Pass a single value if the pin query refers
                to a single channel on a single instrument. Pass a sequence of values if the pin
                query refers to multiple channels on a single instrument or multiple instruments
                with a single channel. Pass a two dimensional sequence of values if the pin query
                refers to multiple channels on multiple instruments.
            published_data_id: The unique ID for distinguishing the measurement when you publish
                multiple measurements for the same pins within the same code module. This ID must
                match one of the values in the Published Data Id column on the Tests tab of the
                Semiconductor Multi Test step.
        

#### `def _publish_float_scalar(self, data, published_data_id)`

#### `def _publish_bool_scalar(self, data, published_data_id)`

#### `def _publish_sequence(self, data, published_data_id)`

#### `def _publish_float_1d(self, data, published_data_id)`

#### `def _publish_bool_1d(self, data, published_data_id)`

#### `def _publish_sequence_2d(self, data, published_data_id)`

#### `def _publish_float_2d(self, data, published_data_id)`

#### `def _publish_bool_2d(self, data, published_data_id)`

### `class DigitalPatternPinQueryContext(PinQueryContext)`

An object the pins_to_nidigital_session_for_pattern and
    pins_to_nidigital_sessions_for_pattern methods return to track the sessions and channels
    associated with the pins for one or more sites. Use this object to publish measurements to the
    Semiconductor Multi Test step and to extract data from a set of measurements.
    

#### `def __init__(self, tsm_context, pins, site_lists)`

Not for public use.

#### `def publish_pattern_results(self, instrument_site_pattern_results: '_PublishPatternArg', published_data_id='')`

Publishes results from NI-Digital pattern burst to the Semiconductor Multi Test step for
        all sites in the Semiconductor Module context. Leave the Pin column blank for the test on
        the Semiconductor Multi Test step when publishing pattern results with this method.

        Args:
            instrument_site_pattern_results: The pattern result data from multiple pins connected to
                one or more NI-Digital Pattern instruments. Provide a dictionary that maps sites to
                result data to publish pattern results from a single NI-Digital Pattern instrument
                session. Provide a sequence of dictionaries that map sites to result data to publish
                pattern results from multiple NI-Digital Pattern instrument sessions. Each element
                in the sequence contains pattern results for the sites of a single instrument
                session. Furthermore, the size of the sequence must be the same size as the session
                data output from the pin query method.
            published_data_id: The unique ID for identifying the results. This ID must match one of
                the values in the Published Data Id column on the Tests tab of the Semiconductor
                Multi Test step.
        

<!--NI_PYTHON_API repo=nitsm-python path=src/nitsm/tsmcontext.py -->
## PYTHON MODULE: src/nitsm/tsmcontext.py

### MODULE DOCSTRING

TSM Context Wrapper

- `__all__ = ['SemiconductorModuleContext']`

### `class SemiconductorModuleContext()`

Provides a pythonic interface to an instance of ISemiconductorModuleContext.

    The Semiconductor Multi Test step creates an ISemiconductorModuleContext object that
    describes a subset of pins, relays, sites, and instruments on a test system for the instance of
    the multisite code module. Pass the Step.SemiconductorModuleContext property to the code module
    as an ISemiconductorModuleContext interface to write a test for multisite situations.
    

#### `def __init__(self, tsm_dispatch: '_ISemiconductorModuleContext')`

Wraps an instance of ISemiconductorModuleContext.

        Args:
            tsm_dispatch: The win32com.client.dynamic.CDispatch object provided by TestStand.
        

#### `def get_pin_names(self, instrument_type_id: '_InstrTypeIdArg'=nitsm.enums.InstrumentTypeIdConstants.ANY, capability: '_CapabilityArg'=nitsm.enums.Capability.ALL) -> '_Tuple[_StringTuple, _StringTuple]'`

Returns all DUT and system pins available in the Semiconductor Module context that are
        connected to an instrument of the type you specify in the instrument_type_id. This method
        returns only the pins specified on the Options tab of the Semiconductor Multi Test step.
        Pass an empty string to instrument_type_id to return all available pins.

        Args:
            instrument_type_id: Specifies the type of instrument for which you want to return DUT
                and system pins. All instruments defined in the pin map specify an associated type
                ID. The nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type
                IDs for instrument types that TSM supports natively. For all other types of
                instruments, you must define a type ID for the instrument in the pin map file.
                Typically, this type ID is an instrument driver name or other ID that is common for
                instruments that users program in a similar way. Pass InstrumentTypeIdConstants.ANY
                to include pins from all instruments.
            capability: Limits the filtered pins to those connected to a channel that defines the
                capability you specify. Use capability to differentiate between pins in the same
                instrument with different capabilities, such as NI-HSDIO Dynamic DIO channels and
                PFI lines. If a pin is connected to channels in which the capability is defined only
                for a subset of sites, the method raises an exception. Pass Capability.ALL to return
                all pins that match instrument_type_id.

        Returns:
            dut_pins: Returns a tuple of strings that contains the DUT pins in the Semiconductor
                Module context that are connected to an instrument of the type you specify in the
                instrument_type_id.
            system_pins: Returns a tuple of strings that contains the system pins in the
                Semiconductor Module context that are connected to an instrument of the type you
                specify in the instrument_type_id.
        

#### `def filter_pins_by_instrument_type(self, pins: '_Sequence[str]', instrument_type_id: '_InstrTypeIdArg', capability: '_CapabilityArg') -> '_StringTuple'`

Filters pins by instrument_type_id. Pass a list of all pins or pin groups to return the
        pins connected to instruments of the type you specify in the instrument_type_id. If no pins
        are connected to instruments of the type you specify in instrument_type_id, this method
        returns an empty tuple. The return value is a tuple subset of pin names in pins that are
        connected to an instrument of the filtered instrument_type_id.

        Args:
            pins: A sequence of pins or pin groups to filter. The sequence must contain only pins or
                pin groups that are included in the Semiconductor Module context.
            instrument_type_id: The type of instrument for which you want to return DUT and system
                pins. All instruments defined in the pin map specify an associated type ID. The
                nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for
                instrument types that TSM supports natively. For all other types of instruments, you
                must define a type ID for the instrument in the pin map file. Typically, this type
                ID is an instrument driver name or other ID that is common for instruments that
                users program in a similar way. Pass InstrumentTypeIdConstants.ANY to include pins
                from all instruments.
            capability: Limits the filtered pins to those connected to a channel that defines the
                capability you specify. Use capability to differentiate between pins in the same
                instrument with different capabilities, such as NI-HSDIO Dynamic DIO channels and
                PFI lines. If a pin is connected to channels in which the capability is defined only
                for a subset of sites, the method raises an exception. Pass Capability.ALL to return
                all elements in pins that match instrument_type_id.

        Returns:
            Returns a tuple subset of pin names in the pins that are connected to an instrument of
            the filtered instrument_type_id.
        

#### `def get_pins_in_pin_groups(self, pin_groups: '_PinsArg') -> '_StringTuple'`

Returns a tuple of pins contained in the pin group(s) you specify in the pin_group(s).

        Args:
            pin_groups: A pin group or a sequence of pin groups. The pin group(s) must contain only
                pin groups that are included in the Semiconductor Module context.
        

#### `def site_numbers(self) -> '_Tuple[int, ...]'`

Returns the site numbers in the Semiconductor Module context. The site numbers can be
        different each time a step executes because some sites might not be active. The site numbers
        are in numerical order.
        

#### `def get_semiconductor_module_context_with_sites(self, site_numbers: '_Sequence[int]') -> 'SemiconductorModuleContext'`

Returns a Semiconductor Module context object which holds information and resources
        specific to the site_numbers mentioned.

        Args:
            site_numbers: A sequence of site numbers for which the resources should be used.

        Returns:
            SemiconductorModuleContext object with resources specific to the site_numbers.
        

#### `def set_site_data(self, data_id: str, data: '_Sequence[_Any]') -> None`

Associates a data item with each site. You can associate data with all sites or with the
        sub-set of sites in the Semiconductor Module context. You can use this method to store
        per-site data you initialize in a central location but access within each site. The data
        item is accessible from a process model controller execution and the site with which the
        data is associated. This method supports only basic data types and sequences of basic
        data types that can be represented by a COM VARIANT.

        Args:
            data_id: A unique ID to distinguish the data.
            data: A sequence of data with one element for each site in the system or one element for
                each site in the Semiconductor Module context. If the sequence is None or empty, the
                method deletes any data with the specified data_id if it exists. If the sequence
                contains data for each site in the Semiconductor Module context, each item in the
                sequence contains data for the site specified by the corresponding item in the
                site_numbers property.
        

#### `def get_site_data(self, data_id: str) -> '_Tuple[_Any, ...]'`

Returns per-site data that a previous call to the set_site_data method stores. The
        returned tuple contains the data the Semiconductor Module context stores for each site in
        the same order as the sites that the site_numbers property returns. Raises an exception if a
        data item with the specified data_id does not exist for every site in the Semiconductor
        Module context. Use the site_data_exists method to determine if the specified data_id
        exists.

        Args:
            data_id: The unique ID to distinguish the data. This parameter must match a value you
                specify in a call to the set_site_data method.
        

#### `def site_data_exists(self, data_id: str) -> bool`

Returns a Boolean value indicating whether site data exists for the data ID specified by
        the data_id . Raises an exception if a data item with the specified data_id exists for some,
        but not all, sites in the Semiconductor Module context.

        Args:
            data_id: A unique ID to distinguish the data.
        

#### `def set_global_data(self, data_id: str, data: '_Any') -> None`

Associates a data item with a data_id. You can use this method to store data you
        initialize in a central location but access from multiple sites. The data item is accessible
        from a process model controller execution and all of its test socket executions. This method
        supports only basic data types and sequences of basic data types that can be represented by
        a COM VARIANT.

        Args:
            data_id: A unique ID to distinguish the data.
            data: A data item to store and later retrieve using the specified data_id . If the data
                item is None, the method deletes the data with the specified data_id if it exists.
        

#### `def get_global_data(self, data_id: str) -> '_Any'`

Returns a global data item that a previous call to the set_global_data method stores.
        Throws an exception if no data item with the specified data_id exists. Use the
        global_data_exists method to determine if the specified data_id exists.

        Args:
            data_id: The unique ID to distinguish the data. This parameter must match a value you
                specify in a call to the set_global_data method.
        

#### `def global_data_exists(self, data_id: str) -> bool`

Returns a Boolean value indicating whether global data exists for the data ID specified
        by the data_id.

        Args:
            data_id: A unique ID to distinguish the data.
        

#### `def get_all_nidigital_instrument_names(self) -> '_StringTuple'`

Returns a tuple of instrument names and comma-separated lists of instrument names that
        belong to the same group for all NI-Digital Pattern instruments in the Semiconductor Module
        context. You can use the instrument names and comma-separated lists of instrument names to
        open driver sessions.
        

#### `def set_nidigital_session(self, instrument_name: str, session: 'nidigital.Session') -> None`

Associates an instrument session with an NI-Digital Pattern instrument_name.

        Args:
            instrument_name: The instrument name in the pin map file for the corresponding session.
            session: The instrument session for the corresponding instrument_name.
        

#### `def get_all_nidigital_sessions(self) -> '_Tuple[nidigital.Session, ...]'`

Returns all NI-Digital Pattern instrument sessions in the Semiconductor Module context.
        You can use instrument sessions to close driver sessions.
        

#### `def pins_to_nidigital_session_for_ppmu(self, pins: '_PinsArg') -> '_NIDigitalSingleSessionPpmuQuery'`

Returns the NI-Digital Pattern session and pin_set_string required to perform PPMU
        operations on pin(s). If more than one session is required to access the pin(s), the method
        raises an exception. Each group of NI-Digital Pattern instruments in the pin map creates a
        single instrument session.

        Args:
            pins: The name of the pin(s) or pin group(s) to translate to session and pin_set_string.

        Returns:
            pin_query_context: An object that tracks the session and channels associated with this
                pin query. Use this object to publish measurements and extract data from a set of
                measurements.
            session: Returns the NI-Digital Pattern instrument session for the instruments connected
                to pin(s) for all sites in the Semiconductor Module context.
            pin_set_string: Returns the pin set string for each instrument session required to
                access the pin(s) for all sites in the Semiconductor Module context. The pin set is
                specified by site and pin e.g. "site0/A" as expected by the NI-Digital Pattern
                driver. If any of the pin(s) are connected to the same instrument channel for
                multiple sites, the channel appears only once in the string and is identified by one
                of the site/pin combinations to which it is connected.
        

#### `def pins_to_nidigital_sessions_for_ppmu(self, pins: '_PinsArg') -> '_NIDigitalMultipleSessionPpmuQuery'`

Returns the NI-Digital Pattern sessions and pin_set_strings required to perform PPMU
        operations on pin(s).

        Args:
            pins: The name of the pin(s) or pin group(s) to translate to sessions and
                pin_set_strings.

        Returns:
            pin_query_context: An object that tracks the sessions and channels associated with this
                pin query. Use this object to publish measurements and extract data from a set of
                measurements.
            sessions: Returns the NI-Digital Pattern instrument sessions for the instruments
                connected to pin(s) for all sites in the Semiconductor Module context.
            pin_set_strings: Returns the pin set strings for each instrument session required to
                access the pin(s) for all sites in the Semiconductor Module context. The pin sets
                are specified by site and pin e.g. "site0/A" as expected by the NI-Digital Pattern
                driver. If any of the pin(s) are connected to the same instrument channel for
                multiple sites, the channel appears only once in the string and is identified by one
                of the site/pin combinations to which it is connected.
        

#### `def pins_to_nidigital_session_for_pattern(self, pins: '_PinsArg') -> '_NIDigitalSingleSessionPatternQuery'`

Returns the NI-Digital Pattern session and site_list required to perform pattern
        operations for patterns that use the pin(s). If more than one session is required to access
        the pin(s), the method raises an exception. Each group of NI-Digital Pattern instruments in
        the pin map creates a single instrument session.

        Args:
            pins: The name of the pin(s) or pin group(s) to translate to session and site_list.

        Returns:
            pin_query_context: An object that tracks the session and channels associated with this
                pin query. Use this object to publish measurements and extract data from a set of
                measurements.
            session: Returns the NI-Digital Pattern instrument session for the instruments
                connected to pin(s) for all sites in the Semiconductor Module context.
            site_list: Returns a string that is a comma-separated list of sites (e.g. "site0,site1")
                that correspond to the sites in the Semiconductor Module context. This site_list is
                needed as an input to certain NI-Digital Pattern driver calls.
        

#### `def pins_to_nidigital_sessions_for_pattern(self, pins: '_PinsArg') -> '_NIDigitalMultipleSessionPatternQuery'`

Returns the NI-Digital Pattern sessions and site_lists required to perform pattern
        operations for patterns that use the pin(s).

        Args:
            pins: The name of the pin(s) or pin group(s) to translate to sessions and site_lists.

        Returns:
            pin_query_context: An object that tracks the sessions and channels associated with this
                pin query. Use this object to publish measurements and extract data from a set of
                measurements.
            sessions: Returns the NI-Digital Pattern instrument sessions for the instruments
                connected to pin(s) for all sites in the Semiconductor Module context.
            site_lists: Returns a tuple of comma-separated lists of sites (e.g. "site0,site1") that
                correspond to the sites in the Semiconductor Module context. This site_list is
                needed as an input to certain NI-Digital Pattern driver calls.
        

#### `def pin_map_file_path(self) -> str`

The absolute path to the pin map file for this Semiconductor Module context.

#### `def nidigital_project_specifications_file_paths(self) -> '_StringTuple'`

The absolute paths to the Specifications files in the Digital Pattern Project associated
        with this Semiconductor Module context.
        

#### `def nidigital_project_levels_file_paths(self) -> '_StringTuple'`

The absolute paths to the Levels file in the Digital Pattern Project associated with this
        Semiconductor Module context.
        

#### `def nidigital_project_timing_file_paths(self) -> '_StringTuple'`

The absolute paths to the Timing files in the Digital Pattern Project associated with
        this Semiconductor Module context.
        

#### `def nidigital_project_pattern_file_paths(self) -> '_StringTuple'`

The absolute paths to the Pattern files in the Digital Pattern Project associated with
        this Semiconductor Module context.
        

#### `def nidigital_project_source_waveform_file_paths(self) -> '_StringTuple'`

The absolute paths to the Source Waveform files in the Digital Pattern Project associated
        with this Semiconductor Module context.
        

#### `def nidigital_project_capture_waveform_file_paths(self) -> '_StringTuple'`

The absolute paths to the Capture Waveform files in the Digital Pattern Project
        associated with this Semiconductor Module context.
        

#### `def get_all_nidcpower_resource_strings(self) -> '_StringTuple'`

Returns the resource strings associated with each channel group in the Semiconductor
        Module context. A resource string is a comma-separated list of NI-DCPower resources, where
        each resource is defined by the <instrument>/<channel> associated with the NI-DCPower
        channel group. You can use the resource strings to open driver sessions. The same session
        controls all resources within the same resource string. This method supports only DC Power
        instruments defined with ChannelGroups in the pin map.

        Returns:
            Returns a tuple of the NI-DCPower resource strings.
        

#### `def set_nidcpower_session(self, resource_string: str, session: 'nidcpower.Session')`

Associates an NI-DCPower session with all resources of an NI-DCPower resource_string.
        This method supports only DC Power instruments defined with ChannelGroups in the pin map.

        Args:
            resource_string: The resource string associated with the corresponding session. The
                resource string is a comma-separated list of resources, where each resource is
                defined as <instrument>/<channel>.
            session: The NI-DCPower session for the corresponding resource_string.
        

#### `def get_all_nidcpower_sessions(self) -> '_Tuple[nidcpower.Session, ...]'`

Returns all NI-DCPower instrument sessions in the Semiconductor Module context.
        You can use instrument sessions to close driver sessions.
        

#### `def pins_to_nidcpower_session(self, pins: '_PinsArg') -> '_NIDCPowerSingleSessionQuery'`

Returns the NI-DCPower session and channel_string required to access the pin(s) on all
        sites in the Semiconductor Module context. If multiple sessions are required to access the
        pin(s), the method raises an exception.

        Args:
            pins: The name(s) of the pin(s) or pin group(s) to translate to a session and
                channel_string.

        Returns:
            pin_query_context: An object that tracks the session and channels associated with this
                pin query. Use this object to publish measurements and extract data from a set of
                measurements.
            session: Returns the NI-DCPower instrument session for the instruments and channels
                connected to pin(s) for all sites in the Semiconductor Module context.
            channel_string: Returns the channel string for the NI-DCPower session required to access
                the pin(s) for all sites in the Semiconductor Module context. The channel string is
                a comma-separated list of resources, where each resource is defined as
                <instrument>/<channel>.
        

#### `def pins_to_nidcpower_sessions(self, pins: '_PinsArg') -> '_NIDCPowerMultipleSessionQuery'`

Returns the NI-DCPower sessions and channel_strings required to access the pin(s).

        Args:
            pins: The name(s) of the pin(s) or pin group(s) to translate to sessions and
                channel_strings.

        Returns:
            pin_query_context: An object that tracks the sessions and channels associated with this
                pin query. Use this object to publish measurements and extract data from a set of
                measurements.
            sessions: Returns the NI-DCPower instrument sessions for the instruments and channel
                resources connected to pin(s) for all sites in the Semiconductor Module context.
            channel_strings: Returns the channel strings for each instrument session required to
                access the pin(s) for all sites in the Semiconductor Module context. Each channel
                string is a comma-separated list of channels, where each channel is defined as
                <instrument>/<channel>.
        

#### `def get_all_nidaqmx_task_names(self, task_type: str) -> '_Tuple[_StringTuple, _StringTuple]'`

Returns a tuple of all NI-DAQmx task names and channel lists in the Semiconductor Module
        context. You can use the task names to create DAQmx tasks.

        Args:
            task_type: Specifies the type of NI-DAQmx task to return. Use an empty string to obtain
                the names of all tasks regardless of task type.

        Returns:
            task_names: Returns a tuple of the NI-DAQmx task names.
            channel_lists: Returns a tuple of the NI-DAQmx physical channel names for all channels
                in the Semiconductor Module context.
        

#### `def set_nidaqmx_task(self, task_name: str, task: 'nidaqmx.Task') -> None`

Associates an NI-DAQmx task with an NI-DAQmx task name defined in the pin map.

        Args:
            task_name: The task name in the pin map file for the corresponding task.
            task: The DAQmx task for the corresponding task name.
        

#### `def get_all_nidaqmx_tasks(self, task_type: str) -> '_Tuple[nidaqmx.Task, ...]'`

Returns a tuple of all NI-DAQmx tasks in the Semiconductor Module context whose task type
        matches task_type. You can use tasks to perform NI-DAQmx operations.

        Args:
            task_type: Specifies the type of NI-DAQmx task to return. Use an empty string to obtain
                the names of all tasks regardless of task type.
        

#### `def pins_to_nidaqmx_task(self, pins: '_PinsArg') -> '_NIDAQmxSingleSessionQuery'`

Returns the NI-DAQmx task and available channels list required to access the pin(s). If
        more than one task is required, the method raises an exception.

        Args:
            pins: The name of the pin(s) or pin group(s) to translate to a task.

        Returns:
            pin_query_context: An object that tracks the task associated with this pin query. Use
                this object to publish measurements and extract data from a set of measurements.
            task: Returns the NI-DAQmx task associated with the pin(s) or pin group(s) for all sites
                in the Semiconductor Module context.
            channel_list: Returns the comma-separated list of channels in the task associated with
                the pin(s) or pin group(s) for all sites in the Semiconductor Module context. Use
                the channel list to set the channels to read from for an input task or as an input
                to one of the per task data methods associated with this pin query context for an
                output task. If any of the pins are connected to the same instrument channel for
                multiple sites, the channel appears only once in the list.
        

#### `def pins_to_nidaqmx_tasks(self, pins: '_PinsArg') -> '_NIDAQmxMultipleSessionQuery'`

Returns the NI-DAQmx tasks and available channels lists required to access the pin(s) or
        pin group(s).

        Args:
            pins: The name of the pin(s) or pin group(s) to translate to a set of tasks.

        Returns:
            pin_query_context: An object that tracks the tasks associated with this pin query. Use
                this object to publish measurements and extract data from a set of measurements.
            tasks: Returns the NI-DAQmx tasks associated with the pin(s) or pin group(s) for all
                sites in the Semiconductor Module context.
            channel_lists: Returns the comma-separated lists of channels in the tasks associated
                with the pin(s) or pin group(s) for all sites in the Semiconductor Module context.
                Use the channel lists to set the channels to read from for input tasks or as an
                input to one of the per task data methods associated with this pin query context for
                output tasks. If any of the pin(s) are connected to the same instrument channel for
                multiple sites, the channel appears only once in the list.
        

#### `def get_all_nidmm_instrument_names(self) -> '_StringTuple'`

Returns a tuple of all NI-DMM instrument names in the Semiconductor Module context. You
        can use instrument names to open driver sessions.
        

#### `def set_nidmm_session(self, instrument_name: str, session: 'nidmm.Session') -> None`

Associates an instrument session with an NI-DMM instrument name.

        Args:
            instrument_name: The instrument name in the pin map file for the corresponding session.
            session: The instrument session for the corresponding instrument name.
        

#### `def get_all_nidmm_sessions(self) -> '_Tuple[nidmm.Session, ...]'`

Returns a tuple of all NI-DMM instrument sessions in the Semiconductor Module context.
        You can use instrument sessions to close driver sessions.
        

#### `def pin_to_nidmm_session(self, pin: str) -> '_NIDmmSingleSessionQuery'`

Returns the NI-DMM session required to access the pin. If more than one session is
        required, the method raises an exception.

        Args:
            pin: The name of the pin to translate to an instrument session. If more than one session
            is required, the method raises an exception.

        Returns:
            pin_query_context: An object that tracks the sessions associated with this pin query.
                Use this object to publish measurements and extract data from a set of measurements.
            session: Returns the NI-DMM instrument session for the instrument connected to the pin
                for all sites in the Semiconductor Module context.
        

#### `def pins_to_nidmm_sessions(self, pins: '_PinsArg') -> '_NIDmmMultipleSessionQuery'`

Returns the NI-DMM instrument sessions required to access the pin(s).

        Args:
            pins: The names of the pin(s) or pin group(s) to translate to instrument sessions.

        Returns:
            pin_query_context: An object that tracks the sessions associated with this pin query.
                Use this object to publish measurements and extract data from a set of measurements.
            sessions: Returns the NI-DMM instrument sessions for the instruments connected to the
                pin(s) for all sites in the Semiconductor Module context.
        

#### `def get_all_nifgen_instrument_names(self) -> '_StringTuple'`

Returns a tuple of all NI-FGEN instrument names in the Semiconductor Module context. You
        can use the instrument names to open driver sessions.
        

#### `def set_nifgen_session(self, instrument_name: str, session: 'nifgen.Session') -> None`

Associates an instrument session with an NI-FGEN instrument name.

        Args:
            instrument_name: The instrument name in the pin map file for the corresponding session.
            session: The instrument session for the corresponding instrument name.
        

#### `def get_all_nifgen_sessions(self) -> '_Tuple[nifgen.Session, ...]'`

Returns a tuple of all NI-FGEN instrument sessions in the Semiconductor Module context.
        You can use instrument sessions to close driver sessions.
        

#### `def pins_to_nifgen_session(self, pins: '_PinsArg') -> '_NIFGenSingleSessionQuery'`

Returns the NI-FGEN session and channel list required to access the pin(s). If more than
        one session is required, the method raises an exception.

        Args:
            pins: The name(s) of the pin(s) or pin group(s) to translate to a session. If more than
                one session is required, the method raises an exception.

        Returns:
            pin_query_context: An object that tracks the session associated with this pin query. Use
                this object to publish measurements and extract data from a set of measurements.
            session: Returns the NI-FGEN instrument session for the instrument connected to the
                pin(s) for all sites in the Semiconductor Module context.
            channel_list: Returns the comma-separated channel list for the instrument connected to
                the pin(s) for all sites in the Semiconductor Module context. If any of the pin(s)
                are connected to the same instrument channel for multiple sites, the channel appears
                only once in the list.
        

#### `def pins_to_nifgen_sessions(self, pins: '_PinsArg') -> '_NIFGenMultipleSessionQuery'`

Returns the NI-FGEN sessions and channel lists required to access the pin(s).

        Args:
            pins: The names of the pin(s) or pin group(s) to translate to sessions.

        Returns:
            pin_query_context: An object that tracks the sessions associated with this pin query.
                Use this object to publish measurements and extract data from a set of measurements.
            sessions: Returns the NI-FGEN instrument sessions for the instruments connected to the
                pin(s) for all sites in the Semiconductor Module context.
            channel_lists: Returns the comma-separated channel lists for the instruments connected
                to the pin(s) for all sites in the Semiconductor Module context. If any of the
                pin(s) are connected to the same instrument channel for multiple sites, the channel
                appears only once in the list.
        

#### `def get_all_niscope_instrument_names(self) -> '_StringTuple'`

Returns a tuple of instrument names and comma-separated lists of instrument names that
        belong to the same group for all NI-SCOPE instruments in the Semiconductor Module context.
        You can use the instrument names and comma-separated lists of instrument names to open
        driver sessions.
        

#### `def set_niscope_session(self, instrument_name: str, session: 'niscope.Session') -> None`

Associates an instrument session with an NI-SCOPE instrument name.

        Args:
            instrument_name: The instrument name in the pin map file for the corresponding session.
            session: The instrument session for the corresponding instrument name.
        

#### `def get_all_niscope_sessions(self) -> '_Tuple[niscope.Session, ...]'`

Returns a tuple of all NI-SCOPE instrument sessions in the Semiconductor Module context.
        You can use instrument sessions to close driver sessions.
        

#### `def pins_to_niscope_session(self, pins: '_PinsArg') -> '_NIScopeSingleSessionQuery'`

Returns the NI-SCOPE session and channel list required to access the pin(s). If more than
        one session is required to access the pin(s), the method raises an exception. Each group of
        NI-SCOPE instruments in the pin map creates a single instrument session.

        Args:
            pins: The name(s) of the pin(s) or pin group(s) to translate to a session. If more than
                one session is required, the method raises an exception.

        Returns:
            pin_query_context: An object that tracks the session associated with this pin query. Use
                this object to publish measurements and extract data from a set of measurements.
            session: Returns the NI-SCOPE instrument session for the instrument connected to the
                pin(s) for all sites in the Semiconductor Module context.
            channel_list: Returns the comma-separated channel list for the instrument connected to
                the pin(s) for all sites in the Semiconductor Module context. If any of the pin(s)
                are connected to the same instrument channel for multiple sites, the channel appears
                only once in the list.
        

#### `def pins_to_niscope_sessions(self, pins: '_PinsArg') -> '_NIScopeMultipleSessionQuery'`

Returns the NI-SCOPE sessions and channel lists required to access the pin(s).

        Args:
            pins: The name(s) of the pin(s) or pin group(s) to translate to sessions.

        Returns:
            pin_query_context: An object that tracks the sessions associated with this pin query.
                Use this object to publish measurements and extract data from a set of measurements.
            sessions: Returns the NI-SCOPE instrument sessions for the instruments connected to the
                pin(s) for all sites in the Semiconductor Module context.
            channel_lists: Returns the comma-separated channel lists for the instruments connected
                to the pin(s) for all sites in the Semiconductor Module context. If any of the
                pin(s) are connected to the same instrument channel for multiple sites, the channel
                appears only once in the list.
        

#### `def get_all_switch_names(self, multiplexer_type_id: '_InstrTypeIdArg') -> '_StringTuple'`

Returns the names of all switches of the type specified by the multiplexer_type_id in the
        Semiconductor Module context. You can use switch names to open driver sessions.

        Args:
            multiplexer_type_id: Specifies the type ID for the multiplexer in the pin map file. When
                you add a multiplexer to the pin map file, you can define a type ID for the
                multiplexer, such as the driver name. Multiplexers in the pin map that do not
                specify a type ID have a default ID of
                nitsm.enums.InstrumentTypeIdConstants.NI_GENERIC_MULTIPLEXER.
        

#### `def set_switch_session(self, switch_name: str, session_data: '_Any', multiplexer_type_id: '_InstrTypeIdArg') -> None`

Associates an open switch session with the switch_name for a multiplexer of type
        multiplexer_type_id.

        Args:
            switch_name: The instrument name in the pin map file for the corresponding session_data.
            session_data: The instrument session for the corresponding switch_name and
                multiplexer_type_id.
            multiplexer_type_id: Specifies the type ID for the multiplexer in the pin map file. When
                you add a multiplexer to the pin map file, you can define a type ID for the
                multiplexer, such as the driver name. Multiplexers in the pin map that do not
                specify a type ID have a default ID of
                nitsm.enums.InstrumentTypeIdConstants.NI_GENERIC_MULTIPLEXER.
        

#### `def get_all_switch_sessions(self, multiplexer_type_id: '_InstrTypeIdArg') -> '_AnyTuple'`

Returns a tuple of all switch session data of the type specified by the
        multiplexer_type_id in the Semiconductor Module context.

        Args:
            multiplexer_type_id: Specifies the type ID for the multiplexer in the pin map file. When
                you add a multiplexer to the pin map file, you can define a type ID for the
                multiplexer, such as the driver name. Multiplexers in the pin map that do not
                specify a type ID have a default ID of
                nitsm.enums.InstrumentTypeIdConstants.NI_GENERIC_MULTIPLEXER.
        

#### `def pin_to_switch_sessions(self, pin: str, multiplexer_type_id: '_InstrTypeIdArg') -> '_SwitchQuery'`

Returns the switch sessions, switch routes, and new Semiconductor Module context objects
        required to access the specified switched pin.

        Args:
            pin: The name of the pin to translate to session data and switch routes.
            multiplexer_type_id: Specifies the type ID for the multiplexer in the pin map file. When
                you add a multiplexer to the pin map file, you can define a type ID for the
                multiplexer, such as the driver name. Multiplexers in the pin map that do not
                specify a type ID have a default ID of
                nitsm.enums.InstrumentTypeIdConstants.NI_GENERIC_MULTIPLEXER.

        Returns:
            semiconductor_module_contexts: A tuple of Semiconductor Module context objects. Each
                element in the tuple represents a site that must be executed serially. Use each
                Semiconductor Module context object to query the pin map and publish data.
            session_data: A tuple of the session data required to access the switch that connects an
                instrument channel to the pin.
            switch_routes: The routes required to connect an instrument channel to the pin.
        

#### `def get_relay_driver_module_names(self) -> '_StringTuple'`

Returns a tuple of all relay driver module names in the Semiconductor Module context. You
        can use the relay driver module names to open NI-SWITCH driver sessions for the relay driver
        modules.
        

#### `def get_relay_names(self) -> '_Tuple[_StringTuple, _StringTuple]'`

Returns all site and system relays available in the Semiconductor Module context.

        Returns:
            site_relays: Returns a tuple of strings that contains the site relays in the
                Semiconductor Module context.
            system_relays: Returns a tuple of strings that contains the system relays in the
                Semiconductor Module context.
        

#### `def set_relay_driver_niswitch_session(self, relay_driver_module_name: str, niswitch_session: 'niswitch.Session') -> None`

Associates an NI-SWITCH session with a relay driver module.

        Args:
            relay_driver_module_name: The relay driver module name in the pin map file for the
                corresponding session.
            niswitch_session: The NI-SWITCH session for the corresponding relay driver module name.
        

#### `def get_all_relay_driver_niswitch_sessions(self) -> '_Tuple[niswitch.Session, ...]'`

Returns a tuple of NI-SWITCH sessions for all relay driver modules in the Semiconductor
        Module context. You can use the NI-SWITCH sessions to close the relay driver module
        sessions.
        

#### `def relays_to_relay_driver_niswitch_session(self, relays: '_PinsArg') -> '_RelayDriverSingleSessionQuery'`

Returns the NI-SWITCH session and relay names required to access the relay(s) connected
        to a relay driver module. If more than one session is required to access the relay(s), the
        method raises an exception.

        Args:
            relays: The name(s) of the relay(s) or relay group(s) to translate to an NI-SWITCH
                session and NI-SWITCH relay names.

        Returns:
            niswitch_session: Returns the NI-SWITCH session for the relay driver module connected to
                the relay(s) for all sites in the Semiconductor Module context.
            niswitch_relay_names: Returns a comma-separated list of NI-SWITCH relay names for the
                relay driver module session connected to the relay(s) for all sites in the
                Semiconductor Module context.
        

#### `def relays_to_relay_driver_niswitch_sessions(self, relays: '_PinsArg') -> '_RelayDriverMultipleSessionQuery'`

Returns the NI-SWITCH sessions and relay names required to access the relay(s) connected
        to a relay driver module.

        Args:
            relays: The name(s) of the relay(s) or relay group(s) to translate to NI-SWITCH sessions
                and NI-SWITCH relay names.

        Returns:
            niswitch_sessions: Returns NI-SWITCH sessions for the relay driver modules connected to
                the relay(s) for all sites in the Semiconductor Module context.
            niswitch_relay_names: Returns comma-separated lists of NI-SWITCH relay names for the
                relay driver module sessions connected to the relay(s) for all sites in the
                Semiconductor Module context.
        

#### `def _apply_relay_action(session_ids_for_open, relay_names_to_open, session_ids_for_close, relay_names_to_close)`

#### `def _relay_wait(self, wait_seconds)`

#### `def apply_relay_configuration(self, relay_configuration: str, wait_seconds=0.0) -> None`

Performs the relay actions on the relays in the relay configuration.

        Args:
            relay_configuration: The name of the relay configuration to apply.
            wait_seconds: The time to wait, in seconds, for the relays to settle after performing
                all relay actions.
        

#### `def _control_relays_single_action(self, relays, relay_action, wait_seconds=0.0)`

#### `def _control_relays_multiple_action(self, relays, relay_actions, wait_seconds=0.0)`

#### `def control_relays(self, relays: '_PinsArg', relay_actions: '_Union[niswitch.RelayAction, _Sequence[niswitch.RelayAction]]', wait_seconds=0.0) -> None`

Performs the relay action(s) on the relay(s).

        Args:
            relays: The name(s) of the relay(s) or relay group(s) that identify the relays.
            relay_actions: The action(s) to perform on all identified relays.
            wait_seconds: The time to wait, in seconds, for the relay(s) to settle after performing
                the relay action(s).
        

#### `def get_custom_instrument_names(self, instrument_type_id: '_InstrTypeIdArg') -> '_Tuple[_StringTuple, _StringTuple, _StringTuple]'`

Returns the channel_group_ids and associated instrument_names and channel_lists of all
        instruments of type instrument_type_id defined in the Semiconductor Module context. You can
        use instrument_names, channel_group_ids, and channel_lists to open driver sessions. The
        instrument_names, channel_group_ids, and channel_lists return values always return the same
        number of elements. Instrument names repeat in instrument_names if the instrument has
        multiple channel groups.

        Args:
            instrument_type_id: The type of instrument for which you want to return instrument
                definitions. All instruments defined in the pin map specify an associated type ID.
                The nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs
                for instrument types that TSM supports natively. For all other types of instruments,
                you must define a type ID for the instrument in the pin map file. Typically, this
                type ID is an instrument driver name or other ID that is common for instruments that
                users program in a similar way.

        Returns:
            instrument_names: Returns the names of all instruments in the Semiconductor Module
                context that are of type instrument_type_id.
            channel_group_ids: Returns the IDs of all channel groups in the Semiconductor Module
                context that belong to an instrument of type instrument_type_id. For channels that
                do not belong to a channel group in the pin map, the Semiconductor Module creates a
                channel group with the same ID as the channel.
            channel_lists: Returns the channel lists for each element of channel_group_ids. Each
                channel list is a comma-separated list of channels.
        

#### `def set_custom_session(self, instrument_type_id: str, instrument_name: str, channel_group_id: str, session_data: '_Any') -> None`

Associates a session with an instrument and channel group.

        Args:
            instrument_type_id: The type of instrument for which you want to set the session. All
                instruments defined in the pin map specify an associated type ID. The
                nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for
                instrument types that TSM supports natively. For all other types of instruments, you
                must define a type ID for the instrument in the pin map file. Typically, this type
                ID is an instrument driver name or other ID that is common for instruments that
                users program in a similar way.
            instrument_name: The instrument name in the pin map file for the corresponding session.
                The instrument must be of type instrument_type_id.
            channel_group_id: The channel group in the pin map file for the corresponding session.
                For channels that do not belong to a channel group in the pin map, the Semiconductor
                Module creates a channel group with the same ID as the channel.
            session_data: The session for the corresponding instrument_name and channel_group_id.
        

#### `def get_all_custom_sessions(self, instrument_type_id: '_InstrTypeIdArg') -> '_Tuple[_Tuple[_Any, ...], _StringTuple, _StringTuple]'`

Returns all set sessions in the Semiconductor Module context that belong to instruments
        of type instrument_type_id.

        Args:
            instrument_type_id: The type of instrument for which you want to get sessions.
                All instruments defined in the pin map specify an associated type ID.
                The nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs
                for instrument types that TSM supports natively. For all other types of instruments,
                you must define a type ID for the instrument in the pin map file. Typically, this
                type ID is an instrument driver name or other ID that is common for instruments that
                users program in a similar way.

        Returns:
            session_data: Returns a tuple of session data set in the Semiconductor Module context.
            channel_group_ids: Returns the IDs of the channel groups on which session_data was
                stored. For channels that do not belong to a channel group in the pin map, the
                Semiconductor Module creates a channel group with the same ID as the channel.
            channel_lists: Returns the channel lists for each of the channel_group_ids. Each channel
                list is a comma-separated list of channels.
        

#### `def pins_to_custom_session(self, instrument_type_id: '_InstrTypeIdArg', pins: '_PinsArg') -> '_CustomSingleSessionQuery'`

Returns the session in the Semiconductor Module context associated with pin(s).

        Args:
            instrument_type_id: The type of instrument for which you want to get a session. All
                instruments defined in the pin map specify an associated type ID. The
                nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for
                instrument types that TSM supports natively. For all other types of instruments, you
                must define a type ID for the instrument in the pin map file. Typically, this type
                ID is an instrument driver name or other ID that is common for instruments that
                users program in a similar way.
            pins: The name(s) of the pin(s) or pin group(s) to translate to session_data,
                channel_group_id, and channel_list. The pin(s) must be connected to an instrument of
                type instrument_type_id.

        Returns:
            pin_query_context: An object that tracks the sessions and channels associated with this
                pin query. Use this object to publish measurements, extract data from a set of
                measurements, and create or rearrange waveforms.
            session_data: Returns the session data associated with pin(s).
            channel_group_id: Returns the ID of the channel group(s) that contain(s) the channels
                connected to pin(s). For channels that do not belong to a channel group in the pin
                map, the Semiconductor Module creates a channel group with the same ID as the
                channel.
            channel_list: Returns the channel list that corresponds to pin(s) associated with
                session_data and channel_group_id. The channel list is a comma-separated list of
                channels. If any of the pin(s) are connected to the same instrument channel for
                multiple sites, the channel appears only once in the list.
        

#### `def pins_to_custom_sessions(self, instrument_type_id: '_InstrTypeIdArg', pins: '_PinsArg') -> '_CustomMultipleSessionQuery'`

Returns all sessions in the Semiconductor Module context associated with pin(s).

        Args:
            instrument_type_id: The type of instrument for which you want to get sessions. All
                instruments defined in the pin map specify an associated type ID. The
                nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for
                instrument types that TSM supports natively. For all other types of instruments, you
                must define a type ID for the instrument in the pin map file. Typically, this type
                ID is an instrument driver name or other ID that is common for instruments that
                users program in a similar way.
            pins: The name(s) of the pin(s) or pin group(s) to translate to session_data,
                channel_group_ids, and channel_lists. The pin(s) must be connected to instruments of
                type instrument_type_id.

        Returns:
            pin_query_context: An object that tracks the sessions and channels associated with this
                pin query. Use this object to publish measurements, extract data from a set of
                measurements, and create or rearrange waveforms.
            session_data: Returns a tuple of session data associated with pin(s).
            channel_group_ids: Returns the IDs of the channel groups that contain the channels
                connected to pin(s). For channels that do not belong to a channel group in the pin
                map, the Semiconductor Module creates a channel group with the same ID as the
                channel.
            channel_lists: Returns the channel lists that correspond to the pin(s) associated with
                session_data and channel_group_ids. Each channel list is a comma-separated list of
                channels. If any of the pin(s) are connected to the same instrument channel for
                multiple sites, the channel appears only once in the list.
        

#### `def publish_per_site(self, measurements: '_PublishPerSiteMeasurementsArg', published_data_id='', pin='') -> None`

Publishes measurements from multiple sites for the Semiconductor Multi Test step to
        consume. Use this method when you want to publish data for multiple sites in the same order
        in which the sites are defined in the Semiconductor Module context.

        Args:
            measurements: The measurement data for all sites in the Semiconductor Module context.
                The number of elements passed to this parameter must be equal to the size of the
                site_numbers property. You must return results in the same order as the sites in the
                Semiconductor Module context. Use the site_numbers property to obtain the list of
                site numbers.
            published_data_id: The unique ID for distinguishing the measurement when you publish
                multiple measurements within the same code module.
            pin: The name of the pin associated with the data. This parameter must match a value you
                specify in the Pin column on the Tests tab of the Semiconductor Multi Test step. If
                you pass a blank pin, you don't have to specify a pin name in the Tests tab.
        

#### `def get_specifications_value(self, namespaced_symbol: str) -> str`

Returns the value calculated for the namespaced_symbol in the Semiconductor Module
        context specifications file. Raises an exception when the associated specifications file or
        symbol cannot be found.
        

#### `def get_specifications_values(self, namespaced_symbols: '_Sequence[str]') -> '_StringTuple'`

Returns the values calculated for the namespaced_symbols in the Semiconductor Module
        context specifications file. Raises an exception when the associated specifications file or
        any symbol cannot be found.
        

<!--NI_PYTHON_API repo=nitsm-python path=systemtests/conftest.py -->
## PYTHON MODULE: systemtests/conftest.py

### `def get_env_variable_from_registry(variable_name)`

### `class SystemTestRunner()`

#### `def __init__(self, sequence_file_path, offline_mode_cfg_path='')`

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_val, exc_tb)`

#### `def run(self)`

### `def teststand_login_override()`

### `def system_test_runner(request)`

<!--NI_PYTHON_API repo=nitsm-python path=systemtests/custom_instruments_codemodules.py -->
## PYTHON MODULE: systemtests/custom_instruments_codemodules.py

### `class CustomSession()`

#### `def __init__(self, instrument_type_id, instrument_name, channel_group_id, channel_list)`

#### `def instrument_type_id(self)`

#### `def instrument_name(self)`

#### `def channel_group_id(self)`

#### `def channel_list(self)`

### `def open_sessions(tsm_context: SemiconductorModuleContext, instrument_type_id)`

### `def measure(tsm_context: SemiconductorModuleContext, instrument_type_id, pins, expected_instrument_names, expected_channel_group_ids, expected_channel_lists)`

### `def close_sessions(tsm_context: SemiconductorModuleContext, instrument_type_id)`

<!--NI_PYTHON_API repo=nitsm-python path=systemtests/nidaqmx_codemodules.py -->
## PYTHON MODULE: systemtests/nidaqmx_codemodules.py

### `def open_sessions(tsm_context: SemiconductorModuleContext)`

### `def measure(tsm_context: SemiconductorModuleContext, pins, expected_task_names, expected_channel_lists)`

### `def close_sessions(tsm_context: SemiconductorModuleContext)`

<!--NI_PYTHON_API repo=nitsm-python path=systemtests/nidcpower_codemodules.py -->
## PYTHON MODULE: systemtests/nidcpower_codemodules.py

- `OPTIONS = {'Simulate': True, 'DriverSetup': {'Model': '4162', 'BoardType': 'PXIe'}}`

### `def open_sessions(tsm_context: SemiconductorModuleContext)`

### `def measure(tsm_context: SemiconductorModuleContext, pins, expected_channel_strings)`

### `def close_sessions(tsm_context: SemiconductorModuleContext)`

<!--NI_PYTHON_API repo=nitsm-python path=systemtests/nidigital_codemodules.py -->
## PYTHON MODULE: systemtests/nidigital_codemodules.py

- `OPTIONS = {'Simulate': True, 'driver_setup': {'Model': '6570'}}`

### `def open_sessions(tsm_context: SemiconductorModuleContext)`

### `def measure_ppmu(tsm_context: SemiconductorModuleContext, pins, expected_instrument_names, expected_pin_set_strings)`

### `def measure_pattern(tsm_context: SemiconductorModuleContext, pins, expected_instrument_names, expected_site_lists)`

### `def check_project_paths(tsm_context: SemiconductorModuleContext, specifications_paths, levels_paths, timing_paths, pattern_paths, source_waveform_paths, capture_waveform_paths)`

### `def close_sessions(tsm_context: SemiconductorModuleContext)`

<!--NI_PYTHON_API repo=nitsm-python path=systemtests/nidmm_codemodules.py -->
## PYTHON MODULE: systemtests/nidmm_codemodules.py

- `OPTIONS = {'Simulate': True, 'DriverSetup': {'Model': '4071', 'BoardType': 'PXI'}}`

### `def open_sessions(tsm_context: SemiconductorModuleContext)`

### `def measure(tsm_context: SemiconductorModuleContext, pins, expected_instrument_names)`

### `def close_sessions(tsm_context: SemiconductorModuleContext)`

<!--NI_PYTHON_API repo=nitsm-python path=systemtests/nifgen_codemodules.py -->
## PYTHON MODULE: systemtests/nifgen_codemodules.py

### `def open_sessions(tsm_context: SemiconductorModuleContext)`

### `def measure(tsm_context: SemiconductorModuleContext, pins, expected_instrument_names, expected_channel_lists)`

### `def close_sessions(tsm_context: SemiconductorModuleContext)`

<!--NI_PYTHON_API repo=nitsm-python path=systemtests/nirelaydriver_codemodules.py -->
## PYTHON MODULE: systemtests/nirelaydriver_codemodules.py

### `class MockSwitchSession(niswitch.Session)`

#### `def __init__(self, resource_name, *args, **kwargs)`

#### `def io_resource_descriptor(self)`

### `def open_sessions(tsm_context: SemiconductorModuleContext)`

### `def measure(tsm_context: SemiconductorModuleContext, relays, expected_instrument_names, expected_relay_names)`

### `def close_sessions(tsm_context: SemiconductorModuleContext)`

<!--NI_PYTHON_API repo=nitsm-python path=systemtests/niscope_codemodules.py -->
## PYTHON MODULE: systemtests/niscope_codemodules.py

### `def open_sessions(tsm_context: nitsm.codemoduleapi.SemiconductorModuleContext)`

### `def measure(tsm_context: nitsm.codemoduleapi.SemiconductorModuleContext, pins, expected_instrument_names, expected_channel_lists)`

### `def close_sessions(tsm_context: nitsm.codemoduleapi.SemiconductorModuleContext)`

<!--NI_PYTHON_API repo=nitsm-python path=systemtests/sessionutils.py -->
## PYTHON MODULE: systemtests/sessionutils.py

### `def get_resource_name_from_session(session) -> str`


    session.io_resource_descriptor isn't 100% reliable for simulated sessions. This method uses a
    regular expression to get the resource name from the object's repr.
    

### `def get_task_name_from_task(task) -> str`

Uses a regular expression on the task's repr to return the task's name.

<!--NI_PYTHON_API repo=nitsm-python path=systemtests/site_and_global_data_codemodules.py -->
## PYTHON MODULE: systemtests/site_and_global_data_codemodules.py

### `def set_global_data(tsm_context: SemiconductorModuleContext, data_id, data)`

### `def check_global_data(tsm_context: SemiconductorModuleContext, data_id, data)`

### `def set_site_data(tsm_context: SemiconductorModuleContext, data_id, data)`

### `def check_site_data(tsm_context: SemiconductorModuleContext, data_id, data)`

### `def clear_site_data(tsm_context: SemiconductorModuleContext, data_id)`

### `def check_site_data_cleared(tsm_context: SemiconductorModuleContext, data_id)`

<!--NI_PYTHON_API repo=nitsm-python path=systemtests/specifications_codemodules.py -->
## PYTHON MODULE: systemtests/specifications_codemodules.py

### `def measure(tsm_context, namespaced_symbols, expected_values)`

<!--NI_PYTHON_API repo=nitsm-python path=systemtests/switch_codemodules.py -->
## PYTHON MODULE: systemtests/switch_codemodules.py

- `MULTIPLEXER_TYPE_ID = 'SimulatedMultiplexer'`

### `def open_sessions(tsm_context: tsm.SemiconductorModuleContext)`

### `def measure(tsm_context: tsm.SemiconductorModuleContext, pin, expected_switch_names, expected_switch_routes)`

### `def close_sessions(tsm_context: tsm.SemiconductorModuleContext)`

<!--NI_PYTHON_API repo=nitsm-python path=systemtests/test_system.py -->
## PYTHON MODULE: systemtests/test_system.py

### `def test_nidmm(system_test_runner)`

### `def test_nidcpower(system_test_runner)`

### `def test_nifgen(system_test_runner)`

### `def test_nidaqmx(system_test_runner)`

### `def test_niscope(system_test_runner)`

### `def test_nidigital(system_test_runner)`

### `def test_nirelaydriver(system_test_runner)`

### `def test_custom_instruments(system_test_runner)`

### `def test_site_and_global_data(system_test_runner)`

### `def test_specifications(system_test_runner)`

### `def test_switch(system_test_runner)`

<!--NI_PYTHON_API repo=nitsm-python path=tests/conftest.py -->
## PYTHON MODULE: tests/conftest.py

### `def _published_data_reader_factory(request)`

### `def standalone_tsm_context_com_object(_published_data_reader_factory)`

### `def standalone_tsm_context(standalone_tsm_context_com_object)`

### `class PublishedDataType(enum.Enum)`

### `class PublishedData()`

#### `def __init__(self, published_data_com_obj)`

#### `def boolean_value(self) -> bool`

#### `def double_value(self) -> float`

#### `def pin(self) -> str`

#### `def published_data_id(self) -> str`

#### `def site_number(self) -> int`

#### `def string_value(self) -> str`

#### `def type(self) -> PublishedDataType`

### `class PublishedDataReader()`

#### `def __init__(self, published_data_reader_com_obj)`

#### `def get_and_clear_published_data(self)`

### `def published_data_reader(_published_data_reader_factory)`

<!--NI_PYTHON_API repo=nitsm-python path=tests/test_codemoduleapi.py -->
## PYTHON MODULE: tests/test_codemoduleapi.py

### `class TestCodeModuleApi()`

#### `def test_static_method_converts(standalone_tsm_context_com_object)`

#### `def test_static_method_does_not_convert(standalone_tsm_context)`

#### `def test_instance_method_converts(self, standalone_tsm_context_com_object)`

#### `def test_instance_method_does_not_convert(self, standalone_tsm_context)`

#### `def class_method_converts_core(cls, standalone_tsm_context_com_object)`

#### `def test_class_method_converts(standalone_tsm_context_com_object)`

#### `def class_method_does_not_convert_core(cls, standalone_tsm_context)`

#### `def test_class_method_does_not_convert(standalone_tsm_context)`

#### `def _invalid_number_of_positional_arguments(self)`

Does not contain a positional argument for the TSM context.

#### `def test_invalid_number_of_positional_arguments(self)`

#### `def _tsm_context_not_first_positional_argument(self, first_argument, tsm_context)`

#### `def test_tsm_context_not_first_positional_argument(self, first_argument, standalone_tsm_context_com_object)`

#### `def test_positional_arguments_after_tsm_context(self, standalone_tsm_context_com_object, second_argument)`

### `def test_function_converts(standalone_tsm_context_com_object)`

### `def test_function_does_not_convert(standalone_tsm_context)`

<!--NI_PYTHON_API repo=nitsm-python path=tests/test_custom_instruments.py -->
## PYTHON MODULE: tests/test_custom_instruments.py

### `def simulated_custom_instrument_sessions(standalone_tsm_context)`

### `class TestCustomInstruments()`

#### `def test_get_custom_instrument_names(self, standalone_tsm_context: SemiconductorModuleContext)`

#### `def test_set_custom_session(self, standalone_tsm_context: SemiconductorModuleContext)`

#### `def test_get_all_custom_sessions(self, standalone_tsm_context: SemiconductorModuleContext, simulated_custom_instrument_sessions)`

#### `def test_pins_to_custom_session_single_pin(self, standalone_tsm_context: SemiconductorModuleContext, simulated_custom_instrument_sessions)`

#### `def test_pins_to_custom_session_multiple_pins(self, standalone_tsm_context: SemiconductorModuleContext, simulated_custom_instrument_sessions)`

#### `def test_pins_to_custom_sessions_single_pin(self, standalone_tsm_context: SemiconductorModuleContext, simulated_custom_instrument_sessions)`

#### `def test_pins_to_custom_sessions_multiple_pin(self, standalone_tsm_context: SemiconductorModuleContext, simulated_custom_instrument_sessions)`

<!--NI_PYTHON_API repo=nitsm-python path=tests/test_general_and_advanced.py -->
## PYTHON MODULE: tests/test_general_and_advanced.py

### `class TestGeneralAndAdvanced()`

#### `def test_get_pin_names(self, standalone_tsm_context)`

#### `def test_filter_pins_by_instrument_type(self, standalone_tsm_context)`

#### `def test_get_pins_in_pin_groups(self, standalone_tsm_context, pin_groups)`

<!--NI_PYTHON_API repo=nitsm-python path=tests/test_multi_site.py -->
## PYTHON MODULE: tests/test_multi_site.py

### `class TestMultiSite()`

#### `def test_get_semiconductor_module_with_sites(self, standalone_tsm_context)`

<!--NI_PYTHON_API repo=nitsm-python path=tests/test_nidaqmx.py -->
## PYTHON MODULE: tests/test_nidaqmx.py

### `def simulated_nidaqmx_tasks(standalone_tsm_context)`

### `class TestNIDAQmx()`

#### `def test_get_all_nidaqmx_task_names(self, standalone_tsm_context: SemiconductorModuleContext)`

#### `def test_set_nidaqmx_task(self, standalone_tsm_context: SemiconductorModuleContext)`

#### `def test_get_all_nidaqmx_tasks(self, standalone_tsm_context, simulated_nidaqmx_tasks)`

#### `def test_pins_to_nidaqmx_task_single_pin(self, standalone_tsm_context, simulated_nidaqmx_tasks)`

#### `def test_pins_to_nidaqmx_task_multiple_pins(self, standalone_tsm_context, simulated_nidaqmx_tasks)`

#### `def test_pins_to_nidaqmx_tasks_single_pin(self, standalone_tsm_context, simulated_nidaqmx_tasks)`

#### `def test_pins_to_nidaqmx_tasks_multiple_pins(self, standalone_tsm_context, simulated_nidaqmx_tasks)`

<!--NI_PYTHON_API repo=nitsm-python path=tests/test_nidcpower.py -->
## PYTHON MODULE: tests/test_nidcpower.py

- `OPTIONS = {'Simulate': True, 'DriverSetup': {'Model': '4162'}}`

### `def simulated_nidcpower_sessions(standalone_tsm_context)`

### `class TestNIDCPower()`

#### `def test_get_all_nidcpower_resource_strings(self, standalone_tsm_context)`

#### `def test_set_nidcpower_session(self, standalone_tsm_context)`

#### `def test_get_all_nidcpower_sessions(self, standalone_tsm_context, simulated_nidcpower_sessions)`

#### `def test_pins_to_nidcpower_session_single_pin(self, standalone_tsm_context, simulated_nidcpower_sessions)`

#### `def test_pins_to_nidcpower_session_multiple_pins(self, standalone_tsm_context, simulated_nidcpower_sessions)`

#### `def test_pins_to_nidcpower_sessions_single_pin(self, standalone_tsm_context, simulated_nidcpower_sessions)`

#### `def test_pins_to_nidcpower_sessions_multiple_pins(self, standalone_tsm_context, simulated_nidcpower_sessions)`

<!--NI_PYTHON_API repo=nitsm-python path=tests/test_nidigital.py -->
## PYTHON MODULE: tests/test_nidigital.py

### `def simulated_nidigital_sessions(standalone_tsm_context)`

### `class TestNIDigital()`

#### `def test_get_all_nidigital_instrument_names(self, standalone_tsm_context)`

#### `def test_set_nidigital_session(self, standalone_tsm_context)`

#### `def test_get_all_nidigital_sessions(self, standalone_tsm_context, simulated_nidigital_sessions)`

#### `def test_pins_to_nidigital_session_for_ppmu_single_pin(self, standalone_tsm_context, simulated_nidigital_sessions)`

#### `def test_pins_to_nidigital_session_for_pattern_single_pin(self, standalone_tsm_context, simulated_nidigital_sessions)`

#### `def test_pins_to_nidigital_session_for_ppmu_multiple_pins(self, standalone_tsm_context, simulated_nidigital_sessions)`

#### `def test_pins_to_nidigital_session_for_pattern_multiple_pins(self, standalone_tsm_context, simulated_nidigital_sessions)`

#### `def test_pins_to_nidigital_sessions_for_ppmu_single_pin(self, standalone_tsm_context, simulated_nidigital_sessions)`

#### `def test_pins_to_nidigital_sessions_for_pattern_single_pin(self, standalone_tsm_context, simulated_nidigital_sessions)`

#### `def test_pins_to_nidigital_sessions_for_ppmu_multiple_pins(self, standalone_tsm_context, simulated_nidigital_sessions)`

#### `def test_pins_to_nidigital_sessions_for_pattern_multiple_pins(self, standalone_tsm_context, simulated_nidigital_sessions)`

#### `def test_pin_map_file_path(self, standalone_tsm_context)`

<!--NI_PYTHON_API repo=nitsm-python path=tests/test_nidmm.py -->
## PYTHON MODULE: tests/test_nidmm.py

### `def simulated_nidmm_sessions(standalone_tsm_context)`

### `class TestNIDMM()`

#### `def test_get_all_nidmm_instrument_names(self, standalone_tsm_context: SemiconductorModuleContext)`

#### `def test_set_nidmm_session(self, standalone_tsm_context: SemiconductorModuleContext)`

#### `def test_get_all_nidmm_sessions(self, standalone_tsm_context: SemiconductorModuleContext, simulated_nidmm_sessions)`

#### `def test_pin_to_nidmm_session(self, standalone_tsm_context: SemiconductorModuleContext, simulated_nidmm_sessions)`

#### `def test_pins_to_nidmm_sessions_single_pin(self, standalone_tsm_context: SemiconductorModuleContext, simulated_nidmm_sessions)`

#### `def test_pins_to_nidmm_sessions_multiple_pins(self, standalone_tsm_context: SemiconductorModuleContext, simulated_nidmm_sessions)`

<!--NI_PYTHON_API repo=nitsm-python path=tests/test_nifgen.py -->
## PYTHON MODULE: tests/test_nifgen.py

- `OPTIONS = {'Simulate': True, 'DriverSetup': {'Model': '5442', 'BoardType': 'PXIe'}}`

### `def simulated_nifgen_sessions(standalone_tsm_context)`

### `class TestNIFGen()`

#### `def test_get_all_nifgen_instrument_names(self, standalone_tsm_context)`

#### `def test_set_nifgen_session(self, standalone_tsm_context)`

#### `def test_get_all_nifgen_sessions(self, standalone_tsm_context, simulated_nifgen_sessions)`

#### `def test_pin_to_nifgen_session_single_pin(self, standalone_tsm_context, simulated_nifgen_sessions)`

#### `def test_pins_to_nifgen_session_muliple_pins(self, standalone_tsm_context, simulated_nifgen_sessions)`

#### `def test_pins_to_nifgen_sessions_single_pin(self, standalone_tsm_context, simulated_nifgen_sessions)`

#### `def test_pins_to_nifgen_sessions_multiple_pins(self, standalone_tsm_context, simulated_nifgen_sessions)`

<!--NI_PYTHON_API repo=nitsm-python path=tests/test_nirelaydriver.py -->
## PYTHON MODULE: tests/test_nirelaydriver.py

### `def simulated_niswitch_sessions(standalone_tsm_context)`

### `def assert_relay_positions(standalone_tsm_context, pin_map_relays, relay_position)`

### `class TestNIRelayDriver()`

#### `def test_get_relay_driver_module_names(self, standalone_tsm_context: SemiconductorModuleContext)`

#### `def test_get_relay_names(self, standalone_tsm_context: SemiconductorModuleContext)`

#### `def test_set_relay_driver_niswitch_session(self, standalone_tsm_context: SemiconductorModuleContext)`

#### `def test_get_all_relay_driver_niswitch_sessions(self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions)`

#### `def test_relays_to_relay_driver_niswitch_session_single_relay(self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions)`

#### `def test_relays_to_relay_driver_niswitch_session_multiple_relays(self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions)`

#### `def test_relays_to_relay_driver_niswitch_sessions_single_relay(self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions)`

#### `def test_relays_to_relay_driver_niswitch_sessions_multiple_relays(self, standalone_tsm_context: SemiconductorModuleContext, simulated_niswitch_sessions)`

#### `def test_apply_relay_configuration(self, standalone_tsm_context: SemiconductorModuleContext)`

#### `def test_control_relays_single_action_open_system_relay(self, standalone_tsm_context: SemiconductorModuleContext)`

#### `def test_control_relays_single_action_close_system_relay(self, standalone_tsm_context: SemiconductorModuleContext)`

#### `def test_control_relays_single_action_open_all_site_relays(self, standalone_tsm_context: SemiconductorModuleContext)`

#### `def test_control_relays_single_action_close_all_site_relays(self, standalone_tsm_context: SemiconductorModuleContext)`

#### `def test_control_relays_multiple_action_open_all_site_relays(self, standalone_tsm_context: SemiconductorModuleContext)`

#### `def test_control_relays_multiple_action_close_all_site_relays(self, standalone_tsm_context: SemiconductorModuleContext)`

#### `def test_control_relays_multiple_action_mixed_site_relay_positions(self, standalone_tsm_context: SemiconductorModuleContext)`

<!--NI_PYTHON_API repo=nitsm-python path=tests/test_niscope.py -->
## PYTHON MODULE: tests/test_niscope.py

### `def simulated_niscope_sessions(standalone_tsm_context)`

### `class TestNIScope()`

#### `def test_get_all_niscope_instrument_names(self, standalone_tsm_context: SemiconductorModuleContext)`

#### `def test_set_niscope_session(self, standalone_tsm_context: SemiconductorModuleContext)`

#### `def test_get_all_niscope_sessions(self, standalone_tsm_context: SemiconductorModuleContext, simulated_niscope_sessions)`

#### `def test_pins_to_niscope_session_single_pin(self, standalone_tsm_context: SemiconductorModuleContext, simulated_niscope_sessions)`

#### `def test_pins_to_niscope_session_multiple_pins(self, standalone_tsm_context: SemiconductorModuleContext, simulated_niscope_sessions)`

#### `def test_pins_to_niscope_sessions_single_pin(self, standalone_tsm_context: SemiconductorModuleContext, simulated_niscope_sessions)`

#### `def test_pins_to_niscope_sessions_multiple_pins(self, standalone_tsm_context: SemiconductorModuleContext, simulated_niscope_sessions)`

<!--NI_PYTHON_API repo=nitsm-python path=tests/test_pinquerycontext.py -->
## PYTHON MODULE: tests/test_pinquerycontext.py

### `def simulated_nidigital_sessions(standalone_tsm_context)`

### `class TestPinQueryContext()`

#### `def test_get_session_and_channel_index(self, standalone_tsm_context: 'SemiconductorModuleContext')`

<!--NI_PYTHON_API repo=nitsm-python path=tests/test_publish.py -->
## PYTHON MODULE: tests/test_publish.py

### `def simulated_nidigital_sessions(standalone_tsm_context: SemiconductorModuleContext)`

### `class TestSinglePinScalar()`

#### `def pin_query_context(self, standalone_tsm_context)`

#### `def test_publish_float_scalar(self, pin_query_context, published_data_reader)`

#### `def test_publish_bool_scalar(self, pin_query_context, published_data_reader)`

### `class TestSinglePin1d()`

#### `def pin_query_context(self, standalone_tsm_context)`

#### `def test_publish_float_1d(self, pin_query_context, published_data_reader)`

#### `def test_publish_bool_1d(self, pin_query_context, published_data_reader)`

#### `def test_publish_pattern(self, standalone_tsm_context, published_data_reader)`

### `class TestSinglePin2d()`

#### `def pin_query_context(self, standalone_tsm_context)`

#### `def test_publish_float_2d(self, pin_query_context, published_data_reader)`

#### `def test_publish_bool_2d(self, pin_query_context, published_data_reader)`

#### `def test_publish_pattern(self, standalone_tsm_context, published_data_reader)`

### `class TestMultiplePins1d()`

#### `def pin_query_context(self, standalone_tsm_context)`

#### `def test_publish_float_1d(self, pin_query_context, published_data_reader)`

#### `def test_publish_bool_1d(self, pin_query_context, published_data_reader)`

#### `def test_publish_pattern(self, standalone_tsm_context, published_data_reader)`

### `class TestMultiplePins2d()`

#### `def pin_query_context(self, standalone_tsm_context)`

#### `def test_publish_float_2d(self, pin_query_context, published_data_reader)`

#### `def test_publish_bool_2d(self, pin_query_context, published_data_reader)`

#### `def test_publish_pattern(self, standalone_tsm_context, published_data_reader)`

### `class TestPerSiteMultiSite()`

#### `def test_publish_per_site_numeric_1d(self, standalone_tsm_context, published_data_reader, test_data)`

#### `def test_publish_per_site_bool_1d(self, standalone_tsm_context, published_data_reader)`

#### `def test_publish_per_site_string_1d(self, standalone_tsm_context, published_data_reader)`

### `class TestPerSiteSingleSite()`

#### `def test_publish_per_site_numeric_scalar(self, standalone_tsm_context, published_data_reader, test_data)`

#### `def test_publish_per_site_bool_scalar(self, standalone_tsm_context, published_data_reader)`

#### `def test_publish_per_site_string_scalar(self, standalone_tsm_context, published_data_reader)`

<!--NI_PYTHON_API repo=nitsm-python path=tests/test_site_and_global_data.py -->
## PYTHON MODULE: tests/test_site_and_global_data.py

### `class TestSiteAndGlobalData()`

#### `def simulated_site_data(self, standalone_tsm_context)`

#### `def test_get_site_data(self, standalone_tsm_context, simulated_site_data)`

#### `def test_site_data_exists(self, standalone_tsm_context, simulated_site_data)`

#### `def simulated_global_data(self, standalone_tsm_context)`

#### `def test_get_global_data(self, standalone_tsm_context, simulated_global_data)`

#### `def test_global_data_exists(self, standalone_tsm_context, simulated_global_data)`

<!--NI_PYTHON_API repo=nitsm-python path=tests/test_switch.py -->
## PYTHON MODULE: tests/test_switch.py

### `def simulated_switch_sessions(standalone_tsm_context)`

### `class TestSwitch()`

#### `def test_get_all_switch_names(self, standalone_tsm_context, multiplexer_type_id)`

#### `def test_set_switch_session(self, standalone_tsm_context, multiplexer_type_id)`

#### `def test_get_all_switch_sessions(self, standalone_tsm_context, simulated_switch_sessions, multiplexer_type_id)`

#### `def test_pin_to_switch_sessions(self, standalone_tsm_context, simulated_switch_sessions, multiplexer_type_id)`

<!--NI_PYTHON_API repo=nitsm-python path=tools/makepy_pinmapinterfaces.py -->
## PYTHON MODULE: tools/makepy_pinmapinterfaces.py

### MODULE DOCSTRING

Generates _pinmapinterfaces.py

You must register the correct version of TSM with TestStand Version Selector prior to running this
script.

