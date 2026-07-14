# NI OSS SOURCE SNAPSHOT: measurement-plugin-python

<!--NI_OSS_SNAPSHOT repo=ni/measurement-plugin-python commit=2e57ec3e5bd703abc8690f8a46df62b28f0380e2 -->

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niscope_acquire_waveform/NIScopeAcquireWaveform_example.seq sha256=e691fef8111682874653555846530d48f8680298e2a4e4c707b6ee1b9e42ac81 bytes=195534 -->
## FILE: examples/niscope_acquire_waveform/NIScopeAcquireWaveform_example.seq

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niscope_acquire_waveform/NIScopeAcquireWaveform_example.seq`
- sha256: `e691fef8111682874653555846530d48f8680298e2a4e4c707b6ee1b9e42ac81`
- bytes: 195534

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
											<Step typename='NI_Measurement' xsi:type='NI_Measurement' name='Acquire a waveform using an NI oscilloscope'>
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
																<value>ni.examples.NIScopeAcquireWaveform_Python</value>
															</Name>
															<Parameters classname='Objs'>
																<value lbound='[0]' ubound='[15]'>
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
																					<value>measurement_pins</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>{"PinGroup1"}</value>
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
																					<value>vertical_range</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>5</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>false</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
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
																					<value>vertical_coupling</value>
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
																					<value representation='Int64'>3</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>Enum</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[2]'>
																						<value>
																							<Num name='AC'>
																								<value representation='Int64'>0</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='DC'>
																								<value representation='Int64'>1</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='GND'>
																								<value representation='Int64'>2</value>
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
																					<value>input_impedance</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>1000000</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>false</value>
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
																					<value>min_sample_rate</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>10000000</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>false</value>
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
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>min_record_length</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>40000i64</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>false</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeInt32</value>
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
																					<value>trigger_pin</value>
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
																					<value representation='Int64'>7</value>
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
																					<value>trigger_level</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>0.5</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>false</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>8</value>
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
																					<value>trigger_slope</value>
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
																					<value representation='Int64'>9</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>Enum</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[2]'>
																						<value>
																							<Num name='NEGATIVE'>
																								<value representation='Int64'>0</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='POSITIVE'>
																								<value representation='Int64'>1</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='SLOPE_EITHER'>
																								<value representation='Int64'>3</value>
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
																					<value>auto_trigger</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>False</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>false</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeBool</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>10</value>
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
																					<value>trigger_coupling</value>
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
																					<value representation='Int64'>11</value>
																				</ID>
																				<TypeSpecialization classname='Str'>
																					<value>Enum</value>
																				</TypeSpecialization>
																				<EnumDefinition classname='Objs'>
																					<value lbound='[0]' ubound='[4]'>
																						<value>
																							<Num name='AC'>
																								<value representation='Int64'>0</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='DC'>
																								<value representation='Int64'>1</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='HF_REJECT'>
																								<value representation='Int64'>3</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='LF_REJECT'>
																								<value representation='Int64'>4</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='AC_PLUS_HF_REJECT'>
																								<value representation='Int64'>1001</value>
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
																					<value>timeout</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>5</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>false</value>
																				</Log>
																				<Dimension classname='Num'>
																					<value representation='UInt64'>0</value>
																				</Dimension>
																				<Type classname='Str'>
																					<value>TypeDouble</value>
																				</Type>
																				<ID classname='Num'>
																					<value representation='Int64'>12</value>
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
																					<value>waveform0</value>
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
																					<value>waveform1</value>
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
																					<value>TypeDouble</value>
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
																					<value>waveform2</value>
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
																					<value>waveform3</value>
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
																<value>ID#:hZan+9mU7hGhxGDjK76h1B</value>
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
														<value>"NIScopeAcquireWaveform.pinmap"</value>
													</PinMapPath>
												</subprops>
											</Step>
										</value>
										<value>
											<Step typename='Action' xsi:type='Action' name='Create and register NI-Scope Sessions'>
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
																				<value>teststand_niscope.py</value>
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
																				<value>create_niscope_sessions</value>
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
											<Step typename='Action' xsi:type='Action' name='Destroy and unregister NI-Scope Sessions'>
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
																				<value>teststand_niscope.py</value>
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
																				<value>destroy_niscope_sessions</value>
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

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niscope_acquire_waveform/poetry.toml sha256=ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e bytes=34 -->
## FILE: examples/niscope_acquire_waveform/poetry.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niscope_acquire_waveform/poetry.toml`
- sha256: `ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e`
- bytes: 34

````toml
[virtualenvs]
in-project = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niscope_acquire_waveform/pyproject.toml sha256=b19abaca6ec52a0cc9d4d88c3cd6bf41c612b022410509c011062ab6a699d996 bytes=1105 -->
## FILE: examples/niscope_acquire_waveform/pyproject.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niscope_acquire_waveform/pyproject.toml`
- sha256: `b19abaca6ec52a0cc9d4d88c3cd6bf41c612b022410509c011062ab6a699d996`
- bytes: 1105

````toml
[tool.poetry]
name = "niscope_acquire_waveform"
version = "0.5.0"
package-mode = false
description = "Measurement plug-in example that acquires a waveform using an NI oscilloscope."
authors = ["National Instruments"]

[tool.poetry.dependencies]
python = "^3.10"
niscope = { version = ">=1.4.4", extras = ["grpc"] }
ni-measurement-plugin-sdk-service = {version = ">=2.3.1,<4.0"}
click = ">=7.1.2, !=8.1.4" # mypy fails with click 8.1.4: https://github.com/pallets/click/issues/2558
grpcio = "*"

[tool.poetry.group.dev.dependencies]
ni-python-styleguide = ">=0.4.1"
mypy = ">=1.0"
types-grpcio = ">=1.0"
# Uncomment to use prerelease dependencies.
# niscope = { git = "https://github.com/ni/nimi-python.git", subdirectory = "generated/niscope", extras = ["grpc"] }
# ni-measurement-plugin-sdk-service = {path = "../../packages/service", develop = true}

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.mypy]
disallow_untyped_defs = true

[[tool.mypy.overrides]]
module = [
    "niscope.*",
]
ignore_missing_imports = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niscope_acquire_waveform/README.md sha256=56908bea90b924821df0a9b95869c6672701092bca8767fd811d45edf66bd42c bytes=2096 -->
## FILE: examples/niscope_acquire_waveform/README.md

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niscope_acquire_waveform/README.md`
- sha256: `56908bea90b924821df0a9b95869c6672701092bca8767fd811d45edf66bd42c`
- bytes: 2096

````markdown
## NI-SCOPE Acquire Waveform

This is a measurement plug-in example that acquires a waveform using an NI
oscilloscope.

### Features

- Uses the `niscope` package to access NI-SCOPE from Python
- Demonstrates how to cancel a running measurement while polling measurement
  status
- Pin-aware, supporting one session, multiple pins, and one selected site
  - Acquires from up to 4 pins
  - Trigger source demonstrates mapping a specific pin to a channel
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
- NI-SCOPE
- Recommended: TestStand 2021 SP1 or later

### Required Hardware

This example requires an NI oscilloscope (e.g. PXIe-5162 (4CH)).

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
  MEASUREMENT_PLUGIN_NISCOPE_SIMULATE=1
  MEASUREMENT_PLUGIN_NISCOPE_BOARD_TYPE=PXIe
  MEASUREMENT_PLUGIN_NISCOPE_MODEL=5162 (4CH)
  ```
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niscope_acquire_waveform/start.bat sha256=bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851 bytes=253 -->
## FILE: examples/niscope_acquire_waveform/start.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niscope_acquire_waveform/start.bat`
- sha256: `bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851`
- bytes: 253

````batch
@echo off
REM The discovery service uses this script to start the measurement service.
REM You can customize this script for your Python setup. The -v option logs
REM messages with level INFO and above.

.venv\Scripts\python.exe measurement.py -v
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niscope_acquire_waveform/teststand_niscope.py sha256=8a50241190e9eb8205b98311145441dadeb865114ff26234020f7aed48be8e7e bytes=2605 -->
## FILE: examples/niscope_acquire_waveform/teststand_niscope.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niscope_acquire_waveform/teststand_niscope.py`
- sha256: `8a50241190e9eb8205b98311145441dadeb865114ff26234020f7aed48be8e7e`
- bytes: 2605

````python
"""Functions to set up and tear down sessions of NI-Scope devices in NI TestStand."""

from typing import Any

from _helpers import TestStandSupport
from ni_measurement_plugin_sdk_service.discovery import DiscoveryClient
from ni_measurement_plugin_sdk_service.grpc.channelpool import GrpcChannelPool
from ni_measurement_plugin_sdk_service.session_management import (
    INSTRUMENT_TYPE_NI_SCOPE,
    PinMapContext,
    SessionInitializationBehavior,
    SessionManagementClient,
)


def create_niscope_sessions(sequence_context: Any) -> None:
    """Create and register all NI-Scope sessions.

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
            pin_map_context, instrument_type_id=INSTRUMENT_TYPE_NI_SCOPE
        ) as reservation:
            with reservation.initialize_niscope_sessions(
                initialization_behavior=SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH
            ):
                pass

            session_management_client.register_sessions(reservation.session_info)


def destroy_niscope_sessions() -> None:
    """Destroy and unregister all NI-Scope sessions."""
    with GrpcChannelPool() as grpc_channel_pool:
        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with session_management_client.reserve_all_registered_sessions(
            instrument_type_id=INSTRUMENT_TYPE_NI_SCOPE,
        ) as reservation:
            if not reservation.session_info:
                return

            session_management_client.unregister_sessions(reservation.session_info)

            with reservation.initialize_niscope_sessions(
                initialization_behavior=SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE
            ):
                pass
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niswitch_control_relays/.serviceignore sha256=997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912 bytes=148 -->
## FILE: examples/niswitch_control_relays/.serviceignore

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niswitch_control_relays/.serviceignore`
- sha256: `997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912`
- bytes: 148

````text
# This file specifies that when we publish this plug-in to a plug-in library,
# we should not copy the following directories:
.venv
__pycache__
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niswitch_control_relays/_helpers.py sha256=0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426 bytes=2920 -->
## FILE: examples/niswitch_control_relays/_helpers.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niswitch_control_relays/_helpers.py`
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

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niswitch_control_relays/install.bat sha256=695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025 bytes=205 -->
## FILE: examples/niswitch_control_relays/install.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niswitch_control_relays/install.bat`
- sha256: `695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025`
- bytes: 205

````batch
@echo off
REM The discovery service uses this script to install the dependencies
REM for the measurement service. You can customize this script for your
REM Python setup.

poetry install --only main
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niswitch_control_relays/measurement.py sha256=712a040458d4c304f62bdb6365e94fd4ce59c1525854eeeb3a611c87041863c3 bytes=2199 -->
## FILE: examples/niswitch_control_relays/measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niswitch_control_relays/measurement.py`
- sha256: `712a040458d4c304f62bdb6365e94fd4ce59c1525854eeeb3a611c87041863c3`
- bytes: 2199

````python
"""Control relays using an NI relay driver (e.g. PXI-2567)."""

import logging
import pathlib
import sys

import click
import ni_measurement_plugin_sdk_service as nims
from _helpers import configure_logging, verbosity_option
from niswitch.enums import RelayAction

script_or_exe = sys.executable if getattr(sys, "frozen", False) else __file__
service_directory = pathlib.Path(script_or_exe).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "NISwitchControlRelays.serviceconfig",
    ui_file_paths=[service_directory / "NISwitchControlRelays.measui"],
)


@measurement_service.register_measurement
@measurement_service.configuration("relay_names", nims.DataType.String, "SiteRelay1")
@measurement_service.configuration("close_relay", nims.DataType.Boolean, True)
def measure(
    relay_names: str,
    close_relays: bool,
) -> tuple[()]:
    """Control relays using an NI relay driver (e.g. PXI-2567)."""
    logging.info(
        "Controlling relays: relay_names=%s close_relay=%s",
        relay_names,
        close_relays,
    )

    with measurement_service.context.reserve_sessions(relay_names) as reservation:
        with reservation.initialize_niswitch_sessions() as session_infos:
            # Open or close all relays corresponding to the selected pins and
            # sites.
            for session_info in session_infos:
                session_info.session.relay_control(
                    session_info.channel_list,
                    RelayAction.CLOSE if close_relays else RelayAction.OPEN,
                )

            # Wait for all of the relays to activate and debounce.
            for session_info in session_infos:
                session_info.session.wait_for_debounce()

    logging.info("Completed operation")
    return ()


@click.command
@verbosity_option
def main(verbosity: int) -> None:
    """Control relays using an NI relay driver (e.g. PXI-2567)."""
    configure_logging(verbosity)

    with measurement_service.host_service():
        input("Press enter to close the measurement service.\n")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niswitch_control_relays/NISwitchControlRelays.instudioproj sha256=8a2cc0350f883545cf959d7a306b0d2a80538734873ca188a5bfa8b726903eb1 bytes=2031 -->
## FILE: examples/niswitch_control_relays/NISwitchControlRelays.instudioproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niswitch_control_relays/NISwitchControlRelays.instudioproj`
- sha256: `8a2cc0350f883545cf959d7a306b0d2a80538734873ca188a5bfa8b726903eb1`
- bytes: 2031

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="755BBE97F835AF798E1D590F18C5A07D40F11C1489C7A69EEE11449848E465BADA1F9E96D29C7C3A0718749A45828C6486A96023AC96754FA2736517F7CAEB11" xmlns="http://www.ni.com/PlatformFramework">
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
			<FileReference Id="220548d6210a4dd2a988a7b3517efb9e" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="NISwitchControlRelays.pinmap" StoragePath="NISwitchControlRelays.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
			<SourceFileReference Bindings="EnvoyManager" Id="6094280033194578b89a7f8195bf54ae" ModelDefinitionType="NationalInstruments.InstrumentFramework.Document.SourceModel.UnifiedTask" Name="NISwitchControlRelays.sfp" StoragePath="NISwitchControlRelays.sfp" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niswitch_control_relays/NISwitchControlRelays.measproj sha256=5fd2ad02ed0905820a48e71df3d473329587eee8bc8781f2a47be54527da6654 bytes=3820 -->
## FILE: examples/niswitch_control_relays/NISwitchControlRelays.measproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niswitch_control_relays/NISwitchControlRelays.measproj`
- sha256: `5fd2ad02ed0905820a48e71df3d473329587eee8bc8781f2a47be54527da6654`
- bytes: 3820

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="2AFB8D39B5FD6BD2B8D6D21555B12ECCB06AFF011D0BC0C9BD5CE051320AF15E11D0053A0F120AE3C9A15285CD174F65350E5435AF8E74E71DC25B2F3A369D1C" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.0.0.2225" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="23.0.0.2225" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2225" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2225" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/EnvoyManagement" OldestCompatibleVersion="5.0.0.0" Version="5.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2225" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemDiagram" OldestCompatibleVersion="8.0.0.49152" Version="8.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2225" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemModelCore" OldestCompatibleVersion="5.1.0.5" Version="5.2.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.2225" Name="MeasurementLink UI Editor" Version="23.0.0.2225" />
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
			<SourceFileReference Id="ed5e93555f7044dfbef5ebcfe37fdf04" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="NISwitchControlRelays.measui" StoragePath="NISwitchControlRelays.measui" />
			<FileReference Id="91ec00920dff4da997e3a16c2dd4c84c" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="NISwitchControlRelays.pinmap" StoragePath="NISwitchControlRelays.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niswitch_control_relays/NISwitchControlRelays.measui sha256=65aba5d122bb739c6e96f3831cc0152ea98f97ed725c5476c7e95e7dc4b6774c bytes=3508 -->
## FILE: examples/niswitch_control_relays/NISwitchControlRelays.measui

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niswitch_control_relays/NISwitchControlRelays.measui`
- sha256: `65aba5d122bb739c6e96f3831cc0152ea98f97ed725c5476c7e95e7dc4b6774c`
- bytes: 3508

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="4F3FB4CBDC5E2F572D8BD5E2B3D20565F1337B731FAF5DFC96F454B3821DC6A745AFA8C09FD7FAC6624815C584A871F1168AB7F1D9A0C83936CA53FDFC6CDD2A" Timestamp="1D8FB93A6FA1A79" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.7.0.1849" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="6.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.1849" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="23.0.0.1849" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.1849" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.1849" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.1849" Name="MeasurementLink UI Editor" Version="23.0.0.1849" />
	</SourceModelFeatureSet>
	<Screen ClientId="{7fed05fb-fa1b-42d4-ad87-057cceb3a161}" DisplayName="NI-SWITCH Control Relays (Py)" Id="8aaad0184c14eef9bc37e28934c8983" ServiceClass="ni.examples.NISwitchControlRelays_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
		<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]160" Id="2f335a14de344add99fe42aefe8d1927" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]180" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
			<ChannelStringControl AcceptsReturn="[bool]False" BaseName="[string]String" Channel="[string]{7fed05fb-fa1b-42d4-ad87-057cceb3a161}/Configuration/relay_names" Enabled="[bool]True" Height="[float]24" HorizontalScrollBarVisibility="[ScrollBarVisibility]Hidden" Id="ed7a56536e4c4a2788d1cd49a1812eda" IsLabelBoundToChannel="[bool]False" Label="[UIModel]895c5131f04c858236fda3f80a52c8" Left="[float]22" Text="[string]SiteRelay1" Top="[float]33" VerticalScrollBarVisibility="[ScrollBarVisibility]Auto" Width="[float]142" />
			<Label Height="[float]16" Id="895c5131f04c858236fda3f80a52c8" LabelOwner="[UIModel]ed7a56536e4c4a2788d1cd49a1812eda" Left="[float]22" Text="[string]Relay names" Top="[float]13" Width="[float]66" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelSwitch BaseName="[string]Switch" Channel="[string]{7fed05fb-fa1b-42d4-ad87-057cceb3a161}/Configuration/close_relay" Enabled="[bool]True" FalseContent="[string]Open" Height="[float]50" Id="fb3b53a6ec4f4f198ec55b2878fb16b8" IsLabelBoundToChannel="[bool]False" Label="[UIModel]d6f215f36ae4f07833660e49972902e" Left="[float]22" MinHeight="[float]24" MinWidth="[float]12" Orientation="[SMOrientation]Vertical" Shape="[SwitchShape]Slider" Top="[float]92" TrueContent="[string]Close" Width="[float]63" />
			<Label Height="[float]16" Id="d6f215f36ae4f07833660e49972902e" LabelOwner="[UIModel]fb3b53a6ec4f4f198ec55b2878fb16b8" Left="[float]22" Text="[string]Relay action" Top="[float]72" Width="[float]64" xmlns="http://www.ni.com/PanelCommon" />
		</ScreenSurface>
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niswitch_control_relays/NISwitchControlRelays.pinmap sha256=aa96747985c9a40de029fcd2f342ab1bda853e64996d19ac2be2dedfdefd29dc bytes=1332 -->
## FILE: examples/niswitch_control_relays/NISwitchControlRelays.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niswitch_control_relays/NISwitchControlRelays.pinmap`
- sha256: `aa96747985c9a40de029fcd2f342ab1bda853e64996d19ac2be2dedfdefd29dc`
- bytes: 1332

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.4">
	<Instruments>
		<NIRelayDriverModule name="RelayDriver1" numberOfControlLines="64" />
	</Instruments>
	<Pins></Pins>
	<PinGroups></PinGroups>
	<Relays>
		<SiteRelay name="SiteRelay1" />
		<SiteRelay name="SiteRelay2" />
		<SystemRelay name="SystemRelay1" />
		<SystemRelay name="SystemRelay2" />
	</Relays>
	<RelayGroups>
		<RelayGroup name="AllSiteRelays">
			<RelayReference relay="SiteRelay1" />
			<RelayReference relay="SiteRelay2" />
		</RelayGroup>
		<RelayGroup name="AllSystemRelays">
			<RelayReference relay="SystemRelay1" />
			<RelayReference relay="SystemRelay2" />
		</RelayGroup>
	</RelayGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<RelayConnection relay="SiteRelay1" siteNumber="0" relayDriverModule="RelayDriver1" controlLine="K0" />
		<RelayConnection relay="SiteRelay2" siteNumber="0" relayDriverModule="RelayDriver1" controlLine="K1" />
		<SystemRelayConnection relay="SystemRelay1" relayDriverModule="RelayDriver1" controlLine="K2" />
		<SystemRelayConnection relay="SystemRelay2" relayDriverModule="RelayDriver1" controlLine="K3" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niswitch_control_relays/NISwitchControlRelays.serviceconfig sha256=562cf1ba38963cca06a31cc4914a665c46a2d053272735161e9486bb3d085d9b bytes=697 -->
## FILE: examples/niswitch_control_relays/NISwitchControlRelays.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niswitch_control_relays/NISwitchControlRelays.serviceconfig`
- sha256: `562cf1ba38963cca06a31cc4914a665c46a2d053272735161e9486bb3d085d9b`
- bytes: 697

````json
{
  "services": [
    {
      "displayName": "NI-SWITCH Control Relays (Py)",
      "version": "1.0.0",
      "serviceClass": "ni.examples.NISwitchControlRelays_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "installPath": "install.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in example that controls relays using an NI relay driver (e.g. PXI-2567).",
        "ni/service.collection": "NI.Examples",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niswitch_control_relays/NISwitchControlRelays.sfp sha256=23b73d5c4bbcb73a2fa503e776c6b6101e44e3d994d87ec1970c3a6b33e1e5eb bytes=6496 -->
## FILE: examples/niswitch_control_relays/NISwitchControlRelays.sfp

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niswitch_control_relays/NISwitchControlRelays.sfp`
- sha256: `23b73d5c4bbcb73a2fa503e776c6b6101e44e3d994d87ec1970c3a6b33e1e5eb`
- bytes: 6496

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="E0347EF7EE8F0FAB7BB1E4A560D6A3EE83A79B6BD7E501463D9C08927C26FE76AAFCCE06DC298A001E53DA273B91AFBB1CDE7071B5D2D7F305D15F115E4229CA" Timestamp="1D909DECD67F1F5" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.7.0.2317" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="6.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2317" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="23.0.0.2317" FeatureSetName="UnifiedTask" Name="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" Version="1.0.0.0" />
		<ParsableNamespace AssemblyFileVersion="23.0.0.2317" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2317" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2317" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.2317" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="23.0.0.2317" />
	</SourceModelFeatureSet>
	<UnifiedTask Id="eae6a11e71754b7fb4e092de32ccc22e" LayoutInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Layout Information&quot;:{&quot;Sections&quot;:[{&quot;Columns Progressive Count&quot;:1,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Columns&quot;:[{&quot;Containers Progressive Count&quot;:1,&quot;Layout Information Index&quot;:0,&quot;Containers&quot;:[{&quot;Container Model Defition&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Container Assignment State&quot;:&quot;Available&quot;,&quot;Container Identifier&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen.task&quot;,&quot;Container Instrument Name&quot;:&quot;NI-SWITCH Control Relays (Py)&quot;,&quot;Layout Information Name&quot;:&quot;NI-SWITCH Control Relays (Py) 1&quot;,&quot;Layout Information Index&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Items&quot;:[{&quot;Identification Number&quot;:4294963201,&quot;Model Definition Type&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Parent Or Group Name&quot;:&quot;Measurements&quot;,&quot;Panel Type&quot;:&quot;NI-SWITCH Control Relays (Py)&quot;,&quot;Layout Information Name&quot;:&quot;ni.examples.NISwitchControlRelays_Python&quot;,&quot;Layout Information Index&quot;:0}]}]}]},{&quot;Columns Progressive Count&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationOnly&quot;}]}}" PinAwareInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Selected Sites&quot;:[{&quot;Site Number&quot;:0}]}" xmlns="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" />
	<EnvoyManagerFile Id="b5fd673a4af44cfe94af37dd90399b29" xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="27c54b1509be4834804fed64e519423a" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<NameScopingEnvoy AutomaticallyResolveUp="True" Id="9054e16db0954590b631a9972fdaf160" Name="NISwitchControlRelays.sfp" NameTracksFileName="True" />
		<EmbeddedDefinitionReference Id="bccff83056254616bb26cdab22bbf87e" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="{http\://www.ni.com/InstrumentFramework/ScreenDocument}Screen.task">
			<Screen ClientId="{503f784f-b340-4d87-9e53-296570d966c8}" ConfigurationParameters="{&quot;@type&quot;:&quot;type.googleapis.com/ni.measurementlink.measurement.v1.MeasurementConfigurations&quot;,&quot;relayNames&quot;:&quot;SiteRelay1&quot;,&quot;closeRelay&quot;:true}" DisplayName="NI-SWITCH Control Relays (Py)" Id="c83c6a63fe2b47a088a0743ad571f1a2" PanelPresentation="ConfigurationWithVisualization" ServiceClass="ni.examples.NISwitchControlRelays_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
				<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]160" Id="776fc7863b8c48a3a4dc7eb828bafc9e" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]180" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
					<ChannelStringControl AcceptsReturn="[bool]False" BaseName="[string]String" Channel="[string]{503f784f-b340-4d87-9e53-296570d966c8}/Configuration/relay_names" Enabled="[bool]True" Height="[float]24" HorizontalScrollBarVisibility="[ScrollBarVisibility]Hidden" Id="902e608d1b424b0da9e02a33e30401a1" IsLabelBoundToChannel="[bool]False" Label="[UIModel]84e31d550c3242c9b28273eddac706cf" Left="[float]22" Text="[string]SiteRelay1" Top="[float]33" VerticalScrollBarVisibility="[ScrollBarVisibility]Auto" Width="[float]142" />
					<Label Height="[float]16" Id="84e31d550c3242c9b28273eddac706cf" LabelOwner="[UIModel]902e608d1b424b0da9e02a33e30401a1" Left="[float]22" Text="[string]Relay names" Top="[float]13" Width="[float]66" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelSwitch BaseName="[string]Switch" Channel="[string]{503f784f-b340-4d87-9e53-296570d966c8}/Configuration/close_relay" Enabled="[bool]True" FalseContent="[string]Open" Height="[float]50" Id="32196c5f764240ed9e17a02cbafa576e" IsLabelBoundToChannel="[bool]False" Label="[UIModel]c4d6a6a76ebc46cba469b2fd3eae5c5f" Left="[float]22" MinHeight="[float]24" MinWidth="[float]12" Orientation="[SMOrientation]Vertical" Shape="[SwitchShape]Slider" Top="[float]92" TrueContent="[string]Close" Width="[float]63" />
					<Label Height="[float]16" Id="c4d6a6a76ebc46cba469b2fd3eae5c5f" LabelOwner="[UIModel]32196c5f764240ed9e17a02cbafa576e" Left="[float]22" Text="[string]Relay action" Top="[float]72" Width="[float]64" xmlns="http://www.ni.com/PanelCommon" />
				</ScreenSurface>
			</Screen>
		</EmbeddedDefinitionReference>
	</EnvoyManagerFile>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niswitch_control_relays/NISwitchControlRelays_example.seq sha256=691a4f518471bf38b7547b61c10b6efff2cf8f1b3a5388f339f14ee1ffc37640 bytes=317867 -->
## FILE: examples/niswitch_control_relays/NISwitchControlRelays_example.seq

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niswitch_control_relays/NISwitchControlRelays_example.seq`
- sha256: `691a4f518471bf38b7547b61c10b6efff2cf8f1b3a5388f339f14ee1ffc37640`
- bytes: 317867

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
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='23'>
			<NI_CommonCParameterResult classname='CommonCParameterResult' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
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
			</NI_CommonCParameterResult>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='24'>
			<FCParameter classname='FCParameter' isroottypedef='true' typecategory='3' timestamp='1650060844' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Name classname='Str'>
						<value>_notNamed</value>
					</Name>
					<Type classname='Num'>
						<value>0</value>
					</Type>
					<NumType classname='Num'>
						<value>4</value>
					</NumType>
					<ObjType classname='Num'>
						<value>0</value>
					</ObjType>
					<StructType classname='Str'>
						<value/>
					</StructType>
					<NumPass classname='Num'>
						<value>0</value>
					</NumPass>
					<StrPass classname='Num'>
						<value>0</value>
					</StrPass>
					<ElemPass classname='Num'>
						<value>0</value>
					</ElemPass>
					<ArrayDimensionsSize classname='Objs'>
						<value lbound='[0]' ubound='[]'>
							<elemproto>
								<_NAME_IN_ATTRIBUTE_ typename='Expression' xsi:type='Expression' name='' classname='ExprValue' structureflags='131072'>
									<value>1024</value>
								</_NAME_IN_ATTRIBUTE_>
							</elemproto>
						</value>
					</ArrayDimensionsSize>
					<StrSize typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value>1024</value>
					</StrSize>
					<ResultAct classname='Num' instanceoverrideflags='5177368'>
						<value>0</value>
					</ResultAct>
					<ArgVal typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgVal>
					<ArgDisplayVal typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgDisplayVal>
					<Flags classname='Num' instanceoverrideflags='5177368'>
						<value>0</value>
					</Flags>
					<AdditionalResults classname='Obj'>
						<subprops>
							<Input typename='NI_CommonCParameterResult' xsi:type='NI_CommonCParameterResult' classname='CommonCParameterResult'>
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
							<Output typename='NI_CommonCParameterResult' xsi:type='NI_CommonCParameterResult' classname='CommonCParameterResult'>
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
					<ArgValImag typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ArgValImag>
				</subprops>
			</FCParameter>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='25'>
			<FlexCStepAdditions classname='FCModule' isroottypedef='true' typecategory='3' timestamp='1650060844' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'>
				<subprops>
					<Call classname='ExternalCall'>
						<subprops>
							<LibPath typename='Path' xsi:type='Path' classname='PathValue'>
								<value/>
							</LibPath>
							<Func classname='Str'>
								<value/>
							</Func>
							<Parms classname='Objs'>
								<value lbound='[0]' ubound='[0]'>
									<elemproto>
										<_NAME_IN_ATTRIBUTE_ typename='FCParameter' xsi:type='FCParameter' name='' classname='FCParameter' structureflags='131072'>
											<subprops>
												<Name classname='Str'>
													<value>_notNamed</value>
												</Name>
												<Type classname='Num'>
													<value>0</value>
												</Type>
												<NumType classname='Num'>
													<value>4</value>
												</NumType>
												<ObjType classname='Num'>
													<value>0</value>
												</ObjType>
												<StructType classname='Str'>
													<value/>
												</StructType>
												<NumPass classname='Num'>
													<value>0</value>
												</NumPass>
												<StrPass classname='Num'>
													<value>0</value>
												</StrPass>
												<ElemPass classname='Num'>
													<value>0</value>
												</ElemPass>
												<ArrayDimensionsSize classname='Objs'>
													<value lbound='[0]' ubound='[]'>
														<elemproto>
															<_NAME_IN_ATTRIBUTE_ name='' classname='ExprValue' structureflags='0'>
																<value>1024</value>
															</_NAME_IN_ATTRIBUTE_>
														</elemproto>
													</value>
												</ArrayDimensionsSize>
												<StrSize classname='ExprValue'>
													<value>1024</value>
												</StrSize>
												<ResultAct classname='Num'>
													<value>0</value>
												</ResultAct>
												<ArgVal classname='ExprValue'>
													<value/>
												</ArgVal>
												<ArgDisplayVal classname='ExprValue'>
													<value/>
												</ArgDisplayVal>
												<Flags classname='Num'>
													<value>0</value>
												</Flags>
												<AdditionalResults classname='Obj'>
													<subprops>
														<Input classname='CommonCParameterResult'>
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
														<Output classname='CommonCParameterResult'>
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
												<ArgValImag classname='ExprValue'>
													<value/>
												</ArgValImag>
											</subprops>
										</_NAME_IN_ATTRIBUTE_>
									</elemproto>
									<value>
										<FCParameter typename='FCParameter' xsi:type='FCParameter' name=''>
											<subprops>
												<Name classname='Str'>
													<value>Return Value</value>
												</Name>
												<Type classname='Num'>
													<value>3</value>
												</Type>
												<NumType classname='Num'>
													<value>4</value>
												</NumType>
												<ObjType classname='Num'>
													<value>0</value>
												</ObjType>
												<StructType classname='Str'>
													<value/>
												</StructType>
												<NumPass classname='Num'>
													<value>0</value>
												</NumPass>
												<StrPass classname='Num'>
													<value>0</value>
												</StrPass>
												<ElemPass classname='Num'>
													<value>0</value>
												</ElemPass>
												<ArrayDimensionsSize classname='Objs'>
													<value lbound='[0]' ubound='[]'>
														<elemproto>
															<_NAME_IN_ATTRIBUTE_ name='' classname='ExprValue' structureflags='0'>
																<value>1024</value>
															</_NAME_IN_ATTRIBUTE_>
														</elemproto>
													</value>
												</ArrayDimensionsSize>
												<StrSize classname='ExprValue'>
													<value>1024</value>
												</StrSize>
												<ResultAct classname='Num'>
													<value>0</value>
												</ResultAct>
												<ArgVal classname='ExprValue'>
													<value/>
												</ArgVal>
												<ArgDisplayVal classname='ExprValue'>
													<value/>
												</ArgDisplayVal>
												<Flags classname='Num'>
													<value>0</value>
												</Flags>
												<AdditionalResults classname='Obj'>
													<subprops>
														<Input classname='CommonCParameterResult'>
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
														<Output classname='CommonCParameterResult'>
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
												<ArgValImag classname='ExprValue'>
													<value/>
												</ArgValImag>
											</subprops>
										</FCParameter>
									</value>
								</value>
							</Parms>
						</subprops>
					</Call>
					<ModuleSrcPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModuleSrcPath>
					<ModulePrjPath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModulePrjPath>
					<ModuleWorkspacePath typename='Path' xsi:type='Path' classname='PathValue'>
						<value/>
					</ModuleWorkspacePath>
					<CodeTemplateName classname='Str'>
						<value/>
					</CodeTemplateName>
					<ModuleCreateSrcType classname='Num'>
						<value>0</value>
					</ModuleCreateSrcType>
				</subprops>
			</FlexCStepAdditions>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='22'>
			<EditSubstep classname='StepType' isroottypedef='true' typecategory='1' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554438' flagsforinstances='4194304' instanceoverrideflags='4194304'>
				<subprops>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>"%ModuleDescription"</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_STEPTYPES", "EDIT_DEF_SUBSTEP_NAME")</value>
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
								<value>ResStr("NI_STEPTYPES", "EDIT_SUBSTEP_MENU_ITEM_NAME")</value>
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
								<value>EditSubsteps</value>
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
					<MenuName typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</MenuName>
					<SupportsReadOnly classname='Bool'>
						<value>false</value>
					</SupportsReadOnly>
					<HasEditPanel classname='Bool'>
						<value>false</value>
					</HasEditPanel>
				</subprops>
			</EditSubstep>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='29'>
			<NI_Wait classname='StepType' isroottypedef='true' typecategory='1' timestamp='1618215666' typeversion='21.0.0.2' typelastmodversion='21.0.0.0' typeminprodversion='21.0.0.0' typeflags='33554446'>
				<subprops>
					<DescriptionFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_WAIT_STEP_TYPE_TARGET_NAME", Str(Step.WaitForTarget)) +
"(" +
((Step.WaitForTarget == 0) ? LocalizeExpression(Step.TimeExpr):
 (Step.WaitForTarget == 1) ? LocalizeExpression(Step.TimeExpr):
 (Step.WaitForTarget == 2) ?
       (Step.SpecifyBySeqCall
         ? ((Step.SeqCallName == "")
             ? ResStr("NI_WAIT_STEP_TYPE", "UNSPECIFIED")
             : TargetName(RunState.Sequence, Step.SeqCallName, false, true, Step.SeqCallStepGroupIdx, RunState.StepGroup))
         : LocalizeExpression(Step.ThreadRefExpr)) :
 (Step.WaitForTarget == 3) ?
       (Step.SpecifyBySeqCall
         ? ((Step.SeqCallName == "")
             ? ResStr("NI_WAIT_STEP_TYPE", "UNSPECIFIED")
             : TargetName(RunState.Sequence, Step.SeqCallName, false, true, Step.SeqCallStepGroupIdx, RunState.StepGroup))
         : LocalizeExpression(Step.ExecutionRefExpr)) :
 "")
+ ")"</value>
					</DescriptionFormat>
					<DefaultNameFormat typename='Expression' xsi:type='Expression' classname='ExprValue' flagsforinstances='4718616' instanceoverrideflags='4718616' valueflags='4194328' structureflags='524288'>
						<value>ResStr("NI_WAIT_STEP_TYPE", "DEF_STEP_NAME")</value>
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
								<value>ResStr("NI_WAIT_STEP_TYPE", "MENU_ITEM_NAME")</value>
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
								<value>NI_NonAdvSynchronization</value>
							</Group>
						</subprops>
					</Menu>
					<Substeps typename='StepTypeSubstepsArray' xsi:type='StepTypeSubstepsArray' classname='Objs' flagsforinstances='524312' instanceoverrideflags='655384'>
						<value lbound='[0]' ubound='[2]'>
							<value>
								<Step typename='Substep' xsi:type='Substep' name='OnNewStep'>
									<subprops>
										<TS classname='Obj'>
											<subprops>
												<Id classname='Str'>
													<value>ID#:yr4D9fxyAUOd3qDH2OVePB</value>
												</Id>
												<Icon classname='Str'>
													<value/>
												</Icon>
												<SData typename='FlexCStepAdditions' xsi:type='FlexCStepAdditions' classname='FCModule' structureflags='2097152'>
													<subprops>
														<Call classname='ExternalCall'>
															<subprops>
																<LibPath classname='PathValue'>
																	<value>syncsteps.dll</value>
																</LibPath>
																<Func classname='Str'>
																	<value>?SetWaitAdditionalResultsHintsForOperation@@YAXPAUStep@TS@@@Z</value>
																</Func>
																<Parms classname='Objs'>
																	<value lbound='[0]' ubound='[1]'>
																		<elemproto>
																			<_NAME_IN_ATTRIBUTE_ name='' classname='FCParameter' structureflags='0'/>
																		</elemproto>
																		<value>
																			<FCParameter typename='FCParameter' xsi:type='FCParameter' name=''>
																				<subprops>
																					<Name classname='Str'>
																						<value>Return Value</value>
																					</Name>
																					<Type classname='Num'>
																						<value>3</value>
																					</Type>
																					<NumType classname='Num'>
																						<value>4</value>
																					</NumType>
																					<ObjType classname='Num'>
																						<value>0</value>
																					</ObjType>
																					<StructType classname='Str'>
																						<value/>
																					</StructType>
																					<NumPass classname='Num'>
																						<value>0</value>
																					</NumPass>
																					<StrPass classname='Num'>
																						<value>0</value>
																					</StrPass>
																					<ElemPass classname='Num'>
																						<value>0</value>
																					</ElemPass>
																					<ArrayDimensionsSize classname='Objs'>
																						<value lbound='[0]' ubound='[]'>
																							<elemproto>
																								<_NAME_IN_ATTRIBUTE_ name='' classname='ExprValue' structureflags='0'>
																									<value>1024</value>
																								</_NAME_IN_ATTRIBUTE_>
																							</elemproto>
																						</value>
																					</ArrayDimensionsSize>
																					<StrSize classname='ExprValue'>
																						<value>1024</value>
																					</StrSize>
																					<ResultAct classname='Num' instanceoverrideflags='5177369'>
																						<value>0</value>
																					</ResultAct>
																					<ArgVal classname='ExprValue'>
																						<value/>
																					</ArgVal>
																					<ArgDisplayVal classname='ExprValue'>
																						<value/>
																					</ArgDisplayVal>
																					<Flags classname='Num' instanceoverrideflags='5177369'>
																						<value>0</value>
																					</Flags>
																					<AdditionalResults classname='Obj'>
																						<subprops>
																							<Input classname='CommonCParameterResult'>
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
																							<Output classname='CommonCParameterResult'>
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
																					<ArgValImag classname='ExprValue'>
																						<value/>
																					</ArgValImag>
																				</subprops>
																			</FCParameter>
																		</value>
																		<value>
																			<FCParameter typename='FCParameter' xsi:type='FCParameter' name=''>
																				<subprops>
																					<Name classname='Str'>
																						<value>_notNamed</value>
																					</Name>
																					<Type classname='Num'>
																						<value>205</value>
																					</Type>
																					<NumType classname='Num'>
																						<value>4</value>
																					</NumType>
																					<ObjType classname='Num'>
																						<value>0</value>
																					</ObjType>
																					<StructType classname='Str'>
																						<value>TS::Step</value>
																					</StructType>
																					<NumPass classname='Num'>
																						<value>0</value>
																					</NumPass>
																					<StrPass classname='Num'>
																						<value>0</value>
																					</StrPass>
																					<ElemPass classname='Num'>
																						<value>0</value>
																					</ElemPass>
																					<ArrayDimensionsSize classname='Objs'>
																						<value lbound='[0]' ubound='[]'>
																							<elemproto>
																								<_NAME_IN_ATTRIBUTE_ name='' classname='ExprValue' structureflags='0'>
																									<value>1024</value>
																								</_NAME_IN_ATTRIBUTE_>
																							</elemproto>
																						</value>
																					</ArrayDimensionsSize>
																					<StrSize classname='ExprValue'>
																						<value>1024</value>
																					</StrSize>
																					<ResultAct classname='Num' instanceoverrideflags='5177369'>
																						<value>0</value>
																					</ResultAct>
																					<ArgVal classname='ExprValue'>
																						<value>Step</value>
																					</ArgVal>
																					<ArgDisplayVal classname='ExprValue'>
																						<value/>
																					</ArgDisplayVal>
																					<Flags classname='Num' instanceoverrideflags='5177369'>
																						<value>0</value>
																					</Flags>
																					<AdditionalResults classname='Obj'>
																						<subprops>
																							<Input classname='CommonCParameterResult'>
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
																							<Output classname='CommonCParameterResult'>
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
																					<ArgValImag classname='ExprValue'>
																						<value/>
																					</ArgValImag>
																				</subprops>
																			</FCParameter>
																		</value>
																	</value>
																</Parms>
															</subprops>
														</Call>
														<ModuleSrcPath classname='PathValue'>
															<value/>
														</ModuleSrcPath>
														<ModulePrjPath classname='PathValue'>
															<value/>
														</ModulePrjPath>
														<ModuleWorkspacePath classname='PathValue'>
															<value/>
														</ModuleWorkspacePath>
														<CodeTemplateName classname='Str'>
															<value/>
														</CodeTemplateName>
														<ModuleCreateSrcType classname='Num'>
															<value>0</value>
														</ModuleCreateSrcType>
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
								<Step typename='PostSubstep' xsi:type='PostSubstep' name='Post'>
									<subprops>
										<TS classname='Obj' flagsforinstances='262168' instanceoverrideflags='262168'>
											<subprops>
												<Id classname='Str'>
													<value/>
												</Id>
												<Icon classname='Str'>
													<value/>
												</Icon>
												<SData typename='FlexCStepAdditions' xsi:type='FlexCStepAdditions' classname='FCModule' flagsforinstances='2097152' instanceoverrideflags='2097152' structureflags='2097152'>
													<subprops>
														<Call classname='ExternalCall'>
															<subprops>
																<LibPath classname='PathValue'>
																	<value>SyncSteps.dll</value>
																</LibPath>
																<Func classname='Str'>
																	<value>DoWaitStep</value>
																</Func>
																<Parms classname='Objs'>
																	<value lbound='[0]' ubound='[1]'>
																		<elemproto>
																			<_NAME_IN_ATTRIBUTE_ name='' classname='FCParameter' structureflags='0'/>
																		</elemproto>
																		<value>
																			<FCParameter typename='FCParameter' xsi:type='FCParameter' name=''>
																				<subprops>
																					<Name classname='Str'>
																						<value>Return Value</value>
																					</Name>
																					<Type classname='Num'>
																						<value>3</value>
																					</Type>
																					<NumType classname='Num'>
																						<value>4</value>
																					</NumType>
																					<ObjType classname='Num'>
																						<value>0</value>
																					</ObjType>
																					<StructType classname='Str'>
																						<value/>
																					</StructType>
																					<NumPass classname='Num'>
																						<value>0</value>
																					</NumPass>
																					<StrPass classname='Num'>
																						<value>0</value>
																					</StrPass>
																					<ElemPass classname='Num'>
																						<value>0</value>
																					</ElemPass>
																					<ArrayDimensionsSize classname='Objs'>
																						<value lbound='[0]' ubound='[]'>
																							<elemproto>
																								<_NAME_IN_ATTRIBUTE_ name='' classname='ExprValue' structureflags='0'>
																									<value>1024</value>
																								</_NAME_IN_ATTRIBUTE_>
																							</elemproto>
																						</value>
																					</ArrayDimensionsSize>
																					<StrSize classname='ExprValue'>
																						<value>1024</value>
																					</StrSize>
																					<ResultAct classname='Num' instanceoverrideflags='5177369'>
																						<value>0</value>
																					</ResultAct>
																					<ArgVal classname='ExprValue'>
																						<value/>
																					</ArgVal>
																					<ArgDisplayVal classname='ExprValue'>
																						<value/>
																					</ArgDisplayVal>
																					<Flags classname='Num' instanceoverrideflags='5177369'>
																						<value>0</value>
																					</Flags>
																					<AdditionalResults classname='Obj'>
																						<subprops>
																							<Input classname='CommonCParameterResult'>
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
																							<Output classname='CommonCParameterResult'>
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
																					<ArgValImag classname='ExprValue'>
																						<value/>
																					</ArgValImag>
																				</subprops>
																			</FCParameter>
																		</value>
																		<value>
																			<FCParameter typename='FCParameter' xsi:type='FCParameter' name=''>
																				<subprops>
																					<Name classname='Str'>
																						<value>seqContext</value>
																					</Name>
																					<Type classname='Num'>
																						<value>4</value>
																					</Type>
																					<NumType classname='Num'>
																						<value>4</value>
																					</NumType>
																					<ObjType classname='Num'>
																						<value>0</value>
																					</ObjType>
																					<StructType classname='Str'>
																						<value/>
																					</StructType>
																					<NumPass classname='Num'>
																						<value>0</value>
																					</NumPass>
																					<StrPass classname='Num'>
																						<value>0</value>
																					</StrPass>
																					<ElemPass classname='Num'>
																						<value>0</value>
																					</ElemPass>
																					<ArrayDimensionsSize classname='Objs'>
																						<value lbound='[0]' ubound='[]'>
																							<elemproto>
																								<_NAME_IN_ATTRIBUTE_ name='' classname='ExprValue' structureflags='0'>
																									<value>1024</value>
																								</_NAME_IN_ATTRIBUTE_>
																							</elemproto>
																						</value>
																					</ArrayDimensionsSize>
																					<StrSize classname='ExprValue'>
																						<value>1024</value>
																					</StrSize>
																					<ResultAct classname='Num' instanceoverrideflags='5177369'>
																						<value>0</value>
																					</ResultAct>
																					<ArgVal classname='ExprValue'>
																						<value>ThisContext</value>
																					</ArgVal>
																					<ArgDisplayVal classname='ExprValue'>
																						<value>ThisContext</value>
																					</ArgDisplayVal>
																					<Flags classname='Num' instanceoverrideflags='5177369'>
																						<value>0</value>
																					</Flags>
																					<AdditionalResults classname='Obj'>
																						<subprops>
																							<Input classname='CommonCParameterResult'>
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
																							<Output classname='CommonCParameterResult'>
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
																					<ArgValImag classname='ExprValue'>
																						<value/>
																					</ArgValImag>
																				</subprops>
																			</FCParameter>
																		</value>
																	</value>
																</Parms>
															</subprops>
														</Call>
														<ModuleSrcPath classname='PathValue'>
															<value/>
														</ModuleSrcPath>
														<ModulePrjPath classname='PathValue'>
															<value/>
														</ModulePrjPath>
														<ModuleWorkspacePath classname='PathValue'>
															<value/>
														</ModuleWorkspacePath>
														<CodeTemplateName classname='Str'>
															<value/>
														</CodeTemplateName>
														<ModuleCreateSrcType classname='Num'>
															<value>0</value>
														</ModuleCreateSrcType>
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
																		<value>"Foo"</value>
																	</Name>
																	<ValueToLog classname='ExprValue'>
																		<value>12</value>
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
																		<value>false</value>
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
												<Error classname='Obj' instanceoverrideflags='4194304'>
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
												<ReportText classname='Str' flagsforinstances='0'>
													<value/>
												</ReportText>
												<Common classname='Obj' instanceoverrideflags='4194304'/>
											</subprops>
										</Result>
									</subprops>
								</Step>
							</value>
							<value>
								<Step typename='EditSubstep' xsi:type='EditSubstep' name='Edit'>
									<subprops>
										<TS classname='Obj' flagsforinstances='262168' instanceoverrideflags='262168'>
											<subprops>
												<Id classname='Str'>
													<value/>
												</Id>
												<Icon classname='Str'>
													<value/>
												</Icon>
												<SData typename='FlexCStepAdditions' xsi:type='FlexCStepAdditions' classname='FCModule' flagsforinstances='2097152' instanceoverrideflags='2097152' structureflags='2097152'>
													<subprops>
														<Call classname='ExternalCall'>
															<subprops>
																<LibPath classname='PathValue'>
																	<value>SyncSteps.dll</value>
																</LibPath>
																<Func classname='Str'>
																	<value>EditWaitStep</value>
																</Func>
																<Parms classname='Objs'>
																	<value lbound='[0]' ubound='[3]'>
																		<elemproto>
																			<_NAME_IN_ATTRIBUTE_ name='' classname='FCParameter' structureflags='0'/>
																		</elemproto>
																		<value>
																			<FCParameter typename='FCParameter' xsi:type='FCParameter' name=''>
																				<subprops>
																					<Name classname='Str'>
																						<value>Return Value</value>
																					</Name>
																					<Type classname='Num'>
																						<value>3</value>
																					</Type>
																					<NumType classname='Num'>
																						<value>4</value>
																					</NumType>
																					<ObjType classname='Num'>
																						<value>0</value>
																					</ObjType>
																					<StructType classname='Str'>
																						<value/>
																					</StructType>
																					<NumPass classname='Num'>
																						<value>0</value>
																					</NumPass>
																					<StrPass classname='Num'>
																						<value>0</value>
																					</StrPass>
																					<ElemPass classname='Num'>
																						<value>0</value>
																					</ElemPass>
																					<ArrayDimensionsSize classname='Objs'>
																						<value lbound='[0]' ubound='[]'>
																							<elemproto>
																								<_NAME_IN_ATTRIBUTE_ name='' classname='ExprValue' structureflags='0'>
																									<value>1024</value>
																								</_NAME_IN_ATTRIBUTE_>
																							</elemproto>
																						</value>
																					</ArrayDimensionsSize>
																					<StrSize classname='ExprValue'>
																						<value>1024</value>
																					</StrSize>
																					<ResultAct classname='Num' instanceoverrideflags='5177369'>
																						<value>0</value>
																					</ResultAct>
																					<ArgVal classname='ExprValue'>
																						<value/>
																					</ArgVal>
																					<ArgDisplayVal classname='ExprValue'>
																						<value/>
																					</ArgDisplayVal>
																					<Flags classname='Num' instanceoverrideflags='5177369'>
																						<value>0</value>
																					</Flags>
																					<AdditionalResults classname='Obj'>
																						<subprops>
																							<Input classname='CommonCParameterResult'>
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
																							<Output classname='CommonCParameterResult'>
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
																					<ArgValImag classname='ExprValue'>
																						<value/>
																					</ArgValImag>
																				</subprops>
																			</FCParameter>
																		</value>
																		<value>
																			<FCParameter typename='FCParameter' xsi:type='FCParameter' name=''>
																				<subprops>
																					<Name classname='Str'>
																						<value>seqContextDisp</value>
																					</Name>
																					<Type classname='Num'>
																						<value>4</value>
																					</Type>
																					<NumType classname='Num'>
																						<value>4</value>
																					</NumType>
																					<ObjType classname='Num'>
																						<value>0</value>
																					</ObjType>
																					<StructType classname='Str'>
																						<value/>
																					</StructType>
																					<NumPass classname='Num'>
																						<value>0</value>
																					</NumPass>
																					<StrPass classname='Num'>
																						<value>0</value>
																					</StrPass>
																					<ElemPass classname='Num'>
																						<value>0</value>
																					</ElemPass>
																					<ArrayDimensionsSize classname='Objs'>
																						<value lbound='[0]' ubound='[]'>
																							<elemproto>
																								<_NAME_IN_ATTRIBUTE_ name='' classname='ExprValue' structureflags='0'>
																									<value>1024</value>
																								</_NAME_IN_ATTRIBUTE_>
																							</elemproto>
																						</value>
																					</ArrayDimensionsSize>
																					<StrSize classname='ExprValue'>
																						<value>1024</value>
																					</StrSize>
																					<ResultAct classname='Num' instanceoverrideflags='5177369'>
																						<value>0</value>
																					</ResultAct>
																					<ArgVal classname='ExprValue'>
																						<value>ThisContext</value>
																					</ArgVal>
																					<ArgDisplayVal classname='ExprValue'>
																						<value/>
																					</ArgDisplayVal>
																					<Flags classname='Num' instanceoverrideflags='5177369'>
																						<value>0</value>
																					</Flags>
																					<AdditionalResults classname='Obj'>
																						<subprops>
																							<Input classname='CommonCParameterResult'>
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
																							<Output classname='CommonCParameterResult'>
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
																					<ArgValImag classname='ExprValue'>
																						<value/>
																					</ArgValImag>
																				</subprops>
																			</FCParameter>
																		</value>
																		<value>
																			<FCParameter typename='FCParameter' xsi:type='FCParameter' name=''>
																				<subprops>
																					<Name classname='Str'>
																						<value>reserved</value>
																					</Name>
																					<Type classname='Num'>
																						<value>0</value>
																					</Type>
																					<NumType classname='Num'>
																						<value>4</value>
																					</NumType>
																					<ObjType classname='Num'>
																						<value>0</value>
																					</ObjType>
																					<StructType classname='Str'>
																						<value/>
																					</StructType>
																					<NumPass classname='Num'>
																						<value>0</value>
																					</NumPass>
																					<StrPass classname='Num'>
																						<value>0</value>
																					</StrPass>
																					<ElemPass classname='Num'>
																						<value>0</value>
																					</ElemPass>
																					<ArrayDimensionsSize classname='Objs'>
																						<value lbound='[0]' ubound='[]'>
																							<elemproto>
																								<_NAME_IN_ATTRIBUTE_ name='' classname='ExprValue' structureflags='0'>
																									<value>1024</value>
																								</_NAME_IN_ATTRIBUTE_>
																							</elemproto>
																						</value>
																					</ArrayDimensionsSize>
																					<StrSize classname='ExprValue'>
																						<value>1024</value>
																					</StrSize>
																					<ResultAct classname='Num' instanceoverrideflags='5177369'>
																						<value>0</value>
																					</ResultAct>
																					<ArgVal classname='ExprValue'>
																						<value>0</value>
																					</ArgVal>
																					<ArgDisplayVal classname='ExprValue'>
																						<value/>
																					</ArgDisplayVal>
																					<Flags classname='Num' instanceoverrideflags='5177369'>
																						<value>0</value>
																					</Flags>
																					<AdditionalResults classname='Obj'>
																						<subprops>
																							<Input classname='CommonCParameterResult'>
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
																							<Output classname='CommonCParameterResult'>
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
																					<ArgValImag classname='ExprValue'>
																						<value/>
																					</ArgValImag>
																				</subprops>
																			</FCParameter>
																		</value>
																		<value>
																			<FCParameter typename='FCParameter' xsi:type='FCParameter' name=''>
																				<subprops>
																					<Name classname='Str'>
																						<value>changeCount</value>
																					</Name>
																					<Type classname='Num'>
																						<value>0</value>
																					</Type>
																					<NumType classname='Num'>
																						<value>4</value>
																					</NumType>
																					<ObjType classname='Num'>
																						<value>0</value>
																					</ObjType>
																					<StructType classname='Str'>
																						<value/>
																					</StructType>
																					<NumPass classname='Num'>
																						<value>1</value>
																					</NumPass>
																					<StrPass classname='Num'>
																						<value>0</value>
																					</StrPass>
																					<ElemPass classname='Num'>
																						<value>0</value>
																					</ElemPass>
																					<ArrayDimensionsSize classname='Objs'>
																						<value lbound='[0]' ubound='[]'>
																							<elemproto>
																								<_NAME_IN_ATTRIBUTE_ name='' classname='ExprValue' structureflags='0'>
																									<value>1024</value>
																								</_NAME_IN_ATTRIBUTE_>
																							</elemproto>
																						</value>
																					</ArrayDimensionsSize>
																					<StrSize classname='ExprValue'>
																						<value>1024</value>
																					</StrSize>
																					<ResultAct classname='Num' instanceoverrideflags='5177369'>
																						<value>0</value>
																					</ResultAct>
																					<ArgVal classname='ExprValue'>
																						<value>RunState.InitialSelection.SelectedFile.ChangeCount</value>
																					</ArgVal>
																					<ArgDisplayVal classname='ExprValue'>
																						<value>RunState.InitialSelection.SelectedFile.ChangeCount</value>
																					</ArgDisplayVal>
																					<Flags classname='Num' instanceoverrideflags='5177369'>
																						<value>0</value>
																					</Flags>
																					<AdditionalResults classname='Obj'>
																						<subprops>
																							<Input classname='CommonCParameterResult'>
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
																							<Output classname='CommonCParameterResult'>
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
																					<ArgValImag classname='ExprValue'>
																						<value/>
																					</ArgValImag>
																				</subprops>
																			</FCParameter>
																		</value>
																	</value>
																</Parms>
															</subprops>
														</Call>
														<ModuleSrcPath classname='PathValue'>
															<value/>
														</ModuleSrcPath>
														<ModulePrjPath classname='PathValue'>
															<value/>
														</ModulePrjPath>
														<ModuleWorkspacePath classname='PathValue'>
															<value/>
														</ModuleWorkspacePath>
														<CodeTemplateName classname='Str'>
															<value/>
														</CodeTemplateName>
														<ModuleCreateSrcType classname='Num'>
															<value>0</value>
														</ModuleCreateSrcType>
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
																		<value>"Foo"</value>
																	</Name>
																	<ValueToLog classname='ExprValue'>
																		<value>12</value>
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
																		<value>false</value>
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
												<Error classname='Obj' instanceoverrideflags='4194304'>
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
												<ReportText classname='Str' flagsforinstances='0'>
													<value/>
												</ReportText>
												<Common classname='Obj' instanceoverrideflags='4194304'/>
											</subprops>
										</Result>
										<MenuName classname='ExprValue'>
											<value>ResStr("NI_WAIT_STEP_TYPE", "EDIT_STEP_MENU_NAME")</value>
										</MenuName>
										<SupportsReadOnly classname='Bool'>
											<value>true</value>
										</SupportsReadOnly>
										<HasEditPanel classname='Bool'>
											<value>true</value>
										</HasEditPanel>
									</subprops>
								</Step>
							</value>
						</value>
					</Substeps>
					<CodeTemplates classname='Str' valueflags='4194328' structureflags='524288'>
						<value>Default_Template</value>
					</CodeTemplates>
					<AdditionalResultsHints classname='Objs' valueflags='4194328' structureflags='524288'>
						<value lbound='[0]' ubound='[0]'>
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
							<value>
								<CustomResult typename='NI_CustomResult' xsi:type='NI_CustomResult' name=''>
									<subprops>
										<Name classname='ExprValue'>
											<value>ResStr("NI_WAIT_STEP_TYPE", "OPERATION")</value>
										</Name>
										<ValueToLog classname='ExprValue'>
											<value>ResStr("NI_WAIT_STEP_TYPE_TARGET_NAME", Str(Step.WaitForTarget))</value>
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
								</CustomResult>
							</value>
						</value>
					</AdditionalResultsHints>
					<TS typename='TEInf' xsi:type='TEInf' classname='Obj' flagsforinstances='262168' instanceoverrideflags='4456472'>
						<subprops>
							<Id classname='Str'>
								<value/>
							</Id>
							<Icon classname='Str'>
								<value>ni_hourglass.ico</value>
							</Icon>
							<SData typename='NoneStepAdditions' xsi:type='NoneStepAdditions' classname='NoneModule' flagsforinstances='2097152' instanceoverrideflags='7143448' structureflags='2097152'/>
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
								<value>2</value>
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
													<value>"Foo"</value>
												</Name>
												<ValueToLog classname='ExprValue'>
													<value>12</value>
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
													<value>false</value>
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
								<value lbound='[0]' ubound='[0]'>
									<value arrayindex='[0]'>NIStepTypeControls.dll|NationalInstruments.TestStand.StepTypeControls.WaitTabInfo</value>
								</value>
							</EditPanels>
						</subprops>
					</NI_Data>
					<Result classname='Obj' flagsforinstances='6291456' valueflags='4194304' structureflags='2097152'>
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
					<TimeoutEnabled classname='Bool'>
						<value>false</value>
					</TimeoutEnabled>
					<ErrorOnTimeout classname='Bool'>
						<value>true</value>
					</ErrorOnTimeout>
					<ThreadRefExpr typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ThreadRefExpr>
					<SeqCallName classname='Str'>
						<value/>
					</SeqCallName>
					<SeqCallStepGroupIdx classname='Num'>
						<value>0</value>
					</SeqCallStepGroupIdx>
					<TimeoutExpr typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</TimeoutExpr>
					<WaitForTarget classname='Num'>
						<value>0</value>
					</WaitForTarget>
					<TimeExpr typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</TimeExpr>
					<ExecutionRefExpr typename='Expression' xsi:type='Expression' classname='ExprValue'>
						<value/>
					</ExecutionRefExpr>
					<SpecifyBySeqCall classname='Bool'>
						<value>true</value>
					</SpecifyBySeqCall>
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
				</subprops>
			</NI_Wait>
		</typedef>
		<protected>E@=3BJiO100h]L]MGkcK3fBoaKgcnO1C[KY^3VgFg3&gt;\:dbWRb]WYj9]fEBBdNLc7&gt;=16bK:DD9ZS9kmc`7`;Q202^ND^J[e]L&lt;T3\0L@M0;FPga5obWXWOl&gt;^9&lt;lL_jcnWW:a&gt;MZ?4E;Lg^0MoVU]MW&lt;fcB0_&lt;LSOEOlk&gt;l5n^eKJk\_G_5C9H=B8D\&gt;F7]gm&gt;[iT_ooIIIfYO=L^O\EW&gt;2e6N`aY\gNMO9mS0IJ@ZCR4\WodAFQ^G7KQHTiL?KH9dR6IEG0nh?_S7SHFGF@h;B=W&gt;RD9oMFfjMom&gt;1nQc\dM7Bf5D`fSF_]kGQfobQQLhIR4cn\FEO\lXn=k8J9\lP5IEKO`?WOMLOOof\gPPo?P_CH&gt;OnPB@g:QcCcQg7okOlO[JY@fj?E_N?SVGSka7Y^7kib_NoedMWkNKOiOmg&lt;o&lt;7;&gt;ike:?N[B_Vl9;?acGg4_NLMmmMS7ngm3;G_7SCJnkTRIc9FGgdC\IWWogjaWTf7S_9LVPRQ&lt;F&gt;^B:H_=U``cbR=a[3M[gcf\mMa=KO`:=l7[n[fh\@cCNNX7AGh@A=EL2kGk`H7mjNQU3KYD5dAdR_KF&lt;6\jnS4SADDfOLn\g&gt;HJkaPMlgEI55k5cNO1_XPXHikJ;dXYCK6B?BmX_?kN&lt;??7CQEhde3iHOM&gt;XO]gCoY?7?iniKP]iOM&gt;&gt;^O6SYoXjZefZ`7ilbT?nk4SD&lt;D&gt;KJ7M^Lj^MEWOLA_noIb6]]A17&lt;9HFehEYOQjo=1BW:nHb&lt;T[[fhJX3j]Bok0U:CmH&lt;GncN95?efaPi`dmBM?3LXdLX=_3Y&gt;HjKf=PjVG:CY1`N8ghTi1:CgKR[NT5lgRF;:ii_g_nT2TAg5FJdbV4WJTbjT;c:KBW;ZfZNZ`n8YTZLS^3oJa;L4TbEO^IY2QZAo&lt;P99C@jafhG7f:8P2]HFhG@eY^]Qibi=:VLlI4;cV[OR9Pi4\jZ\BQiX@UC=idX1oUdSkS@U@J&gt;4J2AaW9eB^cNA0oOM5QZRYMn4f?dImTLGD]Yf0^cKUhn]E[X3&lt;\STRZ@L5&gt;SZdN5&gt;6E59M;ki&lt;^o:G^2gIa[;oMg\]MEhg3C@OHS1ZOUl09f&lt;&gt;STMW;;@DY^MKb3&lt;5]_T\djD1gTe5S\lE=D?C3gGVdnZg__IkO6WolkGdlho`ZS\k_6K_ool^2I2&lt;TMe8WX:dCHUiQPh6^]KCS?Z:5CAcWaTham8?C[[B`1?NTVNd&lt;?7_H=[9CEJO6cWE?T;cWGGiaHNmFC6566&lt;fMTCmo67e:X9cRJoMg01CkmhRC5Uc[3VPbW]O^dZgS[mK1d@jcj@mcMlNVJ&gt;5dHS9Yg\gCB2WQK18ESO9c;ZJBE4dQIFoaN]bBLJX8TORTcdQWMgE\M]0dGN&gt;V8P=2f0T;B?TaN5UaR3jd\d7[_fhY?jgkHD295o3?4@Majm`ZH]?VJK6T17UILTA8li;_F4;=W1&gt;dlI;j84;Zm:VN[0jG0\^`INAUL5AFfgGn&gt;aZ&gt;oa9?Y9aVWmK2T7=cBXHLAg2c:hELeWaJB\YHT;QAY_j&gt;7@3[7^n2cJZ1m\dFil145f?EYGFm6K7mdPcfFOZ4gk]6@aA:fICkCSYni_HQJPCeHE4c:G;[F&gt;RRP[CEbe&gt;X[YhOkmaBg5No;4Q:FXZFFcKH7ilTS3b;hGFFbX^Y@MO`0bPjSHC[;YfL[]&lt;Vc1C1BhRZF]ShjZI=:cYA1h;Po4WbiB:fZMV&lt;D@PJHe6:7:6C6e54=_4QH:XgMoERL[S:1GRLR84QW07W?Fbllo7g]HDj:GKE;j;EODh3ogEMCU3]cfah^m:mZ2M8W1&gt;nmA6lk`EBJ1L;&lt;Ki3U4ZALQJIW1UWCDN&lt;kc3P[_Bm^RKn_kM1CLF]e5KM;j[=S_DRT^XkRTWOZVI0j1mT]Mef0kLO8R&lt;I5DF737WCGBDPNUGV^XU03cB\E6TeKg[EBFXKSN]:f^6JFYYBb03dQ@5]fIaCEMHJj^:mf^PAhHoQJ:j=[UFiRK8]H3Qh8UQNYaJUFEk]Y;FE1IZbLO6V[I7c`hZ]Hi3URUd6d`jW[0cL[HBBY8dHY39Hdo2jA94ln0_1_[ebmaQ2NgI`[CHgQ]]Zh&lt;dQ]BbBCTOGT@`9mCcBb?iiOI7h&gt;QV?NA\Q=&lt;CcZ_4h28a_YR9CjRI5cRmAM:\ZNKk3aEX_RV_?oGUh;OXPnLDQ]FSYJdhFCkObUdE4Lln@AR7VndEXK4R@C`O2J&lt;fa]U`_=Ol[o:cn5FETf;R@a9f8S[bhc=O7&gt;lb0?&gt;Wk=9YA57DZ]T1`EIWn7noOK`in^0]_F1^de]=2PL^V`AQZObbZYaQLOX7^SQ^gHgcdNN=9gPPYgPa8?OnA8PPZXB8ma7\SOl0cafagHh?EAZD[bebcbP_:h41\E&lt;[?hK8C;BnK45YZTPV8iLSQH`[`&lt;Tn][Q2\eP3[JMV:PT:a@@5O3H03VLF1BDEWDc1=cNC&gt;T?SH1BVKl0`;CHX2EdF1:KC^ZVP4=DP4=4_OOHl`?&lt;jDBA3CTQXGLN@K5PK5CAdfWIMCCG]aZ4=&gt;kOkCHeLDKZKe&lt;A=cKoC4DfDHJ5ZWoB3WoiA2:GWoOHJ0kmQ:7Y=L^155fJ?JKGObM6=I489I\_9[MEkTfmj8dDS[F5Q8ML^gV9V_3OW6JH]=eF7C^i=@8^C8ehgVPi7T2&lt;&gt;SfW&gt;nL:VgL&lt;LJg=oHZaObbObm56Z`IGZ^ZmKade4ZDYgYV:cLJBHj&gt;kHEIg&lt;\7e3@a2iAa\LYD&lt;eF&lt;VQmDT8?OMhg0R2l]40aonj]LW`Hn&gt;V`]7hV]gOi9k35W&gt;S;3:^&gt;2UZH3DWKkX=57o;PgD8TPBEKYh`MGm&lt;2?33j?3OUOLL9X@0kRPBDKMTkUGVM[C&gt;4eL90fZcBFNH9lja;c?9iiJ2k1GYCSeInMB@C[L6cP_&lt;8=GdX:I6a;JBcTQPVYDM&lt;^YYbnbN:GZ2HTJ[\@]]g[OZSLI_fJ[[d4dZCW@aOVX?1[R\S53FPnKQo=jCBdiPC7:[71NcWCgIF6U^2AW\m[O59:oa?9N7?E7L\k;aD8n1MkKNB8:XdVDK?27iYYU6d&gt;HCdjhM73IB=CmIg&gt;;R7cVS&gt;aVkMF5U5i6A@o8c_C&lt;gOjS3ZB2CK\^7kJ_mf8Q@KRVEC;Uf2=\\&gt;7VJFolf^9BkAB0Qo4JRKj1M25iY&lt;a\lTR\&lt;&gt;9MchMOm04@PgFG8:F46U`G`=?`W[d[A7MJCUDl4b;n7cgb3PW]4dPeZ4c[bQ:DG8Q&lt;MI6PO:YM9_FBaRj&lt;af\0:Z@aeYE]G]&lt;497=GRd1;&gt;7]CaZ8&gt;Yjd^=IAj8YjRf]6FEjbaMN:m_]AkJL\21_HmSVjSh4RbMYOCg?DndN\D3[b4@mFW3H5SKc8dX0LH61KA91G:MCCVKE@W67f0bBc@Zon=mN5X?Z:4SH:&lt;_aLoOk5@Z`Q9a&gt;gFAk^`:8BAS;6DS&gt;6D`DgiOWb3RB]B`KKEP15ffgHeZ\&gt;XoTSA]A&gt;^@5=8Nc8a4f&gt;HbAVd0chhcBcc1&gt;KU0M1=&gt;QDW4b24T&lt;d2_EcATZ@N6h__3&lt;:h[==N51I&gt;0[1ZJ^cEA0em&gt;DFM4GLQ5Hd805;ahZ7WnEBbLX9j=EX4&lt;Ch06_Q9DlFN6nUe;a=d4OAl^7a&gt;:mDjPDN]Dc]PaZY]2ee2^cDklDG1HFg4HVG;H:K&gt;;k[9;e[MFd?DcYQOMoC:=3jLd9SCM6Dg?:OAc;ciGTFAUCY3=eKgGTb\]9R5=6a8VhUgF&lt;k[J:dR:nU]&lt;DKfR1DdG[j4D7oXoVFX7gfQn&lt;=n0_g5iF8_CdUFn`RU0@E7okbNeh9I4W&lt;AJ;DG4M&lt;;1cFoF\@F6_F`;_Y&lt;B7&gt;5K5mUfSe9j@V:g4mK5H&gt;WiQj&lt;LGa6]BdA:KYAE?ZV;Z`2JE[O;^49DoHX360`?jCUoNlV`XS@h@lmZN46[:PoKYH:nGCT5&lt;&gt;g5PeiK0M1SK65h&gt;D9EfHEKZRU]TANn[Ie&lt;9Sc?efGLS?AEN\i\i:GmS?=efLLS?eefLSg?]KYN3=TfZc@4`jImCZS1&lt;IUch1bk`:g28mT\Zci[;QkRj`0RPnH&lt;;_iSinc1XBgfRImTZO\k^ZQ:&lt;BMCFRH[B\;;2bhTSINkYX[;Ub[=F=?;\QBk\j9i5A2bUO1=_?^1l=2e5aaZ\L:\ZK&gt;YCMXfQFe;P3V`YF47FF\8CPJm&gt;UohN2Yj4YjFD^J?OJW;Km=X=9bnINoG&gt;MoKA`oMEgV_n]PFDon?N&gt;S:oO]N^M;=W[^:930C][6U?OcboOnBOg]5`5kQgClC3NGDjDWA:G&lt;5BhIE6UGM\XD;^b@\6N=WXZQ2nVji2T][A]k5kTHN@TMEIh\V8G5a&lt;mEAXI&gt;1NW\UK9DC5L@=k?0CV=hkDVk&gt;T6[;4LB7;oLAU`1Zl5@kGA6m0=VM2e:g8k_1Vn]O1]?TRa9IkjbHY15hgFJNMU;mYbaSfacPD6[&gt;M;DV]OX[MdN;_\66g5:oV`LUDN[HU[TU?oAGhKdVNFTJ25fkEh2Y^ZXNY;@Uek]8CTa\]Ycf547o2&lt;9aU794i2cb7c\D&gt;?mkFDIiZ?[7SPSNo;cc21hX4nmZHklN[nhW]?mPCim:?CE9:BnmVDe^cCC5BMiXfhS5M;239S9OH11kQ9cR5ckh70b;obLjY\KIZM^NW6c@7T:ZOWYBn&lt;l5@QfXgYU0:n?EBJiRKDc@XV[OU29n=i`HklOhF[nROcoR7?8DC4Z&lt;l4@4b07QIPS?0XSAAZa8&lt;`64R=@d`S=e2834GIiP:DP@RE\J8DI84jakHl`8@i_TJ7JPl@5ID8nYV300QSJ\@6X\&lt;8Pb53&lt;1;4R30ITRoDAC7SOn&lt;Q;nJQD00n&lt;e`mh0`X@@mFS0ND7hA0DhZPCh0i:EhMHj@M0U?8VXS3fAA&lt;;C&gt;&lt;3a7UPPnO&gt;&gt;5aN3QP00Lelf66KfSNf:@`S=1&gt;B652&lt;0@e&lt;60J4e59F&gt;S9[T1&gt;@jHoBS9M018SQ0IcQ\&lt;0GC689H2SlD3:E2R&lt;aA`j`Bb6SV6l05I==4dB&gt;7_2M`0@0^V02G]f:52eAHPJ80A18L;=R45Q3X6l0]a[TF`E9DYR6;Bak3WP`@D3KD:2ZHA`&lt;X6`&lt;DHg4Af0LSL9E4=2\KH0B=02;@l46:IR9n\`8l9YUD4;BO6@nD0&gt;5Ha12ASKV15&lt;IhK0K4&lt;A3Q:M@7`QkDkkMiU5LPh:1&lt;=d][G0P:H00_GDN9[c2gm:Dgcan8d`_kOIDWaM3lPA7kjNnKO_9:gnU&lt;W[:E5S@k6C\B_:1@PS4N^i_:2QJW4eWa8;@4bbZg@&lt;]9NfYHWPARQFkXF0l^b;YW=L]0]H6WIRdaQT\eB\V[BKC@9WFBJUHAZc;XE9WCeb2VEG&lt;U6GFS[QeA49JE&gt;TF=jTJ1n@3RYB0ROBE?91PcP]1CP[NL_X`BNge;hD[nRF&gt;f?aF6JI;^kA:jaaSF&lt;:Gd6U][YdK9&lt;Fji;jeD5]kFRmh;LQW=3C3DEG]9@]U^aNLRM[DT9&lt;ec44US;g&lt;`m@WmED3TM2ji68RS?PD6Z0B6JSQTa:9JS4VX_&lt;\B6XJY&lt;Ba6XYX&lt;BM9;S463m@nic0_7nEeXF8GmQGonYn4eRENlN;JH31;LP4PP\N1G@OV&gt;:IWJ5277[cQf&gt;KBEN;MgW=&lt;fo^i=_Kii&lt;:mJKAA`_W6O1cJH&gt;?ObVbdYJGd0@E&gt;X&gt;G9VEg9&gt;0&lt;FcJXXNjDdABZN8jKjG;lEP[26P7=2NJSO058P0H]3F6H`aT4S&lt;QhI53k01Q_A`dD80jP:HG=b6Nkm`P:C`D&lt;QFi3HPI25WCZFTF@F_ol@V:E8Xb6EJZE5l=jBMAhh&gt;BF1:6j&lt;jMKdQNP]m8^6a:&gt;m[b\U79Of3N&gt;?0k9Cglkg=Kigb[J_5Q^Wg;:HiIh?\Ynm3_cFYaog=h&gt;nB\Xao2kJe7h</protected>
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
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='28'>
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
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='27'>
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
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='26'>
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
									<value lbound='[0]' ubound='[2]'>
										<value>
											<Step typename='NI_Measurement' xsi:type='NI_Measurement' name='Close relays using an NI relay driver'>
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
																<value>ni.examples.NISwitchControlRelays_Python</value>
															</Name>
															<Parameters classname='Objs'>
																<value lbound='[0]' ubound='[1]'>
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
																					<value>relay_names</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>"SiteRelay1"</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>false</value>
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
																					<value>close_relay</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>True</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>false</value>
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
																</value>
															</Parameters>
														</subprops>
													</Measurement>
												</subprops>
											</Step>
										</value>
										<value>
											<Step typename='NI_Wait' xsi:type='NI_Wait' name='Wait 5 seconds'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:Y5gFOYZ27RGuNtVZ8EufkC</value>
															</Id>
															<Icon classname='Str'>
																<value>ni_hourglass.ico</value>
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
																<value>2</value>
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
																					<value>"Foo"</value>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value>12</value>
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
																					<value>false</value>
																				</IsAnyType>
																			</subprops>
																		</_NAME_IN_ATTRIBUTE_>
																	</elemproto>
																</value>
															</CustomResults>
															<AdditionalResultsHints classname='Objs'>
																<value lbound='[0]' ubound='[0]'>
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
																	<value>
																		<CustomResult typename='NI_CustomResult' xsi:type='NI_CustomResult' name=''>
																			<subprops>
																				<Name classname='ExprValue'>
																					<value>ResStr("NI_WAIT_STEP_TYPE", "TIME_TO_WAIT")</value>
																				</Name>
																				<ValueToLog classname='ExprValue'>
																					<value>Evaluate(Step.TimeExpr)</value>
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
																		</CustomResult>
																	</value>
																</value>
															</AdditionalResultsHints>
														</subprops>
													</TS>
													<TimeoutEnabled classname='Bool'>
														<value>false</value>
													</TimeoutEnabled>
													<ErrorOnTimeout classname='Bool'>
														<value>true</value>
													</ErrorOnTimeout>
													<ThreadRefExpr classname='ExprValue'>
														<value/>
													</ThreadRefExpr>
													<SeqCallName classname='Str'>
														<value/>
													</SeqCallName>
													<SeqCallStepGroupIdx classname='Num'>
														<value>0</value>
													</SeqCallStepGroupIdx>
													<TimeoutExpr classname='ExprValue'>
														<value/>
													</TimeoutExpr>
													<WaitForTarget classname='Num'>
														<value>0</value>
													</WaitForTarget>
													<TimeExpr classname='ExprValue'>
														<value>5</value>
													</TimeExpr>
													<ExecutionRefExpr classname='ExprValue'>
														<value/>
													</ExecutionRefExpr>
													<SpecifyBySeqCall classname='Bool'>
														<value>true</value>
													</SpecifyBySeqCall>
												</subprops>
											</Step>
										</value>
										<value>
											<Step typename='NI_Measurement' xsi:type='NI_Measurement' name='Open relays using an NI relay driver'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:DdLjW4Z27RGuNtVZ8EufkC</value>
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
																<value>ni.examples.NISwitchControlRelays_Python</value>
															</Name>
															<Parameters classname='Objs'>
																<value lbound='[0]' ubound='[1]'>
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
																					<value>relay_names</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>"SiteRelay1"</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>false</value>
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
																					<value>close_relay</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>False</value>
																				</ArgumentValue>
																				<Direction classname='Str'>
																					<value>In</value>
																				</Direction>
																				<Log classname='Bool'>
																					<value>false</value>
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
																<value>ID#:ox+fdtuU7hGhxGDjK76h1B</value>
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
														<value>"NISwitchControlRelays.pinmap"</value>
													</PinMapPath>
												</subprops>
											</Step>
										</value>
										<value>
											<Step typename='Action' xsi:type='Action' name='Create and register NI-Switch Sessions'>
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
																				<value>3</value>
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
																				<value>teststand_niswitch.py</value>
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
																				<value>create_niswitch_sessions</value>
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
											<Step typename='Action' xsi:type='Action' name='Destroy and unregister NI-Switch sessions'>
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
																				<value>3</value>
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
																				<value>teststand_niswitch.py</value>
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
																				<value>destroy_niswitch_sessions</value>
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

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niswitch_control_relays/poetry.toml sha256=ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e bytes=34 -->
## FILE: examples/niswitch_control_relays/poetry.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niswitch_control_relays/poetry.toml`
- sha256: `ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e`
- bytes: 34

````toml
[virtualenvs]
in-project = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niswitch_control_relays/pyproject.toml sha256=75468ddbb17dba37377d9c7f711c5e0b2ea39bcf62b87884584e1a2680fa598d bytes=1120 -->
## FILE: examples/niswitch_control_relays/pyproject.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niswitch_control_relays/pyproject.toml`
- sha256: `75468ddbb17dba37377d9c7f711c5e0b2ea39bcf62b87884584e1a2680fa598d`
- bytes: 1120

````toml
[tool.poetry]
name = "niswitch_control_relays"
version = "0.5.0"
package-mode = false
description = "Measurement plug-in example that controls relays using an NI relay driver (e.g. PXI-2567)."
authors = ["National Instruments"]

[tool.poetry.dependencies]
python = "^3.10"
niswitch = { version = ">=1.4.4", extras = ["grpc"] }
ni-measurement-plugin-sdk-service = {version = ">=2.3.1,<4.0"}
click = ">=7.1.2, !=8.1.4" # mypy fails with click 8.1.4: https://github.com/pallets/click/issues/2558
grpcio = "*"

[tool.poetry.group.dev.dependencies]
ni-python-styleguide = ">=0.4.1"
mypy = ">=1.0"
types-grpcio = ">=1.0"
# Uncomment to use prerelease dependencies.
# niswitch = { git = "https://github.com/ni/nimi-python.git", subdirectory = "generated/niswitch", extras = ["grpc"] }
# ni-measurement-plugin-sdk-service = {path = "../../packages/service", develop = true}

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.mypy]
disallow_untyped_defs = true

[[tool.mypy.overrides]]
module = [
    "niswitch.*",
]
ignore_missing_imports = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niswitch_control_relays/README.md sha256=dd2dacd2a8d0d52b064ff43da03eaa3979627d62be7e334b4f86d478c8eeb173 bytes=2012 -->
## FILE: examples/niswitch_control_relays/README.md

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niswitch_control_relays/README.md`
- sha256: `dd2dacd2a8d0d52b064ff43da03eaa3979627d62be7e334b4f86d478c8eeb173`
- bytes: 2012

````markdown
## NI-Switch Control Relays

This is a measurement plug-in example that controls relays using an NI relay driver
(e.g. PXI-2567).

### Features

- Uses the `niswitch` package to access NI-SWITCH from Python
- Pin-aware, supporting multiple sessions, multiple pins, and multiple selected
  sites
  - Performs the same operation (open/close relay) on all selected pin/site
    combinations
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
- NI-SWITCH
- Recommended: TestStand 2021 SP1 or later

### Required Hardware

This example requires an NI relay driver (e.g. PXI-2567).

By default, this example uses a physical instrument or a simulated instrument
created in NI MAX. To automatically simulate an instrument without using NI MAX,
follow the steps below:
- Create a `.env` file in the measurement service's directory or one of its
  parent directories (such as the root of your Git repository or
  `C:\ProgramData\National Instruments\Plug-Ins\Measurements` for statically
  registered measurement services).
- Add the following options to the `.env` file to enable simulation via the
  driver's `simulate` and `topology` parameters:

  ```
  MEASUREMENT_PLUGIN_NISWITCH_SIMULATE=1
  MEASUREMENT_PLUGIN_NISWITCH_TOPOLOGY=2567/Independent
  ```
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niswitch_control_relays/start.bat sha256=bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851 bytes=253 -->
## FILE: examples/niswitch_control_relays/start.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niswitch_control_relays/start.bat`
- sha256: `bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851`
- bytes: 253

````batch
@echo off
REM The discovery service uses this script to start the measurement service.
REM You can customize this script for your Python setup. The -v option logs
REM messages with level INFO and above.

.venv\Scripts\python.exe measurement.py -v
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/niswitch_control_relays/teststand_niswitch.py sha256=5fd65a15b479e1d99d22c3a40d03247a908dfd3283f030c42905ae1751379a0f bytes=4902 -->
## FILE: examples/niswitch_control_relays/teststand_niswitch.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/niswitch_control_relays/teststand_niswitch.py`
- sha256: `5fd65a15b479e1d99d22c3a40d03247a908dfd3283f030c42905ae1751379a0f`
- bytes: 4902

````python
"""Functions to set up and tear down sessions of NI-Switch devices in NI TestStand."""

from typing import Any

from _helpers import TestStandSupport
from ni_measurement_plugin_sdk_service.discovery import DiscoveryClient
from ni_measurement_plugin_sdk_service.grpc.channelpool import GrpcChannelPool
from ni_measurement_plugin_sdk_service.session_management import (
    INSTRUMENT_TYPE_NI_RELAY_DRIVER,
    PinMapContext,
    SessionInitializationBehavior,
    SessionManagementClient,
)


def create_niswitch_sessions(sequence_context: Any) -> None:
    """Create and register all NI-Switch sessions.

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
            instrument_type_id=INSTRUMENT_TYPE_NI_RELAY_DRIVER,
        ) as reservation:
            with reservation.initialize_niswitch_sessions(
                initialization_behavior=SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH
            ):
                pass

            session_management_client.register_sessions(reservation.session_info)


def destroy_niswitch_sessions() -> None:
    """Destroy and unregister all NI-Switch sessions."""
    with GrpcChannelPool() as grpc_channel_pool:
        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with session_management_client.reserve_all_registered_sessions(
            instrument_type_id=INSTRUMENT_TYPE_NI_RELAY_DRIVER,
        ) as reservation:
            if not reservation.session_info:
                return

            session_management_client.unregister_sessions(reservation.session_info)

            with reservation.initialize_niswitch_sessions(
                initialization_behavior=SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE
            ):
                pass


def create_niswitch_multiplexer_sessions(sequence_context: Any) -> None:
    """Create and register all NI-SWITCH multiplexer sessions.

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
        with session_management_client.get_multiplexer_sessions(
            pin_map_context
        ) as session_container:
            with session_container.initialize_niswitch_multiplexer_sessions(
                initialization_behavior=SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH
            ):
                pass

            session_management_client.register_multiplexer_sessions(
                session_container.multiplexer_session_info
            )


def destroy_niswitch_multiplexer_sessions() -> None:
    """Destroy and unregister all NI-SWITCH multiplexer sessions."""
    with GrpcChannelPool() as grpc_channel_pool:
        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with session_management_client.get_all_registered_multiplexer_sessions() as session_container:
            if not session_container.multiplexer_session_info:
                return

            session_management_client.unregister_multiplexer_sessions(
                session_container.multiplexer_session_info
            )
            with session_container.initialize_niswitch_multiplexer_sessions(
                initialization_behavior=SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE
            ):
                pass
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/.serviceignore sha256=997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912 bytes=148 -->
## FILE: examples/nivisa_dmm_measurement/.serviceignore

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/.serviceignore`
- sha256: `997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912`
- bytes: 148

````text
# This file specifies that when we publish this plug-in to a plug-in library,
# we should not copy the following directories:
.venv
__pycache__
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/_helpers.py sha256=0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426 bytes=2920 -->
## FILE: examples/nivisa_dmm_measurement/_helpers.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/_helpers.py`
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

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/_visa_dmm.py sha256=c65dd70dc2df5495836ef3f7ce9f83063a6ed98869fbccb082c76cedd183f330 bytes=4565 -->
## FILE: examples/nivisa_dmm_measurement/_visa_dmm.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/_visa_dmm.py`
- sha256: `c65dd70dc2df5495836ef3f7ce9f83063a6ed98869fbccb082c76cedd183f330`
- bytes: 4565

````python
"""Custom instrument driver for measurement plug-in NI-VISA DMM examples."""

from __future__ import annotations

import pathlib
import sys
from enum import Enum
from types import TracebackType
from typing import TYPE_CHECKING

import pyvisa
import pyvisa.resources
import pyvisa.typing

if TYPE_CHECKING:
    if sys.version_info >= (3, 11):
        from typing import Self
    else:
        from typing_extensions import Self


# Pin map instrument type constant for VISA DMM
INSTRUMENT_TYPE_VISA_DMM = "VisaDmm"

_SIMULATION_YAML_PATH = pathlib.Path(__file__).resolve().parent / "_visa_dmm_sim.yaml"

_RESOLUTION_DIGITS_TO_VALUE = {"3.5": 0.001, "4.5": 0.0001, "5.5": 1e-5, "6.5": 1e-6}

# Supported NI-VISA DMM instrument IDs, both real and simulated, can be added here
_SUPPORTED_INSTRUMENT_IDS = [
    # Keysight/Agilent/HP 34401A
    "34401",
    "34410",
    "34411",
    "L4411",
    # NI Instrument Simulator v2.0
    "Instrument Simulator",  # single instrument
    "Waveform Generator Simulator",  # multi-instrument
]


class Function(Enum):
    """Enum that represents the measurement function."""

    DC_VOLTS = 0
    AC_VOLTS = 1


_FUNCTION_TO_VALUE = {
    Function.DC_VOLTS: "VOLT:DC",
    Function.AC_VOLTS: "VOLT:AC",
}


class Session:
    """An NI-VISA DMM session."""

    def __init__(
        self,
        resource_name: str,
        id_query: bool = True,
        reset_device: bool = True,
        simulate: bool = False,
    ) -> None:
        """Open NI-VISA DMM session."""
        # Create a real or simulated VISA resource manager."""
        visa_library = f"{_SIMULATION_YAML_PATH}@sim" if simulate else ""
        resource_manager = pyvisa.ResourceManager(visa_library)

        session = resource_manager.open_resource(
            resource_name, read_termination="\n", write_termination="\n"
        )

        if not isinstance(session, pyvisa.resources.MessageBasedResource):
            raise TypeError("The 'session' object must be an instance of MessageBasedResource.")
        self._session = session

        if id_query:
            self._validate_id()

        if reset_device:
            self._reset()

    def close(self) -> None:
        """Close the session."""
        self._session.close()

    def __enter__(self) -> Self:
        """Context management protocol. Returns self."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Context management protocol. Calls close()."""
        self.close()

    def configure_measurement_digits(
        self, function: Function, range: float, resolution_digits: float
    ) -> None:
        """Configure the common properties of the measurement.

        These properties include function, range, and resolution_digits.
        """
        function_enum = _FUNCTION_TO_VALUE[function]
        resolution_value = _RESOLUTION_DIGITS_TO_VALUE[str(resolution_digits)]

        self._session.write("CONF:%s %.g,%.g" % (function_enum, range, resolution_value))
        self._check_error()

    def read(self) -> float:
        """Acquires a single measurement and returns the measured value."""
        response = self._session.query("READ?")
        self._check_error()
        return float(response)

    def _check_error(self) -> None:
        """Query the instrument's error queue."""
        response = self._session.query("SYST:ERR?")
        fields = response.split(",", maxsplit=1)
        assert len(fields) >= 1
        if int(fields[0]) != 0:
            raise RuntimeError("Instrument returned error %s: %s" % (fields[0], fields[1]))

    def _validate_id(self) -> None:
        """Check the selected instrument is proper and responding.."""
        instrument_id = self._session.query("*IDN?")
        if not any(id_check in instrument_id for id_check in _SUPPORTED_INSTRUMENT_IDS):
            raise RuntimeError(
                "The ID query failed. This may mean that you selected the wrong instrument, your instrument did not respond, "
                f"or you are using a model that is not officially supported by this driver. Instrument ID: {instrument_id}"
            )

    def _reset(self) -> None:
        """Reset the instrument to a known state."""
        self._session.write("*CLS")
        self._session.write("*RST")
        self._check_error()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/_visa_dmm_session_management.py sha256=ec1aa1a0325668c7c615bae639212a22eed91dafdde1e68d2ba075dca81c9860 bytes=2618 -->
## FILE: examples/nivisa_dmm_measurement/_visa_dmm_session_management.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/_visa_dmm_session_management.py`
- sha256: `ec1aa1a0325668c7c615bae639212a22eed91dafdde1e68d2ba075dca81c9860`
- bytes: 2618

````python
import logging

from _visa_dmm import Session
from _visa_grpc import build_visa_grpc_resource_string, get_visa_grpc_insecure_address
from decouple import AutoConfig
from ni_measurement_plugin_sdk_service.discovery import DiscoveryClient
from ni_measurement_plugin_sdk_service.session_management import (
    SessionInformation,
    SessionInitializationBehavior,
)

_logger = logging.getLogger(__name__)


class VisaDmmSessionConstructor:
    """Measurement plug-in constructor for VISA DMM sessions."""

    def __init__(
        self,
        config: AutoConfig,
        discovery_client: DiscoveryClient,
        initialization_behavior: SessionInitializationBehavior = SessionInitializationBehavior.AUTO,
    ) -> None:
        """Construct a VisaDmmSessionConstructor."""
        self._config = config
        self._discovery_client = discovery_client
        self._initialization_behavior = initialization_behavior

        # Hack: config is a parameter for now so TestStand code modules use the right config path.
        self._visa_dmm_simulate: bool = config(
            "MEASUREMENT_PLUGIN_VISA_DMM_SIMULATE", default=False, cast=bool
        )

        if self._visa_dmm_simulate:
            # _visa_dmm_sim.yaml doesn't include the grpc:// resource names.
            _logger.debug("Not using NI gRPC Device Server due to simulation")
            self._address = ""
        else:
            self._address = get_visa_grpc_insecure_address(config, discovery_client)
            if self._address:
                _logger.debug("NI gRPC Device Server address: http://%s", self._address)
            else:
                _logger.debug("Not using NI gRPC Device Server")

    def __call__(self, session_info: SessionInformation) -> Session:
        """Construct a VISA DMM session based on measurement plug-in info."""
        resource_name = session_info.resource_name
        if self._address:
            resource_name = build_visa_grpc_resource_string(
                resource_name,
                self._address,
                session_info.session_name,
                self._initialization_behavior,
            )

        # When this measurement is called from outside of TestStand (session_exists
        # == False), reset the instrument to a known state. In TestStand,
        # ProcessSetup resets the instrument.
        reset_device = not session_info.session_exists

        _logger.debug("VISA resource name: %s", resource_name)
        return Session(resource_name, reset_device=reset_device, simulate=self._visa_dmm_simulate)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/_visa_dmm_sim.yaml sha256=42b0613184bcabf53401a702437d3a387d1b6d7c9fbf37b53a9cf74b837fe480 bytes=743 -->
## FILE: examples/nivisa_dmm_measurement/_visa_dmm_sim.yaml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/_visa_dmm_sim.yaml`
- sha256: `42b0613184bcabf53401a702437d3a387d1b6d7c9fbf37b53a9cf74b837fe480`
- bytes: 743

````yaml
spec: "1.1"
devices:
  VisaDmm:
    eom:
      GPIB INSTR:
        q: "\n"
        r: "\n"
    dialogues:
      - q: "*CLS"
      - q: "*IDN?"
        r: "National Instruments,Waveform Generator Simulator (simulated with pyvisa-sim),00000000,2.0.1"
      - q: "*RST"
      - q: "READ?"
        r: "1.23456"
    error:
      error_queue:
        - q: 'SYST:ERR?'
          default: '0,No Error'
          command_error: '-100,Command Error'
          query_error: '-400,Query Error'
    properties:
      configuration:
        default: "VOLT:DC 5.000000,0.001000"
        getter:
          q: "CONF?"
          r: "{:s}"
        setter:
          q: "CONF:{:s}"

resources:
  GPIB0::3::INSTR:
    device: VisaDmm
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/_visa_grpc.py sha256=c6f8dd68dbe9a27fb3ad8dc56d72335a5f798977dbfccf8f29452fca96e3449b bytes=2100 -->
## FILE: examples/nivisa_dmm_measurement/_visa_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/_visa_grpc.py`
- sha256: `c6f8dd68dbe9a27fb3ad8dc56d72335a5f798977dbfccf8f29452fca96e3449b`
- bytes: 2100

````python
from urllib.parse import urlencode, urlsplit

from decouple import AutoConfig
from ni_measurement_plugin_sdk_service.discovery import DiscoveryClient
from ni_measurement_plugin_sdk_service.session_management import SessionInitializationBehavior

_INITIALIZATION_BEHAVIOR = {
    SessionInitializationBehavior.AUTO: 0,
    SessionInitializationBehavior.INITIALIZE_SERVER_SESSION: 1,
    SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION: 2,
    SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH: 3,
    SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE: 4,
}

GRPC_SERVICE_INTERFACE_NAME = "visa_grpc.Visa"
SERVICE_CLASS = "ni.measurementlink.v1.grpcdeviceserver"


def build_visa_grpc_resource_string(
    resource_name: str,
    address: str,
    session_name: str = "",
    initialization_behavior: SessionInitializationBehavior = SessionInitializationBehavior.AUTO,
) -> str:
    """Build an grpc:// resource string for remoting with NI-VISA."""
    query = {
        "init_behavior": _INITIALIZATION_BEHAVIOR[initialization_behavior],
        "session_name": session_name,
    }
    return f"grpc://{address}/{resource_name}?" + urlencode(query)


def get_visa_grpc_insecure_address(config: AutoConfig, discovery_client: DiscoveryClient) -> str:
    """Get the insecure address of NI gRPC Device Server's VISA interface in host:port format."""
    # Hack: config is a parameter for now so TestStand code modules use the right config path.
    use_grpc_device_server: bool = config(
        "MEASUREMENT_PLUGIN_USE_GRPC_DEVICE_SERVER", default=True, cast=bool
    )
    grpc_device_server_address: str = config(
        "MEASUREMENT_PLUGIN_GRPC_DEVICE_SERVER_ADDRESS", default=""
    )

    if not use_grpc_device_server:
        return ""

    if grpc_device_server_address:
        return urlsplit(grpc_device_server_address).netloc
    else:
        service_location = discovery_client.resolve_service(
            GRPC_SERVICE_INTERFACE_NAME, SERVICE_CLASS
        )
        return service_location.insecure_address
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/install.bat sha256=695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025 bytes=205 -->
## FILE: examples/nivisa_dmm_measurement/install.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/install.bat`
- sha256: `695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025`
- bytes: 205

````batch
@echo off
REM The discovery service uses this script to install the dependencies
REM for the measurement service. You can customize this script for your
REM Python setup.

poetry install --only main
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/measurement.py sha256=97456a0c88a17a603f397ddb51c2833e2151439a1fc521efecb8c4274eb9ecab bytes=2810 -->
## FILE: examples/nivisa_dmm_measurement/measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/measurement.py`
- sha256: `97456a0c88a17a603f397ddb51c2833e2151439a1fc521efecb8c4274eb9ecab`
- bytes: 2810

````python
"""Perform a DMM measurement using NI-VISA and an NI Instrument Simulator v2.0."""

import logging
import pathlib
import sys

import click
import ni_measurement_plugin_sdk_service as nims
from _helpers import configure_logging, verbosity_option
from _visa_dmm import INSTRUMENT_TYPE_VISA_DMM, Function
from _visa_dmm_session_management import VisaDmmSessionConstructor
from decouple import AutoConfig

script_or_exe = sys.executable if getattr(sys, "frozen", False) else __file__
service_directory = pathlib.Path(script_or_exe).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "NIVisaDmmMeasurement.serviceconfig",
    ui_file_paths=[service_directory / "NIVisaDmmMeasurement.measui"],
)

# Search for the `.env` file starting with the current directory.
_config = AutoConfig(str(pathlib.Path.cwd()))


@measurement_service.register_measurement
@measurement_service.configuration(
    "pin_name", nims.DataType.IOResource, "Pin1", instrument_type=INSTRUMENT_TYPE_VISA_DMM
)
@measurement_service.configuration(
    "measurement_type", nims.DataType.Enum, Function.DC_VOLTS, enum_type=Function
)
@measurement_service.configuration("range", nims.DataType.Double, 1.0)
@measurement_service.configuration("resolution_digits", nims.DataType.Double, 3.5)
@measurement_service.output("measured_value", nims.DataType.Double)
def measure(
    pin_name: str,
    measurement_type: Function,
    range: float,
    resolution_digits: float,
) -> tuple[float]:
    """Perform a DMM measurement using NI-VISA and an NI Instrument Simulator v2.0."""
    logging.info(
        "Starting measurement: pin_name=%s measurement_type=%s range=%g resolution_digits=%g",
        pin_name,
        measurement_type,
        range,
        resolution_digits,
    )

    session_constructor = VisaDmmSessionConstructor(_config, measurement_service.discovery_client)

    with measurement_service.context.reserve_session(pin_name) as reservation:
        with reservation.initialize_session(
            session_constructor, INSTRUMENT_TYPE_VISA_DMM
        ) as session_info:
            session = session_info.session
            session.configure_measurement_digits(measurement_type, range, resolution_digits)
            measured_value = session.read()

    logging.info("Completed measurement: measured_value=%g", measured_value)
    return (measured_value,)


@click.command
@verbosity_option
def main(verbosity: int) -> None:
    """Perform a DMM measurement using NI-VISA and an NI Instrument Simulator v2.0."""
    configure_logging(verbosity)

    with measurement_service.host_service():
        input("Press enter to close the measurement service.\n")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/NIVisaDmmMeasurement.instudioproj sha256=3ee67856cf6b100764022fbca4fc009b74639119c39af32f758010bf7931ee7b bytes=2031 -->
## FILE: examples/nivisa_dmm_measurement/NIVisaDmmMeasurement.instudioproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/NIVisaDmmMeasurement.instudioproj`
- sha256: `3ee67856cf6b100764022fbca4fc009b74639119c39af32f758010bf7931ee7b`
- bytes: 2031

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="018457C032D712874D688A0EC6F9169F3DA413F1F69C8C9ACD311BC2858926C03CE4FA831BD6775206CA64BF02655629349142D1DCA70C3C400A8B32C4B1FF73" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.0.0.49209" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49209" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.49209" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="23.0.0.49209" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="f53d543da7be447d977505512a9de1b1" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="7a73cec96722445aaeae940b880f627c" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="f0fd0a1d98c944258fd0797c80775378" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Bindings="EnvoyManager" Id="48290a0c581843548d2eaeb7c3a50ff8" ModelDefinitionType="NationalInstruments.InstrumentFramework.Document.SourceModel.UnifiedTask" Name="NIVisaDmmMeasurement.sfp" StoragePath="NIVisaDmmMeasurement.sfp" />
			<FileReference Id="7be6ee99c4eb4151a21d94166b6d4b4a" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="NIVisaDmmMeasurement.pinmap" StoragePath="NIVisaDmmMeasurement.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/NIVisaDmmMeasurement.measproj sha256=a4f5056d70931c8c20a68fcf2596e1f100b536b99d93b2678ef75ebb7727b038 bytes=3824 -->
## FILE: examples/nivisa_dmm_measurement/NIVisaDmmMeasurement.measproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/NIVisaDmmMeasurement.measproj`
- sha256: `a4f5056d70931c8c20a68fcf2596e1f100b536b99d93b2678ef75ebb7727b038`
- bytes: 3824

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="E6875FA9612A2308B842160B9B265538A4301B12DE21889AAE3B27439BDF164A4BAFF8C464E1255C4FF9B969A12330FF3BCB7E0DDC4C8FC54B4F91A34A560688" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.0.0.49209" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="23.0.0.49209" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49209" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49209" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/EnvoyManagement" OldestCompatibleVersion="5.0.0.0" Version="5.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49209" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemDiagram" OldestCompatibleVersion="8.0.0.49152" Version="8.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49209" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemModelCore" OldestCompatibleVersion="5.1.0.5" Version="5.2.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.49209" Name="MeasurementLink UI Editor" Version="23.0.0.49209" />
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
			<FileReference Id="bc6ee95bbfeb42cc992bf0708b654bbe" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="NIVisaDmmMeasurement.pinmap" StoragePath="NIVisaDmmMeasurement.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
			<SourceFileReference Id="d5e4bd3e8510459ea77718b72b2e520a" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="NIVisaDmmMeasurement.measui" StoragePath="NIVisaDmmMeasurement.measui" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/NIVisaDmmMeasurement.measui sha256=e2351d939c867874e7baacf6f2bba737ba1d70e8a8bddb5a7b8240074e5a5100 bytes=7026 -->
## FILE: examples/nivisa_dmm_measurement/NIVisaDmmMeasurement.measui

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/NIVisaDmmMeasurement.measui`
- sha256: `e2351d939c867874e7baacf6f2bba737ba1d70e8a8bddb5a7b8240074e5a5100`
- bytes: 7026

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="0690AFACC21E8251ECA0B4F0B977D42734ED495FD12F73064D83AD9E676D56C31D17A228F760A2A08C0DEBF68392B80BB944ADD54BFD055109D887ED886CB6D4" Timestamp="1D9F0B5598D3E01" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.9.0.50025" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="9.8.1.49152" />
		<ParsableNamespace AssemblyFileVersion="9.9.0.50025" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="23.5.0.50025" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.9.0.50025" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.9.0.50025" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.5.0.50026" Name="MeasurementLink UI Editor" Version="23.5.0.50026" />
	</SourceModelFeatureSet>
	<Screen ClientId="{26c56ad8-e31a-456d-979e-87865b3f5c61}" DisplayName="NI-VISA DMM Measurement (Py)" Id="f4480b18b95d49bfbefdf2b9d4958707" ServiceClass="ni.examples.NIVisaDmmMeasurement_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
		<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]310" Id="d5c4d136f87c4189a41619217b0d4f32" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]450" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
			<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BaseName="[string]Canvas" Height="[float]143" Id="299e88201b64436290271ab48c3f88c1" Label="[UIModel]8a81dfd7bc5c46228026d1c21aa98288" Left="[float]23" Top="[float]140" Width="[float]150">
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{26c56ad8-e31a-456d-979e-87865b3f5c61}/Configuration/range" Enabled="[bool]True" Height="[float]24" Id="3425530122134004b914e5caafe7fa5c" IsLabelBoundToChannel="[bool]False" Label="[UIModel]c24c5007263c45aaab35919b80ade906" Left="[float]15" RadixBase="[RadixBase]0" RadixVisibility="[SMVisibility]Collapsed" TabIndex="[int]0" Top="[float]36" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=SystemInternational:Digits=2:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
				<Label Height="[float]16" Id="c24c5007263c45aaab35919b80ade906" LabelOwner="[UIModel]3425530122134004b914e5caafe7fa5c" Left="[float]15" Text="[string]Range" Top="[float]16" Width="[float]33" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{26c56ad8-e31a-456d-979e-87865b3f5c61}/Configuration/resolution_digits" Enabled="[bool]True" Height="[float]24" Id="f00e4a6e2da64780a841bd86ebbe1932" IsLabelBoundToChannel="[bool]False" Label="[UIModel]6110b26a8afe4a14b3e3be3bee9d797e" Left="[float]16" TabIndex="[int]1" Top="[float]93" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]70" />
				<Label Height="[float]16" Id="6110b26a8afe4a14b3e3be3bee9d797e" LabelOwner="[UIModel]f00e4a6e2da64780a841bd86ebbe1932" Left="[float]16" Text="[string]Resolution (digits)" Top="[float]73" Width="[float]95" xmlns="http://www.ni.com/PanelCommon" />
			</ScreenSurfaceCanvas>
			<Label Height="[float]16" Id="8a81dfd7bc5c46228026d1c21aa98288" LabelOwner="[UIModel]299e88201b64436290271ab48c3f88c1" Left="[float]23" Text="[string]Configuration" Top="[float]120" Width="[float]73" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{26c56ad8-e31a-456d-979e-87865b3f5c61}/Output/measured_value" Height="[float]51" Id="b8c14ae283ec4bf8ad8a037705e08afc" IsLabelBoundToChannel="[bool]False" IsReadOnly="[bool]True" Label="[UIModel]71a08f4917d143caa1a9edb08cfff3c8" Left="[float]195" MinHeight="[float]51" TabIndex="[int]0" Top="[float]30" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=7:DigitDisplayType=SignificantDigits:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]230">
				<FontSetting FontFamily="Segoe UI" FontSize="24" Id="142973a4882412f8a4bf0df63295bf1" xmlns="http://www.ni.com/PlatformFramework" />
			</ChannelNumericText>
			<Label Height="[float]16" Id="71a08f4917d143caa1a9edb08cfff3c8" LabelOwner="[UIModel]b8c14ae283ec4bf8ad8a037705e08afc" Left="[float]195" Text="[string]Measured value" Top="[float]10" Width="[float]84" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{26c56ad8-e31a-456d-979e-87865b3f5c61}/Configuration/pin_name" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="f7b79f2403f9467782561c9c75a54604" IsLabelBoundToChannel="[bool]False" Label="[UIModel]9905796649f44175a56f9eb34178d24e" Left="[float]23" SelectedResource="[NI_Core_DataValues_TagRefnum]Pin1" Top="[float]30" Width="[float]150" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
			<Label Height="[float]16" Id="9905796649f44175a56f9eb34178d24e" LabelOwner="[UIModel]f7b79f2403f9467782561c9c75a54604" Left="[float]23" Text="[string]Pin name" Top="[float]10" Width="[float]49" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{26c56ad8-e31a-456d-979e-87865b3f5c61}/Configuration/measurement_type" Enabled="[bool]True" Height="[float]24" Id="dada7f23e27f4f468c0faf48553a7b66" IsLabelBoundToChannel="[bool]False" Label="[UIModel]570f36c6f42d4eb6a90f7e8a826ab54d" Left="[float]23" Top="[float]85" Width="[float]150" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
				<RingSelectorInfo DisplayValue="[string]DC_VOLTS" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]AC_VOLTS" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
			</ChannelEnumSelector>
			<Label Height="[float]16" Id="570f36c6f42d4eb6a90f7e8a826ab54d" LabelOwner="[UIModel]dada7f23e27f4f468c0faf48553a7b66" Left="[float]23" Text="[string]Measurement type" Top="[float]65" Width="[float]99" xmlns="http://www.ni.com/PanelCommon" />
		</ScreenSurface>
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/NIVisaDmmMeasurement.pinmap sha256=f9e00f73077da2904088013d03bcc3b24789c23838229320bd1d54d1837af68f bytes=579 -->
## FILE: examples/nivisa_dmm_measurement/NIVisaDmmMeasurement.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/NIVisaDmmMeasurement.pinmap`
- sha256: `f9e00f73077da2904088013d03bcc3b24789c23838229320bd1d54d1837af68f`
- bytes: 579

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.1">
	<Instruments>
		<Instrument name="GPIB0::3::INSTR" instrumentTypeId="VisaDmm">
			<Channel id="0" />
		</Instrument>
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="GPIB0::3::INSTR" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/NIVisaDmmMeasurement.serviceconfig sha256=05ec0b00b0791cd3ad2975575a88f154619d479d97461b12c103dd8afd817522 bytes=715 -->
## FILE: examples/nivisa_dmm_measurement/NIVisaDmmMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/NIVisaDmmMeasurement.serviceconfig`
- sha256: `05ec0b00b0791cd3ad2975575a88f154619d479d97461b12c103dd8afd817522`
- bytes: 715

````json
{
  "services": [
    {
      "displayName": "NI-VISA DMM Measurement (Py)",
      "version": "1.0.0",
      "serviceClass": "ni.examples.NIVisaDmmMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "installPath": "install.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in example that performs a DMM measurement using NI-VISA and an NI Instrument Simulator v2.0.",
        "ni/service.collection": "NI.Examples",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/NIVisaDmmMeasurement.sfp sha256=36331fe73bf6514ca61657538e5d48dd49ac7269716608d14dfb8502987ce341 bytes=9903 -->
## FILE: examples/nivisa_dmm_measurement/NIVisaDmmMeasurement.sfp

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/NIVisaDmmMeasurement.sfp`
- sha256: `36331fe73bf6514ca61657538e5d48dd49ac7269716608d14dfb8502987ce341`
- bytes: 9903

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="B1CAE5A0BBD16DF9143F89B3647CE23B31C49AAA8EE0F387E34EC63545B1FC3651B94586743E77AC2B35CD9266A96B00B587AF2ADCE2AADD0D92DA3EF5A01DF7" Timestamp="1D92540F3754F05" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.7.0.49209" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="6.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49209" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="23.0.0.49209" FeatureSetName="UnifiedTask" Name="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" Version="1.0.0.0" />
		<ParsableNamespace AssemblyFileVersion="23.0.0.49209" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49209" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.49209" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.49209" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="23.0.0.49209" />
	</SourceModelFeatureSet>
	<UnifiedTask Id="71e714fb199e4eac9ac630d63e786eac" LayoutInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Layout Information&quot;:{&quot;Sections&quot;:[{&quot;Columns Progressive Count&quot;:2,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Columns&quot;:[{&quot;Containers Progressive Count&quot;:1,&quot;Layout Information Index&quot;:1,&quot;Containers&quot;:[{&quot;Container Model Defition&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Container Assignment State&quot;:&quot;Available&quot;,&quot;Container Identifier&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen_2.task&quot;,&quot;Container Instrument Name&quot;:&quot;NI-VISA DMM Measurement (Py)&quot;,&quot;Layout Information Name&quot;:&quot;NI-VISA DMM Measurement (Py) 1&quot;,&quot;Layout Information Index&quot;:1,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Items&quot;:[{&quot;Identification Number&quot;:4294963201,&quot;Model Definition Type&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Parent Or Group Name&quot;:&quot;Measurements&quot;,&quot;Panel Type&quot;:&quot;NI-VISA DMM Measurement (Py)&quot;,&quot;Layout Information Name&quot;:&quot;ni.examples.NIVisaDmmMeasurement_Python&quot;,&quot;Layout Information Index&quot;:0}]}]}]},{&quot;Columns Progressive Count&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationOnly&quot;}]}}" PinAwareInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Selected Sites&quot;:[{&quot;Site Number&quot;:0}]}" xmlns="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" />
	<EnvoyManagerFile Id="39f1f22746e848bba57a105f24ffb630" xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="fd6a63646a49441397168a07c9d77ba2" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<NameScopingEnvoy AutomaticallyResolveUp="True" Id="596109ca19934794899596939c6f4686" Name="NIVisaDmmMeasurement.sfp" NameTracksFileName="True" />
		<EmbeddedDefinitionReference Id="8e85e9831a8442a9a9c288a57115fbcf" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="{http\://www.ni.com/InstrumentFramework/ScreenDocument}Screen_2.task">
			<Screen ClientId="{45254ae8-b217-44c3-8d28-7aeafb3597cf}" ConfigurationParameters="{&quot;@type&quot;:&quot;type.googleapis.com/ni.measurementlink.measurement.v1.MeasurementConfigurations&quot;,&quot;pinName&quot;:&quot;Pin1&quot;,&quot;measurementType&quot;:&quot;DC Volts&quot;,&quot;range&quot;:1.0,&quot;resolutionDigits&quot;:3.5}" DisplayName="NI-VISA DMM Measurement (Py)" Id="8907f5c915bd40d399f1f05cbebc1f0c" PanelPresentation="ConfigurationWithVisualization" ServiceClass="ni.examples.NIVisaDmmMeasurement_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
				<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]310" Id="da52556c2e7b48b5bd54b43091c6224d" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]410" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
					<ChannelStringControl AcceptsReturn="[bool]False" BaseName="[string]String" Channel="[string]{45254ae8-b217-44c3-8d28-7aeafb3597cf}/Configuration/measurement_type" Enabled="[bool]True" Height="[float]24" HorizontalScrollBarVisibility="[ScrollBarVisibility]Hidden" Id="3a3632eb84e24ea4883a59a6b10a74c1" IsLabelBoundToChannel="[bool]False" Label="[UIModel]d22c1c55766242d5ad9721a37ade857a" Left="[float]23" Text="[string]DC Volts" Top="[float]85" VerticalScrollBarVisibility="[ScrollBarVisibility]Auto" Width="[float]72" />
					<Label Height="[float]16" Id="d22c1c55766242d5ad9721a37ade857a" LabelOwner="[UIModel]3a3632eb84e24ea4883a59a6b10a74c1" Left="[float]23" Text="[string]Measurement type" Top="[float]65" Width="[float]99" xmlns="http://www.ni.com/PanelCommon" />
					<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BaseName="[string]Canvas" Height="[float]143" Id="456a3aa0a2cd49de969f5d23625398ab" Label="[UIModel]542ed5b07a1942d48c7713d80f29daff" Left="[float]23" Top="[float]140" Width="[float]127">
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{45254ae8-b217-44c3-8d28-7aeafb3597cf}/Configuration/range" Enabled="[bool]True" Height="[float]24" Id="95ebe7f3db834dcead51322fc115f774" IsLabelBoundToChannel="[bool]False" Label="[UIModel]a4dc111131a34cd6b94e8d5d032cae0a" Left="[float]15" RadixBase="[RadixBase]0" RadixVisibility="[SMVisibility]Collapsed" Top="[float]36" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=SystemInternational:Digits=2:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
						<Label Height="[float]16" Id="a4dc111131a34cd6b94e8d5d032cae0a" LabelOwner="[UIModel]95ebe7f3db834dcead51322fc115f774" Left="[float]15" Text="[string]Range" Top="[float]16" Width="[float]33" xmlns="http://www.ni.com/PanelCommon" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{45254ae8-b217-44c3-8d28-7aeafb3597cf}/Configuration/resolution_digits" Enabled="[bool]True" Height="[float]24" Id="b46074dfb6eb41299e6313887970aa6f" IsLabelBoundToChannel="[bool]False" Label="[UIModel]fb7a6bc0f8624b7092c7192b910472b6" Left="[float]15" Top="[float]96" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=1:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]70" />
						<Label Height="[float]16" Id="fb7a6bc0f8624b7092c7192b910472b6" LabelOwner="[UIModel]b46074dfb6eb41299e6313887970aa6f" Left="[float]15" Text="[string]Resolution (digits)" Top="[float]76" Width="[float]95" xmlns="http://www.ni.com/PanelCommon" />
					</ScreenSurfaceCanvas>
					<Label Height="[float]16" Id="542ed5b07a1942d48c7713d80f29daff" LabelOwner="[UIModel]456a3aa0a2cd49de969f5d23625398ab" Left="[float]23" Text="[string]Configuration" Top="[float]120" Width="[float]73" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{45254ae8-b217-44c3-8d28-7aeafb3597cf}/Output/measured_value" Height="[float]51" Id="3b0a52a98ae34e709c68c691ffc6e891" IsLabelBoundToChannel="[bool]False" IsReadOnly="[bool]True" Label="[UIModel]bb194d5b33744748a16759fe6a382776" Left="[float]195" MinHeight="[float]51" Top="[float]30" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=6:DigitDisplayType=DigitsOfPrecision:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]185">
						<FontSetting FontFamily="Segoe UI" FontSize="24" Id="61f2f2d796414a7aa6c69614b51133b8" xmlns="http://www.ni.com/PlatformFramework" />
					</ChannelNumericText>
					<Label Height="[float]16" Id="bb194d5b33744748a16759fe6a382776" LabelOwner="[UIModel]3b0a52a98ae34e709c68c691ffc6e891" Left="[float]195" Text="[string]Measured value" Top="[float]10" Width="[float]84" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{45254ae8-b217-44c3-8d28-7aeafb3597cf}/Configuration/pin_name" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="335b247cd9684fd7914d540217719f42" IsLabelBoundToChannel="[bool]False" Label="[UIModel]82d727693978442797b4ea568dce06e3" Left="[float]23" SelectedResource="[NI_Core_DataValues_TagRefnum]Pin1" Top="[float]30" Width="[float]127" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
					<Label Height="[float]16" Id="82d727693978442797b4ea568dce06e3" LabelOwner="[UIModel]335b247cd9684fd7914d540217719f42" Left="[float]23" Text="[string]Pin name" Top="[float]10" Width="[float]49" xmlns="http://www.ni.com/PanelCommon" />
				</ScreenSurface>
			</Screen>
		</EmbeddedDefinitionReference>
	</EnvoyManagerFile>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/NIVisaDmmMeasurement_example.seq sha256=a51bd4438da4d4a7e1fd2a6af56c6e86802ce4e8124b52b962a19bbdbe52b0aa bytes=176936 -->
## FILE: examples/nivisa_dmm_measurement/NIVisaDmmMeasurement_example.seq

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/NIVisaDmmMeasurement_example.seq`
- sha256: `a51bd4438da4d4a7e1fd2a6af56c6e86802ce4e8124b52b962a19bbdbe52b0aa`
- bytes: 176936

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
											<Step typename='NI_Measurement' xsi:type='NI_Measurement' name='Perform a measurement using a DMM simulator'>
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
																<value>ni.examples.NIVisaDmmMeasurement_Python</value>
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
																					<value>0i64</value>
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
																					<value lbound='[0]' ubound='[1]'>
																						<value>
																							<Num name='DC_VOLTS'>
																								<value representation='Int64'>0</value>
																							</Num>
																						</value>
																						<value>
																							<Num name='AC_VOLTS'>
																								<value representation='Int64'>1</value>
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
																					<value>1</value>
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
																					<value>3.5</value>
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
																<value>ID#:CqYU/eKU7hGhxWDjK76h1B</value>
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
														<value>"NIVisaDmmMeasurement.pinmap"</value>
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
																				<value>teststand_nivisa_dmm.py</value>
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
																				<value>create_nivisa_dmm_sessions</value>
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
																				<value>teststand_nivisa_dmm.py</value>
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
																				<value>destroy_nivisa_dmm_sessions</value>
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

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/poetry.toml sha256=ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e bytes=34 -->
## FILE: examples/nivisa_dmm_measurement/poetry.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/poetry.toml`
- sha256: `ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e`
- bytes: 34

````toml
[virtualenvs]
in-project = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/pyproject.toml sha256=38d81cdebd928f99a4b5ed4e0f9f9d964662eaf8850efe02127d45d4927e9ce1 bytes=1122 -->
## FILE: examples/nivisa_dmm_measurement/pyproject.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/pyproject.toml`
- sha256: `38d81cdebd928f99a4b5ed4e0f9f9d964662eaf8850efe02127d45d4927e9ce1`
- bytes: 1122

````toml
[tool.poetry]
name = "nivisa_dmm_measurement"
version = "0.5.0"
package-mode = false
description = "Measurement plug-in example that performs a DMM measurement using NI-VISA and an NI Instrument Simulator v2.0."
authors = ["National Instruments"]

[tool.poetry.dependencies]
python = "^3.10"
ni-measurement-plugin-sdk-service = {version = ">=2.3.1,<4.0"}
PyVISA = "^1.13.0"
PyVISA-sim = "^0.5.1"
click = ">=7.1.2, !=8.1.4" # mypy fails with click 8.1.4: https://github.com/pallets/click/issues/2558
grpcio = "*"
python-decouple = ">=3.8"

[tool.poetry.group.dev.dependencies]
ni-python-styleguide = ">=0.4.1"
mypy = ">=1.0"
types-grpcio = ">=1.0"
# Uncomment to use prerelease dependencies.
# ni-measurement-plugin-sdk-service = {path = "../../packages/service", develop = true}

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.mypy]
disallow_untyped_defs = true

[[tool.mypy.overrides]]
module = [
  # https://github.com/HBNetwork/python-decouple/issues/122 - Add support for type stubs
  "decouple.*",
]
ignore_missing_imports = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/README.md sha256=cf824da3790cd83df9808bd67d37892cb865bc9b8c1868f6f86c9c07f03f2149 bytes=3222 -->
## FILE: examples/nivisa_dmm_measurement/README.md

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/README.md`
- sha256: `cf824da3790cd83df9808bd67d37892cb865bc9b8c1868f6f86c9c07f03f2149`
- bytes: 3222

````markdown
## NI-VISA DMM Measurement

This is a measurement plug-in example that performs a DMM measurement using NI-VISA
and a DMM that supports SCPI commands.

### Features

- Uses the open-source `PyVISA` package to access NI-VISA from Python
- Uses the open-source `PyVISA-sim` package to simulate instruments in software
- Pin-aware, supporting a custom instrument type and a single session/pin/site
- Includes InstrumentStudio and Measurement Plug-In UI Editor project files
- Includes a TestStand sequence showing how to configure the pin map, register
  instrument resources with the session management service, and run a
  measurement
  - For the sake of simplicity, the TestStand sequence handles pin map and
    session registration and unregistration in the `Setup` and `Cleanup`
    sections of the main sequence. For **Test UUTs** and batch process model use
    cases, these steps should be moved to the `ProcessSetup` and
    `ProcessCleanup` callbacks.
- Uses the NI gRPC Device Server to allow sharing instrument sessions with other
  measurement services when running measurements from TestStand

### Required Software

- InstrumentStudio 2025 Q1 or later
- NI-488.2 and/or NI-Serial
- NI-VISA
  - gRPC support requires NI-VISA 2024 Q1 or later and the NI-VISA gRPC Runtime package.
- Recommended: TestStand 2021 SP1 or later
- Optional: NI Instrument Simulator software

> **Note:**
>
> This example uses the custom instrument driver `_visa_dmm.py` to perform the
> device-specific commands and queries.

### Required Hardware

Supported instrument models:
- NI Instrument Simulator v2.0
- HP/Agilent/Keysight 34401A DMM

By default, this example uses a physical instrument. To simulate an instrument
in software, follow the steps below:
- Create a `.env` file in the measurement service's directory or one of its
  parent directories (such as the root of your Git repository or
  `C:\ProgramData\National Instruments\Plug-Ins\Measurements` for statically
  registered measurement services).
- Add the following option to the `.env` file to enable simulation via the
  driver's `simulate` parameter:

  ```
  MEASUREMENT_PLUGIN_VISA_DMM_SIMULATE=1
  ```

The `_visa_dmm.py` instrument driver implements simulation using PyVISA-sim.
[`_visa_dmm_sim.yaml`](./_visa_dmm_sim.yaml) defines the behavior of the
simulated instrument.

To use a physical instrument:
- Connect the instrument to a supported interface, such as GPIB or serial.
- By default, the pin map included with this example uses the resource name
  `GPIB0::3::INSTR`, which matches the NI Instrument Simulator's factory default
  settings when connected via GPIB.
  - If this doesn't match your instrument's configuration, edit
    [`NIVisaDmmMeasurement.pinmap`](./NIVisaDmmMeasurement.pinmap) and replace
    `GPIB0::3::INSTR` with the desired resource name (e.g. `ASRL1::INSTR`).
  - To modify the NI Instrument Simulator configuration (e.g. GPIB address,
    serial configuration), use the `Instrument Simulator Wizard` included with
    the NI Instrument Simulator software.
  - To configure third party instruments, see the documentation provided with
    the instrument.
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/start.bat sha256=bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851 bytes=253 -->
## FILE: examples/nivisa_dmm_measurement/start.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/start.bat`
- sha256: `bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851`
- bytes: 253

````batch
@echo off
REM The discovery service uses this script to start the measurement service.
REM You can customize this script for your Python setup. The -v option logs
REM messages with level INFO and above.

.venv\Scripts\python.exe measurement.py -v
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/teststand_nivisa_dmm.py sha256=181a20b310a66bf4360811cfe3e41eaa79ec51b8bfc0f5cb1edb2f2dafbe9c2f bytes=3346 -->
## FILE: examples/nivisa_dmm_measurement/teststand_nivisa_dmm.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/nivisa_dmm_measurement/teststand_nivisa_dmm.py`
- sha256: `181a20b310a66bf4360811cfe3e41eaa79ec51b8bfc0f5cb1edb2f2dafbe9c2f`
- bytes: 3346

````python
"""Functions to set up and tear down NI-VISA DMM sessions in NI TestStand."""

import pathlib
from typing import Any

from _helpers import TestStandSupport
from _visa_dmm import INSTRUMENT_TYPE_VISA_DMM
from _visa_dmm_session_management import VisaDmmSessionConstructor
from decouple import AutoConfig
from ni_measurement_plugin_sdk_service.discovery import DiscoveryClient
from ni_measurement_plugin_sdk_service.grpc.channelpool import GrpcChannelPool
from ni_measurement_plugin_sdk_service.session_management import (
    PinMapContext,
    SessionInitializationBehavior,
    SessionManagementClient,
)

# Search for the `.env` file starting with this code module's parent directory.
_config = AutoConfig(str(pathlib.Path(__file__).resolve().parent))
_VISA_DMM_SIMULATE: bool = _config("MEASUREMENT_PLUGIN_VISA_DMM_SIMULATE", default=False, cast=bool)


def create_nivisa_dmm_sessions(sequence_context: Any) -> None:
    """Create and register all NI-VISA DMM sessions.

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
        session_constructor = VisaDmmSessionConstructor(
            _config,
            discovery_client,
            SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH,
        )

        with session_management_client.reserve_sessions(
            context=pin_map_context, instrument_type_id=INSTRUMENT_TYPE_VISA_DMM
        ) as reservation:
            with reservation.initialize_sessions(
                session_constructor, instrument_type_id=INSTRUMENT_TYPE_VISA_DMM
            ):
                pass

            session_management_client.register_sessions(reservation.session_info)


def destroy_nivisa_dmm_sessions() -> None:
    """Destroy and unregister all NI-VISA DMM sessions."""
    with GrpcChannelPool() as grpc_channel_pool:
        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        session_constructor = VisaDmmSessionConstructor(
            _config,
            discovery_client,
            SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE,
        )

        with session_management_client.reserve_all_registered_sessions(
            instrument_type_id=INSTRUMENT_TYPE_VISA_DMM,
        ) as reservation:
            if not reservation.session_info:
                return

            with reservation.initialize_sessions(
                session_constructor, instrument_type_id=INSTRUMENT_TYPE_VISA_DMM
            ):
                pass

            session_management_client.unregister_sessions(reservation.session_info)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/.serviceignore sha256=997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912 bytes=148 -->
## FILE: examples/output_voltage_measurement/.serviceignore

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/.serviceignore`
- sha256: `997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912`
- bytes: 148

````text
# This file specifies that when we publish this plug-in to a plug-in library,
# we should not copy the following directories:
.venv
__pycache__
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/_helpers.py sha256=0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426 bytes=2920 -->
## FILE: examples/output_voltage_measurement/_helpers.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/_helpers.py`
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

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/_visa_dmm.py sha256=c65dd70dc2df5495836ef3f7ce9f83063a6ed98869fbccb082c76cedd183f330 bytes=4565 -->
## FILE: examples/output_voltage_measurement/_visa_dmm.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/_visa_dmm.py`
- sha256: `c65dd70dc2df5495836ef3f7ce9f83063a6ed98869fbccb082c76cedd183f330`
- bytes: 4565

````python
"""Custom instrument driver for measurement plug-in NI-VISA DMM examples."""

from __future__ import annotations

import pathlib
import sys
from enum import Enum
from types import TracebackType
from typing import TYPE_CHECKING

import pyvisa
import pyvisa.resources
import pyvisa.typing

if TYPE_CHECKING:
    if sys.version_info >= (3, 11):
        from typing import Self
    else:
        from typing_extensions import Self


# Pin map instrument type constant for VISA DMM
INSTRUMENT_TYPE_VISA_DMM = "VisaDmm"

_SIMULATION_YAML_PATH = pathlib.Path(__file__).resolve().parent / "_visa_dmm_sim.yaml"

_RESOLUTION_DIGITS_TO_VALUE = {"3.5": 0.001, "4.5": 0.0001, "5.5": 1e-5, "6.5": 1e-6}

# Supported NI-VISA DMM instrument IDs, both real and simulated, can be added here
_SUPPORTED_INSTRUMENT_IDS = [
    # Keysight/Agilent/HP 34401A
    "34401",
    "34410",
    "34411",
    "L4411",
    # NI Instrument Simulator v2.0
    "Instrument Simulator",  # single instrument
    "Waveform Generator Simulator",  # multi-instrument
]


class Function(Enum):
    """Enum that represents the measurement function."""

    DC_VOLTS = 0
    AC_VOLTS = 1


_FUNCTION_TO_VALUE = {
    Function.DC_VOLTS: "VOLT:DC",
    Function.AC_VOLTS: "VOLT:AC",
}


class Session:
    """An NI-VISA DMM session."""

    def __init__(
        self,
        resource_name: str,
        id_query: bool = True,
        reset_device: bool = True,
        simulate: bool = False,
    ) -> None:
        """Open NI-VISA DMM session."""
        # Create a real or simulated VISA resource manager."""
        visa_library = f"{_SIMULATION_YAML_PATH}@sim" if simulate else ""
        resource_manager = pyvisa.ResourceManager(visa_library)

        session = resource_manager.open_resource(
            resource_name, read_termination="\n", write_termination="\n"
        )

        if not isinstance(session, pyvisa.resources.MessageBasedResource):
            raise TypeError("The 'session' object must be an instance of MessageBasedResource.")
        self._session = session

        if id_query:
            self._validate_id()

        if reset_device:
            self._reset()

    def close(self) -> None:
        """Close the session."""
        self._session.close()

    def __enter__(self) -> Self:
        """Context management protocol. Returns self."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Context management protocol. Calls close()."""
        self.close()

    def configure_measurement_digits(
        self, function: Function, range: float, resolution_digits: float
    ) -> None:
        """Configure the common properties of the measurement.

        These properties include function, range, and resolution_digits.
        """
        function_enum = _FUNCTION_TO_VALUE[function]
        resolution_value = _RESOLUTION_DIGITS_TO_VALUE[str(resolution_digits)]

        self._session.write("CONF:%s %.g,%.g" % (function_enum, range, resolution_value))
        self._check_error()

    def read(self) -> float:
        """Acquires a single measurement and returns the measured value."""
        response = self._session.query("READ?")
        self._check_error()
        return float(response)

    def _check_error(self) -> None:
        """Query the instrument's error queue."""
        response = self._session.query("SYST:ERR?")
        fields = response.split(",", maxsplit=1)
        assert len(fields) >= 1
        if int(fields[0]) != 0:
            raise RuntimeError("Instrument returned error %s: %s" % (fields[0], fields[1]))

    def _validate_id(self) -> None:
        """Check the selected instrument is proper and responding.."""
        instrument_id = self._session.query("*IDN?")
        if not any(id_check in instrument_id for id_check in _SUPPORTED_INSTRUMENT_IDS):
            raise RuntimeError(
                "The ID query failed. This may mean that you selected the wrong instrument, your instrument did not respond, "
                f"or you are using a model that is not officially supported by this driver. Instrument ID: {instrument_id}"
            )

    def _reset(self) -> None:
        """Reset the instrument to a known state."""
        self._session.write("*CLS")
        self._session.write("*RST")
        self._check_error()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/_visa_dmm_session_management.py sha256=2513ba32f13749571007447e6052806f1f7b19f8f7d2ecf9c4e169c2f2123f4b bytes=2634 -->
## FILE: examples/output_voltage_measurement/_visa_dmm_session_management.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/_visa_dmm_session_management.py`
- sha256: `2513ba32f13749571007447e6052806f1f7b19f8f7d2ecf9c4e169c2f2123f4b`
- bytes: 2634

````python
import logging

from _visa_dmm import Session
from _visa_grpc import build_visa_grpc_resource_string, get_visa_grpc_insecure_address
from decouple import AutoConfig
from ni_measurement_plugin_sdk_service.discovery import DiscoveryClient
from ni_measurement_plugin_sdk_service.session_management import (
    SessionInformation,
    SessionInitializationBehavior,
)

_logger = logging.getLogger(__name__)


class VisaDmmSessionConstructor:
    """Measurement plug-in session constructor for VISA DMM sessions."""

    def __init__(
        self,
        config: AutoConfig,
        discovery_client: DiscoveryClient,
        initialization_behavior: SessionInitializationBehavior = SessionInitializationBehavior.AUTO,
    ) -> None:
        """Construct a VisaDmmSessionConstructor."""
        self._config = config
        self._discovery_client = discovery_client
        self._initialization_behavior = initialization_behavior

        # Hack: config is a parameter for now so TestStand code modules use the right config path.
        self._visa_dmm_simulate: bool = config(
            "MEASUREMENT_PLUGIN_VISA_DMM_SIMULATE", default=False, cast=bool
        )

        if self._visa_dmm_simulate:
            # _visa_dmm_sim.yaml doesn't include the grpc:// resource names.
            _logger.debug("Not using NI gRPC Device Server due to simulation")
            self._address = ""
        else:
            self._address = get_visa_grpc_insecure_address(config, discovery_client)
            if self._address:
                _logger.debug("NI gRPC Device Server address: http://%s", self._address)
            else:
                _logger.debug("Not using NI gRPC Device Server")

    def __call__(self, session_info: SessionInformation) -> Session:
        """Construct a VISA DMM session based on measurement plug-in session info."""
        resource_name = session_info.resource_name
        if self._address:
            resource_name = build_visa_grpc_resource_string(
                resource_name,
                self._address,
                session_info.session_name,
                self._initialization_behavior,
            )

        # When this measurement is called from outside of TestStand (session_exists
        # == False), reset the instrument to a known state. In TestStand,
        # ProcessSetup resets the instrument.
        reset_device = not session_info.session_exists

        _logger.debug("VISA resource name: %s", resource_name)
        return Session(resource_name, reset_device=reset_device, simulate=self._visa_dmm_simulate)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/_visa_dmm_sim.yaml sha256=42b0613184bcabf53401a702437d3a387d1b6d7c9fbf37b53a9cf74b837fe480 bytes=743 -->
## FILE: examples/output_voltage_measurement/_visa_dmm_sim.yaml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/_visa_dmm_sim.yaml`
- sha256: `42b0613184bcabf53401a702437d3a387d1b6d7c9fbf37b53a9cf74b837fe480`
- bytes: 743

````yaml
spec: "1.1"
devices:
  VisaDmm:
    eom:
      GPIB INSTR:
        q: "\n"
        r: "\n"
    dialogues:
      - q: "*CLS"
      - q: "*IDN?"
        r: "National Instruments,Waveform Generator Simulator (simulated with pyvisa-sim),00000000,2.0.1"
      - q: "*RST"
      - q: "READ?"
        r: "1.23456"
    error:
      error_queue:
        - q: 'SYST:ERR?'
          default: '0,No Error'
          command_error: '-100,Command Error'
          query_error: '-400,Query Error'
    properties:
      configuration:
        default: "VOLT:DC 5.000000,0.001000"
        getter:
          q: "CONF?"
          r: "{:s}"
        setter:
          q: "CONF:{:s}"

resources:
  GPIB0::3::INSTR:
    device: VisaDmm
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/_visa_grpc.py sha256=c6f8dd68dbe9a27fb3ad8dc56d72335a5f798977dbfccf8f29452fca96e3449b bytes=2100 -->
## FILE: examples/output_voltage_measurement/_visa_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/_visa_grpc.py`
- sha256: `c6f8dd68dbe9a27fb3ad8dc56d72335a5f798977dbfccf8f29452fca96e3449b`
- bytes: 2100

````python
from urllib.parse import urlencode, urlsplit

from decouple import AutoConfig
from ni_measurement_plugin_sdk_service.discovery import DiscoveryClient
from ni_measurement_plugin_sdk_service.session_management import SessionInitializationBehavior

_INITIALIZATION_BEHAVIOR = {
    SessionInitializationBehavior.AUTO: 0,
    SessionInitializationBehavior.INITIALIZE_SERVER_SESSION: 1,
    SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION: 2,
    SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH: 3,
    SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE: 4,
}

GRPC_SERVICE_INTERFACE_NAME = "visa_grpc.Visa"
SERVICE_CLASS = "ni.measurementlink.v1.grpcdeviceserver"


def build_visa_grpc_resource_string(
    resource_name: str,
    address: str,
    session_name: str = "",
    initialization_behavior: SessionInitializationBehavior = SessionInitializationBehavior.AUTO,
) -> str:
    """Build an grpc:// resource string for remoting with NI-VISA."""
    query = {
        "init_behavior": _INITIALIZATION_BEHAVIOR[initialization_behavior],
        "session_name": session_name,
    }
    return f"grpc://{address}/{resource_name}?" + urlencode(query)


def get_visa_grpc_insecure_address(config: AutoConfig, discovery_client: DiscoveryClient) -> str:
    """Get the insecure address of NI gRPC Device Server's VISA interface in host:port format."""
    # Hack: config is a parameter for now so TestStand code modules use the right config path.
    use_grpc_device_server: bool = config(
        "MEASUREMENT_PLUGIN_USE_GRPC_DEVICE_SERVER", default=True, cast=bool
    )
    grpc_device_server_address: str = config(
        "MEASUREMENT_PLUGIN_GRPC_DEVICE_SERVER_ADDRESS", default=""
    )

    if not use_grpc_device_server:
        return ""

    if grpc_device_server_address:
        return urlsplit(grpc_device_server_address).netloc
    else:
        service_location = discovery_client.resolve_service(
            GRPC_SERVICE_INTERFACE_NAME, SERVICE_CLASS
        )
        return service_location.insecure_address
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/install.bat sha256=695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025 bytes=205 -->
## FILE: examples/output_voltage_measurement/install.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/install.bat`
- sha256: `695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025`
- bytes: 205

````batch
@echo off
REM The discovery service uses this script to install the dependencies
REM for the measurement service. You can customize this script for your
REM Python setup.

poetry install --only main
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/measurement.py sha256=3589e6c05376901bab86aa140a3696aa064342035b9e3f9624cc6df19ce0418c bytes=7217 -->
## FILE: examples/output_voltage_measurement/measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/measurement.py`
- sha256: `3589e6c05376901bab86aa140a3696aa064342035b9e3f9624cc6df19ce0418c`
- bytes: 7217

````python
"""Source DC voltage as input with an NI SMU and measure output using NI-VISA DMM."""

import logging
import pathlib
import threading
import time

import _visa_dmm
import click
import grpc
import hightime
import ni_measurement_plugin_sdk_service as nims
import nidcpower
import nidcpower.session
from _helpers import configure_logging, verbosity_option
from _visa_dmm_session_management import VisaDmmSessionConstructor
from decouple import AutoConfig

_NIDCPOWER_WAIT_FOR_EVENT_TIMEOUT_ERROR_CODE = -1074116059
_NIDCPOWER_TIMEOUT_EXCEEDED_ERROR_CODE = -1074097933
_NIDCPOWER_TIMEOUT_ERROR_CODES = [
    _NIDCPOWER_WAIT_FOR_EVENT_TIMEOUT_ERROR_CODE,
    _NIDCPOWER_TIMEOUT_EXCEEDED_ERROR_CODE,
]

service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "OutputVoltageMeasurement.serviceconfig",
    ui_file_paths=[service_directory / "OutputVoltageMeasurement.measui"],
)

# Search for the `.env` file starting with the current directory.
_config = AutoConfig(str(pathlib.Path.cwd()))


@measurement_service.register_measurement
# NI-DCPower configuration
@measurement_service.configuration("voltage_level", nims.DataType.Double, 6.0)
@measurement_service.configuration("voltage_level_range", nims.DataType.Double, 6.0)
@measurement_service.configuration("current_limit", nims.DataType.Double, 0.01)
@measurement_service.configuration("current_limit_range", nims.DataType.Double, 0.01)
@measurement_service.configuration("source_delay", nims.DataType.Double, 0.0)
@measurement_service.configuration(
    "input_pin",
    nims.DataType.IOResource,
    "InPin",
    instrument_type=nims.session_management.INSTRUMENT_TYPE_NI_DCPOWER,
)
# NI-VISA DMM configuration
@measurement_service.configuration(
    "measurement_type",
    nims.DataType.Enum,
    _visa_dmm.Function.DC_VOLTS,
    enum_type=_visa_dmm.Function,
)
@measurement_service.configuration("range", nims.DataType.Double, 10.0)
@measurement_service.configuration("resolution_digits", nims.DataType.Double, 3.5)
@measurement_service.configuration(
    "output_pin",
    nims.DataType.IOResource,
    "OutPin",
    instrument_type=_visa_dmm.INSTRUMENT_TYPE_VISA_DMM,
)
@measurement_service.output("measured_value", nims.DataType.Double)
def measure(
    voltage_level: float,
    voltage_level_range: float,
    current_limit: float,
    current_limit_range: float,
    source_delay: float,
    input_pin: str,
    measurement_type: _visa_dmm.Function,
    range: float,
    resolution_digits: float,
    output_pin: str,
) -> tuple[float]:
    """Source DC voltage as input with an NI SMU and measure output using NI-VISA DMM."""
    logging.info(
        "Executing measurement: pin_names=%s voltage_level=%g measurement_type=%s range=%g resolution_digits=%g",
        [input_pin, output_pin],
        voltage_level,
        measurement_type,
        range,
        resolution_digits,
    )

    cancellation_event = threading.Event()
    measurement_service.context.add_cancel_callback(cancellation_event.set)

    dmm_session_constructor = VisaDmmSessionConstructor(
        _config, measurement_service.discovery_client
    )

    with measurement_service.context.reserve_sessions([input_pin, output_pin]) as reservation:
        with reservation.initialize_nidcpower_session(), reservation.initialize_session(
            dmm_session_constructor, _visa_dmm.INSTRUMENT_TYPE_VISA_DMM
        ):
            # Configure the SMU channel connected to the input pin.
            source_connection = reservation.get_nidcpower_connection(input_pin)
            source_channel = source_connection.session.channels[source_connection.channel_name]
            source_channel.source_mode = nidcpower.SourceMode.SINGLE_POINT
            source_channel.output_function = nidcpower.OutputFunction.DC_VOLTAGE
            source_channel.current_limit = current_limit
            source_channel.voltage_level_range = voltage_level_range
            source_channel.current_limit_range = current_limit_range
            source_channel.source_delay = hightime.timedelta(seconds=source_delay)
            source_channel.voltage_level = voltage_level

            # Configure the DMM connected to the output pin.
            measure_connection = reservation.get_connection(_visa_dmm.Session, output_pin)
            measure_session = measure_connection.session
            measure_session.configure_measurement_digits(measurement_type, range, resolution_digits)

            # Initiate the source channel to start sourcing a voltage on the
            # input pin. initiate() returns a context manager that aborts the
            # measurement when the function returns or raises an exception.
            with source_channel.initiate():
                # Wait for the output to settle.
                timeout = source_delay + 10.0
                _wait_for_nidcpower_event(
                    source_channel,
                    cancellation_event,
                    nidcpower.enums.Event.SOURCE_COMPLETE,
                    timeout,
                )

            # Measure the voltage on the output pin.
            measured_value = measure_session.read()

            # Reset the channel to a known state
            source_channel.reset()

    logging.info("Completed measurement: measured_value=%g", measured_value)
    return (measured_value,)


def _wait_for_nidcpower_event(
    channels: nidcpower.session._SessionBase,
    cancellation_event: threading.Event,
    event_id: nidcpower.enums.Event,
    timeout: float,
) -> None:
    """Wait for a NI-DCPower event or until error/cancellation occurs."""
    grpc_deadline = time.time() + measurement_service.context.time_remaining
    user_deadline = time.time() + timeout

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

        # Wait for the NI-DCPower event. If this takes more than 100 ms, check
        # whether the measurement was canceled and try again. NI-DCPower does
        # not support canceling a call to wait_for_event().
        try:
            channels.wait_for_event(event_id, timeout=100e-3)
            break
        except nidcpower.errors.DriverError as e:
            if e.code in _NIDCPOWER_TIMEOUT_ERROR_CODES:
                pass
            raise


@click.command
@verbosity_option
def main(verbosity: int) -> None:
    """Source DC voltage as input with an NI SMU and measure output using NI-VISA DMM."""
    configure_logging(verbosity)

    with measurement_service.host_service():
        input("Press enter to close the measurement service.\n")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/OutputVoltageMeasurement.instudioproj sha256=8838b15c7b4802c550da678898471f270642c8505019ef91fda80af40e169eac bytes=2044 -->
## FILE: examples/output_voltage_measurement/OutputVoltageMeasurement.instudioproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/OutputVoltageMeasurement.instudioproj`
- sha256: `8838b15c7b4802c550da678898471f270642c8505019ef91fda80af40e169eac`
- bytes: 2044

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="62A3A74C95C26713B7624CD6996C1D87F91D14BCEC877012783C419916151651A131E8D785CA00920B05E34C8B86A952E460908BE46C952400D8F6FCDFFFF9DE" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.8.0.1008" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="9.10.0.1008" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.8.0.1008" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="23.8.0.1008" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="bc8bce40174d4cfeb33eb53b84e0e272" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="ccc1c94a81f649fabbd28af06fc59524" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="eea51d76a45f4d28b4a92aea14b08c38" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<FileReference Id="1f20098d6772451f8fd6b30390e18916" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="OutputVoltageMeasurement.pinmap" StoragePath="OutputVoltageMeasurement.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
			<SourceFileReference Bindings="EnvoyManager" Id="b9737b7049a843b29a33221257eb315c" ModelDefinitionType="NationalInstruments.InstrumentFramework.Document.SourceModel.UnifiedTask" Name="OutputVoltageMeasurement.sfp" StoragePath="OutputVoltageMeasurement.sfp" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/OutputVoltageMeasurement.measproj sha256=2c7f5c04bda7b62d55113cc662552b44c3cfa5eba8c7510a6a495b7a452ab339 bytes=3836 -->
## FILE: examples/output_voltage_measurement/OutputVoltageMeasurement.measproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/OutputVoltageMeasurement.measproj`
- sha256: `2c7f5c04bda7b62d55113cc662552b44c3cfa5eba8c7510a6a495b7a452ab339`
- bytes: 3836

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="3AA8CFFF7D439D562731B15B947690ACE12CB3EA5FDEB7A98FCD787C4173032B2C66DA87C73E3FF00BCD2E095DCD316071ADDA5C14972E58CC225464571AA7C4" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.8.0.1008" FeatureSetName="Pin Map" Name="http://www.ni.com/InstrumentFramework/PinMap" OldestCompatibleVersion="21.3.0.0" Version="21.3.0.0" />
		<ParsableNamespace AssemblyFileVersion="23.8.0.1008" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.10.0.1008" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.10.0.1008" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/EnvoyManagement" OldestCompatibleVersion="5.0.0.0" Version="5.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.10.0.1008" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemDiagram" OldestCompatibleVersion="8.0.0.49152" Version="8.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.10.0.1008" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemModelCore" OldestCompatibleVersion="5.1.0.5" Version="5.2.0.49152" />
		<ApplicationVersionInfo Build="23.8.0.1008" Name="MeasurementLink UI Editor" Version="23.8.0.1008" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="bcdf26cc4754339a87377a413930d1e" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="2327a42208f24147adfb3af11fcff261" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<EmbeddedDefinitionReference Id="6145e69fa95a4b7aba8db7e32da0f9ed" ModelDefinitionType="NationalInstruments.SystemDesigner.SystemDiagram.SystemDiagramDefinition" Name="SystemDiagram">
			<SystemDiagram Id="4c356b1d1ae342c7b6df52931cd9e32f" SystemDiagramVersion="75" xmlns="http://www.ni.com/SystemDesigner/SystemDiagram">
				<EnvoySuperimpositionContainer Id="e1894cbb6d7c4a7d92f5fddc071f7789" xmlns="http://www.ni.com/SystemDesigner/EnvoyManagement">
					<MappingManager Id="b092d1ae0db74b86a335e917123423cf" xmlns="http://www.ni.com/SystemDesigner/SystemModelCore">
						<Superimposition Id="2669a6cd6cd84bfe8847c814378d9857" Name="Root Superimposition" />
					</MappingManager>
				</EnvoySuperimpositionContainer>
				<SystemDiagramRootDiagram Id="7623d386bfa443239c0d3057ba33652d" />
			</SystemDiagram>
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="d2e3baa5dda446fb909f7a776abacac4" ModelDefinitionType="NullTarget" Name="NullTarget">
			<NullTarget />
		</NameScopingEnvoy>
		<NameScopingEnvoy Id="c63f5ac83cb34e108bb4ec589ce96130" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<FileReference Id="e112c28b0d9c4472a4cf6bece0cbda64" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/PinMap}PinMapDefinition" Name="OutputVoltageMeasurement.pinmap" StoragePath="OutputVoltageMeasurement.pinmap" p4:IsActive="True" xmlns:p4="http://www.ni.com/InstrumentFramework/PinMap" />
			<SourceFileReference Id="d0c6ffe5ebc24ec381db3c6fa34800ef" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="OutputVoltageMeasurement.measui" StoragePath="OutputVoltageMeasurement.measui" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/OutputVoltageMeasurement.measui sha256=efe03dcd376672dc6d83aae3993d0516c131148fe89196e5063de6d3787d200a bytes=11833 -->
## FILE: examples/output_voltage_measurement/OutputVoltageMeasurement.measui

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/OutputVoltageMeasurement.measui`
- sha256: `efe03dcd376672dc6d83aae3993d0516c131148fe89196e5063de6d3787d200a`
- bytes: 11833

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="C055FD2EB2DC532BD00E91239D96A2EA9A8788054B01E38639F968C3EA00DA553BDB710BBB18F200D600457674EB08FEB6B891E6871E8F3045DEC31C5E3D0ED5" Timestamp="1D9F2371AC37AF2" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.9.0.50025" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="9.8.1.49152" />
		<ParsableNamespace AssemblyFileVersion="9.9.0.50025" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="23.5.0.50025" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.9.0.50025" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.9.0.50025" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.5.0.50026" Name="MeasurementLink UI Editor" Version="23.5.0.50026" />
	</SourceModelFeatureSet>
	<Screen ClientId="{c49a8444-50b4-4a7e-a53d-5e73bb070843}" DisplayName="Output Voltage Measurement (Py)" Id="348479cea2604293ad04f34470b8e3d3" ServiceClass="ni.examples.OutputVoltageMeasurement_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
		<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]385" Id="6182aa5303164ddfbf4fd9e71c9573fb" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]736" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
			<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]268" Id="85e66a8c8349409cbc42e5e06bbd5ebf" Label="[UIModel]81206002783247279b0d082c08a5de89" Left="[float]23" Top="[float]94" Width="[float]192">
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{c49a8444-50b4-4a7e-a53d-5e73bb070843}/Configuration/voltage_level" Enabled="[bool]True" Height="[float]24" Id="6a331f48b672444ea8293583fb2c8f61" IsLabelBoundToChannel="[bool]False" Label="[UIModel]5190bc685dfe4688b3d5835069649633" Left="[float]16" Top="[float]28" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{c49a8444-50b4-4a7e-a53d-5e73bb070843}/Configuration/current_limit" Enabled="[bool]True" Height="[float]24" Id="aa8fc66579b144a9bceb8ad7af4c245f" IsLabelBoundToChannel="[bool]False" Label="[UIModel]62e6ffbde24a49b49e1da5a89cf751ea" Left="[float]16" Top="[float]78" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{c49a8444-50b4-4a7e-a53d-5e73bb070843}/Configuration/voltage_level_range" Enabled="[bool]True" Height="[float]24" Id="c9d188f1e4c74ce3a9ba71d3c771464f" IsLabelBoundToChannel="[bool]False" Label="[UIModel]f702db70874f4899841167a16854f27f" Left="[float]16" Top="[float]128" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{c49a8444-50b4-4a7e-a53d-5e73bb070843}/Configuration/current_limit_range" Enabled="[bool]True" Height="[float]24" Id="2a41a65576be42c8bccd80a1c8f344eb" IsLabelBoundToChannel="[bool]False" Label="[UIModel]7b24316c52594088ae2ddd8825b2a3fa" Left="[float]16" Top="[float]178" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{c49a8444-50b4-4a7e-a53d-5e73bb070843}/Configuration/source_delay" Enabled="[bool]True" Height="[float]24" Id="2dc7b9f3c95940bb91b287362bbfc0f4" IsLabelBoundToChannel="[bool]False" Label="[UIModel]f4dc039b2b92408cbf09356335161c02" Left="[float]16" Top="[float]228" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
				<Label Height="[float]16" Id="5190bc685dfe4688b3d5835069649633" LabelOwner="[UIModel]6a331f48b672444ea8293583fb2c8f61" Left="[float]16" Text="[string]Voltage level (V)" Top="[float]8" Width="[float]86" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="62e6ffbde24a49b49e1da5a89cf751ea" LabelOwner="[UIModel]aa8fc66579b144a9bceb8ad7af4c245f" Left="[float]16" Text="[string]Current limit (A)" Top="[float]58" Width="[float]84" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="f702db70874f4899841167a16854f27f" LabelOwner="[UIModel]c9d188f1e4c74ce3a9ba71d3c771464f" Left="[float]16" Text="[string]Voltage level range (V)" Top="[float]108" Width="[float]119" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="7b24316c52594088ae2ddd8825b2a3fa" LabelOwner="[UIModel]2a41a65576be42c8bccd80a1c8f344eb" Left="[float]16" Text="[string]Current limit range (A)" Top="[float]158" Width="[float]118" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="f4dc039b2b92408cbf09356335161c02" LabelOwner="[UIModel]2dc7b9f3c95940bb91b287362bbfc0f4" Left="[float]16" Text="[string]Source delay (s)" Top="[float]208" Width="[float]83" xmlns="http://www.ni.com/PanelCommon" />
			</ScreenSurfaceCanvas>
			<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{c49a8444-50b4-4a7e-a53d-5e73bb070843}/Output/measured_value" Height="[float]51" Id="4901c2fdd92b4ad4a9a36063c22048c7" IsLabelBoundToChannel="[bool]False" IsReadOnly="[bool]True" Label="[UIModel]f33d5c10204747279147a06045cd2e96" Left="[float]493" MinHeight="[float]51" TabIndex="[int]0" Top="[float]39" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=7:DigitDisplayType=SignificantDigits:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]220">
				<FontSetting FontFamily="Segoe UI" FontSize="24" Id="f2c809d8ad3f43869ee8e345a1f3d6da" xmlns="http://www.ni.com/PlatformFramework" />
			</ChannelNumericText>
			<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]166" Id="d2232cb87dd84720830e0135c3ded96c" Label="[UIModel]3cdb33d820d44aa0ad712c428546e218" Left="[float]258" Top="[float]94" Width="[float]192">
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{c49a8444-50b4-4a7e-a53d-5e73bb070843}/Configuration/range" Enabled="[bool]True" Height="[float]24" Id="de6253a560d04608b0a896311abd14e9" IsLabelBoundToChannel="[bool]False" Label="[UIModel]e1250ea2c9d840f8949ee7da2af47708" Left="[float]16" TabIndex="[int]0" Top="[float]26" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{c49a8444-50b4-4a7e-a53d-5e73bb070843}/Configuration/resolution_digits" Enabled="[bool]True" Height="[float]24" Id="7084d0498e7946efb05fa45092a5d410" IsLabelBoundToChannel="[bool]False" Label="[UIModel]70b97ed95fd74de5b9a30efa9c9e050c" Left="[float]16" TabIndex="[int]1" Top="[float]76" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
				<Label Height="[float]16" Id="e1250ea2c9d840f8949ee7da2af47708" LabelOwner="[UIModel]de6253a560d04608b0a896311abd14e9" Left="[float]16" Text="[string]Range" Top="[float]6" Width="[float]33" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="70b97ed95fd74de5b9a30efa9c9e050c" LabelOwner="[UIModel]7084d0498e7946efb05fa45092a5d410" Left="[float]16" Text="[string]Resolution (digits)" Top="[float]56" Width="[float]95" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{c49a8444-50b4-4a7e-a53d-5e73bb070843}/Configuration/measurement_type" Enabled="[bool]True" Height="[float]24" Id="6fd9f936e63040ec96c0e5710e08757b" IsLabelBoundToChannel="[bool]False" Label="[UIModel]44ced7f77c9944a98cdf171dc542a45c" Left="[float]15" Top="[float]126" Width="[float]160" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
					<RingSelectorInfo DisplayValue="[string]DC_VOLTS" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]AC_VOLTS" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</ChannelEnumSelector>
				<Label Height="[float]16" Id="44ced7f77c9944a98cdf171dc542a45c" LabelOwner="[UIModel]6fd9f936e63040ec96c0e5710e08757b" Left="[float]15" Text="[string]Measurement type" Top="[float]106" Width="[float]99" xmlns="http://www.ni.com/PanelCommon" />
			</ScreenSurfaceCanvas>
			<Label Height="[float]16" Id="81206002783247279b0d082c08a5de89" LabelOwner="[UIModel]85e66a8c8349409cbc42e5e06bbd5ebf" Left="[float]23" Text="[string]Source configuration" Top="[float]74" Width="[float]110" xmlns="http://www.ni.com/PanelCommon" />
			<Label Height="[float]16" Id="f33d5c10204747279147a06045cd2e96" LabelOwner="[UIModel]4901c2fdd92b4ad4a9a36063c22048c7" Left="[float]493" Text="[string]Measured value" Top="[float]19" Width="[float]84" xmlns="http://www.ni.com/PanelCommon" />
			<Label Height="[float]16" Id="3cdb33d820d44aa0ad712c428546e218" LabelOwner="[UIModel]d2232cb87dd84720830e0135c3ded96c" Left="[float]258" Text="[string]Measurement configuration" Top="[float]74" Width="[float]147" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{c49a8444-50b4-4a7e-a53d-5e73bb070843}/Configuration/input_pin" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="948eb4fbc6d04766ac5be2a1a07069b9" IsLabelBoundToChannel="[bool]False" Label="[UIModel]87be1a245b8f4ef384d82983ff41c5d6" Left="[float]23" SelectedResource="[NI_Core_DataValues_TagRefnum]Pin1" Top="[float]39" Width="[float]192" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
			<Label Height="[float]16" Id="87be1a245b8f4ef384d82983ff41c5d6" LabelOwner="[UIModel]948eb4fbc6d04766ac5be2a1a07069b9" Left="[float]23" Text="[string]Input pin" Top="[float]19" Width="[float]48" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{c49a8444-50b4-4a7e-a53d-5e73bb070843}/Configuration/output_pin" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="afaa9f5fe312425baa7c5555d199620f" IsLabelBoundToChannel="[bool]False" Label="[UIModel]6426d31b9bfe44d1aebcaf7cb24ce04d" Left="[float]258" SelectedResource="[NI_Core_DataValues_TagRefnum]Pin1" Top="[float]39" Width="[float]192" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
			<Label Height="[float]16" Id="6426d31b9bfe44d1aebcaf7cb24ce04d" LabelOwner="[UIModel]afaa9f5fe312425baa7c5555d199620f" Left="[float]258" Text="[string]Output pin" Top="[float]19" Width="[float]58" xmlns="http://www.ni.com/PanelCommon" />
		</ScreenSurface>
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/OutputVoltageMeasurement.pinmap sha256=1d721b311b6586e60f518494c00104159ce7d3b97c3e7f45097a1a99f074abc4 bytes=831 -->
## FILE: examples/output_voltage_measurement/OutputVoltageMeasurement.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/OutputVoltageMeasurement.pinmap`
- sha256: `1d721b311b6586e60f518494c00104159ce7d3b97c3e7f45097a1a99f074abc4`
- bytes: 831

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.6">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="CommonDCPowerChannelGroup" />
		</NIDCPowerInstrument>
		<Instrument name="GPIB0::3::INSTR" instrumentTypeId="VisaDmm">
			<Channel id="0" />
		</Instrument>
	</Instruments>
	<Pins>
		<DUTPin name="InPin" />
		<DUTPin name="OutPin" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="InPin" siteNumber="0" instrument="DCPower1" channel="0" />
		<Connection pin="OutPin" siteNumber="0" instrument="GPIB0::3::INSTR" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/OutputVoltageMeasurement.serviceconfig sha256=861340a3b5275406b313ceb79c5bbe1eb9f56b6bdbb0f982a0e89cd35bba341e bytes=727 -->
## FILE: examples/output_voltage_measurement/OutputVoltageMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/OutputVoltageMeasurement.serviceconfig`
- sha256: `861340a3b5275406b313ceb79c5bbe1eb9f56b6bdbb0f982a0e89cd35bba341e`
- bytes: 727

````json
{
  "services": [
    {
      "displayName": "Output Voltage Measurement (Py)",
      "version": "1.0.0",
      "serviceClass": "ni.examples.OutputVoltageMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "installPath": "install.bat",
      "annotations": {
        "ni/service.description": "Source DC voltage as input with an NI SMU and measure output using NI-VISA DMM and an NI Instrument Simulator v2.0.",
        "ni/service.collection": "NI.Examples",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/OutputVoltageMeasurement.sfp sha256=259b01f089922941a987862917183df18ded7642daa433c28e5703b393f01df3 bytes=15156 -->
## FILE: examples/output_voltage_measurement/OutputVoltageMeasurement.sfp

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/OutputVoltageMeasurement.sfp`
- sha256: `259b01f089922941a987862917183df18ded7642daa433c28e5703b393f01df3`
- bytes: 15156

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="820688F1D047BFF203E9BEB55832B0FFCF3B850E2344033DF551CAB96D56E102D6485C0FA67F3E230C85918675C4373467B36C17CD679EF28ED094CF1A15C473" Timestamp="1DA0CD44EA2E49B" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.10.0.49733" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="9.8.1.49152" />
		<ParsableNamespace AssemblyFileVersion="9.10.0.49733" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="23.8.0.49733" FeatureSetName="UnifiedTask" Name="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" Version="1.0.0.0" />
		<ParsableNamespace AssemblyFileVersion="23.8.0.49733" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.10.0.49733" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.10.0.49733" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.8.0.49733" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="23.8.0.49733" />
	</SourceModelFeatureSet>
	<UnifiedTask Id="c4117d626eb94287a77ae475e30c0013" LayoutInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Layout Information&quot;:{&quot;Sections&quot;:[{&quot;Columns Progressive Count&quot;:1,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Columns&quot;:[{&quot;Containers Progressive Count&quot;:1,&quot;Layout Information Index&quot;:0,&quot;Containers&quot;:[{&quot;Container Model Defition&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Container Assignment State&quot;:&quot;Available&quot;,&quot;Container Identifier&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen_2.task&quot;,&quot;Container Instrument Name&quot;:&quot;Output Voltage Measurement (Py)&quot;,&quot;Layout Information Name&quot;:&quot;Output Voltage Measurement (Py) 1&quot;,&quot;Layout Information Index&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Items&quot;:[{&quot;Identification Number&quot;:4294963201,&quot;Model Definition Type&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Parent Or Group Name&quot;:&quot;Measurements&quot;,&quot;Panel Type&quot;:&quot;Output Voltage Measurement (Py)&quot;,&quot;Layout Information Name&quot;:&quot;ni.examples.OutputVoltageMeasurement_Python&quot;,&quot;Layout Information Index&quot;:0}]}]}]},{&quot;Columns Progressive Count&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationOnly&quot;}]}}" PinAwareInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Selected Sites&quot;:[{&quot;Site Number&quot;:0}]}" xmlns="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" />
	<EnvoyManagerFile Id="ea43d0a4eb56448cb331780823bc7513" xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="1387f606ef984ff99ba90cd4eee0cf07" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<NameScopingEnvoy AutomaticallyResolveUp="True" Id="ae3f896090304055a5fcfab72f5f6809" Name="OutputVoltageMeasurement.sfp" NameTracksFileName="True" />
		<EmbeddedDefinitionReference Id="856c51493dcd4079841c11319ca0b2d1" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="{http\://www.ni.com/InstrumentFramework/ScreenDocument}Screen_2.task">
			<Screen ClientId="{b37d015a-2d50-46d4-886a-f374ede5cee6}" ConfigurationParameters="{&quot;@type&quot;:&quot;type.googleapis.com/ni.measurementlink.measurement.v2.MeasurementConfigurations&quot;,&quot;voltageLevel&quot;:6.0,&quot;voltageLevelRange&quot;:6.0,&quot;currentLimit&quot;:0.01,&quot;currentLimitRange&quot;:0.01,&quot;sourceDelay&quot;:0.0,&quot;inputPin&quot;:&quot;InPin&quot;,&quot;measurementType&quot;:0,&quot;range&quot;:10.0,&quot;resolutionDigits&quot;:3.5,&quot;outputPin&quot;:&quot;OutPin&quot;}" DisplayName="Output Voltage Measurement (Py)" Id="13884f19c874442f8f52de3d21783f78" PanelPresentation="ConfigurationWithVisualization" ServiceClass="ni.examples.OutputVoltageMeasurement_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
				<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]385" Id="8c8c84a9a03549aeb56c79e0f9324bc9" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]736" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
					<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]268" Id="c545e91856f84a3897a0c8b5d1ab4c0a" Label="[UIModel]2aec71eeb9d240bda813ff04d59c1d6f" Left="[float]23" Top="[float]94" Width="[float]192">
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{b37d015a-2d50-46d4-886a-f374ede5cee6}/Configuration/voltage_level" Enabled="[bool]True" Height="[float]24" Id="5a9fe0ffda814a13aaca4c717d20f5a8" IsLabelBoundToChannel="[bool]False" Label="[UIModel]eaaff335fe2041958f1f59f08e7ae346" Left="[float]16" Top="[float]28" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{b37d015a-2d50-46d4-886a-f374ede5cee6}/Configuration/current_limit" Enabled="[bool]True" Height="[float]24" Id="a94fca51c4c54a7394e04d12393ef70f" IsLabelBoundToChannel="[bool]False" Label="[UIModel]6c7b943e697c43629c0862a8e08b7355" Left="[float]16" Top="[float]78" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{b37d015a-2d50-46d4-886a-f374ede5cee6}/Configuration/voltage_level_range" Enabled="[bool]True" Height="[float]24" Id="afc019e106e745c9ac3b1a11fec99090" IsLabelBoundToChannel="[bool]False" Label="[UIModel]ca34e34607734e7b8fc2e6d7d1010058" Left="[float]16" Top="[float]128" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{b37d015a-2d50-46d4-886a-f374ede5cee6}/Configuration/current_limit_range" Enabled="[bool]True" Height="[float]24" Id="bdde2a6fc1da427e8a36ab17de7405b7" IsLabelBoundToChannel="[bool]False" Label="[UIModel]79b7811bb5c0422e9f0c24b9171f2666" Left="[float]16" Top="[float]178" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{b37d015a-2d50-46d4-886a-f374ede5cee6}/Configuration/source_delay" Enabled="[bool]True" Height="[float]24" Id="574c9dc32abd4f6686d4dabd31ce9c4a" IsLabelBoundToChannel="[bool]False" Label="[UIModel]d1202e5cc16f43c893ee78b805b48298" Left="[float]16" Top="[float]228" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
						<Label Height="[float]16" Id="eaaff335fe2041958f1f59f08e7ae346" LabelOwner="[UIModel]5a9fe0ffda814a13aaca4c717d20f5a8" Left="[float]16" Text="[string]Voltage level (V)" Top="[float]8" Width="[float]86" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="6c7b943e697c43629c0862a8e08b7355" LabelOwner="[UIModel]a94fca51c4c54a7394e04d12393ef70f" Left="[float]16" Text="[string]Current limit (A)" Top="[float]58" Width="[float]84" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="ca34e34607734e7b8fc2e6d7d1010058" LabelOwner="[UIModel]afc019e106e745c9ac3b1a11fec99090" Left="[float]16" Text="[string]Voltage level range (V)" Top="[float]108" Width="[float]119" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="79b7811bb5c0422e9f0c24b9171f2666" LabelOwner="[UIModel]bdde2a6fc1da427e8a36ab17de7405b7" Left="[float]16" Text="[string]Current limit range (A)" Top="[float]158" Width="[float]118" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="d1202e5cc16f43c893ee78b805b48298" LabelOwner="[UIModel]574c9dc32abd4f6686d4dabd31ce9c4a" Left="[float]16" Text="[string]Source delay (s)" Top="[float]208" Width="[float]83" xmlns="http://www.ni.com/PanelCommon" />
					</ScreenSurfaceCanvas>
					<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{b37d015a-2d50-46d4-886a-f374ede5cee6}/Output/measured_value" Height="[float]51" Id="691c66bc1381495795c3130a4d519674" IsLabelBoundToChannel="[bool]False" IsReadOnly="[bool]True" Label="[UIModel]340c4bd57f1a46558c58618aa5523016" Left="[float]493" MinHeight="[float]51" TabIndex="[int]0" Top="[float]39" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=7:DigitDisplayType=SignificantDigits:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Double" Width="[float]220">
						<FontSetting FontFamily="Segoe UI" FontSize="24" Id="8baed79f5b3942b196686634260b4036" xmlns="http://www.ni.com/PlatformFramework" />
					</ChannelNumericText>
					<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]166" Id="39f8d514e9c94def99a9b7f26359f52c" Label="[UIModel]287d5cd03b894ca89708d0e6f153044e" Left="[float]258" Top="[float]94" Width="[float]192">
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{b37d015a-2d50-46d4-886a-f374ede5cee6}/Configuration/range" Enabled="[bool]True" Height="[float]24" Id="766c8ff2074c43489fe40083aba35470" IsLabelBoundToChannel="[bool]False" Label="[UIModel]270c2a63d55e4478837632f2869a6a18" Left="[float]16" TabIndex="[int]0" Top="[float]26" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{b37d015a-2d50-46d4-886a-f374ede5cee6}/Configuration/resolution_digits" Enabled="[bool]True" Height="[float]24" Id="716aaa8e0e5b4909a2c6a6867f4532e7" IsLabelBoundToChannel="[bool]False" Label="[UIModel]348bd8afdf9b4a8283bab17b111ca444" Left="[float]16" TabIndex="[int]1" Top="[float]76" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]160" />
						<Label Height="[float]16" Id="270c2a63d55e4478837632f2869a6a18" LabelOwner="[UIModel]766c8ff2074c43489fe40083aba35470" Left="[float]16" Text="[string]Range" Top="[float]6" Width="[float]33" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="348bd8afdf9b4a8283bab17b111ca444" LabelOwner="[UIModel]716aaa8e0e5b4909a2c6a6867f4532e7" Left="[float]16" Text="[string]Resolution (digits)" Top="[float]56" Width="[float]95" xmlns="http://www.ni.com/PanelCommon" />
						<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{b37d015a-2d50-46d4-886a-f374ede5cee6}/Configuration/measurement_type" Enabled="[bool]True" Height="[float]24" Id="f29eed38a1bd4e119dc391338731b1ae" IsLabelBoundToChannel="[bool]False" Label="[UIModel]b56ae2bc804b4c8bbdd8d86af36233e7" Left="[float]15" Top="[float]126" Value="[int]0" Width="[float]160" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
							<RingSelectorInfo DisplayValue="[string]DC_VOLTS" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
							<RingSelectorInfo DisplayValue="[string]AC_VOLTS" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
						</ChannelEnumSelector>
						<Label Height="[float]16" Id="b56ae2bc804b4c8bbdd8d86af36233e7" LabelOwner="[UIModel]f29eed38a1bd4e119dc391338731b1ae" Left="[float]15" Text="[string]Measurement type" Top="[float]106" Width="[float]99" xmlns="http://www.ni.com/PanelCommon" />
					</ScreenSurfaceCanvas>
					<Label Height="[float]16" Id="2aec71eeb9d240bda813ff04d59c1d6f" LabelOwner="[UIModel]c545e91856f84a3897a0c8b5d1ab4c0a" Left="[float]23" Text="[string]Source configuration" Top="[float]74" Width="[float]110" xmlns="http://www.ni.com/PanelCommon" />
					<Label Height="[float]16" Id="340c4bd57f1a46558c58618aa5523016" LabelOwner="[UIModel]691c66bc1381495795c3130a4d519674" Left="[float]493" Text="[string]Measured value" Top="[float]19" Width="[float]84" xmlns="http://www.ni.com/PanelCommon" />
					<Label Height="[float]16" Id="287d5cd03b894ca89708d0e6f153044e" LabelOwner="[UIModel]39f8d514e9c94def99a9b7f26359f52c" Left="[float]258" Text="[string]Measurement configuration" Top="[float]74" Width="[float]147" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{b37d015a-2d50-46d4-886a-f374ede5cee6}/Configuration/input_pin" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="f8606e8f73dc445cafe678eb8ec36d69" IsLabelBoundToChannel="[bool]False" Label="[UIModel]147c56dbcd98421caae9439e650ef006" Left="[float]23" SelectedResource="[NI_Core_DataValues_TagRefnum]Pin1" Top="[float]39" Width="[float]192" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
					<Label Height="[float]16" Id="147c56dbcd98421caae9439e650ef006" LabelOwner="[UIModel]f8606e8f73dc445cafe678eb8ec36d69" Left="[float]23" Text="[string]Input pin" Top="[float]19" Width="[float]48" xmlns="http://www.ni.com/PanelCommon" />
					<ChannelPinSelector AllowUndefinedValues="[bool]True" BaseName="[string]Pin" Channel="[string]{b37d015a-2d50-46d4-886a-f374ede5cee6}/Configuration/output_pin" DataType="[Type]String" Enabled="[bool]True" Height="[float]24" Id="f5f9b8300c424ed7b3f1877f4fd23252" IsLabelBoundToChannel="[bool]False" Label="[UIModel]28a20995854246eb9767d3067bb42193" Left="[float]258" SelectedResource="[NI_Core_DataValues_TagRefnum]Pin1" Top="[float]39" Width="[float]192" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument" />
					<Label Height="[float]16" Id="28a20995854246eb9767d3067bb42193" LabelOwner="[UIModel]f5f9b8300c424ed7b3f1877f4fd23252" Left="[float]258" Text="[string]Output pin" Top="[float]19" Width="[float]58" xmlns="http://www.ni.com/PanelCommon" />
				</ScreenSurface>
			</Screen>
		</EmbeddedDefinitionReference>
	</EnvoyManagerFile>
</SourceFile>
````
