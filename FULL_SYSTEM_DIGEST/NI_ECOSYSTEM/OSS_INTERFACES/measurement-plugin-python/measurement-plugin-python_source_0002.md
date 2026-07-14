# NI OSS SOURCE SNAPSHOT: measurement-plugin-python

<!--NI_OSS_SNAPSHOT repo=ni/measurement-plugin-python commit=2e57ec3e5bd703abc8690f8a46df62b28f0380e2 -->

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/NIDigitalSPI.sfp sha256=38f583b7df2c8cb1cff13cbd7ccb8e79cf9c8c4c14738acc7d6b4cb0bb9452c3 bytes=8400 -->
## FILE: examples/nidigital_spi/NIDigitalSPI.sfp

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/NIDigitalSPI.sfp`
- sha256: `38f583b7df2c8cb1cff13cbd7ccb8e79cf9c8c4c14738acc7d6b4cb0bb9452c3`
- bytes: 8400

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="3D8F1FA7B18DA2CEDF4B941B4720A6E7F767530793EA7A3F511219469577814DF585ECB50B1DB2E55004DA86FA407ED4EE2A34A0E3DA80F2DF7555199C04AFC3" Timestamp="1D971902937844C" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.8.0.50004" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="6.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.50000" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="23.3.0.50000" FeatureSetName="UnifiedTask" Name="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" Version="1.0.0.0" />
		<ParsableNamespace AssemblyFileVersion="23.3.0.50004" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.50000" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.8.0.50000" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.3.0.50000" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="23.3.0.50000" />
	</SourceModelFeatureSet>
	<UnifiedTask Id="61783f6f83fb4883980167b7e39c8572" LayoutInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Layout Information&quot;:{&quot;Sections&quot;:[{&quot;Columns Progressive Count&quot;:1,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Columns&quot;:[{&quot;Containers Progressive Count&quot;:1,&quot;Layout Information Index&quot;:0,&quot;Containers&quot;:[{&quot;Container Model Defition&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Container Assignment State&quot;:&quot;Available&quot;,&quot;Container Identifier&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen.task&quot;,&quot;Container Instrument Name&quot;:&quot;NI-Digital SPI (Py)&quot;,&quot;Layout Information Name&quot;:&quot;NI-Digital SPI (Py) 1&quot;,&quot;Layout Information Index&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Items&quot;:[{&quot;Identification Number&quot;:4294963201,&quot;Model Definition Type&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Parent Or Group Name&quot;:&quot;Measurements&quot;,&quot;Panel Type&quot;:&quot;NI-Digital SPI (Py)&quot;,&quot;Layout Information Name&quot;:&quot;ni.examples.NIDigitalSPI_Python&quot;,&quot;Layout Information Index&quot;:0}]}]}]},{&quot;Columns Progressive Count&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationOnly&quot;}]}}" PinAwareInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Selected Sites&quot;:[{&quot;Site Number&quot;:0}]}" xmlns="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" />
	<EnvoyManagerFile Id="6c31f1cca31b4b2fa7969d75081ad3bd" xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="e948a5811cee45b3a3807dae45535633" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<NameScopingEnvoy AutomaticallyResolveUp="True" Id="78b3f18a9db84d6ea5f2e3e81919b7b2" Name="NIDigitalSPI.sfp" NameTracksFileName="True" />
		<EmbeddedDefinitionReference Id="a4b06c4b696e4fc69fa02b8af0aa05a4" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="{http\://www.ni.com/InstrumentFramework/ScreenDocument}Screen.task">
			<Screen ClientId="{4e624bc4-ee53-476d-8221-e267b8671382}" ConfigurationParameters="{&quot;@type&quot;:&quot;type.googleapis.com/ni.measurementlink.measurement.v1.MeasurementConfigurations&quot;,&quot;pinNames&quot;:[&quot;SPI_PINS&quot;]}" DisplayName="NI-Digital SPI (Py)" Id="7319682d2bea49af95dbd40688eb3193" PanelPresentation="ConfigurationWithVisualization" ServiceClass="ni.examples.NIDigitalSPI_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
				<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]200" Id="fece5e258a91453ca3f0cbd2837ab796" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]450" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
					<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{4e624bc4-ee53-476d-8221-e267b8671382}/Configuration/pin_names" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="cfadf4e9c70f4b478d7a9b147e437d55" IsLabelBoundToChannel="[bool]False" Label="[UIModel]aa0027e3aa8d469fb061d408a5a9c793" Left="[float]20" MultipleSelectionMode="[MultipleSelectionModes]List" Top="[float]38" Width="[float]136" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
					<Label Height="[float]16" Id="aa0027e3aa8d469fb061d408a5a9c793" LabelOwner="[UIModel]cfadf4e9c70f4b478d7a9b147e437d55" Left="[float]20" Text="[string]Pin Names" Top="[float]18" Width="[float]56" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelArrayViewer AdaptsToType="[bool]True" ArrayElement="[UIModel]8aa07bffa7874d8f9d1058773c9e1365" BaseName="[string]Numeric Array Output" Channel="[string]{4e624bc4-ee53-476d-8221-e267b8671382}/Output/passing_sites" Columns="[int]1" Dimensions="[int]1" Height="[float]120" Id="e0b51635f4e4f86adaac92ff301106a" IndexVisibility="[Visibility]Collapsed" IsFixedSize="[bool]False" IsLabelBoundToChannel="[bool]False" Label="[UIModel]45f46a0a43a142b69df742e78e9e68ad" Left="[float]185" Orientation="[SMOrientation]Vertical" Rows="[int]4" TabIndex="[int]0" Top="[float]38" VerticalScrollBarVisibility="[ScrollBarVisibility]Visible" Width="[float]104">
						<p.DefaultElementValue>0</p.DefaultElementValue>
						<ChannelArrayNumericText BaseName="[string]Numeric" Height="[float]24" Id="8aa07bffa7874d8f9d1058773c9e1365" Interval="[int]1" IsReadOnly="[bool]True" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=0:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Int32" Width="[float]72" />
					</ChannelArrayViewer>
					<Label Height="[float]16" Id="45f46a0a43a142b69df742e78e9e68ad" LabelOwner="[UIModel]e0b51635f4e4f86adaac92ff301106a" Left="[float]185" Text="[string]Passing Sites" Top="[float]18" Width="[float]67" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelArrayViewer AdaptsToType="[bool]True" ArrayElement="[UIModel]7906e3ed85a54ea4b21f7da7152efed0" BaseName="[string]Numeric Array Output" Channel="[string]{4e624bc4-ee53-476d-8221-e267b8671382}/Output/failing_sites" Columns="[int]1" Dimensions="[int]1" Height="[float]120" Id="3621435f7829404b8e522a7479cc6a78" IndexVisibility="[Visibility]Collapsed" IsFixedSize="[bool]False" IsLabelBoundToChannel="[bool]False" Label="[UIModel]71d682844abb47f4ad21bc506613028c" Left="[float]318" Orientation="[SMOrientation]Vertical" Rows="[int]4" TabIndex="[int]1" Top="[float]38" VerticalScrollBarVisibility="[ScrollBarVisibility]Visible" Width="[float]104">
						<p.DefaultElementValue>0</p.DefaultElementValue>
						<ChannelArrayNumericText BaseName="[string]Numeric" Height="[float]24" Id="7906e3ed85a54ea4b21f7da7152efed0" Interval="[int]1" IsReadOnly="[bool]True" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=0:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Int32" Width="[float]72" />
					</ChannelArrayViewer>
					<Label Height="[float]16" Id="71d682844abb47f4ad21bc506613028c" LabelOwner="[UIModel]3621435f7829404b8e522a7479cc6a78" Left="[float]318" Text="[string]Failing Sites" Top="[float]18" Width="[float]62" xmlns="http://www.ni.com/PanelCommon" />
				</ScreenSurface>
			</Screen>
		</EmbeddedDefinitionReference>
	</EnvoyManagerFile>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/NIDigitalSPI_example.seq sha256=3d0afffb03a55cdb4b956cd427b5449bacf0e193a27d43f73f32ba16d59cccbe bytes=250300 -->
## FILE: examples/nidigital_spi/NIDigitalSPI_example.seq

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/NIDigitalSPI_example.seq`
- sha256: `3d0afffb03a55cdb4b956cd427b5449bacf0e193a27d43f73f32ba16d59cccbe`
- bytes: 250300

````text
<?xml version="1.0" encoding="UTF-8"?>
<teststandfileheader type='SequenceFile' fileversion='962' productname='TestStand' productversion='2021 (21.0.0.49156)' compatibleversion='21.0.0.0' buildversion='21.0.0.49156' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.ni.com/TestStand/21.0.0/SequenceFile">
	<typelist>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='1'>
			<Expression classname='ExprValue' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<value/>
			</Expression>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='2'>
			<StepTypeMenu classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='24'>
				<subprops>
					<CanBeSubstepType classname='Bool'>
						<value>false</value>
					</CanBeSubstepType>
					<CanOnlyBeSubstepType classname='Bool'>
						<value>false</value>
					</CanOnlyBeSubstepType>
					<Category classname='Str'>
						<value>""</value>
					</Category>
					<ItemName typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value>""</value>
					</ItemName>
					<SingularItemName classname='Str'>
						<value>""</value>
					</SingularItemName>
					<SeparatorBeforeCategory classname='Bool'>
						<value>false</value>
					</SeparatorBeforeCategory>
					<SeparatorBeforeItemName classname='Bool'>
						<value>false</value>
					</SeparatorBeforeItemName>
					<Group classname='Str'>
						<value/>
					</Group>
				</subprops>
			</StepTypeMenu>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='3'>
			<StepTypeSubstepsArray classname='Objs' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4718616' instanceoverrideflags='4849688' valueflags='24'>
				<value lbound='[0]' ubound='[]'/>
			</StepTypeSubstepsArray>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='4'>
			<NI_ArrayDimensions classname='ArrayDimensions' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<LowerBounds classname='Nums'>
						<value lbound='[0]' ubound='[]'/>
					</LowerBounds>
					<UpperBounds classname='Nums'>
						<value lbound='[0]' ubound='[]'/>
					</UpperBounds>
				</subprops>
			</NI_ArrayDimensions>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='5'>
			<NI_PropertyObjectType classname='PropertyObjectType' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<ValueType classname='Num'>
						<value>3</value>
					</ValueType>
					<IsObject classname='Bool'>
						<value>true</value>
					</IsObject>
					<TypeName classname='Str'>
						<value/>
					</TypeName>
					<ElementType classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</ElementType>
					<ArrayDimensions typename='NI_ArrayDimensions' xsi:type='NI_ArrayDimensions' classname='ArrayDimensions'>
						<subprops>
							<LowerBounds classname='Nums'>
								<value lbound='[0]' ubound='[]'/>
							</LowerBounds>
							<UpperBounds classname='Nums'>
								<value lbound='[0]' ubound='[]'/>
							</UpperBounds>
						</subprops>
					</ArrayDimensions>
					<Representation classname='Num'>
						<value>1</value>
					</Representation>
					<ClassName classname='Str'>
						<value/>
					</ClassName>
				</subprops>
			</NI_PropertyObjectType>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='6'>
			<NI_CustomResult classname='CustomResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Name>
					<ValueToLog typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ValueToLog>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>2</value>
					</CheckedState>
					<Type typename='NI_PropertyObjectType' xsi:type='NI_PropertyObjectType' classname='PropertyObjectType'>
						<subprops>
							<ValueType classname='Num'>
								<value>3</value>
							</ValueType>
							<IsObject classname='Bool'>
								<value>true</value>
							</IsObject>
							<TypeName classname='Str'>
								<value/>
							</TypeName>
							<ElementType classname='Objs'>
								<value lbound='[0]' ubound='[]'/>
							</ElementType>
							<ArrayDimensions classname='ArrayDimensions'>
								<subprops>
									<LowerBounds classname='Nums'>
										<value lbound='[0]' ubound='[]'/>
									</LowerBounds>
									<UpperBounds classname='Nums'>
										<value lbound='[0]' ubound='[]'/>
									</UpperBounds>
								</subprops>
							</ArrayDimensions>
							<Representation classname='Num'>
								<value>1</value>
							</Representation>
							<ClassName classname='Str'>
								<value/>
							</ClassName>
						</subprops>
					</Type>
					<Elements classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</Elements>
					<IsAnyType classname='Bool'>
						<value>true</value>
					</IsAnyType>
				</subprops>
			</NI_CustomResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='7'>
			<TEInf classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4456472' instanceoverrideflags='4456472' valueflags='24'>
				<subprops>
					<Id classname='Str' flagsforinstances='1' instanceoverrideflags='5046297'>
						<value/>
					</Id>
					<Icon classname='Str' instanceoverrideflags='5046296'>
						<value/>
					</Icon>
					<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7143448' structureflags='2097152'/>
					<PreCond typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PreCond>
					<LoadOpt classname='Str' instanceoverrideflags='5046296'>
						<value>PreloadWhenExecuted</value>
					</LoadOpt>
					<UnloadOpt classname='Str' instanceoverrideflags='5046296'>
						<value>UnloadWithFile</value>
					</UnloadOpt>
					<Mode classname='Str' instanceoverrideflags='5046296'>
						<value>Normal</value>
					</Mode>
					<WindowActivation classname='Str' instanceoverrideflags='5046296'>
						<value>None</value>
					</WindowActivation>
					<ResultOption classname='Num' instanceoverrideflags='5046296'>
						<value>1</value>
					</ResultOption>
					<StepFCSeqF classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</StepFCSeqF>
					<IgnoreRTE classname='Bool' instanceoverrideflags='5046296'>
						<value>false</value>
					</IgnoreRTE>
					<UseMutex classname='Bool' instanceoverrideflags='5046296'>
						<value>false</value>
					</UseMutex>
					<MutexNameOrRef typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</MutexNameOrRef>
					<BatchSyncOpt classname='Num' instanceoverrideflags='5046296'>
						<value>0</value>
					</BatchSyncOpt>
					<SwitchEnabled classname='Bool' instanceoverrideflags='5046296'>
						<value>false</value>
					</SwitchEnabled>
					<VirtualDeviceName typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</VirtualDeviceName>
					<SwitchOperation classname='Num' instanceoverrideflags='5046296'>
						<value>1</value>
					</SwitchOperation>
					<RouteGroupConnect typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</RouteGroupConnect>
					<RouteGroupDisconnect typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</RouteGroupDisconnect>
					<MulticonnectMode classname='Num' instanceoverrideflags='5046296'>
						<value>1</value>
					</MulticonnectMode>
					<OperationOrder classname='Num' instanceoverrideflags='5046296'>
						<value>2</value>
					</OperationOrder>
					<ConnectionLifetime classname='Num' instanceoverrideflags='5046296'>
						<value>4</value>
					</ConnectionLifetime>
					<WaitForDebounce classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</WaitForDebounce>
					<PassAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</PassAct>
					<FailAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</FailAct>
					<PassActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PassActTarget>
					<FailActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</FailActTarget>
					<CustExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</CustExpr>
					<CustTrueAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</CustTrueAct>
					<CustFalseAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</CustFalseAct>
					<CustTrueActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</CustTrueActTarget>
					<CustFalseActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</CustFalseActTarget>
					<LoopType classname='Str' instanceoverrideflags='5046296'>
						<value>NoLooping</value>
					</LoopType>
					<LoopWhile typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</LoopWhile>
					<LoopStatus typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</LoopStatus>
					<LoopIncrement typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value>RunState.LoopIndex += 1</value>
					</LoopIncrement>
					<LoopInitialize typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value>RunState.LoopIndex = 0</value>
					</LoopInitialize>
					<LoopOpt classname='Num' instanceoverrideflags='5046296'>
						<value>0</value>
					</LoopOpt>
					<PreExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PreExpr>
					<PostExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PostExpr>
					<StatusExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</StatusExpr>
					<CanSpecifyModule classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanSpecifyModule>
					<CanEditCode classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanEditCode>
					<CanEditModulePrototype classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanEditModulePrototype>
					<CanEditParameterAdditionalResults classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanEditParameterAdditionalResults>
					<PrecondIntExe classname='Num' instanceoverrideflags='5046296'>
						<value>0</value>
					</PrecondIntExe>
					<Requirements classname='Obj' flagsforinstances='2097153' instanceoverrideflags='7143449' valueflags='1' structureflags='2097152'>
						<subprops>
							<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
								<value lbound='[0]' ubound='[]'/>
							</Links>
						</subprops>
					</Requirements>
					<CustomResults classname='Objs' instanceoverrideflags='5046296'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</CustomResults>
					<AdditionalResultsHints classname='Objs' instanceoverrideflags='5046296'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
				</subprops>
			</TEInf>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='8'>
			<StepTypeNIData classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='24'>
				<subprops>
					<EditPanels classname='Strs'>
						<value lbound='[0]' ubound='[]'/>
					</EditPanels>
				</subprops>
			</StepTypeNIData>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='9'>
			<Error classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<extdata controllername='STRUCT' allowstructpassing='true' packingoption='8' exclude='false' type='0' arraystorage='0' strbuffersize='256' strstorage='0'/>
				<extdata controllername='CLUST' allowclusterpassing='true' exclude='false' memberlabel=''/>
				<extdata controllername='DNSTRUCT' allowstructpassing='true' exclude='false' membername=''/>
				<extdata controllername='BLVCLUSTER' allowclusterpassing='true' exclude='false' memberlabel=''/>
				<subprops>
					<Code classname='Num' flagsforinstances='4194304' valueflags='4194304'>
						<value>0</value>
						<extdata controllername='STRUCT' allowstructpassing='false' packingoption='0' exclude='false' type='6' arraystorage='0' strbuffersize='256' strstorage='0'/>
						<extdata controllername='CLUST' allowclusterpassing='false' exclude='false' memberlabel='code'/>
						<extdata controllername='DNSTRUCT' allowstructpassing='false' exclude='false' membername='code'/>
						<extdata controllername='BLVCLUSTER' allowclusterpassing='false' exclude='false' memberlabel='code'/>
					</Code>
					<Msg classname='Str' flagsforinstances='4194304' valueflags='4194304'>
						<value/>
						<extdata controllername='STRUCT' allowstructpassing='false' packingoption='0' exclude='false' type='2' arraystorage='0' strbuffersize='1024' strstorage='1'/>
						<extdata controllername='CLUST' allowclusterpassing='false' exclude='false' memberlabel='source'/>
						<extdata controllername='DNSTRUCT' allowstructpassing='false' exclude='false' membername='msg'/>
						<extdata controllername='BLVCLUSTER' allowclusterpassing='false' exclude='false' memberlabel='source'/>
					</Msg>
					<Occurred classname='Bool' flagsforinstances='4194304' valueflags='4194304'>
						<value>false</value>
						<extdata controllername='STRUCT' allowstructpassing='false' packingoption='0' exclude='false' type='6' arraystorage='0' strbuffersize='256' strstorage='0'/>
						<extdata controllername='CLUST' allowclusterpassing='false' exclude='false' memberlabel='status'/>
						<extdata controllername='DNSTRUCT' allowstructpassing='false' exclude='false' membername='occurred'/>
						<extdata controllername='BLVCLUSTER' allowclusterpassing='false' exclude='false' memberlabel='status'/>
					</Occurred>
				</subprops>
			</Error>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='10'>
			<CommonResults classname='Obj' isroottypedef='true' typecategory='3' timestamp='1465572565' typeversion='3.1.0.100' typelastmodversion='21.0.0.49156' typeminprodversion='3.1.0.0' typeflags='33554432' flagsforinstances='4194304' valueflags='4194304'/>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='11'>
			<Substep classname='StepType' isroottypedef='true' typecategory='1' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554438' flagsforinstances='4194304' instanceoverrideflags='4194304'>
				<subprops>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>"%ModuleDescription"</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "GENERIC_DEF_SUBSTEP_NAME")</value>
					</DefaultNameFormat>
					<BlockStartTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockStartTypes>
					<BlockEndTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockEndTypes>
					<AppliesToBlockStructure classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</AppliesToBlockStructure>
					<Menu typename='StepTypeMenu' xsi:type='StepTypeMenu' classname='Obj'>
						<subprops>
							<CanBeSubstepType classname='Bool'>
								<value>true</value>
							</CanBeSubstepType>
							<CanOnlyBeSubstepType classname='Bool'>
								<value>true</value>
							</CanOnlyBeSubstepType>
							<Category classname='Str'>
								<value>""</value>
							</Category>
							<ItemName classname='ExprValue'>
								<value>ResStr("NI_STEPTYPES", "GENERIC_SUBSTEP_MENU_ITEM_NAME")</value>
							</ItemName>
							<SingularItemName classname='Str'>
								<value>""</value>
							</SingularItemName>
							<SeparatorBeforeCategory classname='Bool'>
								<value>false</value>
							</SeparatorBeforeCategory>
							<SeparatorBeforeItemName classname='Bool'>
								<value>false</value>
							</SeparatorBeforeItemName>
							<Group classname='Str'>
								<value>GenericSubsteps</value>
							</Group>
						</subprops>
					</Menu>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</Substeps>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>DefaultLabVIEWNXG|DefaultLabVIEW|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|DefaultHTB80_Template|Default_Template</value>
					</CodeTemplates>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value/>
							</Icon>
							<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7274521' structureflags='2097152'/>
							<PreCond classname='ExprValue'>
								<value/>
							</PreCond>
							<LoadOpt classname='Str'>
								<value>PreloadWhenExecuted</value>
							</LoadOpt>
							<UnloadOpt classname='Str'>
								<value>UnloadWithFile</value>
							</UnloadOpt>
							<Mode classname='Str'>
								<value>Normal</value>
							</Mode>
							<WindowActivation classname='Str'>
								<value>None</value>
							</WindowActivation>
							<ResultOption classname='Num'>
								<value>1</value>
							</ResultOption>
							<StepFCSeqF classname='Bool'>
								<value>true</value>
							</StepFCSeqF>
							<IgnoreRTE classname='Bool'>
								<value>false</value>
							</IgnoreRTE>
							<UseMutex classname='Bool'>
								<value>false</value>
							</UseMutex>
							<MutexNameOrRef classname='ExprValue'>
								<value/>
							</MutexNameOrRef>
							<BatchSyncOpt classname='Num'>
								<value>0</value>
							</BatchSyncOpt>
							<SwitchEnabled classname='Bool'>
								<value>false</value>
							</SwitchEnabled>
							<VirtualDeviceName classname='ExprValue'>
								<value/>
							</VirtualDeviceName>
							<SwitchOperation classname='Num'>
								<value>1</value>
							</SwitchOperation>
							<RouteGroupConnect classname='ExprValue'>
								<value/>
							</RouteGroupConnect>
							<RouteGroupDisconnect classname='ExprValue'>
								<value/>
							</RouteGroupDisconnect>
							<MulticonnectMode classname='Num'>
								<value>1</value>
							</MulticonnectMode>
							<OperationOrder classname='Num'>
								<value>2</value>
							</OperationOrder>
							<ConnectionLifetime classname='Num'>
								<value>4</value>
							</ConnectionLifetime>
							<WaitForDebounce classname='Bool'>
								<value>true</value>
							</WaitForDebounce>
							<PassAct classname='Str'>
								<value>Next</value>
							</PassAct>
							<FailAct classname='Str'>
								<value>Next</value>
							</FailAct>
							<PassActTarget classname='ExprValue'>
								<value/>
							</PassActTarget>
							<FailActTarget classname='ExprValue'>
								<value/>
							</FailActTarget>
							<CustExpr classname='ExprValue'>
								<value/>
							</CustExpr>
							<CustTrueAct classname='Str'>
								<value>Next</value>
							</CustTrueAct>
							<CustFalseAct classname='Str'>
								<value>Next</value>
							</CustFalseAct>
							<CustTrueActTarget classname='ExprValue'>
								<value/>
							</CustTrueActTarget>
							<CustFalseActTarget classname='ExprValue'>
								<value/>
							</CustFalseActTarget>
							<LoopType classname='Str'>
								<value>NoLooping</value>
							</LoopType>
							<LoopWhile classname='ExprValue'>
								<value/>
							</LoopWhile>
							<LoopStatus classname='ExprValue'>
								<value/>
							</LoopStatus>
							<LoopIncrement classname='ExprValue'>
								<value>RunState.LoopIndex += 1</value>
							</LoopIncrement>
							<LoopInitialize classname='ExprValue'>
								<value>RunState.LoopIndex = 0</value>
							</LoopInitialize>
							<LoopOpt classname='Num'>
								<value>0</value>
							</LoopOpt>
							<PreExpr classname='ExprValue'>
								<value/>
							</PreExpr>
							<PostExpr classname='ExprValue'>
								<value/>
							</PostExpr>
							<StatusExpr classname='ExprValue'>
								<value/>
							</StatusExpr>
							<CanSpecifyModule classname='Bool'>
								<value>true</value>
							</CanSpecifyModule>
							<CanEditCode classname='Bool'>
								<value>true</value>
							</CanEditCode>
							<CanEditModulePrototype classname='Bool'>
								<value>true</value>
							</CanEditModulePrototype>
							<CanEditParameterAdditionalResults classname='Bool'>
								<value>true</value>
							</CanEditParameterAdditionalResults>
							<PrecondIntExe classname='Num'>
								<value>0</value>
							</PrecondIntExe>
							<Requirements classname='Obj' flagsforinstances='1' valueflags='1' structureflags='2097152'>
								<subprops>
									<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
										<value lbound='[0]' ubound='[]'/>
									</Links>
								</subprops>
							</Requirements>
							<CustomResults classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</CustomResults>
							<AdditionalResultsHints classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</AdditionalResultsHints>
						</subprops>
					</TS>
					<NI_Data typename='StepTypeNIData' xsi:type='StepTypeNIData' classname='Obj'>
						<subprops>
							<EditPanels classname='Strs'>
								<value lbound='[0]' ubound='[]'/>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
						<subprops>
							<Error typename='Error' xsi:type='Error' classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
								<subprops>
									<Code classname='Num'>
										<value>0</value>
									</Code>
									<Msg classname='Str'>
										<value/>
									</Msg>
									<Occurred classname='Bool'>
										<value>false</value>
									</Occurred>
								</subprops>
							</Error>
							<Status classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</Status>
							<ReportText classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</ReportText>
							<Common typename='CommonResults' xsi:type='CommonResults' classname='Obj'/>
						</subprops>
					</Result>
					<CanEncapsulate classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</CanEncapsulate>
				</subprops>
			</Substep>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='12'>
			<NI_DotNetParameterResult classname='DotNetParameterResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>1</value>
					</CheckedState>
				</subprops>
			</NI_DotNetParameterResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='13'>
			<DotNetParameter classname='DotNetParameter' isroottypedef='true' typecategory='3' timestamp='1650061192' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name classname='Str'>
						<value>_notNamed</value>
					</Name>
					<ArgVal typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgVal>
					<ArgDisplayVal typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgDisplayVal>
					<Type classname='Num'>
						<value>0</value>
					</Type>
					<TypeName classname='Str'>
						<value/>
					</TypeName>
					<Flags classname='Num'>
						<value>0</value>
					</Flags>
					<IsOptional classname='Bool'>
						<value>false</value>
					</IsOptional>
					<CallDispose classname='Bool'>
						<value>false</value>
					</CallDispose>
					<NumDimensions classname='Nums'>
						<value lbound='[0]' ubound='[]'/>
					</NumDimensions>
					<MultiElement classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</MultiElement>
					<AdditionalResults classname='Obj'>
						<subprops>
							<Input typename='NI_DotNetParameterResult' xsi:type='NI_DotNetParameterResult' classname='DotNetParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Input>
							<Output typename='NI_DotNetParameterResult' xsi:type='NI_DotNetParameterResult' classname='DotNetParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Output>
						</subprops>
					</AdditionalResults>
					<UserData classname='Obj' flagsforinstances='2097152' structureflags='2097152'/>
				</subprops>
			</DotNetParameter>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='14'>
			<NI_DotNetCallResult classname='DotNetCallResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>1</value>
					</CheckedState>
				</subprops>
			</NI_DotNetCallResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='15'>
			<DotNetCall classname='DotNetCall' isroottypedef='true' typecategory='3' timestamp='1650061192' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<ClassName classname='Str'>
						<value/>
					</ClassName>
					<MemberType classname='Num'>
						<value>0</value>
					</MemberType>
					<Static classname='Bool'>
						<value>false</value>
					</Static>
					<MemberName classname='Str'>
						<value/>
					</MemberName>
					<Params classname='Objs'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='DotNetParameter' xsi:type='DotNetParameter' name='' classname='DotNetParameter' structureflags='131072'>
									<subprops>
										<Name classname='Str'>
											<value>_notNamed</value>
										</Name>
										<ArgVal classname='ExprValue'>
											<value/>
										</ArgVal>
										<ArgDisplayVal classname='ExprValue'>
											<value/>
										</ArgDisplayVal>
										<Type classname='Num'>
											<value>0</value>
										</Type>
										<TypeName classname='Str'>
											<value/>
										</TypeName>
										<Flags classname='Num'>
											<value>0</value>
										</Flags>
										<IsOptional classname='Bool'>
											<value>false</value>
										</IsOptional>
										<CallDispose classname='Bool'>
											<value>false</value>
										</CallDispose>
										<NumDimensions classname='Nums'>
											<value lbound='[0]' ubound='[]'/>
										</NumDimensions>
										<MultiElement classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</MultiElement>
										<AdditionalResults classname='Obj'>
											<subprops>
												<Input classname='DotNetParameterResult'>
													<subprops>
														<Condition classname='ExprValue'>
															<value/>
														</Condition>
														<Flags classname='Num'>
															<value>8192</value>
														</Flags>
														<CheckedState classname='Num'>
															<value>1</value>
														</CheckedState>
													</subprops>
												</Input>
												<Output classname='DotNetParameterResult'>
													<subprops>
														<Condition classname='ExprValue'>
															<value/>
														</Condition>
														<Flags classname='Num'>
															<value>8192</value>
														</Flags>
														<CheckedState classname='Num'>
															<value>1</value>
														</CheckedState>
													</subprops>
												</Output>
											</subprops>
										</AdditionalResults>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</Params>
					<AdditionalResult typename='NI_DotNetCallResult' xsi:type='NI_DotNetCallResult' classname='DotNetCallResult'>
						<subprops>
							<Condition classname='ExprValue'>
								<value/>
							</Condition>
							<Flags classname='Num'>
								<value>8192</value>
							</Flags>
							<CheckedState classname='Num'>
								<value>1</value>
							</CheckedState>
						</subprops>
					</AdditionalResult>
				</subprops>
			</DotNetCall>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='0'>
			<Path classname='PathValue' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<value/>
			</Path>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='16'>
			<DotNetStepAdditions classname='DotNetModule' isroottypedef='true' typecategory='3' timestamp='1650061192' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Calls classname='Objs'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='DotNetCall' xsi:type='DotNetCall' name='' classname='DotNetCall' structureflags='131072'>
									<subprops>
										<ClassName classname='Str'>
											<value/>
										</ClassName>
										<MemberType classname='Num'>
											<value>0</value>
										</MemberType>
										<Static classname='Bool'>
											<value>false</value>
										</Static>
										<MemberName classname='Str'>
											<value/>
										</MemberName>
										<Params classname='Objs'>
											<value lbound='[0]' ubound='[]'>
												<elemproto>
													<_NAME_IN_ATTRIBUTE_ name='' classname='DotNetParameter' structureflags='0'/>
												</elemproto>
											</value>
										</Params>
										<AdditionalResult classname='DotNetCallResult'>
											<subprops>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>1</value>
												</CheckedState>
											</subprops>
										</AdditionalResult>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</Calls>
					<AssemblyPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</AssemblyPath>
					<AssemblyStrongName classname='Str'>
						<value/>
					</AssemblyStrongName>
					<AssemblyLocation classname='Num'>
						<value>0</value>
					</AssemblyLocation>
					<ClassName classname='Str'>
						<value/>
					</ClassName>
					<IsStruct classname='Bool'>
						<value>false</value>
					</IsStruct>
					<StructDef typename='DotNetParameter' xsi:type='DotNetParameter' classname='DotNetParameter'>
						<subprops>
							<Name classname='Str'>
								<value>_notNamed</value>
							</Name>
							<ArgVal classname='ExprValue'>
								<value/>
							</ArgVal>
							<ArgDisplayVal classname='ExprValue'>
								<value/>
							</ArgDisplayVal>
							<Type classname='Num'>
								<value>0</value>
							</Type>
							<TypeName classname='Str'>
								<value/>
							</TypeName>
							<Flags classname='Num'>
								<value>0</value>
							</Flags>
							<IsOptional classname='Bool'>
								<value>false</value>
							</IsOptional>
							<CallDispose classname='Bool'>
								<value>false</value>
							</CallDispose>
							<NumDimensions classname='Nums'>
								<value lbound='[0]' ubound='[]'/>
							</NumDimensions>
							<MultiElement classname='Objs'>
								<value lbound='[0]' ubound='[]'/>
							</MultiElement>
							<AdditionalResults classname='Obj'>
								<subprops>
									<Input classname='DotNetParameterResult'>
										<subprops>
											<Condition classname='ExprValue'>
												<value/>
											</Condition>
											<Flags classname='Num'>
												<value>8192</value>
											</Flags>
											<CheckedState classname='Num'>
												<value>1</value>
											</CheckedState>
										</subprops>
									</Input>
									<Output classname='DotNetParameterResult'>
										<subprops>
											<Condition classname='ExprValue'>
												<value/>
											</Condition>
											<Flags classname='Num'>
												<value>8192</value>
											</Flags>
											<CheckedState classname='Num'>
												<value>1</value>
											</CheckedState>
										</subprops>
									</Output>
								</subprops>
							</AdditionalResults>
						</subprops>
					</StructDef>
					<RemoteSpecifiedByExpr classname='Bool'>
						<value>false</value>
					</RemoteSpecifiedByExpr>
					<UseLoadSpec classname='Bool'>
						<value>false</value>
					</UseLoadSpec>
					<ModuleSrcPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModuleSrcPath>
					<ModulePrjPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModulePrjPath>
					<ModuleSlnPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModuleSlnPath>
					<FunctionName classname='Str'>
						<value/>
					</FunctionName>
				</subprops>
			</DotNetStepAdditions>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='17'>
			<PostSubstep classname='StepType' isroottypedef='true' typecategory='1' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554438' flagsforinstances='4194304' instanceoverrideflags='4194304'>
				<subprops>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>"%ModuleDescription"</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "POST_DEF_SUBSTEP_NAME")</value>
					</DefaultNameFormat>
					<BlockStartTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockStartTypes>
					<BlockEndTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockEndTypes>
					<AppliesToBlockStructure classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</AppliesToBlockStructure>
					<Menu typename='StepTypeMenu' xsi:type='StepTypeMenu' classname='Obj'>
						<subprops>
							<CanBeSubstepType classname='Bool'>
								<value>true</value>
							</CanBeSubstepType>
							<CanOnlyBeSubstepType classname='Bool'>
								<value>true</value>
							</CanOnlyBeSubstepType>
							<Category classname='Str'>
								<value>""</value>
							</Category>
							<ItemName classname='ExprValue'>
								<value>ResStr("NI_STEPTYPES", "POST_SUBSTEP_MENU_ITEM_NAME")</value>
							</ItemName>
							<SingularItemName classname='Str'>
								<value>""</value>
							</SingularItemName>
							<SeparatorBeforeCategory classname='Bool'>
								<value>false</value>
							</SeparatorBeforeCategory>
							<SeparatorBeforeItemName classname='Bool'>
								<value>false</value>
							</SeparatorBeforeItemName>
							<Group classname='Str'>
								<value>ExecSubsteps</value>
							</Group>
						</subprops>
					</Menu>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</Substeps>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>DefaultLabVIEWNXG|DefaultLabVIEW|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|DefaultHTB80_Template|Default_Template</value>
					</CodeTemplates>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value/>
							</Icon>
							<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7274521' structureflags='2097152'/>
							<PreCond classname='ExprValue'>
								<value/>
							</PreCond>
							<LoadOpt classname='Str'>
								<value>PreloadWhenExecuted</value>
							</LoadOpt>
							<UnloadOpt classname='Str'>
								<value>UnloadWithFile</value>
							</UnloadOpt>
							<Mode classname='Str'>
								<value>Normal</value>
							</Mode>
							<WindowActivation classname='Str'>
								<value>None</value>
							</WindowActivation>
							<ResultOption classname='Num'>
								<value>1</value>
							</ResultOption>
							<StepFCSeqF classname='Bool'>
								<value>true</value>
							</StepFCSeqF>
							<IgnoreRTE classname='Bool'>
								<value>false</value>
							</IgnoreRTE>
							<UseMutex classname='Bool'>
								<value>false</value>
							</UseMutex>
							<MutexNameOrRef classname='ExprValue'>
								<value/>
							</MutexNameOrRef>
							<BatchSyncOpt classname='Num'>
								<value>0</value>
							</BatchSyncOpt>
							<SwitchEnabled classname='Bool'>
								<value>false</value>
							</SwitchEnabled>
							<VirtualDeviceName classname='ExprValue'>
								<value/>
							</VirtualDeviceName>
							<SwitchOperation classname='Num'>
								<value>1</value>
							</SwitchOperation>
							<RouteGroupConnect classname='ExprValue'>
								<value/>
							</RouteGroupConnect>
							<RouteGroupDisconnect classname='ExprValue'>
								<value/>
							</RouteGroupDisconnect>
							<MulticonnectMode classname='Num'>
								<value>1</value>
							</MulticonnectMode>
							<OperationOrder classname='Num'>
								<value>2</value>
							</OperationOrder>
							<ConnectionLifetime classname='Num'>
								<value>4</value>
							</ConnectionLifetime>
							<WaitForDebounce classname='Bool'>
								<value>true</value>
							</WaitForDebounce>
							<PassAct classname='Str'>
								<value>Next</value>
							</PassAct>
							<FailAct classname='Str'>
								<value>Next</value>
							</FailAct>
							<PassActTarget classname='ExprValue'>
								<value/>
							</PassActTarget>
							<FailActTarget classname='ExprValue'>
								<value/>
							</FailActTarget>
							<CustExpr classname='ExprValue'>
								<value/>
							</CustExpr>
							<CustTrueAct classname='Str'>
								<value>Next</value>
							</CustTrueAct>
							<CustFalseAct classname='Str'>
								<value>Next</value>
							</CustFalseAct>
							<CustTrueActTarget classname='ExprValue'>
								<value/>
							</CustTrueActTarget>
							<CustFalseActTarget classname='ExprValue'>
								<value/>
							</CustFalseActTarget>
							<LoopType classname='Str'>
								<value>NoLooping</value>
							</LoopType>
							<LoopWhile classname='ExprValue'>
								<value/>
							</LoopWhile>
							<LoopStatus classname='ExprValue'>
								<value/>
							</LoopStatus>
							<LoopIncrement classname='ExprValue'>
								<value>RunState.LoopIndex += 1</value>
							</LoopIncrement>
							<LoopInitialize classname='ExprValue'>
								<value>RunState.LoopIndex = 0</value>
							</LoopInitialize>
							<LoopOpt classname='Num'>
								<value>0</value>
							</LoopOpt>
							<PreExpr classname='ExprValue'>
								<value/>
							</PreExpr>
							<PostExpr classname='ExprValue'>
								<value/>
							</PostExpr>
							<StatusExpr classname='ExprValue'>
								<value/>
							</StatusExpr>
							<CanSpecifyModule classname='Bool'>
								<value>true</value>
							</CanSpecifyModule>
							<CanEditCode classname='Bool'>
								<value>true</value>
							</CanEditCode>
							<CanEditModulePrototype classname='Bool'>
								<value>true</value>
							</CanEditModulePrototype>
							<CanEditParameterAdditionalResults classname='Bool'>
								<value>true</value>
							</CanEditParameterAdditionalResults>
							<PrecondIntExe classname='Num'>
								<value>0</value>
							</PrecondIntExe>
							<Requirements classname='Obj' flagsforinstances='1' valueflags='1' structureflags='2097152'>
								<subprops>
									<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
										<value lbound='[0]' ubound='[]'/>
									</Links>
								</subprops>
							</Requirements>
							<CustomResults classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</CustomResults>
							<AdditionalResultsHints classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</AdditionalResultsHints>
						</subprops>
					</TS>
					<NI_Data typename='StepTypeNIData' xsi:type='StepTypeNIData' classname='Obj'>
						<subprops>
							<EditPanels classname='Strs'>
								<value lbound='[0]' ubound='[]'/>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
						<subprops>
							<Error typename='Error' xsi:type='Error' classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
								<subprops>
									<Code classname='Num'>
										<value>0</value>
									</Code>
									<Msg classname='Str'>
										<value/>
									</Msg>
									<Occurred classname='Bool'>
										<value>false</value>
									</Occurred>
								</subprops>
							</Error>
							<Status classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</Status>
							<ReportText classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</ReportText>
							<Common typename='CommonResults' xsi:type='CommonResults' classname='Obj'/>
						</subprops>
					</Result>
					<CanEncapsulate classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</CanEncapsulate>
				</subprops>
			</PostSubstep>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='18'>
			<NoneStepAdditions classname='NoneModule' isroottypedef='true' typecategory='3' timestamp='1650060850' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'/>
		</typedef>
		<protected>E@=3HJL4100hYLEDF=_K@0@mKCYo_1KN2&lt;dfASB`]CF^aUXa]Y\4WmD]203VfR;kS;KgdGgF285WU]RaSJgcjNlM7MFC4LiX=a48\7dW:L403mZ4BUAT82I&gt;KQH8\T8QFE`DA2\LAVbMD5YRMT13fTiE^i&lt;boIle7[=C_LeZbKM2QXhVTH;?4hTX]A[17:2T;Dh\^Co3kY9PA5QK23^C]l262h09La1?5^k3J0BQZ@@EeDRZTO=\cKd?XKjmGb1N\X&lt;J[IS9OXJj22Qc=R\WEEn\IKCaHCAUNi97;EVjaJCX4&gt;UU36B3oib::mkjjIJFOY^^C_gK;?Ngamc6b1^HOM^Rl@oHoiaG802US0o36;lHiif[]oe&lt;FRliGlo^CMk69OeFDNDnIQUXNS=iA3JmW&lt;KbcFOCL6bWF;DdY7d2\SSH4mB7[^9gAb5EgM5G;l^DR5mXURj&lt;_=4b_aTDS965fd7ACLdkeA7kamDL&gt;;lWi[PA07_B@&gt;cR[mGK`_XMGdK4NmjkVR8?micjQcMS=oX^9@cW^5\93S[[2ZkFbBiZ=Q@AM0FkKdo:gUd&lt;lVVcfi&gt;bV3&gt;kl[1UR_FW&gt;JkW]_EREPX34oO2LYb;J&gt;k9nWLWBEg6Tk&gt;koggGTQ&gt;kL6kJL@dKQ2_E0Z</protected>
		<protected>E@=3HJB4110h]L]MDk_K3gBocK7LAg@bF0m7:L\7mUH^jTPf8UWji4?JObL37e`G1BU_]bJEEgG9OLd39Oi??^9QJSUTD=2428\B0kcT_7T&lt;Q@obH[[G3o^A&lt;D=J_&gt;g1Hi&lt;R`WmR7Y7K&gt;c7;g@f3WI&gt;MaH=lc7S9&gt;c?IG77K\]]6niUiBAL4CCDj_[5AJfWeomR_OoKJmJZM?&lt;_&gt;RAC]I2d0NnLHDh&gt;Dli&gt;23CM5CXi6DO^g`LX&lt;Q2hSHndMR7[D8BMh8aJ7oQSA@fKWPh;Dm5&gt;RW9o]Rgj]F^W_JkHFKk?2&gt;8;5iifgAJkk=k]f8VDCi5;PF:WC?2M3dfNg9]a`emUH&lt;]ARooBLZ\:kUkkkmM^^;g[CAF?o9BS9X&lt;V_06oLo]n`VOa[dMZmhLlJ^=?^T^nMbojKJkCSoWN4WIgV\ckgWCOWb7&gt;jno&gt;;[OS_oVacNOW7jg77?7OooD2OombloUnEI9_InB&lt;HI4[kZLf&lt;]bOKRmn::VQk1Tm`8F4;5W&gt;TA&lt;Kcd`aI[R8DKQka6aboN?k=I&gt;UJRNToCflBd:9=GW1XijhYcm92_e]^Rg?N[eOQO^9B&lt;2LjSQk=KKS8Eo?8kT9]m3^^fWPk?AQN^K4hZkc&lt;Vm&gt;gFc`@RgL^O5bET;[D_=R`WO?&gt;&gt;77S_K[1miPR@lgJ;?^^n6om3JliJgSBbAO&lt;J&gt;_7OGSQoU5Mo5ainP9oNj=DL&lt;NdI=^]VXFK0i[_\n0emoFJc]\=:4K&lt;HYHRl[4;=V_6SaC6ETl6dE1KV^E5NV9OgQBU&gt;n`WYOLgi&gt;S84nN^1mG5`SPC1]S:d;`B=4NjKmH&lt;UULW:0\;?2W8FOA:^K?M9TIFdMZj?UgUemK:5BfZf19WV&gt;o2K6[k;XS0HEj\8[[9QY;;_Z:UlBgN&gt;g897SGQPF^OS\Ba8&lt;Nl5AB?;oWBQ6aJP@1SQNGhXj:1DK9OHN&lt;6lGSkolg=dM`l2hG?AKRH2^5E7fbmmi:cJ2A056EVl9@Ll@B9;Ml6POPlacQAcKJf4N0AbVYZdLjl=5el2I6[[UbiSJdAiTCbBdeiYEk9g6Sa7[CFB8`Nkc\S4`dNB53K4Y@M`QAkbIdlgkPUJ??fmoGj]cMHcUoJH_X:heHfm2bQ96d\&gt;Y;:5diBn6JoC0O8DGdkT9VIPBjN^1cB`TcbjfVBJNQ[?b\onSkg@kON1onmnGNoOnYOo&gt;kc^Ofm]G7mB&gt;Qba^I&gt;6iVCm0GSnGTYgQ_Ig4AOR9MZMAk1Il1RgBV7TIAM`A=\k&lt;V4O9c?_3Y:O3l:dCYMk^gg;jl0L0CVKCUWH5`j7aeFkA[b&gt;CTQ95a^731VBF_IoV`TDggl4NO?G?^6Y3k&lt;P]4e7VRbee]]ZcM@Jf4&lt;;aWfGU&gt;9^:[`SDoKE?YZ:Vd8[TTU\cVW7EE&lt;cK2Y;_LD3MKjVT98S3E]O@NF=[GoXgC=`=OMNoZQ@@l2P:F[`T0:[LS53m:IMEkRTe@8gJE`&lt;]Y2:U`M8HkClI4_aPZN:4ZLOC2BoZFX8GCf8_I0;U^`[:e@:ILD&lt;808A]97NXjMJdHVK5&lt;6@ZRfV:AX6kPcgf@:31?M9dKQa?=RA:`f5TCI^bQLjbA?jYd&lt;_1^@Iek6[helE6RFL:EWA[cHLkB2l7QLeCBJX]0hDPWUWlCJ=:^m5gJjn&gt;SW9DRT1Q[Y5`gAf&lt;OdDdj1YNo:`NeELR3c2mU`G:e&gt;j8@]gAR?Ad48]8;:;&lt;S;EUJcjMiOVF1m50TbUD\Tl58jH?d\X8T^08T=W9[Z683aTA&gt;]W[5Oi5M?52E\:71[03U?V`4l_1WVH4j:GKI9hcEGRk3?_;k:;F_ej5SiN:WT:RF=Gmdl:=knc:UD^Hj9obj;AE\I7HC&gt;FB&gt;jYl8f56nJ&lt;UcI=fiN&lt;i;VXUJ55KE9jS9S_DR5N1k`PSNZVY0Z0iTYNej0?V_@UDHkL6Co5UCKBGPJYGR_Ti@1C@\A6TiIe;E\]e=ZZKd\ZVfURZTM50e8JQ[&lt;TMTUjFdJKR_9CXd\N38JN&gt;Q&gt;\UNF]@;FB8LQX@?dbU@[8mfDU3:S0dI&gt;?SmaPSHhfe6&lt;gV@A0JSZnmSECILX[AB98eHXQ9`R?5E3I6[4N=mYUREb_5jZURE5lhN6VZ\P`:`^;AQONF8O:Plbm4XSolW7VZN&lt;?OL8@0JK^m:5oh&lt;AR[a:BRlMniCM&lt;Q^\X\Nkg7G3ZMAi7nm:9PFFe3mCA1\]DY\Df;6aG&lt;iI]h2G6MG`BA\[I]008f:U6XXSNH2jcIXFSGI5Q2bBEKA`&lt;X]h_:@RfNklLbR7Sji9F_895&lt;R=Q572IULj=^noMWZiZ`ddKH`@`He:jliNb34YNl9[QT6cAlE&lt;6LflQ9e?nUMDFlcJBlA3?PP6fSobc@Of_fBSccJNY=&gt;?N3lZRDPO[EVgdA&lt;FBDB`XE&lt;^e]0&lt;&gt;VkM0OT@X&gt;YTBh&lt;5IL&lt;3?]`D2\9TbD=P9XH933VJR1BePO?6H6&lt;2;Rb:@82Hbj[IF&gt;5Pl5;dH0QG4:@48T&lt;39AjLjU172J17:JNl=j0P6NHX8U6RT@@_R0PglmF;;HX\i:jV^ULZBDKEBVfUTf9YQgX[9IDjjfT&gt;:iY`4VU&gt;jmJ&gt;^lE2G:UodJJ0?kJBH?eL@[95RbKJUIOlaNeJ04aJ?]A4YMiXMjb8EdSS:FQ@7jO^6V2_52W:f:]&lt;6e5Cd?=1I1S`LR^aZ9L?2:i8gKEhKfCL5bbPaMloUSe;o9aiAW[oE2DcNMo=]V3VZ3j=;eK0o5HDY[@\W;=e@Vl8XLFANQC9E&gt;QSA=CQY79hkh3K&lt;7T?;nR9;Z6LT?Nc&gt;S&lt;VnOhN&gt;A7dhl]K:oLi0N`lo`P8XYbiZhgEiMHkPY4;7?ho]9J`Z9g^0o=n=LSnOn?ieOB64nHAQFTK8PM_MC[JSeR8@G2bZIEdgH&lt;RZ;OM]&gt;@_LW:9G&lt;i8_M&lt;G0iefC[hgQ3@MR?7jB\Tc1Tf;FbZLgF5X3L[[i7=`i99aTj6Bf9hoc4f&gt;K\mAKJU5HVOhmaTQmdX?THaTcA20&lt;o\eFYJL5Fl`OaV0Lg^m=dM8dKEXZbi_aM`N4iNOTmgWYL3]hN6L7iae8^GXbD:O\Y6CH3&gt;KSj1^`C4a]&gt;WQ7OESNDVeoS81il`C&lt;lI\h;BR2o8`kOIUYaC_UM6UhYa5^:Vn4Tg@DYb3U\b\fAFX]aIIO3S\LG^&lt;VA[9&lt;di1?XH4d]PXFb[&lt;mS6WM1H7n4QOPX3V8JcaJ3Bc2f`3kS9^djl1&lt;NFQDkA93Ufmf&lt;amc=`80X1e3HkQ:L]YabEBD05fi1W2^:CkBEDcH^&lt;iZ;L:\8jH][;VZj4R5VRdB6F7g=a:g99Z[d9NoQ89XZfYU6Ej\lMNK`GXE8]&gt;kb1[e?Qc4mH:lRM9\OK7F\j_JGQ2X&lt;8nV91\\ReIUTd4;L6nZ4o7O&gt;5To5e:L?2S2kY98YfOPONej0UZd28\R5Kk_&gt;WnN^DH2Ra&gt;8JPmDGUT4BS3E6S6N6PXQ^o?DU4hlJ1V&gt;V1L?:__=@EIUOn9X7KR2Lo=2KmV9A8=\\T\C=1?n1D=@?IkA\=f2ii0CCN:&lt;9RPOFL`NU8DSQ&lt;`;_2&lt;nB]=6e51SI8613fMTW3Oj[L^R]8&gt;Pi:a`A2D=\4K&gt;il^UBR7P9]^G5NXA2^X7951G[YT\OKLGG4l=UQn;H7@B;8&gt;da:ibOD[XBR`]o&gt;VZ6DOCdK3AP?3A_33UbkQTneQOg=b`jYf;]h]AolQHPG^On43=0kIj9]cNR^:eSCY@7J3d:fE\We:Vb01HQD:H^8XDCNhWA\A:WD1Gl3&lt;U7dkK=5DgXUKgD\cnF6@[17\Fk=:4E@TUiP?Fl@0i9ZoM2bEb`155W4J=3T3DML1\aF:FfPQ_KUbIc:4Ya3JFAmR\aJMI0a[C4^ef5m^Fi4&gt;XZHB6?JU:=DZ87J56eH&gt;DmEMhP4D2oO3SJP&gt;1jMO2&lt;naOX3XeHoDCM;;J:PJlY8lXGAERILBl6Ze45f=C_H1EH@IjHR`mDHLk&gt;RloAEY7C[?GIk&gt;fJcE8?]mNG9gjfLehW\mLW]iM[?]hJNCWK\EIR0P]hk6`E4NUFW`L?jP9&lt;3@in]\&gt;b[aNQRj1@R1@lHWUO7cje0A&gt;LK;JhC[BgiI]\2@eSX:;QfRU@U&gt;]@_lm`4NmBZ\:ZoSFUb?TlhO5;?&gt;B1H?gA7=g=C1ji=292Ke0J\FnE9DeX&gt;CIC;iJ0Q`DXj&gt;W\&lt;PEOYPYk5m[A0\aN8N8UXTPGU[n]bW5n:`?nZlnnf\Imkoebbigkc`ofP\eP3l@ZOUX`?B@DZR_DX[^jV=gj=d1Ym4Z&lt;ob`?C`SLo9T5_eOKONeoF]7?koVKmXXP&gt;@mOLEB_KIcmYAEE:TPO\X\:IW;;f\GU_9nGfb7gkm2FX@_m\=LZKGW]]fQbgkjIKFn:Z?7OkIIKJ[SO\hURRIoOHS?5Im13fdEU3GX6A:fkd1W=WEW;WIRW;nf8PFKmj0I6c\Ol161GZUA]d;MJ:ZYK=VEA5\=d;6WchfDOoda;nMHPO^dHdLa@nRM@8^2Oa`S?HXLF4nDR@[gd@3ZWg?=HDeoV\ekeE:jne_Z_g?4HH]X`?HL\fA&gt;3IiNAk6W1m3G0_2TCL=LYO`T`_HK@l\3K6f3=3kY61mh3P6N;k6W1m37PK&lt;`\K6`f=3Y6;mn30n@QPPL_O`T`_HNXdTNm3PcB7f3=3k]61F3f^\2K6J51o9_dONJi[aZ=PgGoQ_YlegmNBlj]Mg1Y9kjW]mhcf\AE?5N[_l]E?eCjcMOO`&gt;NKk6j1FegWdiGIk&gt;gJcF[NcfKLeBjFNcffLFL[]in=6bC_H8^oNbA_H\`Ig&lt;[Zjc\IO`GPnSnRYk245=G437EhljgHLTJJgAIlMMmTC]5Ofg3k7l1=okWM^WiPP\Tb&lt;_gjXVbPjlMb^O2?7g2GoojlSJ\BolCmm&lt;eolmTbca0HGIPS7WELFBRNnUKon6]o_boQc4&lt;O7WakMAfZ1;@;]BVhfZ6d;A]\Y;]^C\2JNWl@EDkjHUD]8Gj3k:Gg9M]64UVIhV`0kFZjnXDXH9Ul?3UgC&lt;4E`da=l&lt;6aYaK?YSB&lt;ZlK8AkLXPga:L6Y9WXb^R2:;XfCCXg46QgO@OonCH=04lnD]G?@JU0oW&gt;8R[cd5WUn`Lj&gt;_L4H7acI]&lt;]SYiCVkXMEcP^ab7Tf\&lt;L36cdmoD7?&gt;U&gt;FXnG58NQBfkE`&gt;Y&gt;ZXN^;LUDk^0CT`]]YcV503o2&lt;9aY76Tb5=h;3n^l@;GR:DEml&lt;HjcCj]?2BHSYcAH8LcPLdmXLfl9&lt;R?P&gt;m[d_OAF47OMiiSBYLBDIO:B2mBEQejeLI1_lDOkc^TPmOSR;N?RhN=R3X@`aEX13VmJG`^nJRDXYeb7QSJiLJ`NX5Qkf=]imm&gt;nKg_CV6OK]RK94GkTDXQ&gt;HaT13fb00I9PG6JX1RmPQA@CXT2Ci9A4;\8804oTS3&gt;9F@3jQ0Q`Yb6PH2J8=QIl&lt;U65fY12^T^l2@8TQ51B^@UA:oVP&lt;O1`X1PnPjXO0`P3GQkdBQm:cV001le`9l2VYAPg8&lt;0k8Bm6`QjeP@j2ciUhWLj@0LY?3AP784;S@YWHX1S?Qn1m1kHbJS6f811fJb&lt;=99l6:nE1PPJ=8l=&lt;a\P0dAX0LXTD&gt;iH&lt;5QR6^dF;Bab60@I1@Q0HZS?9?A@TRA`J1PHiRc:Q:_jX1GeY=N[B&lt;3V2Pd60J^Y3@[1hD0XF2MP;&lt;B3RX2_H4PG43R;`1ZV@8E0R&lt;KHgh4VHe2B0H4:Y&lt;H5&lt;Q723C@d@1WBS^63LMX3=h4n91c3XeS;4aDhDR99PE40@14SA4S8Z_QlfJ^kenOQMQl\MFkQ32aVj``BUAmNDAB3?\R55J4A\37PAhR]3=KA6W&lt;86890Ck1NP@_[g:D6dV4Q49fS?IJ_C2;S^7mbE9SkO2G9Ii^ggHKkT`F370_j7b?jkWkEQ]:?XVf6A2ilo3@QYRZ82LV4K6^KABIXe``g6B7e1HCJK8hP9k^0X&gt;O;4j2^RRM3c2=aH8f`YUfUlb`B&lt;3I37=]e&gt;@JZ?KI:?@GJMZ]DOXZDNYX\cVFBbZ1RmDIF82=NNZDMK0dibVYa6E8b@nBP&lt;5Tl&lt;05lIDYhX^b6F\?\XfTjW:PUgjFJNIm\aeD&lt;eoRAhT`S]9IT7:LUghEY&gt;2fJODYDMFWDNBTdof=ITOaPAL59FVSX7NGk\MRM]DU&gt;&lt;nm39CJKab2S9fP&gt;SbRPR`h&lt;R0@D@5P9ZV08\FAR=6B[D?`iF9Xa6Q9e:U\ARX=B]93S4;17PliCP_8N5h`&gt;i6V3&gt;38TciG@Te@WT`HL8`hPj;\D6gSlTdaAYJMc8Hiaf&gt;[[@NAUBeHhFNTm7NYnXia&gt;:JBgQ?oS?;U9jT\\=AYoUTMCT\81ZYRXNJb\lbEEL&gt;e79ib&gt;:2`]U2jToCY]80BfV:4``\X1a4BL&lt;9?9ATRQ4bcK7^1A4RoX@7_2@S;hfe90M;0D;DJ]?I]5@0Y`&gt;NV3LF5`I1LYCFZTJU@=fTdVb2IPfC6dDZZ8JGTc2QOh;^L8HnSlnS?YbH5TGiYN5i9a8XWVIV]cK^:A]LH[5Lm2L34ZfLDn&lt;hgf2IHQJV6o[CK&gt;:33MOAcD5k&gt;LcEW&lt;&gt;D1CTFD^e69IAD3mLk&gt;C56YaKeFci;[THhLnK]V7iaZ:O5@PcUHH0f];^:5a0o2@FhcUKMQ5D&gt;nJn?Ija2clJo0KQ0:6Z&lt;7KD=:2I^YmJGE@ELPHG[9N\9mCc046gh\;[KBUd_I=RJbRBo&gt;kD8\BUXbUB8c&lt;]fF[BViXJSLNm=oWLlRY</protected>
		<protected>E@=3BJiO100h]L]MGkcK3fBoaKgcnO1C[KY_3VgFg3f\:dbWRb]W]ja3ZeDT&gt;gG&lt;F3C`h&lt;FRIEB:dR&gt;oal1lR8P`R;7UdVj]0WcI1;0g&lt;G02gHM\_?LJaZU?0;bU&gt;?K&gt;mo9iW:SW4SQU`7k?R&gt;OCUM]W&lt;jeB0_&lt;LPOEolh&gt;\=nNYf_\cHOnG4WQd6UA`SLO_Ad?fO&gt;njZG]]_]Neo`^=LRZTLTT5MG&gt;RnKeM2h&gt;L8iUjM&gt;8RC2OMoIfR2X&lt;C_Lka@&gt;B]G96ESU?&gt;o2XYIhW38;liQ9CWZnPo?&gt;KMefNkmo`5lF^ST9RZ7HULfI]cIoi@K&gt;L&lt;a3YOo;ZgDOf&gt;hfcFAc_HL4EFmLci?Ggf3&gt;&gt;foggfacn]leXS49aC0bmIFlclng=o=V]&gt;_kmhdVblRiH=4n&lt;n=l&lt;lnghEb_jco^\QknmkMQFgm8mGNnb:Ale;FNmHYmlooibXo[_JhdiOHNmn;LMfCJU=VL9lYlWUS;ho\mEk8WaK@i;f13GQ6dgBMD6\2\7O2GA9AIOfSfo7oNGI^laUnL0cjRg&gt;`?6im]Q34Hi1?MI0:Udgjk7MPSGM9j`5EI87&gt;WbVf5X\`Zob5B5QoWUnMNgXBWkV\CWVj;XX?hX^Jg?&gt;Z:ASVm8O8jiUbah9onn\n=Xl2oI&lt;]6GGomAM]Hne?gigOX`\_OKE_Jc1mh\f8hJ&lt;K_^_]^kGW3WohXebO25P[dTAoQ6]g1Ijc9e]ikO]lLBJNd04EQIE^MjQlkChJaR4&gt;]?hVjVSSej@&lt;Zi;KLZL?71d=gWMd`HE`gG;cOSa=T&lt;5k;9b:bL6[QoN9&lt;VkPYdI=8[EP3[B2\ie9]f&gt;LF&lt;[J^eL_CkVen7&gt;5Ba[UQ5WE&gt;`:o6;k8hWPIej\\[Z9i[;8_Z:U&gt;V`O=f897RGQXFMNSRB98&lt;Nm93YWU?cUk34&lt;jI21Bg5In^6F:[CWNP&gt;EY=mP^fdM;8B;XRWR8IN3BIhAK3?fFC2g0k2=^YUT1QDaWN@WlFS9mdce0D^GmJQ[ga4CM7:5hEB&gt;a\FKY6[O[i&gt;6`0b^]ZjAaTl1e[IXG@MH[ah7O\kgbQbH?N_l]WmnGWk9omP4&gt;G68d:7IJ`b=c2h9lIbBKE:;]Fl@L1k;:[M&lt;aAM9aaHKGeC5n4`m;INon][Kk^WQ&lt;_On0OMn_nnhk^knnK_oWk`jDm9W`bIJA&gt;UVB^HHWa[9nDXcORQhdL9LG^L?n3TJ6T\`hkii?McS5;FcgRTeMGQdcYCin&lt;YfAONf:&gt;jbo08@ZVKTn_7hA69mF6D[acNhIR[7AlbWDf]8GD^ekBM^E^hmiGO&lt;J^7WB_V3VkLSP0Nc?aUnWfg4L98VM25HnBlbTVTUG=H6JOLWP\dG2JRY=HilehI74eKg&gt;PmeQCiRh30=h9L4I9lkJ5LH3&gt;=kLaY5?o]bAnGC9XYPj`IhD;67BNM[gAL9R8dh=Rck9B9Wmieb_^Y4Yn6_A9GYK1]7e4cEcW200EnSXZLco2:^mJ?IlMQ_`iQ]M6d\ZKK\DQ&gt;JQCc2Fh&gt;iXJcVDF;j8EKT1TbMmGihOXU0EGhF:]`G`FjW[HhPSiZE_Z?hYXGnmF62^=hn`MBjMJ1fDZgZ`EWO5cLkSb6mEX6YMY=JA4LdWbBN4I]=dgc_ONh&gt;dC_YM492mEBR&gt;KSHYOd=CV1Og::N3eER0;N8ELWdGZe1VFc=eAlQ5R0:MLER&lt;HO\TbAa1mRh?IdWA4^7g96EX&lt;I:C&lt;33OHY8NPB`ZHX90`LKjUfcYLOkADaHV&lt;;L?PdTmPT1[&gt;?gjhnME:GQU[Zi\edCN_PWUj[jX`]_=N?EViO]?2QDk1W?V8W_FJ23HS1YI_`H9V:3&gt;cS\gTT:U;YW5HTM]bOmnCWe7k`JYZeRUS[YVmaDHBLLEeNfde;U6C8gZ7T]b&gt;N9bkCI;bS@gZXPNTZH?:4cnB&lt;]5D`0ZJUJUT^cTc&lt;JF][dO=IFL@KbEEB^R0VT\X5VH^b:E;K?\aGB3dJg5_D3WWaE4b?&lt;PYEk047iaD[=]k4ZS_]=QRbHK=F;g8lmAXF&gt;QmESVhD&lt;iF8&gt;eoTUU6S5B:b506cU913NBHoJ_0G_&gt;UPUHFfoLL0[4K^Mb[VlBEM?9Vl5G&gt;RbhcB49^QWD&gt;2n?Wok?8G9nTA;9]TYFRN54@Oh`VeQDa2gVcPj:kTCM5EcPgoJk^&gt;]neYg4&lt;_I&gt;=LO9ZlU4\=CgOZRJKfl[J833OjRn@4g5J]374ZRGK038Vn5jf]9M_moj6g`]:&lt;F34bNeja&lt;oVgnmC89?NiQHToa:Ub8H2]l;@^Ro&lt;gXiokCnO7UoU52Z5V^CAH&lt;`&lt;LVM&lt;U;@NUe]LSUcXjRHj3eO?WMTDl;TJbC_;`P8G=&lt;ZZ22cDC;&lt;bf=0lOCKo7iALI1PiZ[0oW?XZ0Cf0Fajb&lt;3;di\Fg1HVR6VX:@c:F&gt;a?&gt;3PhKfRd8BgYhRQRV&lt;V1H7A`da05dXR1E\ADe6A`L`odU&lt;jQ2M\\f1;Rc`15VHQ8MT`hUZ&gt;L:D8O6D`obe1&gt;7kP@3]a6d16Lj15VeMhAN`1GWcF3eiE;FWNjPdc;g==J=eeOI;H8dceE=&lt;=Z=UYObfGLdbK9]Xdnfg]85hCW^lDm8YFG@Pg[Tii?UGMVBiH^@a2^hN3J7VWD?&lt;g4fVA_2DUEf_R@bIjMCF^HS\iUJb]T64JJ7^m0g5i1VEb9HgAldSV_iUTk@nig16kZFACb[_F]1;DGcMOX&gt;WSJFSjB=eKoQD4gBA4^^&lt;V@VkN[6:;[98UJ&lt;WXTaV8i]S4Olj0Tk7BdTY5_8kAN[U4l5bgW1_57a[od&gt;;N0_lOAINdAaDD`5JjmKJY1\lH96o72R3YfJ85i_lP7JnZgCin?XiVD:61bJAA\THP`K_ce[Jg9RX?:2fI[Ed4N:V=JOL=l9?GaJ=&lt;SKJ?nf[2TJHeQL5QD4^W43CfV:MBPJU57e9[ERb5_EecH6hDa4TMIS5\]mO@=KWQ]mEJQUUFROj9akhn5:LQ2MYd&lt;0a?Bk]NXFT5QOlJ2i8LIkO&lt;1gbf9E:Rd]K_J:F&gt;Do&gt;nKj^TNPK?TQ4&gt;o^N=U246SQeMCjB8D9;gVTcJ_REY2nL@KZL:TngB8iLOKe:Mh=b\&gt;Y:;^0jMJiMhliFIJDANdHPecLg\Ve76bL@[VLJd5EZRCen@_djBCkP\F586bl@8M]Zf28DU?c6aXB;`3jW&lt;gQge21C3dMHP4YIKWD1O2emO]_A45Nf?TEBB`;_Ll?O&lt;X3LBjB39?C=8QJZO9Q5dATCl8ZTTWmK6_9X6hHcXWX0D5WDM0fcU2Le8`A5k3Lf7RYPWlXCVDV7R_WZJQVHFmY9fBkXmUg7YHcb7VlP6_K[Q928gWWlN7mBCHkm&gt;]]80ddI&lt;BRI_b?PS43aH46^T55LeE&lt;&gt;^TG1J?NI=F8&lt;Yomhl@hKmRZZ&lt;BPYle4clb_G[k144=hN6h]iZ6S8&lt;2=H=3iI0EAMo^O:9K8d3F=\235EIfOQZScnmZB&gt;dA5h11Fgj`:R@SKh9H5J0o?1DL;&gt;44k\=@f5iT4CAb:9C&gt;`AlND&lt;BTY0IhQo:2b[_&lt;gFD45W2Q\7ZVj&gt;7&lt;1EiDCKADMcELR@1?D&gt;QS[LiEF9cPSTfHGRbL&lt;QHYl4@d`JIhiG^`7eAFo5h&lt;O7XfdB25CjBc&gt;f5XZT8nFGig&lt;@bECNSMHLQUHMP4X^_h\_^iD^IcAo=YU5ddm?g?&lt;ZB5U?d4I@o7[m?=]&lt;MVCJEH=TeeD\?^C9g8R;d&gt;H6IiPFH=c][&lt;ZB[hjDbFB_957AN]_Y@;LmlTJJLoNJh0bd1_oGRAHQ=kBGkh192G2Emo\9;b`C9J&gt;Id:FX8XjH3JV]]jHQ=`N\FDOBTP&gt;Mf]:j\m7Zd=P=^69k;9`Mcl3diU^SJVTXE&gt;fBZ&lt;NDFdEPe6ZFGhL9YHna62=1NAeVn]ehPiA6a7ohBYm9FVD0giCam0^W;RIL:n1Ze90k69f&lt;`XLXZJ\abmD4Jk9RlbFcI^C6NN[\ij6N[?lHHKcEji6N[k\i6WN[\^i6NhKdm97K\fEV8GPdjl6E29IbWka2fB1D5]AjIgEVF?C34MeQ5F0lH7FO5&gt;cm2KAT]k5b9iEkadMUD:ITV_\4F4TIF?4U9C7cfdBAGL;UK8]KGoH3gEHdc9:ST@2nKHNN2`iK[7:REBIhOAGgCPVk]B3]Fi16P`C\?P\\@WW1j7L;aYm5E&gt;9C\69MO0neG=gjA[JCl2clGo&gt;mKoQPMneg_Jo]F3Do?bN&gt;;&gt;oONd^N?:V[:haSC0]ZUk?Oc?oOBfOg5g`5Q[gCCa3^DNjDFD:G5aBhEU6UEM\X;Q^c\06NWfXZ27nVi[2T[gQM5]kTNQ@TEfIhV`8GaE&lt;mADXI1jNWUaK9CA5L=0k?C3V=kSDV&gt;^T6;]4L79;oA`U`Z5l5k0GAmJ0=MH2egZ8k1nVnOd1]TlRaIWkjH8Y1hEgFNXMUm_YbSgFaP&gt;D6&gt;]M;VB]O[QMd;h_\6Hg5oYV`UbDNH^U[UA?oG7hKVBNFJC25kHEhY:^ZNQY;U2ek8gCT\7]Yf&lt;54oL2&lt;aTU74Wi2b&gt;7cDc&gt;?keFDiTZ?6n3P1?o;c?21XS4nZgHmAk]lPS]?PgCi:e?C9G:BmkVD^EcC5?BM`V^h5&lt;M;389SOTH1k7V9R;5ch_70;9objaU\H^ZM^kW6@&lt;7TZZOWBWn&lt;5c@QXJgY0D:nEoBJRWKD@&gt;XVO\U2nW=iH&lt;mLogXf`g_IafSW:A926DN2R:I0@=\`7?0d858eT06h2Ta6jXHAJBQT2U;\`A5Z8QA:=@T:TI2mm1&lt;nTQ8LBd]S`LN8&lt;9ZTdfc10P@AfE83FC64IZ210IU21W0&lt;A:o:YP3aodV`Od=`P8POJahNPBHDX1N;06?ZL4XPl0e@l\0l:dL&gt;mj8&gt;B374D_a1X&lt;X69N7VHU3b@RO?7nRHQD`@0Q&gt;JkBS3kEA_U?XH660WS4210`XJ3JP=JRR4WWa4BD0WmZ&lt;Oa\4&gt;0S4A0Q&lt;iF86PY4ST&lt;c1aZ@Q5Q9aVX1HmY1I3C&gt;3n2P&lt;62JjY3Dg1h@PXG:C0;&lt;FK2d1J\2@]0b80&gt;c562T2@D&gt;3nFQHE;Rh::HDa5_YHQEC`XP:1ZG5Q&lt;D8HD@SH:h\K88k0ab^4R9VQ=H\0V4018FNR54\AOBFhNa4D:XRU_538ZFP7&lt;ZhP8_Ae06R6l@=PRl6X@\5^SSH@ZnMml`dR`Bl5636jEA[P5:&lt;0G:;:TneHK&gt;N5kQiHTOjHIN[_aPh&gt;N\@XN_mX^f]E5CKm6Zce:l2AmS399@g58P@a?QgL5lQ`cm2JHTTUR8IIKM864C_k&lt;BC`a1@[dE;Pgki5CC6^0Zf\C?\Ah9`BJIYFEVY=XT4cY\]BXbEIDo:T96jiC\:;BjS;a]E@XXRTZL7BV&lt;mBPFO8A6DYA:?9WYTPIX@F9R@e^EgDY]?[U1lZOFA[KdWHSV]&lt;GfMXMeHH;46Uj_SbEHdjTO6[lG5MZQRf[mAnUk&gt;@6VQY:]:[4cXfG2h_ab^Eb9T6i;RRARUkHKn8N6ZZB=&gt;QlO34A47@S0e0SW=AB2HU=CARD5g69HSDdE69SQDd6j9F5JAR1?n8lMi03e_jh:WTnW`[oLdoJPb:nf_5\d10&gt;E@R@8F?;Q8_7WU&lt;=&gt;RQ3UeiKX7]Z^?5kccV[KoGViG=lC6U]a]`hZ@c?TPI\d77iMcidQ]:PPX:DfW;Co:KkH0Vi5]D?IM:X0YETom=[F5N`2aQ@TS6?V=APERT0P&lt;F;=3\h3B26&gt;@lRj1m0P@Gh0JZ0BM@&lt;e;JSU?Mh@`Uh7:V3RLQ`J&lt;1C0Yeb&gt;[8g4oNcP5:D@I3]ReZN:Vm^58LW@1;523mMi^e`9_@NHTgH=U7EKif3YT_Q6_70lmTk_NmVW]li?e]2M`gJ&gt;UUlB&lt;LFOdoQjgid]hGR9lWYMfDo=1g2X7l</protected>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='21'>
			<Action classname='StepType' isroottypedef='true' typecategory='1' timestamp='1618215606' typeversion='21.0.0.2' typelastmodversion='21.0.0.0' typeminprodversion='21.0.0.0' typeflags='33554446'>
				<subprops>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs' flagsforinstances='524312' instanceoverrideflags='655384'>
						<value lbound='[0]' ubound='[]'/>
					</Substeps>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "ACTION_DESCRIPTION_NAME") + (("%ModuleDescription" == "") ? "" : ",  %ModuleDescription")</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "ACTION_DEF_STEP_NAME")</value>
					</DefaultNameFormat>
					<Menu typename='StepTypeMenu' xsi:type='StepTypeMenu' classname='Obj' flagsforinstances='524312' instanceoverrideflags='524312'>
						<subprops>
							<CanBeSubstepType classname='Bool'>
								<value>false</value>
							</CanBeSubstepType>
							<CanOnlyBeSubstepType classname='Bool'>
								<value>false</value>
							</CanOnlyBeSubstepType>
							<Category classname='Str'>
								<value>""</value>
							</Category>
							<ItemName classname='ExprValue'>
								<value>ResStr("NI_STEPTYPES", "ACTION_MENU_ITEM_NAME")</value>
							</ItemName>
							<SingularItemName classname='Str'>
								<value>""</value>
							</SingularItemName>
							<SeparatorBeforeCategory classname='Bool'>
								<value>false</value>
							</SeparatorBeforeCategory>
							<SeparatorBeforeItemName classname='Bool'>
								<value>false</value>
							</SeparatorBeforeItemName>
							<Group classname='Str'>
								<value>Action</value>
							</Group>
						</subprops>
					</Menu>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='262168' instanceoverrideflags='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value/>
							</Icon>
							<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7143448' structureflags='2097152'/>
							<PreCond classname='ExprValue'>
								<value/>
							</PreCond>
							<LoadOpt classname='Str'>
								<value>PreloadWhenExecuted</value>
							</LoadOpt>
							<UnloadOpt classname='Str'>
								<value>UnloadWithFile</value>
							</UnloadOpt>
							<Mode classname='Str'>
								<value>Normal</value>
							</Mode>
							<WindowActivation classname='Str'>
								<value>None</value>
							</WindowActivation>
							<ResultOption classname='Num'>
								<value>1</value>
							</ResultOption>
							<StepFCSeqF classname='Bool'>
								<value>true</value>
							</StepFCSeqF>
							<IgnoreRTE classname='Bool'>
								<value>false</value>
							</IgnoreRTE>
							<UseMutex classname='Bool'>
								<value>false</value>
							</UseMutex>
							<MutexNameOrRef classname='ExprValue'>
								<value/>
							</MutexNameOrRef>
							<BatchSyncOpt classname='Num'>
								<value>0</value>
							</BatchSyncOpt>
							<SwitchEnabled classname='Bool'>
								<value>false</value>
							</SwitchEnabled>
							<VirtualDeviceName classname='ExprValue'>
								<value/>
							</VirtualDeviceName>
							<SwitchOperation classname='Num'>
								<value>1</value>
							</SwitchOperation>
							<RouteGroupConnect classname='ExprValue'>
								<value/>
							</RouteGroupConnect>
							<RouteGroupDisconnect classname='ExprValue'>
								<value/>
							</RouteGroupDisconnect>
							<MulticonnectMode classname='Num'>
								<value>1</value>
							</MulticonnectMode>
							<OperationOrder classname='Num'>
								<value>2</value>
							</OperationOrder>
							<ConnectionLifetime classname='Num'>
								<value>0</value>
							</ConnectionLifetime>
							<WaitForDebounce classname='Bool'>
								<value>true</value>
							</WaitForDebounce>
							<PassAct classname='Str' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value>Next</value>
							</PassAct>
							<FailAct classname='Str' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value>Next</value>
							</FailAct>
							<PassActTarget classname='ExprValue' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value/>
							</PassActTarget>
							<FailActTarget classname='ExprValue' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value/>
							</FailActTarget>
							<CustExpr classname='ExprValue'>
								<value/>
							</CustExpr>
							<CustTrueAct classname='Str'>
								<value>Next</value>
							</CustTrueAct>
							<CustFalseAct classname='Str'>
								<value>Next</value>
							</CustFalseAct>
							<CustTrueActTarget classname='ExprValue'>
								<value/>
							</CustTrueActTarget>
							<CustFalseActTarget classname='ExprValue'>
								<value/>
							</CustFalseActTarget>
							<LoopType classname='Str'>
								<value>NoLooping</value>
							</LoopType>
							<LoopWhile classname='ExprValue'>
								<value/>
							</LoopWhile>
							<LoopStatus classname='ExprValue'>
								<value/>
							</LoopStatus>
							<LoopIncrement classname='ExprValue'>
								<value>RunState.LoopIndex += 1</value>
							</LoopIncrement>
							<LoopInitialize classname='ExprValue'>
								<value>RunState.LoopIndex = 0</value>
							</LoopInitialize>
							<LoopOpt classname='Num'>
								<value>0</value>
							</LoopOpt>
							<PreExpr classname='ExprValue'>
								<value/>
							</PreExpr>
							<PostExpr classname='ExprValue'>
								<value/>
							</PostExpr>
							<StatusExpr classname='ExprValue'>
								<value/>
							</StatusExpr>
							<CanSpecifyModule classname='Bool'>
								<value>true</value>
							</CanSpecifyModule>
							<CanEditCode classname='Bool'>
								<value>true</value>
							</CanEditCode>
							<CanEditModulePrototype classname='Bool'>
								<value>true</value>
							</CanEditModulePrototype>
							<CanEditParameterAdditionalResults classname='Bool'>
								<value>true</value>
							</CanEditParameterAdditionalResults>
							<PrecondIntExe classname='Num'>
								<value>0</value>
							</PrecondIntExe>
							<Requirements classname='Obj' flagsforinstances='1' valueflags='1' structureflags='2097152'>
								<subprops>
									<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
										<value lbound='[0]' ubound='[]'/>
									</Links>
								</subprops>
							</Requirements>
							<CustomResults classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</CustomResults>
							<AdditionalResultsHints classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</AdditionalResultsHints>
						</subprops>
					</TS>
					<NI_Data typename='StepTypeNIData' xsi:type='StepTypeNIData' classname='Obj'>
						<subprops>
							<EditPanels classname='Strs'>
								<value lbound='[0]' ubound='[]'/>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
						<subprops>
							<Error typename='Error' xsi:type='Error' classname='Obj' flagsforinstances='4194304' instanceoverrideflags='4194304' valueflags='4194304'>
								<subprops>
									<Code classname='Num'>
										<value>0</value>
									</Code>
									<Msg classname='Str'>
										<value/>
									</Msg>
									<Occurred classname='Bool'>
										<value>false</value>
									</Occurred>
								</subprops>
							</Error>
							<Status classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</Status>
							<ReportText classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</ReportText>
							<Common typename='CommonResults' xsi:type='CommonResults' classname='Obj' instanceoverrideflags='4194304'/>
						</subprops>
					</Result>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>DefaultLabVIEW|DefaultLabVIEWNXG|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|DefaultHTB80_Template|Default_Template</value>
					</CodeTemplates>
					<BlockStartTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockStartTypes>
					<BlockEndTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockEndTypes>
					<AppliesToBlockStructure classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</AppliesToBlockStructure>
					<CanEncapsulate classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</CanEncapsulate>
					<Category classname='Str' valueflags='24' structureflags='524288'>
						<value>Action</value>
					</Category>
				</subprops>
			</Action>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='24'>
			<NI_PythonParameterResult classname='PythonParameterResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>1</value>
					</CheckedState>
				</subprops>
			</NI_PythonParameterResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='23'>
			<NI_PythonParameter classname='CPythonParameter' isroottypedef='true' typecategory='3' timestamp='1650060872' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name classname='Str'>
						<value>_notNamed</value>
					</Name>
					<Type classname='Num'>
						<value>7</value>
					</Type>
					<ArgumentValue typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgumentValue>
					<ArgumentDisplayValue typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgumentDisplayValue>
					<AdditionalResults classname='Obj'>
						<subprops>
							<Input typename='NI_PythonParameterResult' xsi:type='NI_PythonParameterResult' classname='PythonParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Input>
							<Output typename='NI_PythonParameterResult' xsi:type='NI_PythonParameterResult' classname='PythonParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Output>
						</subprops>
					</AdditionalResults>
				</subprops>
			</NI_PythonParameter>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='22'>
			<PythonStepAdditions classname='CPythonModule' isroottypedef='true' typecategory='3' timestamp='1650060872' typeversion='21.0.0.49156' typelastmodversion='21.0.0.49156' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<PythonCall classname='CPythonCall'>
						<subprops>
							<UseAdapterSettingsForInterpreterSession classname='Bool'>
								<value>true</value>
							</UseAdapterSettingsForInterpreterSession>
							<InterpreterSessionScope classname='Num'>
								<value>3</value>
							</InterpreterSessionScope>
							<PythonVersion classname='Str'>
								<value/>
							</PythonVersion>
							<PythonVirtualEnvironmentPath classname='Str'>
								<value/>
							</PythonVirtualEnvironmentPath>
							<InterpreterLocation typename='Expression' xsi:type='Expression' classname='ExprValue'>
								<value/>
							</InterpreterLocation>
							<CreateIfInterpreterDoesNotExist classname='Bool'>
								<value>true</value>
							</CreateIfInterpreterDoesNotExist>
							<ModulePath typename='Path' xsi:type='Path' classname='PathValue'>
								<value/>
							</ModulePath>
							<OperationType classname='Num'>
								<value>1</value>
							</OperationType>
							<OperationScope classname='Num'>
								<value>0</value>
							</OperationScope>
							<ClassName classname='Str'>
								<value/>
							</ClassName>
							<ClassInstanceLocation typename='Expression' xsi:type='Expression' classname='ExprValue'>
								<value/>
							</ClassInstanceLocation>
							<FunctionOrAttributeName classname='Str'>
								<value/>
							</FunctionOrAttributeName>
							<Parameters classname='Objs'>
								<value lbound='[0]' ubound='[0]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name='' classname='CPythonParameter' structureflags='131072'>
											<subprops>
												<Name classname='Str'>
													<value>_notNamed</value>
												</Name>
												<Type classname='Num'>
													<value>7</value>
												</Type>
												<ArgumentValue classname='ExprValue'>
													<value/>
												</ArgumentValue>
												<ArgumentDisplayValue classname='ExprValue'>
													<value/>
												</ArgumentDisplayValue>
												<AdditionalResults classname='Obj'>
													<subprops>
														<Input classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Input>
														<Output classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Output>
													</subprops>
												</AdditionalResults>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
									<value>
										<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
											<subprops>
												<Name classname='Str'>
													<value>Return Value</value>
												</Name>
												<Type classname='Num'>
													<value>7</value>
												</Type>
												<ArgumentValue classname='ExprValue'>
													<value/>
												</ArgumentValue>
												<ArgumentDisplayValue classname='ExprValue'>
													<value/>
												</ArgumentDisplayValue>
												<AdditionalResults classname='Obj'>
													<subprops>
														<Input classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Input>
														<Output classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Output>
													</subprops>
												</AdditionalResults>
											</subprops>
										</CPythonParameter>
									</value>
								</value>
							</Parameters>
							<DefaultParamCategoryForArray classname='Num'>
								<value>5</value>
							</DefaultParamCategoryForArray>
						</subprops>
					</PythonCall>
				</subprops>
			</PythonStepAdditions>
		</typedef>
	</typelist>
	<Data classname='SequenceFileData' valueflags='4194304'>
		<subprops>
			<Seq classname='Objs' valueflags='4194304'>
				<value lbound='[0]' ubound='[0]'>
					<value>
						<Sequence name='MainSequence'>
							<subprops>
								<Parameters classname='Obj' valueflags='4456448'/>
								<Locals classname='Obj' valueflags='4194304'>
									<subprops>
										<ResultList classname='Objs' valueflags='4194304'>
											<value lbound='[0]' ubound='[]'>
												<elemproto>
													<_NAME_IN_ATTRIBUTE_ name='' classname='TEResult'/>
												</elemproto>
											</value>
										</ResultList>
									</subprops>
								</Locals>
								<Main classname='Objs' valueflags='4194304'>
									<value lbound='[0]' ubound='[0]'>
										<value>
											<Step typename='NI_Measurement' xsi:type='NI_Measurement' name='Test SPI device'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:1m8fotxw7RGuNrjdh1OqZD</value>
															</Id>
															<Icon classname='Str'>
																<value>Measurement\Measurement.ico</value>
															</Icon>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>1</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>4</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
													<Measurement classname='Obj'>
														<subprops>
															<Name classname='Str'>
																<value>ni.examples.NIDigitalSPI_Python</value>
															</Name>
															<Parameters classname='Objs'>
																<value lbound='[0]' ubound='[7]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='Obj'>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value/>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value/>
																				</Direction>
																				<Log classname='Bool'>
																					<value>false</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value/>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>0</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value/>
																				</TypeSpecialization>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>pin_names</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>{"SPI_PINS"}</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>1</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeString</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>1</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>IOResource</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>specification_file_path</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>"Specifications.specs"</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeString</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>2</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>Path</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>levels_file_path</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>"PinLevels.digilevels"</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeString</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>3</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>Path</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>timing_file_path</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>"Timing.digitiming"</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeString</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>4</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>Path</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>pattern_file_path</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>"Pattern.digipat"</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeString</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>5</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>Path</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>load_files</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>False</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeBool</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>6</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>passing_sites</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>Out</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>1</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeInt32</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>1</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>failing_sites</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>Out</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>1</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeInt32</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>2</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																</value>
															</Parameters>
														</subprops>
													</Measurement>
												</subprops>
											</Step>
										</value>
									</value>
								</Main>
								<Setup classname='Objs' valueflags='4194304'>
									<value lbound='[0]' ubound='[4]'>
										<value>
											<Step typename='NI_UpdatePinMap' xsi:type='NI_UpdatePinMap' name='Update pin map'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:Pun9seiU7hGhxWDjK76h1B</value>
															</Id>
															<Icon classname='Str'>
																<value>NI_SequenceEditor\StepSettings\ni_UpdateMapping.ico</value>
															</Icon>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>4</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
													<PinMapPath classname='PathValue'>
														<value>FileGlobals.MeasurementPlugIns.PinMapPath</value>
													</PinMapPath>
												</subprops>
											</Step>
										</value>
										<value>
											<Step typename='Action' xsi:type='Action' name='Create and register NI-Digital sessions'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:xOJc8WLo7RGhzZiQlrVX7C</value>
															</Id>
															<Icon classname='Str'>
																<value/>
															</Icon>
															<SData typename='PythonStepAdditions' xsi:type='PythonStepAdditions' classname='CPythonModule'>
																<subprops>
																	<PythonCall classname='CPythonCall'>
																		<subprops>
																			<UseAdapterSettingsForInterpreterSession classname='Bool'>
																				<value>false</value>
																			</UseAdapterSettingsForInterpreterSession>
																			<InterpreterSessionScope classname='Num'>
																				<value>2</value>
																			</InterpreterSessionScope>
																			<PythonVersion classname='Str'>
																				<value>3.10</value>
																			</PythonVersion>
																			<PythonVirtualEnvironmentPath classname='Str'>
																				<value>.venv</value>
																			</PythonVirtualEnvironmentPath>
																			<InterpreterLocation classname='ExprValue'>
																				<value/>
																			</InterpreterLocation>
																			<CreateIfInterpreterDoesNotExist classname='Bool'>
																				<value>true</value>
																			</CreateIfInterpreterDoesNotExist>
																			<ModulePath classname='PathValue'>
																				<value>teststand_nidigital.py</value>
																			</ModulePath>
																			<OperationType classname='Num'>
																				<value>1</value>
																			</OperationType>
																			<OperationScope classname='Num'>
																				<value>0</value>
																			</OperationScope>
																			<ClassName classname='Str'>
																				<value/>
																			</ClassName>
																			<ClassInstanceLocation classname='ExprValue'>
																				<value/>
																			</ClassInstanceLocation>
																			<FunctionOrAttributeName classname='Str'>
																				<value>create_nidigital_sessions</value>
																			</FunctionOrAttributeName>
																			<Parameters classname='Objs'>
																				<value lbound='[0]' ubound='[1]'>
																					<elemproto>
																						<_NAME_IN_ATTRIBUTE_ name='' classname='CPythonParameter' structureflags='0'/>
																					</elemproto>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>Return Value</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value/>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>sequence_context</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value>ThisContext</value>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																				</value>
																			</Parameters>
																			<DefaultParamCategoryForArray classname='Num'>
																				<value>5</value>
																			</DefaultParamCategoryForArray>
																		</subprops>
																	</PythonCall>
																</subprops>
															</SData>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>0</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
												</subprops>
											</Step>
										</value>
										<value>
											<Step typename='Action' xsi:type='Action' name='Load NI-Digital pin map'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:aaiakmPo7RGhzZiQlrVX7C</value>
															</Id>
															<Icon classname='Str'>
																<value/>
															</Icon>
															<SData typename='PythonStepAdditions' xsi:type='PythonStepAdditions' classname='CPythonModule'>
																<subprops>
																	<PythonCall classname='CPythonCall'>
																		<subprops>
																			<UseAdapterSettingsForInterpreterSession classname='Bool'>
																				<value>false</value>
																			</UseAdapterSettingsForInterpreterSession>
																			<InterpreterSessionScope classname='Num'>
																				<value>2</value>
																			</InterpreterSessionScope>
																			<PythonVersion classname='Str'>
																				<value>3.10</value>
																			</PythonVersion>
																			<PythonVirtualEnvironmentPath classname='Str'>
																				<value>.venv</value>
																			</PythonVirtualEnvironmentPath>
																			<InterpreterLocation classname='ExprValue'>
																				<value/>
																			</InterpreterLocation>
																			<CreateIfInterpreterDoesNotExist classname='Bool'>
																				<value>true</value>
																			</CreateIfInterpreterDoesNotExist>
																			<ModulePath classname='PathValue'>
																				<value>teststand_nidigital.py</value>
																			</ModulePath>
																			<OperationType classname='Num'>
																				<value>1</value>
																			</OperationType>
																			<OperationScope classname='Num'>
																				<value>0</value>
																			</OperationScope>
																			<ClassName classname='Str'>
																				<value/>
																			</ClassName>
																			<ClassInstanceLocation classname='ExprValue'>
																				<value/>
																			</ClassInstanceLocation>
																			<FunctionOrAttributeName classname='Str'>
																				<value>load_nidigital_pin_map</value>
																			</FunctionOrAttributeName>
																			<Parameters classname='Objs'>
																				<value lbound='[0]' ubound='[2]'>
																					<elemproto>
																						<_NAME_IN_ATTRIBUTE_ name='' classname='CPythonParameter' structureflags='0'/>
																					</elemproto>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>Return Value</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value/>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>pin_map_path</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value>FileGlobals.MeasurementPlugIns.PinMapPath</value>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>sequence_context</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value>ThisContext</value>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																				</value>
																			</Parameters>
																			<DefaultParamCategoryForArray classname='Num'>
																				<value>5</value>
																			</DefaultParamCategoryForArray>
																		</subprops>
																	</PythonCall>
																</subprops>
															</SData>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>0</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
												</subprops>
											</Step>
										</value>
										<value>
											<Step typename='Action' xsi:type='Action' name='Load NI-Digital specifications, levels, and timing'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:RUvVq2Po7RGhzZiQlrVX7C</value>
															</Id>
															<Icon classname='Str'>
																<value/>
															</Icon>
															<SData typename='PythonStepAdditions' xsi:type='PythonStepAdditions' classname='CPythonModule'>
																<subprops>
																	<PythonCall classname='CPythonCall'>
																		<subprops>
																			<UseAdapterSettingsForInterpreterSession classname='Bool'>
																				<value>false</value>
																			</UseAdapterSettingsForInterpreterSession>
																			<InterpreterSessionScope classname='Num'>
																				<value>2</value>
																			</InterpreterSessionScope>
																			<PythonVersion classname='Str'>
																				<value>3.10</value>
																			</PythonVersion>
																			<PythonVirtualEnvironmentPath classname='Str'>
																				<value>.venv</value>
																			</PythonVirtualEnvironmentPath>
																			<InterpreterLocation classname='ExprValue'>
																				<value/>
																			</InterpreterLocation>
																			<CreateIfInterpreterDoesNotExist classname='Bool'>
																				<value>true</value>
																			</CreateIfInterpreterDoesNotExist>
																			<ModulePath classname='PathValue'>
																				<value>teststand_nidigital.py</value>
																			</ModulePath>
																			<OperationType classname='Num'>
																				<value>1</value>
																			</OperationType>
																			<OperationScope classname='Num'>
																				<value>0</value>
																			</OperationScope>
																			<ClassName classname='Str'>
																				<value/>
																			</ClassName>
																			<ClassInstanceLocation classname='ExprValue'>
																				<value/>
																			</ClassInstanceLocation>
																			<FunctionOrAttributeName classname='Str'>
																				<value>load_nidigital_specifications_levels_and_timing</value>
																			</FunctionOrAttributeName>
																			<Parameters classname='Objs'>
																				<value lbound='[0]' ubound='[4]'>
																					<elemproto>
																						<_NAME_IN_ATTRIBUTE_ name='' classname='CPythonParameter' structureflags='0'/>
																					</elemproto>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>Return Value</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value/>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>specifications_file_paths</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value>FileGlobals.MeasurementPlugIns.SpecificationsFilePaths</value>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>levels_file_paths</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value>FileGlobals.MeasurementPlugIns.LevelsFilePaths</value>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>timing_file_paths</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value>FileGlobals.MeasurementPlugIns.TimingFilePaths</value>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>sequence_context</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value>ThisContext</value>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																				</value>
																			</Parameters>
																			<DefaultParamCategoryForArray classname='Num'>
																				<value>5</value>
																			</DefaultParamCategoryForArray>
																		</subprops>
																	</PythonCall>
																</subprops>
															</SData>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>0</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
												</subprops>
											</Step>
										</value>
										<value>
											<Step typename='Action' xsi:type='Action' name='Load NI-Digital patterns'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:RkvVq2Po7RGhzZiQlrVX7C</value>
															</Id>
															<Icon classname='Str'>
																<value/>
															</Icon>
															<SData typename='PythonStepAdditions' xsi:type='PythonStepAdditions' classname='CPythonModule'>
																<subprops>
																	<PythonCall classname='CPythonCall'>
																		<subprops>
																			<UseAdapterSettingsForInterpreterSession classname='Bool'>
																				<value>false</value>
																			</UseAdapterSettingsForInterpreterSession>
																			<InterpreterSessionScope classname='Num'>
																				<value>2</value>
																			</InterpreterSessionScope>
																			<PythonVersion classname='Str'>
																				<value>3.10</value>
																			</PythonVersion>
																			<PythonVirtualEnvironmentPath classname='Str'>
																				<value>.venv</value>
																			</PythonVirtualEnvironmentPath>
																			<InterpreterLocation classname='ExprValue'>
																				<value/>
																			</InterpreterLocation>
																			<CreateIfInterpreterDoesNotExist classname='Bool'>
																				<value>true</value>
																			</CreateIfInterpreterDoesNotExist>
																			<ModulePath classname='PathValue'>
																				<value>teststand_nidigital.py</value>
																			</ModulePath>
																			<OperationType classname='Num'>
																				<value>1</value>
																			</OperationType>
																			<OperationScope classname='Num'>
																				<value>0</value>
																			</OperationScope>
																			<ClassName classname='Str'>
																				<value/>
																			</ClassName>
																			<ClassInstanceLocation classname='ExprValue'>
																				<value/>
																			</ClassInstanceLocation>
																			<FunctionOrAttributeName classname='Str'>
																				<value>load_nidigital_patterns</value>
																			</FunctionOrAttributeName>
																			<Parameters classname='Objs'>
																				<value lbound='[0]' ubound='[2]'>
																					<elemproto>
																						<_NAME_IN_ATTRIBUTE_ name='' classname='CPythonParameter' structureflags='0'/>
																					</elemproto>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>Return Value</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value/>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>pattern_file_paths</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value>FileGlobals.MeasurementPlugIns.PatternFilePaths</value>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>sequence_context</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value>ThisContext</value>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																				</value>
																			</Parameters>
																			<DefaultParamCategoryForArray classname='Num'>
																				<value>5</value>
																			</DefaultParamCategoryForArray>
																		</subprops>
																	</PythonCall>
																</subprops>
															</SData>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>0</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
												</subprops>
											</Step>
										</value>
									</value>
								</Setup>
								<Cleanup classname='Objs' valueflags='4194304'>
									<value lbound='[0]' ubound='[0]'>
										<value>
											<Step typename='Action' xsi:type='Action' name='Destroy and unregister NI-Digital sessions'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:2uQF+WLo7RGhzZiQlrVX7C</value>
															</Id>
															<Icon classname='Str'>
																<value/>
															</Icon>
															<SData typename='PythonStepAdditions' xsi:type='PythonStepAdditions' classname='CPythonModule'>
																<subprops>
																	<PythonCall classname='CPythonCall'>
																		<subprops>
																			<UseAdapterSettingsForInterpreterSession classname='Bool'>
																				<value>false</value>
																			</UseAdapterSettingsForInterpreterSession>
																			<InterpreterSessionScope classname='Num'>
																				<value>2</value>
																			</InterpreterSessionScope>
																			<PythonVersion classname='Str'>
																				<value>3.10</value>
																			</PythonVersion>
																			<PythonVirtualEnvironmentPath classname='Str'>
																				<value>.venv</value>
																			</PythonVirtualEnvironmentPath>
																			<InterpreterLocation classname='ExprValue'>
																				<value/>
																			</InterpreterLocation>
																			<CreateIfInterpreterDoesNotExist classname='Bool'>
																				<value>true</value>
																			</CreateIfInterpreterDoesNotExist>
																			<ModulePath classname='PathValue'>
																				<value>teststand_nidigital.py</value>
																			</ModulePath>
																			<OperationType classname='Num'>
																				<value>1</value>
																			</OperationType>
																			<OperationScope classname='Num'>
																				<value>0</value>
																			</OperationScope>
																			<ClassName classname='Str'>
																				<value/>
																			</ClassName>
																			<ClassInstanceLocation classname='ExprValue'>
																				<value/>
																			</ClassInstanceLocation>
																			<FunctionOrAttributeName classname='Str'>
																				<value>destroy_nidigital_sessions</value>
																			</FunctionOrAttributeName>
																			<Parameters classname='Objs'>
																				<value lbound='[0]' ubound='[0]'>
																					<elemproto>
																						<_NAME_IN_ATTRIBUTE_ name='' classname='CPythonParameter' structureflags='0'/>
																					</elemproto>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>Return Value</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value/>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																				</value>
																			</Parameters>
																			<DefaultParamCategoryForArray classname='Num'>
																				<value>5</value>
																			</DefaultParamCategoryForArray>
																		</subprops>
																	</PythonCall>
																</subprops>
															</SData>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>0</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
												</subprops>
											</Step>
										</value>
									</value>
								</Cleanup>
								<RecordResults classname='Bool' valueflags='4194312'>
									<value>true</value>
								</RecordResults>
								<RTS classname='Obj' valueflags='4456456'>
									<subprops>
										<Type classname='Num' valueflags='4194304'>
											<value>0</value>
										</Type>
										<OptimizeNonReentrantCalls classname='Bool' valueflags='4194304'>
											<value>true</value>
										</OptimizeNonReentrantCalls>
										<EPNameExpr classname='Str' valueflags='4194304'>
											<value>"Unnamed Entry Point"</value>
										</EPNameExpr>
										<EPEnabledExpr classname='Str' valueflags='4194304'>
											<value>True</value>
										</EPEnabledExpr>
										<EPMenuHint classname='Str' valueflags='4194304'>
											<value/>
										</EPMenuHint>
										<EPIgnoreClient classname='Bool' valueflags='4194304'>
											<value>false</value>
										</EPIgnoreClient>
										<EPInitiallyHidden classname='Bool' valueflags='4194304'>
											<value>false</value>
										</EPInitiallyHidden>
										<EPCheckToSaveTitledFile classname='Bool' valueflags='4194304'>
											<value>true</value>
										</EPCheckToSaveTitledFile>
										<ShowEPAlways classname='Bool' valueflags='4194304'>
											<value>false</value>
										</ShowEPAlways>
										<ShowEPForFileWin classname='Bool' valueflags='4194304'>
											<value>true</value>
										</ShowEPForFileWin>
										<ShowEPForExeWin classname='Bool' valueflags='4194304'>
											<value>false</value>
										</ShowEPForExeWin>
										<ShowEPForEditorOnly classname='Bool' valueflags='4194304'>
											<value>false</value>
										</ShowEPForEditorOnly>
										<AllowIntExeOfEP classname='Bool' valueflags='4194304'>
											<value>false</value>
										</AllowIntExeOfEP>
										<CopyStepsOnOverriding classname='Bool' valueflags='4194304'>
											<value>true</value>
										</CopyStepsOnOverriding>
										<Priority classname='Num' valueflags='4194304'>
											<value>2953567917</value>
										</Priority>
									</subprops>
								</RTS>
								<Requirements classname='Obj' valueflags='4456456'>
									<subprops>
										<Links classname='Strs' valueflags='71303168'>
											<value lbound='[0]' ubound='[]'/>
										</Links>
									</subprops>
								</Requirements>
								<FailureAction classname='Num' valueflags='4194312'>
									<value>2</value>
								</FailureAction>
							</subprops>
						</Sequence>
					</value>
				</value>
			</Seq>
			<FileGlobalDefaults classname='Obj' valueflags='4194304'>
				<subprops>
					<MeasurementPlugIns classname='Obj'>
						<subprops>
							<EnableMonitoring classname='Bool'>
								<value>false</value>
							</EnableMonitoring>
							<PinMapPath typename='Path' xsi:type='Path' classname='PathValue'>
								<value>PinMap.pinmap</value>
							</PinMapPath>
							<SpecificationsFilePaths classname='Strs'>
								<value lbound='[0]' ubound='[0]'>
									<value arrayindex='[0]'>Specifications.specs</value>
								</value>
							</SpecificationsFilePaths>
							<LevelsFilePaths classname='Strs'>
								<value lbound='[0]' ubound='[0]'>
									<value arrayindex='[0]'>PinLevels.digilevels</value>
								</value>
							</LevelsFilePaths>
							<TimingFilePaths classname='Strs'>
								<value lbound='[0]' ubound='[0]'>
									<value arrayindex='[0]'>Timing.digitiming</value>
								</value>
							</TimingFilePaths>
							<PatternFilePaths classname='Strs'>
								<value lbound='[0]' ubound='[0]'>
									<value arrayindex='[0]'>Pattern.digipat</value>
								</value>
							</PatternFilePaths>
						</subprops>
					</MeasurementPlugIns>
				</subprops>
			</FileGlobalDefaults>
			<ModelFile typename='Path' xsi:type='Path' classname='PathValue' valueflags='4194312'>
				<value/>
			</ModelFile>
			<LoadOpt classname='Str' valueflags='4194312'>
				<value>UseStepLoadOpt</value>
			</LoadOpt>
			<UnloadOpt classname='Str' valueflags='4194312'>
				<value>UseStepUnloadOpt</value>
			</UnloadOpt>
			<Version classname='Str' valueflags='4194312'>
				<value>0.0.0.0</value>
			</Version>
			<BatchSync classname='Num' valueflags='4194312'>
				<value>1</value>
			</BatchSync>
			<SFGlobalsScope classname='Num' valueflags='4194312'>
				<value>0</value>
			</SFGlobalsScope>
			<Type classname='Num' valueflags='4194312'>
				<value>0</value>
			</Type>
			<ModelOption classname='Num' valueflags='4194312'>
				<value>0</value>
			</ModelOption>
			<Requirements classname='Obj' valueflags='4194305'>
				<subprops>
					<Links classname='Strs' valueflags='71303168'>
						<value lbound='[0]' ubound='[]'/>
					</Links>
				</subprops>
			</Requirements>
		</subprops>
	</Data>
</teststandfileheader>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/PinLevels.digilevels sha256=736ee06c9eb56920fffc3849d2d8c575f4a9c43daeb9c6e2bd53b66bb5894f31 bytes=1632 -->
## FILE: examples/nidigital_spi/PinLevels.digilevels

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/PinLevels.digilevels`
- sha256: `736ee06c9eb56920fffc3849d2d8c575f4a9c43daeb9c6e2bd53b66bb5894f31`
- bytes: 1632

````text
<?xml version="1.0" encoding="utf-8"?>
<PinLevelsFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/PinLevels">
  <PinLevelsSheet>
    <DigitalPinLevelSets>
      <DigitalPinLevelSet pin="CS">
        <Vil>dc.vcc * 0.7</Vil>
        <Vih>0</Vih>
        <Vol>2.5</Vol>
        <Voh>0.5</Voh>
        <Iol>1.5 m</Iol>
        <Ioh>-1.5 m</Ioh>
        <Vcom>0</Vcom>
        <Vterm>0</Vterm>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
      <DigitalPinLevelSet pin="SCLK">
        <Vil>dc.vcc * 0.7</Vil>
        <Vih>0</Vih>
        <Vol>2.5</Vol>
        <Voh>0.5</Voh>
        <Iol>1.5 m</Iol>
        <Ioh>-1.5 m</Ioh>
        <Vcom>0</Vcom>
        <Vterm>0</Vterm>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
      <DigitalPinLevelSet pin="MOSI">
        <Vil>dc.vcc * 0.7</Vil>
        <Vih>0</Vih>
        <Vol>2.5</Vol>
        <Voh>0.5</Voh>
        <Iol>1.5 m</Iol>
        <Ioh>-1.5 m</Ioh>
        <Vcom>0</Vcom>
        <Vterm>0</Vterm>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
      <DigitalPinLevelSet pin="MISO">
        <Vil>dc.vcc * 0.7</Vil>
        <Vih>0</Vih>
        <Vol>2.5</Vol>
        <Voh>0.5</Voh>
        <Iol>1.5 m</Iol>
        <Ioh>-1.5 m</Ioh>
        <Vcom>0</Vcom>
        <Vterm>0</Vterm>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
    </DigitalPinLevelSets>
  </PinLevelsSheet>
</PinLevelsFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/PinMap.pinmap sha256=0c246ff0829db4d0d9d1127cefbd3b8428a5b5ec1dd1d3be122a1ad0a6d524c4 bytes=2261 -->
## FILE: examples/nidigital_spi/PinMap.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/PinMap.pinmap`
- sha256: `0c246ff0829db4d0d9d1127cefbd3b8428a5b5ec1dd1d3be122a1ad0a6d524c4`
- bytes: 2261

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.5" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDigitalPatternInstrument name="DigitalPattern1" numberOfChannels="32" group="Digital" />
		<NIDigitalPatternInstrument name="DigitalPattern2" numberOfChannels="32" group="Digital" />
	</Instruments>
	<Pins>
		<DUTPin name="CS" />
		<DUTPin name="SCLK" />
		<DUTPin name="MOSI" />
		<DUTPin name="MISO" />
	</Pins>
	<PinGroups>
		<PinGroup name="SPI_PINS">
			<PinReference pin="SCLK" />
			<PinReference pin="CS" />
			<PinReference pin="MOSI" />
			<PinReference pin="MISO" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
		<Site siteNumber="2" />
		<Site siteNumber="3" />
	</Sites>
	<Connections>
		<Connection pin="CS" siteNumber="0" instrument="DigitalPattern1" channel="0" />
		<Connection pin="SCLK" siteNumber="0" instrument="DigitalPattern1" channel="1" />
		<Connection pin="MOSI" siteNumber="0" instrument="DigitalPattern1" channel="2" />
		<Connection pin="MISO" siteNumber="0" instrument="DigitalPattern1" channel="3" />
		<Connection pin="CS" siteNumber="1" instrument="DigitalPattern1" channel="4" />
		<Connection pin="CS" siteNumber="2" instrument="DigitalPattern2" channel="0" />
		<Connection pin="CS" siteNumber="3" instrument="DigitalPattern2" channel="4" />
		<Connection pin="SCLK" siteNumber="1" instrument="DigitalPattern1" channel="5" />
		<Connection pin="MOSI" siteNumber="1" instrument="DigitalPattern1" channel="6" />
		<Connection pin="MISO" siteNumber="1" instrument="DigitalPattern1" channel="7" />
		<Connection pin="MISO" siteNumber="2" instrument="DigitalPattern2" channel="3" />
		<Connection pin="MISO" siteNumber="3" instrument="DigitalPattern2" channel="7" />
		<Connection pin="MOSI" siteNumber="2" instrument="DigitalPattern2" channel="2" />
		<Connection pin="MOSI" siteNumber="3" instrument="DigitalPattern2" channel="6" />
		<Connection pin="SCLK" siteNumber="2" instrument="DigitalPattern2" channel="1" />
		<Connection pin="SCLK" siteNumber="3" instrument="DigitalPattern2" channel="5" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/poetry.toml sha256=ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e bytes=34 -->
## FILE: examples/nidigital_spi/poetry.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/poetry.toml`
- sha256: `ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e`
- bytes: 34

````toml
[virtualenvs]
in-project = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/pyproject.toml sha256=cc90a116287e6adfe0d9a8b98037eb67389c115b1d9feb4265ce541ed3da6e1a bytes=1115 -->
## FILE: examples/nidigital_spi/pyproject.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/pyproject.toml`
- sha256: `cc90a116287e6adfe0d9a8b98037eb67389c115b1d9feb4265ce541ed3da6e1a`
- bytes: 1115

````toml
[tool.poetry]
name = "nidigital_spi"
version = "0.5.0"
package-mode = false
description = "Measurement plug-in example that tests a SPI device using an NI Digital Pattern instrument."
authors = ["National Instruments"]

[tool.poetry.dependencies]
python = "^3.10"
nidigital = { version = ">=1.4.4", extras = ["grpc"] }
ni-measurement-plugin-sdk-service = {version = ">=2.3.1,<4.0"}
click = ">=7.1.2, !=8.1.4" # mypy fails with click 8.1.4: https://github.com/pallets/click/issues/2558
grpcio = "*"

[tool.poetry.group.dev.dependencies]
ni-python-styleguide = ">=0.4.1"
mypy = ">=1.0"
types-grpcio = ">=1.0"
# Uncomment to use prerelease dependencies.
# nidigital = { git = "https://github.com/ni/nimi-python.git", subdirectory = "generated/nidigital", extras = ["grpc"] }
# ni-measurement-plugin-sdk-service = {path = "../../packages/service", develop = true}

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.mypy]
disallow_untyped_defs = true

[[tool.mypy.overrides]]
module = [
    "nidigital.*",
]
ignore_missing_imports = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/README.md sha256=dcda3468a84c71d85a67e72fd51348bf8fc48ad9b699d5bd36eb89821b53de64 bytes=2041 -->
## FILE: examples/nidigital_spi/README.md

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/README.md`
- sha256: `dcda3468a84c71d85a67e72fd51348bf8fc48ad9b699d5bd36eb89821b53de64`
- bytes: 2041

````markdown
## NI-Digital SPI

This is a measurement plug-in example that tests an SPI device using an NI Digital
Pattern instrument.

### Features

- Uses the `nidigital` package to access the NI-Digital Pattern Driver from
  Python
- Pin-aware, supporting one session, multiple pins, and multiple selected sites
- Includes project files for Digital Pattern Editor, InstrumentStudio,
  Measurement Plug-In UI Editor
- Includes a TestStand sequence showing how to configure the pin map, register
  instrument sessions with the session management service, pre-load files into
  the NI-Digital Pattern Driver, and run a measurement
  - For the sake of simplicity, the TestStand sequence handles pin map and
  session registration and unregistration in the `Setup` and `Cleanup` sections
  of the main sequence. For **Test UUTs** and batch process model use cases,
  these steps should be moved to the `ProcessSetup` and `ProcessCleanup`
  callbacks.
- Uses the NI gRPC Device Server to allow sharing instrument sessions with other
  measurement services when running measurements from TestStand

### Required Software

- InstrumentStudio 2025 Q1 or later
- NI-Digital Pattern Driver
- Recommended: TestStand 2021 SP1 or later

### Required Hardware

This example requires an NI Digital Pattern instrument (e.g. PXIe-6570).

By default, this example uses a physical instrument or a simulated instrument
created in NI MAX. To automatically simulate an instrument without using NI MAX,
follow the steps below:
- Create a `.env` file in the measurement service's directory or one of its
  parent directories (such as the root of your Git repository or
  `C:\ProgramData\National Instruments\Plug-Ins\Measurements` for statically
  registered measurement services).
- Add the following options to the `.env` file to enable simulation via the
  driver's option string:

  ```
  MEASUREMENT_PLUGIN_NIDIGITAL_SIMULATE=1
  MEASUREMENT_PLUGIN_NIDIGITAL_BOARD_TYPE=PXIe
  MEASUREMENT_PLUGIN_NIDIGITAL_MODEL=6570
  ```
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/Shmoo.digishmoo sha256=2eaa3e963f29cf93ddbb8b6f8f5e11eb85c3dc966262c6e83018b195d0bfc38b bytes=1208 -->
## FILE: examples/nidigital_spi/Shmoo.digishmoo

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/Shmoo.digishmoo`
- sha256: `2eaa3e963f29cf93ddbb8b6f8f5e11eb85c3dc966262c6e83018b195d0bfc38b`
- bytes: 1208

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="D2BAABBF12CBC90C7D79BDBE3006E7C3" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="4.0.0.24189" FeatureSetName="NI Digital Pattern Editor" MinimumParsableVersion="4.0.0.0" MinimumSemanticallyEquivalentVersion="4.0.0.0" Name="http://www.ni.com/PatternBasedDigital" Version="4.0.0.0" />
		<ParsableNamespace AssemblyFileVersion="4.0.0.24189" FeatureSetName="Editor" MinimumParsableVersion="4.0.0.0" MinimumSemanticallyEquivalentVersion="4.0.0.0" Name="http://www.ni.com/PlatformFramework" Version="4.0.0.29" />
		<ApplicationVersionInfo Name="Digital Pattern Editor" Version="4.0.0.24189" />
	</SourceModelFeatureSet>
	<ShmooSetupDefinition xmlns="http://www.ni.com/PatternBasedDigital">
		<Shmoo Id="1" OutputPath="" PatternName="SPI_Pattern">
			<ShmooAxisSetup Id="2" Name="X-Axis" PinItems="MISO" ShmooType="CompareStrobe" Start="0 µs" StepSize="10 ns" Stop="1.2 µs" TimeSets="SPI" />
			<ShmooAxisSetup Id="3" Name="Y-Axis" PinItems="MISO" ShmooType="Voh" Start="2 V" StepSize="0.1 V" Stop="3 V" TimeSets="SPI" />
		</Shmoo>
	</ShmooSetupDefinition>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/Specifications.specs sha256=52670a64f710ba837694327d5f532b8e6406b7872be001e9d461ab533c3a02a9 bytes=586 -->
## FILE: examples/nidigital_spi/Specifications.specs

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/Specifications.specs`
- sha256: `52670a64f710ba837694327d5f532b8e6406b7872be001e9d461ab533c3a02a9`
- bytes: 586

````text
<?xml version="1.0" encoding="utf-8"?>
<Specifications xmlns:f="http://www.ni.com/schemas/Semiconductor/Formula.xsd" schemaVersion="1.0" xmlns="http://www.ni.com/schemas/Semiconductor/Specifications.xsd">
  <Section name="dc">
    <f:Formula symbol="vcc">
      <f:Definition>5</f:Definition>
      <f:Description>V</f:Description>
    </f:Formula>
  </Section>
  <Section name="ac">
    <f:Formula symbol="period">
      <f:Definition>1 / 1000000</f:Definition>
      <f:Description>1 MHz</f:Description>
    </f:Formula>
  </Section>
  <Description />
</Specifications>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/SPI Example.digiproj sha256=19f34392f02201634d559455405b687c0f3ef96bb1016e309adb814e4fcc9d79 bytes=3546 -->
## FILE: examples/nidigital_spi/SPI Example.digiproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/SPI Example.digiproj`
- sha256: `19f34392f02201634d559455405b687c0f3ef96bb1016e309adb814e4fcc9d79`
- bytes: 3546

````text
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="BB0032E819E476A89A56C8757D885885" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="5.3.1.51258" FeatureSetName="Digital Pattern Editor" Name="http://www.ni.com/PatternBasedDigital" OldestCompatibleVersion="4.5.0.0" Version="4.6.0.49152" />
		<ParsableNamespace AssemblyFileVersion="5.3.1.51258" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="5.2.0.49153" Version="5.2.0.49153" />
		<ApplicationVersionInfo Build="5.3.1.51258" Name="Digital Pattern Editor" Version="19.0.0" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<ProjectSettings Id="1" ModelDefinitionType="ProjectSettings" Name="ZProjectSettings" />
		<NameScopingEnvoy Id="2" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<FileReference Id="44" ModelDefinitionType="PinLevelsDefinition" Name="PinLevels\.digilevels" StoragePath="PinLevels.digilevels" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<SourceFileReference Id="45" ModelDefinitionType="ShmooSetupDefinition" Name="Shmoo\.digishmoo" StoragePath="Shmoo.digishmoo" />
			<FileReference Id="46" ModelDefinitionType="SpecificationsDefinition" Name="Specifications\.specs" StoragePath="Specifications.specs" />
			<FileReference Id="49" ModelDefinitionType="TimingDefinition" Name="Timing\.digitiming" StoragePath="Timing.digitiming" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="56" ModelDefinitionType="PinMap" Name="PinMap\.pinmap" StoragePath="PinMap.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/PatternBasedDigital" />
			<FileReference Id="57" ModelDefinitionType="DigitalPatternEditor.PatternDefinition" Name="Pattern\.digipat" StoragePath="Pattern.digipat" />
			<EmbeddedDefinitionReference Id="58" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}CaptureResultsDefinition" Name="CaptureResults">
				<CaptureResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="60" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}BurstResultsDefinition" Name="BurstResults">
				<BurstResultsDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="62" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}SystemInfoDefinition" Name="SystemInfo">
				<SystemInfoDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="63" ModelDefinitionType="{http://www.ni.com/PatternBasedDigital}DigitalScopeDefinition" Name="DigitalScope">
				<DigitalScopeDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
		<EmbeddedDefinitionReference Id="5" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<EmbeddedDefinitionReference Id="37" ModelDefinitionType="DigitalPatternEditor.ProjectPropertiesDefinition" Name="ProjectProperties">
			<ProjectPropertiesDefinition xmlns="http://www.ni.com/PatternBasedDigital" />
		</EmbeddedDefinitionReference>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/start.bat sha256=bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851 bytes=253 -->
## FILE: examples/nidigital_spi/start.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/start.bat`
- sha256: `bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851`
- bytes: 253

````batch
@echo off
REM The discovery service uses this script to start the measurement service.
REM You can customize this script for your Python setup. The -v option logs
REM messages with level INFO and above.

.venv\Scripts\python.exe measurement.py -v
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/teststand_nidigital.py sha256=4cc37acda454374eb0ac44392c8e7b459e65b96345aae1d5cf6082e4853b3c47 bytes=7817 -->
## FILE: examples/nidigital_spi/teststand_nidigital.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/teststand_nidigital.py`
- sha256: `4cc37acda454374eb0ac44392c8e7b459e65b96345aae1d5cf6082e4853b3c47`
- bytes: 7817

````python
"""Functions to set up and tear down sessions of NI Digital Pattern instruments in NI TestStand."""

from collections.abc import Iterable
from typing import Any

from _helpers import TestStandSupport
from ni_measurement_plugin_sdk_service.discovery import DiscoveryClient
from ni_measurement_plugin_sdk_service.grpc.channelpool import GrpcChannelPool
from ni_measurement_plugin_sdk_service.session_management import (
    INSTRUMENT_TYPE_NI_DIGITAL_PATTERN,
    MultiSessionReservation,
    PinMapContext,
    SessionInitializationBehavior,
    SessionManagementClient,
)


def create_nidigital_sessions(sequence_context: Any) -> None:
    """Create and register all NI-Digital sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    """
    teststand_support = TestStandSupport(sequence_context)
    pin_map_id = teststand_support.get_active_pin_map_id()

    with GrpcChannelPool() as grpc_channel_pool:
        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with _reserve_sessions(
            session_management_client, pin_map_id, INSTRUMENT_TYPE_NI_DIGITAL_PATTERN
        ) as reservation:
            with reservation.initialize_nidigital_sessions(
                initialization_behavior=SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH
            ):
                pass

            session_management_client.register_sessions(reservation.session_info)


def load_nidigital_pin_map(pin_map_path: str, sequence_context: Any) -> None:
    """Load the pin map into the registered NI-Digital sessions.

    Args:
        pin_map_path: An absolute or relative path to the pin map file.
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    """
    teststand_support = TestStandSupport(sequence_context)
    pin_map_id = teststand_support.get_active_pin_map_id()
    pin_map_abs_path = teststand_support.resolve_file_path(pin_map_path)

    with GrpcChannelPool() as grpc_channel_pool:
        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with _reserve_sessions(
            session_management_client, pin_map_id, INSTRUMENT_TYPE_NI_DIGITAL_PATTERN
        ) as reservation:
            with reservation.initialize_nidigital_sessions(
                initialization_behavior=SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION
            ) as session_infos:
                for session_info in session_infos:
                    session_info.session.load_pin_map(pin_map_abs_path)


def load_nidigital_specifications_levels_and_timing(
    specifications_file_paths: Iterable[str],
    levels_file_paths: Iterable[str],
    timing_file_paths: Iterable[str],
    sequence_context: Any,
) -> None:
    """Load specifications, levels, and timing files into NI-Digital sessions.

    Args:
        specifications_file_paths: Absolute or relative paths to the specifications files.
        levels_file_paths: Absolute or relative paths to the levels files.
        timing_file_paths: Absolute or relative paths to the timing files.
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    """
    teststand_support = TestStandSupport(sequence_context)
    pin_map_id = teststand_support.get_active_pin_map_id()
    specifications_file_abs_paths = [
        teststand_support.resolve_file_path(p) for p in specifications_file_paths
    ]
    levels_file_abs_paths = [teststand_support.resolve_file_path(p) for p in levels_file_paths]
    timing_file_abs_paths = [teststand_support.resolve_file_path(p) for p in timing_file_paths]

    with GrpcChannelPool() as grpc_channel_pool:
        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with _reserve_sessions(
            session_management_client, pin_map_id, INSTRUMENT_TYPE_NI_DIGITAL_PATTERN
        ) as reservation:
            with reservation.initialize_nidigital_sessions(
                initialization_behavior=SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION
            ) as session_infos:
                for session_info in session_infos:
                    session_info.session.load_specifications_levels_and_timing(
                        specifications_file_abs_paths, levels_file_abs_paths, timing_file_abs_paths
                    )


def load_nidigital_patterns(
    pattern_file_paths: Iterable[str],
    sequence_context: Any,
) -> None:
    """Load specifications, levels, and timing files into NI-Digital sessions.

    Args:
        pattern_file_paths: Absolute or relative paths to the pattern files.
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    """
    teststand_support = TestStandSupport(sequence_context)
    pin_map_id = teststand_support.get_active_pin_map_id()
    pattern_file_abs_paths = [teststand_support.resolve_file_path(p) for p in pattern_file_paths]

    with GrpcChannelPool() as grpc_channel_pool:
        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with _reserve_sessions(
            session_management_client, pin_map_id, INSTRUMENT_TYPE_NI_DIGITAL_PATTERN
        ) as reservation:
            with reservation.initialize_nidigital_sessions(
                initialization_behavior=SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION
            ) as session_infos:
                for session_info in session_infos:
                    for pattern_file_abs_path in pattern_file_abs_paths:
                        session_info.session.load_pattern(pattern_file_abs_path)


def destroy_nidigital_sessions() -> None:
    """Destroy and unregister all NI-Digital sessions."""
    with GrpcChannelPool() as grpc_channel_pool:
        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with session_management_client.reserve_all_registered_sessions(
            instrument_type_id=INSTRUMENT_TYPE_NI_DIGITAL_PATTERN,
        ) as reservation:
            if not reservation.session_info:
                return

            session_management_client.unregister_sessions(reservation.session_info)
            with reservation.initialize_nidigital_sessions(
                initialization_behavior=SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE
            ):
                pass


def _reserve_sessions(
    session_management_client: SessionManagementClient,
    pin_map_id: str,
    instrument_type_id: str,
) -> MultiSessionReservation:
    pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=None)

    return session_management_client.reserve_sessions(
        pin_map_context, instrument_type_id=instrument_type_id
    )
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidigital_spi/Timing.digitiming sha256=f142d9372d74e6116a91f0b9e462dd486843a001aa69d5a957767115eb9160d2 bytes=1938 -->
## FILE: examples/nidigital_spi/Timing.digitiming

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidigital_spi/Timing.digitiming`
- sha256: `f142d9372d74e6116a91f0b9e462dd486843a001aa69d5a957767115eb9160d2`
- bytes: 1938

````text
<?xml version="1.0" encoding="utf-8"?>
<TimingFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/Timing">
  <TimingSheet>
    <TimeSets>
      <TimeSet name="SPI">
        <Period>ac.period</Period>
        <PinEdges>
          <PinEdge pin="CS">
            <DriveNonReturn>
              <On>0</On>
              <Data>0</Data>
              <Off>ac.period</Off>
            </DriveNonReturn>
            <CompareStrobe>
              <Strobe>(3 * ac.period) / 4</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
          <PinEdge pin="SCLK">
            <ReturnToLow>
              <On>ac.period / 2</On>
              <Data>ac.period / 2</Data>
              <Return>ac.period</Return>
              <Off>ac.period</Off>
            </ReturnToLow>
            <CompareStrobe>
              <Strobe>(3 * ac.period) / 4</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
          <PinEdge pin="MOSI">
            <DriveNonReturn>
              <On>0</On>
              <Data>0</Data>
              <Off>ac.period</Off>
            </DriveNonReturn>
            <CompareStrobe>
              <Strobe>(3 * ac.period) / 4</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
          <PinEdge pin="MISO">
            <DriveNonReturn>
              <On>0</On>
              <Data>0</Data>
              <Off>ac.period</Off>
            </DriveNonReturn>
            <CompareStrobe>
              <Strobe>(3 * ac.period) / 4</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
        </PinEdges>
      </TimeSet>
    </TimeSets>
  </TimingSheet>
</TimingFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidmm_measurement/.serviceignore sha256=997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912 bytes=148 -->
## FILE: examples/nidmm_measurement/.serviceignore

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidmm_measurement/.serviceignore`
- sha256: `997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912`
- bytes: 148

````text
# This file specifies that when we publish this plug-in to a plug-in library,
# we should not copy the following directories:
.venv
__pycache__
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidmm_measurement/_helpers.py sha256=0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426 bytes=2920 -->
## FILE: examples/nidmm_measurement/_helpers.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidmm_measurement/_helpers.py`
- sha256: `0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426`
- bytes: 2920

````python
"""Helper classes and functions for measurement plug-in examples."""

from __future__ import annotations

import logging
import pathlib
from typing import Any, Callable, TypeVar

import click


class TestStandSupport:
    """Class that communicates with TestStand."""

    _PIN_MAP_ID_VAR = "NI.MeasurementPlugIns.PinMapId"

    def __init__(self, sequence_context: Any) -> None:
        """Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        """
        self._sequence_context = sequence_context

    def get_active_pin_map_id(self) -> str:
        """Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        """
        run_time_variables = self._sequence_context.Execution.RunTimeVariables
        if not run_time_variables.Exists(self._PIN_MAP_ID_VAR, 0x0):
            return ""
        return run_time_variables.GetValString(self._PIN_MAP_ID_VAR, 0x0)

    def resolve_file_path(self, file_path: str) -> str:
        """Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        """
        if pathlib.Path(file_path).is_absolute():
            return file_path
        (_, absolute_path, _, _, user_canceled) = self._sequence_context.Engine.FindFileEx(
            fileToFind=file_path,
            absolutePath=None,
            srchDirType=None,
            searchDirectoryIndex=None,
            userCancelled=None,  # Must match spelling used by TestStand
            searchContext=self._sequence_context.SequenceFile,
        )
        if user_canceled:
            raise RuntimeError("File lookup canceled by user.")
        return absolute_path


def configure_logging(verbosity: int) -> None:
    """Configure logging for this process."""
    if verbosity > 1:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=level)


F = TypeVar("F", bound=Callable)


def verbosity_option(func: F) -> F:
    """Decorator for --verbose command line option."""
    return click.option(
        "-v",
        "--verbose",
        "verbosity",
        count=True,
        help="Enable verbose logging. Repeat to increase verbosity.",
    )(func)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidmm_measurement/install.bat sha256=695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025 bytes=205 -->
## FILE: examples/nidmm_measurement/install.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidmm_measurement/install.bat`
- sha256: `695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025`
- bytes: 205

````batch
@echo off
REM The discovery service uses this script to install the dependencies
REM for the measurement service. You can customize this script for your
REM Python setup.

poetry install --only main
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidmm_measurement/measurement.py sha256=05d7475da9efe4e555e283379d3ba26adca3e0d7b872551c7ee7817abe0779b1 bytes=3841 -->
## FILE: examples/nidmm_measurement/measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidmm_measurement/measurement.py`
- sha256: `05d7475da9efe4e555e283379d3ba26adca3e0d7b872551c7ee7817abe0779b1`
- bytes: 3841

````python
"""Perform a measurement using an NI DMM."""

import logging
import math
import pathlib
import sys
from enum import Enum

import click
import ni_measurement_plugin_sdk_service as nims
import nidmm
from _helpers import configure_logging, verbosity_option

script_or_exe = sys.executable if getattr(sys, "frozen", False) else __file__
service_directory = pathlib.Path(script_or_exe).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "NIDmmMeasurement.serviceconfig",
    ui_file_paths=[service_directory / "NIDmmMeasurement.measui"],
)


class Function(Enum):
    """Wrapper enum that contains a zero value."""

    NONE = 0
    DC_VOLTS = nidmm.Function.DC_VOLTS.value
    AC_VOLTS = nidmm.Function.AC_VOLTS.value
    DC_CURRENT = nidmm.Function.DC_CURRENT.value
    AC_CURRENT = nidmm.Function.AC_CURRENT.value
    TWO_WIRE_RES = nidmm.Function.TWO_WIRE_RES.value
    FOUR_WIRE_RES = nidmm.Function.FOUR_WIRE_RES.value
    FREQ = nidmm.Function.FREQ.value
    PERIOD = nidmm.Function.PERIOD.value
    TEMPERATURE = nidmm.Function.TEMPERATURE.value
    AC_VOLTS_DC_COUPLED = nidmm.Function.AC_VOLTS_DC_COUPLED.value
    DIODE = nidmm.Function.DIODE.value
    WAVEFORM_VOLTAGE = nidmm.Function.WAVEFORM_VOLTAGE.value
    WAVEFORM_CURRENT = nidmm.Function.WAVEFORM_CURRENT.value
    CAPACITANCE = nidmm.Function.CAPACITANCE.value
    INDUCTANCE = nidmm.Function.INDUCTANCE.value


@measurement_service.register_measurement
@measurement_service.configuration(
    "pin_name",
    nims.DataType.IOResource,
    "Pin1",
    instrument_type=nims.session_management.INSTRUMENT_TYPE_NI_DMM,
)
@measurement_service.configuration(
    "measurement_type", nims.DataType.Enum, Function.DC_VOLTS, enum_type=Function
)
@measurement_service.configuration("range", nims.DataType.Double, 10.0)
@measurement_service.configuration("resolution_digits", nims.DataType.Double, 5.5)
@measurement_service.output("measured_value", nims.DataType.Double)
@measurement_service.output("signal_out_of_range", nims.DataType.Boolean)
@measurement_service.output("absolute_resolution", nims.DataType.Double)
def measure(
    pin_name: str,
    measurement_type: Function,
    range: float,
    resolution_digits: float,
) -> tuple[float, bool, float]:
    """Perform a measurement using an NI DMM."""
    logging.info(
        "Starting measurement: pin_name=%s measurement_type=%s range=%g resolution_digits=%g",
        pin_name,
        measurement_type,
        range,
        resolution_digits,
    )

    # If the measurement type is not specified, use DC_VOLTS.
    nidmm_function = nidmm.Function(measurement_type.value or Function.DC_VOLTS.value)

    with measurement_service.context.reserve_session(pin_name) as reservation:
        with reservation.initialize_nidmm_session() as session_info:
            session = session_info.session
            session.configure_measurement_digits(nidmm_function, range, resolution_digits)
            measured_value = session.read()
            signal_out_of_range = math.isnan(measured_value) or math.isinf(measured_value)
            absolute_resolution = session.resolution_absolute

    logging.info(
        "Completed measurement: measured_value=%g signal_out_of_range=%s absolute_resolution=%g",
        measured_value,
        signal_out_of_range,
        absolute_resolution,
    )
    return (measured_value, signal_out_of_range, absolute_resolution)


@click.command
@verbosity_option
def main(verbosity: int) -> None:
    """Perform a measurement using an NI DMM."""
    configure_logging(verbosity)

    with measurement_service.host_service():
        input("Press enter to close the measurement service.\n")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidmm_measurement/NIDmmMeasurement.instudioproj sha256=1bacf4c9b8e5f8229d51beafe62724959f93907e83bf7a1d36f6fbd60574b890 bytes=2011 -->
## FILE: examples/nidmm_measurement/NIDmmMeasurement.instudioproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidmm_measurement/NIDmmMeasurement.instudioproj`
- sha256: `1bacf4c9b8e5f8229d51beafe62724959f93907e83bf7a1d36f6fbd60574b890`
- bytes: 2011

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="F0FF82718392C522B83B862254C17FE688C88FF7942BED29C6056DD1DDF16F3C20B10CBF953012C08903635C7A57F13DB255295A6A49C063032380B97172FA59" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.0.0.2317" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2317" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.2317" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="23.0.0.2317" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="f53d543da7be447d977505512a9de1b1" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="7a73cec96722445aaeae940b880f627c" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="f0fd0a1d98c944258fd0797c80775378" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<FileReference Id="56e70fed357c4d8e9ceee504efb458ff" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="NIDmmMeasurement.pinmap" StoragePath="NIDmmMeasurement.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
			<SourceFileReference Bindings="EnvoyManager" Id="48290a0c581843548d2eaeb7c3a50ff8" ModelDefinitionType="NationalInstruments.InstrumentFramework.Document.SourceModel.UnifiedTask" Name="NIDmmMeasurement.sfp" StoragePath="NIDmmMeasurement.sfp" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidmm_measurement/NIDmmMeasurement.measproj sha256=2c31ed31af1385f3f9c31167bc3b63d74663666065a71e2ff7489bce7745dec6 bytes=3800 -->
## FILE: examples/nidmm_measurement/NIDmmMeasurement.measproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidmm_measurement/NIDmmMeasurement.measproj`
- sha256: `2c31ed31af1385f3f9c31167bc3b63d74663666065a71e2ff7489bce7745dec6`
- bytes: 3800

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="D792BBE46574E2FF1DF29E5E2C7D474BF2910F3FF747D2C154781A13E43BE0C9A734913FEDB54672B69FBAAF70DA094CD3F7F0B529A6D3F0CBF74CEF3FF6E8B8" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.0.0.1849" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="23.0.0.1849" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.1849" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.1849" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/EnvoyManagement" OldestCompatibleVersion="5.0.0.0" Version="5.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.1849" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemDiagram" OldestCompatibleVersion="8.0.0.49152" Version="8.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.1849" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemModelCore" OldestCompatibleVersion="5.1.0.5" Version="5.2.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.1849" Name="MeasurementLink UI Editor" Version="23.0.0.1849" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="be463a1023bd4d8c8d22ddb4fd3487a9" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="778ee081853f42058e12959c41c30519" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<EmbeddedDefinitionReference Id="3b4ec0ccec9d43a5b8ab2369c8cfc500" ModelDefinitionType="NationalInstruments.SystemDesigner.SystemDiagram.SystemDiagramDefinition" Name="SystemDiagram">
			<SystemDiagram Id="f3b7cf3339e46aaae85f6ac88aa1de9" SystemDiagramVersion="75" xmlns="http://www.ni.com/SystemDesigner/SystemDiagram">
				<EnvoySuperimpositionContainer Id="608d72bf0a4140ff903dcc1083221dcf" xmlns="http://www.ni.com/SystemDesigner/EnvoyManagement">
					<MappingManager Id="2d7e8a1f82a24f40ae9da3aef7106ef9" xmlns="http://www.ni.com/SystemDesigner/SystemModelCore">
						<Superimposition Id="a56bbf8d750649ec99102d7cd66d46af" Name="Root Superimposition" />
					</MappingManager>
				</EnvoySuperimpositionContainer>
				<SystemDiagramRootDiagram Id="5ab98081b92241ef9d936a66a84e3f1c" />
			</SystemDiagram>
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="d50fb22d2d844728b909564dd4853830" ModelDefinitionType="NullTarget" Name="NullTarget">
			<NullTarget />
		</NameScopingEnvoy>
		<NameScopingEnvoy Id="8a1540a79f81438a8407889bf4817e48" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<FileReference Id="bc6ee95bbfeb42cc992bf0708b654bbe" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="NIDmmMeasurement.pinmap" StoragePath="NIDmmMeasurement.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
			<SourceFileReference Id="d5e4bd3e8510459ea77718b72b2e520a" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="NIDmmMeasurement.measui" StoragePath="NIDmmMeasurement.measui" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidmm_measurement/NIDmmMeasurement.measui sha256=682d0883dd89027800b616604d6e4a69019adf3d32facbff548b40b0aebd5b2f bytes=11001 -->
## FILE: examples/nidmm_measurement/NIDmmMeasurement.measui

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidmm_measurement/NIDmmMeasurement.measui`
- sha256: `682d0883dd89027800b616604d6e4a69019adf3d32facbff548b40b0aebd5b2f`
- bytes: 11001

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="5F497C8D817BD8D9B234A31CC0F19340165F7BD82894EDC6EBFF5AA093070E48F5C451B57321EE41181F5FF3853EB9F65DDC103F5C404E8718DA78D734A88259" Timestamp="1D9F0BBEFB62892" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.9.0.50025" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="9.8.1.49152" />
		<ParsableNamespace AssemblyFileVersion="9.9.0.50025" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="23.5.0.50025" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.9.0.50025" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.9.0.50025" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.5.0.50026" Name="MeasurementLink UI Editor" Version="23.5.0.50026" />
	</SourceModelFeatureSet>
	<Screen ClientId="{26c56ad8-e31a-456d-979e-87865b3f5c61}" DisplayName="NI-DMM Measurement (Py)" Id="f4480b18b95d49bfbefdf2b9d4958707" ServiceClass="ni.examples.NIDmmMeasurement_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
		<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]310" Id="d5c4d136f87c4189a41619217b0d4f32" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]440" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
			<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BaseName="[string]Canvas" Height="[float]143" Id="299e88201b64436290271ab48c3f88c1" Label="[UIModel]8a81dfd7bc5c46228026d1c21aa98288" Left="[float]23" Top="[float]140" Width="[float]127">
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{26c56ad8-e31a-456d-979e-87865b3f5c61}/Configuration/range" Enabled="[bool]True" Height="[float]24" Id="3425530122134004b914e5caafe7fa5c" IsLabelBoundToChannel="[bool]False" Label="[UIModel]c24c5007263c45aaab35919b80ade906" Left="[float]15" RadixBase="[RadixBase]0" RadixVisibility="[SMVisibility]Collapsed" Top="[float]36" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=SystemInternational:Digits=2:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
				<Label Height="[float]16" Id="c24c5007263c45aaab35919b80ade906" LabelOwner="[UIModel]3425530122134004b914e5caafe7fa5c" Left="[float]15" Text="[string]Range" Top="[float]16" Width="[float]33" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{26c56ad8-e31a-456d-979e-87865b3f5c61}/Configuration/resolution_digits" Enabled="[bool]True" Height="[float]24" Id="b2e53e13b3334da8bed886c6b444f06d" IsLabelBoundToChannel="[bool]False" Label="[UIModel]7bf60aff2b8a4acabc48c6f4fbcbfcca" Left="[float]15" Top="[float]96" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=1:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
				<Label Height="[float]16" Id="7bf60aff2b8a4acabc48c6f4fbcbfcca" LabelOwner="[UIModel]b2e53e13b3334da8bed886c6b444f06d" Left="[float]15" Text="[string]Resolution (digits)" Top="[float]76" Width="[float]95" xmlns="http://www.ni.com/PanelCommon" />
			</ScreenSurfaceCanvas>
			<Label Height="[float]16" Id="8a81dfd7bc5c46228026d1c21aa98288" LabelOwner="[UIModel]299e88201b64436290271ab48c3f88c1" Left="[float]23" Text="[string]Configuration" Top="[float]120" Width="[float]73" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{26c56ad8-e31a-456d-979e-87865b3f5c61}/Output/measured_value" Height="[float]51" Id="b8c14ae283ec4bf8ad8a037705e08afc" IsLabelBoundToChannel="[bool]False" IsReadOnly="[bool]True" Label="[UIModel]71a08f4917d143caa1a9edb08cfff3c8" Left="[float]195" MinHeight="[float]51" Top="[float]30" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=7:DigitDisplayType=SignificantDigits:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]220">
				<FontSetting FontFamily="Segoe UI" FontSize="24" Id="142973a4882412f8a4bf0df63295bf1" xmlns="http://www.ni.com/PlatformFramework" />
			</ChannelNumericText>
			<Label Height="[float]16" Id="71a08f4917d143caa1a9edb08cfff3c8" LabelOwner="[UIModel]b8c14ae283ec4bf8ad8a037705e08afc" Left="[float]195" Text="[string]Measured value" Top="[float]10" Width="[float]84" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelLED BaseName="[string]Round LED" Channel="[string]{26c56ad8-e31a-456d-979e-87865b3f5c61}/Output/signal_out_of_range" ContentVisibility="[Visibility]Collapsed" FalseBackground="[SMSolidColorBrush]#ff007133" FalseContent="[string]Off" Height="[float]30" Id="f2df98d24370483dbd8dcef44305f465" IsLabelBoundToChannel="[bool]False" IsReadOnly="[bool]True" Label="[UIModel]9dd1018fef5443e588ca62789b6050fa" Left="[float]195" MinHeight="[float]20" MinWidth="[float]20" Shape="[LEDShape]Round" Top="[float]115" TrueBackground="[SMSolidColorBrush]#ff83ca9d" TrueContent="[string]On" Width="[float]30" />
			<Label Height="[float]16" Id="9dd1018fef5443e588ca62789b6050fa" LabelOwner="[UIModel]f2df98d24370483dbd8dcef44305f465" Left="[float]195" Text="[string]Signal out of range" Top="[float]95" Width="[float]101" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{26c56ad8-e31a-456d-979e-87865b3f5c61}/Output/absolute_resolution" Height="[float]24" Id="6b2cada7604e4852977da8ff18c273e1" IsLabelBoundToChannel="[bool]False" IsReadOnly="[bool]True" Label="[UIModel]60d7911814ad44b890fb464cbbd80e5d" Left="[float]195" RadixBase="[RadixBase]0" RadixVisibility="[SMVisibility]Collapsed" Top="[float]183" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=SystemInternational:Digits=3:DigitDisplayType=SignificantDigits:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
			<Label Height="[float]16" Id="60d7911814ad44b890fb464cbbd80e5d" LabelOwner="[UIModel]6b2cada7604e4852977da8ff18c273e1" Left="[float]195" Text="[string]Absolute resolution" Top="[float]163" Width="[float]103" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{26c56ad8-e31a-456d-979e-87865b3f5c61}/Configuration/pin_name" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="f7b79f2403f9467782561c9c75a54604" IsLabelBoundToChannel="[bool]False" Label="[UIModel]9905796649f44175a56f9eb34178d24e" Left="[float]23" SelectedResource="[NI_Core_DataValues_TagRefnum]Pin1" Top="[float]30" Width="[float]127" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
			<Label Height="[float]16" Id="9905796649f44175a56f9eb34178d24e" LabelOwner="[UIModel]f7b79f2403f9467782561c9c75a54604" Left="[float]23" Text="[string]Pin name" Top="[float]10" Width="[float]49" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{26c56ad8-e31a-456d-979e-87865b3f5c61}/Configuration/measurement_type" Enabled="[bool]True" Height="[float]24" Id="b97cd7939a794245b11a90b37c297997" IsLabelBoundToChannel="[bool]False" Label="[UIModel]d1f28964d0af4b10835729f4ec94466e" Left="[float]23" Top="[float]83" Value="[int]1" Width="[float]127" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
				<RingSelectorInfo DisplayValue="[string]NONE" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]DC_VOLTS" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]AC_VOLTS" IsEnabled="[bool]True" Value="[int]2" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]DC_CURRENT" IsEnabled="[bool]True" Value="[int]3" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]AC_CURRENT" IsEnabled="[bool]True" Value="[int]4" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]TWO_WIRE_RES" IsEnabled="[bool]True" Value="[int]5" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]FOUR_WIRE_RES" IsEnabled="[bool]True" Value="[int]101" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]FREQ" IsEnabled="[bool]True" Value="[int]104" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]PERIOD" IsEnabled="[bool]True" Value="[int]105" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]TEMPERATURE" IsEnabled="[bool]True" Value="[int]108" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]AC_VOLTS_DC_COUPLED" IsEnabled="[bool]True" Value="[int]1001" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]DIODE" IsEnabled="[bool]True" Value="[int]1002" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]WAVEFORM_VOLTAGE" IsEnabled="[bool]True" Value="[int]1003" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]WAVEFORM_CURRENT" IsEnabled="[bool]True" Value="[int]1004" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]CAPACITANCE" IsEnabled="[bool]True" Value="[int]1005" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]INDUCTANCE" IsEnabled="[bool]True" Value="[int]1006" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
			</ChannelEnumSelector>
			<Label Height="[float]16" Id="d1f28964d0af4b10835729f4ec94466e" LabelOwner="[UIModel]b97cd7939a794245b11a90b37c297997" Left="[float]23" Text="[string]Measurement type" Top="[float]63" Width="[float]99" xmlns="http://www.ni.com/PanelCommon" />
		</ScreenSurface>
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidmm_measurement/NIDmmMeasurement.pinmap sha256=7a7bedc1fa3c4e0e3417663c8d28f274eee19d3803a1af9b6e1ac87544342ef4 bytes=497 -->
## FILE: examples/nidmm_measurement/NIDmmMeasurement.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidmm_measurement/NIDmmMeasurement.pinmap`
- sha256: `7a7bedc1fa3c4e0e3417663c8d28f274eee19d3803a1af9b6e1ac87544342ef4`
- bytes: 497

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.1">
	<Instruments>
		<NIDmmInstrument name="DMM1" />
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="DMM1" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidmm_measurement/NIDmmMeasurement.serviceconfig sha256=4eac9ffc285840a94229701247165de026012ff9b53f19e17314bf6c93a8f9f6 bytes=668 -->
## FILE: examples/nidmm_measurement/NIDmmMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidmm_measurement/NIDmmMeasurement.serviceconfig`
- sha256: `4eac9ffc285840a94229701247165de026012ff9b53f19e17314bf6c93a8f9f6`
- bytes: 668

````json
{
  "services": [
    {
      "displayName": "NI-DMM Measurement (Py)",
      "version": "1.0.0",
      "serviceClass": "ni.examples.NIDmmMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "installPath": "install.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in example that performs a measurement using an NI DMM.",
        "ni/service.collection": "NI.Examples",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidmm_measurement/NIDmmMeasurement.sfp sha256=556ea118498ec964074c34dc3bee840b62b424b61fe8b2a7527da2549adcc63e bytes=11631 -->
## FILE: examples/nidmm_measurement/NIDmmMeasurement.sfp

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidmm_measurement/NIDmmMeasurement.sfp`
- sha256: `556ea118498ec964074c34dc3bee840b62b424b61fe8b2a7527da2549adcc63e`
- bytes: 11631

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="D48B0A331BB69DEF82ADE9920FDB9FFA6BECB80F6BAB1A28AC55466B3933F0E1FA39E8D46815E797651C819C544CE4D55883852301588B9A2B09C7A70C5031F9" Timestamp="1D909C6DB1C9A47" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.7.0.2317" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="6.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2317" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="23.0.0.2317" FeatureSetName="UnifiedTask" Name="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" Version="1.0.0.0" />
		<ParsableNamespace AssemblyFileVersion="23.0.0.2317" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2317" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2317" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.2317" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="23.0.0.2317" />
	</SourceModelFeatureSet>
	<UnifiedTask Id="71e714fb199e4eac9ac630d63e786eac" LayoutInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Layout Information&quot;:{&quot;Sections&quot;:[{&quot;Columns Progressive Count&quot;:1,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Columns&quot;:[{&quot;Containers Progressive Count&quot;:1,&quot;Layout Information Index&quot;:0,&quot;Containers&quot;:[{&quot;Container Model Defition&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Container Assignment State&quot;:&quot;Available&quot;,&quot;Container Identifier&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen.task&quot;,&quot;Container Instrument Name&quot;:&quot;NI-DMM Measurement (Py)&quot;,&quot;Layout Information Name&quot;:&quot;NI-DMM Measurement (Py) 1&quot;,&quot;Layout Information Index&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Items&quot;:[{&quot;Identification Number&quot;:4294963201,&quot;Model Definition Type&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Parent Or Group Name&quot;:&quot;Measurements&quot;,&quot;Panel Type&quot;:&quot;NI-DMM Measurement (Py)&quot;,&quot;Layout Information Name&quot;:&quot;ni.examples.NIDmmMeasurement_Python&quot;,&quot;Layout Information Index&quot;:0}]}]}]},{&quot;Columns Progressive Count&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationOnly&quot;}]}}" PinAwareInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Selected Sites&quot;:[{&quot;Site Number&quot;:0}]}" xmlns="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" />
	<EnvoyManagerFile Id="39f1f22746e848bba57a105f24ffb630" xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="fd6a63646a49441397168a07c9d77ba2" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<NameScopingEnvoy AutomaticallyResolveUp="True" Id="596109ca19934794899596939c6f4686" Name="NIDmmMeasurement.sfp" NameTracksFileName="True" />
		<EmbeddedDefinitionReference Id="f35ddf8c9c204f23b0186f7bc0fbe81e" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="{http\://www.ni.com/InstrumentFramework/ScreenDocument}Screen.task">
			<Screen ClientId="{6d0ab410-b553-474b-9904-d836adc3e499}" ConfigurationParameters="{&quot;@type&quot;:&quot;type.googleapis.com/ni.measurementlink.measurement.v1.MeasurementConfigurations&quot;,&quot;pinName&quot;:&quot;Pin1&quot;,&quot;measurementType&quot;:&quot;DC Volts&quot;,&quot;range&quot;:10.0,&quot;resolutionDigits&quot;:5.5}" DisplayName="NI-DMM Measurement (Py)" Id="5f35a5a563e04c16b5a919b37115e77a" PanelPresentation="ConfigurationWithVisualization" ServiceClass="ni.examples.NIDmmMeasurement_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
				<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]310" Id="9b61037be31b4d789c208aa80a91f097" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]410" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
					<ChannelStringControl AcceptsReturn="[bool]False" BaseName="[string]String" Channel="[string]{6d0ab410-b553-474b-9904-d836adc3e499}/Configuration/measurement_type" Enabled="[bool]True" Height="[float]24" HorizontalScrollBarVisibility="[ScrollBarVisibility]Hidden" Id="547e2686e4d44c7083bd70d1dd6ed92d" IsLabelBoundToChannel="[bool]False" Label="[UIModel]ba7ae61ddc1b44a7bdb8fcffa1fda88d" Left="[float]23" Text="[string]DC Volts" Top="[float]85" VerticalScrollBarVisibility="[ScrollBarVisibility]Auto" Width="[float]72" />
					<Label Height="[float]16" Id="ba7ae61ddc1b44a7bdb8fcffa1fda88d" LabelOwner="[UIModel]547e2686e4d44c7083bd70d1dd6ed92d" Left="[float]23" Text="[string]Measurement type" Top="[float]65" Width="[float]99" xmlns="http://www.ni.com/PanelCommon" />
					<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BaseName="[string]Canvas" Height="[float]143" Id="af577d341fa04b8fb14f068e7c00208b" Label="[UIModel]ae250636782040e5a8f0350529d47fd5" Left="[float]23" Top="[float]140" Width="[float]127">
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{6d0ab410-b553-474b-9904-d836adc3e499}/Configuration/range" Enabled="[bool]True" Height="[float]24" Id="d3f575a56b4b416d884dd2b1fc9166e8" IsLabelBoundToChannel="[bool]False" Label="[UIModel]3ccb357e98f544f484e23c622c0771ea" Left="[float]15" RadixBase="[RadixBase]0" RadixVisibility="[SMVisibility]Collapsed" Top="[float]36" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=SystemInternational:Digits=2:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
						<Label Height="[float]16" Id="3ccb357e98f544f484e23c622c0771ea" LabelOwner="[UIModel]d3f575a56b4b416d884dd2b1fc9166e8" Left="[float]15" Text="[string]Range" Top="[float]16" Width="[float]33" xmlns="http://www.ni.com/PanelCommon" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{6d0ab410-b553-474b-9904-d836adc3e499}/Configuration/resolution_digits" Enabled="[bool]True" Height="[float]24" Id="d40402c881434bbda8be128cde735720" IsLabelBoundToChannel="[bool]False" Label="[UIModel]eb238a18bfe44f8b9df4f90ac1baf109" Left="[float]15" Top="[float]96" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=1:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
						<Label Height="[float]16" Id="eb238a18bfe44f8b9df4f90ac1baf109" LabelOwner="[UIModel]d40402c881434bbda8be128cde735720" Left="[float]15" Text="[string]Resolution (digits)" Top="[float]76" Width="[float]95" xmlns="http://www.ni.com/PanelCommon" />
					</ScreenSurfaceCanvas>
					<Label Height="[float]16" Id="ae250636782040e5a8f0350529d47fd5" LabelOwner="[UIModel]af577d341fa04b8fb14f068e7c00208b" Left="[float]23" Text="[string]Configuration" Top="[float]120" Width="[float]73" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{6d0ab410-b553-474b-9904-d836adc3e499}/Output/measured_value" Height="[float]51" Id="de25957eb914ef08dcc26a7a379bfb7" IsLabelBoundToChannel="[bool]False" IsReadOnly="[bool]True" Label="[UIModel]44197c7d5da248baad059df1fb6463fc" Left="[float]195" MinHeight="[float]51" Top="[float]30" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=6:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]185">
						<FontSetting FontFamily="Segoe UI" FontSize="24" Id="1698925e3f6a4c04a65c79cd4f3b8cd3" xmlns="http://www.ni.com/PlatformFramework" />
					</ChannelNumericText>
					<Label Height="[float]16" Id="44197c7d5da248baad059df1fb6463fc" LabelOwner="[UIModel]de25957eb914ef08dcc26a7a379bfb7" Left="[float]195" Text="[string]Measured value" Top="[float]10" Width="[float]84" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelLED BaseName="[string]Round LED" Channel="[string]{6d0ab410-b553-474b-9904-d836adc3e499}/Output/signal_out_of_range" ContentVisibility="[Visibility]Collapsed" FalseBackground="[SMSolidColorBrush]#ff007133" FalseContent="[string]Off" Height="[float]30" Id="5ea2a61e958e4bbcb4f277ca96c176b7" IsLabelBoundToChannel="[bool]False" IsReadOnly="[bool]True" Label="[UIModel]977b4f391e6e44479a1826eb7d6ddc6a" Left="[float]195" MinHeight="[float]20" MinWidth="[float]20" Shape="[LEDShape]Round" Top="[float]115" TrueBackground="[SMSolidColorBrush]#ff83ca9d" TrueContent="[string]On" Width="[float]30" />
					<Label Height="[float]16" Id="977b4f391e6e44479a1826eb7d6ddc6a" LabelOwner="[UIModel]5ea2a61e958e4bbcb4f277ca96c176b7" Left="[float]195" Text="[string]Signal out of range" Top="[float]95" Width="[float]101" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{6d0ab410-b553-474b-9904-d836adc3e499}/Output/absolute_resolution" Height="[float]24" Id="dacf90ede3c84d56b0b045d163190e07" IsLabelBoundToChannel="[bool]False" IsReadOnly="[bool]True" Label="[UIModel]4f27dad8555e463592bfbebb26936f29" Left="[float]195" RadixBase="[RadixBase]0" RadixVisibility="[SMVisibility]Collapsed" Top="[float]183" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=SystemInternational:Digits=3:DigitDisplayType=SignificantDigits:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
					<Label Height="[float]16" Id="4f27dad8555e463592bfbebb26936f29" LabelOwner="[UIModel]dacf90ede3c84d56b0b045d163190e07" Left="[float]195" Text="[string]Absolute resolution" Top="[float]163" Width="[float]103" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{6d0ab410-b553-474b-9904-d836adc3e499}/Configuration/pin_name" DataType="[Type]String" Height="[float]24" Id="18efb4e37edb44e49873751a77b84085" IsLabelBoundToChannel="[bool]False" Label="[UIModel]99dbea3b3ebc44759e242a213f2688f0" Left="[float]23" SelectedResource="[NI_Core_DataValues_TagRefnum]Pin1" Top="[float]30" Width="[float]127" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
					<Label Height="[float]16" Id="99dbea3b3ebc44759e242a213f2688f0" LabelOwner="[UIModel]18efb4e37edb44e49873751a77b84085" Left="[float]23" Text="[string]Pin name" Top="[float]10" Width="[float]49" xmlns="http://www.ni.com/PanelCommon" />
				</ScreenSurface>
			</Screen>
		</EmbeddedDefinitionReference>
	</EnvoyManagerFile>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidmm_measurement/NIDmmMeasurement_example.seq sha256=4e2c701eae9a0bb714e6efa2beadf89381ab35d9f88566048ea6dd6cc5b36035 bytes=182863 -->
## FILE: examples/nidmm_measurement/NIDmmMeasurement_example.seq

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidmm_measurement/NIDmmMeasurement_example.seq`
- sha256: `4e2c701eae9a0bb714e6efa2beadf89381ab35d9f88566048ea6dd6cc5b36035`
- bytes: 182863

````text
<?xml version="1.0" encoding="UTF-8"?>
<teststandfileheader type='SequenceFile' fileversion='962' productname='TestStand' productversion='2021 SP1 (21.1.0.49154)' compatibleversion='21.0.0.0' buildversion='21.0.0.49156' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.ni.com/TestStand/21.0.0/SequenceFile">
	<typelist>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='1'>
			<Expression classname='ExprValue' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<value/>
			</Expression>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='2'>
			<StepTypeMenu classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='24'>
				<subprops>
					<CanBeSubstepType classname='Bool'>
						<value>false</value>
					</CanBeSubstepType>
					<CanOnlyBeSubstepType classname='Bool'>
						<value>false</value>
					</CanOnlyBeSubstepType>
					<Category classname='Str'>
						<value>""</value>
					</Category>
					<ItemName typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value>""</value>
					</ItemName>
					<SingularItemName classname='Str'>
						<value>""</value>
					</SingularItemName>
					<SeparatorBeforeCategory classname='Bool'>
						<value>false</value>
					</SeparatorBeforeCategory>
					<SeparatorBeforeItemName classname='Bool'>
						<value>false</value>
					</SeparatorBeforeItemName>
					<Group classname='Str'>
						<value/>
					</Group>
				</subprops>
			</StepTypeMenu>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='3'>
			<StepTypeSubstepsArray classname='Objs' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4718616' instanceoverrideflags='4849688' valueflags='24'>
				<value lbound='[0]' ubound='[]'/>
			</StepTypeSubstepsArray>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='4'>
			<NI_ArrayDimensions classname='ArrayDimensions' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<LowerBounds classname='Nums'>
						<value lbound='[0]' ubound='[]'/>
					</LowerBounds>
					<UpperBounds classname='Nums'>
						<value lbound='[0]' ubound='[]'/>
					</UpperBounds>
				</subprops>
			</NI_ArrayDimensions>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='5'>
			<NI_PropertyObjectType classname='PropertyObjectType' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<ValueType classname='Num'>
						<value>3</value>
					</ValueType>
					<IsObject classname='Bool'>
						<value>true</value>
					</IsObject>
					<TypeName classname='Str'>
						<value/>
					</TypeName>
					<ElementType classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</ElementType>
					<ArrayDimensions typename='NI_ArrayDimensions' xsi:type='NI_ArrayDimensions' classname='ArrayDimensions'>
						<subprops>
							<LowerBounds classname='Nums'>
								<value lbound='[0]' ubound='[]'/>
							</LowerBounds>
							<UpperBounds classname='Nums'>
								<value lbound='[0]' ubound='[]'/>
							</UpperBounds>
						</subprops>
					</ArrayDimensions>
					<Representation classname='Num'>
						<value>1</value>
					</Representation>
					<ClassName classname='Str'>
						<value/>
					</ClassName>
				</subprops>
			</NI_PropertyObjectType>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='6'>
			<NI_CustomResult classname='CustomResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Name>
					<ValueToLog typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ValueToLog>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>2</value>
					</CheckedState>
					<Type typename='NI_PropertyObjectType' xsi:type='NI_PropertyObjectType' classname='PropertyObjectType'>
						<subprops>
							<ValueType classname='Num'>
								<value>3</value>
							</ValueType>
							<IsObject classname='Bool'>
								<value>true</value>
							</IsObject>
							<TypeName classname='Str'>
								<value/>
							</TypeName>
							<ElementType classname='Objs'>
								<value lbound='[0]' ubound='[]'/>
							</ElementType>
							<ArrayDimensions classname='ArrayDimensions'>
								<subprops>
									<LowerBounds classname='Nums'>
										<value lbound='[0]' ubound='[]'/>
									</LowerBounds>
									<UpperBounds classname='Nums'>
										<value lbound='[0]' ubound='[]'/>
									</UpperBounds>
								</subprops>
							</ArrayDimensions>
							<Representation classname='Num'>
								<value>1</value>
							</Representation>
							<ClassName classname='Str'>
								<value/>
							</ClassName>
						</subprops>
					</Type>
					<Elements classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</Elements>
					<IsAnyType classname='Bool'>
						<value>true</value>
					</IsAnyType>
				</subprops>
			</NI_CustomResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='7'>
			<TEInf classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4456472' instanceoverrideflags='4456472' valueflags='24'>
				<subprops>
					<Id classname='Str' flagsforinstances='1' instanceoverrideflags='5046297'>
						<value/>
					</Id>
					<Icon classname='Str' instanceoverrideflags='5046296'>
						<value/>
					</Icon>
					<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7143448' structureflags='2097152'/>
					<PreCond typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PreCond>
					<LoadOpt classname='Str' instanceoverrideflags='5046296'>
						<value>PreloadWhenExecuted</value>
					</LoadOpt>
					<UnloadOpt classname='Str' instanceoverrideflags='5046296'>
						<value>UnloadWithFile</value>
					</UnloadOpt>
					<Mode classname='Str' instanceoverrideflags='5046296'>
						<value>Normal</value>
					</Mode>
					<WindowActivation classname='Str' instanceoverrideflags='5046296'>
						<value>None</value>
					</WindowActivation>
					<ResultOption classname='Num' instanceoverrideflags='5046296'>
						<value>1</value>
					</ResultOption>
					<StepFCSeqF classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</StepFCSeqF>
					<IgnoreRTE classname='Bool' instanceoverrideflags='5046296'>
						<value>false</value>
					</IgnoreRTE>
					<UseMutex classname='Bool' instanceoverrideflags='5046296'>
						<value>false</value>
					</UseMutex>
					<MutexNameOrRef typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</MutexNameOrRef>
					<BatchSyncOpt classname='Num' instanceoverrideflags='5046296'>
						<value>0</value>
					</BatchSyncOpt>
					<SwitchEnabled classname='Bool' instanceoverrideflags='5046296'>
						<value>false</value>
					</SwitchEnabled>
					<VirtualDeviceName typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</VirtualDeviceName>
					<SwitchOperation classname='Num' instanceoverrideflags='5046296'>
						<value>1</value>
					</SwitchOperation>
					<RouteGroupConnect typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</RouteGroupConnect>
					<RouteGroupDisconnect typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</RouteGroupDisconnect>
					<MulticonnectMode classname='Num' instanceoverrideflags='5046296'>
						<value>1</value>
					</MulticonnectMode>
					<OperationOrder classname='Num' instanceoverrideflags='5046296'>
						<value>2</value>
					</OperationOrder>
					<ConnectionLifetime classname='Num' instanceoverrideflags='5046296'>
						<value>4</value>
					</ConnectionLifetime>
					<WaitForDebounce classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</WaitForDebounce>
					<PassAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</PassAct>
					<FailAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</FailAct>
					<PassActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PassActTarget>
					<FailActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</FailActTarget>
					<CustExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</CustExpr>
					<CustTrueAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</CustTrueAct>
					<CustFalseAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</CustFalseAct>
					<CustTrueActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</CustTrueActTarget>
					<CustFalseActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</CustFalseActTarget>
					<LoopType classname='Str' instanceoverrideflags='5046296'>
						<value>NoLooping</value>
					</LoopType>
					<LoopWhile typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</LoopWhile>
					<LoopStatus typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</LoopStatus>
					<LoopIncrement typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value>RunState.LoopIndex += 1</value>
					</LoopIncrement>
					<LoopInitialize typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value>RunState.LoopIndex = 0</value>
					</LoopInitialize>
					<LoopOpt classname='Num' instanceoverrideflags='5046296'>
						<value>0</value>
					</LoopOpt>
					<PreExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PreExpr>
					<PostExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PostExpr>
					<StatusExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</StatusExpr>
					<CanSpecifyModule classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanSpecifyModule>
					<CanEditCode classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanEditCode>
					<CanEditModulePrototype classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanEditModulePrototype>
					<CanEditParameterAdditionalResults classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanEditParameterAdditionalResults>
					<PrecondIntExe classname='Num' instanceoverrideflags='5046296'>
						<value>0</value>
					</PrecondIntExe>
					<Requirements classname='Obj' flagsforinstances='2097153' instanceoverrideflags='7143449' valueflags='1' structureflags='2097152'>
						<subprops>
							<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
								<value lbound='[0]' ubound='[]'/>
							</Links>
						</subprops>
					</Requirements>
					<CustomResults classname='Objs' instanceoverrideflags='5046296'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</CustomResults>
					<AdditionalResultsHints classname='Objs' instanceoverrideflags='5046296'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
				</subprops>
			</TEInf>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='8'>
			<StepTypeNIData classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='24'>
				<subprops>
					<EditPanels classname='Strs'>
						<value lbound='[0]' ubound='[]'/>
					</EditPanels>
				</subprops>
			</StepTypeNIData>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='9'>
			<Error classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<extdata controllername='STRUCT' allowstructpassing='true' packingoption='8' exclude='false' type='0' arraystorage='0' strbuffersize='256' strstorage='0'/>
				<extdata controllername='CLUST' allowclusterpassing='true' exclude='false' memberlabel=''/>
				<extdata controllername='DNSTRUCT' allowstructpassing='true' exclude='false' membername=''/>
				<extdata controllername='BLVCLUSTER' allowclusterpassing='true' exclude='false' memberlabel=''/>
				<subprops>
					<Code classname='Num' flagsforinstances='4194304' valueflags='4194304'>
						<value>0</value>
						<extdata controllername='STRUCT' allowstructpassing='false' packingoption='0' exclude='false' type='6' arraystorage='0' strbuffersize='256' strstorage='0'/>
						<extdata controllername='CLUST' allowclusterpassing='false' exclude='false' memberlabel='code'/>
						<extdata controllername='DNSTRUCT' allowstructpassing='false' exclude='false' membername='code'/>
						<extdata controllername='BLVCLUSTER' allowclusterpassing='false' exclude='false' memberlabel='code'/>
					</Code>
					<Msg classname='Str' flagsforinstances='4194304' valueflags='4194304'>
						<value/>
						<extdata controllername='STRUCT' allowstructpassing='false' packingoption='0' exclude='false' type='2' arraystorage='0' strbuffersize='1024' strstorage='1'/>
						<extdata controllername='CLUST' allowclusterpassing='false' exclude='false' memberlabel='source'/>
						<extdata controllername='DNSTRUCT' allowstructpassing='false' exclude='false' membername='msg'/>
						<extdata controllername='BLVCLUSTER' allowclusterpassing='false' exclude='false' memberlabel='source'/>
					</Msg>
					<Occurred classname='Bool' flagsforinstances='4194304' valueflags='4194304'>
						<value>false</value>
						<extdata controllername='STRUCT' allowstructpassing='false' packingoption='0' exclude='false' type='6' arraystorage='0' strbuffersize='256' strstorage='0'/>
						<extdata controllername='CLUST' allowclusterpassing='false' exclude='false' memberlabel='status'/>
						<extdata controllername='DNSTRUCT' allowstructpassing='false' exclude='false' membername='occurred'/>
						<extdata controllername='BLVCLUSTER' allowclusterpassing='false' exclude='false' memberlabel='status'/>
					</Occurred>
				</subprops>
			</Error>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='10'>
			<CommonResults classname='Obj' isroottypedef='true' typecategory='3' timestamp='1465572565' typeversion='3.1.0.100' typelastmodversion='21.1.0.49154' typeminprodversion='3.1.0.0' typeflags='33554432' flagsforinstances='4194304' valueflags='4194304'/>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='11'>
			<Substep classname='StepType' isroottypedef='true' typecategory='1' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554438' flagsforinstances='4194304' instanceoverrideflags='4194304'>
				<subprops>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>"%ModuleDescription"</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "GENERIC_DEF_SUBSTEP_NAME")</value>
					</DefaultNameFormat>
					<BlockStartTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockStartTypes>
					<BlockEndTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockEndTypes>
					<AppliesToBlockStructure classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</AppliesToBlockStructure>
					<Menu typename='StepTypeMenu' xsi:type='StepTypeMenu' classname='Obj'>
						<subprops>
							<CanBeSubstepType classname='Bool'>
								<value>true</value>
							</CanBeSubstepType>
							<CanOnlyBeSubstepType classname='Bool'>
								<value>true</value>
							</CanOnlyBeSubstepType>
							<Category classname='Str'>
								<value>""</value>
							</Category>
							<ItemName classname='ExprValue'>
								<value>ResStr("NI_STEPTYPES", "GENERIC_SUBSTEP_MENU_ITEM_NAME")</value>
							</ItemName>
							<SingularItemName classname='Str'>
								<value>""</value>
							</SingularItemName>
							<SeparatorBeforeCategory classname='Bool'>
								<value>false</value>
							</SeparatorBeforeCategory>
							<SeparatorBeforeItemName classname='Bool'>
								<value>false</value>
							</SeparatorBeforeItemName>
							<Group classname='Str'>
								<value>GenericSubsteps</value>
							</Group>
						</subprops>
					</Menu>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</Substeps>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>DefaultLabVIEWNXG|DefaultLabVIEW|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|DefaultHTB80_Template|Default_Template</value>
					</CodeTemplates>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value/>
							</Icon>
							<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7274521' structureflags='2097152'/>
							<PreCond classname='ExprValue'>
								<value/>
							</PreCond>
							<LoadOpt classname='Str'>
								<value>PreloadWhenExecuted</value>
							</LoadOpt>
							<UnloadOpt classname='Str'>
								<value>UnloadWithFile</value>
							</UnloadOpt>
							<Mode classname='Str'>
								<value>Normal</value>
							</Mode>
							<WindowActivation classname='Str'>
								<value>None</value>
							</WindowActivation>
							<ResultOption classname='Num'>
								<value>1</value>
							</ResultOption>
							<StepFCSeqF classname='Bool'>
								<value>true</value>
							</StepFCSeqF>
							<IgnoreRTE classname='Bool'>
								<value>false</value>
							</IgnoreRTE>
							<UseMutex classname='Bool'>
								<value>false</value>
							</UseMutex>
							<MutexNameOrRef classname='ExprValue'>
								<value/>
							</MutexNameOrRef>
							<BatchSyncOpt classname='Num'>
								<value>0</value>
							</BatchSyncOpt>
							<SwitchEnabled classname='Bool'>
								<value>false</value>
							</SwitchEnabled>
							<VirtualDeviceName classname='ExprValue'>
								<value/>
							</VirtualDeviceName>
							<SwitchOperation classname='Num'>
								<value>1</value>
							</SwitchOperation>
							<RouteGroupConnect classname='ExprValue'>
								<value/>
							</RouteGroupConnect>
							<RouteGroupDisconnect classname='ExprValue'>
								<value/>
							</RouteGroupDisconnect>
							<MulticonnectMode classname='Num'>
								<value>1</value>
							</MulticonnectMode>
							<OperationOrder classname='Num'>
								<value>2</value>
							</OperationOrder>
							<ConnectionLifetime classname='Num'>
								<value>4</value>
							</ConnectionLifetime>
							<WaitForDebounce classname='Bool'>
								<value>true</value>
							</WaitForDebounce>
							<PassAct classname='Str'>
								<value>Next</value>
							</PassAct>
							<FailAct classname='Str'>
								<value>Next</value>
							</FailAct>
							<PassActTarget classname='ExprValue'>
								<value/>
							</PassActTarget>
							<FailActTarget classname='ExprValue'>
								<value/>
							</FailActTarget>
							<CustExpr classname='ExprValue'>
								<value/>
							</CustExpr>
							<CustTrueAct classname='Str'>
								<value>Next</value>
							</CustTrueAct>
							<CustFalseAct classname='Str'>
								<value>Next</value>
							</CustFalseAct>
							<CustTrueActTarget classname='ExprValue'>
								<value/>
							</CustTrueActTarget>
							<CustFalseActTarget classname='ExprValue'>
								<value/>
							</CustFalseActTarget>
							<LoopType classname='Str'>
								<value>NoLooping</value>
							</LoopType>
							<LoopWhile classname='ExprValue'>
								<value/>
							</LoopWhile>
							<LoopStatus classname='ExprValue'>
								<value/>
							</LoopStatus>
							<LoopIncrement classname='ExprValue'>
								<value>RunState.LoopIndex += 1</value>
							</LoopIncrement>
							<LoopInitialize classname='ExprValue'>
								<value>RunState.LoopIndex = 0</value>
							</LoopInitialize>
							<LoopOpt classname='Num'>
								<value>0</value>
							</LoopOpt>
							<PreExpr classname='ExprValue'>
								<value/>
							</PreExpr>
							<PostExpr classname='ExprValue'>
								<value/>
							</PostExpr>
							<StatusExpr classname='ExprValue'>
								<value/>
							</StatusExpr>
							<CanSpecifyModule classname='Bool'>
								<value>true</value>
							</CanSpecifyModule>
							<CanEditCode classname='Bool'>
								<value>true</value>
							</CanEditCode>
							<CanEditModulePrototype classname='Bool'>
								<value>true</value>
							</CanEditModulePrototype>
							<CanEditParameterAdditionalResults classname='Bool'>
								<value>true</value>
							</CanEditParameterAdditionalResults>
							<PrecondIntExe classname='Num'>
								<value>0</value>
							</PrecondIntExe>
							<Requirements classname='Obj' flagsforinstances='1' valueflags='1' structureflags='2097152'>
								<subprops>
									<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
										<value lbound='[0]' ubound='[]'/>
									</Links>
								</subprops>
							</Requirements>
							<CustomResults classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</CustomResults>
							<AdditionalResultsHints classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</AdditionalResultsHints>
						</subprops>
					</TS>
					<NI_Data typename='StepTypeNIData' xsi:type='StepTypeNIData' classname='Obj'>
						<subprops>
							<EditPanels classname='Strs'>
								<value lbound='[0]' ubound='[]'/>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
						<subprops>
							<Error typename='Error' xsi:type='Error' classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
								<subprops>
									<Code classname='Num'>
										<value>0</value>
									</Code>
									<Msg classname='Str'>
										<value/>
									</Msg>
									<Occurred classname='Bool'>
										<value>false</value>
									</Occurred>
								</subprops>
							</Error>
							<Status classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</Status>
							<ReportText classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</ReportText>
							<Common typename='CommonResults' xsi:type='CommonResults' classname='Obj'/>
						</subprops>
					</Result>
					<CanEncapsulate classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</CanEncapsulate>
				</subprops>
			</Substep>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='12'>
			<NI_DotNetParameterResult classname='DotNetParameterResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>1</value>
					</CheckedState>
				</subprops>
			</NI_DotNetParameterResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='13'>
			<DotNetParameter classname='DotNetParameter' isroottypedef='true' typecategory='3' timestamp='1650061192' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name classname='Str'>
						<value>_notNamed</value>
					</Name>
					<ArgVal typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgVal>
					<ArgDisplayVal typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgDisplayVal>
					<Type classname='Num'>
						<value>0</value>
					</Type>
					<TypeName classname='Str'>
						<value/>
					</TypeName>
					<Flags classname='Num'>
						<value>0</value>
					</Flags>
					<IsOptional classname='Bool'>
						<value>false</value>
					</IsOptional>
					<CallDispose classname='Bool'>
						<value>false</value>
					</CallDispose>
					<NumDimensions classname='Nums'>
						<value lbound='[0]' ubound='[]'/>
					</NumDimensions>
					<MultiElement classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</MultiElement>
					<AdditionalResults classname='Obj'>
						<subprops>
							<Input typename='NI_DotNetParameterResult' xsi:type='NI_DotNetParameterResult' classname='DotNetParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Input>
							<Output typename='NI_DotNetParameterResult' xsi:type='NI_DotNetParameterResult' classname='DotNetParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Output>
						</subprops>
					</AdditionalResults>
					<UserData classname='Obj' flagsforinstances='2097152' structureflags='2097152'/>
				</subprops>
			</DotNetParameter>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='14'>
			<NI_DotNetCallResult classname='DotNetCallResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>1</value>
					</CheckedState>
				</subprops>
			</NI_DotNetCallResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='15'>
			<DotNetCall classname='DotNetCall' isroottypedef='true' typecategory='3' timestamp='1650061192' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<ClassName classname='Str'>
						<value/>
					</ClassName>
					<MemberType classname='Num'>
						<value>0</value>
					</MemberType>
					<Static classname='Bool'>
						<value>false</value>
					</Static>
					<MemberName classname='Str'>
						<value/>
					</MemberName>
					<Params classname='Objs'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='DotNetParameter' xsi:type='DotNetParameter' name='' classname='DotNetParameter' structureflags='131072'>
									<subprops>
										<Name classname='Str'>
											<value>_notNamed</value>
										</Name>
										<ArgVal classname='ExprValue'>
											<value/>
										</ArgVal>
										<ArgDisplayVal classname='ExprValue'>
											<value/>
										</ArgDisplayVal>
										<Type classname='Num'>
											<value>0</value>
										</Type>
										<TypeName classname='Str'>
											<value/>
										</TypeName>
										<Flags classname='Num'>
											<value>0</value>
										</Flags>
										<IsOptional classname='Bool'>
											<value>false</value>
										</IsOptional>
										<CallDispose classname='Bool'>
											<value>false</value>
										</CallDispose>
										<NumDimensions classname='Nums'>
											<value lbound='[0]' ubound='[]'/>
										</NumDimensions>
										<MultiElement classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</MultiElement>
										<AdditionalResults classname='Obj'>
											<subprops>
												<Input classname='DotNetParameterResult'>
													<subprops>
														<Condition classname='ExprValue'>
															<value/>
														</Condition>
														<Flags classname='Num'>
															<value>8192</value>
														</Flags>
														<CheckedState classname='Num'>
															<value>1</value>
														</CheckedState>
													</subprops>
												</Input>
												<Output classname='DotNetParameterResult'>
													<subprops>
														<Condition classname='ExprValue'>
															<value/>
														</Condition>
														<Flags classname='Num'>
															<value>8192</value>
														</Flags>
														<CheckedState classname='Num'>
															<value>1</value>
														</CheckedState>
													</subprops>
												</Output>
											</subprops>
										</AdditionalResults>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</Params>
					<AdditionalResult typename='NI_DotNetCallResult' xsi:type='NI_DotNetCallResult' classname='DotNetCallResult'>
						<subprops>
							<Condition classname='ExprValue'>
								<value/>
							</Condition>
							<Flags classname='Num'>
								<value>8192</value>
							</Flags>
							<CheckedState classname='Num'>
								<value>1</value>
							</CheckedState>
						</subprops>
					</AdditionalResult>
				</subprops>
			</DotNetCall>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='0'>
			<Path classname='PathValue' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<value/>
			</Path>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='16'>
			<DotNetStepAdditions classname='DotNetModule' isroottypedef='true' typecategory='3' timestamp='1650061192' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Calls classname='Objs'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='DotNetCall' xsi:type='DotNetCall' name='' classname='DotNetCall' structureflags='131072'>
									<subprops>
										<ClassName classname='Str'>
											<value/>
										</ClassName>
										<MemberType classname='Num'>
											<value>0</value>
										</MemberType>
										<Static classname='Bool'>
											<value>false</value>
										</Static>
										<MemberName classname='Str'>
											<value/>
										</MemberName>
										<Params classname='Objs'>
											<value lbound='[0]' ubound='[]'>
												<elemproto>
													<_NAME_IN_ATTRIBUTE_ name='' classname='DotNetParameter' structureflags='0'/>
												</elemproto>
											</value>
										</Params>
										<AdditionalResult classname='DotNetCallResult'>
											<subprops>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>1</value>
												</CheckedState>
											</subprops>
										</AdditionalResult>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</Calls>
					<AssemblyPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</AssemblyPath>
					<AssemblyStrongName classname='Str'>
						<value/>
					</AssemblyStrongName>
					<AssemblyLocation classname='Num'>
						<value>0</value>
					</AssemblyLocation>
					<ClassName classname='Str'>
						<value/>
					</ClassName>
					<IsStruct classname='Bool'>
						<value>false</value>
					</IsStruct>
					<StructDef typename='DotNetParameter' xsi:type='DotNetParameter' classname='DotNetParameter'>
						<subprops>
							<Name classname='Str'>
								<value>_notNamed</value>
							</Name>
							<ArgVal classname='ExprValue'>
								<value/>
							</ArgVal>
							<ArgDisplayVal classname='ExprValue'>
								<value/>
							</ArgDisplayVal>
							<Type classname='Num'>
								<value>0</value>
							</Type>
							<TypeName classname='Str'>
								<value/>
							</TypeName>
							<Flags classname='Num'>
								<value>0</value>
							</Flags>
							<IsOptional classname='Bool'>
								<value>false</value>
							</IsOptional>
							<CallDispose classname='Bool'>
								<value>false</value>
							</CallDispose>
							<NumDimensions classname='Nums'>
								<value lbound='[0]' ubound='[]'/>
							</NumDimensions>
							<MultiElement classname='Objs'>
								<value lbound='[0]' ubound='[]'/>
							</MultiElement>
							<AdditionalResults classname='Obj'>
								<subprops>
									<Input classname='DotNetParameterResult'>
										<subprops>
											<Condition classname='ExprValue'>
												<value/>
											</Condition>
											<Flags classname='Num'>
												<value>8192</value>
											</Flags>
											<CheckedState classname='Num'>
												<value>1</value>
											</CheckedState>
										</subprops>
									</Input>
									<Output classname='DotNetParameterResult'>
										<subprops>
											<Condition classname='ExprValue'>
												<value/>
											</Condition>
											<Flags classname='Num'>
												<value>8192</value>
											</Flags>
											<CheckedState classname='Num'>
												<value>1</value>
											</CheckedState>
										</subprops>
									</Output>
								</subprops>
							</AdditionalResults>
						</subprops>
					</StructDef>
					<RemoteSpecifiedByExpr classname='Bool'>
						<value>false</value>
					</RemoteSpecifiedByExpr>
					<UseLoadSpec classname='Bool'>
						<value>false</value>
					</UseLoadSpec>
					<ModuleSrcPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModuleSrcPath>
					<ModulePrjPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModulePrjPath>
					<ModuleSlnPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModuleSlnPath>
					<FunctionName classname='Str'>
						<value/>
					</FunctionName>
				</subprops>
			</DotNetStepAdditions>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='17'>
			<PostSubstep classname='StepType' isroottypedef='true' typecategory='1' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554438' flagsforinstances='4194304' instanceoverrideflags='4194304'>
				<subprops>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>"%ModuleDescription"</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "POST_DEF_SUBSTEP_NAME")</value>
					</DefaultNameFormat>
					<BlockStartTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockStartTypes>
					<BlockEndTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockEndTypes>
					<AppliesToBlockStructure classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</AppliesToBlockStructure>
					<Menu typename='StepTypeMenu' xsi:type='StepTypeMenu' classname='Obj'>
						<subprops>
							<CanBeSubstepType classname='Bool'>
								<value>true</value>
							</CanBeSubstepType>
							<CanOnlyBeSubstepType classname='Bool'>
								<value>true</value>
							</CanOnlyBeSubstepType>
							<Category classname='Str'>
								<value>""</value>
							</Category>
							<ItemName classname='ExprValue'>
								<value>ResStr("NI_STEPTYPES", "POST_SUBSTEP_MENU_ITEM_NAME")</value>
							</ItemName>
							<SingularItemName classname='Str'>
								<value>""</value>
							</SingularItemName>
							<SeparatorBeforeCategory classname='Bool'>
								<value>false</value>
							</SeparatorBeforeCategory>
							<SeparatorBeforeItemName classname='Bool'>
								<value>false</value>
							</SeparatorBeforeItemName>
							<Group classname='Str'>
								<value>ExecSubsteps</value>
							</Group>
						</subprops>
					</Menu>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</Substeps>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>DefaultLabVIEWNXG|DefaultLabVIEW|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|DefaultHTB80_Template|Default_Template</value>
					</CodeTemplates>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value/>
							</Icon>
							<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7274521' structureflags='2097152'/>
							<PreCond classname='ExprValue'>
								<value/>
							</PreCond>
							<LoadOpt classname='Str'>
								<value>PreloadWhenExecuted</value>
							</LoadOpt>
							<UnloadOpt classname='Str'>
								<value>UnloadWithFile</value>
							</UnloadOpt>
							<Mode classname='Str'>
								<value>Normal</value>
							</Mode>
							<WindowActivation classname='Str'>
								<value>None</value>
							</WindowActivation>
							<ResultOption classname='Num'>
								<value>1</value>
							</ResultOption>
							<StepFCSeqF classname='Bool'>
								<value>true</value>
							</StepFCSeqF>
							<IgnoreRTE classname='Bool'>
								<value>false</value>
							</IgnoreRTE>
							<UseMutex classname='Bool'>
								<value>false</value>
							</UseMutex>
							<MutexNameOrRef classname='ExprValue'>
								<value/>
							</MutexNameOrRef>
							<BatchSyncOpt classname='Num'>
								<value>0</value>
							</BatchSyncOpt>
							<SwitchEnabled classname='Bool'>
								<value>false</value>
							</SwitchEnabled>
							<VirtualDeviceName classname='ExprValue'>
								<value/>
							</VirtualDeviceName>
							<SwitchOperation classname='Num'>
								<value>1</value>
							</SwitchOperation>
							<RouteGroupConnect classname='ExprValue'>
								<value/>
							</RouteGroupConnect>
							<RouteGroupDisconnect classname='ExprValue'>
								<value/>
							</RouteGroupDisconnect>
							<MulticonnectMode classname='Num'>
								<value>1</value>
							</MulticonnectMode>
							<OperationOrder classname='Num'>
								<value>2</value>
							</OperationOrder>
							<ConnectionLifetime classname='Num'>
								<value>4</value>
							</ConnectionLifetime>
							<WaitForDebounce classname='Bool'>
								<value>true</value>
							</WaitForDebounce>
							<PassAct classname='Str'>
								<value>Next</value>
							</PassAct>
							<FailAct classname='Str'>
								<value>Next</value>
							</FailAct>
							<PassActTarget classname='ExprValue'>
								<value/>
							</PassActTarget>
							<FailActTarget classname='ExprValue'>
								<value/>
							</FailActTarget>
							<CustExpr classname='ExprValue'>
								<value/>
							</CustExpr>
							<CustTrueAct classname='Str'>
								<value>Next</value>
							</CustTrueAct>
							<CustFalseAct classname='Str'>
								<value>Next</value>
							</CustFalseAct>
							<CustTrueActTarget classname='ExprValue'>
								<value/>
							</CustTrueActTarget>
							<CustFalseActTarget classname='ExprValue'>
								<value/>
							</CustFalseActTarget>
							<LoopType classname='Str'>
								<value>NoLooping</value>
							</LoopType>
							<LoopWhile classname='ExprValue'>
								<value/>
							</LoopWhile>
							<LoopStatus classname='ExprValue'>
								<value/>
							</LoopStatus>
							<LoopIncrement classname='ExprValue'>
								<value>RunState.LoopIndex += 1</value>
							</LoopIncrement>
							<LoopInitialize classname='ExprValue'>
								<value>RunState.LoopIndex = 0</value>
							</LoopInitialize>
							<LoopOpt classname='Num'>
								<value>0</value>
							</LoopOpt>
							<PreExpr classname='ExprValue'>
								<value/>
							</PreExpr>
							<PostExpr classname='ExprValue'>
								<value/>
							</PostExpr>
							<StatusExpr classname='ExprValue'>
								<value/>
							</StatusExpr>
							<CanSpecifyModule classname='Bool'>
								<value>true</value>
							</CanSpecifyModule>
							<CanEditCode classname='Bool'>
								<value>true</value>
							</CanEditCode>
							<CanEditModulePrototype classname='Bool'>
								<value>true</value>
							</CanEditModulePrototype>
							<CanEditParameterAdditionalResults classname='Bool'>
								<value>true</value>
							</CanEditParameterAdditionalResults>
							<PrecondIntExe classname='Num'>
								<value>0</value>
							</PrecondIntExe>
							<Requirements classname='Obj' flagsforinstances='1' valueflags='1' structureflags='2097152'>
								<subprops>
									<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
										<value lbound='[0]' ubound='[]'/>
									</Links>
								</subprops>
							</Requirements>
							<CustomResults classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</CustomResults>
							<AdditionalResultsHints classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</AdditionalResultsHints>
						</subprops>
					</TS>
					<NI_Data typename='StepTypeNIData' xsi:type='StepTypeNIData' classname='Obj'>
						<subprops>
							<EditPanels classname='Strs'>
								<value lbound='[0]' ubound='[]'/>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
						<subprops>
							<Error typename='Error' xsi:type='Error' classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
								<subprops>
									<Code classname='Num'>
										<value>0</value>
									</Code>
									<Msg classname='Str'>
										<value/>
									</Msg>
									<Occurred classname='Bool'>
										<value>false</value>
									</Occurred>
								</subprops>
							</Error>
							<Status classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</Status>
							<ReportText classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</ReportText>
							<Common typename='CommonResults' xsi:type='CommonResults' classname='Obj'/>
						</subprops>
					</Result>
					<CanEncapsulate classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</CanEncapsulate>
				</subprops>
			</PostSubstep>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='18'>
			<NoneStepAdditions classname='NoneModule' isroottypedef='true' typecategory='3' timestamp='1650060850' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'/>
		</typedef>
		<protected>E@=3HJL4100hYLEDF=_K@0@mKCYo_1KN2&lt;dfASB`]CF^aUXa]Y\4WmD]203VfR;kS;KgdGgF285WU]RaSJgcjNlM7MFC4LiX=a48\7dW:L403mZ4BUAT82I&gt;KQH8\T8QFE`DA2\LAVbMD5YRMT13fTiE^i&lt;boIle7[=C_LeZbKM2QXhVTH;?4hTX]A[17:2T;Dh\^Co3kY9PA5QK23^C]l262h09La1?5^k3J0BQZ@@EeDRZTO=\cKd?XKjmGb1N\X&lt;J[IS9OXJj22Qc=R\WEEn\IKCaHCAUNi97;EVjaJCX4&gt;UU36B3oib::mkjjIJFOY^^C_gK;?Ngamc6b1^HOM^Rl@oHoiaG802US0o36;lHiif[]oe&lt;FRliGlo^CMk69OeFDNDnIQUXNS=iA3JmW&lt;KbcFOCL6bWF;DdY7d2\SSH4mB7[^9gAb5EgM5G;l^DR5mXURj&lt;_=4b_aTDS965fd7ACLdkeA7kamDL&gt;;lWi[PA07_B@&gt;cR[mGK`_XMGdK4NmjkVR8?micjQcMS=oX^9@cW^5\93S[[2ZkFbBiZ=Q@AM0FkKdo:gUd&lt;lVVcfi&gt;bV3&gt;kl[1UR_FW&gt;JkW]_EREPX34oO2LYb;J&gt;k9nWLWBEg6Tk&gt;koggGTQ&gt;kL6kJL@dKQ2_E0Z</protected>
		<protected>E@=3HJB4110h]L]MDk_K3gBocK7LAg@bF0m7:L\7mUH^jTPf8UWji4?JObL37e`G1BU_]bJEEgG9OLd39Oi??^9QJSUTD=2428\B0kcT_7T&lt;Q@obH[[G3o^A&lt;D=J_&gt;g1Hi&lt;R`WmR7Y7K&gt;c7;g@f3WI&gt;MaH=lc7S9&gt;c?IG77K\]]6niUiBAL4CCDj_[5AJfWeomR_OoKJmJZM?&lt;_&gt;RAC]I2d0NnLHDh&gt;Dli&gt;23CM5CXi6DO^g`LX&lt;Q2hSHndMR7[D8BMh8aJ7oQSA@fKWPh;Dm5&gt;RW9o]Rgj]F^W_JkHFKk?2&gt;8;5iifgAJkk=k]f8VDCi5;PF:WC?2M3dfNg9]a`emUH&lt;]ARooBLZ\:kUkkkmM^^;g[CAF?o9BS9X&lt;V_06oLo]n`VOa[dMZmhLlJ^=?^T^nMbojKJkCSoWN4WIgV\ckgWCOWb7&gt;jno&gt;;[OS_oVacNOW7jg77?7OooD2OombloUnEI9_InB&lt;HI4[kZLf&lt;]bOKRmn::VQk1Tm`8F4;5W&gt;TA&lt;Kcd`aI[R8DKQka6aboN?k=I&gt;UJRNToCflBd:9=GW1XijhYcm92_e]^Rg?N[eOQO^9B&lt;2LjSQk=KKS8Eo?8kT9]m3^^fWPk?AQN^K4hZkc&lt;Vm&gt;gFc`@RgL^O5bET;[D_=R`WO?&gt;&gt;77S_K[1miPR@lgJ;?^^n6om3JliJgSBbAO&lt;J&gt;_7OGSQoU5Mo5ainP9oNj=DL&lt;NdI=^]VXFK0i[_\n0emoFJc]\=:4K&lt;HYHRl[4;=V_6SaC6ETl6dE1KV^E5NV9OgQBU&gt;n`WYOLgi&gt;S84nN^1mG5`SPC1]S:d;`B=4NjKmH&lt;UULW:0\;?2W8FOA:^K?M9TIFdMZj?UgUemK:5BfZf19WV&gt;o2K6[k;XS0HEj\8[[9QY;;_Z:UlBgN&gt;g897SGQPF^OS\Ba8&lt;Nl5AB?;oWBQ6aJP@1SQNGhXj:1DK9OHN&lt;6lGSkolg=dM`l2hG?AKRH2^5E7fbmmi:cJ2A056EVl9@Ll@B9;Ml6POPlacQAcKJf4N0AbVYZdLjl=5el2I6[[UbiSJdAiTCbBdeiYEk9g6Sa7[CFB8`Nkc\S4`dNB53K4Y@M`QAkbIdlgkPUJ??fmoGj]cMHcUoJH_X:heHfm2bQ96d\&gt;Y;:5diBn6JoC0O8DGdkT9VIPBjN^1cB`TcbjfVBJNQ[?b\onSkg@kON1onmnGNoOnYOo&gt;kc^Ofm]G7mB&gt;Qba^I&gt;6iVCm0GSnGTYgQ_Ig4AOR9MZMAk1Il1RgBV7TIAM`A=\k&lt;V4O9c?_3Y:O3l:dCYMk^gg;jl0L0CVKCUWH5`j7aeFkA[b&gt;CTQ95a^731VBF_IoV`TDggl4NO?G?^6Y3k&lt;P]4e7VRbee]]ZcM@Jf4&lt;;aWfGU&gt;9^:[`SDoKE?YZ:Vd8[TTU\cVW7EE&lt;cK2Y;_LD3MKjVT98S3E]O@NF=[GoXgC=`=OMNoZQ@@l2P:F[`T0:[LS53m:IMEkRTe@8gJE`&lt;]Y2:U`M8HkClI4_aPZN:4ZLOC2BoZFX8GCf8_I0;U^`[:e@:ILD&lt;808A]97NXjMJdHVK5&lt;6@ZRfV:AX6kPcgf@:31?M9dKQa?=RA:`f5TCI^bQLjbA?jYd&lt;_1^@Iek6[helE6RFL:EWA[cHLkB2l7QLeCBJX]0hDPWUWlCJ=:^m5gJjn&gt;SW9DRT1Q[Y5`gAf&lt;OdDdj1YNo:`NeELR3c2mU`G:e&gt;j8@]gAR?Ad48]8;:;&lt;S;EUJcjMiOVF1m50TbUD\Tl58jH?d\X8T^08T=W9[Z683aTA&gt;]W[5Oi5M?52E\:71[03U?V`4l_1WVH4j:GKI9hcEGRk3?_;k:;F_ej5SiN:WT:RF=Gmdl:=knc:UD^Hj9obj;AE\I7HC&gt;FB&gt;jYl8f56nJ&lt;UcI=fiN&lt;i;VXUJ55KE9jS9S_DR5N1k`PSNZVY0Z0iTYNej0?V_@UDHkL6Co5UCKBGPJYGR_Ti@1C@\A6TiIe;E\]e=ZZKd\ZVfURZTM50e8JQ[&lt;TMTUjFdJKR_9CXd\N38JN&gt;Q&gt;\UNF]@;FB8LQX@?dbU@[8mfDU3:S0dI&gt;?SmaPSHhfe6&lt;gV@A0JSZnmSECILX[AB98eHXQ9`R?5E3I6[4N=mYUREb_5jZURE5lhN6VZ\P`:`^;AQONF8O:Plbm4XSolW7VZN&lt;?OL8@0JK^m:5oh&lt;AR[a:BRlMniCM&lt;Q^\X\Nkg7G3ZMAi7nm:9PFFe3mCA1\]DY\Df;6aG&lt;iI]h2G6MG`BA\[I]008f:U6XXSNH2jcIXFSGI5Q2bBEKA`&lt;X]h_:@RfNklLbR7Sji9F_895&lt;R=Q572IULj=^noMWZiZ`ddKH`@`He:jliNb34YNl9[QT6cAlE&lt;6LflQ9e?nUMDFlcJBlA3?PP6fSobc@Of_fBSccJNY=&gt;?N3lZRDPO[EVgdA&lt;FBDB`XE&lt;^e]0&lt;&gt;VkM0OT@X&gt;YTBh&lt;5IL&lt;3?]`D2\9TbD=P9XH933VJR1BePO?6H6&lt;2;Rb:@82Hbj[IF&gt;5Pl5;dH0QG4:@48T&lt;39AjLjU172J17:JNl=j0P6NHX8U6RT@@_R0PglmF;;HX\i:jV^ULZBDKEBVfUTf9YQgX[9IDjjfT&gt;:iY`4VU&gt;jmJ&gt;^lE2G:UodJJ0?kJBH?eL@[95RbKJUIOlaNeJ04aJ?]A4YMiXMjb8EdSS:FQ@7jO^6V2_52W:f:]&lt;6e5Cd?=1I1S`LR^aZ9L?2:i8gKEhKfCL5bbPaMloUSe;o9aiAW[oE2DcNMo=]V3VZ3j=;eK0o5HDY[@\W;=e@Vl8XLFANQC9E&gt;QSA=CQY79hkh3K&lt;7T?;nR9;Z6LT?Nc&gt;S&lt;VnOhN&gt;A7dhl]K:oLi0N`lo`P8XYbiZhgEiMHkPY4;7?ho]9J`Z9g^0o=n=LSnOn?ieOB64nHAQFTK8PM_MC[JSeR8@G2bZIEdgH&lt;RZ;OM]&gt;@_LW:9G&lt;i8_M&lt;G0iefC[hgQ3@MR?7jB\Tc1Tf;FbZLgF5X3L[[i7=`i99aTj6Bf9hoc4f&gt;K\mAKJU5HVOhmaTQmdX?THaTcA20&lt;o\eFYJL5Fl`OaV0Lg^m=dM8dKEXZbi_aM`N4iNOTmgWYL3]hN6L7iae8^GXbD:O\Y6CH3&gt;KSj1^`C4a]&gt;WQ7OESNDVeoS81il`C&lt;lI\h;BR2o8`kOIUYaC_UM6UhYa5^:Vn4Tg@DYb3U\b\fAFX]aIIO3S\LG^&lt;VA[9&lt;di1?XH4d]PXFb[&lt;mS6WM1H7n4QOPX3V8JcaJ3Bc2f`3kS9^djl1&lt;NFQDkA93Ufmf&lt;amc=`80X1e3HkQ:L]YabEBD05fi1W2^:CkBEDcH^&lt;iZ;L:\8jH][;VZj4R5VRdB6F7g=a:g99Z[d9NoQ89XZfYU6Ej\lMNK`GXE8]&gt;kb1[e?Qc4mH:lRM9\OK7F\j_JGQ2X&lt;8nV91\\ReIUTd4;L6nZ4o7O&gt;5To5e:L?2S2kY98YfOPONej0UZd28\R5Kk_&gt;WnN^DH2Ra&gt;8JPmDGUT4BS3E6S6N6PXQ^o?DU4hlJ1V&gt;V1L?:__=@EIUOn9X7KR2Lo=2KmV9A8=\\T\C=1?n1D=@?IkA\=f2ii0CCN:&lt;9RPOFL`NU8DSQ&lt;`;_2&lt;nB]=6e51SI8613fMTW3Oj[L^R]8&gt;Pi:a`A2D=\4K&gt;il^UBR7P9]^G5NXA2^X7951G[YT\OKLGG4l=UQn;H7@B;8&gt;da:ibOD[XBR`]o&gt;VZ6DOCdK3AP?3A_33UbkQTneQOg=b`jYf;]h]AolQHPG^On43=0kIj9]cNR^:eSCY@7J3d:fE\We:Vb01HQD:H^8XDCNhWA\A:WD1Gl3&lt;U7dkK=5DgXUKgD\cnF6@[17\Fk=:4E@TUiP?Fl@0i9ZoM2bEb`155W4J=3T3DML1\aF:FfPQ_KUbIc:4Ya3JFAmR\aJMI0a[C4^ef5m^Fi4&gt;XZHB6?JU:=DZ87J56eH&gt;DmEMhP4D2oO3SJP&gt;1jMO2&lt;naOX3XeHoDCM;;J:PJlY8lXGAERILBl6Ze45f=C_H1EH@IjHR`mDHLk&gt;RloAEY7C[?GIk&gt;fJcE8?]mNG9gjfLehW\mLW]iM[?]hJNCWK\EIR0P]hk6`E4NUFW`L?jP9&lt;3@in]\&gt;b[aNQRj1@R1@lHWUO7cje0A&gt;LK;JhC[BgiI]\2@eSX:;QfRU@U&gt;]@_lm`4NmBZ\:ZoSFUb?TlhO5;?&gt;B1H?gA7=g=C1ji=292Ke0J\FnE9DeX&gt;CIC;iJ0Q`DXj&gt;W\&lt;PEOYPYk5m[A0\aN8N8UXTPGU[n]bW5n:`?nZlnnf\Imkoebbigkc`ofP\eP3l@ZOUX`?B@DZR_DX[^jV=gj=d1Ym4Z&lt;ob`?C`SLo9T5_eOKONeoF]7?koVKmXXP&gt;@mOLEB_KIcmYAEE:TPO\X\:IW;;f\GU_9nGfb7gkm2FX@_m\=LZKGW]]fQbgkjIKFn:Z?7OkIIKJ[SO\hURRIoOHS?5Im13fdEU3GX6A:fkd1W=WEW;WIRW;nf8PFKmj0I6c\Ol161GZUA]d;MJ:ZYK=VEA5\=d;6WchfDOoda;nMHPO^dHdLa@nRM@8^2Oa`S?HXLF4nDR@[gd@3ZWg?=HDeoV\ekeE:jne_Z_g?4HH]X`?HL\fA&gt;3IiNAk6W1m3G0_2TCL=LYO`T`_HK@l\3K6f3=3kY61mh3P6N;k6W1m37PK&lt;`\K6`f=3Y6;mn30n@QPPL_O`T`_HNXdTNm3PcB7f3=3k]61F3f^\2K6J51o9_dONJi[aZ=PgGoQ_YlegmNBlj]Mg1Y9kjW]mhcf\AE?5N[_l]E?eCjcMOO`&gt;NKk6j1FegWdiGIk&gt;gJcF[NcfKLeBjFNcffLFL[]in=6bC_H8^oNbA_H\`Ig&lt;[Zjc\IO`GPnSnRYk245=G437EhljgHLTJJgAIlMMmTC]5Ofg3k7l1=okWM^WiPP\Tb&lt;_gjXVbPjlMb^O2?7g2GoojlSJ\BolCmm&lt;eolmTbca0HGIPS7WELFBRNnUKon6]o_boQc4&lt;O7WakMAfZ1;@;]BVhfZ6d;A]\Y;]^C\2JNWl@EDkjHUD]8Gj3k:Gg9M]64UVIhV`0kFZjnXDXH9Ul?3UgC&lt;4E`da=l&lt;6aYaK?YSB&lt;ZlK8AkLXPga:L6Y9WXb^R2:;XfCCXg46QgO@OonCH=04lnD]G?@JU0oW&gt;8R[cd5WUn`Lj&gt;_L4H7acI]&lt;]SYiCVkXMEcP^ab7Tf\&lt;L36cdmoD7?&gt;U&gt;FXnG58NQBfkE`&gt;Y&gt;ZXN^;LUDk^0CT`]]YcV503o2&lt;9aY76Tb5=h;3n^l@;GR:DEml&lt;HjcCj]?2BHSYcAH8LcPLdmXLfl9&lt;R?P&gt;m[d_OAF47OMiiSBYLBDIO:B2mBEQejeLI1_lDOkc^TPmOSR;N?RhN=R3X@`aEX13VmJG`^nJRDXYeb7QSJiLJ`NX5Qkf=]imm&gt;nKg_CV6OK]RK94GkTDXQ&gt;HaT13fb00I9PG6JX1RmPQA@CXT2Ci9A4;\8804oTS3&gt;9F@3jQ0Q`Yb6PH2J8=QIl&lt;U65fY12^T^l2@8TQ51B^@UA:oVP&lt;O1`X1PnPjXO0`P3GQkdBQm:cV001le`9l2VYAPg8&lt;0k8Bm6`QjeP@j2ciUhWLj@0LY?3AP784;S@YWHX1S?Qn1m1kHbJS6f811fJb&lt;=99l6:nE1PPJ=8l=&lt;a\P0dAX0LXTD&gt;iH&lt;5QR6^dF;Bab60@I1@Q0HZS?9?A@TRA`J1PHiRc:Q:_jX1GeY=N[B&lt;3V2Pd60J^Y3@[1hD0XF2MP;&lt;B3RX2_H4PG43R;`1ZV@8E0R&lt;KHgh4VHe2B0H4:Y&lt;H5&lt;Q723C@d@1WBS^63LMX3=h4n91c3XeS;4aDhDR99PE40@14SA4S8Z_QlfJ^kenOQMQl\MFkQ32aVj``BUAmNDAB3?\R55J4A\37PAhR]3=KA6W&lt;86890Ck1NP@_[g:D6dV4Q49fS?IJ_C2;S^7mbE9SkO2G9Ii^ggHKkT`F370_j7b?jkWkEQ]:?XVf6A2ilo3@QYRZ82LV4K6^KABIXe``g6B7e1HCJK8hP9k^0X&gt;O;4j2^RRM3c2=aH8f`YUfUlb`B&lt;3I37=]e&gt;@JZ?KI:?@GJMZ]DOXZDNYX\cVFBbZ1RmDIF82=NNZDMK0dibVYa6E8b@nBP&lt;5Tl&lt;05lIDYhX^b6F\?\XfTjW:PUgjFJNIm\aeD&lt;eoRAhT`S]9IT7:LUghEY&gt;2fJODYDMFWDNBTdof=ITOaPAL59FVSX7NGk\MRM]DU&gt;&lt;nm39CJKab2S9fP&gt;SbRPR`h&lt;R0@D@5P9ZV08\FAR=6B[D?`iF9Xa6Q9e:U\ARX=B]93S4;17PliCP_8N5h`&gt;i6V3&gt;38TciG@Te@WT`HL8`hPj;\D6gSlTdaAYJMc8Hiaf&gt;[[@NAUBeHhFNTm7NYnXia&gt;:JBgQ?oS?;U9jT\\=AYoUTMCT\81ZYRXNJb\lbEEL&gt;e79ib&gt;:2`]U2jToCY]80BfV:4``\X1a4BL&lt;9?9ATRQ4bcK7^1A4RoX@7_2@S;hfe90M;0D;DJ]?I]5@0Y`&gt;NV3LF5`I1LYCFZTJU@=fTdVb2IPfC6dDZZ8JGTc2QOh;^L8HnSlnS?YbH5TGiYN5i9a8XWVIV]cK^:A]LH[5Lm2L34ZfLDn&lt;hgf2IHQJV6o[CK&gt;:33MOAcD5k&gt;LcEW&lt;&gt;D1CTFD^e69IAD3mLk&gt;C56YaKeFci;[THhLnK]V7iaZ:O5@PcUHH0f];^:5a0o2@FhcUKMQ5D&gt;nJn?Ija2clJo0KQ0:6Z&lt;7KD=:2I^YmJGE@ELPHG[9N\9mCc046gh\;[KBUd_I=RJbRBo&gt;kD8\BUXbUB8c&lt;]fF[BViXJSLNm=oWLlRY</protected>
		<protected>E@=3BJiO100h]L]MGkcK3fBoaKgcnO1C[KY_3VgFg3f\:dbWRb]W]ja3ZeDT&gt;gG&lt;F3C`h&lt;FRIEB:dR&gt;oal1lR8P`R;7UdVj]0WcI1;0g&lt;G02gHM\_?LJaZU?0;bU&gt;?K&gt;mo9iW:SW4SQU`7k?R&gt;OCUM]W&lt;jeB0_&lt;LPOEolh&gt;\=nNYf_\cHOnG4WQd6UA`SLO_Ad?fO&gt;njZG]]_]Neo`^=LRZTLTT5MG&gt;RnKeM2h&gt;L8iUjM&gt;8RC2OMoIfR2X&lt;C_Lka@&gt;B]G96ESU?&gt;o2XYIhW38;liQ9CWZnPo?&gt;KMefNkmo`5lF^ST9RZ7HULfI]cIoi@K&gt;L&lt;a3YOo;ZgDOf&gt;hfcFAc_HL4EFmLci?Ggf3&gt;&gt;foggfacn]leXS49aC0bmIFlclng=o=V]&gt;_kmhdVblRiH=4n&lt;n=l&lt;lnghEb_jco^\QknmkMQFgm8mGNnb:Ale;FNmHYmlooibXo[_JhdiOHNmn;LMfCJU=VL9lYlWUS;ho\mEk8WaK@i;f13GQ6dgBMD6\2\7O2GA9AIOfSfo7oNGI^laUnL0cjRg&gt;`?6im]Q34Hi1?MI0:Udgjk7MPSGM9j`5EI87&gt;WbVf5X\`Zob5B5QoWUnMNgXBWkV\CWVj;XX?hX^Jg?&gt;Z:ASVm8O8jiUbah9onn\n=Xl2oI&lt;]6GGomAM]Hne?gigOX`\_OKE_Jc1mh\f8hJ&lt;K_^_]^kGW3WohXebO25P[dTAoQ6]g1Ijc9e]ikO]lLBJNd04EQIE^MjQlkChJaR4&gt;]?hVjVSSej@&lt;Zi;KLZL?71d=gWMd`HE`gG;cOSa=T&lt;5k;9b:bL6[QoN9&lt;VkPYdI=8[EP3[B2\ie9]f&gt;LF&lt;[J^eL_CkVen7&gt;5Ba[UQ5WE&gt;`:o6;k8hWPIej\\[Z9i[;8_Z:U&gt;V`O=f897RGQXFMNSRB98&lt;Nm93YWU?cUk34&lt;jI21Bg5In^6F:[CWNP&gt;EY=mP^fdM;8B;XRWR8IN3BIhAK3?fFC2g0k2=^YUT1QDaWN@WlFS9mdce0D^GmJQ[ga4CM7:5hEB&gt;a\FKY6[O[i&gt;6`0b^]ZjAaTl1e[IXG@MH[ah7O\kgbQbH?N_l]WmnGWk9omP4&gt;G68d:7IJ`b=c2h9lIbBKE:;]Fl@L1k;:[M&lt;aAM9aaHKGeC5n4`m;INon][Kk^WQ&lt;_On0OMn_nnhk^knnK_oWk`jDm9W`bIJA&gt;UVB^HHWa[9nDXcORQhdL9LG^L?n3TJ6T\`hkii?McS5;FcgRTeMGQdcYCin&lt;YfAONf:&gt;jbo08@ZVKTn_7hA69mF6D[acNhIR[7AlbWDf]8GD^ekBM^E^hmiGO&lt;J^7WB_V3VkLSP0Nc?aUnWfg4L98VM25HnBlbTVTUG=H6JOLWP\dG2JRY=HilehI74eKg&gt;PmeQCiRh30=h9L4I9lkJ5LH3&gt;=kLaY5?o]bAnGC9XYPj`IhD;67BNM[gAL9R8dh=Rck9B9Wmieb_^Y4Yn6_A9GYK1]7e4cEcW200EnSXZLco2:^mJ?IlMQ_`iQ]M6d\ZKK\DQ&gt;JQCc2Fh&gt;iXJcVDF;j8EKT1TbMmGihOXU0EGhF:]`G`FjW[HhPSiZE_Z?hYXGnmF62^=hn`MBjMJ1fDZgZ`EWO5cLkSb6mEX6YMY=JA4LdWbBN4I]=dgc_ONh&gt;dC_YM492mEBR&gt;KSHYOd=CV1Og::N3eER0;N8ELWdGZe1VFc=eAlQ5R0:MLER&lt;HO\TbAa1mRh?IdWA4^7g96EX&lt;I:C&lt;33OHY8NPB`ZHX90`LKjUfcYLOkADaHV&lt;;L?PdTmPT1[&gt;?gjhnME:GQU[Zi\edCN_PWUj[jX`]_=N?EViO]?2QDk1W?V8W_FJ23HS1YI_`H9V:3&gt;cS\gTT:U;YW5HTM]bOmnCWe7k`JYZeRUS[YVmaDHBLLEeNfde;U6C8gZ7T]b&gt;N9bkCI;bS@gZXPNTZH?:4cnB&lt;]5D`0ZJUJUT^cTc&lt;JF][dO=IFL@KbEEB^R0VT\X5VH^b:E;K?\aGB3dJg5_D3WWaE4b?&lt;PYEk047iaD[=]k4ZS_]=QRbHK=F;g8lmAXF&gt;QmESVhD&lt;iF8&gt;eoTUU6S5B:b506cU913NBHoJ_0G_&gt;UPUHFfoLL0[4K^Mb[VlBEM?9Vl5G&gt;RbhcB49^QWD&gt;2n?Wok?8G9nTA;9]TYFRN54@Oh`VeQDa2gVcPj:kTCM5EcPgoJk^&gt;]neYg4&lt;_I&gt;=LO9ZlU4\=CgOZRJKfl[J833OjRn@4g5J]374ZRGK038Vn5jf]9M_moj6g`]:&lt;F34bNeja&lt;oVgnmC89?NiQHToa:Ub8H2]l;@^Ro&lt;gXiokCnO7UoU52Z5V^CAH&lt;`&lt;LVM&lt;U;@NUe]LSUcXjRHj3eO?WMTDl;TJbC_;`P8G=&lt;ZZ22cDC;&lt;bf=0lOCKo7iALI1PiZ[0oW?XZ0Cf0Fajb&lt;3;di\Fg1HVR6VX:@c:F&gt;a?&gt;3PhKfRd8BgYhRQRV&lt;V1H7A`da05dXR1E\ADe6A`L`odU&lt;jQ2M\\f1;Rc`15VHQ8MT`hUZ&gt;L:D8O6D`obe1&gt;7kP@3]a6d16Lj15VeMhAN`1GWcF3eiE;FWNjPdc;g==J=eeOI;H8dceE=&lt;=Z=UYObfGLdbK9]Xdnfg]85hCW^lDm8YFG@Pg[Tii?UGMVBiH^@a2^hN3J7VWD?&lt;g4fVA_2DUEf_R@bIjMCF^HS\iUJb]T64JJ7^m0g5i1VEb9HgAldSV_iUTk@nig16kZFACb[_F]1;DGcMOX&gt;WSJFSjB=eKoQD4gBA4^^&lt;V@VkN[6:;[98UJ&lt;WXTaV8i]S4Olj0Tk7BdTY5_8kAN[U4l5bgW1_57a[od&gt;;N0_lOAINdAaDD`5JjmKJY1\lH96o72R3YfJ85i_lP7JnZgCin?XiVD:61bJAA\THP`K_ce[Jg9RX?:2fI[Ed4N:V=JOL=l9?GaJ=&lt;SKJ?nf[2TJHeQL5QD4^W43CfV:MBPJU57e9[ERb5_EecH6hDa4TMIS5\]mO@=KWQ]mEJQUUFROj9akhn5:LQ2MYd&lt;0a?Bk]NXFT5QOlJ2i8LIkO&lt;1gbf9E:Rd]K_J:F&gt;Do&gt;nKj^TNPK?TQ4&gt;o^N=U246SQeMCjB8D9;gVTcJ_REY2nL@KZL:TngB8iLOKe:Mh=b\&gt;Y:;^0jMJiMhliFIJDANdHPecLg\Ve76bL@[VLJd5EZRCen@_djBCkP\F586bl@8M]Zf28DU?c6aXB;`3jW&lt;gQge21C3dMHP4YIKWD1O2emO]_A45Nf?TEBB`;_Ll?O&lt;X3LBjB39?C=8QJZO9Q5dATCl8ZTTWmK6_9X6hHcXWX0D5WDM0fcU2Le8`A5k3Lf7RYPWlXCVDV7R_WZJQVHFmY9fBkXmUg7YHcb7VlP6_K[Q928gWWlN7mBCHkm&gt;]]80ddI&lt;BRI_b?PS43aH46^T55LeE&lt;&gt;^TG1J?NI=F8&lt;Yomhl@hKmRZZ&lt;BPYle4clb_G[k144=hN6h]iZ6S8&lt;2=H=3iI0EAMo^O:9K8d3F=\235EIfOQZScnmZB&gt;dA5h11Fgj`:R@SKh9H5J0o?1DL;&gt;44k\=@f5iT4CAb:9C&gt;`AlND&lt;BTY0IhQo:2b[_&lt;gFD45W2Q\7ZVj&gt;7&lt;1EiDCKADMcELR@1?D&gt;QS[LiEF9cPSTfHGRbL&lt;QHYl4@d`JIhiG^`7eAFo5h&lt;O7XfdB25CjBc&gt;f5XZT8nFGig&lt;@bECNSMHLQUHMP4X^_h\_^iD^IcAo=YU5ddm?g?&lt;ZB5U?d4I@o7[m?=]&lt;MVCJEH=TeeD\?^C9g8R;d&gt;H6IiPFH=c][&lt;ZB[hjDbFB_957AN]_Y@;LmlTJJLoNJh0bd1_oGRAHQ=kBGkh192G2Emo\9;b`C9J&gt;Id:FX8XjH3JV]]jHQ=`N\FDOBTP&gt;Mf]:j\m7Zd=P=^69k;9`Mcl3diU^SJVTXE&gt;fBZ&lt;NDFdEPe6ZFGhL9YHna62=1NAeVn]ehPiA6a7ohBYm9FVD0giCam0^W;RIL:n1Ze90k69f&lt;`XLXZJ\abmD4Jk9RlbFcI^C6NN[\ij6N[?lHHKcEji6N[k\i6WN[\^i6NhKdm97K\fEV8GPdjl6E29IbWka2fB1D5]AjIgEVF?C34MeQ5F0lH7FO5&gt;cm2KAT]k5b9iEkadMUD:ITV_\4F4TIF?4U9C7cfdBAGL;UK8]KGoH3gEHdc9:ST@2nKHNN2`iK[7:REBIhOAGgCPVk]B3]Fi16P`C\?P\\@WW1j7L;aYm5E&gt;9C\69MO0neG=gjA[JCl2clGo&gt;mKoQPMneg_Jo]F3Do?bN&gt;;&gt;oONd^N?:V[:haSC0]ZUk?Oc?oOBfOg5g`5Q[gCCa3^DNjDFD:G5aBhEU6UEM\X;Q^c\06NWfXZ27nVi[2T[gQM5]kTNQ@TEfIhV`8GaE&lt;mADXI1jNWUaK9CA5L=0k?C3V=kSDV&gt;^T6;]4L79;oA`U`Z5l5k0GAmJ0=MH2egZ8k1nVnOd1]TlRaIWkjH8Y1hEgFNXMUm_YbSgFaP&gt;D6&gt;]M;VB]O[QMd;h_\6Hg5oYV`UbDNH^U[UA?oG7hKVBNFJC25kHEhY:^ZNQY;U2ek8gCT\7]Yf&lt;54oL2&lt;aTU74Wi2b&gt;7cDc&gt;?keFDiTZ?6n3P1?o;c?21XS4nZgHmAk]lPS]?PgCi:e?C9G:BmkVD^EcC5?BM`V^h5&lt;M;389SOTH1k7V9R;5ch_70;9objaU\H^ZM^kW6@&lt;7TZZOWBWn&lt;5c@QXJgY0D:nEoBJRWKD@&gt;XVO\U2nW=iH&lt;mLogXf`g_IafSW:A926DN2R:I0@=\`7?0d858eT06h2Ta6jXHAJBQT2U;\`A5Z8QA:=@T:TI2mm1&lt;nTQ8LBd]S`LN8&lt;9ZTdfc10P@AfE83FC64IZ210IU21W0&lt;A:o:YP3aodV`Od=`P8POJahNPBHDX1N;06?ZL4XPl0e@l\0l:dL&gt;mj8&gt;B374D_a1X&lt;X69N7VHU3b@RO?7nRHQD`@0Q&gt;JkBS3kEA_U?XH660WS4210`XJ3JP=JRR4WWa4BD0WmZ&lt;Oa\4&gt;0S4A0Q&lt;iF86PY4ST&lt;c1aZ@Q5Q9aVX1HmY1I3C&gt;3n2P&lt;62JjY3Dg1h@PXG:C0;&lt;FK2d1J\2@]0b80&gt;c562T2@D&gt;3nFQHE;Rh::HDa5_YHQEC`XP:1ZG5Q&lt;D8HD@SH:h\K88k0ab^4R9VQ=H\0V4018FNR54\AOBFhNa4D:XRU_538ZFP7&lt;ZhP8_Ae06R6l@=PRl6X@\5^SSH@ZnMml`dR`Bl5636jEA[P5:&lt;0G:;:TneHK&gt;N5kQiHTOjHIN[_aPh&gt;N\@XN_mX^f]E5CKm6Zce:l2AmS399@g58P@a?QgL5lQ`cm2JHTTUR8IIKM864C_k&lt;BC`a1@[dE;Pgki5CC6^0Zf\C?\Ah9`BJIYFEVY=XT4cY\]BXbEIDo:T96jiC\:;BjS;a]E@XXRTZL7BV&lt;mBPFO8A6DYA:?9WYTPIX@F9R@e^EgDY]?[U1lZOFA[KdWHSV]&lt;GfMXMeHH;46Uj_SbEHdjTO6[lG5MZQRf[mAnUk&gt;@6VQY:]:[4cXfG2h_ab^Eb9T6i;RRARUkHKn8N6ZZB=&gt;QlO34A47@S0e0SW=AB2HU=CARD5g69HSDdE69SQDd6j9F5JAR1?n8lMi03e_jh:WTnW`[oLdoJPb:nf_5\d10&gt;E@R@8F?;Q8_7WU&lt;=&gt;RQ3UeiKX7]Z^?5kccV[KoGViG=lC6U]a]`hZ@c?TPI\d77iMcidQ]:PPX:DfW;Co:KkH0Vi5]D?IM:X0YETom=[F5N`2aQ@TS6?V=APERT0P&lt;F;=3\h3B26&gt;@lRj1m0P@Gh0JZ0BM@&lt;e;JSU?Mh@`Uh7:V3RLQ`J&lt;1C0Yeb&gt;[8g4oNcP5:D@I3]ReZN:Vm^58LW@1;523mMi^e`9_@NHTgH=U7EKif3YT_Q6_70lmTk_NmVW]li?e]2M`gJ&gt;UUlB&lt;LFOdoQjgid]hGR9lWYMfDo=1g2X7l</protected>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='21'>
			<Action classname='StepType' isroottypedef='true' typecategory='1' timestamp='1618215606' typeversion='21.0.0.2' typelastmodversion='21.0.0.0' typeminprodversion='21.0.0.0' typeflags='33554446'>
				<subprops>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs' flagsforinstances='524312' instanceoverrideflags='655384'>
						<value lbound='[0]' ubound='[]'/>
					</Substeps>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "ACTION_DESCRIPTION_NAME") + (("%ModuleDescription" == "") ? "" : ",  %ModuleDescription")</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "ACTION_DEF_STEP_NAME")</value>
					</DefaultNameFormat>
					<Menu typename='StepTypeMenu' xsi:type='StepTypeMenu' classname='Obj' flagsforinstances='524312' instanceoverrideflags='524312'>
						<subprops>
							<CanBeSubstepType classname='Bool'>
								<value>false</value>
							</CanBeSubstepType>
							<CanOnlyBeSubstepType classname='Bool'>
								<value>false</value>
							</CanOnlyBeSubstepType>
							<Category classname='Str'>
								<value>""</value>
							</Category>
							<ItemName classname='ExprValue'>
								<value>ResStr("NI_STEPTYPES", "ACTION_MENU_ITEM_NAME")</value>
							</ItemName>
							<SingularItemName classname='Str'>
								<value>""</value>
							</SingularItemName>
							<SeparatorBeforeCategory classname='Bool'>
								<value>false</value>
							</SeparatorBeforeCategory>
							<SeparatorBeforeItemName classname='Bool'>
								<value>false</value>
							</SeparatorBeforeItemName>
							<Group classname='Str'>
								<value>Action</value>
							</Group>
						</subprops>
					</Menu>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='262168' instanceoverrideflags='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value/>
							</Icon>
							<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7143448' structureflags='2097152'/>
							<PreCond classname='ExprValue'>
								<value/>
							</PreCond>
							<LoadOpt classname='Str'>
								<value>PreloadWhenExecuted</value>
							</LoadOpt>
							<UnloadOpt classname='Str'>
								<value>UnloadWithFile</value>
							</UnloadOpt>
							<Mode classname='Str'>
								<value>Normal</value>
							</Mode>
							<WindowActivation classname='Str'>
								<value>None</value>
							</WindowActivation>
							<ResultOption classname='Num'>
								<value>1</value>
							</ResultOption>
							<StepFCSeqF classname='Bool'>
								<value>true</value>
							</StepFCSeqF>
							<IgnoreRTE classname='Bool'>
								<value>false</value>
							</IgnoreRTE>
							<UseMutex classname='Bool'>
								<value>false</value>
							</UseMutex>
							<MutexNameOrRef classname='ExprValue'>
								<value/>
							</MutexNameOrRef>
							<BatchSyncOpt classname='Num'>
								<value>0</value>
							</BatchSyncOpt>
							<SwitchEnabled classname='Bool'>
								<value>false</value>
							</SwitchEnabled>
							<VirtualDeviceName classname='ExprValue'>
								<value/>
							</VirtualDeviceName>
							<SwitchOperation classname='Num'>
								<value>1</value>
							</SwitchOperation>
							<RouteGroupConnect classname='ExprValue'>
								<value/>
							</RouteGroupConnect>
							<RouteGroupDisconnect classname='ExprValue'>
								<value/>
							</RouteGroupDisconnect>
							<MulticonnectMode classname='Num'>
								<value>1</value>
							</MulticonnectMode>
							<OperationOrder classname='Num'>
								<value>2</value>
							</OperationOrder>
							<ConnectionLifetime classname='Num'>
								<value>0</value>
							</ConnectionLifetime>
							<WaitForDebounce classname='Bool'>
								<value>true</value>
							</WaitForDebounce>
							<PassAct classname='Str' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value>Next</value>
							</PassAct>
							<FailAct classname='Str' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value>Next</value>
							</FailAct>
							<PassActTarget classname='ExprValue' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value/>
							</PassActTarget>
							<FailActTarget classname='ExprValue' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value/>
							</FailActTarget>
							<CustExpr classname='ExprValue'>
								<value/>
							</CustExpr>
							<CustTrueAct classname='Str'>
								<value>Next</value>
							</CustTrueAct>
							<CustFalseAct classname='Str'>
								<value>Next</value>
							</CustFalseAct>
							<CustTrueActTarget classname='ExprValue'>
								<value/>
							</CustTrueActTarget>
							<CustFalseActTarget classname='ExprValue'>
								<value/>
							</CustFalseActTarget>
							<LoopType classname='Str'>
								<value>NoLooping</value>
							</LoopType>
							<LoopWhile classname='ExprValue'>
								<value/>
							</LoopWhile>
							<LoopStatus classname='ExprValue'>
								<value/>
							</LoopStatus>
							<LoopIncrement classname='ExprValue'>
								<value>RunState.LoopIndex += 1</value>
							</LoopIncrement>
							<LoopInitialize classname='ExprValue'>
								<value>RunState.LoopIndex = 0</value>
							</LoopInitialize>
							<LoopOpt classname='Num'>
								<value>0</value>
							</LoopOpt>
							<PreExpr classname='ExprValue'>
								<value/>
							</PreExpr>
							<PostExpr classname='ExprValue'>
								<value/>
							</PostExpr>
							<StatusExpr classname='ExprValue'>
								<value/>
							</StatusExpr>
							<CanSpecifyModule classname='Bool'>
								<value>true</value>
							</CanSpecifyModule>
							<CanEditCode classname='Bool'>
								<value>true</value>
							</CanEditCode>
							<CanEditModulePrototype classname='Bool'>
								<value>true</value>
							</CanEditModulePrototype>
							<CanEditParameterAdditionalResults classname='Bool'>
								<value>true</value>
							</CanEditParameterAdditionalResults>
							<PrecondIntExe classname='Num'>
								<value>0</value>
							</PrecondIntExe>
							<Requirements classname='Obj' flagsforinstances='1' valueflags='1' structureflags='2097152'>
								<subprops>
									<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
										<value lbound='[0]' ubound='[]'/>
									</Links>
								</subprops>
							</Requirements>
							<CustomResults classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</CustomResults>
							<AdditionalResultsHints classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</AdditionalResultsHints>
						</subprops>
					</TS>
					<NI_Data typename='StepTypeNIData' xsi:type='StepTypeNIData' classname='Obj'>
						<subprops>
							<EditPanels classname='Strs'>
								<value lbound='[0]' ubound='[]'/>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
						<subprops>
							<Error typename='Error' xsi:type='Error' classname='Obj' flagsforinstances='4194304' instanceoverrideflags='4194304' valueflags='4194304'>
								<subprops>
									<Code classname='Num'>
										<value>0</value>
									</Code>
									<Msg classname='Str'>
										<value/>
									</Msg>
									<Occurred classname='Bool'>
										<value>false</value>
									</Occurred>
								</subprops>
							</Error>
							<Status classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</Status>
							<ReportText classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</ReportText>
							<Common typename='CommonResults' xsi:type='CommonResults' classname='Obj' instanceoverrideflags='4194304'/>
						</subprops>
					</Result>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>DefaultLabVIEW|DefaultLabVIEWNXG|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|DefaultHTB80_Template|Default_Template</value>
					</CodeTemplates>
					<BlockStartTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockStartTypes>
					<BlockEndTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockEndTypes>
					<AppliesToBlockStructure classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</AppliesToBlockStructure>
					<CanEncapsulate classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</CanEncapsulate>
					<Category classname='Str' valueflags='24' structureflags='524288'>
						<value>Action</value>
					</Category>
				</subprops>
			</Action>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='24'>
			<NI_PythonParameterResult classname='PythonParameterResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>1</value>
					</CheckedState>
				</subprops>
			</NI_PythonParameterResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='23'>
			<NI_PythonParameter classname='CPythonParameter' isroottypedef='true' typecategory='3' timestamp='1650060872' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name classname='Str'>
						<value>_notNamed</value>
					</Name>
					<Type classname='Num'>
						<value>7</value>
					</Type>
					<ArgumentValue typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgumentValue>
					<ArgumentDisplayValue typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgumentDisplayValue>
					<AdditionalResults classname='Obj'>
						<subprops>
							<Input typename='NI_PythonParameterResult' xsi:type='NI_PythonParameterResult' classname='PythonParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Input>
							<Output typename='NI_PythonParameterResult' xsi:type='NI_PythonParameterResult' classname='PythonParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Output>
						</subprops>
					</AdditionalResults>
				</subprops>
			</NI_PythonParameter>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='22'>
			<PythonStepAdditions classname='CPythonModule' isroottypedef='true' typecategory='3' timestamp='1650060872' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<PythonCall classname='CPythonCall'>
						<subprops>
							<UseAdapterSettingsForInterpreterSession classname='Bool'>
								<value>true</value>
							</UseAdapterSettingsForInterpreterSession>
							<InterpreterSessionScope classname='Num'>
								<value>3</value>
							</InterpreterSessionScope>
							<PythonVersion classname='Str'>
								<value/>
							</PythonVersion>
							<PythonVirtualEnvironmentPath classname='Str'>
								<value/>
							</PythonVirtualEnvironmentPath>
							<InterpreterLocation typename='Expression' xsi:type='Expression' classname='ExprValue'>
								<value/>
							</InterpreterLocation>
							<CreateIfInterpreterDoesNotExist classname='Bool'>
								<value>true</value>
							</CreateIfInterpreterDoesNotExist>
							<ModulePath typename='Path' xsi:type='Path' classname='PathValue'>
								<value/>
							</ModulePath>
							<OperationType classname='Num'>
								<value>1</value>
							</OperationType>
							<OperationScope classname='Num'>
								<value>0</value>
							</OperationScope>
							<ClassName classname='Str'>
								<value/>
							</ClassName>
							<ClassInstanceLocation typename='Expression' xsi:type='Expression' classname='ExprValue'>
								<value/>
							</ClassInstanceLocation>
							<FunctionOrAttributeName classname='Str'>
								<value/>
							</FunctionOrAttributeName>
							<Parameters classname='Objs'>
								<value lbound='[0]' ubound='[0]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name='' classname='CPythonParameter' structureflags='131072'>
											<subprops>
												<Name classname='Str'>
													<value>_notNamed</value>
												</Name>
												<Type classname='Num'>
													<value>7</value>
												</Type>
												<ArgumentValue classname='ExprValue'>
													<value/>
												</ArgumentValue>
												<ArgumentDisplayValue classname='ExprValue'>
													<value/>
												</ArgumentDisplayValue>
												<AdditionalResults classname='Obj'>
													<subprops>
														<Input classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Input>
														<Output classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Output>
													</subprops>
												</AdditionalResults>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
									<value>
										<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
											<subprops>
												<Name classname='Str'>
													<value>Return Value</value>
												</Name>
												<Type classname='Num'>
													<value>7</value>
												</Type>
												<ArgumentValue classname='ExprValue'>
													<value/>
												</ArgumentValue>
												<ArgumentDisplayValue classname='ExprValue'>
													<value/>
												</ArgumentDisplayValue>
												<AdditionalResults classname='Obj'>
													<subprops>
														<Input classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Input>
														<Output classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Output>
													</subprops>
												</AdditionalResults>
											</subprops>
										</CPythonParameter>
									</value>
								</value>
							</Parameters>
							<DefaultParamCategoryForArray classname='Num'>
								<value>5</value>
							</DefaultParamCategoryForArray>
						</subprops>
					</PythonCall>
				</subprops>
			</PythonStepAdditions>
		</typedef>
	</typelist>
	<Data classname='SequenceFileData' valueflags='4194304'>
		<subprops>
			<Seq classname='Objs' valueflags='4194304'>
				<value lbound='[0]' ubound='[0]'>
					<value>
						<Sequence name='MainSequence'>
							<subprops>
								<Parameters classname='Obj' valueflags='4456448'/>
								<Locals classname='Obj' valueflags='4194304'>
									<subprops>
										<ResultList classname='Objs' valueflags='4194304'>
											<value lbound='[0]' ubound='[]'>
												<elemproto>
													<_NAME_IN_ATTRIBUTE_ name='' classname='TEResult'/>
												</elemproto>
											</value>
										</ResultList>
									</subprops>
								</Locals>
								<Main classname='Objs' valueflags='4194304'>
									<value lbound='[0]' ubound='[0]'>
										<value>
											<Step typename='NI_Measurement' xsi:type='NI_Measurement' name='Perform a measurement using an NI DMM'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:1m8fotxw7RGuNrjdh1OqZD</value>
															</Id>
															<Icon classname='Str'>
																<value>Measurement\Measurement.ico</value>
															</Icon>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>1</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>4</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
													<Measurement classname='Obj'>
														<subprops>
															<Name classname='Str'>
																<value>ni.examples.NIDmmMeasurement_Python</value>
															</Name>
															<Parameters classname='Objs'>
																<value lbound='[0]' ubound='[6]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='Obj'>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value/>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value/>
																				</Direction>
																				<Log classname='Bool'>
																					<value>false</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value/>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>0</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value/>
																				</TypeSpecialization>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>pin_name</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>"Pin1"</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeString</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>1</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>IOResource</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>measurement_type</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>1i64</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeEnum</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>2</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>Enum</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[15]'>
																						<value>
																							<Num name='NONE'>
																								<value representation='Int64'>0</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='DC_VOLTS'>
																								<value representation='Int64'>1</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='AC_VOLTS'>
																								<value representation='Int64'>2</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='DC_CURRENT'>
																								<value representation='Int64'>3</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='AC_CURRENT'>
																								<value representation='Int64'>4</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='TWO_WIRE_RES'>
																								<value representation='Int64'>5</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='FOUR_WIRE_RES'>
																								<value representation='Int64'>101</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='FREQ'>
																								<value representation='Int64'>104</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='PERIOD'>
																								<value representation='Int64'>105</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='TEMPERATURE'>
																								<value representation='Int64'>108</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='AC_VOLTS_DC_COUPLED'>
																								<value representation='Int64'>1001</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='DIODE'>
																								<value representation='Int64'>1002</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='WAVEFORM_VOLTAGE'>
																								<value representation='Int64'>1003</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='WAVEFORM_CURRENT'>
																								<value representation='Int64'>1004</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='CAPACITANCE'>
																								<value representation='Int64'>1005</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='INDUCTANCE'>
																								<value representation='Int64'>1006</value>
																							</Num>
																						</value>
																					</value>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>range</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>10</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>3</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>resolution_digits</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>5.5</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>4</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>measured_value</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>Out</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>1</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>signal_out_of_range</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>Out</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeBool</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>2</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>absolute_resolution</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>Out</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>3</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																</value>
															</Parameters>
														</subprops>
													</Measurement>
												</subprops>
											</Step>
										</value>
									</value>
								</Main>
								<Setup classname='Objs' valueflags='4194304'>
									<value lbound='[0]' ubound='[1]'>
										<value>
											<Step typename='NI_UpdatePinMap' xsi:type='NI_UpdatePinMap' name='Update pin map'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:GEg07tGU7hGhxGDjK76h1B</value>
															</Id>
															<Icon classname='Str'>
																<value>NI_SequenceEditor\StepSettings\ni_UpdateMapping.ico</value>
															</Icon>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>4</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
													<PinMapPath classname='PathValue'>
														<value>"NIDmmMeasurement.pinmap"</value>
													</PinMapPath>
												</subprops>
											</Step>
										</value>
										<value>
											<Step typename='Action' xsi:type='Action' name='Create and register NI-DMM Sessions'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:c5USoqlx7RGuNrjdh1OqZD</value>
															</Id>
															<Icon classname='Str'>
																<value/>
															</Icon>
															<SData typename='PythonStepAdditions' xsi:type='PythonStepAdditions' classname='CPythonModule'>
																<subprops>
																	<PythonCall classname='CPythonCall'>
																		<subprops>
																			<UseAdapterSettingsForInterpreterSession classname='Bool'>
																				<value>false</value>
																			</UseAdapterSettingsForInterpreterSession>
																			<InterpreterSessionScope classname='Num'>
																				<value>2</value>
																			</InterpreterSessionScope>
																			<PythonVersion classname='Str'>
																				<value>3.10</value>
																			</PythonVersion>
																			<PythonVirtualEnvironmentPath classname='Str'>
																				<value>.venv</value>
																			</PythonVirtualEnvironmentPath>
																			<InterpreterLocation classname='ExprValue'>
																				<value/>
																			</InterpreterLocation>
																			<CreateIfInterpreterDoesNotExist classname='Bool'>
																				<value>true</value>
																			</CreateIfInterpreterDoesNotExist>
																			<ModulePath classname='PathValue'>
																				<value>teststand_nidmm.py</value>
																			</ModulePath>
																			<OperationType classname='Num'>
																				<value>1</value>
																			</OperationType>
																			<OperationScope classname='Num'>
																				<value>0</value>
																			</OperationScope>
																			<ClassName classname='Str'>
																				<value/>
																			</ClassName>
																			<ClassInstanceLocation classname='ExprValue'>
																				<value/>
																			</ClassInstanceLocation>
																			<FunctionOrAttributeName classname='Str'>
																				<value>create_nidmm_sessions</value>
																			</FunctionOrAttributeName>
																			<Parameters classname='Objs'>
																				<value lbound='[0]' ubound='[1]'>
																					<elemproto>
																						<_NAME_IN_ATTRIBUTE_ name='' classname='CPythonParameter' structureflags='0'/>
																					</elemproto>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>Return Value</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value/>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>sequence_context</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value>ThisContext</value>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>2</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																				</value>
																			</Parameters>
																			<DefaultParamCategoryForArray classname='Num'>
																				<value>5</value>
																			</DefaultParamCategoryForArray>
																		</subprops>
																	</PythonCall>
																</subprops>
															</SData>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>0</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
												</subprops>
											</Step>
										</value>
									</value>
								</Setup>
								<Cleanup classname='Objs' valueflags='4194304'>
									<value lbound='[0]' ubound='[0]'>
										<value>
											<Step typename='Action' xsi:type='Action' name='Destroy and unregister NI-DMM sessions'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:syCDFOVw7RGuNrjdh1OqZD</value>
															</Id>
															<Icon classname='Str'>
																<value/>
															</Icon>
															<SData typename='PythonStepAdditions' xsi:type='PythonStepAdditions' classname='CPythonModule'>
																<subprops>
																	<PythonCall classname='CPythonCall'>
																		<subprops>
																			<UseAdapterSettingsForInterpreterSession classname='Bool'>
																				<value>false</value>
																			</UseAdapterSettingsForInterpreterSession>
																			<InterpreterSessionScope classname='Num'>
																				<value>2</value>
																			</InterpreterSessionScope>
																			<PythonVersion classname='Str'>
																				<value>3.10</value>
																			</PythonVersion>
																			<PythonVirtualEnvironmentPath classname='Str'>
																				<value>.venv</value>
																			</PythonVirtualEnvironmentPath>
																			<InterpreterLocation classname='ExprValue'>
																				<value/>
																			</InterpreterLocation>
																			<CreateIfInterpreterDoesNotExist classname='Bool'>
																				<value>true</value>
																			</CreateIfInterpreterDoesNotExist>
																			<ModulePath classname='PathValue'>
																				<value>teststand_nidmm.py</value>
																			</ModulePath>
																			<OperationType classname='Num'>
																				<value>1</value>
																			</OperationType>
																			<OperationScope classname='Num'>
																				<value>0</value>
																			</OperationScope>
																			<ClassName classname='Str'>
																				<value/>
																			</ClassName>
																			<ClassInstanceLocation classname='ExprValue'>
																				<value/>
																			</ClassInstanceLocation>
																			<FunctionOrAttributeName classname='Str'>
																				<value>destroy_nidmm_sessions</value>
																			</FunctionOrAttributeName>
																			<Parameters classname='Objs'>
																				<value lbound='[0]' ubound='[0]'>
																					<elemproto>
																						<_NAME_IN_ATTRIBUTE_ name='' classname='CPythonParameter' structureflags='0'/>
																					</elemproto>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>Return Value</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value/>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																				</value>
																			</Parameters>
																			<DefaultParamCategoryForArray classname='Num'>
																				<value>5</value>
																			</DefaultParamCategoryForArray>
																		</subprops>
																	</PythonCall>
																</subprops>
															</SData>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>0</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
												</subprops>
											</Step>
										</value>
									</value>
								</Cleanup>
								<RecordResults classname='Bool' valueflags='4194312'>
									<value>true</value>
								</RecordResults>
								<RTS classname='Obj' valueflags='4456456'>
									<subprops>
										<Type classname='Num' valueflags='4194304'>
											<value>0</value>
										</Type>
										<OptimizeNonReentrantCalls classname='Bool' valueflags='4194304'>
											<value>true</value>
										</OptimizeNonReentrantCalls>
										<EPNameExpr classname='Str' valueflags='4194304'>
											<value>"Unnamed Entry Point"</value>
										</EPNameExpr>
										<EPEnabledExpr classname='Str' valueflags='4194304'>
											<value>True</value>
										</EPEnabledExpr>
										<EPMenuHint classname='Str' valueflags='4194304'>
											<value/>
										</EPMenuHint>
										<EPIgnoreClient classname='Bool' valueflags='4194304'>
											<value>false</value>
										</EPIgnoreClient>
										<EPInitiallyHidden classname='Bool' valueflags='4194304'>
											<value>false</value>
										</EPInitiallyHidden>
										<EPCheckToSaveTitledFile classname='Bool' valueflags='4194304'>
											<value>true</value>
										</EPCheckToSaveTitledFile>
										<ShowEPAlways classname='Bool' valueflags='4194304'>
											<value>false</value>
										</ShowEPAlways>
										<ShowEPForFileWin classname='Bool' valueflags='4194304'>
											<value>true</value>
										</ShowEPForFileWin>
										<ShowEPForExeWin classname='Bool' valueflags='4194304'>
											<value>false</value>
										</ShowEPForExeWin>
										<ShowEPForEditorOnly classname='Bool' valueflags='4194304'>
											<value>false</value>
										</ShowEPForEditorOnly>
										<AllowIntExeOfEP classname='Bool' valueflags='4194304'>
											<value>false</value>
										</AllowIntExeOfEP>
										<CopyStepsOnOverriding classname='Bool' valueflags='4194304'>
											<value>true</value>
										</CopyStepsOnOverriding>
										<Priority classname='Num' valueflags='4194304'>
											<value>2953567917</value>
										</Priority>
									</subprops>
								</RTS>
								<Requirements classname='Obj' valueflags='4456456'>
									<subprops>
										<Links classname='Strs' valueflags='71303168'>
											<value lbound='[0]' ubound='[]'/>
										</Links>
									</subprops>
								</Requirements>
								<FailureAction classname='Num' valueflags='4194312'>
									<value>2</value>
								</FailureAction>
							</subprops>
						</Sequence>
					</value>
				</value>
			</Seq>
			<FileGlobalDefaults classname='Obj' valueflags='4194304'>
				<subprops>
					<MeasurementPlugIns classname='Obj'>
						<subprops>
							<EnableMonitoring classname='Bool'>
								<value>false</value>
							</EnableMonitoring>
						</subprops>
					</MeasurementPlugIns>
				</subprops>
			</FileGlobalDefaults>
			<ModelFile typename='Path' xsi:type='Path' classname='PathValue' valueflags='4194312'>
				<value/>
			</ModelFile>
			<LoadOpt classname='Str' valueflags='4194312'>
				<value>UseStepLoadOpt</value>
			</LoadOpt>
			<UnloadOpt classname='Str' valueflags='4194312'>
				<value>UseStepUnloadOpt</value>
			</UnloadOpt>
			<Version classname='Str' valueflags='4194312'>
				<value>0.0.0.0</value>
			</Version>
			<BatchSync classname='Num' valueflags='4194312'>
				<value>1</value>
			</BatchSync>
			<SFGlobalsScope classname='Num' valueflags='4194312'>
				<value>0</value>
			</SFGlobalsScope>
			<Type classname='Num' valueflags='4194312'>
				<value>0</value>
			</Type>
			<ModelOption classname='Num' valueflags='4194312'>
				<value>0</value>
			</ModelOption>
			<Requirements classname='Obj' valueflags='4194305'>
				<subprops>
					<Links classname='Strs' valueflags='71303168'>
						<value lbound='[0]' ubound='[]'/>
					</Links>
				</subprops>
			</Requirements>
		</subprops>
	</Data>
</teststandfileheader>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidmm_measurement/poetry.toml sha256=ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e bytes=34 -->
## FILE: examples/nidmm_measurement/poetry.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidmm_measurement/poetry.toml`
- sha256: `ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e`
- bytes: 34

````toml
[virtualenvs]
in-project = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidmm_measurement/pyproject.toml sha256=8ef874175dd6168e4460bcd70b71aa0467f9eb2bf4544a72253b5aa87bbb1062 bytes=1084 -->
## FILE: examples/nidmm_measurement/pyproject.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidmm_measurement/pyproject.toml`
- sha256: `8ef874175dd6168e4460bcd70b71aa0467f9eb2bf4544a72253b5aa87bbb1062`
- bytes: 1084

````toml
[tool.poetry]
name = "nidmm_measurement"
version = "0.5.0"
package-mode = false
description = "Measurement plug-in example that performs a measurement using an NI DMM."
authors = ["National Instruments"]

[tool.poetry.dependencies]
python = "^3.10"
nidmm = { version = ">=1.4.4", extras = ["grpc"] }
ni-measurement-plugin-sdk-service = {version = ">=2.3.1,<4.0"}
click = ">=7.1.2, !=8.1.4" # mypy fails with click 8.1.4: https://github.com/pallets/click/issues/2558
grpcio = "*"

[tool.poetry.group.dev.dependencies]
ni-python-styleguide = ">=0.4.1"
mypy = ">=1.0"
types-grpcio = ">=1.0"
# Uncomment to use prerelease dependencies.
# nidmm = { git = "https://github.com/ni/nimi-python.git", subdirectory = "generated/nidmm", extras = ["grpc"] }
# ni-measurement-plugin-sdk-service = {path = "../../packages/service", develop = true}

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.mypy]
disallow_untyped_defs = true

[[tool.mypy.overrides]]
module = [
    "nidmm.*",
]
ignore_missing_imports = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidmm_measurement/README.md sha256=83b1f13d5803e112076a7fa1641bda05fc54bf8136e8656d2fc453441e614cac bytes=1854 -->
## FILE: examples/nidmm_measurement/README.md

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidmm_measurement/README.md`
- sha256: `83b1f13d5803e112076a7fa1641bda05fc54bf8136e8656d2fc453441e614cac`
- bytes: 1854

````markdown
## NI-DMM Measurement

This is a measurement plug-in example that performs a measurement using an NI DMM.

### Features

- Uses the `nidmm` package to access NI-DMM from Python
- Pin-aware, supporting one session, one pin, and one selected site
- Includes InstrumentStudio and Measurement Plug-In UI Editor project files
- Includes a TestStand sequence showing how to configure the pin map, register
  instrument sessions with the session management service, and run a measurement
  - For the sake of simplicity, the TestStand sequence handles pin map and
    session registration and unregistration in the `Setup` and `Cleanup`
    sections of the main sequence. For **Test UUTs** and batch process model use
    cases, these steps should be moved to the `ProcessSetup` and
    `ProcessCleanup` callbacks.
- Uses the NI gRPC Device Server to allow sharing instrument sessions with other
  measurement services when running measurements from TestStand

### Required Software

- InstrumentStudio 2025 Q1 or later
- NI-DMM
- Recommended: TestStand 2021 SP1 or later

### Required Hardware

This example requires an NI DMM (e.g. PXIe-4081).

By default, this example uses a physical instrument or a simulated instrument
created in NI MAX. To automatically simulate an instrument without using NI MAX,
follow the steps below:
- Create a `.env` file in the measurement service's directory or one of its
  parent directories (such as the root of your Git repository or
  `C:\ProgramData\National Instruments\Plug-Ins\Measurements` for statically
  registered measurement services).
- Add the following options to the `.env` file to enable simulation via the
  driver's option string:

  ```
  MEASUREMENT_PLUGIN_NIDMM_SIMULATE=1
  MEASUREMENT_PLUGIN_NIDMM_BOARD_TYPE=PXIe
  MEASUREMENT_PLUGIN_NIDMM_MODEL=4081
  ```
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidmm_measurement/start.bat sha256=bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851 bytes=253 -->
## FILE: examples/nidmm_measurement/start.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidmm_measurement/start.bat`
- sha256: `bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851`
- bytes: 253

````batch
@echo off
REM The discovery service uses this script to start the measurement service.
REM You can customize this script for your Python setup. The -v option logs
REM messages with level INFO and above.

.venv\Scripts\python.exe measurement.py -v
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nidmm_measurement/teststand_nidmm.py sha256=ac976433d7cbac4fa5ae2d55a9704e439bc486837ee87ebc6fd2ad5159a07ec2 bytes=2585 -->
## FILE: examples/nidmm_measurement/teststand_nidmm.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nidmm_measurement/teststand_nidmm.py`
- sha256: `ac976433d7cbac4fa5ae2d55a9704e439bc486837ee87ebc6fd2ad5159a07ec2`
- bytes: 2585

````python
"""Functions to set up and tear down sessions of NI-DMM devices in NI TestStand."""

from typing import Any

from _helpers import TestStandSupport
from ni_measurement_plugin_sdk_service.discovery import DiscoveryClient
from ni_measurement_plugin_sdk_service.grpc.channelpool import GrpcChannelPool
from ni_measurement_plugin_sdk_service.session_management import (
    INSTRUMENT_TYPE_NI_DMM,
    PinMapContext,
    SessionInitializationBehavior,
    SessionManagementClient,
)


def create_nidmm_sessions(sequence_context: Any) -> None:
    """Create and register all NI-DMM sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    """
    with GrpcChannelPool() as grpc_channel_pool:
        teststand_support = TestStandSupport(sequence_context)
        pin_map_id = teststand_support.get_active_pin_map_id()
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=None)

        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )

        with session_management_client.reserve_sessions(
            pin_map_context, instrument_type_id=INSTRUMENT_TYPE_NI_DMM
        ) as reservation:
            with reservation.initialize_nidmm_sessions(
                initialization_behavior=SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH
            ):
                pass

            session_management_client.register_sessions(reservation.session_info)


def destroy_nidmm_sessions() -> None:
    """Destroy and unregister all NI-DMM sessions."""
    with GrpcChannelPool() as grpc_channel_pool:
        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with session_management_client.reserve_all_registered_sessions(
            instrument_type_id=INSTRUMENT_TYPE_NI_DMM,
        ) as reservation:
            if not reservation.session_info:
                return

            session_management_client.unregister_sessions(reservation.session_info)
            with reservation.initialize_nidmm_sessions(
                initialization_behavior=SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE
            ):
                pass
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nifgen_standard_function/.serviceignore sha256=997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912 bytes=148 -->
## FILE: examples/nifgen_standard_function/.serviceignore

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nifgen_standard_function/.serviceignore`
- sha256: `997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912`
- bytes: 148

````text
# This file specifies that when we publish this plug-in to a plug-in library,
# we should not copy the following directories:
.venv
__pycache__
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nifgen_standard_function/_helpers.py sha256=0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426 bytes=2920 -->
## FILE: examples/nifgen_standard_function/_helpers.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nifgen_standard_function/_helpers.py`
- sha256: `0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426`
- bytes: 2920

````python
"""Helper classes and functions for measurement plug-in examples."""

from __future__ import annotations

import logging
import pathlib
from typing import Any, Callable, TypeVar

import click


class TestStandSupport:
    """Class that communicates with TestStand."""

    _PIN_MAP_ID_VAR = "NI.MeasurementPlugIns.PinMapId"

    def __init__(self, sequence_context: Any) -> None:
        """Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        """
        self._sequence_context = sequence_context

    def get_active_pin_map_id(self) -> str:
        """Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        """
        run_time_variables = self._sequence_context.Execution.RunTimeVariables
        if not run_time_variables.Exists(self._PIN_MAP_ID_VAR, 0x0):
            return ""
        return run_time_variables.GetValString(self._PIN_MAP_ID_VAR, 0x0)

    def resolve_file_path(self, file_path: str) -> str:
        """Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        """
        if pathlib.Path(file_path).is_absolute():
            return file_path
        (_, absolute_path, _, _, user_canceled) = self._sequence_context.Engine.FindFileEx(
            fileToFind=file_path,
            absolutePath=None,
            srchDirType=None,
            searchDirectoryIndex=None,
            userCancelled=None,  # Must match spelling used by TestStand
            searchContext=self._sequence_context.SequenceFile,
        )
        if user_canceled:
            raise RuntimeError("File lookup canceled by user.")
        return absolute_path


def configure_logging(verbosity: int) -> None:
    """Configure logging for this process."""
    if verbosity > 1:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=level)


F = TypeVar("F", bound=Callable)


def verbosity_option(func: F) -> F:
    """Decorator for --verbose command line option."""
    return click.option(
        "-v",
        "--verbose",
        "verbosity",
        count=True,
        help="Enable verbose logging. Repeat to increase verbosity.",
    )(func)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nifgen_standard_function/install.bat sha256=695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025 bytes=205 -->
## FILE: examples/nifgen_standard_function/install.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nifgen_standard_function/install.bat`
- sha256: `695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025`
- bytes: 205

````batch
@echo off
REM The discovery service uses this script to install the dependencies
REM for the measurement service. You can customize this script for your
REM Python setup.

poetry install --only main
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nifgen_standard_function/measurement.py sha256=ad28ff1d77f71b1a2e989a9cbfcee68e68f48624136cf246f2ea4067d0d2b358 bytes=6412 -->
## FILE: examples/nifgen_standard_function/measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nifgen_standard_function/measurement.py`
- sha256: `ad28ff1d77f71b1a2e989a9cbfcee68e68f48624136cf246f2ea4067d0d2b358`
- bytes: 6412

````python
"""Generate a standard function waveform using an NI waveform generator."""

import logging
import pathlib
import sys
import threading
import time
from collections.abc import Iterable, Sequence
from contextlib import ExitStack
from enum import Enum

import click
import grpc
import hightime
import ni_measurement_plugin_sdk_service as nims
import nifgen
from _helpers import configure_logging, verbosity_option

_NIFGEN_OPERATION_TIMED_OUT_ERROR_CODE = -1074098044
_NIFGEN_MAX_TIME_EXCEEDED_ERROR_CODE = -1074118637
_NIFGEN_TIMEOUT_ERROR_CODES = [
    _NIFGEN_OPERATION_TIMED_OUT_ERROR_CODE,
    _NIFGEN_MAX_TIME_EXCEEDED_ERROR_CODE,
]

script_or_exe = sys.executable if getattr(sys, "frozen", False) else __file__
service_directory = pathlib.Path(script_or_exe).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "NIFgenStandardFunction.serviceconfig",
    ui_file_paths=[service_directory / "NIFgenStandardFunction.measui"],
)


class Waveform(Enum):
    """Wrapper enum that contains a zero value."""

    NONE = 0
    SINE = nifgen.Waveform.SINE.value
    SQUARE = nifgen.Waveform.SQUARE.value
    TRIANGLE = nifgen.Waveform.TRIANGLE.value
    RAMP_UP = nifgen.Waveform.RAMP_UP.value
    RAMP_DOWN = nifgen.Waveform.RAMP_DOWN.value
    DC = nifgen.Waveform.DC.value
    NOISE = nifgen.Waveform.NOISE.value
    USER = nifgen.Waveform.USER.value


@measurement_service.register_measurement
@measurement_service.configuration(
    "pin_names",
    nims.DataType.IOResourceArray1D,
    ["Pin1"],
    instrument_type=nims.session_management.INSTRUMENT_TYPE_NI_FGEN,
)
@measurement_service.configuration(
    "waveform_type", nims.DataType.Enum, Waveform.SINE, enum_type=Waveform
)
@measurement_service.configuration("frequency", nims.DataType.Double, 1.0e6)
@measurement_service.configuration("amplitude", nims.DataType.Double, 2.0)
@measurement_service.configuration("duration", nims.DataType.Double, 10.0)
def measure(
    pin_names: Iterable[str],
    waveform_type: Waveform,
    frequency: float,
    amplitude: float,
    duration: float,
) -> tuple[()]:
    """Generate a standard function waveform using an NI waveform generator."""
    logging.info(
        "Starting generation: pin_names=%s waveform_type=%s frequency=%g amplitude=%g",
        pin_names,
        waveform_type,
        frequency,
        amplitude,
    )

    cancellation_event = threading.Event()
    measurement_service.context.add_cancel_callback(cancellation_event.set)

    # If the waveform type is not specified, use SINE.
    nifgen_waveform = nifgen.Waveform(waveform_type.value or Waveform.SINE.value)

    with measurement_service.context.reserve_sessions(pin_names) as reservation:
        with reservation.initialize_nifgen_sessions() as session_infos:
            for session_info in session_infos:
                # Output mode must be the same for all channels in the session.
                session_info.session.output_mode = nifgen.OutputMode.FUNC

                # Configure the same waveform settings for all channels
                # corresponding to the selected pins and sites.
                channels = session_info.session.channels[session_info.channel_list]
                channels.configure_standard_waveform(nifgen_waveform, amplitude, frequency)

            with ExitStack() as stack:
                # Initiate the generation for all sessions. initiate() returns a
                # context manager that aborts the generation when the function
                # returns or raises an exception. Use an ExitStack to manage
                # multiple context managers.
                for session_info in session_infos:
                    stack.enter_context(session_info.session.initiate())

                # Wait until the generation is done.
                sessions = [session_info.session for session_info in session_infos]
                _wait_until_done(sessions, cancellation_event, duration)

    logging.info("Completed generation")
    return ()


def _wait_until_done(
    sessions: Sequence[nifgen.Session], cancellation_event: threading.Event, duration: float
) -> None:
    """Wait until all sessions are done, the duration expires, or error/cancellation occurs.

    Note that ``duration`` is a minimum time, not a timeout.
    """
    is_simulated = any(session.simulate for session in sessions)
    grpc_deadline = time.time() + measurement_service.context.time_remaining
    stop_time = time.time() + duration

    while True:
        if time.time() >= stop_time:
            break
        if time.time() > grpc_deadline:
            measurement_service.context.abort(
                grpc.StatusCode.DEADLINE_EXCEEDED, "Deadline exceeded."
            )
        if cancellation_event.is_set():
            measurement_service.context.abort(
                grpc.StatusCode.CANCELLED, "Client requested cancellation."
            )

        if is_simulated:
            # With simulated NI-FGEN instruments, wait_for_done() succeeds
            # immediately, so use time.sleep() instead.
            remaining_time = max(stop_time - time.time(), 0.0)
            sleep_time = min(remaining_time, 100e-3)
            time.sleep(sleep_time)
        else:
            # Wait until all sessions are done. If any session takes more than
            # 100 ms, check for cancellation and try again. NI-FGEN does not
            # support canceling a call to wait_until_done().
            try:
                for session in sessions:
                    remaining_time = max(stop_time - time.time(), 0.0)
                    sleep_time = min(remaining_time, 100e-3)
                    session.wait_until_done(hightime.timedelta(seconds=sleep_time))
                break
            except nifgen.errors.DriverError as e:
                if e.code in _NIFGEN_TIMEOUT_ERROR_CODES:
                    pass
                raise


@click.command
@verbosity_option
def main(verbosity: int) -> None:
    """Generate a standard function waveform using an NI waveform generator."""
    configure_logging(verbosity)

    with measurement_service.host_service():
        input("Press enter to close the measurement service.\n")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nifgen_standard_function/NIFgenStandardFunction.instudioproj sha256=b55c38aa5b65a016a34023b3181341469fad77fd0ec47a296e23dfda4db97d6a bytes=2035 -->
## FILE: examples/nifgen_standard_function/NIFgenStandardFunction.instudioproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nifgen_standard_function/NIFgenStandardFunction.instudioproj`
- sha256: `b55c38aa5b65a016a34023b3181341469fad77fd0ec47a296e23dfda4db97d6a`
- bytes: 2035

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="636B8A4121891ADC7E9326C85B7BA9115C479129BA233433D379D25F66AFE0F147AA94F3B1EC0EF0B2C517D86974D6C2EEA61674398978CE1C7FE354FD8D6AAA" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.0.0.2317" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2317" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.2317" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="23.0.0.2317" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="f53d543da7be447d977505512a9de1b1" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="7a73cec96722445aaeae940b880f627c" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="f0fd0a1d98c944258fd0797c80775378" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<FileReference Id="799eacc860914f69ba775aec1c9820ef" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="NIFgenStandardFunction.pinmap" StoragePath="NIFgenStandardFunction.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
			<SourceFileReference Bindings="EnvoyManager" Id="36d52064253b4c64b0eeb878b074e26f" ModelDefinitionType="NationalInstruments.InstrumentFramework.Document.SourceModel.UnifiedTask" Name="NIFgenStandardFunction.sfp" StoragePath="NIFgenStandardFunction.sfp" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nifgen_standard_function/NIFgenStandardFunction.measproj sha256=40aede837cc32069175ac6d97be916420aa2d9d512c44fdc1e76cd2d680bb7bf bytes=3824 -->
## FILE: examples/nifgen_standard_function/NIFgenStandardFunction.measproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nifgen_standard_function/NIFgenStandardFunction.measproj`
- sha256: `40aede837cc32069175ac6d97be916420aa2d9d512c44fdc1e76cd2d680bb7bf`
- bytes: 3824

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="FBC04D75D4D2CAC863C0EB80488EA67C2DB9960F527CB8C1E2DD2F6D67BBD596DAE89682B28480DADAF71CBF38678D8817061B40730F018D56BFFD03DF9BCEA6" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.0.0.1849" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="23.0.0.1849" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.1849" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.1849" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/EnvoyManagement" OldestCompatibleVersion="5.0.0.0" Version="5.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.1849" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemDiagram" OldestCompatibleVersion="8.0.0.49152" Version="8.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.1849" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemModelCore" OldestCompatibleVersion="5.1.0.5" Version="5.2.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.1849" Name="MeasurementLink UI Editor" Version="23.0.0.1849" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="da4cd1d914354e11b0387be34f755295" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="c39e3701f5824cb0a30e9c9a09a23568" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<EmbeddedDefinitionReference Id="edc367d7e4d64f6d8bbb1ba36e4eb8d3" ModelDefinitionType="NationalInstruments.SystemDesigner.SystemDiagram.SystemDiagramDefinition" Name="SystemDiagram">
			<SystemDiagram Id="f37e9886becf42e2a815979184f4ab74" SystemDiagramVersion="75" xmlns="http://www.ni.com/SystemDesigner/SystemDiagram">
				<EnvoySuperimpositionContainer Id="3ef9e64774f644eebcc66017e48a9953" xmlns="http://www.ni.com/SystemDesigner/EnvoyManagement">
					<MappingManager Id="e2c493594e634c77ab11a9938a4f77eb" xmlns="http://www.ni.com/SystemDesigner/SystemModelCore">
						<Superimposition Id="df479caae2f24111a03677af1f5f7b1b" Name="Root Superimposition" />
					</MappingManager>
				</EnvoySuperimpositionContainer>
				<SystemDiagramRootDiagram Id="2e5335977053482e88426c43c4a8379c" />
			</SystemDiagram>
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="686ec28c706b4a57b4278e1071f9c4d1" ModelDefinitionType="NullTarget" Name="NullTarget">
			<NullTarget />
		</NameScopingEnvoy>
		<NameScopingEnvoy Id="d97e60887a849da82595650ae900c59" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Id="e0c4551d76cb4ce6ad71ae6b0f04668b" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="NIFgenStandardFunction.measui" StoragePath="NIFgenStandardFunction.measui" />
			<FileReference Id="591bb4a8d9304ab7b26a3ff2d0d3dcca" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="NIFgenStandardFunction.pinmap" StoragePath="NIFgenStandardFunction.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nifgen_standard_function/NIFgenStandardFunction.measui sha256=dd06f39018b4ea86261cd76dc2f1e96195e6c60e02870d6993c47e92ef5b1c45 bytes=8384 -->
## FILE: examples/nifgen_standard_function/NIFgenStandardFunction.measui

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nifgen_standard_function/NIFgenStandardFunction.measui`
- sha256: `dd06f39018b4ea86261cd76dc2f1e96195e6c60e02870d6993c47e92ef5b1c45`
- bytes: 8384

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="BF94D2CD368F1551E6A109189326013E7DBD55F5499D5BBAE7C98DC11B51A94780EAB8EBA0A3613EA3933FFD38BEDFF38CCD9B37DC5D5AA31346E1DFE36C40DF" Timestamp="1DA7511060DA6E7" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.11.0.49428" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="9.8.1.49152" />
		<ParsableNamespace AssemblyFileVersion="9.11.0.49428" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="24.0.0.49428" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.11.0.49428" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.11.0.49428" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="24.0.0.49428" Name="MeasurementLink UI Editor" Version="24.0.0.49428" />
	</SourceModelFeatureSet>
	<Screen ClientId="{782d1b4c-4bb0-4fee-b195-03544d32de7c}" DisplayName="NI-FGEN Standard Function (Py)" Id="4e74a15e122740b596612afe9f35308c" ServiceClass="ni.examples.NIFgenStandardFunction_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
		<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]450" Id="625f0974374047b2bc643babf49a74e5" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]270" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
			<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BaseName="[string]Canvas" Height="[float]194" Id="9d7236c231a4412cb3c46bb2b395e0f0" Label="[UIModel]cb2217f529d84fb2b1017f06e1eb3ed8" Left="[float]16" Top="[float]89" Width="[float]235">
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{782d1b4c-4bb0-4fee-b195-03544d32de7c}/Configuration/frequency" Enabled="[bool]True" Height="[float]24" Id="84be291b24b54f34b65a3afae7435a55" IsLabelBoundToChannel="[bool]False" Label="[UIModel]ec6cc654896a476d9cf9a69516049715" Left="[float]17" RadixBase="[RadixBase]0" RadixVisibility="[SMVisibility]Collapsed" Top="[float]95" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=SystemInternational:Digits=5:DigitDisplayType=SignificantDigits:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{782d1b4c-4bb0-4fee-b195-03544d32de7c}/Configuration/amplitude" Enabled="[bool]True" Height="[float]24" Id="32b1ec08610c44dba09e9fe6b14e2caf" IsLabelBoundToChannel="[bool]False" Label="[UIModel]987157f6aba7443abfa6f48f5e7597b6" Left="[float]17" Top="[float]155" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=2:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
				<Label Height="[float]16" Id="ec6cc654896a476d9cf9a69516049715" LabelOwner="[UIModel]84be291b24b54f34b65a3afae7435a55" Left="[float]17" Text="[string]Frequency (Hz)" Top="[float]75" Width="[float]80" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="987157f6aba7443abfa6f48f5e7597b6" LabelOwner="[UIModel]32b1ec08610c44dba09e9fe6b14e2caf" Left="[float]17" Text="[string]Amplitude (V)" Top="[float]135" Width="[float]73" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{782d1b4c-4bb0-4fee-b195-03544d32de7c}/Configuration/waveform_type" Enabled="[bool]True" Height="[float]24" Id="4344d2c6994d4a90a5ad6cd85287b94f" IsLabelBoundToChannel="[bool]False" Label="[UIModel]e8bb70bf42c4ca28559ef5bdf1b4b48" Left="[float]17" Top="[float]35" Value="[int]1" Width="[float]136" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
					<RingSelectorInfo DisplayValue="[string]NONE" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]SINE" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]SQUARE" IsEnabled="[bool]True" Value="[int]2" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]TRIANGLE" IsEnabled="[bool]True" Value="[int]3" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]RAMP_UP" IsEnabled="[bool]True" Value="[int]4" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]RAMP_DOWN" IsEnabled="[bool]True" Value="[int]5" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]DC" IsEnabled="[bool]True" Value="[int]6" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]NOISE" IsEnabled="[bool]True" Value="[int]101" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]USER" IsEnabled="[bool]True" Value="[int]102" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</ChannelEnumSelector>
				<Label Height="[float]16" Id="e8bb70bf42c4ca28559ef5bdf1b4b48" LabelOwner="[UIModel]4344d2c6994d4a90a5ad6cd85287b94f" Left="[float]17" Text="[string]Waveform type" Top="[float]15" Width="[float]81" xmlns="http://www.ni.com/PanelCommon" />
			</ScreenSurfaceCanvas>
			<Label Height="[float]16" Id="cb2217f529d84fb2b1017f06e1eb3ed8" LabelOwner="[UIModel]9d7236c231a4412cb3c46bb2b395e0f0" Left="[float]16" Text="[string]Waveform" Top="[float]69" Width="[float]56" xmlns="http://www.ni.com/PanelCommon" />
			<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BaseName="[string]Canvas" Height="[float]78" Id="4c70df2eda7f4028ab09f2f5161c11c3" Label="[UIModel]baf1504130a5409a8e3970f76111e2a8" Left="[float]16" Top="[float]318" Width="[float]235">
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{782d1b4c-4bb0-4fee-b195-03544d32de7c}/Configuration/duration" Enabled="[bool]True" Height="[float]24" Id="c2b1de59a7c344f680a0f3d6811fa3ba" IsLabelBoundToChannel="[bool]False" Label="[UIModel]e4a9dee5b67f4a7898c643c0dfb2cc08" Left="[float]17" Top="[float]35" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]70" />
				<Label Height="[float]16" Id="e4a9dee5b67f4a7898c643c0dfb2cc08" LabelOwner="[UIModel]c2b1de59a7c344f680a0f3d6811fa3ba" Left="[float]17" Text="[string]Duration (s)" Top="[float]15" Width="[float]63" xmlns="http://www.ni.com/PanelCommon" />
			</ScreenSurfaceCanvas>
			<Label Height="[float]16" Id="baf1504130a5409a8e3970f76111e2a8" LabelOwner="[UIModel]4c70df2eda7f4028ab09f2f5161c11c3" Left="[float]16" Text="[string]Execution" Top="[float]298" Width="[float]52" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{782d1b4c-4bb0-4fee-b195-03544d32de7c}/Configuration/pin_names" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="66db519df5724b6abe32b6cb766d6952" IsLabelBoundToChannel="[bool]False" Label="[UIModel]95d399ecd74544039046fa6b09fb64ce" Left="[float]17" MultipleSelectionMode="[MultipleSelectionModes]List" SelectedResource="[NI_Core_DataValues_TagRefnum]Pin1" Top="[float]35" Width="[float]136" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
			<Label Height="[float]16" Id="95d399ecd74544039046fa6b09fb64ce" LabelOwner="[UIModel]66db519df5724b6abe32b6cb766d6952" Left="[float]17" Text="[string]Pin names" Top="[float]15" Width="[float]55" xmlns="http://www.ni.com/PanelCommon" />
		</ScreenSurface>
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nifgen_standard_function/NIFgenStandardFunction.pinmap sha256=364bfd912753d983db78483c6d0bc4dfacf003d152a4b3348b8a27e844447010 bytes=521 -->
## FILE: examples/nifgen_standard_function/NIFgenStandardFunction.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nifgen_standard_function/NIFgenStandardFunction.pinmap`
- sha256: `364bfd912753d983db78483c6d0bc4dfacf003d152a4b3348b8a27e844447010`
- bytes: 521

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.1">
	<Instruments>
		<NIFGenInstrument name="FGEN1" numberOfChannels="1" />
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="FGEN1" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nifgen_standard_function/NIFgenStandardFunction.serviceconfig sha256=1fde35f91e3f234e26815b3391a9487a18cba4e5dcb22f62568a2b6b7fbd3a22 bytes=712 -->
## FILE: examples/nifgen_standard_function/NIFgenStandardFunction.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nifgen_standard_function/NIFgenStandardFunction.serviceconfig`
- sha256: `1fde35f91e3f234e26815b3391a9487a18cba4e5dcb22f62568a2b6b7fbd3a22`
- bytes: 712

````json
{
  "services": [
    {
      "displayName": "NI-FGEN Standard Function (Py)",
      "version": "1.0.0",
      "serviceClass": "ni.examples.NIFgenStandardFunction_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "installPath": "install.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in example that generates a standard function waveform using an NI waveform generator.",
        "ni/service.collection": "NI.Examples",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nifgen_standard_function/NIFgenStandardFunction.sfp sha256=fd2e240a605354d02ad908bf63ee7385a6bef47d2c86f4f8cae7de65fb32e04c bytes=11492 -->
## FILE: examples/nifgen_standard_function/NIFgenStandardFunction.sfp

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nifgen_standard_function/NIFgenStandardFunction.sfp`
- sha256: `fd2e240a605354d02ad908bf63ee7385a6bef47d2c86f4f8cae7de65fb32e04c`
- bytes: 11492

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="8ECA1E17406EB0CABDF36648DE9FF6C640878C464E32B1D5C35D1129547436437E2FD90E2E28036C962D805CC3DDD49279408FF69DB602BCE4B1378742A7BBCD" Timestamp="1DA75113C07929E" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.11.0.49428" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="9.8.1.49152" />
		<ParsableNamespace AssemblyFileVersion="9.11.0.49505" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="24.0.0.49505" FeatureSetName="UnifiedTask" Name="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" Version="1.0.0.0" />
		<ParsableNamespace AssemblyFileVersion="24.0.0.49428" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.11.0.49505" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.11.0.49505" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="24.0.0.49505" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="24.0.0.49505" />
	</SourceModelFeatureSet>
	<UnifiedTask Id="41898a52ae884eb8af51c8df4504c7d6" LayoutInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Layout Information&quot;:{&quot;Sections&quot;:[{&quot;Columns Progressive Count&quot;:1,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Columns&quot;:[{&quot;Containers Progressive Count&quot;:1,&quot;Layout Information Index&quot;:0,&quot;Containers&quot;:[{&quot;Container Model Defition&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Container Assignment State&quot;:&quot;Available&quot;,&quot;Container Identifier&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen.task&quot;,&quot;Container Instrument Name&quot;:&quot;NI-FGEN Standard Function (Py)&quot;,&quot;Layout Information Name&quot;:&quot;NI-FGEN Standard Function (Py) 1&quot;,&quot;Layout Information Index&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Items&quot;:[{&quot;Identification Number&quot;:4294963201,&quot;Model Definition Type&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Parent Or Group Name&quot;:&quot;Measurements&quot;,&quot;Panel Type&quot;:&quot;NI-FGEN Standard Function (Py)&quot;,&quot;Layout Information Name&quot;:&quot;ni.examples.NIFgenStandardFunction_Python&quot;,&quot;Layout Information Index&quot;:0}]}]}]},{&quot;Columns Progressive Count&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationOnly&quot;}]}}" PinAwareInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Selected Sites&quot;:[{&quot;Site Number&quot;:0}]}" xmlns="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" />
	<EnvoyManagerFile Id="4cd30de369664227ab3afad8d8faba29" xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="9df76e6a92bc42cbb28c6dc3011a53b3" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<NameScopingEnvoy AutomaticallyResolveUp="True" Id="851d1f6a731c470d82bb6d26596887c7" Name="NIFgenStandardFunction.sfp" NameTracksFileName="True" />
		<EmbeddedDefinitionReference Id="bef04a82754e49439773c620e24159e0" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="{http\://www.ni.com/InstrumentFramework/ScreenDocument}Screen.task">
			<Screen ClientId="{77b83973-0d6a-48d0-8612-4f61bc92e844}" ConfigurationParameters="{&quot;@type&quot;:&quot;type.googleapis.com/ni.measurementlink.measurement.v2.MeasurementConfigurations&quot;,&quot;pinNames&quot;:[&quot;Pin1&quot;],&quot;waveformType&quot;:1,&quot;frequency&quot;:1000000.0,&quot;amplitude&quot;:2.0,&quot;duration&quot;:10.0}" DisplayName="NI-FGEN Standard Function (Py)" Id="b2ac1f48e1334e13ae0eff27a2fb2d6d" PanelPresentation="ConfigurationWithVisualization" ServiceClass="ni.examples.NIFgenStandardFunction_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
				<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]450" Id="68d7fa38e5a0493da1ccca1745af4fd3" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]270" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
					<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BaseName="[string]Canvas" Height="[float]194" Id="2ffdcdb273fe4862be3202e131f03c97" Label="[UIModel]71f1cdbbfff74b2288e50335e2febe5a" Left="[float]16" Top="[float]89" Width="[float]235">
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{77b83973-0d6a-48d0-8612-4f61bc92e844}/Configuration/frequency" Enabled="[bool]True" Height="[float]24" Id="c4fdeab37cd74a77968739bcac528aa7" IsLabelBoundToChannel="[bool]False" Label="[UIModel]186f69f4bb0247a2aa10777aa516e7b2" Left="[float]17" RadixBase="[RadixBase]0" RadixVisibility="[SMVisibility]Collapsed" Top="[float]95" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=SystemInternational:Digits=5:DigitDisplayType=SignificantDigits:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{77b83973-0d6a-48d0-8612-4f61bc92e844}/Configuration/amplitude" Enabled="[bool]True" Height="[float]24" Id="91e8c6fd4984e0499993ebc5be258c1" IsLabelBoundToChannel="[bool]False" Label="[UIModel]4f8a2b2e67c447368e2d43f00a18b4a2" Left="[float]17" Top="[float]155" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=2:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
						<Label Height="[float]16" Id="186f69f4bb0247a2aa10777aa516e7b2" LabelOwner="[UIModel]c4fdeab37cd74a77968739bcac528aa7" Left="[float]17" Text="[string]Frequency (Hz)" Top="[float]75" Width="[float]80" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="4f8a2b2e67c447368e2d43f00a18b4a2" LabelOwner="[UIModel]91e8c6fd4984e0499993ebc5be258c1" Left="[float]17" Text="[string]Amplitude (V)" Top="[float]135" Width="[float]73" xmlns="http://www.ni.com/PanelCommon" />
						<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{77b83973-0d6a-48d0-8612-4f61bc92e844}/Configuration/waveform_type" Enabled="[bool]True" Height="[float]24" Id="7f260a0fb0264525bf6fe93386a70475" IsLabelBoundToChannel="[bool]False" Label="[UIModel]c37d811a42074f978d66f5a4eabb0a1b" Left="[float]17" Top="[float]35" Value="[int]1" Width="[float]136" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
							<RingSelectorInfo DisplayValue="[string]NONE" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
							<RingSelectorInfo DisplayValue="[string]SINE" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
							<RingSelectorInfo DisplayValue="[string]SQUARE" IsEnabled="[bool]True" Value="[int]2" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
							<RingSelectorInfo DisplayValue="[string]TRIANGLE" IsEnabled="[bool]True" Value="[int]3" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
							<RingSelectorInfo DisplayValue="[string]RAMP_UP" IsEnabled="[bool]True" Value="[int]4" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
							<RingSelectorInfo DisplayValue="[string]RAMP_DOWN" IsEnabled="[bool]True" Value="[int]5" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
							<RingSelectorInfo DisplayValue="[string]DC" IsEnabled="[bool]True" Value="[int]6" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
							<RingSelectorInfo DisplayValue="[string]NOISE" IsEnabled="[bool]True" Value="[int]101" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
							<RingSelectorInfo DisplayValue="[string]USER" IsEnabled="[bool]True" Value="[int]102" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						</ChannelEnumSelector>
						<Label Height="[float]16" Id="c37d811a42074f978d66f5a4eabb0a1b" LabelOwner="[UIModel]7f260a0fb0264525bf6fe93386a70475" Left="[float]17" Text="[string]Waveform type" Top="[float]15" Width="[float]81" xmlns="http://www.ni.com/PanelCommon" />
					</ScreenSurfaceCanvas>
					<Label Height="[float]16" Id="71f1cdbbfff74b2288e50335e2febe5a" LabelOwner="[UIModel]2ffdcdb273fe4862be3202e131f03c97" Left="[float]16" Text="[string]Waveform" Top="[float]69" Width="[float]56" xmlns="http://www.ni.com/PanelCommon" />
					<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BaseName="[string]Canvas" Height="[float]78" Id="551f49447d274e789eb3a73aec6d0022" Label="[UIModel]42728973c8064b108944d3ef215a42cd" Left="[float]16" Top="[float]318" Width="[float]235">
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{77b83973-0d6a-48d0-8612-4f61bc92e844}/Configuration/duration" Enabled="[bool]True" Height="[float]24" Id="5a14ab7b98e6427ebc063e246b5342d9" IsLabelBoundToChannel="[bool]False" Label="[UIModel]ef2ea30a9e4c4bfeb88dd423151c9d93" Left="[float]17" Top="[float]35" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]70" />
						<Label Height="[float]16" Id="ef2ea30a9e4c4bfeb88dd423151c9d93" LabelOwner="[UIModel]5a14ab7b98e6427ebc063e246b5342d9" Left="[float]17" Text="[string]Duration (s)" Top="[float]15" Width="[float]63" xmlns="http://www.ni.com/PanelCommon" />
					</ScreenSurfaceCanvas>
					<Label Height="[float]16" Id="42728973c8064b108944d3ef215a42cd" LabelOwner="[UIModel]551f49447d274e789eb3a73aec6d0022" Left="[float]16" Text="[string]Execution" Top="[float]298" Width="[float]52" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{77b83973-0d6a-48d0-8612-4f61bc92e844}/Configuration/pin_names" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="667ec7adf5d14ba7856694b0bd17045e" IsLabelBoundToChannel="[bool]False" Label="[UIModel]cfc85d2289f0417588fcf86dd06f0503" Left="[float]17" MultipleSelectionMode="[MultipleSelectionModes]List" SelectedResource="[NI_Core_DataValues_TagRefnum]Pin1" Top="[float]35" Width="[float]136" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
					<Label Height="[float]16" Id="cfc85d2289f0417588fcf86dd06f0503" LabelOwner="[UIModel]667ec7adf5d14ba7856694b0bd17045e" Left="[float]17" Text="[string]Pin names" Top="[float]15" Width="[float]56" xmlns="http://www.ni.com/PanelCommon" />
				</ScreenSurface>
			</Screen>
		</EmbeddedDefinitionReference>
	</EnvoyManagerFile>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nifgen_standard_function/NIFgenStandardFunction_example.seq sha256=b96deba9ffab3f5d6898ed0b825d6881b16367fc3ba695cc8d4f553978bbbbc3 bytes=178369 -->
## FILE: examples/nifgen_standard_function/NIFgenStandardFunction_example.seq

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nifgen_standard_function/NIFgenStandardFunction_example.seq`
- sha256: `b96deba9ffab3f5d6898ed0b825d6881b16367fc3ba695cc8d4f553978bbbbc3`
- bytes: 178369

````text
<?xml version="1.0" encoding="UTF-8"?>
<teststandfileheader type='SequenceFile' fileversion='962' productname='TestStand' productversion='2021 SP1 (21.1.0.49154)' compatibleversion='21.0.0.0' buildversion='21.0.0.49156' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.ni.com/TestStand/21.0.0/SequenceFile">
	<typelist>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='1'>
			<Expression classname='ExprValue' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<value/>
			</Expression>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='2'>
			<StepTypeMenu classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='24'>
				<subprops>
					<CanBeSubstepType classname='Bool'>
						<value>false</value>
					</CanBeSubstepType>
					<CanOnlyBeSubstepType classname='Bool'>
						<value>false</value>
					</CanOnlyBeSubstepType>
					<Category classname='Str'>
						<value>""</value>
					</Category>
					<ItemName typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value>""</value>
					</ItemName>
					<SingularItemName classname='Str'>
						<value>""</value>
					</SingularItemName>
					<SeparatorBeforeCategory classname='Bool'>
						<value>false</value>
					</SeparatorBeforeCategory>
					<SeparatorBeforeItemName classname='Bool'>
						<value>false</value>
					</SeparatorBeforeItemName>
					<Group classname='Str'>
						<value/>
					</Group>
				</subprops>
			</StepTypeMenu>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='3'>
			<StepTypeSubstepsArray classname='Objs' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4718616' instanceoverrideflags='4849688' valueflags='24'>
				<value lbound='[0]' ubound='[]'/>
			</StepTypeSubstepsArray>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='4'>
			<NI_ArrayDimensions classname='ArrayDimensions' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<LowerBounds classname='Nums'>
						<value lbound='[0]' ubound='[]'/>
					</LowerBounds>
					<UpperBounds classname='Nums'>
						<value lbound='[0]' ubound='[]'/>
					</UpperBounds>
				</subprops>
			</NI_ArrayDimensions>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='5'>
			<NI_PropertyObjectType classname='PropertyObjectType' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<ValueType classname='Num'>
						<value>3</value>
					</ValueType>
					<IsObject classname='Bool'>
						<value>true</value>
					</IsObject>
					<TypeName classname='Str'>
						<value/>
					</TypeName>
					<ElementType classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</ElementType>
					<ArrayDimensions typename='NI_ArrayDimensions' xsi:type='NI_ArrayDimensions' classname='ArrayDimensions'>
						<subprops>
							<LowerBounds classname='Nums'>
								<value lbound='[0]' ubound='[]'/>
							</LowerBounds>
							<UpperBounds classname='Nums'>
								<value lbound='[0]' ubound='[]'/>
							</UpperBounds>
						</subprops>
					</ArrayDimensions>
					<Representation classname='Num'>
						<value>1</value>
					</Representation>
					<ClassName classname='Str'>
						<value/>
					</ClassName>
				</subprops>
			</NI_PropertyObjectType>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='6'>
			<NI_CustomResult classname='CustomResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Name>
					<ValueToLog typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ValueToLog>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>2</value>
					</CheckedState>
					<Type typename='NI_PropertyObjectType' xsi:type='NI_PropertyObjectType' classname='PropertyObjectType'>
						<subprops>
							<ValueType classname='Num'>
								<value>3</value>
							</ValueType>
							<IsObject classname='Bool'>
								<value>true</value>
							</IsObject>
							<TypeName classname='Str'>
								<value/>
							</TypeName>
							<ElementType classname='Objs'>
								<value lbound='[0]' ubound='[]'/>
							</ElementType>
							<ArrayDimensions classname='ArrayDimensions'>
								<subprops>
									<LowerBounds classname='Nums'>
										<value lbound='[0]' ubound='[]'/>
									</LowerBounds>
									<UpperBounds classname='Nums'>
										<value lbound='[0]' ubound='[]'/>
									</UpperBounds>
								</subprops>
							</ArrayDimensions>
							<Representation classname='Num'>
								<value>1</value>
							</Representation>
							<ClassName classname='Str'>
								<value/>
							</ClassName>
						</subprops>
					</Type>
					<Elements classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</Elements>
					<IsAnyType classname='Bool'>
						<value>true</value>
					</IsAnyType>
				</subprops>
			</NI_CustomResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='7'>
			<TEInf classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4456472' instanceoverrideflags='4456472' valueflags='24'>
				<subprops>
					<Id classname='Str' flagsforinstances='1' instanceoverrideflags='5046297'>
						<value/>
					</Id>
					<Icon classname='Str' instanceoverrideflags='5046296'>
						<value/>
					</Icon>
					<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7143448' structureflags='2097152'/>
					<PreCond typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PreCond>
					<LoadOpt classname='Str' instanceoverrideflags='5046296'>
						<value>PreloadWhenExecuted</value>
					</LoadOpt>
					<UnloadOpt classname='Str' instanceoverrideflags='5046296'>
						<value>UnloadWithFile</value>
					</UnloadOpt>
					<Mode classname='Str' instanceoverrideflags='5046296'>
						<value>Normal</value>
					</Mode>
					<WindowActivation classname='Str' instanceoverrideflags='5046296'>
						<value>None</value>
					</WindowActivation>
					<ResultOption classname='Num' instanceoverrideflags='5046296'>
						<value>1</value>
					</ResultOption>
					<StepFCSeqF classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</StepFCSeqF>
					<IgnoreRTE classname='Bool' instanceoverrideflags='5046296'>
						<value>false</value>
					</IgnoreRTE>
					<UseMutex classname='Bool' instanceoverrideflags='5046296'>
						<value>false</value>
					</UseMutex>
					<MutexNameOrRef typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</MutexNameOrRef>
					<BatchSyncOpt classname='Num' instanceoverrideflags='5046296'>
						<value>0</value>
					</BatchSyncOpt>
					<SwitchEnabled classname='Bool' instanceoverrideflags='5046296'>
						<value>false</value>
					</SwitchEnabled>
					<VirtualDeviceName typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</VirtualDeviceName>
					<SwitchOperation classname='Num' instanceoverrideflags='5046296'>
						<value>1</value>
					</SwitchOperation>
					<RouteGroupConnect typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</RouteGroupConnect>
					<RouteGroupDisconnect typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</RouteGroupDisconnect>
					<MulticonnectMode classname='Num' instanceoverrideflags='5046296'>
						<value>1</value>
					</MulticonnectMode>
					<OperationOrder classname='Num' instanceoverrideflags='5046296'>
						<value>2</value>
					</OperationOrder>
					<ConnectionLifetime classname='Num' instanceoverrideflags='5046296'>
						<value>4</value>
					</ConnectionLifetime>
					<WaitForDebounce classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</WaitForDebounce>
					<PassAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</PassAct>
					<FailAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</FailAct>
					<PassActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PassActTarget>
					<FailActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</FailActTarget>
					<CustExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</CustExpr>
					<CustTrueAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</CustTrueAct>
					<CustFalseAct classname='Str' instanceoverrideflags='5046296'>
						<value>Next</value>
					</CustFalseAct>
					<CustTrueActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</CustTrueActTarget>
					<CustFalseActTarget typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</CustFalseActTarget>
					<LoopType classname='Str' instanceoverrideflags='5046296'>
						<value>NoLooping</value>
					</LoopType>
					<LoopWhile typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</LoopWhile>
					<LoopStatus typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</LoopStatus>
					<LoopIncrement typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value>RunState.LoopIndex += 1</value>
					</LoopIncrement>
					<LoopInitialize typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value>RunState.LoopIndex = 0</value>
					</LoopInitialize>
					<LoopOpt classname='Num' instanceoverrideflags='5046296'>
						<value>0</value>
					</LoopOpt>
					<PreExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PreExpr>
					<PostExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</PostExpr>
					<StatusExpr typename='Expression' xsi:type='Expression' classname='ExprValue' instanceoverrideflags='5046296'>
						<value/>
					</StatusExpr>
					<CanSpecifyModule classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanSpecifyModule>
					<CanEditCode classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanEditCode>
					<CanEditModulePrototype classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanEditModulePrototype>
					<CanEditParameterAdditionalResults classname='Bool' instanceoverrideflags='5046296'>
						<value>true</value>
					</CanEditParameterAdditionalResults>
					<PrecondIntExe classname='Num' instanceoverrideflags='5046296'>
						<value>0</value>
					</PrecondIntExe>
					<Requirements classname='Obj' flagsforinstances='2097153' instanceoverrideflags='7143449' valueflags='1' structureflags='2097152'>
						<subprops>
							<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
								<value lbound='[0]' ubound='[]'/>
							</Links>
						</subprops>
					</Requirements>
					<CustomResults classname='Objs' instanceoverrideflags='5046296'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</CustomResults>
					<AdditionalResultsHints classname='Objs' instanceoverrideflags='5046296'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
				</subprops>
			</TEInf>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='8'>
			<StepTypeNIData classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='24'>
				<subprops>
					<EditPanels classname='Strs'>
						<value lbound='[0]' ubound='[]'/>
					</EditPanels>
				</subprops>
			</StepTypeNIData>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='9'>
			<Error classname='Obj' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<extdata controllername='STRUCT' allowstructpassing='true' packingoption='8' exclude='false' type='0' arraystorage='0' strbuffersize='256' strstorage='0'/>
				<extdata controllername='CLUST' allowclusterpassing='true' exclude='false' memberlabel=''/>
				<extdata controllername='DNSTRUCT' allowstructpassing='true' exclude='false' membername=''/>
				<extdata controllername='BLVCLUSTER' allowclusterpassing='true' exclude='false' memberlabel=''/>
				<subprops>
					<Code classname='Num' flagsforinstances='4194304' valueflags='4194304'>
						<value>0</value>
						<extdata controllername='STRUCT' allowstructpassing='false' packingoption='0' exclude='false' type='6' arraystorage='0' strbuffersize='256' strstorage='0'/>
						<extdata controllername='CLUST' allowclusterpassing='false' exclude='false' memberlabel='code'/>
						<extdata controllername='DNSTRUCT' allowstructpassing='false' exclude='false' membername='code'/>
						<extdata controllername='BLVCLUSTER' allowclusterpassing='false' exclude='false' memberlabel='code'/>
					</Code>
					<Msg classname='Str' flagsforinstances='4194304' valueflags='4194304'>
						<value/>
						<extdata controllername='STRUCT' allowstructpassing='false' packingoption='0' exclude='false' type='2' arraystorage='0' strbuffersize='1024' strstorage='1'/>
						<extdata controllername='CLUST' allowclusterpassing='false' exclude='false' memberlabel='source'/>
						<extdata controllername='DNSTRUCT' allowstructpassing='false' exclude='false' membername='msg'/>
						<extdata controllername='BLVCLUSTER' allowclusterpassing='false' exclude='false' memberlabel='source'/>
					</Msg>
					<Occurred classname='Bool' flagsforinstances='4194304' valueflags='4194304'>
						<value>false</value>
						<extdata controllername='STRUCT' allowstructpassing='false' packingoption='0' exclude='false' type='6' arraystorage='0' strbuffersize='256' strstorage='0'/>
						<extdata controllername='CLUST' allowclusterpassing='false' exclude='false' memberlabel='status'/>
						<extdata controllername='DNSTRUCT' allowstructpassing='false' exclude='false' membername='occurred'/>
						<extdata controllername='BLVCLUSTER' allowclusterpassing='false' exclude='false' memberlabel='status'/>
					</Occurred>
				</subprops>
			</Error>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='10'>
			<CommonResults classname='Obj' isroottypedef='true' typecategory='3' timestamp='1465572565' typeversion='3.1.0.100' typelastmodversion='21.1.0.49154' typeminprodversion='3.1.0.0' typeflags='33554432' flagsforinstances='4194304' valueflags='4194304'/>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='11'>
			<Substep classname='StepType' isroottypedef='true' typecategory='1' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554438' flagsforinstances='4194304' instanceoverrideflags='4194304'>
				<subprops>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>"%ModuleDescription"</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "GENERIC_DEF_SUBSTEP_NAME")</value>
					</DefaultNameFormat>
					<BlockStartTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockStartTypes>
					<BlockEndTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockEndTypes>
					<AppliesToBlockStructure classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</AppliesToBlockStructure>
					<Menu typename='StepTypeMenu' xsi:type='StepTypeMenu' classname='Obj'>
						<subprops>
							<CanBeSubstepType classname='Bool'>
								<value>true</value>
							</CanBeSubstepType>
							<CanOnlyBeSubstepType classname='Bool'>
								<value>true</value>
							</CanOnlyBeSubstepType>
							<Category classname='Str'>
								<value>""</value>
							</Category>
							<ItemName classname='ExprValue'>
								<value>ResStr("NI_STEPTYPES", "GENERIC_SUBSTEP_MENU_ITEM_NAME")</value>
							</ItemName>
							<SingularItemName classname='Str'>
								<value>""</value>
							</SingularItemName>
							<SeparatorBeforeCategory classname='Bool'>
								<value>false</value>
							</SeparatorBeforeCategory>
							<SeparatorBeforeItemName classname='Bool'>
								<value>false</value>
							</SeparatorBeforeItemName>
							<Group classname='Str'>
								<value>GenericSubsteps</value>
							</Group>
						</subprops>
					</Menu>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</Substeps>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>DefaultLabVIEWNXG|DefaultLabVIEW|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|DefaultHTB80_Template|Default_Template</value>
					</CodeTemplates>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value/>
							</Icon>
							<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7274521' structureflags='2097152'/>
							<PreCond classname='ExprValue'>
								<value/>
							</PreCond>
							<LoadOpt classname='Str'>
								<value>PreloadWhenExecuted</value>
							</LoadOpt>
							<UnloadOpt classname='Str'>
								<value>UnloadWithFile</value>
							</UnloadOpt>
							<Mode classname='Str'>
								<value>Normal</value>
							</Mode>
							<WindowActivation classname='Str'>
								<value>None</value>
							</WindowActivation>
							<ResultOption classname='Num'>
								<value>1</value>
							</ResultOption>
							<StepFCSeqF classname='Bool'>
								<value>true</value>
							</StepFCSeqF>
							<IgnoreRTE classname='Bool'>
								<value>false</value>
							</IgnoreRTE>
							<UseMutex classname='Bool'>
								<value>false</value>
							</UseMutex>
							<MutexNameOrRef classname='ExprValue'>
								<value/>
							</MutexNameOrRef>
							<BatchSyncOpt classname='Num'>
								<value>0</value>
							</BatchSyncOpt>
							<SwitchEnabled classname='Bool'>
								<value>false</value>
							</SwitchEnabled>
							<VirtualDeviceName classname='ExprValue'>
								<value/>
							</VirtualDeviceName>
							<SwitchOperation classname='Num'>
								<value>1</value>
							</SwitchOperation>
							<RouteGroupConnect classname='ExprValue'>
								<value/>
							</RouteGroupConnect>
							<RouteGroupDisconnect classname='ExprValue'>
								<value/>
							</RouteGroupDisconnect>
							<MulticonnectMode classname='Num'>
								<value>1</value>
							</MulticonnectMode>
							<OperationOrder classname='Num'>
								<value>2</value>
							</OperationOrder>
							<ConnectionLifetime classname='Num'>
								<value>4</value>
							</ConnectionLifetime>
							<WaitForDebounce classname='Bool'>
								<value>true</value>
							</WaitForDebounce>
							<PassAct classname='Str'>
								<value>Next</value>
							</PassAct>
							<FailAct classname='Str'>
								<value>Next</value>
							</FailAct>
							<PassActTarget classname='ExprValue'>
								<value/>
							</PassActTarget>
							<FailActTarget classname='ExprValue'>
								<value/>
							</FailActTarget>
							<CustExpr classname='ExprValue'>
								<value/>
							</CustExpr>
							<CustTrueAct classname='Str'>
								<value>Next</value>
							</CustTrueAct>
							<CustFalseAct classname='Str'>
								<value>Next</value>
							</CustFalseAct>
							<CustTrueActTarget classname='ExprValue'>
								<value/>
							</CustTrueActTarget>
							<CustFalseActTarget classname='ExprValue'>
								<value/>
							</CustFalseActTarget>
							<LoopType classname='Str'>
								<value>NoLooping</value>
							</LoopType>
							<LoopWhile classname='ExprValue'>
								<value/>
							</LoopWhile>
							<LoopStatus classname='ExprValue'>
								<value/>
							</LoopStatus>
							<LoopIncrement classname='ExprValue'>
								<value>RunState.LoopIndex += 1</value>
							</LoopIncrement>
							<LoopInitialize classname='ExprValue'>
								<value>RunState.LoopIndex = 0</value>
							</LoopInitialize>
							<LoopOpt classname='Num'>
								<value>0</value>
							</LoopOpt>
							<PreExpr classname='ExprValue'>
								<value/>
							</PreExpr>
							<PostExpr classname='ExprValue'>
								<value/>
							</PostExpr>
							<StatusExpr classname='ExprValue'>
								<value/>
							</StatusExpr>
							<CanSpecifyModule classname='Bool'>
								<value>true</value>
							</CanSpecifyModule>
							<CanEditCode classname='Bool'>
								<value>true</value>
							</CanEditCode>
							<CanEditModulePrototype classname='Bool'>
								<value>true</value>
							</CanEditModulePrototype>
							<CanEditParameterAdditionalResults classname='Bool'>
								<value>true</value>
							</CanEditParameterAdditionalResults>
							<PrecondIntExe classname='Num'>
								<value>0</value>
							</PrecondIntExe>
							<Requirements classname='Obj' flagsforinstances='1' valueflags='1' structureflags='2097152'>
								<subprops>
									<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
										<value lbound='[0]' ubound='[]'/>
									</Links>
								</subprops>
							</Requirements>
							<CustomResults classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</CustomResults>
							<AdditionalResultsHints classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</AdditionalResultsHints>
						</subprops>
					</TS>
					<NI_Data typename='StepTypeNIData' xsi:type='StepTypeNIData' classname='Obj'>
						<subprops>
							<EditPanels classname='Strs'>
								<value lbound='[0]' ubound='[]'/>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
						<subprops>
							<Error typename='Error' xsi:type='Error' classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
								<subprops>
									<Code classname='Num'>
										<value>0</value>
									</Code>
									<Msg classname='Str'>
										<value/>
									</Msg>
									<Occurred classname='Bool'>
										<value>false</value>
									</Occurred>
								</subprops>
							</Error>
							<Status classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</Status>
							<ReportText classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</ReportText>
							<Common typename='CommonResults' xsi:type='CommonResults' classname='Obj'/>
						</subprops>
					</Result>
					<CanEncapsulate classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</CanEncapsulate>
				</subprops>
			</Substep>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='12'>
			<NI_DotNetParameterResult classname='DotNetParameterResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>1</value>
					</CheckedState>
				</subprops>
			</NI_DotNetParameterResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='13'>
			<DotNetParameter classname='DotNetParameter' isroottypedef='true' typecategory='3' timestamp='1650061192' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name classname='Str'>
						<value>_notNamed</value>
					</Name>
					<ArgVal typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgVal>
					<ArgDisplayVal typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgDisplayVal>
					<Type classname='Num'>
						<value>0</value>
					</Type>
					<TypeName classname='Str'>
						<value/>
					</TypeName>
					<Flags classname='Num'>
						<value>0</value>
					</Flags>
					<IsOptional classname='Bool'>
						<value>false</value>
					</IsOptional>
					<CallDispose classname='Bool'>
						<value>false</value>
					</CallDispose>
					<NumDimensions classname='Nums'>
						<value lbound='[0]' ubound='[]'/>
					</NumDimensions>
					<MultiElement classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</MultiElement>
					<AdditionalResults classname='Obj'>
						<subprops>
							<Input typename='NI_DotNetParameterResult' xsi:type='NI_DotNetParameterResult' classname='DotNetParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Input>
							<Output typename='NI_DotNetParameterResult' xsi:type='NI_DotNetParameterResult' classname='DotNetParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Output>
						</subprops>
					</AdditionalResults>
					<UserData classname='Obj' flagsforinstances='2097152' structureflags='2097152'/>
				</subprops>
			</DotNetParameter>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='14'>
			<NI_DotNetCallResult classname='DotNetCallResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>1</value>
					</CheckedState>
				</subprops>
			</NI_DotNetCallResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='15'>
			<DotNetCall classname='DotNetCall' isroottypedef='true' typecategory='3' timestamp='1650061192' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<ClassName classname='Str'>
						<value/>
					</ClassName>
					<MemberType classname='Num'>
						<value>0</value>
					</MemberType>
					<Static classname='Bool'>
						<value>false</value>
					</Static>
					<MemberName classname='Str'>
						<value/>
					</MemberName>
					<Params classname='Objs'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='DotNetParameter' xsi:type='DotNetParameter' name='' classname='DotNetParameter' structureflags='131072'>
									<subprops>
										<Name classname='Str'>
											<value>_notNamed</value>
										</Name>
										<ArgVal classname='ExprValue'>
											<value/>
										</ArgVal>
										<ArgDisplayVal classname='ExprValue'>
											<value/>
										</ArgDisplayVal>
										<Type classname='Num'>
											<value>0</value>
										</Type>
										<TypeName classname='Str'>
											<value/>
										</TypeName>
										<Flags classname='Num'>
											<value>0</value>
										</Flags>
										<IsOptional classname='Bool'>
											<value>false</value>
										</IsOptional>
										<CallDispose classname='Bool'>
											<value>false</value>
										</CallDispose>
										<NumDimensions classname='Nums'>
											<value lbound='[0]' ubound='[]'/>
										</NumDimensions>
										<MultiElement classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</MultiElement>
										<AdditionalResults classname='Obj'>
											<subprops>
												<Input classname='DotNetParameterResult'>
													<subprops>
														<Condition classname='ExprValue'>
															<value/>
														</Condition>
														<Flags classname='Num'>
															<value>8192</value>
														</Flags>
														<CheckedState classname='Num'>
															<value>1</value>
														</CheckedState>
													</subprops>
												</Input>
												<Output classname='DotNetParameterResult'>
													<subprops>
														<Condition classname='ExprValue'>
															<value/>
														</Condition>
														<Flags classname='Num'>
															<value>8192</value>
														</Flags>
														<CheckedState classname='Num'>
															<value>1</value>
														</CheckedState>
													</subprops>
												</Output>
											</subprops>
										</AdditionalResults>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</Params>
					<AdditionalResult typename='NI_DotNetCallResult' xsi:type='NI_DotNetCallResult' classname='DotNetCallResult'>
						<subprops>
							<Condition classname='ExprValue'>
								<value/>
							</Condition>
							<Flags classname='Num'>
								<value>8192</value>
							</Flags>
							<CheckedState classname='Num'>
								<value>1</value>
							</CheckedState>
						</subprops>
					</AdditionalResult>
				</subprops>
			</DotNetCall>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='0'>
			<Path classname='PathValue' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<value/>
			</Path>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='16'>
			<DotNetStepAdditions classname='DotNetModule' isroottypedef='true' typecategory='3' timestamp='1650061192' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Calls classname='Objs'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='DotNetCall' xsi:type='DotNetCall' name='' classname='DotNetCall' structureflags='131072'>
									<subprops>
										<ClassName classname='Str'>
											<value/>
										</ClassName>
										<MemberType classname='Num'>
											<value>0</value>
										</MemberType>
										<Static classname='Bool'>
											<value>false</value>
										</Static>
										<MemberName classname='Str'>
											<value/>
										</MemberName>
										<Params classname='Objs'>
											<value lbound='[0]' ubound='[]'>
												<elemproto>
													<_NAME_IN_ATTRIBUTE_ name='' classname='DotNetParameter' structureflags='0'/>
												</elemproto>
											</value>
										</Params>
										<AdditionalResult classname='DotNetCallResult'>
											<subprops>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>1</value>
												</CheckedState>
											</subprops>
										</AdditionalResult>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</Calls>
					<AssemblyPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</AssemblyPath>
					<AssemblyStrongName classname='Str'>
						<value/>
					</AssemblyStrongName>
					<AssemblyLocation classname='Num'>
						<value>0</value>
					</AssemblyLocation>
					<ClassName classname='Str'>
						<value/>
					</ClassName>
					<IsStruct classname='Bool'>
						<value>false</value>
					</IsStruct>
					<StructDef typename='DotNetParameter' xsi:type='DotNetParameter' classname='DotNetParameter'>
						<subprops>
							<Name classname='Str'>
								<value>_notNamed</value>
							</Name>
							<ArgVal classname='ExprValue'>
								<value/>
							</ArgVal>
							<ArgDisplayVal classname='ExprValue'>
								<value/>
							</ArgDisplayVal>
							<Type classname='Num'>
								<value>0</value>
							</Type>
							<TypeName classname='Str'>
								<value/>
							</TypeName>
							<Flags classname='Num'>
								<value>0</value>
							</Flags>
							<IsOptional classname='Bool'>
								<value>false</value>
							</IsOptional>
							<CallDispose classname='Bool'>
								<value>false</value>
							</CallDispose>
							<NumDimensions classname='Nums'>
								<value lbound='[0]' ubound='[]'/>
							</NumDimensions>
							<MultiElement classname='Objs'>
								<value lbound='[0]' ubound='[]'/>
							</MultiElement>
							<AdditionalResults classname='Obj'>
								<subprops>
									<Input classname='DotNetParameterResult'>
										<subprops>
											<Condition classname='ExprValue'>
												<value/>
											</Condition>
											<Flags classname='Num'>
												<value>8192</value>
											</Flags>
											<CheckedState classname='Num'>
												<value>1</value>
											</CheckedState>
										</subprops>
									</Input>
									<Output classname='DotNetParameterResult'>
										<subprops>
											<Condition classname='ExprValue'>
												<value/>
											</Condition>
											<Flags classname='Num'>
												<value>8192</value>
											</Flags>
											<CheckedState classname='Num'>
												<value>1</value>
											</CheckedState>
										</subprops>
									</Output>
								</subprops>
							</AdditionalResults>
						</subprops>
					</StructDef>
					<RemoteSpecifiedByExpr classname='Bool'>
						<value>false</value>
					</RemoteSpecifiedByExpr>
					<UseLoadSpec classname='Bool'>
						<value>false</value>
					</UseLoadSpec>
					<ModuleSrcPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModuleSrcPath>
					<ModulePrjPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModulePrjPath>
					<ModuleSlnPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModuleSlnPath>
					<FunctionName classname='Str'>
						<value/>
					</FunctionName>
				</subprops>
			</DotNetStepAdditions>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='17'>
			<PostSubstep classname='StepType' isroottypedef='true' typecategory='1' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554438' flagsforinstances='4194304' instanceoverrideflags='4194304'>
				<subprops>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>"%ModuleDescription"</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "POST_DEF_SUBSTEP_NAME")</value>
					</DefaultNameFormat>
					<BlockStartTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockStartTypes>
					<BlockEndTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockEndTypes>
					<AppliesToBlockStructure classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</AppliesToBlockStructure>
					<Menu typename='StepTypeMenu' xsi:type='StepTypeMenu' classname='Obj'>
						<subprops>
							<CanBeSubstepType classname='Bool'>
								<value>true</value>
							</CanBeSubstepType>
							<CanOnlyBeSubstepType classname='Bool'>
								<value>true</value>
							</CanOnlyBeSubstepType>
							<Category classname='Str'>
								<value>""</value>
							</Category>
							<ItemName classname='ExprValue'>
								<value>ResStr("NI_STEPTYPES", "POST_SUBSTEP_MENU_ITEM_NAME")</value>
							</ItemName>
							<SingularItemName classname='Str'>
								<value>""</value>
							</SingularItemName>
							<SeparatorBeforeCategory classname='Bool'>
								<value>false</value>
							</SeparatorBeforeCategory>
							<SeparatorBeforeItemName classname='Bool'>
								<value>false</value>
							</SeparatorBeforeItemName>
							<Group classname='Str'>
								<value>ExecSubsteps</value>
							</Group>
						</subprops>
					</Menu>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs'>
						<value lbound='[0]' ubound='[]'/>
					</Substeps>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>DefaultLabVIEWNXG|DefaultLabVIEW|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|DefaultHTB80_Template|Default_Template</value>
					</CodeTemplates>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value/>
							</Icon>
							<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7274521' structureflags='2097152'/>
							<PreCond classname='ExprValue'>
								<value/>
							</PreCond>
							<LoadOpt classname='Str'>
								<value>PreloadWhenExecuted</value>
							</LoadOpt>
							<UnloadOpt classname='Str'>
								<value>UnloadWithFile</value>
							</UnloadOpt>
							<Mode classname='Str'>
								<value>Normal</value>
							</Mode>
							<WindowActivation classname='Str'>
								<value>None</value>
							</WindowActivation>
							<ResultOption classname='Num'>
								<value>1</value>
							</ResultOption>
							<StepFCSeqF classname='Bool'>
								<value>true</value>
							</StepFCSeqF>
							<IgnoreRTE classname='Bool'>
								<value>false</value>
							</IgnoreRTE>
							<UseMutex classname='Bool'>
								<value>false</value>
							</UseMutex>
							<MutexNameOrRef classname='ExprValue'>
								<value/>
							</MutexNameOrRef>
							<BatchSyncOpt classname='Num'>
								<value>0</value>
							</BatchSyncOpt>
							<SwitchEnabled classname='Bool'>
								<value>false</value>
							</SwitchEnabled>
							<VirtualDeviceName classname='ExprValue'>
								<value/>
							</VirtualDeviceName>
							<SwitchOperation classname='Num'>
								<value>1</value>
							</SwitchOperation>
							<RouteGroupConnect classname='ExprValue'>
								<value/>
							</RouteGroupConnect>
							<RouteGroupDisconnect classname='ExprValue'>
								<value/>
							</RouteGroupDisconnect>
							<MulticonnectMode classname='Num'>
								<value>1</value>
							</MulticonnectMode>
							<OperationOrder classname='Num'>
								<value>2</value>
							</OperationOrder>
							<ConnectionLifetime classname='Num'>
								<value>4</value>
							</ConnectionLifetime>
							<WaitForDebounce classname='Bool'>
								<value>true</value>
							</WaitForDebounce>
							<PassAct classname='Str'>
								<value>Next</value>
							</PassAct>
							<FailAct classname='Str'>
								<value>Next</value>
							</FailAct>
							<PassActTarget classname='ExprValue'>
								<value/>
							</PassActTarget>
							<FailActTarget classname='ExprValue'>
								<value/>
							</FailActTarget>
							<CustExpr classname='ExprValue'>
								<value/>
							</CustExpr>
							<CustTrueAct classname='Str'>
								<value>Next</value>
							</CustTrueAct>
							<CustFalseAct classname='Str'>
								<value>Next</value>
							</CustFalseAct>
							<CustTrueActTarget classname='ExprValue'>
								<value/>
							</CustTrueActTarget>
							<CustFalseActTarget classname='ExprValue'>
								<value/>
							</CustFalseActTarget>
							<LoopType classname='Str'>
								<value>NoLooping</value>
							</LoopType>
							<LoopWhile classname='ExprValue'>
								<value/>
							</LoopWhile>
							<LoopStatus classname='ExprValue'>
								<value/>
							</LoopStatus>
							<LoopIncrement classname='ExprValue'>
								<value>RunState.LoopIndex += 1</value>
							</LoopIncrement>
							<LoopInitialize classname='ExprValue'>
								<value>RunState.LoopIndex = 0</value>
							</LoopInitialize>
							<LoopOpt classname='Num'>
								<value>0</value>
							</LoopOpt>
							<PreExpr classname='ExprValue'>
								<value/>
							</PreExpr>
							<PostExpr classname='ExprValue'>
								<value/>
							</PostExpr>
							<StatusExpr classname='ExprValue'>
								<value/>
							</StatusExpr>
							<CanSpecifyModule classname='Bool'>
								<value>true</value>
							</CanSpecifyModule>
							<CanEditCode classname='Bool'>
								<value>true</value>
							</CanEditCode>
							<CanEditModulePrototype classname='Bool'>
								<value>true</value>
							</CanEditModulePrototype>
							<CanEditParameterAdditionalResults classname='Bool'>
								<value>true</value>
							</CanEditParameterAdditionalResults>
							<PrecondIntExe classname='Num'>
								<value>0</value>
							</PrecondIntExe>
							<Requirements classname='Obj' flagsforinstances='1' valueflags='1' structureflags='2097152'>
								<subprops>
									<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
										<value lbound='[0]' ubound='[]'/>
									</Links>
								</subprops>
							</Requirements>
							<CustomResults classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</CustomResults>
							<AdditionalResultsHints classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</AdditionalResultsHints>
						</subprops>
					</TS>
					<NI_Data typename='StepTypeNIData' xsi:type='StepTypeNIData' classname='Obj'>
						<subprops>
							<EditPanels classname='Strs'>
								<value lbound='[0]' ubound='[]'/>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
						<subprops>
							<Error typename='Error' xsi:type='Error' classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
								<subprops>
									<Code classname='Num'>
										<value>0</value>
									</Code>
									<Msg classname='Str'>
										<value/>
									</Msg>
									<Occurred classname='Bool'>
										<value>false</value>
									</Occurred>
								</subprops>
							</Error>
							<Status classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</Status>
							<ReportText classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</ReportText>
							<Common typename='CommonResults' xsi:type='CommonResults' classname='Obj'/>
						</subprops>
					</Result>
					<CanEncapsulate classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</CanEncapsulate>
				</subprops>
			</PostSubstep>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='18'>
			<NoneStepAdditions classname='NoneModule' isroottypedef='true' typecategory='3' timestamp='1650060850' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'/>
		</typedef>
		<protected>E@=3HJL4100hYLEDF=_K@0@mKCYo_1KN2&lt;dfASB`]CF^aUXa]Y\4WmD]203VfR;kS;KgdGgF285WU]RaSJgcjNlM7MFC4LiX=a48\7dW:L403mZ4BUAT82I&gt;KQH8\T8QFE`DA2\LAVbMD5YRMT13fTiE^i&lt;boIle7[=C_LeZbKM2QXhVTH;?4hTX]A[17:2T;Dh\^Co3kY9PA5QK23^C]l262h09La1?5^k3J0BQZ@@EeDRZTO=\cKd?XKjmGb1N\X&lt;J[IS9OXJj22Qc=R\WEEn\IKCaHCAUNi97;EVjaJCX4&gt;UU36B3oib::mkjjIJFOY^^C_gK;?Ngamc6b1^HOM^Rl@oHoiaG802US0o36;lHiif[]oe&lt;FRliGlo^CMk69OeFDNDnIQUXNS=iA3JmW&lt;KbcFOCL6bWF;DdY7d2\SSH4mB7[^9gAb5EgM5G;l^DR5mXURj&lt;_=4b_aTDS965fd7ACLdkeA7kamDL&gt;;lWi[PA07_B@&gt;cR[mGK`_XMGdK4NmjkVR8?micjQcMS=oX^9@cW^5\93S[[2ZkFbBiZ=Q@AM0FkKdo:gUd&lt;lVVcfi&gt;bV3&gt;kl[1UR_FW&gt;JkW]_EREPX34oO2LYb;J&gt;k9nWLWBEg6Tk&gt;koggGTQ&gt;kL6kJL@dKQ2_E0Z</protected>
		<protected>E@=3HJB4110h]L]MDk_K3gBocK7LAg@bF0m7:L\7mUH^jTPf8UWji4?JObL37e`G1BU_]bJEEgG9OLd39Oi??^9QJSUTD=2428\B0kcT_7T&lt;Q@obH[[G3o^A&lt;D=J_&gt;g1Hi&lt;R`WmR7Y7K&gt;c7;g@f3WI&gt;MaH=lc7S9&gt;c?IG77K\]]6niUiBAL4CCDj_[5AJfWeomR_OoKJmJZM?&lt;_&gt;RAC]I2d0NnLHDh&gt;Dli&gt;23CM5CXi6DO^g`LX&lt;Q2hSHndMR7[D8BMh8aJ7oQSA@fKWPh;Dm5&gt;RW9o]Rgj]F^W_JkHFKk?2&gt;8;5iifgAJkk=k]f8VDCi5;PF:WC?2M3dfNg9]a`emUH&lt;]ARooBLZ\:kUkkkmM^^;g[CAF?o9BS9X&lt;V_06oLo]n`VOa[dMZmhLlJ^=?^T^nMbojKJkCSoWN4WIgV\ckgWCOWb7&gt;jno&gt;;[OS_oVacNOW7jg77?7OooD2OombloUnEI9_InB&lt;HI4[kZLf&lt;]bOKRmn::VQk1Tm`8F4;5W&gt;TA&lt;Kcd`aI[R8DKQka6aboN?k=I&gt;UJRNToCflBd:9=GW1XijhYcm92_e]^Rg?N[eOQO^9B&lt;2LjSQk=KKS8Eo?8kT9]m3^^fWPk?AQN^K4hZkc&lt;Vm&gt;gFc`@RgL^O5bET;[D_=R`WO?&gt;&gt;77S_K[1miPR@lgJ;?^^n6om3JliJgSBbAO&lt;J&gt;_7OGSQoU5Mo5ainP9oNj=DL&lt;NdI=^]VXFK0i[_\n0emoFJc]\=:4K&lt;HYHRl[4;=V_6SaC6ETl6dE1KV^E5NV9OgQBU&gt;n`WYOLgi&gt;S84nN^1mG5`SPC1]S:d;`B=4NjKmH&lt;UULW:0\;?2W8FOA:^K?M9TIFdMZj?UgUemK:5BfZf19WV&gt;o2K6[k;XS0HEj\8[[9QY;;_Z:UlBgN&gt;g897SGQPF^OS\Ba8&lt;Nl5AB?;oWBQ6aJP@1SQNGhXj:1DK9OHN&lt;6lGSkolg=dM`l2hG?AKRH2^5E7fbmmi:cJ2A056EVl9@Ll@B9;Ml6POPlacQAcKJf4N0AbVYZdLjl=5el2I6[[UbiSJdAiTCbBdeiYEk9g6Sa7[CFB8`Nkc\S4`dNB53K4Y@M`QAkbIdlgkPUJ??fmoGj]cMHcUoJH_X:heHfm2bQ96d\&gt;Y;:5diBn6JoC0O8DGdkT9VIPBjN^1cB`TcbjfVBJNQ[?b\onSkg@kON1onmnGNoOnYOo&gt;kc^Ofm]G7mB&gt;Qba^I&gt;6iVCm0GSnGTYgQ_Ig4AOR9MZMAk1Il1RgBV7TIAM`A=\k&lt;V4O9c?_3Y:O3l:dCYMk^gg;jl0L0CVKCUWH5`j7aeFkA[b&gt;CTQ95a^731VBF_IoV`TDggl4NO?G?^6Y3k&lt;P]4e7VRbee]]ZcM@Jf4&lt;;aWfGU&gt;9^:[`SDoKE?YZ:Vd8[TTU\cVW7EE&lt;cK2Y;_LD3MKjVT98S3E]O@NF=[GoXgC=`=OMNoZQ@@l2P:F[`T0:[LS53m:IMEkRTe@8gJE`&lt;]Y2:U`M8HkClI4_aPZN:4ZLOC2BoZFX8GCf8_I0;U^`[:e@:ILD&lt;808A]97NXjMJdHVK5&lt;6@ZRfV:AX6kPcgf@:31?M9dKQa?=RA:`f5TCI^bQLjbA?jYd&lt;_1^@Iek6[helE6RFL:EWA[cHLkB2l7QLeCBJX]0hDPWUWlCJ=:^m5gJjn&gt;SW9DRT1Q[Y5`gAf&lt;OdDdj1YNo:`NeELR3c2mU`G:e&gt;j8@]gAR?Ad48]8;:;&lt;S;EUJcjMiOVF1m50TbUD\Tl58jH?d\X8T^08T=W9[Z683aTA&gt;]W[5Oi5M?52E\:71[03U?V`4l_1WVH4j:GKI9hcEGRk3?_;k:;F_ej5SiN:WT:RF=Gmdl:=knc:UD^Hj9obj;AE\I7HC&gt;FB&gt;jYl8f56nJ&lt;UcI=fiN&lt;i;VXUJ55KE9jS9S_DR5N1k`PSNZVY0Z0iTYNej0?V_@UDHkL6Co5UCKBGPJYGR_Ti@1C@\A6TiIe;E\]e=ZZKd\ZVfURZTM50e8JQ[&lt;TMTUjFdJKR_9CXd\N38JN&gt;Q&gt;\UNF]@;FB8LQX@?dbU@[8mfDU3:S0dI&gt;?SmaPSHhfe6&lt;gV@A0JSZnmSECILX[AB98eHXQ9`R?5E3I6[4N=mYUREb_5jZURE5lhN6VZ\P`:`^;AQONF8O:Plbm4XSolW7VZN&lt;?OL8@0JK^m:5oh&lt;AR[a:BRlMniCM&lt;Q^\X\Nkg7G3ZMAi7nm:9PFFe3mCA1\]DY\Df;6aG&lt;iI]h2G6MG`BA\[I]008f:U6XXSNH2jcIXFSGI5Q2bBEKA`&lt;X]h_:@RfNklLbR7Sji9F_895&lt;R=Q572IULj=^noMWZiZ`ddKH`@`He:jliNb34YNl9[QT6cAlE&lt;6LflQ9e?nUMDFlcJBlA3?PP6fSobc@Of_fBSccJNY=&gt;?N3lZRDPO[EVgdA&lt;FBDB`XE&lt;^e]0&lt;&gt;VkM0OT@X&gt;YTBh&lt;5IL&lt;3?]`D2\9TbD=P9XH933VJR1BePO?6H6&lt;2;Rb:@82Hbj[IF&gt;5Pl5;dH0QG4:@48T&lt;39AjLjU172J17:JNl=j0P6NHX8U6RT@@_R0PglmF;;HX\i:jV^ULZBDKEBVfUTf9YQgX[9IDjjfT&gt;:iY`4VU&gt;jmJ&gt;^lE2G:UodJJ0?kJBH?eL@[95RbKJUIOlaNeJ04aJ?]A4YMiXMjb8EdSS:FQ@7jO^6V2_52W:f:]&lt;6e5Cd?=1I1S`LR^aZ9L?2:i8gKEhKfCL5bbPaMloUSe;o9aiAW[oE2DcNMo=]V3VZ3j=;eK0o5HDY[@\W;=e@Vl8XLFANQC9E&gt;QSA=CQY79hkh3K&lt;7T?;nR9;Z6LT?Nc&gt;S&lt;VnOhN&gt;A7dhl]K:oLi0N`lo`P8XYbiZhgEiMHkPY4;7?ho]9J`Z9g^0o=n=LSnOn?ieOB64nHAQFTK8PM_MC[JSeR8@G2bZIEdgH&lt;RZ;OM]&gt;@_LW:9G&lt;i8_M&lt;G0iefC[hgQ3@MR?7jB\Tc1Tf;FbZLgF5X3L[[i7=`i99aTj6Bf9hoc4f&gt;K\mAKJU5HVOhmaTQmdX?THaTcA20&lt;o\eFYJL5Fl`OaV0Lg^m=dM8dKEXZbi_aM`N4iNOTmgWYL3]hN6L7iae8^GXbD:O\Y6CH3&gt;KSj1^`C4a]&gt;WQ7OESNDVeoS81il`C&lt;lI\h;BR2o8`kOIUYaC_UM6UhYa5^:Vn4Tg@DYb3U\b\fAFX]aIIO3S\LG^&lt;VA[9&lt;di1?XH4d]PXFb[&lt;mS6WM1H7n4QOPX3V8JcaJ3Bc2f`3kS9^djl1&lt;NFQDkA93Ufmf&lt;amc=`80X1e3HkQ:L]YabEBD05fi1W2^:CkBEDcH^&lt;iZ;L:\8jH][;VZj4R5VRdB6F7g=a:g99Z[d9NoQ89XZfYU6Ej\lMNK`GXE8]&gt;kb1[e?Qc4mH:lRM9\OK7F\j_JGQ2X&lt;8nV91\\ReIUTd4;L6nZ4o7O&gt;5To5e:L?2S2kY98YfOPONej0UZd28\R5Kk_&gt;WnN^DH2Ra&gt;8JPmDGUT4BS3E6S6N6PXQ^o?DU4hlJ1V&gt;V1L?:__=@EIUOn9X7KR2Lo=2KmV9A8=\\T\C=1?n1D=@?IkA\=f2ii0CCN:&lt;9RPOFL`NU8DSQ&lt;`;_2&lt;nB]=6e51SI8613fMTW3Oj[L^R]8&gt;Pi:a`A2D=\4K&gt;il^UBR7P9]^G5NXA2^X7951G[YT\OKLGG4l=UQn;H7@B;8&gt;da:ibOD[XBR`]o&gt;VZ6DOCdK3AP?3A_33UbkQTneQOg=b`jYf;]h]AolQHPG^On43=0kIj9]cNR^:eSCY@7J3d:fE\We:Vb01HQD:H^8XDCNhWA\A:WD1Gl3&lt;U7dkK=5DgXUKgD\cnF6@[17\Fk=:4E@TUiP?Fl@0i9ZoM2bEb`155W4J=3T3DML1\aF:FfPQ_KUbIc:4Ya3JFAmR\aJMI0a[C4^ef5m^Fi4&gt;XZHB6?JU:=DZ87J56eH&gt;DmEMhP4D2oO3SJP&gt;1jMO2&lt;naOX3XeHoDCM;;J:PJlY8lXGAERILBl6Ze45f=C_H1EH@IjHR`mDHLk&gt;RloAEY7C[?GIk&gt;fJcE8?]mNG9gjfLehW\mLW]iM[?]hJNCWK\EIR0P]hk6`E4NUFW`L?jP9&lt;3@in]\&gt;b[aNQRj1@R1@lHWUO7cje0A&gt;LK;JhC[BgiI]\2@eSX:;QfRU@U&gt;]@_lm`4NmBZ\:ZoSFUb?TlhO5;?&gt;B1H?gA7=g=C1ji=292Ke0J\FnE9DeX&gt;CIC;iJ0Q`DXj&gt;W\&lt;PEOYPYk5m[A0\aN8N8UXTPGU[n]bW5n:`?nZlnnf\Imkoebbigkc`ofP\eP3l@ZOUX`?B@DZR_DX[^jV=gj=d1Ym4Z&lt;ob`?C`SLo9T5_eOKONeoF]7?koVKmXXP&gt;@mOLEB_KIcmYAEE:TPO\X\:IW;;f\GU_9nGfb7gkm2FX@_m\=LZKGW]]fQbgkjIKFn:Z?7OkIIKJ[SO\hURRIoOHS?5Im13fdEU3GX6A:fkd1W=WEW;WIRW;nf8PFKmj0I6c\Ol161GZUA]d;MJ:ZYK=VEA5\=d;6WchfDOoda;nMHPO^dHdLa@nRM@8^2Oa`S?HXLF4nDR@[gd@3ZWg?=HDeoV\ekeE:jne_Z_g?4HH]X`?HL\fA&gt;3IiNAk6W1m3G0_2TCL=LYO`T`_HK@l\3K6f3=3kY61mh3P6N;k6W1m37PK&lt;`\K6`f=3Y6;mn30n@QPPL_O`T`_HNXdTNm3PcB7f3=3k]61F3f^\2K6J51o9_dONJi[aZ=PgGoQ_YlegmNBlj]Mg1Y9kjW]mhcf\AE?5N[_l]E?eCjcMOO`&gt;NKk6j1FegWdiGIk&gt;gJcF[NcfKLeBjFNcffLFL[]in=6bC_H8^oNbA_H\`Ig&lt;[Zjc\IO`GPnSnRYk245=G437EhljgHLTJJgAIlMMmTC]5Ofg3k7l1=okWM^WiPP\Tb&lt;_gjXVbPjlMb^O2?7g2GoojlSJ\BolCmm&lt;eolmTbca0HGIPS7WELFBRNnUKon6]o_boQc4&lt;O7WakMAfZ1;@;]BVhfZ6d;A]\Y;]^C\2JNWl@EDkjHUD]8Gj3k:Gg9M]64UVIhV`0kFZjnXDXH9Ul?3UgC&lt;4E`da=l&lt;6aYaK?YSB&lt;ZlK8AkLXPga:L6Y9WXb^R2:;XfCCXg46QgO@OonCH=04lnD]G?@JU0oW&gt;8R[cd5WUn`Lj&gt;_L4H7acI]&lt;]SYiCVkXMEcP^ab7Tf\&lt;L36cdmoD7?&gt;U&gt;FXnG58NQBfkE`&gt;Y&gt;ZXN^;LUDk^0CT`]]YcV503o2&lt;9aY76Tb5=h;3n^l@;GR:DEml&lt;HjcCj]?2BHSYcAH8LcPLdmXLfl9&lt;R?P&gt;m[d_OAF47OMiiSBYLBDIO:B2mBEQejeLI1_lDOkc^TPmOSR;N?RhN=R3X@`aEX13VmJG`^nJRDXYeb7QSJiLJ`NX5Qkf=]imm&gt;nKg_CV6OK]RK94GkTDXQ&gt;HaT13fb00I9PG6JX1RmPQA@CXT2Ci9A4;\8804oTS3&gt;9F@3jQ0Q`Yb6PH2J8=QIl&lt;U65fY12^T^l2@8TQ51B^@UA:oVP&lt;O1`X1PnPjXO0`P3GQkdBQm:cV001le`9l2VYAPg8&lt;0k8Bm6`QjeP@j2ciUhWLj@0LY?3AP784;S@YWHX1S?Qn1m1kHbJS6f811fJb&lt;=99l6:nE1PPJ=8l=&lt;a\P0dAX0LXTD&gt;iH&lt;5QR6^dF;Bab60@I1@Q0HZS?9?A@TRA`J1PHiRc:Q:_jX1GeY=N[B&lt;3V2Pd60J^Y3@[1hD0XF2MP;&lt;B3RX2_H4PG43R;`1ZV@8E0R&lt;KHgh4VHe2B0H4:Y&lt;H5&lt;Q723C@d@1WBS^63LMX3=h4n91c3XeS;4aDhDR99PE40@14SA4S8Z_QlfJ^kenOQMQl\MFkQ32aVj``BUAmNDAB3?\R55J4A\37PAhR]3=KA6W&lt;86890Ck1NP@_[g:D6dV4Q49fS?IJ_C2;S^7mbE9SkO2G9Ii^ggHKkT`F370_j7b?jkWkEQ]:?XVf6A2ilo3@QYRZ82LV4K6^KABIXe``g6B7e1HCJK8hP9k^0X&gt;O;4j2^RRM3c2=aH8f`YUfUlb`B&lt;3I37=]e&gt;@JZ?KI:?@GJMZ]DOXZDNYX\cVFBbZ1RmDIF82=NNZDMK0dibVYa6E8b@nBP&lt;5Tl&lt;05lIDYhX^b6F\?\XfTjW:PUgjFJNIm\aeD&lt;eoRAhT`S]9IT7:LUghEY&gt;2fJODYDMFWDNBTdof=ITOaPAL59FVSX7NGk\MRM]DU&gt;&lt;nm39CJKab2S9fP&gt;SbRPR`h&lt;R0@D@5P9ZV08\FAR=6B[D?`iF9Xa6Q9e:U\ARX=B]93S4;17PliCP_8N5h`&gt;i6V3&gt;38TciG@Te@WT`HL8`hPj;\D6gSlTdaAYJMc8Hiaf&gt;[[@NAUBeHhFNTm7NYnXia&gt;:JBgQ?oS?;U9jT\\=AYoUTMCT\81ZYRXNJb\lbEEL&gt;e79ib&gt;:2`]U2jToCY]80BfV:4``\X1a4BL&lt;9?9ATRQ4bcK7^1A4RoX@7_2@S;hfe90M;0D;DJ]?I]5@0Y`&gt;NV3LF5`I1LYCFZTJU@=fTdVb2IPfC6dDZZ8JGTc2QOh;^L8HnSlnS?YbH5TGiYN5i9a8XWVIV]cK^:A]LH[5Lm2L34ZfLDn&lt;hgf2IHQJV6o[CK&gt;:33MOAcD5k&gt;LcEW&lt;&gt;D1CTFD^e69IAD3mLk&gt;C56YaKeFci;[THhLnK]V7iaZ:O5@PcUHH0f];^:5a0o2@FhcUKMQ5D&gt;nJn?Ija2clJo0KQ0:6Z&lt;7KD=:2I^YmJGE@ELPHG[9N\9mCc046gh\;[KBUd_I=RJbRBo&gt;kD8\BUXbUB8c&lt;]fF[BViXJSLNm=oWLlRY</protected>
		<protected>E@=3BJiO100h]L]MGkcK3fBoaKgcnO1C[KY_3VgFg3f\:dbWRb]W]ja3ZeDT&gt;gG&lt;F3C`h&lt;FRIEB:dR&gt;oal1lR8P`R;7UdVj]0WcI1;0g&lt;G02gHM\_?LJaZU?0;bU&gt;?K&gt;mo9iW:SW4SQU`7k?R&gt;OCUM]W&lt;jeB0_&lt;LPOEolh&gt;\=nNYf_\cHOnG4WQd6UA`SLO_Ad?fO&gt;njZG]]_]Neo`^=LRZTLTT5MG&gt;RnKeM2h&gt;L8iUjM&gt;8RC2OMoIfR2X&lt;C_Lka@&gt;B]G96ESU?&gt;o2XYIhW38;liQ9CWZnPo?&gt;KMefNkmo`5lF^ST9RZ7HULfI]cIoi@K&gt;L&lt;a3YOo;ZgDOf&gt;hfcFAc_HL4EFmLci?Ggf3&gt;&gt;foggfacn]leXS49aC0bmIFlclng=o=V]&gt;_kmhdVblRiH=4n&lt;n=l&lt;lnghEb_jco^\QknmkMQFgm8mGNnb:Ale;FNmHYmlooibXo[_JhdiOHNmn;LMfCJU=VL9lYlWUS;ho\mEk8WaK@i;f13GQ6dgBMD6\2\7O2GA9AIOfSfo7oNGI^laUnL0cjRg&gt;`?6im]Q34Hi1?MI0:Udgjk7MPSGM9j`5EI87&gt;WbVf5X\`Zob5B5QoWUnMNgXBWkV\CWVj;XX?hX^Jg?&gt;Z:ASVm8O8jiUbah9onn\n=Xl2oI&lt;]6GGomAM]Hne?gigOX`\_OKE_Jc1mh\f8hJ&lt;K_^_]^kGW3WohXebO25P[dTAoQ6]g1Ijc9e]ikO]lLBJNd04EQIE^MjQlkChJaR4&gt;]?hVjVSSej@&lt;Zi;KLZL?71d=gWMd`HE`gG;cOSa=T&lt;5k;9b:bL6[QoN9&lt;VkPYdI=8[EP3[B2\ie9]f&gt;LF&lt;[J^eL_CkVen7&gt;5Ba[UQ5WE&gt;`:o6;k8hWPIej\\[Z9i[;8_Z:U&gt;V`O=f897RGQXFMNSRB98&lt;Nm93YWU?cUk34&lt;jI21Bg5In^6F:[CWNP&gt;EY=mP^fdM;8B;XRWR8IN3BIhAK3?fFC2g0k2=^YUT1QDaWN@WlFS9mdce0D^GmJQ[ga4CM7:5hEB&gt;a\FKY6[O[i&gt;6`0b^]ZjAaTl1e[IXG@MH[ah7O\kgbQbH?N_l]WmnGWk9omP4&gt;G68d:7IJ`b=c2h9lIbBKE:;]Fl@L1k;:[M&lt;aAM9aaHKGeC5n4`m;INon][Kk^WQ&lt;_On0OMn_nnhk^knnK_oWk`jDm9W`bIJA&gt;UVB^HHWa[9nDXcORQhdL9LG^L?n3TJ6T\`hkii?McS5;FcgRTeMGQdcYCin&lt;YfAONf:&gt;jbo08@ZVKTn_7hA69mF6D[acNhIR[7AlbWDf]8GD^ekBM^E^hmiGO&lt;J^7WB_V3VkLSP0Nc?aUnWfg4L98VM25HnBlbTVTUG=H6JOLWP\dG2JRY=HilehI74eKg&gt;PmeQCiRh30=h9L4I9lkJ5LH3&gt;=kLaY5?o]bAnGC9XYPj`IhD;67BNM[gAL9R8dh=Rck9B9Wmieb_^Y4Yn6_A9GYK1]7e4cEcW200EnSXZLco2:^mJ?IlMQ_`iQ]M6d\ZKK\DQ&gt;JQCc2Fh&gt;iXJcVDF;j8EKT1TbMmGihOXU0EGhF:]`G`FjW[HhPSiZE_Z?hYXGnmF62^=hn`MBjMJ1fDZgZ`EWO5cLkSb6mEX6YMY=JA4LdWbBN4I]=dgc_ONh&gt;dC_YM492mEBR&gt;KSHYOd=CV1Og::N3eER0;N8ELWdGZe1VFc=eAlQ5R0:MLER&lt;HO\TbAa1mRh?IdWA4^7g96EX&lt;I:C&lt;33OHY8NPB`ZHX90`LKjUfcYLOkADaHV&lt;;L?PdTmPT1[&gt;?gjhnME:GQU[Zi\edCN_PWUj[jX`]_=N?EViO]?2QDk1W?V8W_FJ23HS1YI_`H9V:3&gt;cS\gTT:U;YW5HTM]bOmnCWe7k`JYZeRUS[YVmaDHBLLEeNfde;U6C8gZ7T]b&gt;N9bkCI;bS@gZXPNTZH?:4cnB&lt;]5D`0ZJUJUT^cTc&lt;JF][dO=IFL@KbEEB^R0VT\X5VH^b:E;K?\aGB3dJg5_D3WWaE4b?&lt;PYEk047iaD[=]k4ZS_]=QRbHK=F;g8lmAXF&gt;QmESVhD&lt;iF8&gt;eoTUU6S5B:b506cU913NBHoJ_0G_&gt;UPUHFfoLL0[4K^Mb[VlBEM?9Vl5G&gt;RbhcB49^QWD&gt;2n?Wok?8G9nTA;9]TYFRN54@Oh`VeQDa2gVcPj:kTCM5EcPgoJk^&gt;]neYg4&lt;_I&gt;=LO9ZlU4\=CgOZRJKfl[J833OjRn@4g5J]374ZRGK038Vn5jf]9M_moj6g`]:&lt;F34bNeja&lt;oVgnmC89?NiQHToa:Ub8H2]l;@^Ro&lt;gXiokCnO7UoU52Z5V^CAH&lt;`&lt;LVM&lt;U;@NUe]LSUcXjRHj3eO?WMTDl;TJbC_;`P8G=&lt;ZZ22cDC;&lt;bf=0lOCKo7iALI1PiZ[0oW?XZ0Cf0Fajb&lt;3;di\Fg1HVR6VX:@c:F&gt;a?&gt;3PhKfRd8BgYhRQRV&lt;V1H7A`da05dXR1E\ADe6A`L`odU&lt;jQ2M\\f1;Rc`15VHQ8MT`hUZ&gt;L:D8O6D`obe1&gt;7kP@3]a6d16Lj15VeMhAN`1GWcF3eiE;FWNjPdc;g==J=eeOI;H8dceE=&lt;=Z=UYObfGLdbK9]Xdnfg]85hCW^lDm8YFG@Pg[Tii?UGMVBiH^@a2^hN3J7VWD?&lt;g4fVA_2DUEf_R@bIjMCF^HS\iUJb]T64JJ7^m0g5i1VEb9HgAldSV_iUTk@nig16kZFACb[_F]1;DGcMOX&gt;WSJFSjB=eKoQD4gBA4^^&lt;V@VkN[6:;[98UJ&lt;WXTaV8i]S4Olj0Tk7BdTY5_8kAN[U4l5bgW1_57a[od&gt;;N0_lOAINdAaDD`5JjmKJY1\lH96o72R3YfJ85i_lP7JnZgCin?XiVD:61bJAA\THP`K_ce[Jg9RX?:2fI[Ed4N:V=JOL=l9?GaJ=&lt;SKJ?nf[2TJHeQL5QD4^W43CfV:MBPJU57e9[ERb5_EecH6hDa4TMIS5\]mO@=KWQ]mEJQUUFROj9akhn5:LQ2MYd&lt;0a?Bk]NXFT5QOlJ2i8LIkO&lt;1gbf9E:Rd]K_J:F&gt;Do&gt;nKj^TNPK?TQ4&gt;o^N=U246SQeMCjB8D9;gVTcJ_REY2nL@KZL:TngB8iLOKe:Mh=b\&gt;Y:;^0jMJiMhliFIJDANdHPecLg\Ve76bL@[VLJd5EZRCen@_djBCkP\F586bl@8M]Zf28DU?c6aXB;`3jW&lt;gQge21C3dMHP4YIKWD1O2emO]_A45Nf?TEBB`;_Ll?O&lt;X3LBjB39?C=8QJZO9Q5dATCl8ZTTWmK6_9X6hHcXWX0D5WDM0fcU2Le8`A5k3Lf7RYPWlXCVDV7R_WZJQVHFmY9fBkXmUg7YHcb7VlP6_K[Q928gWWlN7mBCHkm&gt;]]80ddI&lt;BRI_b?PS43aH46^T55LeE&lt;&gt;^TG1J?NI=F8&lt;Yomhl@hKmRZZ&lt;BPYle4clb_G[k144=hN6h]iZ6S8&lt;2=H=3iI0EAMo^O:9K8d3F=\235EIfOQZScnmZB&gt;dA5h11Fgj`:R@SKh9H5J0o?1DL;&gt;44k\=@f5iT4CAb:9C&gt;`AlND&lt;BTY0IhQo:2b[_&lt;gFD45W2Q\7ZVj&gt;7&lt;1EiDCKADMcELR@1?D&gt;QS[LiEF9cPSTfHGRbL&lt;QHYl4@d`JIhiG^`7eAFo5h&lt;O7XfdB25CjBc&gt;f5XZT8nFGig&lt;@bECNSMHLQUHMP4X^_h\_^iD^IcAo=YU5ddm?g?&lt;ZB5U?d4I@o7[m?=]&lt;MVCJEH=TeeD\?^C9g8R;d&gt;H6IiPFH=c][&lt;ZB[hjDbFB_957AN]_Y@;LmlTJJLoNJh0bd1_oGRAHQ=kBGkh192G2Emo\9;b`C9J&gt;Id:FX8XjH3JV]]jHQ=`N\FDOBTP&gt;Mf]:j\m7Zd=P=^69k;9`Mcl3diU^SJVTXE&gt;fBZ&lt;NDFdEPe6ZFGhL9YHna62=1NAeVn]ehPiA6a7ohBYm9FVD0giCam0^W;RIL:n1Ze90k69f&lt;`XLXZJ\abmD4Jk9RlbFcI^C6NN[\ij6N[?lHHKcEji6N[k\i6WN[\^i6NhKdm97K\fEV8GPdjl6E29IbWka2fB1D5]AjIgEVF?C34MeQ5F0lH7FO5&gt;cm2KAT]k5b9iEkadMUD:ITV_\4F4TIF?4U9C7cfdBAGL;UK8]KGoH3gEHdc9:ST@2nKHNN2`iK[7:REBIhOAGgCPVk]B3]Fi16P`C\?P\\@WW1j7L;aYm5E&gt;9C\69MO0neG=gjA[JCl2clGo&gt;mKoQPMneg_Jo]F3Do?bN&gt;;&gt;oONd^N?:V[:haSC0]ZUk?Oc?oOBfOg5g`5Q[gCCa3^DNjDFD:G5aBhEU6UEM\X;Q^c\06NWfXZ27nVi[2T[gQM5]kTNQ@TEfIhV`8GaE&lt;mADXI1jNWUaK9CA5L=0k?C3V=kSDV&gt;^T6;]4L79;oA`U`Z5l5k0GAmJ0=MH2egZ8k1nVnOd1]TlRaIWkjH8Y1hEgFNXMUm_YbSgFaP&gt;D6&gt;]M;VB]O[QMd;h_\6Hg5oYV`UbDNH^U[UA?oG7hKVBNFJC25kHEhY:^ZNQY;U2ek8gCT\7]Yf&lt;54oL2&lt;aTU74Wi2b&gt;7cDc&gt;?keFDiTZ?6n3P1?o;c?21XS4nZgHmAk]lPS]?PgCi:e?C9G:BmkVD^EcC5?BM`V^h5&lt;M;389SOTH1k7V9R;5ch_70;9objaU\H^ZM^kW6@&lt;7TZZOWBWn&lt;5c@QXJgY0D:nEoBJRWKD@&gt;XVO\U2nW=iH&lt;mLogXf`g_IafSW:A926DN2R:I0@=\`7?0d858eT06h2Ta6jXHAJBQT2U;\`A5Z8QA:=@T:TI2mm1&lt;nTQ8LBd]S`LN8&lt;9ZTdfc10P@AfE83FC64IZ210IU21W0&lt;A:o:YP3aodV`Od=`P8POJahNPBHDX1N;06?ZL4XPl0e@l\0l:dL&gt;mj8&gt;B374D_a1X&lt;X69N7VHU3b@RO?7nRHQD`@0Q&gt;JkBS3kEA_U?XH660WS4210`XJ3JP=JRR4WWa4BD0WmZ&lt;Oa\4&gt;0S4A0Q&lt;iF86PY4ST&lt;c1aZ@Q5Q9aVX1HmY1I3C&gt;3n2P&lt;62JjY3Dg1h@PXG:C0;&lt;FK2d1J\2@]0b80&gt;c562T2@D&gt;3nFQHE;Rh::HDa5_YHQEC`XP:1ZG5Q&lt;D8HD@SH:h\K88k0ab^4R9VQ=H\0V4018FNR54\AOBFhNa4D:XRU_538ZFP7&lt;ZhP8_Ae06R6l@=PRl6X@\5^SSH@ZnMml`dR`Bl5636jEA[P5:&lt;0G:;:TneHK&gt;N5kQiHTOjHIN[_aPh&gt;N\@XN_mX^f]E5CKm6Zce:l2AmS399@g58P@a?QgL5lQ`cm2JHTTUR8IIKM864C_k&lt;BC`a1@[dE;Pgki5CC6^0Zf\C?\Ah9`BJIYFEVY=XT4cY\]BXbEIDo:T96jiC\:;BjS;a]E@XXRTZL7BV&lt;mBPFO8A6DYA:?9WYTPIX@F9R@e^EgDY]?[U1lZOFA[KdWHSV]&lt;GfMXMeHH;46Uj_SbEHdjTO6[lG5MZQRf[mAnUk&gt;@6VQY:]:[4cXfG2h_ab^Eb9T6i;RRARUkHKn8N6ZZB=&gt;QlO34A47@S0e0SW=AB2HU=CARD5g69HSDdE69SQDd6j9F5JAR1?n8lMi03e_jh:WTnW`[oLdoJPb:nf_5\d10&gt;E@R@8F?;Q8_7WU&lt;=&gt;RQ3UeiKX7]Z^?5kccV[KoGViG=lC6U]a]`hZ@c?TPI\d77iMcidQ]:PPX:DfW;Co:KkH0Vi5]D?IM:X0YETom=[F5N`2aQ@TS6?V=APERT0P&lt;F;=3\h3B26&gt;@lRj1m0P@Gh0JZ0BM@&lt;e;JSU?Mh@`Uh7:V3RLQ`J&lt;1C0Yeb&gt;[8g4oNcP5:D@I3]ReZN:Vm^58LW@1;523mMi^e`9_@NHTgH=U7EKif3YT_Q6_70lmTk_NmVW]li?e]2M`gJ&gt;UUlB&lt;LFOdoQjgid]hGR9lWYMfDo=1g2X7l</protected>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='21'>
			<Action classname='StepType' isroottypedef='true' typecategory='1' timestamp='1618215606' typeversion='21.0.0.2' typelastmodversion='21.0.0.0' typeminprodversion='21.0.0.0' typeflags='33554446'>
				<subprops>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs' flagsforinstances='524312' instanceoverrideflags='655384'>
						<value lbound='[0]' ubound='[]'/>
					</Substeps>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "ACTION_DESCRIPTION_NAME") + (("%ModuleDescription" == "") ? "" : ",  %ModuleDescription")</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "ACTION_DEF_STEP_NAME")</value>
					</DefaultNameFormat>
					<Menu typename='StepTypeMenu' xsi:type='StepTypeMenu' classname='Obj' flagsforinstances='524312' instanceoverrideflags='524312'>
						<subprops>
							<CanBeSubstepType classname='Bool'>
								<value>false</value>
							</CanBeSubstepType>
							<CanOnlyBeSubstepType classname='Bool'>
								<value>false</value>
							</CanOnlyBeSubstepType>
							<Category classname='Str'>
								<value>""</value>
							</Category>
							<ItemName classname='ExprValue'>
								<value>ResStr("NI_STEPTYPES", "ACTION_MENU_ITEM_NAME")</value>
							</ItemName>
							<SingularItemName classname='Str'>
								<value>""</value>
							</SingularItemName>
							<SeparatorBeforeCategory classname='Bool'>
								<value>false</value>
							</SeparatorBeforeCategory>
							<SeparatorBeforeItemName classname='Bool'>
								<value>false</value>
							</SeparatorBeforeItemName>
							<Group classname='Str'>
								<value>Action</value>
							</Group>
						</subprops>
					</Menu>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='NI_CustomResult' xsi:type='NI_CustomResult' name='' classname='CustomResult'>
									<subprops>
										<Name classname='ExprValue'>
											<value/>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value/>
										</ValueToLog>
										<Condition classname='ExprValue'>
											<value/>
										</Condition>
										<Flags classname='Num'>
											<value>8192</value>
										</Flags>
										<CheckedState classname='Num'>
											<value>2</value>
										</CheckedState>
										<Type classname='PropertyObjectType'>
											<subprops>
												<ValueType classname='Num'>
													<value>3</value>
												</ValueType>
												<IsObject classname='Bool'>
													<value>true</value>
												</IsObject>
												<TypeName classname='Str'>
													<value/>
												</TypeName>
												<ElementType classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</ElementType>
												<ArrayDimensions classname='ArrayDimensions'>
													<subprops>
														<LowerBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</LowerBounds>
														<UpperBounds classname='Nums'>
															<value lbound='[0]' ubound='[]'/>
														</UpperBounds>
													</subprops>
												</ArrayDimensions>
												<Representation classname='Num'>
													<value>1</value>
												</Representation>
												<ClassName classname='Str'>
													<value/>
												</ClassName>
											</subprops>
										</Type>
										<Elements classname='Objs'>
											<value lbound='[0]' ubound='[]'/>
										</Elements>
										<IsAnyType classname='Bool'>
											<value>true</value>
										</IsAnyType>
									</subprops>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='262168' instanceoverrideflags='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value/>
							</Icon>
							<SData classname='Obj' flagsforinstances='2097152' instanceoverrideflags='7143448' structureflags='2097152'/>
							<PreCond classname='ExprValue'>
								<value/>
							</PreCond>
							<LoadOpt classname='Str'>
								<value>PreloadWhenExecuted</value>
							</LoadOpt>
							<UnloadOpt classname='Str'>
								<value>UnloadWithFile</value>
							</UnloadOpt>
							<Mode classname='Str'>
								<value>Normal</value>
							</Mode>
							<WindowActivation classname='Str'>
								<value>None</value>
							</WindowActivation>
							<ResultOption classname='Num'>
								<value>1</value>
							</ResultOption>
							<StepFCSeqF classname='Bool'>
								<value>true</value>
							</StepFCSeqF>
							<IgnoreRTE classname='Bool'>
								<value>false</value>
							</IgnoreRTE>
							<UseMutex classname='Bool'>
								<value>false</value>
							</UseMutex>
							<MutexNameOrRef classname='ExprValue'>
								<value/>
							</MutexNameOrRef>
							<BatchSyncOpt classname='Num'>
								<value>0</value>
							</BatchSyncOpt>
							<SwitchEnabled classname='Bool'>
								<value>false</value>
							</SwitchEnabled>
							<VirtualDeviceName classname='ExprValue'>
								<value/>
							</VirtualDeviceName>
							<SwitchOperation classname='Num'>
								<value>1</value>
							</SwitchOperation>
							<RouteGroupConnect classname='ExprValue'>
								<value/>
							</RouteGroupConnect>
							<RouteGroupDisconnect classname='ExprValue'>
								<value/>
							</RouteGroupDisconnect>
							<MulticonnectMode classname='Num'>
								<value>1</value>
							</MulticonnectMode>
							<OperationOrder classname='Num'>
								<value>2</value>
							</OperationOrder>
							<ConnectionLifetime classname='Num'>
								<value>0</value>
							</ConnectionLifetime>
							<WaitForDebounce classname='Bool'>
								<value>true</value>
							</WaitForDebounce>
							<PassAct classname='Str' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value>Next</value>
							</PassAct>
							<FailAct classname='Str' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value>Next</value>
							</FailAct>
							<PassActTarget classname='ExprValue' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value/>
							</PassActTarget>
							<FailActTarget classname='ExprValue' flagsforinstances='1' instanceoverrideflags='5046297'>
								<value/>
							</FailActTarget>
							<CustExpr classname='ExprValue'>
								<value/>
							</CustExpr>
							<CustTrueAct classname='Str'>
								<value>Next</value>
							</CustTrueAct>
							<CustFalseAct classname='Str'>
								<value>Next</value>
							</CustFalseAct>
							<CustTrueActTarget classname='ExprValue'>
								<value/>
							</CustTrueActTarget>
							<CustFalseActTarget classname='ExprValue'>
								<value/>
							</CustFalseActTarget>
							<LoopType classname='Str'>
								<value>NoLooping</value>
							</LoopType>
							<LoopWhile classname='ExprValue'>
								<value/>
							</LoopWhile>
							<LoopStatus classname='ExprValue'>
								<value/>
							</LoopStatus>
							<LoopIncrement classname='ExprValue'>
								<value>RunState.LoopIndex += 1</value>
							</LoopIncrement>
							<LoopInitialize classname='ExprValue'>
								<value>RunState.LoopIndex = 0</value>
							</LoopInitialize>
							<LoopOpt classname='Num'>
								<value>0</value>
							</LoopOpt>
							<PreExpr classname='ExprValue'>
								<value/>
							</PreExpr>
							<PostExpr classname='ExprValue'>
								<value/>
							</PostExpr>
							<StatusExpr classname='ExprValue'>
								<value/>
							</StatusExpr>
							<CanSpecifyModule classname='Bool'>
								<value>true</value>
							</CanSpecifyModule>
							<CanEditCode classname='Bool'>
								<value>true</value>
							</CanEditCode>
							<CanEditModulePrototype classname='Bool'>
								<value>true</value>
							</CanEditModulePrototype>
							<CanEditParameterAdditionalResults classname='Bool'>
								<value>true</value>
							</CanEditParameterAdditionalResults>
							<PrecondIntExe classname='Num'>
								<value>0</value>
							</PrecondIntExe>
							<Requirements classname='Obj' flagsforinstances='1' valueflags='1' structureflags='2097152'>
								<subprops>
									<Links classname='Strs' flagsforinstances='71303168' instanceoverrideflags='72286233' valueflags='71303168'>
										<value lbound='[0]' ubound='[]'/>
									</Links>
								</subprops>
							</Requirements>
							<CustomResults classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</CustomResults>
							<AdditionalResultsHints classname='Objs'>
								<value lbound='[0]' ubound='[]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
											<subprops>
												<Name classname='ExprValue'>
													<value/>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value/>
												</ValueToLog>
												<Condition classname='ExprValue'>
													<value/>
												</Condition>
												<Flags classname='Num'>
													<value>8192</value>
												</Flags>
												<CheckedState classname='Num'>
													<value>2</value>
												</CheckedState>
												<Type classname='PropertyObjectType'>
													<subprops>
														<ValueType classname='Num'>
															<value>3</value>
														</ValueType>
														<IsObject classname='Bool'>
															<value>true</value>
														</IsObject>
														<TypeName classname='Str'>
															<value/>
														</TypeName>
														<ElementType classname='Objs'>
															<value lbound='[0]' ubound='[]'/>
														</ElementType>
														<ArrayDimensions classname='ArrayDimensions'>
															<subprops>
																<LowerBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</LowerBounds>
																<UpperBounds classname='Nums'>
																	<value lbound='[0]' ubound='[]'/>
																</UpperBounds>
															</subprops>
														</ArrayDimensions>
														<Representation classname='Num'>
															<value>1</value>
														</Representation>
														<ClassName classname='Str'>
															<value/>
														</ClassName>
													</subprops>
												</Type>
												<Elements classname='Objs'>
													<value lbound='[0]' ubound='[]'/>
												</Elements>
												<IsAnyType classname='Bool'>
													<value>true</value>
												</IsAnyType>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
								</value>
							</AdditionalResultsHints>
						</subprops>
					</TS>
					<NI_Data typename='StepTypeNIData' xsi:type='StepTypeNIData' classname='Obj'>
						<subprops>
							<EditPanels classname='Strs'>
								<value lbound='[0]' ubound='[]'/>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='4194304' valueflags='4194304'>
						<subprops>
							<Error typename='Error' xsi:type='Error' classname='Obj' flagsforinstances='4194304' instanceoverrideflags='4194304' valueflags='4194304'>
								<subprops>
									<Code classname='Num'>
										<value>0</value>
									</Code>
									<Msg classname='Str'>
										<value/>
									</Msg>
									<Occurred classname='Bool'>
										<value>false</value>
									</Occurred>
								</subprops>
							</Error>
							<Status classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</Status>
							<ReportText classname='Str' flagsforinstances='4194304' valueflags='4194304'>
								<value/>
							</ReportText>
							<Common typename='CommonResults' xsi:type='CommonResults' classname='Obj' instanceoverrideflags='4194304'/>
						</subprops>
					</Result>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>DefaultLabVIEW|DefaultLabVIEWNXG|DefaultCVI|DefaultVB.NET|DefaultCSharp.NET|DefaultC++.NET|DefaultVC++_Template|DefaultHTB72_Template|DefaultHTB80_Template|Default_Template</value>
					</CodeTemplates>
					<BlockStartTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockStartTypes>
					<BlockEndTypes classname='Str' valueflags='4194328' structureflags='524288'>
						<value/>
					</BlockEndTypes>
					<AppliesToBlockStructure classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</AppliesToBlockStructure>
					<CanEncapsulate classname='Bool' valueflags='4194328' structureflags='524288'>
						<value>false</value>
					</CanEncapsulate>
					<Category classname='Str' valueflags='24' structureflags='524288'>
						<value>Action</value>
					</Category>
				</subprops>
			</Action>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='24'>
			<NI_PythonParameterResult classname='PythonParameterResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Condition typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</Condition>
					<Flags classname='Num'>
						<value>8192</value>
						<numericfmt>%#x</numericfmt>
					</Flags>
					<CheckedState classname='Num'>
						<value>1</value>
					</CheckedState>
				</subprops>
			</NI_PythonParameterResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='23'>
			<NI_PythonParameter classname='CPythonParameter' isroottypedef='true' typecategory='3' timestamp='1650060872' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name classname='Str'>
						<value>_notNamed</value>
					</Name>
					<Type classname='Num'>
						<value>7</value>
					</Type>
					<ArgumentValue typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgumentValue>
					<ArgumentDisplayValue typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgumentDisplayValue>
					<AdditionalResults classname='Obj'>
						<subprops>
							<Input typename='NI_PythonParameterResult' xsi:type='NI_PythonParameterResult' classname='PythonParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Input>
							<Output typename='NI_PythonParameterResult' xsi:type='NI_PythonParameterResult' classname='PythonParameterResult'>
								<subprops>
									<Condition classname='ExprValue'>
										<value/>
									</Condition>
									<Flags classname='Num'>
										<value>8192</value>
									</Flags>
									<CheckedState classname='Num'>
										<value>1</value>
									</CheckedState>
								</subprops>
							</Output>
						</subprops>
					</AdditionalResults>
				</subprops>
			</NI_PythonParameter>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='22'>
			<PythonStepAdditions classname='CPythonModule' isroottypedef='true' typecategory='3' timestamp='1650060872' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<PythonCall classname='CPythonCall'>
						<subprops>
							<UseAdapterSettingsForInterpreterSession classname='Bool'>
								<value>true</value>
							</UseAdapterSettingsForInterpreterSession>
							<InterpreterSessionScope classname='Num'>
								<value>3</value>
							</InterpreterSessionScope>
							<PythonVersion classname='Str'>
								<value/>
							</PythonVersion>
							<PythonVirtualEnvironmentPath classname='Str'>
								<value/>
							</PythonVirtualEnvironmentPath>
							<InterpreterLocation typename='Expression' xsi:type='Expression' classname='ExprValue'>
								<value/>
							</InterpreterLocation>
							<CreateIfInterpreterDoesNotExist classname='Bool'>
								<value>true</value>
							</CreateIfInterpreterDoesNotExist>
							<ModulePath typename='Path' xsi:type='Path' classname='PathValue'>
								<value/>
							</ModulePath>
							<OperationType classname='Num'>
								<value>1</value>
							</OperationType>
							<OperationScope classname='Num'>
								<value>0</value>
							</OperationScope>
							<ClassName classname='Str'>
								<value/>
							</ClassName>
							<ClassInstanceLocation typename='Expression' xsi:type='Expression' classname='ExprValue'>
								<value/>
							</ClassInstanceLocation>
							<FunctionOrAttributeName classname='Str'>
								<value/>
							</FunctionOrAttributeName>
							<Parameters classname='Objs'>
								<value lbound='[0]' ubound='[0]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name='' classname='CPythonParameter' structureflags='131072'>
											<subprops>
												<Name classname='Str'>
													<value>_notNamed</value>
												</Name>
												<Type classname='Num'>
													<value>7</value>
												</Type>
												<ArgumentValue classname='ExprValue'>
													<value/>
												</ArgumentValue>
												<ArgumentDisplayValue classname='ExprValue'>
													<value/>
												</ArgumentDisplayValue>
												<AdditionalResults classname='Obj'>
													<subprops>
														<Input classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Input>
														<Output classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Output>
													</subprops>
												</AdditionalResults>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
									<value>
										<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
											<subprops>
												<Name classname='Str'>
													<value>Return Value</value>
												</Name>
												<Type classname='Num'>
													<value>7</value>
												</Type>
												<ArgumentValue classname='ExprValue'>
													<value/>
												</ArgumentValue>
												<ArgumentDisplayValue classname='ExprValue'>
													<value/>
												</ArgumentDisplayValue>
												<AdditionalResults classname='Obj'>
													<subprops>
														<Input classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Input>
														<Output classname='PythonParameterResult'>
															<subprops>
																<Condition classname='ExprValue'>
																	<value/>
																</Condition>
																<Flags classname='Num'>
																	<value>8192</value>
																</Flags>
																<CheckedState classname='Num'>
																	<value>1</value>
																</CheckedState>
															</subprops>
														</Output>
													</subprops>
												</AdditionalResults>
											</subprops>
										</CPythonParameter>
									</value>
								</value>
							</Parameters>
							<DefaultParamCategoryForArray classname='Num'>
								<value>5</value>
							</DefaultParamCategoryForArray>
						</subprops>
					</PythonCall>
				</subprops>
			</PythonStepAdditions>
		</typedef>
	</typelist>
	<Data classname='SequenceFileData' valueflags='4194304'>
		<subprops>
			<Seq classname='Objs' valueflags='4194304'>
				<value lbound='[0]' ubound='[0]'>
					<value>
						<Sequence name='MainSequence'>
							<subprops>
								<Parameters classname='Obj' valueflags='4456448'/>
								<Locals classname='Obj' valueflags='4194304'>
									<subprops>
										<ResultList classname='Objs' valueflags='4194304'>
											<value lbound='[0]' ubound='[]'>
												<elemproto>
													<_NAME_IN_ATTRIBUTE_ name='' classname='TEResult'/>
												</elemproto>
											</value>
										</ResultList>
									</subprops>
								</Locals>
								<Main classname='Objs' valueflags='4194304'>
									<value lbound='[0]' ubound='[0]'>
										<value>
											<Step typename='NI_Measurement' xsi:type='NI_Measurement' name='Generate a standard function waveform using an NI waveform generator'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:1m8fotxw7RGuNrjdh1OqZD</value>
															</Id>
															<Icon classname='Str'>
																<value>Measurement\Measurement.ico</value>
															</Icon>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>1</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>4</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
													<Measurement classname='Obj'>
														<subprops>
															<Name classname='Str'>
																<value>ni.examples.NIFgenStandardFunction_Python</value>
															</Name>
															<Parameters classname='Objs'>
																<value lbound='[0]' ubound='[4]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='Obj'>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value/>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value/>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value/>
																				</Direction>
																				<Log classname='Bool'>
																					<value>false</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value/>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>0</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value/>
																				</TypeSpecialization>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>pin_names</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>{"Pin1"}</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>1</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeString</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>1</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>IOResource</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>waveform_type</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>1i64</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeEnum</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>2</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>Enum</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[8]'>
																						<value>
																							<Num name='NONE'>
																								<value representation='Int64'>0</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='SINE'>
																								<value representation='Int64'>1</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='SQUARE'>
																								<value representation='Int64'>2</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='TRIANGLE'>
																								<value representation='Int64'>3</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='RAMP_UP'>
																								<value representation='Int64'>4</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='RAMP_DOWN'>
																								<value representation='Int64'>5</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='DC'>
																								<value representation='Int64'>6</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='NOISE'>
																								<value representation='Int64'>101</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='USER'>
																								<value representation='Int64'>102</value>
																							</Num>
																						</value>
																					</value>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>frequency</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>1000000</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>3</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>amplitude</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>2</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>4</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>duration</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>10</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>true</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>5</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>None</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</EnumDefinition>
																			</subprops>
																		</Obj>
																	</value>
																</value>
															</Parameters>
														</subprops>
													</Measurement>
												</subprops>
											</Step>
										</value>
									</value>
								</Main>
								<Setup classname='Objs' valueflags='4194304'>
									<value lbound='[0]' ubound='[1]'>
										<value>
											<Step typename='NI_UpdatePinMap' xsi:type='NI_UpdatePinMap' name='Update pin map'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:uyN+89OU7hGhxGDjK76h1B</value>
															</Id>
															<Icon classname='Str'>
																<value>NI_SequenceEditor\StepSettings\ni_UpdateMapping.ico</value>
															</Icon>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>4</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
													<PinMapPath classname='PathValue'>
														<value>"NIFgenStandardFunction.pinmap"</value>
													</PinMapPath>
												</subprops>
											</Step>
										</value>
										<value>
											<Step typename='Action' xsi:type='Action' name='Create and register NI-FGEN Sessions'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:c5USoqlx7RGuNrjdh1OqZD</value>
															</Id>
															<Icon classname='Str'>
																<value/>
															</Icon>
															<SData typename='PythonStepAdditions' xsi:type='PythonStepAdditions' classname='CPythonModule'>
																<subprops>
																	<PythonCall classname='CPythonCall'>
																		<subprops>
																			<UseAdapterSettingsForInterpreterSession classname='Bool'>
																				<value>false</value>
																			</UseAdapterSettingsForInterpreterSession>
																			<InterpreterSessionScope classname='Num'>
																				<value>2</value>
																			</InterpreterSessionScope>
																			<PythonVersion classname='Str'>
																				<value>3.10</value>
																			</PythonVersion>
																			<PythonVirtualEnvironmentPath classname='Str'>
																				<value>.venv</value>
																			</PythonVirtualEnvironmentPath>
																			<InterpreterLocation classname='ExprValue'>
																				<value/>
																			</InterpreterLocation>
																			<CreateIfInterpreterDoesNotExist classname='Bool'>
																				<value>true</value>
																			</CreateIfInterpreterDoesNotExist>
																			<ModulePath classname='PathValue'>
																				<value>teststand_nifgen.py</value>
																			</ModulePath>
																			<OperationType classname='Num'>
																				<value>1</value>
																			</OperationType>
																			<OperationScope classname='Num'>
																				<value>0</value>
																			</OperationScope>
																			<ClassName classname='Str'>
																				<value/>
																			</ClassName>
																			<ClassInstanceLocation classname='ExprValue'>
																				<value/>
																			</ClassInstanceLocation>
																			<FunctionOrAttributeName classname='Str'>
																				<value>create_nifgen_sessions</value>
																			</FunctionOrAttributeName>
																			<Parameters classname='Objs'>
																				<value lbound='[0]' ubound='[1]'>
																					<elemproto>
																						<_NAME_IN_ATTRIBUTE_ name='' classname='CPythonParameter' structureflags='0'/>
																					</elemproto>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>Return Value</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value/>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>sequence_context</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value>ThisContext</value>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>2</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																				</value>
																			</Parameters>
																			<DefaultParamCategoryForArray classname='Num'>
																				<value>5</value>
																			</DefaultParamCategoryForArray>
																		</subprops>
																	</PythonCall>
																</subprops>
															</SData>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>0</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
												</subprops>
											</Step>
										</value>
									</value>
								</Setup>
								<Cleanup classname='Objs' valueflags='4194304'>
									<value lbound='[0]' ubound='[0]'>
										<value>
											<Step typename='Action' xsi:type='Action' name='Destroy and unregister NI-FGEN sessions'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:syCDFOVw7RGuNrjdh1OqZD</value>
															</Id>
															<Icon classname='Str'>
																<value/>
															</Icon>
															<SData typename='PythonStepAdditions' xsi:type='PythonStepAdditions' classname='CPythonModule'>
																<subprops>
																	<PythonCall classname='CPythonCall'>
																		<subprops>
																			<UseAdapterSettingsForInterpreterSession classname='Bool'>
																				<value>false</value>
																			</UseAdapterSettingsForInterpreterSession>
																			<InterpreterSessionScope classname='Num'>
																				<value>2</value>
																			</InterpreterSessionScope>
																			<PythonVersion classname='Str'>
																				<value>3.10</value>
																			</PythonVersion>
																			<PythonVirtualEnvironmentPath classname='Str'>
																				<value>.venv</value>
																			</PythonVirtualEnvironmentPath>
																			<InterpreterLocation classname='ExprValue'>
																				<value/>
																			</InterpreterLocation>
																			<CreateIfInterpreterDoesNotExist classname='Bool'>
																				<value>true</value>
																			</CreateIfInterpreterDoesNotExist>
																			<ModulePath classname='PathValue'>
																				<value>teststand_nifgen.py</value>
																			</ModulePath>
																			<OperationType classname='Num'>
																				<value>1</value>
																			</OperationType>
																			<OperationScope classname='Num'>
																				<value>0</value>
																			</OperationScope>
																			<ClassName classname='Str'>
																				<value/>
																			</ClassName>
																			<ClassInstanceLocation classname='ExprValue'>
																				<value/>
																			</ClassInstanceLocation>
																			<FunctionOrAttributeName classname='Str'>
																				<value>destroy_nifgen_sessions</value>
																			</FunctionOrAttributeName>
																			<Parameters classname='Objs'>
																				<value lbound='[0]' ubound='[0]'>
																					<elemproto>
																						<_NAME_IN_ATTRIBUTE_ name='' classname='CPythonParameter' structureflags='0'/>
																					</elemproto>
																					<value>
																						<CPythonParameter typename='NI_PythonParameter' xsi:type='NI_PythonParameter' name=''>
																							<subprops>
																								<Name classname='Str'>
																									<value>Return Value</value>
																								</Name>
																								<Type classname='Num'>
																									<value>7</value>
																								</Type>
																								<ArgumentValue classname='ExprValue'>
																									<value/>
																								</ArgumentValue>
																								<ArgumentDisplayValue classname='ExprValue'>
																									<value/>
																								</ArgumentDisplayValue>
																								<AdditionalResults classname='Obj'>
																									<subprops>
																										<Input classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Input>
																										<Output classname='PythonParameterResult'>
																											<subprops>
																												<Condition classname='ExprValue'>
																													<value/>
																												</Condition>
																												<Flags classname='Num'>
																													<value>8192</value>
																												</Flags>
																												<CheckedState classname='Num'>
																													<value>1</value>
																												</CheckedState>
																											</subprops>
																										</Output>
																									</subprops>
																								</AdditionalResults>
																							</subprops>
																						</CPythonParameter>
																					</value>
																				</value>
																			</Parameters>
																			<DefaultParamCategoryForArray classname='Num'>
																				<value>5</value>
																			</DefaultParamCategoryForArray>
																		</subprops>
																	</PythonCall>
																</subprops>
															</SData>
															<PreCond classname='ExprValue'>
																<value/>
															</PreCond>
															<LoadOpt classname='Str'>
																<value>PreloadWhenExecuted</value>
															</LoadOpt>
															<UnloadOpt classname='Str'>
																<value>UnloadWithFile</value>
															</UnloadOpt>
															<Mode classname='Str'>
																<value>Normal</value>
															</Mode>
															<WindowActivation classname='Str'>
																<value>None</value>
															</WindowActivation>
															<ResultOption classname='Num'>
																<value>0</value>
															</ResultOption>
															<StepFCSeqF classname='Bool'>
																<value>true</value>
															</StepFCSeqF>
															<IgnoreRTE classname='Bool'>
																<value>false</value>
															</IgnoreRTE>
															<UseMutex classname='Bool'>
																<value>false</value>
															</UseMutex>
															<MutexNameOrRef classname='ExprValue'>
																<value/>
															</MutexNameOrRef>
															<BatchSyncOpt classname='Num'>
																<value>0</value>
															</BatchSyncOpt>
															<SwitchEnabled classname='Bool'>
																<value>false</value>
															</SwitchEnabled>
															<VirtualDeviceName classname='ExprValue'>
																<value/>
															</VirtualDeviceName>
															<SwitchOperation classname='Num'>
																<value>1</value>
															</SwitchOperation>
															<RouteGroupConnect classname='ExprValue'>
																<value/>
															</RouteGroupConnect>
															<RouteGroupDisconnect classname='ExprValue'>
																<value/>
															</RouteGroupDisconnect>
															<MulticonnectMode classname='Num'>
																<value>1</value>
															</MulticonnectMode>
															<OperationOrder classname='Num'>
																<value>2</value>
															</OperationOrder>
															<ConnectionLifetime classname='Num'>
																<value>0</value>
															</ConnectionLifetime>
															<WaitForDebounce classname='Bool'>
																<value>true</value>
															</WaitForDebounce>
															<PassAct classname='Str'>
																<value>Next</value>
															</PassAct>
															<FailAct classname='Str'>
																<value>Next</value>
															</FailAct>
															<PassActTarget classname='ExprValue'>
																<value/>
															</PassActTarget>
															<FailActTarget classname='ExprValue'>
																<value/>
															</FailActTarget>
															<CustExpr classname='ExprValue'>
																<value/>
															</CustExpr>
															<CustTrueAct classname='Str'>
																<value>Next</value>
															</CustTrueAct>
															<CustFalseAct classname='Str'>
																<value>Next</value>
															</CustFalseAct>
															<CustTrueActTarget classname='ExprValue'>
																<value/>
															</CustTrueActTarget>
															<CustFalseActTarget classname='ExprValue'>
																<value/>
															</CustFalseActTarget>
															<LoopType classname='Str'>
																<value>NoLooping</value>
															</LoopType>
															<LoopWhile classname='ExprValue'>
																<value/>
															</LoopWhile>
															<LoopStatus classname='ExprValue'>
																<value/>
															</LoopStatus>
															<LoopIncrement classname='ExprValue'>
																<value>RunState.LoopIndex += 1</value>
															</LoopIncrement>
															<LoopInitialize classname='ExprValue'>
																<value>RunState.LoopIndex = 0</value>
															</LoopInitialize>
															<LoopOpt classname='Num'>
																<value>0</value>
															</LoopOpt>
															<PreExpr classname='ExprValue'>
																<value/>
															</PreExpr>
															<PostExpr classname='ExprValue'>
																<value/>
															</PostExpr>
															<StatusExpr classname='ExprValue'>
																<value/>
															</StatusExpr>
															<CanSpecifyModule classname='Bool'>
																<value>true</value>
															</CanSpecifyModule>
															<CanEditCode classname='Bool'>
																<value>true</value>
															</CanEditCode>
															<CanEditModulePrototype classname='Bool'>
																<value>true</value>
															</CanEditModulePrototype>
															<CanEditParameterAdditionalResults classname='Bool'>
																<value>true</value>
															</CanEditParameterAdditionalResults>
															<PrecondIntExe classname='Num'>
																<value>0</value>
															</PrecondIntExe>
															<CustomResults classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[]'>
																	<elemproto>
																		<_NAME_IN_ATTRIBUTE_ name='' classname='CustomResult'>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value/>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value/>
																				</ValueToLog>
																				<Condition classname='ExprValue'>
																					<value/>
																				</Condition>
																				<Flags classname='Num'>
																					<value>8192</value>
																				</Flags>
																				<CheckedState classname='Num'>
																					<value>2</value>
																				</CheckedState>
																				<Type classname='PropertyObjectType'>
																					<subprops>
																						<ValueType classname='Num'>
																							<value>3</value>
																						</ValueType>
																						<IsObject classname='Bool'>
																							<value>true</value>
																						</IsObject>
																						<TypeName classname='Str'>
																							<value/>
																						</TypeName>
																						<ElementType classname='Objs'>
																							<value lbound='[0]' ubound='[]'/>
																						</ElementType>
																						<ArrayDimensions classname='ArrayDimensions'>
																							<subprops>
																								<LowerBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</LowerBounds>
																								<UpperBounds classname='Nums'>
																									<value lbound='[0]' ubound='[]'/>
																								</UpperBounds>
																							</subprops>
																						</ArrayDimensions>
																						<Representation classname='Num'>
																							<value>1</value>
																						</Representation>
																						<ClassName classname='Str'>
																							<value/>
																						</ClassName>
																					</subprops>
																				</Type>
																				<Elements classname='Objs'>
																					<value lbound='[0]' ubound='[]'/>
																				</Elements>
																				<IsAnyType classname='Bool'>
																					<value>true</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<Result classname='Obj'>
														<subprops>
															<Error classname='Obj'>
																<subprops>
																	<Code classname='Num'>
																		<value>0</value>
																	</Code>
																	<Msg classname='Str'>
																		<value/>
																	</Msg>
																	<Occurred classname='Bool'>
																		<value>false</value>
																	</Occurred>
																</subprops>
															</Error>
															<Status classname='Str'>
																<value/>
															</Status>
															<ReportText classname='Str'>
																<value/>
															</ReportText>
															<Common classname='Obj'/>
														</subprops>
													</Result>
												</subprops>
											</Step>
										</value>
									</value>
								</Cleanup>
								<RecordResults classname='Bool' valueflags='4194312'>
									<value>true</value>
								</RecordResults>
								<RTS classname='Obj' valueflags='4456456'>
									<subprops>
										<Type classname='Num' valueflags='4194304'>
											<value>0</value>
										</Type>
										<OptimizeNonReentrantCalls classname='Bool' valueflags='4194304'>
											<value>true</value>
										</OptimizeNonReentrantCalls>
										<EPNameExpr classname='Str' valueflags='4194304'>
											<value>"Unnamed Entry Point"</value>
										</EPNameExpr>
										<EPEnabledExpr classname='Str' valueflags='4194304'>
											<value>True</value>
										</EPEnabledExpr>
										<EPMenuHint classname='Str' valueflags='4194304'>
											<value/>
										</EPMenuHint>
										<EPIgnoreClient classname='Bool' valueflags='4194304'>
											<value>false</value>
										</EPIgnoreClient>
										<EPInitiallyHidden classname='Bool' valueflags='4194304'>
											<value>false</value>
										</EPInitiallyHidden>
										<EPCheckToSaveTitledFile classname='Bool' valueflags='4194304'>
											<value>true</value>
										</EPCheckToSaveTitledFile>
										<ShowEPAlways classname='Bool' valueflags='4194304'>
											<value>false</value>
										</ShowEPAlways>
										<ShowEPForFileWin classname='Bool' valueflags='4194304'>
											<value>true</value>
										</ShowEPForFileWin>
										<ShowEPForExeWin classname='Bool' valueflags='4194304'>
											<value>false</value>
										</ShowEPForExeWin>
										<ShowEPForEditorOnly classname='Bool' valueflags='4194304'>
											<value>false</value>
										</ShowEPForEditorOnly>
										<AllowIntExeOfEP classname='Bool' valueflags='4194304'>
											<value>false</value>
										</AllowIntExeOfEP>
										<CopyStepsOnOverriding classname='Bool' valueflags='4194304'>
											<value>true</value>
										</CopyStepsOnOverriding>
										<Priority classname='Num' valueflags='4194304'>
											<value>2953567917</value>
										</Priority>
									</subprops>
								</RTS>
								<Requirements classname='Obj' valueflags='4456456'>
									<subprops>
										<Links classname='Strs' valueflags='71303168'>
											<value lbound='[0]' ubound='[]'/>
										</Links>
									</subprops>
								</Requirements>
								<FailureAction classname='Num' valueflags='4194312'>
									<value>2</value>
								</FailureAction>
							</subprops>
						</Sequence>
					</value>
				</value>
			</Seq>
			<FileGlobalDefaults classname='Obj' valueflags='4194304'>
				<subprops>
					<MeasurementPlugIns classname='Obj'>
						<subprops>
							<EnableMonitoring classname='Bool'>
								<value>false</value>
							</EnableMonitoring>
						</subprops>
					</MeasurementPlugIns>
				</subprops>
			</FileGlobalDefaults>
			<ModelFile typename='Path' xsi:type='Path' classname='PathValue' valueflags='4194312'>
				<value/>
			</ModelFile>
			<LoadOpt classname='Str' valueflags='4194312'>
				<value>UseStepLoadOpt</value>
			</LoadOpt>
			<UnloadOpt classname='Str' valueflags='4194312'>
				<value>UseStepUnloadOpt</value>
			</UnloadOpt>
			<Version classname='Str' valueflags='4194312'>
				<value>0.0.0.0</value>
			</Version>
			<BatchSync classname='Num' valueflags='4194312'>
				<value>1</value>
			</BatchSync>
			<SFGlobalsScope classname='Num' valueflags='4194312'>
				<value>0</value>
			</SFGlobalsScope>
			<Type classname='Num' valueflags='4194312'>
				<value>0</value>
			</Type>
			<ModelOption classname='Num' valueflags='4194312'>
				<value>0</value>
			</ModelOption>
			<Requirements classname='Obj' valueflags='4194305'>
				<subprops>
					<Links classname='Strs' valueflags='71303168'>
						<value lbound='[0]' ubound='[]'/>
					</Links>
				</subprops>
			</Requirements>
		</subprops>
	</Data>
</teststandfileheader>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nifgen_standard_function/NIFgenStandardFunctionMultiSite.pinmap sha256=8652493adc3ac5319dc4478f581b83eeda3df0000ce4f2faed32f573c920725e bytes=885 -->
## FILE: examples/nifgen_standard_function/NIFgenStandardFunctionMultiSite.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nifgen_standard_function/NIFgenStandardFunctionMultiSite.pinmap`
- sha256: `8652493adc3ac5319dc4478f581b83eeda3df0000ce4f2faed32f573c920725e`
- bytes: 885

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.1">
	<Instruments>
		<NIFGenInstrument name="FGEN1" numberOfChannels="2" />
		<NIFGenInstrument name="FGEN2" numberOfChannels="2" />
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
		<Site siteNumber="2" />
		<Site siteNumber="3" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="FGEN1" channel="0" />
		<Connection pin="Pin1" siteNumber="1" instrument="FGEN1" channel="1" />
		<Connection pin="Pin1" siteNumber="2" instrument="FGEN2" channel="0" />
		<Connection pin="Pin1" siteNumber="3" instrument="FGEN2" channel="1" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nifgen_standard_function/poetry.toml sha256=ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e bytes=34 -->
## FILE: examples/nifgen_standard_function/poetry.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nifgen_standard_function/poetry.toml`
- sha256: `ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e`
- bytes: 34

````toml
[virtualenvs]
in-project = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nifgen_standard_function/pyproject.toml sha256=e172685398bd33543116c2cc1d5192ff3b44757b218f0e071eed72d9216a0f4f bytes=1145 -->
## FILE: examples/nifgen_standard_function/pyproject.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nifgen_standard_function/pyproject.toml`
- sha256: `e172685398bd33543116c2cc1d5192ff3b44757b218f0e071eed72d9216a0f4f`
- bytes: 1145

````toml
[tool.poetry]
name = "nifgen_standard_function"
version = "0.5.0"
package-mode = false
description = "Measurement plug-in example that generates a standard function waveform using an NI waveform generator."
authors = ["National Instruments"]

[tool.poetry.dependencies]
python = "^3.10"
nifgen = { version = ">=1.4.4", extras = ["grpc"] }
ni-measurement-plugin-sdk-service = {version = ">=2.3.1,<4.0"}
click = ">=7.1.2, !=8.1.4" # mypy fails with click 8.1.4: https://github.com/pallets/click/issues/2558
grpcio = "*"

[tool.poetry.group.dev.dependencies]
ni-python-styleguide = ">=0.4.1"
mypy = ">=1.0"
types-grpcio = ">=1.0"
# Uncomment to use prerelease dependencies.
# nifgen = { git = "https://github.com/ni/nimi-python.git", subdirectory = "generated/nifgen", extras = ["grpc"] }
# ni-measurement-plugin-sdk-service = {path = "../../packages/service", develop = true}

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.mypy]
disallow_untyped_defs = true

[[tool.mypy.overrides]]
module = [
    "hightime.*",
    "nifgen.*",
]
ignore_missing_imports = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nifgen_standard_function/README.md sha256=dec36d169d7d25ad45df5eaf3becbfa51043a411e56f7ff5c18e9d48dedd523b bytes=2176 -->
## FILE: examples/nifgen_standard_function/README.md

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nifgen_standard_function/README.md`
- sha256: `dec36d169d7d25ad45df5eaf3becbfa51043a411e56f7ff5c18e9d48dedd523b`
- bytes: 2176

````markdown
## NI-FGEN Standard Function

This is a measurement plug-in example that generates a standard function waveform
using an NI waveform generator.

### Features

- Uses the `nifgen` package to access NI-FGEN from Python
- Demonstrates how to cancel a running measurement by breaking a long wait into
  multiple short waits
- Pin-aware, supporting multiple sessions, multiple pins, and multiple selected
  sites
  - Outputs the same waveform configuration on all selected pin/site
    combinations
  - Does not synchronize waveforms
- Includes InstrumentStudio and Measurement Plug-In UI Editor project files
- Includes a TestStand sequence showing how to configure the pin map, register
  instrument sessions with the session management service, and run a measurement
  - For the sake of simplicity, the TestStand sequence handles pin map and
    session registration and unregistration in the `Setup` and `Cleanup`
    sections of the main sequence. For **Test UUTs** and batch process model use
    cases, these steps should be moved to the `ProcessSetup` and
    `ProcessCleanup` callbacks.
- Uses the NI gRPC Device Server to allow sharing instrument sessions with other
  measurement services when running measurements from TestStand

### Required Software

- InstrumentStudio 2025 Q1 or later
- NI-FGEN
- Recommended: TestStand 2021 SP1 or later

### Required Hardware

This example requires an NI waveform generator (e.g. PXIe-5423 (2CH)).

By default, this example uses a physical instrument or a simulated instrument
created in NI MAX. To automatically simulate an instrument without using NI MAX,
follow the steps below:
- Create a `.env` file in the measurement service's directory or one of its
  parent directories (such as the root of your Git repository or
  `C:\ProgramData\National Instruments\Plug-Ins\Measurements` for statically
  registered measurement services).
- Add the following options to the `.env` file to enable simulation via the
  driver's option string:

  ```
  MEASUREMENT_PLUGIN_NIFGEN_SIMULATE=1
  MEASUREMENT_PLUGIN_NIFGEN_BOARD_TYPE=PXIe
  MEASUREMENT_PLUGIN_NIFGEN_MODEL=5423 (2CH)
  ```
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nifgen_standard_function/start.bat sha256=bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851 bytes=253 -->
## FILE: examples/nifgen_standard_function/start.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nifgen_standard_function/start.bat`
- sha256: `bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851`
- bytes: 253

````batch
@echo off
REM The discovery service uses this script to start the measurement service.
REM You can customize this script for your Python setup. The -v option logs
REM messages with level INFO and above.

.venv\Scripts\python.exe measurement.py -v
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nifgen_standard_function/teststand_nifgen.py sha256=547424887371a2726a9204d9c25ac6a5cba53cc9d44c70f13d5642a387d7fb85 bytes=2609 -->
## FILE: examples/nifgen_standard_function/teststand_nifgen.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nifgen_standard_function/teststand_nifgen.py`
- sha256: `547424887371a2726a9204d9c25ac6a5cba53cc9d44c70f13d5642a387d7fb85`
- bytes: 2609

````python
"""Functions to set up and tear down sessions of NI-FGEN devices in NI TestStand."""

from typing import Any

from _helpers import TestStandSupport
from ni_measurement_plugin_sdk_service.discovery import DiscoveryClient
from ni_measurement_plugin_sdk_service.grpc.channelpool import GrpcChannelPool
from ni_measurement_plugin_sdk_service.session_management import (
    INSTRUMENT_TYPE_NI_FGEN,
    PinMapContext,
    SessionInitializationBehavior,
    SessionManagementClient,
)


def create_nifgen_sessions(sequence_context: Any) -> None:
    """Create and register all NI-FGEN sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    """
    with GrpcChannelPool() as grpc_channel_pool:
        teststand_support = TestStandSupport(sequence_context)
        pin_map_id = teststand_support.get_active_pin_map_id()
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=None)

        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with session_management_client.reserve_sessions(
            pin_map_context,
            instrument_type_id=INSTRUMENT_TYPE_NI_FGEN,
        ) as reservation:
            with reservation.initialize_nifgen_sessions(
                initialization_behavior=SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH
            ):
                pass

            session_management_client.register_sessions(reservation.session_info)


def destroy_nifgen_sessions() -> None:
    """Destroy and unregister all NI-FGEN sessions."""
    with GrpcChannelPool() as grpc_channel_pool:
        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with session_management_client.reserve_all_registered_sessions(
            instrument_type_id=INSTRUMENT_TYPE_NI_FGEN,
        ) as reservation:
            if not reservation.session_info:
                return

            session_management_client.unregister_sessions(reservation.session_info)

            with reservation.initialize_nifgen_sessions(
                initialization_behavior=SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE
            ):
                pass
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niscope_acquire_waveform/.serviceignore sha256=997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912 bytes=148 -->
## FILE: examples/niscope_acquire_waveform/.serviceignore

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niscope_acquire_waveform/.serviceignore`
- sha256: `997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912`
- bytes: 148

````text
# This file specifies that when we publish this plug-in to a plug-in library,
# we should not copy the following directories:
.venv
__pycache__
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niscope_acquire_waveform/_helpers.py sha256=0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426 bytes=2920 -->
## FILE: examples/niscope_acquire_waveform/_helpers.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niscope_acquire_waveform/_helpers.py`
- sha256: `0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426`
- bytes: 2920

````python
"""Helper classes and functions for measurement plug-in examples."""

from __future__ import annotations

import logging
import pathlib
from typing import Any, Callable, TypeVar

import click


class TestStandSupport:
    """Class that communicates with TestStand."""

    _PIN_MAP_ID_VAR = "NI.MeasurementPlugIns.PinMapId"

    def __init__(self, sequence_context: Any) -> None:
        """Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        """
        self._sequence_context = sequence_context

    def get_active_pin_map_id(self) -> str:
        """Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        """
        run_time_variables = self._sequence_context.Execution.RunTimeVariables
        if not run_time_variables.Exists(self._PIN_MAP_ID_VAR, 0x0):
            return ""
        return run_time_variables.GetValString(self._PIN_MAP_ID_VAR, 0x0)

    def resolve_file_path(self, file_path: str) -> str:
        """Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        """
        if pathlib.Path(file_path).is_absolute():
            return file_path
        (_, absolute_path, _, _, user_canceled) = self._sequence_context.Engine.FindFileEx(
            fileToFind=file_path,
            absolutePath=None,
            srchDirType=None,
            searchDirectoryIndex=None,
            userCancelled=None,  # Must match spelling used by TestStand
            searchContext=self._sequence_context.SequenceFile,
        )
        if user_canceled:
            raise RuntimeError("File lookup canceled by user.")
        return absolute_path


def configure_logging(verbosity: int) -> None:
    """Configure logging for this process."""
    if verbosity > 1:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=level)


F = TypeVar("F", bound=Callable)


def verbosity_option(func: F) -> F:
    """Decorator for --verbose command line option."""
    return click.option(
        "-v",
        "--verbose",
        "verbosity",
        count=True,
        help="Enable verbose logging. Repeat to increase verbosity.",
    )(func)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niscope_acquire_waveform/install.bat sha256=695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025 bytes=205 -->
## FILE: examples/niscope_acquire_waveform/install.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niscope_acquire_waveform/install.bat`
- sha256: `695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025`
- bytes: 205

````batch
@echo off
REM The discovery service uses this script to install the dependencies
REM for the measurement service. You can customize this script for your
REM Python setup.

poetry install --only main
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niscope_acquire_waveform/measurement.py sha256=733fb0e951788c85a2f010d3231c2289579108cc17f34500b6f14409ff3132d1 bytes=7188 -->
## FILE: examples/niscope_acquire_waveform/measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niscope_acquire_waveform/measurement.py`
- sha256: `733fb0e951788c85a2f010d3231c2289579108cc17f34500b6f14409ff3132d1`
- bytes: 7188

````python
"""Acquire a waveform using an NI oscilloscope."""

import logging
import pathlib
import sys
import threading
import time
from collections.abc import Sequence

import click
import grpc
import ni_measurement_plugin_sdk_service as nims
import niscope
from _helpers import configure_logging, verbosity_option

script_or_exe = sys.executable if getattr(sys, "frozen", False) else __file__
service_directory = pathlib.Path(script_or_exe).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "NIScopeAcquireWaveform.serviceconfig",
    ui_file_paths=[service_directory / "NIScopeAcquireWaveform.measui"],
)


@measurement_service.register_measurement
@measurement_service.configuration(
    "measurement_pins",
    nims.DataType.IOResourceArray1D,
    ["PinGroup1"],
    instrument_type=nims.session_management.INSTRUMENT_TYPE_NI_SCOPE,
)
@measurement_service.configuration("vertical_range", nims.DataType.Double, 5.0)
@measurement_service.configuration(
    "vertical_coupling",
    nims.DataType.Enum,
    niscope.VerticalCoupling.DC,
    enum_type=niscope.VerticalCoupling,
)
@measurement_service.configuration("input_impedance", nims.DataType.Double, 1e6)
@measurement_service.configuration("min_sample_rate", nims.DataType.Double, 10e6)
@measurement_service.configuration("min_record_length", nims.DataType.Int32, 40000)
@measurement_service.configuration(
    "trigger_pin",
    nims.DataType.IOResource,
    "Pin1",
    instrument_type=nims.session_management.INSTRUMENT_TYPE_NI_SCOPE,
)
@measurement_service.configuration("trigger_level", nims.DataType.Double, 0.5)
@measurement_service.configuration(
    "trigger_slope",
    nims.DataType.Enum,
    niscope.TriggerSlope.POSITIVE,
    enum_type=niscope.TriggerSlope,
)
@measurement_service.configuration("auto_trigger", nims.DataType.Boolean, False)
@measurement_service.configuration(
    "trigger_coupling",
    nims.DataType.Enum,
    niscope.TriggerCoupling.DC,
    enum_type=niscope.TriggerCoupling,
)
@measurement_service.configuration("timeout", nims.DataType.Double, 5.0)
@measurement_service.output("waveform0", nims.DataType.DoubleArray1D)
@measurement_service.output("waveform1", nims.DataType.DoubleArray1D)
@measurement_service.output("waveform2", nims.DataType.DoubleArray1D)
@measurement_service.output("waveform3", nims.DataType.DoubleArray1D)
def measure(
    measurement_pins: Sequence[str],
    vertical_range: float,
    vertical_coupling: str,
    input_impedance: float,
    min_sample_rate: float,
    min_record_length: int,
    trigger_pin: str,
    trigger_level: float,
    trigger_slope: str,
    auto_trigger: bool,
    trigger_coupling: str,
    timeout: float,
) -> tuple[list[float], ...]:
    """Acquire a waveform using an NI oscilloscope."""
    logging.info(
        "Starting acquisition: measurement_pins=%s vertical_range=%g trigger_pin=%s trigger_level=%g",
        measurement_pins,
        vertical_range,
        trigger_pin,
        trigger_level,
    )

    cancellation_event = threading.Event()
    measurement_service.context.add_cancel_callback(cancellation_event.set)

    with measurement_service.context.reserve_session(
        list(measurement_pins) + [trigger_pin]
    ) as reservation:
        with reservation.initialize_niscope_session() as session_info:
            # Use connections to map pin names to channel names. This sets the
            # channel order based on the pin order and allows mapping the
            # resulting measurements back to the corresponding pins and sites.
            connections = reservation.get_niscope_connections(measurement_pins)
            channel_order = ",".join(connection.channel_name for connection in connections)
            trigger_connection = reservation.get_niscope_connection(trigger_pin)

            # Start with all channels in the session disabled. Some channels may
            # be connected to other pins or sites.
            session = session_info.session
            session.channels[""].channel_enabled = False

            # Enable and configure all channels corresponding to the selected
            # pins and site(s).
            session.channels[channel_order].configure_vertical(
                vertical_range, vertical_coupling, enabled=True
            )
            session.channels[channel_order].configure_chan_characteristics(
                input_impedance, max_input_frequency=0.0
            )

            # Configure timing and triggering for the acquisition.
            session.configure_horizontal_timing(
                min_sample_rate,
                min_record_length,
                ref_position=50.0,
                num_records=1,
                enforce_realtime=True,
            )
            session.configure_trigger_edge(
                trigger_connection.channel_name,
                trigger_level,
                trigger_coupling,
                trigger_slope,
            )
            session.trigger_modifier = (
                niscope.TriggerModifier.AUTO
                if auto_trigger
                else niscope.TriggerModifier.NO_TRIGGER_MOD
            )

            # Initiate the acquisition. initiate() returns a context manager
            # that aborts the measurement when the function returns or raises an
            # exception.
            with session.initiate():
                _wait_until_done(session, cancellation_event, timeout)
                waveform_infos = session.channels[channel_order].fetch()

    logging.info("Completed acquisition")
    return tuple(w.samples for w in waveform_infos)


def _wait_until_done(
    session: niscope.Session,
    cancellation_event: threading.Event,
    timeout: float,
) -> None:
    """Wait until the acquisition is done or error/cancellation occurs."""
    grpc_deadline = time.time() + measurement_service.context.time_remaining
    user_deadline = time.time() + timeout
    deadline = min(grpc_deadline, user_deadline)

    while True:
        if time.time() > user_deadline:
            raise TimeoutError("User timeout expired.")
        if time.time() > grpc_deadline:
            measurement_service.context.abort(
                grpc.StatusCode.DEADLINE_EXCEEDED, "Deadline exceeded."
            )
        if cancellation_event.is_set():
            measurement_service.context.abort(
                grpc.StatusCode.CANCELLED, "Client requested cancellation."
            )

        status = session.acquisition_status()
        if status == niscope.AcquisitionStatus.COMPLETE:
            break

        remaining_time = max(deadline - time.time(), 0.0)
        sleep_time = min(remaining_time, 10e-3)
        time.sleep(sleep_time)


@click.command
@verbosity_option
def main(verbosity: int) -> None:
    """Acquire a waveform using an NI oscilloscope."""
    configure_logging(verbosity)

    with measurement_service.host_service():
        input("Press enter to close the measurement service.\n")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niscope_acquire_waveform/NIScopeAcquireWaveform.instudioproj sha256=ffa14f0fb80de89c1987a9a0f1839ed955e0aca84b7160a89f542bb10b98e431 bytes=2035 -->
## FILE: examples/niscope_acquire_waveform/NIScopeAcquireWaveform.instudioproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niscope_acquire_waveform/NIScopeAcquireWaveform.instudioproj`
- sha256: `ffa14f0fb80de89c1987a9a0f1839ed955e0aca84b7160a89f542bb10b98e431`
- bytes: 2035

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="E52EB8F323DBEED9FDACF6A5F2145E82D614185DF5146B64E35371B1010F57CD48DD2D913AE1CFCE815DD6AB530B84953250BF9F74E29416E347FBA7918EC16B" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.0.0.2317" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2317" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.2317" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="23.0.0.2317" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="f53d543da7be447d977505512a9de1b1" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="7a73cec96722445aaeae940b880f627c" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="f0fd0a1d98c944258fd0797c80775378" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<FileReference Id="10bfd58a002e4201845462e1ed522446" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="NIScopeAcquireWaveform.pinmap" StoragePath="NIScopeAcquireWaveform.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
			<SourceFileReference Bindings="EnvoyManager" Id="f7688179510a4167839887c6eea5288c" ModelDefinitionType="NationalInstruments.InstrumentFramework.Document.SourceModel.UnifiedTask" Name="NIScopeAcquireWaveform.sfp" StoragePath="NIScopeAcquireWaveform.sfp" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niscope_acquire_waveform/NIScopeAcquireWaveform.measproj sha256=db4d3be62b2b81c085bf07395e16eb98a61d4c48f6e29efad03eaa8dbe03ad04 bytes=3824 -->
## FILE: examples/niscope_acquire_waveform/NIScopeAcquireWaveform.measproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niscope_acquire_waveform/NIScopeAcquireWaveform.measproj`
- sha256: `db4d3be62b2b81c085bf07395e16eb98a61d4c48f6e29efad03eaa8dbe03ad04`
- bytes: 3824

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="F27336B7BC10F9D08249AE635991E236751A2B1FABD3139FE59A8A5239BD554FE9DB863D84AEB62422FD7862D884EB7001C98A7F71011D4548514D3568F7284C" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.0.0.1849" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="23.0.0.1849" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.1849" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.1849" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/EnvoyManagement" OldestCompatibleVersion="5.0.0.0" Version="5.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.1849" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemDiagram" OldestCompatibleVersion="8.0.0.49152" Version="8.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.1849" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemModelCore" OldestCompatibleVersion="5.1.0.5" Version="5.2.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.1849" Name="MeasurementLink UI Editor" Version="23.0.0.1849" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="da4cd1d914354e11b0387be34f755295" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="c39e3701f5824cb0a30e9c9a09a23568" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<EmbeddedDefinitionReference Id="edc367d7e4d64f6d8bbb1ba36e4eb8d3" ModelDefinitionType="NationalInstruments.SystemDesigner.SystemDiagram.SystemDiagramDefinition" Name="SystemDiagram">
			<SystemDiagram Id="f37e9886becf42e2a815979184f4ab74" SystemDiagramVersion="75" xmlns="http://www.ni.com/SystemDesigner/SystemDiagram">
				<EnvoySuperimpositionContainer Id="3ef9e64774f644eebcc66017e48a9953" xmlns="http://www.ni.com/SystemDesigner/EnvoyManagement">
					<MappingManager Id="e2c493594e634c77ab11a9938a4f77eb" xmlns="http://www.ni.com/SystemDesigner/SystemModelCore">
						<Superimposition Id="df479caae2f24111a03677af1f5f7b1b" Name="Root Superimposition" />
					</MappingManager>
				</EnvoySuperimpositionContainer>
				<SystemDiagramRootDiagram Id="2e5335977053482e88426c43c4a8379c" />
			</SystemDiagram>
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="686ec28c706b4a57b4278e1071f9c4d1" ModelDefinitionType="NullTarget" Name="NullTarget">
			<NullTarget />
		</NameScopingEnvoy>
		<NameScopingEnvoy Id="d97e60887a849da82595650ae900c59" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Id="74a896797b974d5e8b333378e651aaa6" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="NIScopeAcquireWaveform.measui" StoragePath="NIScopeAcquireWaveform.measui" />
			<FileReference Id="bfb2520225ff48beb04021d44755a643" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="NIScopeAcquireWaveform.pinmap" StoragePath="NIScopeAcquireWaveform.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niscope_acquire_waveform/NIScopeAcquireWaveform.measui sha256=97c3bebd633dd68a5c02840a0c29665b0d2e74b17436e8b6fbad04f5363e672d bytes=23605 -->
## FILE: examples/niscope_acquire_waveform/NIScopeAcquireWaveform.measui

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niscope_acquire_waveform/NIScopeAcquireWaveform.measui`
- sha256: `97c3bebd633dd68a5c02840a0c29665b0d2e74b17436e8b6fbad04f5363e672d`
- bytes: 23605

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="B503B23000D9DA04E976078DC317B16AEEA82980AD834E63ABC0EBFCDA800F52B434A05A68229BE420A14B9BD87EA7BD4531F934DCEDB1DFC199AC70AF9B13FB" Timestamp="1DA8F587BADFCE7" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.12.0.49994" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="9.8.1.49152" />
		<ParsableNamespace AssemblyFileVersion="9.12.0.49994" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="24.3.0.49994" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.12.0.49994" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.12.0.49994" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="24.3.0.49994" Name="MeasurementLink UI Editor" Version="24.3.0.49994" />
	</SourceModelFeatureSet>
	<Screen ClientId="{058ec218-444b-4e09-9a76-99dd0791f991}" DisplayName="NI-SCOPE Acquire Waveform (Py)" Id="7ecb9046d80c4b899a7ab0120284de3c" ServiceClass="ni.examples.NIScopeAcquireWaveform_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
		<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]530" Id="34c8bbb4a92c4d419c8d8e74e2c9c68b" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]911" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
			<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BaseName="[string]Canvas" Height="[float]124" Id="4171c457087442159b6fa1e8910b232d" Label="[UIModel]b8e1f4105fb4bc7ad2323fcc369fba8" Left="[float]22" Top="[float]92" Width="[float]244">
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{058ec218-444b-4e09-9a76-99dd0791f991}/Configuration/vertical_range" Enabled="[bool]True" Height="[float]24" Id="8e653d4bdd7e4e209b8963d1055b83b2" IsLabelBoundToChannel="[bool]False" Label="[UIModel]efc7ad770a5e4fdcac0ee77afb60f8b4" Left="[float]12" Top="[float]32" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=2:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
				<Label Height="[float]16" Id="efc7ad770a5e4fdcac0ee77afb60f8b4" LabelOwner="[UIModel]8e653d4bdd7e4e209b8963d1055b83b2" Left="[float]12" Text="[string]Range" Top="[float]12" Width="[float]34" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{058ec218-444b-4e09-9a76-99dd0791f991}/Configuration/input_impedance" Enabled="[bool]True" Height="[float]24" Id="105e5d576e364b75afc531237f08bfd5" IsLabelBoundToChannel="[bool]False" Label="[UIModel]dac01d8c613d4f23b72970902c411893" Left="[float]139" RadixBase="[RadixBase]0" RadixVisibility="[SMVisibility]Collapsed" Top="[float]32" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=SystemInternational:Digits=5:DigitDisplayType=SignificantDigits:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
				<Label Height="[float]16" Id="dac01d8c613d4f23b72970902c411893" LabelOwner="[UIModel]105e5d576e364b75afc531237f08bfd5" Left="[float]139" Text="[string]Input impedance" Top="[float]12" Width="[float]90" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{058ec218-444b-4e09-9a76-99dd0791f991}/Configuration/vertical_coupling" Enabled="[bool]True" Height="[float]24" Id="ff0048bc78af4a04904c32c20947393a" IsLabelBoundToChannel="[bool]False" Label="[UIModel]ffe5c17e25934889a90246dc0a15d5bd" Left="[float]12" Top="[float]87" Value="[int]1" Width="[float]95" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
					<RingSelectorInfo DisplayValue="[string]AC" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]DC" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]GND" IsEnabled="[bool]True" Value="[int]2" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</ChannelEnumSelector>
				<Label Height="[float]16" Id="ffe5c17e25934889a90246dc0a15d5bd" LabelOwner="[UIModel]ff0048bc78af4a04904c32c20947393a" Left="[float]12" Text="[string]Coupling" Top="[float]67" Width="[float]48" xmlns="http://www.ni.com/PanelCommon" />
			</ScreenSurfaceCanvas>
			<Label Height="[float]16" Id="b8e1f4105fb4bc7ad2323fcc369fba8" LabelOwner="[UIModel]4171c457087442159b6fa1e8910b232d" Left="[float]22" Text="[string]Vertical" Top="[float]72" Width="[float]40" xmlns="http://www.ni.com/PanelCommon" />
			<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BaseName="[string]Canvas" Height="[float]75" Id="c1567a3d97c047ee9a243fcd87ed3447" Label="[UIModel]78ddee97e1f14549af1a6b479b853781" Left="[float]22" Top="[float]246" Width="[float]244">
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{058ec218-444b-4e09-9a76-99dd0791f991}/Configuration/min_sample_rate" Enabled="[bool]True" Height="[float]24" Id="a833e04474734b1384cee079d375b6ff" IsLabelBoundToChannel="[bool]False" Label="[UIModel]1b67bc9d4408445b898c7c47872c3c8b" Left="[float]11" RadixBase="[RadixBase]0" RadixVisibility="[SMVisibility]Collapsed" Top="[float]33" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=SystemInternational:Digits=5:DigitDisplayType=SignificantDigits:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
				<Label Height="[float]16" Id="1b67bc9d4408445b898c7c47872c3c8b" LabelOwner="[UIModel]a833e04474734b1384cee079d375b6ff" Left="[float]11" Text="[string]Min sample rate" Top="[float]13" Width="[float]87" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{058ec218-444b-4e09-9a76-99dd0791f991}/Configuration/min_record_length" Enabled="[bool]True" Height="[float]24" Id="f7a551b9a0a34822aac4d56627b48c08" Interval="[int]1" IsLabelBoundToChannel="[bool]False" Label="[UIModel]be4db0801e974e01a6cfd4782de484a5" Left="[float]137" Top="[float]33" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=0:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Int32" Width="[float]70" />
				<Label Height="[float]16" Id="be4db0801e974e01a6cfd4782de484a5" LabelOwner="[UIModel]f7a551b9a0a34822aac4d56627b48c08" Left="[float]137" Text="[string]Min record length" Top="[float]13" Width="[float]96" xmlns="http://www.ni.com/PanelCommon" />
			</ScreenSurfaceCanvas>
			<Label Height="[float]16" Id="78ddee97e1f14549af1a6b479b853781" LabelOwner="[UIModel]c1567a3d97c047ee9a243fcd87ed3447" Left="[float]22" Text="[string]Horizontal" Top="[float]226" Width="[float]56" xmlns="http://www.ni.com/PanelCommon" />
			<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BaseName="[string]Canvas" Height="[float]156" Id="1bbbff8ff8624d6580b40159945404d9" Label="[UIModel]d3204b2cf2ff4d9f804e0d35af7d8247" Left="[float]22" Top="[float]351" Width="[float]244">
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{058ec218-444b-4e09-9a76-99dd0791f991}/Configuration/trigger_level" Enabled="[bool]True" Height="[float]24" Id="dff278311b148e5a9dd8a2055c4340f" IsLabelBoundToChannel="[bool]False" Label="[UIModel]35032d9a46a548a58a8c894a084da3e2" Left="[float]12" Top="[float]86" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=2:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
				<Label Height="[float]16" Id="35032d9a46a548a58a8c894a084da3e2" LabelOwner="[UIModel]dff278311b148e5a9dd8a2055c4340f" Left="[float]12" Text="[string]Level" Top="[float]66" Width="[float]28" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelCheckBox BaseName="[string]Checkbox" Channel="[string]{058ec218-444b-4e09-9a76-99dd0791f991}/Configuration/auto_trigger" Content="[string]Auto trigger" Enabled="[bool]True" Height="[float]16" Id="2fbc891cc72242fbb131d9666757a75b" IsLabelBoundToChannel="[bool]False" Label="[UIModel]b675e3e875884df1a7b766c6b1f99264" Left="[float]12" MinHeight="[float]16" MinWidth="[float]16" Top="[float]129" Width="[float]87" />
				<Label Height="[float]0" Id="b675e3e875884df1a7b766c6b1f99264" LabelOwner="[UIModel]2fbc891cc72242fbb131d9666757a75b" Left="[float]12" Text="[string]Auto trigger" Top="[float]109" Visible="[bool]False" Width="[float]0" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{058ec218-444b-4e09-9a76-99dd0791f991}/Configuration/trigger_pin" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="80ba77279b36457d9ac495179c38a309" IsLabelBoundToChannel="[bool]False" Label="[UIModel]9d8dba7edc23437eab89be566857fb49" Left="[float]12" Top="[float]33" Width="[float]100" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
				<Label Height="[float]16" Id="9d8dba7edc23437eab89be566857fb49" LabelOwner="[UIModel]80ba77279b36457d9ac495179c38a309" Left="[float]12" Text="[string]Pin" Top="[float]13" Width="[float]17" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{058ec218-444b-4e09-9a76-99dd0791f991}/Configuration/trigger_coupling" Enabled="[bool]True" Height="[float]24" Id="328b6436ae73457fb0015f52672504a2" IsLabelBoundToChannel="[bool]False" Label="[UIModel]f904e0131e4438bad19f5c2b821b525" Left="[float]124" Top="[float]86" Value="[int]1" Width="[float]108" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
					<RingSelectorInfo DisplayValue="[string]AC" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]DC" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]HF_REJECT" IsEnabled="[bool]True" Value="[int]3" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]LF_REJECT" IsEnabled="[bool]True" Value="[int]4" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]AC_PLUS_HF_REJECT" IsEnabled="[bool]True" Value="[int]1001" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</ChannelEnumSelector>
				<Label Height="[float]16" Id="f904e0131e4438bad19f5c2b821b525" LabelOwner="[UIModel]328b6436ae73457fb0015f52672504a2" Left="[float]124" Text="[string]Coupling" Top="[float]66" Width="[float]48" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{058ec218-444b-4e09-9a76-99dd0791f991}/Configuration/trigger_slope" Enabled="[bool]True" Height="[float]24" Id="8eb0ddfc14db436fa3eb90a769c2401a" IsLabelBoundToChannel="[bool]False" Label="[UIModel]1ae642b50fb9418a8dff7164991cd197" Left="[float]125" Top="[float]33" Value="[int]1" Width="[float]107" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
					<RingSelectorInfo DisplayValue="[string]NEGATIVE" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]POSITIVE" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]SLOPE_EITHER" IsEnabled="[bool]True" Value="[int]3" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</ChannelEnumSelector>
				<Label Height="[float]16" Id="1ae642b50fb9418a8dff7164991cd197" LabelOwner="[UIModel]8eb0ddfc14db436fa3eb90a769c2401a" Left="[float]125" Text="[string]Slope" Top="[float]13" Width="[float]31" xmlns="http://www.ni.com/PanelCommon" />
			</ScreenSurfaceCanvas>
			<Label Height="[float]16" Id="d3204b2cf2ff4d9f804e0d35af7d8247" LabelOwner="[UIModel]1bbbff8ff8624d6580b40159945404d9" Left="[float]22" Text="[string]Trigger" Top="[float]331" Width="[float]37" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{058ec218-444b-4e09-9a76-99dd0791f991}/Configuration/timeout" Enabled="[bool]True" Height="[float]24" Id="e7b1f32ae0314730aa611edc3386bb7d" IsLabelBoundToChannel="[bool]False" Label="[UIModel]1e346b6974e9451aa4ee0c455e72832e" Left="[float]288" Top="[float]371" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]70" />
			<Label Height="[float]16" Id="1e346b6974e9451aa4ee0c455e72832e" LabelOwner="[UIModel]e7b1f32ae0314730aa611edc3386bb7d" Left="[float]288" Text="[string]Timeout (s)" Top="[float]351" Width="[float]60" xmlns="http://www.ni.com/PanelCommon" />
			<ArrayGraph Background="[SMSolidColorBrush]#00000000" BaseName="[string]Array Graph" Height="[float]300" Id="9aaf1f2747e7459193238f220d4b8b33" Label="[UIModel]70c9d2a112534b1ab3299bade5d80dbd" Left="[float]288" MinWidth="[float]230" PlotAreaMargin="[SMThickness]68,26,16,27" PreferIndexData="[bool]False" RenderMode="[RenderMode]Hardware" SuppressScaleLayout="[bool]False" Top="[float]41" Width="[float]500">
				<ArrayGraphAxis Adjuster="[RangeAdjuster]FitExactly" Id="51b1732c824c42188be93ab98faf6d9e" Label="[string]Index" LabelVisibility="[SMVisibility]Collapsed" MajorDivisions="[UIModel]159ff18bf3f74568a4e9ef8b74713417" MinorTickVisibility="[SMVisibility]Collapsed" Orientation="[SMOrientation]Horizontal" Range="[IRange]0, 39999, System.Double" ValueType="[Type]Double">
					<RangeLabeledDivisions Id="159ff18bf3f74568a4e9ef8b74713417" xmlns="http://www.ni.com/Controls.LabVIEW.Design">
						<p.LabelPresenter Format="G6" />
					</RangeLabeledDivisions>
				</ArrayGraphAxis>
				<ArrayGraphAxis Adjuster="[RangeAdjuster]FitExactly" Id="716e12d812d543b8b13d8551284d5834" Label="[string]Value" LabelVisibility="[SMVisibility]Collapsed" MajorDivisions="[UIModel]46cf2fb19f7e4ad9bf8e247664879281" Orientation="[SMOrientation]Vertical" Range="[IRange]-2.1225738525390625, 2.2920989990234375, System.Double" ValueType="[Type]Double">
					<RangeLabeledDivisions Id="46cf2fb19f7e4ad9bf8e247664879281" xmlns="http://www.ni.com/Controls.LabVIEW.Design">
						<p.LabelPresenter Format="G6" />
					</RangeLabeledDivisions>
				</ArrayGraphAxis>
				<HmiGraphPlot Channel="[string]{058ec218-444b-4e09-9a76-99dd0791f991}/Output/waveform0" HorizontalScale="[UIModel]51b1732c824c42188be93ab98faf6d9e" Id="aea74322760b467486e3b1773af89924" IsDefaultPlot="[bool]False" Label="[string]waveform0" VerticalScale="[UIModel]716e12d812d543b8b13d8551284d5834">
					<PlotRenderer Id="e1fa5b7d032647d6be20ace1b06fbf14" LineStroke="[SMSolidColorBrush]#ffea4225" LineThickness="[double]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</HmiGraphPlot>
				<HmiGraphPlot Channel="[string]{058ec218-444b-4e09-9a76-99dd0791f991}/Output/waveform1" HorizontalScale="[UIModel]51b1732c824c42188be93ab98faf6d9e" Id="aa0f6f1f29cd4fedbbd0b3dce05e4b3a" IsDefaultPlot="[bool]False" Label="[string]waveform1" VerticalScale="[UIModel]716e12d812d543b8b13d8551284d5834">
					<PlotRenderer Id="2463f83f2ef6479e944ac6e3e8262462" LineStroke="[SMSolidColorBrush]#ffe6cd00" LineThickness="[double]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</HmiGraphPlot>
				<HmiGraphPlot Channel="[string]{058ec218-444b-4e09-9a76-99dd0791f991}/Output/waveform2" HorizontalScale="[UIModel]51b1732c824c42188be93ab98faf6d9e" Id="5e9e8e86ddf54052a18f40aa0944303c" IsDefaultPlot="[bool]False" Label="[string]waveform2" VerticalScale="[UIModel]716e12d812d543b8b13d8551284d5834">
					<PlotRenderer Id="4f2a4c4822b64aea846af8a7e3343cae" LineStroke="[SMSolidColorBrush]#ff5ac59d" LineThickness="[double]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</HmiGraphPlot>
				<HmiGraphPlot Channel="[string]{058ec218-444b-4e09-9a76-99dd0791f991}/Output/waveform3" HorizontalScale="[UIModel]51b1732c824c42188be93ab98faf6d9e" Id="451a077c679848a7b21202de7645138a" IsDefaultPlot="[bool]False" Label="[string]waveform3" VerticalScale="[UIModel]716e12d812d543b8b13d8551284d5834">
					<PlotRenderer Id="d6211a3c13e946158e0f68b57b3f469f" LineStroke="[SMSolidColorBrush]#ff1f3145" LineThickness="[double]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</HmiGraphPlot>
			</ArrayGraph>
			<HmiChartPlotLegend Graph="[UIModel]9aaf1f2747e7459193238f220d4b8b33" Height="[float]106" Id="ddffa0d196ed49428b5cc6b232ae05bb" Left="[float]795" Top="[float]41" />
			<HmiChartCursorLegend Graph="[UIModel]9aaf1f2747e7459193238f220d4b8b33" Height="[float]80" Id="99dc94983a34492da8f1732a6d989688" Left="[float]293" MinHeight="[float]80" Top="[float]370" Visible="[bool]False" Width="[float]316" />
			<HmiChartScaleLegend Graph="[UIModel]9aaf1f2747e7459193238f220d4b8b33" Height="[float]52" Id="604a7607f19a4544bd5e1b5d0b86e7a6" Left="[float]713" Top="[float]348" Visible="[bool]False" />
			<ArrayGraphTools BackgroundColor="[SMSolidColorBrush]#fff7f7f7" Graph="[UIModel]9aaf1f2747e7459193238f220d4b8b33" Height="[float]26" Id="26988604ca374c60bf7b87a96d4a3b0e" Left="[float]634" OffsetX="[float]346" OffsetY="[float]0" Top="[float]41" Width="[float]122">
				<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Horizontal Zoom" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]3df3c5c80a5947f599c2c8946a28ca64" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="e848625f74dd4aef84ee100cb0970e4c" IsMomentary="[bool]False" Label="[UIModel]3c642261aa154be89d390a56337581e1" Left="[float]2" PartName="[string]PART_ZoomHorizontalButton" Top="[float]2" Value="[bool]False" Width="[float]28">
					<Image BaseName="[string]Image" Id="3df3c5c80a5947f599c2c8946a28ca64" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomHorizontal.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
				</ComposableButton>
				<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Vertical Zoom" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]8f9ad77fb22c447883a470b7cdb3df71" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="f23b486d6be14cb4b024425f441121e2" IsMomentary="[bool]False" Label="[UIModel]e18af3a368e34977b0ff79be6cf0945c" Left="[float]32" PartName="[string]PART_ZoomVerticalButton" Top="[float]2" Value="[bool]False" Width="[float]28">
					<Image BaseName="[string]Image" Id="8f9ad77fb22c447883a470b7cdb3df71" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomVertical.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
				</ComposableButton>
				<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Pan" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]147cd568c034420da5d2ab6ee71a159d" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="c8583558c3234688991a298d7b8d4179" IsMomentary="[bool]False" Label="[UIModel]b08e55d26dd54e0e83be785cba19f679" Left="[float]62" PartName="[string]PART_PanButton" Top="[float]2" Value="[bool]False" Width="[float]28">
					<Image BaseName="[string]Image" Id="147cd568c034420da5d2ab6ee71a159d" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomPan.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
				</ComposableButton>
				<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Reset" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]73f12cae7c4b43908331eb45aa32fc28" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="443c58d8141f4c6cb68b25bb76a3ba44" IsMomentary="[bool]True" Label="[UIModel]d683772801d645d89cfcf59059e392f2" Left="[float]92" PartName="[string]PART_ResetButton" Top="[float]2" Value="[bool]False" Width="[float]28">
					<Image BaseName="[string]Image" Id="73f12cae7c4b43908331eb45aa32fc28" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomExtents.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
				</ComposableButton>
				<Label Id="3c642261aa154be89d390a56337581e1" LabelOwner="[UIModel]e848625f74dd4aef84ee100cb0970e4c" Left="[float]2" Text="[string]Horizontal Zoom" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
				<Label Id="e18af3a368e34977b0ff79be6cf0945c" LabelOwner="[UIModel]f23b486d6be14cb4b024425f441121e2" Left="[float]32" Text="[string]Vertical Zoom" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
				<Label Id="b08e55d26dd54e0e83be785cba19f679" LabelOwner="[UIModel]c8583558c3234688991a298d7b8d4179" Left="[float]62" Text="[string]Pan" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
				<Label Id="d683772801d645d89cfcf59059e392f2" LabelOwner="[UIModel]443c58d8141f4c6cb68b25bb76a3ba44" Left="[float]92" Text="[string]Reset" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
			</ArrayGraphTools>
			<Label Height="[float]16" Id="70c9d2a112534b1ab3299bade5d80dbd" LabelOwner="[UIModel]9aaf1f2747e7459193238f220d4b8b33" Left="[float]288" Text="[string]Waveforms" Top="[float]21" Width="[float]60" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{058ec218-444b-4e09-9a76-99dd0791f991}/Configuration/measurement_pins" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="121806bc7ce94bf2810e969e17827ac1" IsLabelBoundToChannel="[bool]False" Label="[UIModel]bb9069c6a58347209a1111168c6be0c7" Left="[float]22" MultipleSelectionMode="[MultipleSelectionModes]List" SelectedResource="[NI_Core_DataValues_TagRefnum]PinGroup1" Top="[float]33" Width="[float]244" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
			<Label Height="[float]16" Id="bb9069c6a58347209a1111168c6be0c7" LabelOwner="[UIModel]121806bc7ce94bf2810e969e17827ac1" Left="[float]22" Text="[string]Measurement pins" Top="[float]13" Width="[float]100" xmlns="http://www.ni.com/PanelCommon" />
		</ScreenSurface>
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niscope_acquire_waveform/NIScopeAcquireWaveform.pinmap sha256=79e3d0e87b3419f6140144c8541542928167791807ade642b5b3160d4cc749f2 bytes=1021 -->
## FILE: examples/niscope_acquire_waveform/NIScopeAcquireWaveform.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niscope_acquire_waveform/NIScopeAcquireWaveform.pinmap`
- sha256: `79e3d0e87b3419f6140144c8541542928167791807ade642b5b3160d4cc749f2`
- bytes: 1021

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.5">
	<Instruments>
		<NIScopeInstrument name="SCOPE1" numberOfChannels="4" group="Scope" />
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
		<DUTPin name="Pin2" />
		<DUTPin name="Pin3" />
		<DUTPin name="Pin4" />
	</Pins>
	<PinGroups>
		<PinGroup name="PinGroup1">
			<PinReference pin="Pin1" />
			<PinReference pin="Pin2" />
			<PinReference pin="Pin3" />
			<PinReference pin="Pin4" />
		</PinGroup>
	</PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="SCOPE1" channel="0" />
		<Connection pin="Pin2" siteNumber="0" instrument="SCOPE1" channel="1" />
		<Connection pin="Pin3" siteNumber="0" instrument="SCOPE1" channel="2" />
		<Connection pin="Pin4" siteNumber="0" instrument="SCOPE1" channel="3" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niscope_acquire_waveform/NIScopeAcquireWaveform.serviceconfig sha256=b53893a1536f1df43baf5260e7435c79b4ca90e60a39b88d2e31cc7ca5d77a0b bytes=687 -->
## FILE: examples/niscope_acquire_waveform/NIScopeAcquireWaveform.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niscope_acquire_waveform/NIScopeAcquireWaveform.serviceconfig`
- sha256: `b53893a1536f1df43baf5260e7435c79b4ca90e60a39b88d2e31cc7ca5d77a0b`
- bytes: 687

````json
{
  "services": [
    {
      "displayName": "NI-SCOPE Acquire Waveform (Py)",
      "version": "1.0.0",
      "serviceClass": "ni.examples.NIScopeAcquireWaveform_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "installPath": "install.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in example that acquires a waveform using an NI oscilloscope.",
        "ni/service.collection": "NI.Examples",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niscope_acquire_waveform/NIScopeAcquireWaveform.sfp sha256=7dd976d7672024dd9f27cdc7f688417940fd8e74876f3a49b915c5597b80800d bytes=27118 -->
## FILE: examples/niscope_acquire_waveform/NIScopeAcquireWaveform.sfp

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niscope_acquire_waveform/NIScopeAcquireWaveform.sfp`
- sha256: `7dd976d7672024dd9f27cdc7f688417940fd8e74876f3a49b915c5597b80800d`
- bytes: 27118

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="FC1E23068ECC9920B3BB0175322BDCB1B84A36E368DED3B6FD9D23E837CB72EBD1F2BF1ACEEAB6CECFEA17B4B7929E70D45C2D3FAC77FECE77210F8E1FE0AE40" Timestamp="1DA8F5898DB5964" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.12.0.49994" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="9.8.1.49152" />
		<ParsableNamespace AssemblyFileVersion="9.12.0.49979" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="24.3.0.49979" FeatureSetName="UnifiedTask" Name="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" Version="1.0.0.0" />
		<ParsableNamespace AssemblyFileVersion="24.3.0.49994" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.12.0.49979" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.12.0.49979" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="24.3.0.49979" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="24.3.0.49979" />
	</SourceModelFeatureSet>
	<UnifiedTask Id="42146b75308d4e8ea4374cfa7b56f737" LayoutInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Layout Information&quot;:{&quot;Sections&quot;:[{&quot;Columns Progressive Count&quot;:1,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Columns&quot;:[{&quot;Containers Progressive Count&quot;:1,&quot;Layout Information Index&quot;:0,&quot;Containers&quot;:[{&quot;Container Model Defition&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Container Assignment State&quot;:&quot;Available&quot;,&quot;Container Identifier&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen.task&quot;,&quot;Container Instrument Name&quot;:&quot;NI-SCOPE Acquire Waveform (Py)&quot;,&quot;Layout Information Name&quot;:&quot;NI-SCOPE Acquire Waveform (Py) 1&quot;,&quot;Layout Information Index&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Items&quot;:[{&quot;Identification Number&quot;:4294963201,&quot;Model Definition Type&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Parent Or Group Name&quot;:&quot;Measurements&quot;,&quot;Panel Type&quot;:&quot;NI-SCOPE Acquire Waveform (Py)&quot;,&quot;Layout Information Name&quot;:&quot;ni.examples.NIScopeAcquireWaveform_Python&quot;,&quot;Layout Information Index&quot;:0}]}]}]},{&quot;Columns Progressive Count&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationOnly&quot;}]}}" PinAwareInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Selected Sites&quot;:[{&quot;Site Number&quot;:0}]}" xmlns="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" />
	<EnvoyManagerFile Id="41ea59644ccc4f46b80a73252fd49185" xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="c6ee4fe8daa44b9ba7b1f08730c4f1e2" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<NameScopingEnvoy AutomaticallyResolveUp="True" Id="a06acae2658a414da3800efef4323c54" Name="NIScopeAcquireWaveform.sfp" NameTracksFileName="True" />
		<EmbeddedDefinitionReference Id="7b2e43f384b9410f9f6bc0daf8316f77" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="{http\://www.ni.com/InstrumentFramework/ScreenDocument}Screen.task">
			<Screen ClientId="{bd779b16-f709-4027-9f10-768896a2a6a3}" ConfigurationParameters="{&quot;@type&quot;:&quot;type.googleapis.com/ni.measurementlink.measurement.v2.MeasurementConfigurations&quot;,&quot;measurementPins&quot;:[&quot;PinGroup1&quot;],&quot;verticalRange&quot;:5.0,&quot;verticalCoupling&quot;:1,&quot;inputImpedance&quot;:1000000.0,&quot;minSampleRate&quot;:10000000.0,&quot;minRecordLength&quot;:40000,&quot;triggerPin&quot;:&quot;Pin1&quot;,&quot;triggerLevel&quot;:0.5,&quot;triggerSlope&quot;:1,&quot;autoTrigger&quot;:false,&quot;triggerCoupling&quot;:1,&quot;timeout&quot;:5.0}" DisplayName="NI-SCOPE Acquire Waveform (Py)" Id="8720edfce9f24045b0c22e7870fbdb1a" PanelPresentation="ConfigurationWithVisualization" ServiceClass="ni.examples.NIScopeAcquireWaveform_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
				<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]530" Id="aeb74c1693c2445496fff3ca5b6a1c1e" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]911" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
					<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BaseName="[string]Canvas" Height="[float]124" Id="8364ffabce17436db8a55dc3e5dd4279" Label="[UIModel]cbf82593070b44b797b15d3d4619c471" Left="[float]22" Top="[float]92" Width="[float]244">
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{bd779b16-f709-4027-9f10-768896a2a6a3}/Configuration/vertical_range" Enabled="[bool]True" Height="[float]24" Id="11a319a55b764b26b6c9b4459e0df139" IsLabelBoundToChannel="[bool]False" Label="[UIModel]4af539d1666f4d4393bc2e8039721e63" Left="[float]12" Top="[float]32" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=2:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
						<Label Height="[float]16" Id="4af539d1666f4d4393bc2e8039721e63" LabelOwner="[UIModel]11a319a55b764b26b6c9b4459e0df139" Left="[float]12" Text="[string]Range" Top="[float]12" Width="[float]34" xmlns="http://www.ni.com/PanelCommon" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{bd779b16-f709-4027-9f10-768896a2a6a3}/Configuration/input_impedance" Enabled="[bool]True" Height="[float]24" Id="b43a1d564d6d41ed841d37bca1db3294" IsLabelBoundToChannel="[bool]False" Label="[UIModel]569e6796a5b24f999a17119ef32a90f1" Left="[float]139" RadixBase="[RadixBase]0" RadixVisibility="[SMVisibility]Collapsed" Top="[float]32" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=SystemInternational:Digits=5:DigitDisplayType=SignificantDigits:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
						<Label Height="[float]16" Id="569e6796a5b24f999a17119ef32a90f1" LabelOwner="[UIModel]b43a1d564d6d41ed841d37bca1db3294" Left="[float]139" Text="[string]Input impedance" Top="[float]12" Width="[float]90" xmlns="http://www.ni.com/PanelCommon" />
						<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{bd779b16-f709-4027-9f10-768896a2a6a3}/Configuration/vertical_coupling" Enabled="[bool]True" Height="[float]24" Id="b20d98bd292d44e48bd7ebfa83fa2541" IsLabelBoundToChannel="[bool]False" Label="[UIModel]e30c99b58a574b54bf53e124e39ebffb" Left="[float]12" Top="[float]87" Value="[int]1" Width="[float]95" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
							<RingSelectorInfo DisplayValue="[string]AC" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
							<RingSelectorInfo DisplayValue="[string]DC" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
							<RingSelectorInfo DisplayValue="[string]GND" IsEnabled="[bool]True" Value="[int]2" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						</ChannelEnumSelector>
						<Label Height="[float]16" Id="e30c99b58a574b54bf53e124e39ebffb" LabelOwner="[UIModel]b20d98bd292d44e48bd7ebfa83fa2541" Left="[float]12" Text="[string]Coupling_2" Top="[float]67" Width="[float]60" xmlns="http://www.ni.com/PanelCommon" />
					</ScreenSurfaceCanvas>
					<Label Height="[float]16" Id="cbf82593070b44b797b15d3d4619c471" LabelOwner="[UIModel]8364ffabce17436db8a55dc3e5dd4279" Left="[float]22" Text="[string]Vertical" Top="[float]72" Width="[float]40" xmlns="http://www.ni.com/PanelCommon" />
					<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BaseName="[string]Canvas" Height="[float]75" Id="85cdd817e854dbebce0e0f803d3a6cf" Label="[UIModel]f327d78a5beb41658bd0d62525005adb" Left="[float]22" Top="[float]246" Width="[float]244">
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{bd779b16-f709-4027-9f10-768896a2a6a3}/Configuration/min_sample_rate" Enabled="[bool]True" Height="[float]24" Id="b12427f2893c4b1ab27bbe14fff4a1fc" IsLabelBoundToChannel="[bool]False" Label="[UIModel]6989be4e554a4f57bb8521fb6ad745c7" Left="[float]11" RadixBase="[RadixBase]0" RadixVisibility="[SMVisibility]Collapsed" Top="[float]33" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=SystemInternational:Digits=5:DigitDisplayType=SignificantDigits:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
						<Label Height="[float]16" Id="6989be4e554a4f57bb8521fb6ad745c7" LabelOwner="[UIModel]b12427f2893c4b1ab27bbe14fff4a1fc" Left="[float]11" Text="[string]Min sample rate" Top="[float]13" Width="[float]87" xmlns="http://www.ni.com/PanelCommon" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{bd779b16-f709-4027-9f10-768896a2a6a3}/Configuration/min_record_length" Enabled="[bool]True" Height="[float]24" Id="e4feae8a51874864a85fbb7966c4fbaf" Interval="[int]1" IsLabelBoundToChannel="[bool]False" Label="[UIModel]ca08e4eaa6d342cfa0d5a7f99c6ab07a" Left="[float]137" Top="[float]33" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=0:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Int32" Width="[float]70" />
						<Label Height="[float]16" Id="ca08e4eaa6d342cfa0d5a7f99c6ab07a" LabelOwner="[UIModel]e4feae8a51874864a85fbb7966c4fbaf" Left="[float]137" Text="[string]Min record length" Top="[float]13" Width="[float]96" xmlns="http://www.ni.com/PanelCommon" />
					</ScreenSurfaceCanvas>
					<Label Height="[float]16" Id="f327d78a5beb41658bd0d62525005adb" LabelOwner="[UIModel]85cdd817e854dbebce0e0f803d3a6cf" Left="[float]22" Text="[string]Horizontal" Top="[float]226" Width="[float]56" xmlns="http://www.ni.com/PanelCommon" />
					<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BaseName="[string]Canvas" Height="[float]156" Id="bea0566bceb4be5bcca6f4a95d548df" Label="[UIModel]bb114527abaa4eba91af98c95f2fe059" Left="[float]22" Top="[float]351" Width="[float]244">
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{bd779b16-f709-4027-9f10-768896a2a6a3}/Configuration/trigger_level" Enabled="[bool]True" Height="[float]24" Id="8d48695f93ad4988b460a869b2d5784c" IsLabelBoundToChannel="[bool]False" Label="[UIModel]fd308f5f83aa4c91831239bf31f8dc2b" Left="[float]12" Top="[float]86" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=2:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
						<Label Height="[float]16" Id="fd308f5f83aa4c91831239bf31f8dc2b" LabelOwner="[UIModel]8d48695f93ad4988b460a869b2d5784c" Left="[float]12" Text="[string]Level" Top="[float]66" Width="[float]28" xmlns="http://www.ni.com/PanelCommon" />
						<ChannelCheckBox BaseName="[string]Checkbox" Channel="[string]{bd779b16-f709-4027-9f10-768896a2a6a3}/Configuration/auto_trigger" Content="[string]Auto trigger" Enabled="[bool]True" Height="[float]16" Id="f55d3d440237488187618dd49744fa96" IsLabelBoundToChannel="[bool]False" Label="[UIModel]e051bef190984ab487d0886792720441" Left="[float]12" MinHeight="[float]16" MinWidth="[float]16" Top="[float]129" Width="[float]87" />
						<Label Height="[float]0" Id="e051bef190984ab487d0886792720441" LabelOwner="[UIModel]f55d3d440237488187618dd49744fa96" Left="[float]12" Text="[string]Auto trigger" Top="[float]109" Visible="[bool]False" Width="[float]0" xmlns="http://www.ni.com/PanelCommon" />
						<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{bd779b16-f709-4027-9f10-768896a2a6a3}/Configuration/trigger_pin" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="92d23f1787bb467b9b736d11888f6a5c" IsLabelBoundToChannel="[bool]False" Label="[UIModel]44592972b3a64d2f8bdf0ba83d745efe" Left="[float]12" Top="[float]33" Width="[float]100" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
						<Label Height="[float]16" Id="44592972b3a64d2f8bdf0ba83d745efe" LabelOwner="[UIModel]92d23f1787bb467b9b736d11888f6a5c" Left="[float]12" Text="[string]Pin" Top="[float]13" Width="[float]17" xmlns="http://www.ni.com/PanelCommon" />
						<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{bd779b16-f709-4027-9f10-768896a2a6a3}/Configuration/trigger_coupling" Enabled="[bool]True" Height="[float]24" Id="8bcfb6c4bf824cba8edea269172ca701" IsLabelBoundToChannel="[bool]False" Label="[UIModel]3fd1c79f04a84e838369e4a7298e69f3" Left="[float]124" Top="[float]86" Value="[int]1" Width="[float]108" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
							<RingSelectorInfo DisplayValue="[string]AC" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
							<RingSelectorInfo DisplayValue="[string]DC" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
							<RingSelectorInfo DisplayValue="[string]HF_REJECT" IsEnabled="[bool]True" Value="[int]3" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
							<RingSelectorInfo DisplayValue="[string]LF_REJECT" IsEnabled="[bool]True" Value="[int]4" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
							<RingSelectorInfo DisplayValue="[string]AC_PLUS_HF_REJECT" IsEnabled="[bool]True" Value="[int]1001" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						</ChannelEnumSelector>
						<Label Height="[float]16" Id="3fd1c79f04a84e838369e4a7298e69f3" LabelOwner="[UIModel]8bcfb6c4bf824cba8edea269172ca701" Left="[float]124" Text="[string]Coupling" Top="[float]66" Width="[float]48" xmlns="http://www.ni.com/PanelCommon" />
						<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{bd779b16-f709-4027-9f10-768896a2a6a3}/Configuration/trigger_slope" Enabled="[bool]True" Height="[float]24" Id="9bd76a0c30c1428ba515dab27f1fb5f7" IsLabelBoundToChannel="[bool]False" Label="[UIModel]84c14e5a73b943019c02208f32399fa2" Left="[float]125" Top="[float]33" Value="[int]1" Width="[float]107" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
							<RingSelectorInfo DisplayValue="[string]NEGATIVE" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
							<RingSelectorInfo DisplayValue="[string]POSITIVE" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
							<RingSelectorInfo DisplayValue="[string]SLOPE_EITHER" IsEnabled="[bool]True" Value="[int]3" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						</ChannelEnumSelector>
						<Label Height="[float]16" Id="84c14e5a73b943019c02208f32399fa2" LabelOwner="[UIModel]9bd76a0c30c1428ba515dab27f1fb5f7" Left="[float]125" Text="[string]Slope" Top="[float]13" Width="[float]31" xmlns="http://www.ni.com/PanelCommon" />
					</ScreenSurfaceCanvas>
					<Label Height="[float]16" Id="bb114527abaa4eba91af98c95f2fe059" LabelOwner="[UIModel]bea0566bceb4be5bcca6f4a95d548df" Left="[float]22" Text="[string]Trigger" Top="[float]331" Width="[float]37" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{bd779b16-f709-4027-9f10-768896a2a6a3}/Configuration/timeout" Enabled="[bool]True" Height="[float]24" Id="e456ffea4206442db11cd35e067d7c3e" IsLabelBoundToChannel="[bool]False" Label="[UIModel]d5843582633e4cad97317c6981b8e30f" Left="[float]288" TabIndex="[int]0" Top="[float]371" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]70" />
					<Label Height="[float]16" Id="d5843582633e4cad97317c6981b8e30f" LabelOwner="[UIModel]e456ffea4206442db11cd35e067d7c3e" Left="[float]288" Text="[string]Timeout (s)" Top="[float]351" Width="[float]60" xmlns="http://www.ni.com/PanelCommon" />
					<ArrayGraph Background="[SMSolidColorBrush]#00000000" BaseName="[string]Array Graph" Height="[float]300" Id="2d5c61cd3e1b4424b3ffb9838895186f" Label="[UIModel]be4cc3bef0f5419ea42cd58f151b546c" Left="[float]288" MinWidth="[float]230" PlotAreaMargin="[SMThickness]68,26,16,27" PreferIndexData="[bool]False" RenderMode="[RenderMode]Hardware" SuppressScaleLayout="[bool]False" Top="[float]41" Width="[float]500">
						<ArrayGraphAxis Adjuster="[RangeAdjuster]FitExactly" Id="8a2bc2e7b4544dcc91e4bd9e61008665" Label="[string]Index" LabelVisibility="[SMVisibility]Collapsed" MajorDivisions="[UIModel]85878439256d48aaa160172ed8d6f333" MinorTickVisibility="[SMVisibility]Collapsed" Orientation="[SMOrientation]Horizontal" Range="[IRange]0, 39999, System.Double" ValueType="[Type]Double">
							<RangeLabeledDivisions Id="85878439256d48aaa160172ed8d6f333" xmlns="http://www.ni.com/Controls.LabVIEW.Design">
								<p.LabelPresenter Format="G6" />
							</RangeLabeledDivisions>
						</ArrayGraphAxis>
						<ArrayGraphAxis Adjuster="[RangeAdjuster]FitExactly" Id="260621ccad684426b4bfd304f7b9b28b" Label="[string]Value" LabelVisibility="[SMVisibility]Collapsed" MajorDivisions="[UIModel]8b465c3ef7bc4287ba13cf7f227f172d" Orientation="[SMOrientation]Vertical" Range="[IRange]-2.1225738525390625, 2.292327880859375, System.Double" ValueType="[Type]Double">
							<RangeLabeledDivisions Id="8b465c3ef7bc4287ba13cf7f227f172d" xmlns="http://www.ni.com/Controls.LabVIEW.Design">
								<p.LabelPresenter Format="G6" />
							</RangeLabeledDivisions>
						</ArrayGraphAxis>
						<HmiGraphPlot Channel="[string]{bd779b16-f709-4027-9f10-768896a2a6a3}/Output/waveform0" HorizontalScale="[UIModel]8a2bc2e7b4544dcc91e4bd9e61008665" Id="1c8bf34dd76b49918771686880392b79" IsDefaultPlot="[bool]False" Label="[string]waveform0" VerticalScale="[UIModel]260621ccad684426b4bfd304f7b9b28b">
							<PlotRenderer Id="98fb34685ae6400f9587afe149a50f97" LineStroke="[SMSolidColorBrush]#ffea4225" LineThickness="[double]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						</HmiGraphPlot>
						<HmiGraphPlot Channel="[string]{bd779b16-f709-4027-9f10-768896a2a6a3}/Output/waveform1" HorizontalScale="[UIModel]8a2bc2e7b4544dcc91e4bd9e61008665" Id="da7d044b6e9847729b99f57254bdc5e7" IsDefaultPlot="[bool]False" Label="[string]waveform1" VerticalScale="[UIModel]260621ccad684426b4bfd304f7b9b28b">
							<PlotRenderer Id="49f5bb2dafea48b1a0b0f2f51c70595a" LineStroke="[SMSolidColorBrush]#ffe6cd00" LineThickness="[double]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						</HmiGraphPlot>
						<HmiGraphPlot Channel="[string]{bd779b16-f709-4027-9f10-768896a2a6a3}/Output/waveform2" HorizontalScale="[UIModel]8a2bc2e7b4544dcc91e4bd9e61008665" Id="f716809638a04682ab86f637cb5d82c2" IsDefaultPlot="[bool]False" Label="[string]waveform2" VerticalScale="[UIModel]260621ccad684426b4bfd304f7b9b28b">
							<PlotRenderer Id="e3c6d4f2b1c4461cb1c11668abfa60db" LineStroke="[SMSolidColorBrush]#ff5ac59d" LineThickness="[double]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						</HmiGraphPlot>
						<HmiGraphPlot Channel="[string]{bd779b16-f709-4027-9f10-768896a2a6a3}/Output/waveform3" HorizontalScale="[UIModel]8a2bc2e7b4544dcc91e4bd9e61008665" Id="e8d0d307a5e9431b89c3b851c4f1d594" IsDefaultPlot="[bool]False" Label="[string]waveform3" VerticalScale="[UIModel]260621ccad684426b4bfd304f7b9b28b">
							<PlotRenderer Id="e40d17791de84aa18f80dcc3754713d9" LineStroke="[SMSolidColorBrush]#ff1f3145" LineThickness="[double]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						</HmiGraphPlot>
					</ArrayGraph>
					<HmiChartPlotLegend Graph="[UIModel]2d5c61cd3e1b4424b3ffb9838895186f" Height="[float]106" Id="4d814acf168a419da940000f06431d80" Left="[float]795" Top="[float]41" />
					<HmiChartCursorLegend Graph="[UIModel]2d5c61cd3e1b4424b3ffb9838895186f" Height="[float]80" Id="ee82a37f2c324894b6f1831ac12eee6c" Left="[float]293" MinHeight="[float]80" Top="[float]370" Visible="[bool]False" Width="[float]316" />
					<HmiChartScaleLegend Graph="[UIModel]2d5c61cd3e1b4424b3ffb9838895186f" Height="[float]52" Id="767de8e8da9042049b8cc3627ae5f742" Left="[float]713" Top="[float]348" Visible="[bool]False" />
					<ArrayGraphTools BackgroundColor="[SMSolidColorBrush]#fff7f7f7" Graph="[UIModel]2d5c61cd3e1b4424b3ffb9838895186f" Height="[float]26" Id="af9e2c774571488099f4c5622eab2415" Left="[float]634" OffsetX="[float]346" OffsetY="[float]0" Top="[float]41" Width="[float]122">
						<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Horizontal Zoom" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]477b01fe1fa1465f9aea3cda4ebe53c1" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="c5bab5e374244f74af63ccfa5da5a447" IsMomentary="[bool]False" Label="[UIModel]e70bef5b5e2c40fcb19b5426bcaa9622" Left="[float]2" PartName="[string]PART_ZoomHorizontalButton" Top="[float]2" Value="[bool]False" Width="[float]28">
							<Image BaseName="[string]Image" Id="477b01fe1fa1465f9aea3cda4ebe53c1" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomHorizontal.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
						</ComposableButton>
						<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Vertical Zoom" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]ef671f9ffce6446e8fe2d06e4bb7d780" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="8346ad8eb6ea4ffa8e2165adeb296fb4" IsMomentary="[bool]False" Label="[UIModel]2013c87dd264446b9880d1b344f01eeb" Left="[float]32" PartName="[string]PART_ZoomVerticalButton" Top="[float]2" Value="[bool]False" Width="[float]28">
							<Image BaseName="[string]Image" Id="ef671f9ffce6446e8fe2d06e4bb7d780" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomVertical.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
						</ComposableButton>
						<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Pan" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]2689ee1c531448b0b8605f69e1e6983c" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="7216ffebde1846a2866660a4cc882f16" IsMomentary="[bool]False" Label="[UIModel]23e135c08b3e4d5b957dabd1f92d42da" Left="[float]62" PartName="[string]PART_PanButton" Top="[float]2" Value="[bool]False" Width="[float]28">
							<Image BaseName="[string]Image" Id="2689ee1c531448b0b8605f69e1e6983c" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomPan.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
						</ComposableButton>
						<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Reset" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]5aa3d82be4064e388b999d8d7ecd7aaf" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="62524d55a21644988e2fb8ba1e97e7ea" IsMomentary="[bool]True" Label="[UIModel]8afe3674c7544ebd8e9e99a2c56f7c9d" Left="[float]92" PartName="[string]PART_ResetButton" Top="[float]2" Value="[bool]False" Width="[float]28">
							<Image BaseName="[string]Image" Id="5aa3d82be4064e388b999d8d7ecd7aaf" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomExtents.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
						</ComposableButton>
						<Label Id="e70bef5b5e2c40fcb19b5426bcaa9622" LabelOwner="[UIModel]c5bab5e374244f74af63ccfa5da5a447" Left="[float]2" Text="[string]Horizontal Zoom" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
						<Label Id="2013c87dd264446b9880d1b344f01eeb" LabelOwner="[UIModel]8346ad8eb6ea4ffa8e2165adeb296fb4" Left="[float]32" Text="[string]Vertical Zoom" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
						<Label Id="23e135c08b3e4d5b957dabd1f92d42da" LabelOwner="[UIModel]7216ffebde1846a2866660a4cc882f16" Left="[float]62" Text="[string]Pan" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
						<Label Id="8afe3674c7544ebd8e9e99a2c56f7c9d" LabelOwner="[UIModel]62524d55a21644988e2fb8ba1e97e7ea" Left="[float]92" Text="[string]Reset" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
					</ArrayGraphTools>
					<Label Height="[float]16" Id="be4cc3bef0f5419ea42cd58f151b546c" LabelOwner="[UIModel]2d5c61cd3e1b4424b3ffb9838895186f" Left="[float]288" Text="[string]Waveforms" Top="[float]21" Width="[float]60" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{bd779b16-f709-4027-9f10-768896a2a6a3}/Configuration/measurement_pins" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="a8dfb57c6a7246778da2a0ef61ff0812" IsLabelBoundToChannel="[bool]False" Label="[UIModel]cc9d3e113c19449fa891682421d1282c" Left="[float]22" MultipleSelectionMode="[MultipleSelectionModes]List" SelectedResource="[NI_Core_DataValues_TagRefnum]PinGroup1" Top="[float]33" Width="[float]244" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
					<Label Height="[float]16" Id="cc9d3e113c19449fa891682421d1282c" LabelOwner="[UIModel]a8dfb57c6a7246778da2a0ef61ff0812" Left="[float]22" Text="[string]Measurement pins" Top="[float]13" Width="[float]100" xmlns="http://www.ni.com/PanelCommon" />
				</ScreenSurface>
			</Screen>
		</EmbeddedDefinitionReference>
	</EnvoyManagerFile>
</SourceFile>
````
