# NI OSS SOURCE SNAPSHOT: measurement-plugin-python

<!--NI_OSS_SNAPSHOT repo=ni/measurement-plugin-python commit=2e57ec3e5bd703abc8690f8a46df62b28f0380e2 -->

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/OutputVoltageMeasurement_example.seq sha256=ad333db6f1645659acdc23c751869ef2db0210fd74afc6cdf18e7d6c1786ac1a bytes=221477 -->
## FILE: examples/output_voltage_measurement/OutputVoltageMeasurement_example.seq

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/OutputVoltageMeasurement_example.seq`
- sha256: `ad333db6f1645659acdc23c751869ef2db0210fd74afc6cdf18e7d6c1786ac1a`
- bytes: 221477

````text
<?xml version="1.0" encoding="UTF-8"?>
<teststandfileheader type='SequenceFile' fileversion='962' productname='TestStand' productversion='2021 SP1 (21.1.0.49154)' compatibleversion='21.0.0.0' buildversion='21.0.0.49156' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.ni.com/TestStand/21.0.0/SequenceFile">
	<typelist>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='2'>
			<Expression classname='ExprValue' isroottypedef='true' typecategory='3' timestamp='1650060499' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436'>
				<value/>
			</Expression>
		</typedef>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='3'>
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
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='1'>
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
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='15'>
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
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='16'>
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
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='17'>
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
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='18'>
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
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='19'>
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
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='20'>
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
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='21'>
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
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='22'>
			<NoneStepAdditions classname='NoneModule' isroottypedef='true' typecategory='3' timestamp='1650060850' typeversion='21.0.0.49156' typelastmodversion='21.1.0.49154' typeminprodversion='21.0.0.0' typeflags='33554436' valueflags='24'/>
		</typedef>
		<protected>E@=3HJL4100hYLEDF=_K@0@mKCYo_1KN&lt;&lt;DO2a9hF9[gHbDhFDfRINZfQ01CgaQ]7^^LIOOI2PDL[f:5OYN&lt;MkcfEfH=McTQQ7Q6:jTo`PP4d\AQ8^;P=E8d=8344V5&gt;ZY2S7DRQ;bCY4Z:C0Q;N?R?;g&lt;U_W6\fjf=VMY&gt;ZlimFH1DL&gt;c&lt;U07Lb_D8e0P5QAb:LOfWoDTjRGhA8k60;2T_a1F&gt;0GRL`839BT@TX4TTkTGICBkhfL\Cl_[[fa85iQSb[CP&gt;6W39S;;4&lt;Z:`KNEiAI]=7Fe5FcTkNS_`EiGL0@cX[8a@Hb&gt;FGo^`bEjSJZVimUoI_7niNP?_H=5KPJja=M3ocoT7O028F&lt;0nDm?aQnZK^lmNc_9aenRSILgUHLoDJGiAj]4]47C[&gt;?]BXNSL@^g^HhFBoJKRR8mTU3J]7iX@JF`5lbG[XbZfjfRaY=^\15EESPZUFQ?k&gt;UMX@D&lt;oDf9im6OMdgC?1]E0o\jfJ\e`l`QdSfBkmkmFBA2g5iLUo;X:dRHo[&lt;fKakfm^06akNF8N:hbb9ZcS:YMS0J2M65TeO7g;EL&gt;6F\VnT@_UNKXd]k^MebbnYZaogjJ&gt;Kk6FldcUR@VojQdKMh9mFNeS^o[dEcoo:MZdBSd_515?I\UE0U</protected>
		<protected>E@=3HJB4110h]L]MDk_K3gBocK7LAg@bF0m7:L\7mUH^jTPf8UWji4?JObL37e`G1BU_]bJEEgG9OLd39Oi??^9QJSUTD=2428\B0kcT_7T&lt;Q@obH[[G3o^A&lt;D=J_&gt;g1Hi&lt;R`WmR7Y7K&gt;c7;g@f3WI&gt;MaH=lc7S9&gt;c?IG77K\]]6niUiBAL4CCDj_[5AJfWkomR_OoKJmJZM?&lt;_&gt;RAC]I2d0NnLHDh&gt;Dli&gt;23CM5CXi6DO^g`LX&lt;Q2hSHndMR7[D8BMh8aJ7oQSA@fKWPh;Dm5&gt;RW9o]Rgj]F^W_JkHFKk?2&gt;8;5iifgAJkk=k]f8VDCi5;PF:WC?2M3dfNg9]a`emUH&lt;]ARooBLZ\:kUkkkmM^^JNW]&lt;NnTH6CHD=O&lt;CnhJlmQofSFkfEjh@ieJUOMMcmjnCefg7V7?Xm9cm_&lt;Wdg_V^o&gt;?7MdoPMGoO7O=nSWoc&gt;?_0???^noY[5okoUi;jm[CJNcTRIa9LFghA]IUYogjAmD=E2g9LjP\18G&gt;^L8H?fVPaSb4;AY3MfSSfTnObfKMH:elG9n]JhTESCJ&gt;_2@eOaCj9C4[mKM_1Ol[?o3MXBU5Uhe2JgJgK6Ao[N@8&gt;CK7oMM&gt;d1fSh2mgU9agAWIkWM^WaPP_6iL;hT[G`GXJl5QoXOL?T&gt;7gkG3co15h@^dNNLM=dokeOhb_B6US2oHMBN?_o63;Z;k;oSc1WCoeRJYIVlYJMLK@Q]fcEFNlW1[n[]eJHIJ93fIC7`5FQ9G&lt;iN=R;W&lt;9jh&lt;ZQ3fLS[:=SBo3]U:mdP?o&gt;i_LI7AlUlLj;^:6A1VJJ6DF`QT8_lej9`I;\i&gt;0@HG5j&gt;AoPRDgQOk9:b]jeEd:o^;kXgDTn\D2TC&gt;Mbo4=MFgAJ61[EdIFAFCB9GFD^E;Ua_m^Q@C7\^2]AMnH&lt;URI4liRYTNnH&gt;U=HSdP436l=_`d2E3fRBnl2H=^g7ghj_KkeQh`2^NgI4`L1:Z]oTjc^EW40R1=^Z&lt;BRQiPPUCjHh=oG1hVJ3Rf&lt;e\mS0R&lt;FCDideh:lZib5&lt;F;LUceKYR9?WUXDZb[JgC&lt;m7RGZV\ACPlWMI7QbXl:16fCSPj26SfbGYhgn1:O7N]o]_eV[ka:KodOC@EZ6a]4lU3&lt;MXIBQFEYjbT&lt;Veo1:n@_dXfB`=bT@el2cWU9GWT\B=UmE2GUoHo7gg_g1nlnNlj^WmomjBoMlgWod]k_^?kLG2TM9cLbb&lt;V1^_7^g9C3jOb9XSnC6kDSkf3h&gt;25Th=&gt;cRSjR6KHHJ=9ChVO7jCE7jhEWcCjLM__eJh11VV=VN:?;EPeRjZ\SLGUWd83;LRM6^2&lt;]CNb=oQ9_d^hlRnNNhL&lt;7IgIJ59Z&lt;o4T[mKJV3kQ]18ISO&gt;];XLBEdGQYJofOmBD&lt;AXA9M9;Wd=?ZZZHg=5BO8hYk=fd9PC@7&gt;[JQYl]G]^o^2WKJ3ojnfD3Q@h4D7]F801DhI7;k:Db[mf5ZRQ@d][PKaB5:@PkaBfWbW9O0HEl8BDiW[4UE\]A_5V]N1b1:LLQEH[Qc0hYAS0AJ;B&gt;@cdkY6`=;;H=ED4\DUS@gg0V]XQD39NjY&gt;f3N&gt;K4DMP\8YVbTc3iU3SOC@YI3kMQ[If=`N[i=j4\DWZ?FKV`fRT5&gt;b3iVYUdJ71a0e&gt;:hXWdEmLk^^ddLd7?YM492MFBPj^RHWoXY`d2lJoElC[Z4U6WjF:PEjZLA6QKSk5NY88@@XGEHK6G;^dVj@co]T3j1l8TXnI8:VAeNDXI@D9M@@8JBlGDAT6RSUMJFZ;n;8kO4\ZH&gt;42G7A:NPT9h3n?=9BdEf[bBW1[_f07NGhgE]NN[;F7cEe&gt;953\KklXhKFfmEH;XaceCUjeG[HHb`ZVLUULdi&lt;A]&lt;ild:aVc\ibmbUF=:0e;f[ZB64C7Yj5;3efQ75mDBU1DcG8BZad1=hNQY^af&lt;UVo:ZVf^@0d_M5ObRQ2PIHR9bbbG][HZ\KEfEYI=E];E@9j1kZ@2@FIkf9:\CYe5KNCANXH7R@eMa2M;Pm]PZG]@4h2Q7OY:5QFk@\Y6]E6X1bL6mjS77a`ZS=H=XQReG6Djb7[c&lt;h@S9UC[4`ABLQ4:ZZ7=JF9JejC5\[T:meE5[[:`Qm=DfI0EDQLRJ2o]Q@o1FhU9oA7hi??EPmHoZhA11dfjSE;aYISGCSD5ChjcQWk3eLIH6mg&gt;X_6k5ScmijD1:\]6jkV2OHJBbHXFV=RIibbaX5_jV^PSGHFK901\5D;@f@6aV4ecHA\_8c:5JUTf]RP@dJaD^Q5mgghUa4?dKcBOP@BIh4J:;?4:=heLolo&gt;mDcPFYYaJPQaC[DhBcm779BiUBG9?=Vh8ZHhd\hCK[N:SkYicVdi1R61k0=7foTQ=o\]_U7W8elK:MO6dhEY@1n[N=_SRI\X4TP[7IMJY1H&lt;`fko@8PLGC9`2H:i9H7JiPYI6B8Y5K0A8`C6H&lt;d34UZo2O&lt;&lt;1H54JTEA34`dBGbMV:0;VGY0@2_DQP880H7RKdi:03?e02&gt;e5lie\01lU`@;4&lt;5PTQN0G1^kP]G`N@IEMe=:ViEY3fZ=E\:]UCB^LAFb?Xe\A9McEBQ=c:Lj1eMiR[5En:neQe0fZdUOCZiF1B:T0gdc^ohlH[d8ARdJXR9kOcAdkTAXl66\A2Qe]nL=T4N5j&gt;DDaKH[R:VORK22O6Q4dLSB0iOEBb@g_[`]9ViUnT0jMin6j[FBoSc?NFn4^XVjanK=\7=6AeK[:f1;YaYG&lt;QIF_KZ=@h@h3]S2RVCMn26J&lt;V2&gt;?Ca`87g?a8OlI4CE8&lt;iOUmV6VH=o`amSW&gt;YiAKgn4hcmGPhPi1ACEUc`B_[k=agB09FNl`nC\eQBE_Mo4Jlho6ml^NcoYU&lt;lP`R\I9f06jOViFeZJ5@_44Tb6[Ya\I4G0okM_QO&gt;RDCHhb@kYI_cGZ\FL`^78QjN7?dIE8V9K\FTbDh]\;@iNFF?&gt;KQB=CSdR=TBfan9K]LIJjSeK:;=7naRo93XhAO`fS8R950ogH[BPdh]ohPRk&lt;1_eLkXZjAfU[@TFcOkIQlbQlnjd_&gt;h&gt;7Kl1=ibmRZM6^AX1EnCR=W61Lgd&gt;3LW49RLl?3n^Z6Yg&lt;[7[A3iIQWhVbIF5U5n6@Po=c;S&lt;WOj_=:B@S;De=m9c^PBaT6HnUHRU]@SZcc6n6I_`LIRaGBYab3@[`9Kg1@TcFH7^=?2Z`?8a3oA47&lt;dFVS65TW]CP67?CMe`i2lW\3fQRB:N\jIfSjKIQ@A42Z`Lf2iGJCU:[T0V:\2H?5DVWg[7XVM4HcF0iEAaeaF]G=d595=n4X&lt;2\&gt;KjSDC]CDY;Cm3YACED]C&lt;][dhSkmP&gt;^AAkJLT&gt;3GOm3VjS`D4PkCnSg?HfdN_@25I4AmBU3H5a[c8hY8h&lt;&lt;m9Bo?M^:9;j[EOU47fABBC@\on6mZ0F;E5TAH:4gfMo?mMQXa5@RLeF0k^d:8Tb66&lt;j6&lt;&lt;e0AMKoN:V8`dU3=&lt;P2iElNOQXZcnhmB&gt;4g5h@nJgDj&lt;S9@KHf9IJ:2N3RYKO7bfH=J\bBb0W8lDCf41\_hQ;Q@Y3=IPO:4IUaKK[P:2c8A&lt;7I\j&gt;S7nF5iMK1ALc6ERR15XHY8gbdhMUh5&gt;BFKL:^l@5LL@B[:2GlB8oRgi^]8h;l2m`:&gt;QG3@LSVEbn4YFUE5Qn\M=&lt;3YoY;f61;N6N966Tmg2lg[2^_JUeEC\JO`KoOh207^MlX871jfcBGKW5cLE7^WB&gt;2d6Da]Z&gt;a[ETS1233XEL6@AVTl`RiIR?3X3iX6H?nYfJ;:YAj;fYnIV]P=Q3??IgPJD[UP8bk1NhRP0CNEo4kT[P13:?X8d6j87jQh2RS]E\d02go;UW9D9R:7eRej4SRek0NRG8NLZ;gkLcQ8LE0aUNTd:K4XE?1d;ZS`LkSZj019Yn0n6eI1Le8jnHGlRA^6AajoXj:FFEC0eCTAi^0S[b2iT=dE[:c\JN:`2aZPb`F5QYZaiLN5iS\[CWjFNcjfLe`WZOFJk^WB_]7i[?GIk&gt;gJcF^NKd0mWfkIZ5=01`jg=Z09l\n?PNdd1H;6QlMKITgFS3d4eQK42h4`&gt;n_?VZ01SiSfGa7VG_AbbI[5Q6iAD2L\5Qh;LPoOiPZ9mTmEIDGn7;aTNi`anFZNL22`NSZ?JK[W2c0K55&lt;f[dBH\ZSCYAZMVV&gt;Fc0G2QAadLH^I0omB0f&lt;;kR&gt;1Im9Al:D@9^G;FJeU?m]DPloDimg]IkOfoToUbfoWP]o1I1_7hD5n:P2OUXDD4XmAGec=Ke]KXCHj8HFoUO4WPhHoB;fOZf[nmo\]JNlfngek@12MQn[i[N3fbkJCR[\D8nDI@DTc?FO\I;jNB_e]U_lfj]A@PkkIKEQf_JmK\UN_fb2g]E`EOojfbg&lt;dGnMI`5j5bn\a7;\bk7O\X:X6^&lt;3SEf`Y2Kh?ZGi?b?6GlAc1\kJd1=OVIhX2=_OD:JJXFd\DEf&gt;K=R]:HXYF=Vna\ofnXFKmj06nM`bYhPNm4P\@MnDRPO&gt;a@]W8m4WPFXYQ6?@_Oa_X[&lt;oI[[;[EmE[OO@_OaU`JP3OaH`\S6VbcS`f=3jk61hN4WSiJBUnQPbO`PLhIg&lt;&lt;\K&lt;6f=&gt;3k6B1=F`f=3ik61[fHI3g&lt;\0K6&lt;&gt;Gk6W1m3G00NUnQPcO`@gX9kV61U&lt;?\K&lt;6f=Y3]\LLHg0&lt;d3inBX[omcDFSKG1_om2NiN[_l_UiJ5k_C?Bf&gt;GKkWF]IZ;N:FdNi[_O[dJVjojPMgbf=37][?nYbcjfLehW\mNW]iJZU]7mW]Si\GfJcJW=UO9`@oWmUO&gt;`HbA_HDLeWcWoQ0ol65dCg92:J9[6&gt;anhd`^i8eC^Si;jk8\WKnm\^f&lt;&gt;hKLnfjoM&gt;1M1ITWINdoA&lt;1GehUhLoN4&gt;^_Gnni@7eUgoijKjHomijTdWR`1^b66?&gt;hX\TlGm:oIl=ooOU2hW9oW&gt;?f;kRDR3FGAJT`e]DYQFRIiCGL\WId6l&gt;QS[Yd?a;KR@^6CgE_XBj=\9;bfa&lt;1Ag\dGmAAQ`BhYO6^XWHZfPXJIiHRfBRONB7IFDhA?RgAf0_D8i&lt;BO?AL@54GF@]WL@^=f2^P^noWPaK9GhlJR^NdC:0&gt;YMAGEWX?n:lh@eLhY9aShVbImK7b?W=@;k[1NMR?D9\IQi7VfXjYY?O;QL]m0_;lC2UfU[PCTLEmCMG:TXg0WW9KGKB&lt;9;0o94HSIB?8aT:a[F7L`iQ_J4E[djh`gdWdHJNU5`6W8SahGV1XgjA\ahC4UN1jdFYoXS]?SnjbH7Uh:UYn9DUj1TZ[NeZbV2OXWogLN90ol75l&gt;N5m5K5@&gt;PP[IA2&lt;KjdQoLl55XA[IU?6&gt;ebd`Pm:F3gJgKbk_Mm^HNW=Qof5XgC^gf8@c2LRA83\HT0c6B0&lt;]d@5Lj0R9QV825WB9S9H8@A9Dn86:MBQT6d1M3PT&gt;=141dA2]bi:S&lt;;BQ349dMiQ4@8;83TPa;SoD&lt;1oT2Q2E1mdAAnPC062ofX3CjD=910iMZPh&lt;4=RL1_H40gTCj=2DeZPCe4bL;`ihePi@BNRH0&gt;97F7B@&gt;`2A7Ol=3jf?`T64&lt;]372]T0HKCIh=l1Z311eJh3JIHJ10RcA0@a8YbQ`I3i4&lt;XS]GS@T&lt;Q3b2210`60OCS\P9SAQd1=`bV5E2ODdA_LZBlhFU6a&lt;5X3=0LCB7G62`0`@\j@0FUT654AOa0Q^84=FPEH&lt;PZ405fV`_8B=a4ZU084DC`P:I&gt;:56PIXP?&lt;T6&lt;S7iAZ6K8AmCV?6@6ZG8XHaXB6C09X0P8I6R6U@D2oi]MFf[oa3kiKIjfa26SG&lt;dQ7U:j:lXT96N4R;;84RI?K0R5@K7fXR=HXA&lt;C20W2?m1ODF^X4&lt;Y9a38]J6OdHNWFE6LkiTZ7Hfo^3BbMN__fFf9\17&gt;NBd&gt;NEefg\[2E]OA\Q=RcDhnQM2BE3A4=Q8gLRfRcG@ZQB_&lt;&gt;BZ2W1dg`C0CL&lt;1AoRF95DM5k47VKAR`]EPC\o;hP0UHc96&gt;KjZMdBDNb:DO_1djJ1YoE1Ym@LIW\TUT3F5kcP\@J0llY1kgYEbTBbS&lt;AjTPTa1I9hhH:ChbBe`@TP=]OgIA8ee&gt;1F:_]3emkNHSX_IZ4]SaQd7JbH8?hF:_[ACM\3dnCSXj&gt;SXl9FXnKWc8Sj0S;QB]6bA&gt;_gfI5_jK:SLHjR7Ce&gt;fR5C7B1WM65G14a4I4P1XP0\BD0VAHS`4JUaFXQib]AHR=BI[DH\S4J4UK6H692?&gt;1cTW1@[m;Q5Mc&lt;P6LAN8V_&gt;Q9Pn?8`3i@`E1dH;X=7oi8SVSBjCVAcER]FbFQSb:Uaka\8cj?CglAS:METE^3oi6O;=BeIcIJBLn:jTW8@U3E4KAmTFHi[1[h[S&gt;CU9MEPEJ:eG8nCHJ@UD\&lt;8EPQAT3STPhHN9BS4c38V0g&gt;3QS9oAAPOX4PGNa\CX1j0:XGecJNJ9:QBCPL&lt;R6i;`PbiKBVD`8dQ]K\Xd=TbF0\=IXXE3Ae9hV4oHaFhSAa7dimONCT;C8_B:m;BISA&gt;A=cJ`WfEVSKacF;jP4i8ND\YclI^B]5`H2e&lt;foFg8LD7;jnW:X:L?iW?ZHL2VV8XdLZCRbR7bjhL9W;CbRf]mWbFJ8aiAmg&lt;_?cD8EnPl0V`[a0JTGL;BR15[Q]WC;g2Y:YlTdmcmdSWBhd1\g3E4&lt;D&gt;PfYDY4cBbke[[PZ1P`_B=mIk&lt;VW87&lt;^H6GGTL:Yc_K5UB4UMigYI5T;TA;UV6HK\aGTc`Adi=mjokh\R`]</protected>
		<protected>E@=3BJiO100h]L]MGkcK3fBoaKgcnO1C[KY_3VgFg3f\:dbWRb]W]ja3ZeDT&gt;gG&lt;F3C`h&lt;FRIEB:dR&gt;oal1lR8P`R;7UdVj]0WcI1;0g&lt;G02gHM\_?LJaZU?0;bU&gt;?K&gt;mo9iW:SW4SQU`7k?R&gt;OCUM]W&lt;jeB0_&lt;LPOEolh&gt;\=nNYf_\cHOnG4WQd6UA`SLO_Ad?fO&gt;njZG]]_]Neo`^=LRZTLTT5MG&gt;RnKeM2h&gt;L8iUjM&gt;8RC2OMoIfR2X&lt;C_Lka@&gt;B]G96ESU?&gt;o2XYIhW38;liQ9CWZnPo?&gt;KMefNkmo`5lF^ST9RZ7HULfI]cIoi@K&gt;L&lt;a3YOo;ZgDOf&gt;hfcFAc_HL4EFmLci?Ggf3&gt;&gt;foggfacn]leXS49aC0bmIFlclng=o=V]&gt;_kmhdVblRiH=4n&lt;n=l&lt;lnghEb_jco^\QknmkMQFgm8mGNnb:Ale;FNmHYmlooibXo[_JhdiOHNmn;LMfCJU=VL9lYlWUS;ho\mEk8WaK@i;f13GQ6dgBMD6\2\7O2GA9AIOfSfo7oNGI^laUnL0cjRg&gt;`?6im]Q34Hi1?MI0:Udgjk7MPSGM9j`5EI87&gt;WbVf5X\`Zob5B5QoWUnMNgXBWkV\CWVj;XX?hX^Jg?&gt;Z:ASVm8O8jiUbah9onn\n=Xl2oI&lt;]6GGomAM]Hne?gigOX`\_OKE_Jc1mh\f8hJ&lt;K_^_]^kGW3WohXebO25P[dTAoQ6]g1Ijc9e]ikO]lLBJNd04EQIE^MjQlkChJaR4&gt;]?hVjVSSej@&lt;Zi;KLZL?71d=gWMd`HE`gG;cOSa=T&lt;5k;9b:bL6[QoN9&lt;VkPYdI=8[EP3[B2\ie9]f&gt;LF&lt;[J^eL_CkVen7&gt;5Ba[UQ5WE&gt;`:o6;k8hWPIej\\[Z9i[;8_Z:U&gt;V`O=f897RGQXFMNSRB98&lt;Nm93YWU?cUk34&lt;jI21Bg5In^6F:[CWNP&gt;EY=mP^fdM;8B;XRWR8IN3BIhAK3?fFC2g0k2=^YUT1QDaWN@WlFS9mdce0D^GmJQ[ga4CM7:5hEB&gt;a\FKY6[O[i&gt;6`0b^]ZjAaTl1e[IXG@MH[ah7O\kgbQbH?N_l]WmnGWk9omP4&gt;G68d:7IJ`b=c2h9lIbBKE:;]Fl@L1k;:[M&lt;aAM9aaHKGeC5n4`m;INon][Kk^WQ&lt;_On0OMn_nnhk^knnK_oWk`jDm9W`bIJA&gt;UVB^HHWa[9nDXcORQhdL9LG^L?n3TJ6T\`hkii?McS5;FcgRTeMGQdcYCin&lt;YfAONf:&gt;jbo08@ZVKTn_7hA69mF6D[acNhIR[7AlbWDf]8GD^ekBM^E^hmiGO&lt;J^7WB_V3VkLSP0Nc?aUnWfg4L98VM25HnBlbTVTUG=H6JOLWP\dG2JRY=HilehI74eKg&gt;PmeQCiRh30=h9L4I9lkJ5LH3&gt;=kLaY5?o]bAnGC9XYPj`IhD;67BNM[gAL9R8dh=Rck9B9Wmieb_^Y4Yn6_A9GYK1]7e4cEcW200EnSXZLco2:^mJ?IlMQ_`iQ]M6d\ZKK\DQ&gt;JQCc2Fh&gt;iXJcVDF;j8EKT1TbMmGihOXU0EGhF:]`G`FjW[HhPSiZE_Z?hYXGnmF62^=hn`MBjMJ1fDZgZ`EWO5cLkSb6mEX6YMY=JA4LdWbBN4I]=dgc_ONh&gt;dC_YM492mEBR&gt;KSHYOd=CV1Og::N3eER0;N8ELWdGZe1VFc=eAlQ5R0:MLER&lt;HO\TbAa1mRh?IdWA4^7g96EX&lt;I:C&lt;33OHY8NPB`ZHX90`LKjUfcYLOkADaHV&lt;;L?PdTmPT1[&gt;?gjhnME:GQU[Zi\edCN_PWUj[jX`]_=N?EViO]?2QDk1W?V8W_FJ23HS1YI_`H9V:3&gt;cS\gTT:U;YW5HTM]bOmnCWe7k`JYZeRUS[YVmaDHBLLEeNfde;U6C8gZ7T]b&gt;N9bkCI;bS@gZXPNTZH?:4cnB&lt;]5D`0ZJUJUT^cTc&lt;JF][dO=IFL@KbEEB^R0VT\X5VH^b:E;K?\aGB3dJg5_D3WWaE4b?&lt;PYEk047iaD[=]k4ZS_]=QRbHK=F;g8lmAXF&gt;QmESVhD&lt;iF8&gt;eoTUU6S5B:b506cU913NBHoJ_0G_&gt;UPUHFfoLL0[4K^Mb[VlBEM?9Vl5G&gt;RbhcB49^QWD&gt;2n?Wok?8G9nTA;9]TYFRN54@Oh`VeQDa2gVcPj:kTCM5EcPgoJk^&gt;]neYg4&lt;_I&gt;=LO9ZlU4\=CgOZRJKfl[J833OjRn@4g5J]374ZRGK038Vn5jf]9M_moj6g`]:&lt;F34bNeja&lt;oVgnmC89?NiQHToa:Ub8H2]l;@^Ro&lt;gXiokCnO7UoU52Z5V^CAH&lt;`&lt;LVM&lt;U;@NUe]LSUcXjRHj3eO?WMTDl;TJbC_;`P8G=&lt;ZZ22cDC;&lt;bf=0lOCKo7iALI1PiZ[0oW?XZ0Cf0Fajb&lt;3;di\Fg1HVR6VX:@c:F&gt;a?&gt;3PhKfRd8BgYhRQRV&lt;V1H7A`da05dXR1E\ADe6A`L`odU&lt;jQ2M\\f1;Rc`15VHQ8MT`hUZ&gt;L:D8O6D`obe1&gt;7kP@3]a6d16Lj15VeMhAN`1GWcF3eiE;FWNjPdc;g==J=eeOI;H8dceE=&lt;=Z=UYObfGLdbK9]Xdnfg]85hCW^lDm8YFG@Pg[Tii?UGMVBiH^@a2^hN3J7VWD?&lt;g4fVA_2DUEf_R@bIjMCF^HS\iUJb]T64JJ7^m0g5i1VEb9HgAldSV_iUTk@nig16kZFACb[_F]1;DGcMOX&gt;WSJFSjB=eKoQD4gBA4^^&lt;V@VkN[6:;[98UJ&lt;WXTaV8i]S4Olj0Tk7BdTY5_8kAN[U4l5bgW1_57a[od&gt;;N0_lOAINdAaDD`5JjmKJY1\lH96o72R3YfJ85i_lP7JnZgCin?XiVD:61bJAA\THP`K_ce[Jg9RX?:2fI[Ed4N:V=JOL=l9?GaJ=&lt;SKJ?nf[2TJHeQL5QD4^W43CfV:MBPJU57e9[ERb5_EecH6hDa4TMIS5\]mO@=KWQ]mEJQUUFROj9akhn5:LQ2MYd&lt;0a?Bk]NXFT5QOlJ2i8LIkO&lt;1gbf9E:Rd]K_J:F&gt;Do&gt;nKj^TNPK?TQ4&gt;o^N=U246SQeMCjB8D9;gVTcJ_REY2nL@KZL:TngB8iLOKe:Mh=b\&gt;Y:;^0jMJiMhliFIJDANdHPecLg\Ve76bL@[VLJd5EZRCen@_djBCkP\F586bl@8M]Zf28DU?c6aXB;`3jW&lt;gQge21C3dMHP4YIKWD1O2emO]_A45Nf?TEBB`;_Ll?O&lt;X3LBjB39?C=8QJZO9Q5dATCl8ZTTWmK6_9X6hHcXWX0D5WDM0fcU2Le8`A5k3Lf7RYPWlXCVDV7R_WZJQVHFmY9fBkXmUg7YHcb7VlP6_K[Q928gWWlN7mBCHkm&gt;]]80ddI&lt;BRI_b?PS43aH46^T55LeE&lt;&gt;^TG1J?NI=F8&lt;Yomhl@hKmRZZ&lt;BPYle4clb_G[k144=hN6h]iZ6S8&lt;2=H=3iI0EAMo^O:9K8d3F=\235EIfOQZScnmZB&gt;dA5h11Fgj`:R@SKh9H5J0o?1DL;&gt;44k\=@f5iT4CAb:9C&gt;`AlND&lt;BTY0IhQo:2b[_&lt;gFD45W2Q\7ZVj&gt;7&lt;1EiDCKADMcELR@1?D&gt;QS[LiEF9cPSTfHGRbL&lt;QHYl4@d`JIhiG^`7eAFo5h&lt;O7XfdB25CjBc&gt;f5XZT8nFGig&lt;@bECNSMHLQUHMP4X^_h\_^iD^IcAo=YU5ddm?g?&lt;ZB5U?d4I@o7[m?=]&lt;MVCJEH=TeeD\?^C9g8R;d&gt;H6IiPFH=c][&lt;ZB[hjDbFB_957AN]_Y@;LmlTJJLoNJh0bd1_oGRAHQ=kBGkh192G2Emo\9;b`C9J&gt;Id:FX8XjH3JV]]jHQ=`N\FDOBTP&gt;Mf]:j\m7Zd=P=^69k;9`Mcl3diU^SJVTXE&gt;fBZ&lt;NDFdEPe6ZFGhL9YHna62=1NAeVn]ehPiA6a7ohBYm9FVD0giCam0^W;RIL:n1Ze90k69f&lt;`XLXZJ\abmD4Jk9RlbFcI^C6NN[\ij6N[?lHHKcEji6N[k\i6WN[\^i6NhKdm97K\fEV8GPdjl6E29IbWka2fB1D5]AjIgEVF?C34MeQ5F0lH7FO5&gt;cm2KAT]k5b9iEkadMUD:ITV_\4F4TIF?4U9C7cfdBAGL;UK8]KGoH3gEHdc9:ST@2nKHNN2`iK[7:REBIhOAGgCPVk]B3]Fi16P`C\?P\\@WW1j7L;aYm5E&gt;9C\69MO0neG=gjA[JCl2clGo&gt;mKoQPMneg_Jo]F3Do?bN&gt;;&gt;oONd^N?:V[:haSC0]ZUk?Oc?oOBfOg5g`5Q[gCCa3^DNjDFD:G5aBhEU6UEM\X;Q^c\06NWfXZ27nVi[2T[gQM5]kTNQ@TEfIhV`8GaE&lt;mADXI1jNWUaK9CA5L=0k?C3V=kSDV&gt;^T6;]4L79;oA`U`Z5l5k0GAmJ0=MH2egZ8k1nVnOd1]TlRaIWkjH8Y1hEgFNXMUm_YbSgFaP&gt;D6&gt;]M;VB]O[QMd;h_\6Hg5oYV`UbDNH^U[UA?oG7hKVBNFJC25kHEhY:^ZNQY;U2ek8gCT\7]Yf&lt;54oL2&lt;aTU74Wi2b&gt;7cDc&gt;?keFDiTZ?6n3P1?o;c?21XS4nZgHmAk]lPS]?PgCi:e?C9G:BmkVD^EcC5?BM`V^h5&lt;M;389SOTH1k7V9R;5ch_70;9objaU\H^ZM^kW6@&lt;7TZZOWBWn&lt;5c@QXJgY0D:nEoBJRWKD@&gt;XVO\U2nW=iH&lt;mLogXf`g_IafSW:A926DN2R:I0@=\`7?0d858eT06h2Ta6jXHAJBQT2U;\`A5Z8QA:=@T:TI2mm1&lt;nTQ8LBd]S`LN8&lt;9ZTdfc10P@AfE83FC64IZ210IU21W0&lt;A:o:YP3aodV`Od=`P8POJahNPBHDX1N;06?ZL4XPl0e@l\0l:dL&gt;mj8&gt;B374D_a1X&lt;X69N7VHU3b@RO?7nRHQD`@0Q&gt;JkBS3kEA_U?XH660WS4210`XJ3JP=JRR4WWa4BD0WmZ&lt;Oa\4&gt;0S4A0Q&lt;iF86PY4ST&lt;c1aZ@Q5Q9aVX1HmY1I3C&gt;3n2P&lt;62JjY3Dg1h@PXG:C0;&lt;FK2d1J\2@]0b80&gt;c562T2@D&gt;3nFQHE;Rh::HDa5_YHQEC`XP:1ZG5Q&lt;D8HD@SH:h\K88k0ab^4R9VQ=H\0V4018FNR54\AOBFhNa4D:XRU_538ZFP7&lt;ZhP8_Ae06R6l@=PRl6X@\5^SSH@ZnMml`dR`Bl5636jEA[P5:&lt;0G:;:TneHK&gt;N5kQiHTOjHIN[_aPh&gt;N\@XN_mX^f]E5CKm6Zce:l2AmS399@g58P@a?QgL5lQ`cm2JHTTUR8IIKM864C_k&lt;BC`a1@[dE;Pgki5CC6^0Zf\C?\Ah9`BJIYFEVY=XT4cY\]BXbEIDo:T96jiC\:;BjS;a]E@XXRTZL7BV&lt;mBPFO8A6DYA:?9WYTPIX@F9R@e^EgDY]?[U1lZOFA[KdWHSV]&lt;GfMXMeHH;46Uj_SbEHdjTO6[lG5MZQRf[mAnUk&gt;@6VQY:]:[4cXfG2h_ab^Eb9T6i;RRARUkHKn8N6ZZB=&gt;QlO34A47@S0e0SW=AB2HU=CARD5g69HSDdE69SQDd6j9F5JAR1?n8lMi03e_jh:WTnW`[oLdoJPb:nf_5\d10&gt;E@R@8F?;Q8_7WU&lt;=&gt;RQ3UeiKX7]Z^?5kccV[KoGViG=lC6U]a]`hZ@c?TPI\d77iMcidQ]:PPX:DfW;Co:KkH0Vi5]D?IM:X0YETom=[F5N`2aQ@TS6?V=APERT0P&lt;F;=3\h3B26&gt;@lRj1m0P@Gh0JZ0BM@&lt;e;JSU?Mh@`Uh7:V3RLQ`J&lt;1C0Yeb&gt;[8g4oNcP5:D@I3]ReZN:Vm^58LW@1;523mMi^e`9_@NHTgH=U7EKif3YT_Q6_70lmTk_NmVW]li?e]2M`gJ&gt;UUlB&lt;LFOdoQjgid]hGR9lWYMfDo=1g2X7l</protected>
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='11'>
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
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='12'>
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
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='13'>
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
		<typedef alwayssavetype='false' additionaltypeflags='0' typelistordernum='14'>
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
											<Step typename='NI_Measurement' xsi:type='NI_Measurement' name='Output voltage test'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:lSaDme0m7hG/g0xEW1VriB</value>
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
																<value>ni.examples.OutputVoltageMeasurement_Python</value>
															</Name>
															<Parameters classname='Objs'>
																<value lbound='[0]' ubound='[10]'>
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
																					<value>voltage_level</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>6</value>
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
																					<value>voltage_level_range</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>6</value>
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
																					<value>current_limit</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>0.01</value>
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
																					<value>current_limit_range</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>0.01</value>
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
																					<value>source_delay</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>0</value>
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
																	<value>
																		<Obj typename='NI_MeasurementParameter' name=''>
																			<subprops>
																				<MessageType classname='Str'>
																					<value/>
																				</MessageType>
																				<Name classname='Str'>
																					<value>input_pin</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>"InPin"</value>
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
																					<value representation='Int64'>6</value>
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
																					<value representation='Int64'>7</value>
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
																					<value representation='Int64'>9</value>
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
																					<value>output_pin</value>
																				</Name>
																				<ArgumentValue classname='ExprValue'>
																					<value>"OutPin"</value>
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
																					<value representation='Int64'>10</value>
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
									<value lbound='[0]' ubound='[2]'>
										<value>
											<Step typename='NI_UpdatePinMap' xsi:type='NI_UpdatePinMap' name='Update pin map'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:oWmczOOU7hGhxWDjK76h1B</value>
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
														<value>"OutputVoltageMeasurement.pinmap"</value>
													</PinMapPath>
												</subprops>
											</Step>
										</value>
										<value>
											<Step typename='Action' xsi:type='Action' name='Create and register NI-DCPower Sessions'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:PZz20+wm7hG/g0xEW1VriB</value>
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
																				<value>teststand_nidcpower.py</value>
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
																				<value>create_nidcpower_sessions</value>
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
										<value>
											<Step typename='Action' xsi:type='Action' name='Create and register NI-DMM Sessions'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:0U7o5ewm7hG/g0xEW1VriB</value>
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
									<value lbound='[0]' ubound='[1]'>
										<value>
											<Step typename='Action' xsi:type='Action' name='Destroy and unregister NI-DCPower sessions'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:HKlD0e0m7hG/g0xEW1VriB</value>
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
																				<value>teststand_nidcpower.py</value>
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
																				<value>destroy_nidcpower_sessions</value>
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
										<value>
											<Step typename='Action' xsi:type='Action' name='Destroy and unregister NI-DMM sessions'>
												<subprops>
													<TS classname='Obj'>
														<subprops>
															<Id classname='Str'>
																<value>ID#:ZU8H3e0m7hG/g0xEW1VriB</value>
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
					<MeasurementLink classname='Obj'>
						<subprops>
							<EnableMonitoring classname='Bool'>
								<value>false</value>
							</EnableMonitoring>
						</subprops>
					</MeasurementLink>
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

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/poetry.toml sha256=03117ffa8ef8551ed1c24d3d0b4fe45af5700d5914f29028eadcb9f9c85c056f bytes=32 -->
## FILE: examples/output_voltage_measurement/poetry.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/poetry.toml`
- sha256: `03117ffa8ef8551ed1c24d3d0b4fe45af5700d5914f29028eadcb9f9c85c056f`
- bytes: 32

````toml
[virtualenvs]
in-project = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/pyproject.toml sha256=57bb87768bb88204e7768382346096283b1cbaa780f1c6dd31648d31ca430097 bytes=1056 -->
## FILE: examples/output_voltage_measurement/pyproject.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/pyproject.toml`
- sha256: `57bb87768bb88204e7768382346096283b1cbaa780f1c6dd31648d31ca430097`
- bytes: 1056

````toml
[tool.poetry]
name = "output_voltage_measurement"
version = "0.5.0"
package-mode = false
description = ""
authors = ["National Instruments"]

[tool.poetry.dependencies]
python = "^3.10"
ni-measurement-plugin-sdk-service = {version = ">=2.3.1,<4.0"}
PyVISA = "^1.13.0"
PyVISA-sim = "^0.5.1"
nidcpower = { version = ">=1.4.4", extras = ["grpc"] }
click = ">=7.1.2"
grpcio = "*"
python-decouple = ">=3.8"

[tool.poetry.group.dev.dependencies]
ni-python-styleguide = ">=0.4.1"
mypy = ">=1.0"
types-grpcio = ">=1.0"
# Uncomment to use prerelease dependencies.
# nidcpower = { git = "https://github.com/ni/nimi-python.git", subdirectory = "generated/nidcpower", extras=["grpc"] }
# ni-measurement-plugin-sdk-service = {path = "../../packages/service", develop = true}

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.mypy]
disallow_untyped_defs = true

[[tool.mypy.overrides]]
module = [
    "decouple.*",
    "hightime.*",
    "nidcpower.*",
]
ignore_missing_imports = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/README.md sha256=fa670de27a6fb6fca06b4707cf584a924b74ca87faa85b1e985d2a3ef295bdac bytes=3768 -->
## FILE: examples/output_voltage_measurement/README.md

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/README.md`
- sha256: `fa670de27a6fb6fca06b4707cf584a924b74ca87faa85b1e985d2a3ef295bdac`
- bytes: 3768

````markdown
## Output Voltage Measurement

This is a measurement plug-in example that sources DC voltage as input to the DUT
with an NI SMU and measures the DUT output with a DMM that supports SCPI
commands using NI-VISA.

### Features

- Uses the `nidcpower` package to access NI-DCPower from Python
- Uses the open-source `PyVISA` package to access NI-VISA from Python
- Uses the open-source `PyVISA-sim` package to simulate instruments in software
- Pin-aware, supporting one session and pin per instrument and a single site
  - Sources the DC voltage level of the DUT input pin
  - Measures the voltage of the DUT output pin
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
- NI-DCPower
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

Supported SMU instrument models:
- An NI SMU that is supported by NI-DCPower (e.g. PXIe-4141)

Supported DMM instrument models:
- NI Instrument Simulator v2.0
- HP/Agilent/Keysight 34401A DMM

By default, this example uses physical instruments (or a simulated SMU created
in NI MAX). To simulate instruments without using NI MAX, follow the steps
below:
- Create a `.env` file in the measurement service's directory or one of its
  parent directories (such as the root of your Git repository or
  `C:\ProgramData\National Instruments\Plug-Ins\Measurements` for statically
  registered measurement services).
- Add the following options to the `.env` file to enable simulation via the
  driver's option string or `simulate` parameter:

  ```
  MEASUREMENT_PLUGIN_NIDCPOWER_SIMULATE=1
  MEASUREMENT_PLUGIN_NIDCPOWER_BOARD_TYPE=PXIe
  MEASUREMENT_PLUGIN_NIDCPOWER_MODEL=4141

  MEASUREMENT_PLUGIN_VISA_DMM_SIMULATE=1
  ```

The `_visa_dmm.py` instrument driver implements simulation using PyVISA-sim.
[`_visa_dmm_sim.yaml`](./_visa_dmm_sim.yaml) defines the behavior of the
simulated instrument.

To use a physical DMM instrument:
- Connect the instrument to a supported interface, such as GPIB or serial.
- By default, the pin map included with this example uses the resource name
  `GPIB0::3::INSTR`, which matches the NI Instrument Simulator's factory default
  settings when connected via GPIB.
  - If this doesn't match your configuration, edit
    [`OutputVoltageMeasurement.pinmap`](./OutputVoltageMeasurement.pinmap) and
    replace `GPIB0::3::INSTR` with the desired resource name (e.g.
    `ASRL1::INSTR`).
  - To modify the NI Instrument Simulator configuration (e.g. GPIB address,
    serial configuration), use the `Instrument Simulator Wizard` included with
    the NI Instrument Simulator software.
  - To configure third party instruments, see the documentation provided with
    the instrument.
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/start.bat sha256=bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851 bytes=253 -->
## FILE: examples/output_voltage_measurement/start.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/start.bat`
- sha256: `bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851`
- bytes: 253

````batch
@echo off
REM The discovery service uses this script to start the measurement service.
REM You can customize this script for your Python setup. The -v option logs
REM messages with level INFO and above.

.venv\Scripts\python.exe measurement.py -v
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/teststand_nidcpower.py sha256=c7e915cb456928aa861c431c5db2d27b01c61d83f06500a435b6aea1219017ea bytes=2623 -->
## FILE: examples/output_voltage_measurement/teststand_nidcpower.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/teststand_nidcpower.py`
- sha256: `c7e915cb456928aa861c431c5db2d27b01c61d83f06500a435b6aea1219017ea`
- bytes: 2623

````python
"""Functions to set up and tear down sessions of NI-DCPower devices in NI TestStand."""

from typing import Any

from _helpers import TestStandSupport
from ni_measurement_plugin_sdk_service.discovery import DiscoveryClient
from ni_measurement_plugin_sdk_service.grpc.channelpool import GrpcChannelPool
from ni_measurement_plugin_sdk_service.session_management import (
    INSTRUMENT_TYPE_NI_DCPOWER,
    PinMapContext,
    SessionInitializationBehavior,
    SessionManagementClient,
)


def create_nidcpower_sessions(sequence_context: Any) -> None:
    """Create and register all NI-DCPower sessions.

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
            pin_map_context, instrument_type_id=INSTRUMENT_TYPE_NI_DCPOWER
        ) as reservation:
            with reservation.initialize_nidcpower_sessions(
                initialization_behavior=SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH
            ):
                pass

            session_management_client.register_sessions(reservation.session_info)


def destroy_nidcpower_sessions() -> None:
    """Destroy and unregister all NI-DCPower sessions."""
    with GrpcChannelPool() as grpc_channel_pool:
        discovery_client = DiscoveryClient(grpc_channel_pool=grpc_channel_pool)
        session_management_client = SessionManagementClient(
            discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
        )
        with session_management_client.reserve_all_registered_sessions(
            instrument_type_id=INSTRUMENT_TYPE_NI_DCPOWER,
        ) as reservation:
            if not reservation.session_info:
                return

            session_management_client.unregister_sessions(reservation.session_info)
            with reservation.initialize_nidcpower_sessions(
                initialization_behavior=SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE
            ):
                pass
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/output_voltage_measurement/teststand_nivisa_dmm.py sha256=181a20b310a66bf4360811cfe3e41eaa79ec51b8bfc0f5cb1edb2f2dafbe9c2f bytes=3346 -->
## FILE: examples/output_voltage_measurement/teststand_nivisa_dmm.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/output_voltage_measurement/teststand_nivisa_dmm.py`
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

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/README.md sha256=a4281b705cdca55c8969f30698caf2a2b2bd0efbccc6021d615dae1424b3f3ff bytes=6988 -->
## FILE: examples/README.md

- repository: `ni/measurement-plugin-python`
- source_path: `examples/README.md`
- sha256: `a4281b705cdca55c8969f30698caf2a2b2bd0efbccc6021d615dae1424b3f3ff`
- bytes: 6988

````markdown

## Example Measurements

These are example measurements for use with InstrumentStudio 2026 Q1 or later.

For best results, use the example measurements corresponding to the version of InstrumentStudio
that you are using. Newer examples may demonstrate features that are not available in older
versions of InstrumentStudio.

| InstrumentStudio Version | Release | Download |
| ------------------------ | -------- | ------- |
| 2026 Q1                  | [3.1.0](https://github.com/ni/measurement-plugin-python/releases/tag/3.1.0) | [measurement-plugin-python-examples-3.1.0.zip](https://github.com/ni/measurement-plugin-python/releases/download/3.1.0/measurement-plugin-python-examples-3.1.0.zip) |
| 2025 Q4                  | [3.0.1](https://github.com/ni/measurement-plugin-python/releases/tag/3.0.1) | [measurement-plugin-python-examples-3.0.1.zip](https://github.com/ni/measurement-plugin-python/releases/download/3.0.1/measurement-plugin-python-examples-3.0.1.zip) |
| 2025 Q3                  | [2.3.1](https://github.com/ni/measurement-plugin-python/releases/tag/2.3.1) | [measurement-plugin-python-examples-2.3.1.zip](https://github.com/ni/measurement-plugin-python/releases/download/2.3.1/measurement-plugin-python-examples-2.3.1.zip) |
| 2025 Q2                  | [2.3.0](https://github.com/ni/measurement-plugin-python/releases/tag/2.3.0) | [measurement-plugin-python-examples-2.3.0.zip](https://github.com/ni/measurement-plugin-python/releases/download/2.3.0/measurement-plugin-python-examples-2.3.0.zip) |
| 2025 Q1                  | [2.2.0](https://github.com/ni/measurement-plugin-python/releases/tag/2.2.0) | [measurement-plugin-python-examples-2.2.0.zip](https://github.com/ni/measurement-plugin-python/releases/download/2.2.0/measurement-plugin-python-examples-2.2.0.zip) |
| 2024 Q4                  | [2.1.0](https://github.com/ni/measurement-plugin-python/releases/tag/2.1.0) | [measurement-plugin-python-examples-2.1.0.zip](https://github.com/ni/measurement-plugin-python/releases/download/2.1.0/measurement-plugin-python-examples-2.1.0.zip) |
| 2024 Q3                  | [2.0.0](https://github.com/ni/measurement-plugin-python/releases/tag/2.0.0) | [measurement-plugin-python-examples-2.0.0.zip](https://github.com/ni/measurement-plugin-python/releases/download/2.0.0/measurement-plugin-python-examples-2.0.0.zip) |
| 2024 Q2                  | [1.4.0](https://github.com/ni/measurement-plugin-python/releases/tag/1.4.0) | [measurementlink-python-examples-1.4.0.zip](https://github.com/ni/measurement-plugin-python/releases/download/1.4.0/measurementlink-python-examples-1.4.0.zip) |
| Older versions | | See [releases](https://github.com/ni/measurement-plugin-python/releases) page |

The TestStand sequence files associated with each example are saved in TestStand 2021 SP1.

### Available Example Measurements

- Instrument-specific
  - `nidaqmx_analog_input`: Performs a finite analog input measurement with NI-DAQmx.
  - `nidcpower_source_dc_voltage`: Sources and measures a DC voltage with an NI SMU. Provides a Measurement UI and a LabVIEW UI.
  - `nidcpower_source_dc_voltage_with_multiplexer`: Sources and measures a DC voltage with an NI SMU via an NI-SWITCH multiplexer.
  - `nidigital_spi`: Tests an SPI device using an NI Digital Pattern instrument.
  - `nidmm_measurement`: Performs a measurement using an NI DMM.
  - `nifgen_standard_function`: Generates a standard function waveform using an NI waveform generator.
  - `niscope_acquire_waveform`: Acquires a waveform using an NI oscilloscope.
  - `niswitch_control_relays`: Controls relays using an NI relay driver (e.g. PXI-2567).
  - `nivisa_dmm_measurement`: Performs a DMM measurement using NI-VISA and an NI Instrument Simulator v2.0.
  - `output_voltage_measurement`: Sources DC voltage as input to the DUT with an NI SMU and measures the DUT output with a DMM and NI-VISA.
- Software-only (no instrument or driver needed)
  - `sample_measurement`: Performs a loopback measurement with various data types. Provides a Measurement UI and a LabVIEW UI.
  - `game_of_life`: Displays Conway's Game of Life in a graph. Shows measurement cancellation and updating the UI during a measurement.

For more details about a specific example, see the `README.md` file included with the example.

### Setting up the Example Measurements

The example measurements are *Poetry-based* projects. Follow the steps below to set up an example measurement:

1. Install `poetry`. Refer to <https://python-poetry.org/docs/#installation> for information on installing Poetry.

2. Open a command prompt and change the working directory to the directory of the example measurement you want to work with.

    ``` cmd
    cd <path_of_example_measurement>
    REM Example: cd "..\measurement-plugin-python\examples\nidcpower_source_dc_voltage"
    ```

3. Run `poetry install`. This command creates/updates the virtual environment (`.venv`) and installs the needed dependencies (including `ni-measurement-plugin-sdk-service` package) into the virtual environment.

    ``` cmd
    poetry install
    ```
    - If you get a "command not found" error during `poetry install`, make sure that you added the Poetry path to the system path. Refer to [https://python-poetry.org/docs/#installing-with-the-official-installer/Add-poetry-to-your-path](https://python-poetry.org/docs/#installing-with-the-official-installer:~:text=Add%20Poetry%20to%20your%20PATH)

### Creating Simulated Devices for Example Measurements

- To enable simulation for all the modular instrument and VISA examples, copy `.env.simulation` to `.env` in the `examples` directory.

### Executing the Example Measurements

1. Start the discovery service if not already started.
2. Use `poetry run` to run the measurement service:

    ``` cmd
    poetry run python measurement.py
    ```

### Static Registration of Example Measurements

To statically register an example measurement service with the NI Discovery Service, do the following:

1. Copy the example measurement's directory (including the `.serviceconfig` file and startup batch file) to a subdirectory of `C:\ProgramData\National Instruments\Plug-Ins\Measurements`.
> **Note**
> Do not copy the `.venv` subdirectory&mdash;the virtual environment must be re-created in the new location.
2. Create a virtual environment in the new location by opening a command prompt to the new example directory under `C:\ProgramData` and running `poetry install`.

    ``` cmd
    cd <path_of_example_measurement>
    REM Example: cd "C:\ProgramData\National Instruments\Plug-Ins\Measurements\dc_measurement"
    poetry install
    ```

Once the example measurement service is statically registered, the NI Discovery Service makes it visible in supported NI applications.

> **Note**
> To set up and statically register all of the example measurements, run [`install_examples.py`](../scripts/install_examples.py).
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/.serviceignore sha256=997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912 bytes=148 -->
## FILE: examples/sample_measurement/.serviceignore

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/.serviceignore`
- sha256: `997580c333df9de0aa99b0cfddca79fbab67869dab40d09bc7810f567995b912`
- bytes: 148

````text
# This file specifies that when we publish this plug-in to a plug-in library,
# we should not copy the following directories:
.venv
__pycache__
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/_array_utils.py sha256=4c5e853ec4118b87bc74b4325e900d92055e1c0922af72a3560f90748e08ddd5 bytes=2738 -->
## FILE: examples/sample_measurement/_array_utils.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/_array_utils.py`
- sha256: `4c5e853ec4118b87bc74b4325e900d92055e1c0922af72a3560f90748e08ddd5`
- bytes: 2738

````python
"""2DArray Conversion Utilities."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ni.protobuf.types import array_pb2

if TYPE_CHECKING:
    import numpy as np
    import numpy.typing as npt


def double2darray_to_ndarray(double2darray: array_pb2.Double2DArray) -> npt.NDArray[np.float64]:
    """Convert Double2DArray to numpy NDArray."""
    import numpy as np

    return np.array(double2darray.data, dtype=np.float64).reshape(
        double2darray.rows, double2darray.columns
    )


def ndarray_to_double2darray(ndarray: npt.NDArray[np.float64]) -> array_pb2.Double2DArray:
    """Convert numpy NDArray to Double2DArray."""
    return array_pb2.Double2DArray(
        data=ndarray.flatten().tolist(), rows=ndarray.shape[0], columns=ndarray.shape[1]
    )


def list_to_double2darray(data: list[list[float]]) -> array_pb2.Double2DArray:
    """Convert list of lists to Double2DArray."""
    rows = len(data)
    columns = len(data[0]) if rows > 0 else 0
    flattened_data = [item for sublist in data for item in sublist]
    return array_pb2.Double2DArray(data=flattened_data, rows=rows, columns=columns)


def double2darray_to_list(double2darray: array_pb2.Double2DArray) -> list[list[float]]:
    """Convert Double2DArray to list of lists."""
    data = double2darray.data
    rows = double2darray.rows
    columns = double2darray.columns
    return [data[i * columns : (i + 1) * columns] for i in range(rows)]


def string2darray_to_ndarray(string2darray: array_pb2.String2DArray) -> npt.NDArray[np.str_]:
    """Convert String2DArray to numpy NDArray."""
    import numpy as np

    return np.array(string2darray.data, dtype=np.str_).reshape(
        string2darray.rows, string2darray.columns
    )


def ndarray_to_string2darray(ndarray: npt.NDArray[np.str_]) -> array_pb2.String2DArray:
    """Convert numpy NDArray to String2DArray."""
    return array_pb2.String2DArray(
        data=ndarray.flatten().tolist(), rows=ndarray.shape[0], columns=ndarray.shape[1]
    )


def string2darray_to_list(string2darray: array_pb2.String2DArray) -> list[list[str]]:
    """Convert String2DArray to list of lists."""
    data = string2darray.data
    rows = string2darray.rows
    columns = string2darray.columns
    return [data[i * columns : (i + 1) * columns] for i in range(rows)]


def list_to_string2darray(data: list[list[str]]) -> array_pb2.String2DArray:
    """Convert list of lists to String2DArray."""
    rows = len(data)
    columns = len(data[0]) if rows > 0 else 0
    flattened_data = [item for sublist in data for item in sublist]
    return array_pb2.String2DArray(data=flattened_data, rows=rows, columns=columns)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/_helpers.py sha256=0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426 bytes=2920 -->
## FILE: examples/sample_measurement/_helpers.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/_helpers.py`
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

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/_stubs/__init__.py sha256=b51b6d6919cd92fa4a9bf965dd516905e90de8d734eebb55421dd3c578e8c83d bytes=50 -->
## FILE: examples/sample_measurement/_stubs/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/_stubs/__init__.py`
- sha256: `b51b6d6919cd92fa4a9bf965dd516905e90de8d734eebb55421dd3c578e8c83d`
- bytes: 50

````python
"""Stubs for sample_measurement's color enum."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/_stubs/color.proto sha256=e51dd6d8b65c9bac6bf53ef12661ef1fc2c0ced77d5677d7d535e9d76a9492b2 bytes=801 -->
## FILE: examples/sample_measurement/_stubs/color.proto

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/_stubs/color.proto`
- sha256: `e51dd6d8b65c9bac6bf53ef12661ef1fc2c0ced77d5677d7d535e9d76a9492b2`
- bytes: 801

````protobuf
//---------------------------------------------------------------------
//---------------------------------------------------------------------
syntax = "proto3";

//---------------------------------------------------------------------
//---------------------------------------------------------------------
package ni.examples;

//---------------------------------------------------------------------
//---------------------------------------------------------------------
option csharp_namespace = "NationalInstruments.MeasurementServices.Measurements";

//---------------------------------------------------------------------
//---------------------------------------------------------------------

enum ProtobufColor{
    NONE = 0;
    PINK = 1;
    WHITE = 2;
    BLACK = 3;
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/_stubs/color_pb2.py sha256=5295dd1c3cbe88dd33f7dbefce7c0d7b7a038e289ac8c57c044b235be2e5cd61 bytes=1199 -->
## FILE: examples/sample_measurement/_stubs/color_pb2.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/_stubs/color_pb2.py`
- sha256: `5295dd1c3cbe88dd33f7dbefce7c0d7b7a038e289ac8c57c044b235be2e5cd61`
- bytes: 1199

````python
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: color.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x63olor.proto\x12\x0bni.examples*9\n\rProtobufColor\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04PINK\x10\x01\x12\t\n\x05WHITE\x10\x02\x12\t\n\x05\x42LACK\x10\x03\x42\x37\xaa\x02\x34NationalInstruments.MeasurementServices.Measurementsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'color_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\0024NationalInstruments.MeasurementServices.Measurements'
  _PROTOBUFCOLOR._serialized_start=28
  _PROTOBUFCOLOR._serialized_end=85
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/_stubs/color_pb2.pyi sha256=0018723c67f5ea819a98b86fd71600f740a97598f0032755ffdd9e9b0b3fb866 bytes=1453 -->
## FILE: examples/sample_measurement/_stubs/color_pb2.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/_stubs/color_pb2.pyi`
- sha256: `0018723c67f5ea819a98b86fd71600f740a97598f0032755ffdd9e9b0b3fb866`
- bytes: 1453

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
---------------------------------------------------------------------
---------------------------------------------------------------------
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ProtobufColor:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ProtobufColorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ProtobufColor.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NONE: _ProtobufColor.ValueType  # 0
    PINK: _ProtobufColor.ValueType  # 1
    WHITE: _ProtobufColor.ValueType  # 2
    BLACK: _ProtobufColor.ValueType  # 3

class ProtobufColor(_ProtobufColor, metaclass=_ProtobufColorEnumTypeWrapper):
    """---------------------------------------------------------------------
    ---------------------------------------------------------------------
    """

NONE: ProtobufColor.ValueType  # 0
PINK: ProtobufColor.ValueType  # 1
WHITE: ProtobufColor.ValueType  # 2
BLACK: ProtobufColor.ValueType  # 3
global___ProtobufColor = ProtobufColor
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/_stubs/color_pb2_grpc.py sha256=fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb bytes=163 -->
## FILE: examples/sample_measurement/_stubs/color_pb2_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/_stubs/color_pb2_grpc.py`
- sha256: `fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb`
- bytes: 163

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/_stubs/color_pb2_grpc.pyi sha256=bcc6cd9c21fc28773cccb72f78f3002ad2f44b48aef1bdcc218758ec4a42f6ba bytes=572 -->
## FILE: examples/sample_measurement/_stubs/color_pb2_grpc.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/_stubs/color_pb2_grpc.pyi`
- sha256: `bcc6cd9c21fc28773cccb72f78f3002ad2f44b48aef1bdcc218758ec4a42f6ba`
- bytes: 572

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
---------------------------------------------------------------------
---------------------------------------------------------------------
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/install.bat sha256=695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025 bytes=205 -->
## FILE: examples/sample_measurement/install.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/install.bat`
- sha256: `695c4e8bef6be1793870d46792c4c82edc8611f713edabb12929b9bfd2e97025`
- bytes: 205

````batch
@echo off
REM The discovery service uses this script to install the dependencies
REM for the measurement service. You can customize this script for your
REM Python setup.

poetry install --only main
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/measurement.py sha256=9b215062665def8c4e26c5acdf2bbb2c9983216765c70cf899351601ed2194e2 bytes=5495 -->
## FILE: examples/sample_measurement/measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/measurement.py`
- sha256: `9b215062665def8c4e26c5acdf2bbb2c9983216765c70cf899351601ed2194e2`
- bytes: 5495

````python
"""Perform a loopback measurement with various data types."""

import logging
import pathlib
import sys
from collections.abc import Iterable
from enum import Enum

import _array_utils
import click
import ni_measurement_plugin_sdk_service as nims
from _helpers import configure_logging, verbosity_option
from ni.protobuf.types import (
    array_pb2,
)

try:
    from _stubs import color_pb2
except ImportError:
    from examples.sample_measurement._stubs import color_pb2  # type: ignore

script_or_exe = sys.executable if getattr(sys, "frozen", False) else __file__
service_directory = pathlib.Path(script_or_exe).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "SampleMeasurement.serviceconfig",
    ui_file_paths=[
        service_directory / "SampleMeasurement.measui",
        service_directory / "SampleAllParameters.measui",
        service_directory / "SampleMeasurement.vi",
    ],
)


class Color(Enum):
    """Primary colors used for example enum-typed config and output."""

    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3


# Define a list of lists of floats
_list_of_lists_of_floats = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]

# Convert the list of lists to a Double2DArray
_converted_double_2d_array = _array_utils.list_to_double2darray(_list_of_lists_of_floats)

# Define a list of lists of strings
_list_of_lists_of_string = [["String1", "String2", "String3"], ["String4", "String5", "String6"]]

# Convert the list of lists to a String2DArray
_converted_string_2d_array = _array_utils.list_to_string2darray(_list_of_lists_of_string)


@measurement_service.register_measurement
@measurement_service.configuration("Float In", nims.DataType.Float, 0.06)
@measurement_service.configuration("Double Array In", nims.DataType.DoubleArray1D, [0.1, 0.2, 0.3])
@measurement_service.configuration("Bool In", nims.DataType.Boolean, False)
@measurement_service.configuration("String In", nims.DataType.String, "sample string")
@measurement_service.configuration("Enum In", nims.DataType.Enum, Color.BLUE, enum_type=Color)
@measurement_service.configuration(
    "Protobuf Enum In",
    nims.DataType.Enum,
    color_pb2.ProtobufColor.BLACK,
    enum_type=color_pb2.ProtobufColor,
)
@measurement_service.configuration(
    "String Array In", nims.DataType.StringArray1D, ["String1", "String2"]
)
@measurement_service.output("Float out", nims.DataType.Float)
@measurement_service.output("Double Array out", nims.DataType.DoubleArray1D)
@measurement_service.output("Bool out", nims.DataType.Boolean)
@measurement_service.output("String out", nims.DataType.String)
@measurement_service.output("Enum out", nims.DataType.Enum, enum_type=Color)
@measurement_service.output(
    "Protobuf Enum out", nims.DataType.Enum, enum_type=color_pb2.ProtobufColor
)
@measurement_service.output("String Array out", nims.DataType.StringArray1D)
@measurement_service.output("Double 2D Array Out", nims.DataType.Double2DArray)
@measurement_service.output("Converted Double 2D Array", nims.DataType.Double2DArray)
@measurement_service.output("String 2D Array Out", nims.DataType.String2DArray)
@measurement_service.output("Converted String 2D Array", nims.DataType.String2DArray)
def measure(
    float_input: float,
    double_array_input: Iterable[float],
    bool_input: bool,
    string_input: str,
    enum_input: Color,
    protobuf_enum_input: color_pb2.ProtobufColor.ValueType,
    string_array_in: Iterable[str],
) -> tuple[
    float,
    Iterable[float],
    bool,
    str,
    Color,
    color_pb2.ProtobufColor.ValueType,
    Iterable[str],
    array_pb2.Double2DArray,
    array_pb2.Double2DArray,
    array_pb2.String2DArray,
    array_pb2.String2DArray,
]:
    """Perform a loopback measurement with various data types."""
    logging.info("Executing measurement")

    def cancel_callback() -> None:
        logging.info("Canceling measurement")

    measurement_service.context.add_cancel_callback(cancel_callback)

    float_output = float_input
    float_array_output = double_array_input
    bool_output = bool_input
    string_output = string_input
    enum_output = enum_input
    protobuf_enum_output = protobuf_enum_input
    string_array_output = string_array_in
    double_2d_array_output = array_pb2.Double2DArray(
        rows=2, columns=3, data=[1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
    )
    converted_double_2d_array_output = _converted_double_2d_array
    string_2d_array_output = array_pb2.String2DArray(
        rows=2, columns=3, data=["ABC", "DEF", "GHI", "JKL", "MNO", "PQR"]
    )
    converted_string_2d_array_output = _converted_string_2d_array
    logging.info("Completed measurement")

    return (
        float_output,
        float_array_output,
        bool_output,
        string_output,
        enum_output,
        protobuf_enum_output,
        string_array_output,
        double_2d_array_output,
        converted_double_2d_array_output,
        string_2d_array_output,
        converted_string_2d_array_output,
    )


@click.command
@verbosity_option
def main(verbosity: int) -> None:
    """Perform a loopback measurement with various data types."""
    configure_logging(verbosity)

    with measurement_service.host_service():
        input("Press enter to close the measurement service.\n")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/poetry.toml sha256=ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e bytes=34 -->
## FILE: examples/sample_measurement/poetry.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/poetry.toml`
- sha256: `ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e`
- bytes: 34

````toml
[virtualenvs]
in-project = true
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/pyproject.toml sha256=2ce8669a0d1906078ffd9aa5b9f0e636d7c42f72f64fd0d7a2d7bc53c4dfadf8 bytes=1245 -->
## FILE: examples/sample_measurement/pyproject.toml

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/pyproject.toml`
- sha256: `2ce8669a0d1906078ffd9aa5b9f0e636d7c42f72f64fd0d7a2d7bc53c4dfadf8`
- bytes: 1245

````toml
[tool.poetry]
name = "sample_measurement"
version = "0.5.0"
package-mode = false
description = "Measurement plug-in example that performs a loopback measurement with various data types."
authors = ["National Instruments"]

[tool.poetry.dependencies]
python = "^3.10"
ni-measurement-plugin-sdk-service = {version = ">=2.3.1,<4.0"}
click = ">=7.1.2, !=8.1.4" # mypy fails with click 8.1.4: https://github.com/pallets/click/issues/2558
ni-protobuf-types = { version = ">=0.1.0dev2", allow-prereleases = true }

[tool.poetry.group.dev.dependencies]
ni-python-styleguide = ">=0.4.1"
mypy = ">=1.0"
types-grpcio = ">=1.0"
grpcio-tools = "1.49.1"
mypy-protobuf = "^3.6.0"
types-protobuf = ">=4.21"
# Uncomment to use prerelease dependencies.
# ni-measurement-plugin-sdk-service = {path = "../../packages/service", develop = true}

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.mypy]
disallow_untyped_defs = true

[[tool.mypy.overrides]]
module = [
    # numpy has type hints but this example does not depend on numpy.
    "numpy.*",
]
ignore_missing_imports = true

[tool.ni-python-styleguide]
extend_exclude = '*_pb2_grpc.py,*_pb2_grpc.pyi,*_pb2.py,*_pb2.pyi'
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/README.md sha256=2497d26430ace8ff338a221c178e5df1e48dbfd4779f43feee52b33f82265a9a bytes=601 -->
## FILE: examples/sample_measurement/README.md

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/README.md`
- sha256: `2497d26430ace8ff338a221c178e5df1e48dbfd4779f43feee52b33f82265a9a`
- bytes: 601

````markdown
## Sample Measurement

This is a measurement plug-in example that performs a loopback measurement with
various data types.

### Features

- Demonstrates various data types
- Includes InstrumentStudio and Measurement Plug-In UI Editor project files
- Includes multiple UI files. Note: InstrumentStudio only displays the 1st UI
  file. To change the UI file used for the example, simply switch the order of
  the `ui_file_paths` array in `measurement.py`

### Required Software

- InstrumentStudio 2025 Q1 or later

### Required Hardware

This example does not require any hardware.
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/SampleAllParameters.measui sha256=04318514d38f68b60577c45a7ab37287c0372249886aee7483cbf8d7b04e42b6 bytes=30901 -->
## FILE: examples/sample_measurement/SampleAllParameters.measui

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/SampleAllParameters.measui`
- sha256: `04318514d38f68b60577c45a7ab37287c0372249886aee7483cbf8d7b04e42b6`
- bytes: 30901

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="35AC9A24627BCC43C6B3DB8AF70B218776EBDC56D1ACA327AACBEA79596C0B83E78072E148C250A28B1D85F307ECDDD793C3D49735D4614E70DE32D5A16AD9D0" Timestamp="1DB76DDF80FECA6" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.16.0.809" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="9.15.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.16.0.809" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="25.3.0.809" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="24.8.0.0" />
		<ParsableNamespace AssemblyFileVersion="9.16.0.809" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.16.0.809" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="25.3.0.809" Name="Measurement Plug-In UI Editor" Version="25.3.0.809" />
	</SourceModelFeatureSet>
	<Screen DisplayName="Sample Measurement (Py)" Id="20c496a981bb4f73bea9d243756baab5" ServiceClass="ni.examples.SampleMeasurement_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
		<ScreenSurface BackgroundColor="[SMSolidColorBrush]#00ffffff" Height="[float]789" Id="c47bc3494c0244bab74b59853ae5087f" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]1330" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
			<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{d001b29b-5739-42de-9c18-004303c47a0b}/Configuration/Float In" Enabled="[bool]True" Height="[float]24" Id="ac8d5d6abc13430eba5b9b5008242f2e" Interval="[float]1" Label="[UIModel]b16b7fdf2cd2444aaba612c28dff288c" Left="[float]31" Top="[float]36" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=5:DigitDisplayType=SignificantDigits:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Single" Width="[float]160" />
			<Label Height="[float]16" Id="b16b7fdf2cd2444aaba612c28dff288c" LabelOwner="[UIModel]ac8d5d6abc13430eba5b9b5008242f2e" Left="[float]31" Text="[string]Float In" Top="[float]16" Width="[float]39" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelCheckBox BaseName="[string]Checkbox" Channel="[string]{d001b29b-5739-42de-9c18-004303c47a0b}/Configuration/Bool In" Content="[string]Off/On" Enabled="[bool]True" Height="[float]16" Id="50072f6dacfc4f4cbbcf875d6d8483cd" Label="[UIModel]72b5606765b48f6a03e01d0505d78c9" Left="[float]31" MinHeight="[float]16" MinWidth="[float]16" Top="[float]91" Width="[float]59" />
			<Label Height="[float]16" Id="72b5606765b48f6a03e01d0505d78c9" LabelOwner="[UIModel]50072f6dacfc4f4cbbcf875d6d8483cd" Left="[float]31" Text="[string]Bool In" Top="[float]71" Width="[float]37" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelStringControl AcceptsReturn="[bool]False" BaseName="[string]String" Channel="[string]{d001b29b-5739-42de-9c18-004303c47a0b}/Configuration/String In" Enabled="[bool]True" Height="[float]24" HorizontalScrollBarVisibility="[ScrollBarVisibility]Hidden" Id="344fe1d909e0448ca0923ced1bcdcb12" Label="[UIModel]4b4dcad2a0248e58564c645943b0c7f" Left="[float]31" Text="[string]" Top="[float]138" VerticalScrollBarVisibility="[ScrollBarVisibility]Auto" Width="[float]160" />
			<Label Height="[float]16" Id="4b4dcad2a0248e58564c645943b0c7f" LabelOwner="[UIModel]344fe1d909e0448ca0923ced1bcdcb12" Left="[float]31" Text="[string]String In" Top="[float]118" Width="[float]44" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelArrayViewer AdaptsToType="[bool]True" ArrayElement="[UIModel]4e1d7f76fed3408c879928fcf2039e63" BaseName="[string]Numeric Array Input" Channel="[string]{d001b29b-5739-42de-9c18-004303c47a0b}/Configuration/Double Array In" Columns="[int]1" Dimensions="[int]1" Enabled="[bool]True" Height="[float]120" Id="2d88c55ec56e4ee58ddb2acd0bee73b0" IndexVisibility="[Visibility]Collapsed" IsFixedSize="[bool]False" Label="[UIModel]3d3aa154901d4d738857fa48bddcef45" Left="[float]30" Orientation="[SMOrientation]Vertical" Rows="[int]4" Top="[float]201" VerticalScrollBarVisibility="[ScrollBarVisibility]Visible" Width="[float]161">
				<p.DefaultElementValue>0x0</p.DefaultElementValue>
				<ChannelArrayNumericText BaseName="[string]Numeric" Height="[float]24" Id="4e1d7f76fed3408c879928fcf2039e63" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]129" />
			</ChannelArrayViewer>
			<Label Height="[float]16" Id="3d3aa154901d4d738857fa48bddcef45" LabelOwner="[UIModel]2d88c55ec56e4ee58ddb2acd0bee73b0" Left="[float]30" Text="[string]Double Array In" Top="[float]181" Width="[float]83" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{d001b29b-5739-42de-9c18-004303c47a0b}/Output/Float out" Height="[float]24" Id="560b0851e24b4be1957fc505ed62f5db" Interval="[float]1" IsReadOnly="[bool]True" Label="[UIModel]a73c7bd96aae4a3792867b1f471247cc" Left="[float]239" Top="[float]36" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=5:DigitDisplayType=SignificantDigits:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Single" Width="[float]160" />
			<Label Height="[float]16" Id="a73c7bd96aae4a3792867b1f471247cc" LabelOwner="[UIModel]560b0851e24b4be1957fc505ed62f5db" Left="[float]239" Text="[string]Float out" Top="[float]16" Width="[float]47" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelLED BaseName="[string]Round LED" Channel="[string]{d001b29b-5739-42de-9c18-004303c47a0b}/Output/Bool out" ContentVisibility="[Visibility]Collapsed" FalseBackground="[SMSolidColorBrush]#ffe0e0e0" FalseContent="[string]Off" Height="[float]20" Id="529587ea90ea4255aec8f53606bc99b9" IsReadOnly="[bool]True" Label="[UIModel]aff1aad914904ce6a6fb6756cba2c866" Left="[float]239" MinHeight="[float]20" MinWidth="[float]20" Shape="[LEDShape]Round" Top="[float]91" TrueContent="[string]On" Width="[float]20" />
			<Label Height="[float]16" Id="aff1aad914904ce6a6fb6756cba2c866" LabelOwner="[UIModel]529587ea90ea4255aec8f53606bc99b9" Left="[float]239" Text="[string]Bool out" Top="[float]71" Width="[float]45" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelStringControl AcceptsReturn="[bool]False" BaseName="[string]String" Channel="[string]{d001b29b-5739-42de-9c18-004303c47a0b}/Output/String out" Height="[float]24" HorizontalScrollBarVisibility="[ScrollBarVisibility]Hidden" Id="fa35489e33a34b0183b746fffa2ced9d" IsReadOnly="[bool]True" Label="[UIModel]94b2b204aefb4bc7b509f1c49eae0c18" Left="[float]239" Top="[float]138" VerticalScrollBarVisibility="[ScrollBarVisibility]Auto" Width="[float]160" />
			<Label Height="[float]16" Id="94b2b204aefb4bc7b509f1c49eae0c18" LabelOwner="[UIModel]fa35489e33a34b0183b746fffa2ced9d" Left="[float]239" Text="[string]String out" Top="[float]118" Width="[float]52" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelArrayViewer AdaptsToType="[bool]True" ArrayElement="[UIModel]9845cec681cb4828a587b9fd395fa78c" BaseName="[string]Numeric Array Output" Channel="[string]{d001b29b-5739-42de-9c18-004303c47a0b}/Output/Double Array out" Columns="[int]1" Dimensions="[int]1" Height="[float]120" Id="13707da33a16404e92bf506121dc2dbc" IndexVisibility="[Visibility]Collapsed" IsFixedSize="[bool]False" Label="[UIModel]4d641544433e4a3ab6f691b85e44d2d2" Left="[float]239" Orientation="[SMOrientation]Vertical" Rows="[int]4" Top="[float]201" VerticalScrollBarVisibility="[ScrollBarVisibility]Visible" Width="[float]160">
				<p.DefaultElementValue>0x0</p.DefaultElementValue>
				<ChannelArrayNumericText BaseName="[string]Numeric" Height="[float]24" Id="9845cec681cb4828a587b9fd395fa78c" IsReadOnly="[bool]True" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]128" />
			</ChannelArrayViewer>
			<Label Height="[float]16" Id="4d641544433e4a3ab6f691b85e44d2d2" LabelOwner="[UIModel]13707da33a16404e92bf506121dc2dbc" Left="[float]239" Text="[string]Double Array out" Top="[float]181" Width="[float]91" xmlns="http://www.ni.com/PanelCommon" />
			<ArrayGraph Background="[SMSolidColorBrush]#00000000" BaseName="[string]Array Graph" Height="[float]300" Id="7a4e3733e44a4251a517215af2e6fb34" Label="[UIModel]7d653a1b8e82474fa5957187f74dc876" Left="[float]563" MinWidth="[float]230" PlotAreaMargin="[SMThickness]37,26,7,27" PreferIndexData="[bool]False" RenderMode="[RenderMode]Hardware" SuppressScaleLayout="[bool]False" Top="[float]38" Width="[float]500">
				<ArrayGraphAxis Adjuster="[RangeAdjuster]FitExactly" Id="c0565cae4648f2ba4df1ea58a2f8a7" Label="[string]Index" LabelVisibility="[SMVisibility]Collapsed" MajorDivisions="[UIModel]9ade996a17d43088b767857a7664a57" MinorTickVisibility="[SMVisibility]Collapsed" Orientation="[SMOrientation]Horizontal" Range="[IRange]0, 2, System.Double" ValueType="[Type]Double">
					<RangeLabeledDivisions Id="9ade996a17d43088b767857a7664a57" xmlns="http://www.ni.com/Controls.LabVIEW.Design">
						<p.LabelPresenter Format="G6" />
					</RangeLabeledDivisions>
				</ArrayGraphAxis>
				<ArrayGraphAxis Adjuster="[RangeAdjuster]FitExactly" Id="f1a87538e8e24c2ea11b7444cf2b6963" Label="[string]Value" LabelVisibility="[SMVisibility]Collapsed" MajorDivisions="[UIModel]967427c1936f4c0183152fa54f00f391" Orientation="[SMOrientation]Vertical" Range="[IRange]0.1, 0.3, System.Double" ValueType="[Type]Double">
					<RangeLabeledDivisions Id="967427c1936f4c0183152fa54f00f391" xmlns="http://www.ni.com/Controls.LabVIEW.Design">
						<p.LabelPresenter Format="G6" />
					</RangeLabeledDivisions>
				</ArrayGraphAxis>
				<HmiGraphPlot Channel="[string]{d001b29b-5739-42de-9c18-004303c47a0b}/Output/Double Array out" HorizontalScale="[UIModel]c0565cae4648f2ba4df1ea58a2f8a7" Id="effebee353c5439d83f900e31d3c5f4c" IsDefaultPlot="[bool]False" Label="[string]Double Array out" VerticalScale="[UIModel]f1a87538e8e24c2ea11b7444cf2b6963">
					<PlotRenderer Id="bfa8cdd706b74f828a1194a5a99a9eb0" LineStroke="[SMSolidColorBrush]#ffea4225" LineThickness="[double]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</HmiGraphPlot>
			</ArrayGraph>
			<HmiChartPlotLegend Graph="[UIModel]7a4e3733e44a4251a517215af2e6fb34" Height="[float]28" Id="b58e6580121b48e499f7b93e9a6128b6" Left="[float]1070" Top="[float]38" />
			<HmiChartCursorLegend Graph="[UIModel]7a4e3733e44a4251a517215af2e6fb34" Height="[float]80" Id="1f4572e884ce4422a72a6baf1873193b" Left="[float]568" MinHeight="[float]80" Top="[float]367" Visible="[bool]False" Width="[float]316" />
			<HmiChartScaleLegend Graph="[UIModel]7a4e3733e44a4251a517215af2e6fb34" Height="[float]52" Id="3538db2f6302464287a98c35d89afaec" Left="[float]988" Top="[float]345" Visible="[bool]False" />
			<ArrayGraphTools BackgroundColor="[SMSolidColorBrush]#fff7f7f7" Graph="[UIModel]7a4e3733e44a4251a517215af2e6fb34" Height="[float]26" Id="2fc284fd64c54336a9d723d588aa3c81" Left="[float]909" OffsetX="[float]346" OffsetY="[float]0" Top="[float]38" Width="[float]122">
				<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Horizontal Zoom" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]12620252458a45539a315d2d4bec982d" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="274c723135754d628924a47608d1ec3b" IsMomentary="[bool]False" Label="[UIModel]8ea2460bf8db46ba8c06406d1cd4c9ec" Left="[float]2" PartName="[string]PART_ZoomHorizontalButton" Top="[float]2" Value="[bool]False" Width="[float]28">
					<Image BaseName="[string]Image" Id="12620252458a45539a315d2d4bec982d" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomHorizontal.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
				</ComposableButton>
				<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Vertical Zoom" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]afdf326007b54e9793e1285c559607c3" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="46d7f2b09d4e4cf8b79a9293f146695e" IsMomentary="[bool]False" Label="[UIModel]4928ee82548e4f1fae6550b6164aee6e" Left="[float]32" PartName="[string]PART_ZoomVerticalButton" Top="[float]2" Value="[bool]False" Width="[float]28">
					<Image BaseName="[string]Image" Id="afdf326007b54e9793e1285c559607c3" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomVertical.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
				</ComposableButton>
				<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Pan" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]e079820be0cc4cf5baecf45947d92817" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="30d2367b849e446789f0ebae1a3b8b5c" IsMomentary="[bool]False" Label="[UIModel]5a4b5477a8784afcb3536bf327d4857d" Left="[float]62" PartName="[string]PART_PanButton" Top="[float]2" Value="[bool]False" Width="[float]28">
					<Image BaseName="[string]Image" Id="e079820be0cc4cf5baecf45947d92817" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomPan.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
				</ComposableButton>
				<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Reset" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]826a35475724f97b30fbe6b5a2d8e00" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="7791599dec5e40c98da2dc1dff8203f7" IsMomentary="[bool]True" Label="[UIModel]5fdaffd604954eab8c40eece223bace6" Left="[float]92" PartName="[string]PART_ResetButton" Top="[float]2" Value="[bool]False" Width="[float]28">
					<Image BaseName="[string]Image" Id="826a35475724f97b30fbe6b5a2d8e00" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomExtents.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
				</ComposableButton>
				<Label Id="8ea2460bf8db46ba8c06406d1cd4c9ec" LabelOwner="[UIModel]274c723135754d628924a47608d1ec3b" Left="[float]2" Text="[string]Horizontal Zoom" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
				<Label Id="4928ee82548e4f1fae6550b6164aee6e" LabelOwner="[UIModel]46d7f2b09d4e4cf8b79a9293f146695e" Left="[float]32" Text="[string]Vertical Zoom" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
				<Label Id="5a4b5477a8784afcb3536bf327d4857d" LabelOwner="[UIModel]30d2367b849e446789f0ebae1a3b8b5c" Left="[float]62" Text="[string]Pan" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
				<Label Id="5fdaffd604954eab8c40eece223bace6" LabelOwner="[UIModel]7791599dec5e40c98da2dc1dff8203f7" Left="[float]92" Text="[string]Reset" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
			</ArrayGraphTools>
			<Label Height="[float]16" Id="7d653a1b8e82474fa5957187f74dc876" LabelOwner="[UIModel]7a4e3733e44a4251a517215af2e6fb34" Left="[float]563" Text="[string]Double Array out" Top="[float]18" Width="[float]91" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{d001b29b-5739-42de-9c18-004303c47a0b}/Configuration/Enum In" Enabled="[bool]True" Height="[float]24" Id="604b159420bd4525aa1b71300d41d9be" Label="[UIModel]6ecc1177484d4f099186d5680091578b" Left="[float]30" Top="[float]355" Value="[int]3" Width="[float]136" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
				<RingSelectorInfo DisplayValue="[string]NONE" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]RED" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]GREEN" IsEnabled="[bool]True" Value="[int]2" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]BLUE" IsEnabled="[bool]True" Value="[int]3" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
			</ChannelEnumSelector>
			<Label Height="[float]16" Id="6ecc1177484d4f099186d5680091578b" LabelOwner="[UIModel]604b159420bd4525aa1b71300d41d9be" Left="[float]30" Text="[string]Enum In" Top="[float]335" Width="[float]43" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{d001b29b-5739-42de-9c18-004303c47a0b}/Output/Enum out" Height="[float]24" Id="b82a4cfdbd2d47b3b3457b17fe57c29e" InteractionMode="[SelectorInteractionModes]ReadOnly" Label="[UIModel]f45987e5f4b442508b463a26fab7b15a" Left="[float]239" Top="[float]355" Width="[float]136" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
				<RingSelectorInfo DisplayValue="[string]NONE" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]RED" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]GREEN" IsEnabled="[bool]True" Value="[int]2" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]BLUE" IsEnabled="[bool]True" Value="[int]3" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
			</ChannelEnumSelector>
			<Label Height="[float]16" Id="f45987e5f4b442508b463a26fab7b15a" LabelOwner="[UIModel]b82a4cfdbd2d47b3b3457b17fe57c29e" Left="[float]239" Text="[string]Enum out" Top="[float]335" Width="[float]51" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{d001b29b-5739-42de-9c18-004303c47a0b}/Output/Protobuf Enum out" Height="[float]24" Id="f40567b55efb4c1caa64ce1f49d7ca4f" InteractionMode="[SelectorInteractionModes]ReadOnly" Label="[UIModel]cceab74986a742e4bcdcdf9a26427440" Left="[float]239" Top="[float]413" Width="[float]136" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
				<RingSelectorInfo DisplayValue="[string]NONE" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]PINK" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]WHITE" IsEnabled="[bool]True" Value="[int]2" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]BLACK" IsEnabled="[bool]True" Value="[int]3" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
			</ChannelEnumSelector>
			<Label Height="[float]16" Id="cceab74986a742e4bcdcdf9a26427440" LabelOwner="[UIModel]f40567b55efb4c1caa64ce1f49d7ca4f" Left="[float]239" Text="[string]Protobuf Enum out" Top="[float]393" Width="[float]101" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{d001b29b-5739-42de-9c18-004303c47a0b}/Configuration/Protobuf Enum In" Enabled="[bool]True" Height="[float]24" Id="6a69bdf9c93e41bfb4726e3d0794db28" Label="[UIModel]2ee07ceb54f34e5aa0328f4e072cdc96" Left="[float]30" Top="[float]413" Value="[int]3" Width="[float]136" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
				<RingSelectorInfo DisplayValue="[string]NONE" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]PINK" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]WHITE" IsEnabled="[bool]True" Value="[int]2" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				<RingSelectorInfo DisplayValue="[string]BLACK" IsEnabled="[bool]True" Value="[int]3" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
			</ChannelEnumSelector>
			<Label Height="[float]16" Id="2ee07ceb54f34e5aa0328f4e072cdc96" LabelOwner="[UIModel]6a69bdf9c93e41bfb4726e3d0794db28" Left="[float]30" Text="[string]Protobuf Enum In" Top="[float]393" Width="[float]93" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelArrayViewer AdaptsToType="[bool]True" ArrayElement="[UIModel]71169cddc22b42e5be7e2e62744d62d2" BaseName="[string]Numeric Array Output" Channel="[string]{d001b29b-5739-42de-9c18-004303c47a0b}/Output/Double 2D Array Out" Columns="[int]3" Dimensions="[int]2" FirstIndex="[ArrayElementIndex]0,0" Height="[float]120" Id="423a23621bf040b585d96903342472f3" IndexVisibility="[Visibility]Collapsed" IsFixedSize="[bool]False" Label="[UIModel]3943f48256a74c39878788859d09830d" Left="[float]239" Orientation="[SMOrientation]Horizontal" Rows="[int]4" TabIndex="[int]4" Top="[float]482" VerticalScrollBarVisibility="[ScrollBarVisibility]Visible" Width="[float]256">
				<p.DefaultElementValue>0x0</p.DefaultElementValue>
				<ChannelArrayNumericText BaseName="[string]Numeric" Height="[float]24" Id="71169cddc22b42e5be7e2e62744d62d2" IsReadOnly="[bool]True" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]72" />
			</ChannelArrayViewer>
			<Label Height="[float]16" Id="3943f48256a74c39878788859d09830d" LabelOwner="[UIModel]423a23621bf040b585d96903342472f3" Left="[float]239" Text="[string]Double 2D Array Out" Top="[float]462" Width="[float]111" xmlns="http://www.ni.com/PanelCommon" />
			<ArrayGraph Background="[SMSolidColorBrush]#00000000" BaseName="[string]Array Graph" Height="[float]300" Id="30224623887f4abc85df2e71734fa255" Label="[UIModel]ec5b56fee5754a80bc406d962d59e1eb" Left="[float]563" MinWidth="[float]230" PlotAreaMargin="[SMThickness]31,26,7,25" PreferIndexData="[bool]False" RenderMode="[RenderMode]Hardware" SuppressScaleLayout="[bool]False" Top="[float]380" Width="[float]500">
				<ArrayGraphAxis Adjuster="[RangeAdjuster]FitExactly" Id="2d2b84004a184418946c5ad49a596fba" Label="[string]Index" LabelVisibility="[SMVisibility]Collapsed" MajorDivisions="[UIModel]3368f50623b84bf1b84738429e43a7ce" MinorTickVisibility="[SMVisibility]Collapsed" Orientation="[SMOrientation]Horizontal" Range="[IRange]0, 2, System.Double" ValueType="[Type]Double">
					<RangeLabeledDivisions Id="3368f50623b84bf1b84738429e43a7ce" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</ArrayGraphAxis>
				<ArrayGraphAxis Adjuster="[RangeAdjuster]FitExactly" Id="84b74e53723e4b47bd9483cc374e0293" Label="[string]Value" LabelVisibility="[SMVisibility]Collapsed" MajorDivisions="[UIModel]a80145fa77434655a9381356b07c42a3" Orientation="[SMOrientation]Vertical" Range="[IRange]1.5, 6.5, System.Double" ValueType="[Type]Double">
					<RangeLabeledDivisions Id="a80145fa77434655a9381356b07c42a3" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</ArrayGraphAxis>
				<HmiGraphPlot Channel="[string]{d001b29b-5739-42de-9c18-004303c47a0b}/Output/Double 2D Array Out" HorizontalScale="[UIModel]2d2b84004a184418946c5ad49a596fba" Id="9c3b0c99aa5d44dcbfafc66979cbb1ea" IsDefaultPlot="[bool]False" Label="[string]Double 2D Array Out" VerticalScale="[UIModel]84b74e53723e4b47bd9483cc374e0293">
					<PlotRenderer Id="59235c9e6cf44fafb530438c76961ae4" LineStroke="[SMSolidColorBrush]#ffea4225" LineThickness="[double]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</HmiGraphPlot>
			</ArrayGraph>
			<HmiChartPlotLegend Graph="[UIModel]30224623887f4abc85df2e71734fa255" Height="[float]28" Id="89fa6642dd08427b9d797ba4f6b8c02c" Left="[float]1070" Top="[float]380" />
			<HmiChartCursorLegend Graph="[UIModel]30224623887f4abc85df2e71734fa255" Height="[float]80" Id="81f1e3c7379940a6bb622c38fdb893a0" Left="[float]568" MinHeight="[float]80" Top="[float]709" Visible="[bool]False" Width="[float]316" />
			<HmiChartScaleLegend Graph="[UIModel]30224623887f4abc85df2e71734fa255" Height="[float]52" Id="84678c70b4354814871b68e1cbf5610c" Left="[float]988" Top="[float]687" Visible="[bool]False" />
			<ArrayGraphTools BackgroundColor="[SMSolidColorBrush]#fff7f7f7" Graph="[UIModel]30224623887f4abc85df2e71734fa255" Height="[float]26" Id="5b4b80437d2f45b9ab30e6c879069888" Left="[float]909" OffsetX="[float]346" OffsetY="[float]0" Top="[float]380" Width="[float]122">
				<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Horizontal Zoom" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]796a4cb90e6c4ba0af55e89db5b64b12" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="91e014b2ca9b47f69ae77c5c237ee365" IsMomentary="[bool]False" Label="[UIModel]5c8fd09e0f2c420fa01024c5eefe1256" Left="[float]2" PartName="[string]PART_ZoomHorizontalButton" Top="[float]2" Value="[bool]False" Width="[float]28">
					<Image BaseName="[string]Image" Id="796a4cb90e6c4ba0af55e89db5b64b12" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomHorizontal.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
				</ComposableButton>
				<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Vertical Zoom" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]532af7b035cd46cab7c425c34fd4b766" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="dd95704d2f1f487cb145abc75732d0fd" IsMomentary="[bool]False" Label="[UIModel]9f46514aaee24b948852373979bc5b28" Left="[float]32" PartName="[string]PART_ZoomVerticalButton" Top="[float]2" Value="[bool]False" Width="[float]28">
					<Image BaseName="[string]Image" Id="532af7b035cd46cab7c425c34fd4b766" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomVertical.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
				</ComposableButton>
				<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Pan" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]a1a068a92ee74ac6a5a74d48f8c43de8" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="961dbee9005e417887a0d561be0a13e4" IsMomentary="[bool]False" Label="[UIModel]92fb2d045a50408399f350f05164b915" Left="[float]62" PartName="[string]PART_PanButton" Top="[float]2" Value="[bool]False" Width="[float]28">
					<Image BaseName="[string]Image" Id="a1a068a92ee74ac6a5a74d48f8c43de8" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomPan.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
				</ComposableButton>
				<ComposableButton BackingCanDelete="[bool]False" BaseName="[string]Reset" BorderBrush="[SMSolidColorBrush]#00ffffff" Content="[UIModel]6293bdb77e824bd8af0689c0e1b65659" Enabled="[bool]True" FalseBackground="[SMSolidColorBrush]#00ffffff" Height="[float]22" Id="ff4ce97f915241cdb54a704789c769d3" IsMomentary="[bool]True" Label="[UIModel]b7e7b27878654baea46b4ea12eca2683" Left="[float]92" PartName="[string]PART_ResetButton" Top="[float]2" Value="[bool]False" Width="[float]28">
					<Image BaseName="[string]Image" Id="6293bdb77e824bd8af0689c0e1b65659" Left="[float]0" Source="[string]pack://application:,,,/NationalInstruments.Hmi.Core;component/Resources/ZoomExtents.png" Stretch="[SMStretch]Uniform" Top="[float]0" xmlns="http://www.ni.com/PlatformFramework" />
				</ComposableButton>
				<Label Id="5c8fd09e0f2c420fa01024c5eefe1256" LabelOwner="[UIModel]91e014b2ca9b47f69ae77c5c237ee365" Left="[float]2" Text="[string]Horizontal Zoom" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
				<Label Id="9f46514aaee24b948852373979bc5b28" LabelOwner="[UIModel]dd95704d2f1f487cb145abc75732d0fd" Left="[float]32" Text="[string]Vertical Zoom" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
				<Label Id="92fb2d045a50408399f350f05164b915" LabelOwner="[UIModel]961dbee9005e417887a0d561be0a13e4" Left="[float]62" Text="[string]Pan" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
				<Label Id="b7e7b27878654baea46b4ea12eca2683" LabelOwner="[UIModel]ff4ce97f915241cdb54a704789c769d3" Left="[float]92" Text="[string]Reset" Top="[float]-18" Visible="[bool]False" xmlns="http://www.ni.com/PanelCommon" />
			</ArrayGraphTools>
			<Label Height="[float]16" Id="ec5b56fee5754a80bc406d962d59e1eb" LabelOwner="[UIModel]30224623887f4abc85df2e71734fa255" Left="[float]563" Text="[string]Double 2D Array Out Graph" Top="[float]360" Width="[float]147" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelArrayViewer ArrayElement="[UIModel]68047f989f644a6ba80649d08992a488" BaseName="[string]String Array Output" Channel="[string]{d001b29b-5739-42de-9c18-004303c47a0b}/Output/String 2D Array Out" Columns="[int]3" Dimensions="[int]2" FirstIndex="[ArrayElementIndex]0,0" Height="[float]120" Id="7e4848801faf4b8e977f649e3dffcca8" IndexVisibility="[Visibility]Collapsed" IsFixedSize="[bool]False" Label="[UIModel]ddae03c166b643f5947d46bb40aebcb1" Left="[float]239" Orientation="[SMOrientation]Vertical" Rows="[int]4" Top="[float]660" VerticalScrollBarVisibility="[ScrollBarVisibility]Visible" Width="[float]256">
				<p.DefaultElementValue>""</p.DefaultElementValue>
				<ChannelArrayStringControl AcceptsReturn="[bool]False" BaseName="[string]String" Height="[float]24" HorizontalScrollBarVisibility="[ScrollBarVisibility]Hidden" Id="68047f989f644a6ba80649d08992a488" IsReadOnly="[bool]True" VerticalScrollBarVisibility="[ScrollBarVisibility]Auto" Width="[float]72" />
			</ChannelArrayViewer>
			<Label Height="[float]16" Id="ddae03c166b643f5947d46bb40aebcb1" LabelOwner="[UIModel]7e4848801faf4b8e977f649e3dffcca8" Left="[float]239" Text="[string]String 2D Array Out" Top="[float]640" Width="[float]104" xmlns="http://www.ni.com/PanelCommon" />
		</ScreenSurface>
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/SampleMeasurement.instudioproj sha256=14183353a301631a436500d45f6f0d79b3acfe20224d52099039243559dde02e bytes=1534 -->
## FILE: examples/sample_measurement/SampleMeasurement.instudioproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/SampleMeasurement.instudioproj`
- sha256: `14183353a301631a436500d45f6f0d79b3acfe20224d52099039243559dde02e`
- bytes: 1534

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="CCB6B38A5C4AD5B10850DF431B2693A7EA15C1A65460A43141450DDCEC09090BDE8CC5F30F893E9B388A31E9CD2CB4E37EE888EC1024C32CFBB36C73FBD7E3F1" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
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
			<SourceFileReference Bindings="EnvoyManager" Id="18ca4c506614455283f62c6b5059faf2" ModelDefinitionType="NationalInstruments.InstrumentFramework.Document.SourceModel.UnifiedTask" Name="SampleMeasurement.sfp" StoragePath="SampleMeasurement.sfp" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/SampleMeasurement.measproj sha256=a07fd23b6e1bd30210223adc8b2b5152821121179dfdb219dd74462e8aaa6150 bytes=3547 -->
## FILE: examples/sample_measurement/SampleMeasurement.measproj

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/SampleMeasurement.measproj`
- sha256: `a07fd23b6e1bd30210223adc8b2b5152821121179dfdb219dd74462e8aaa6150`
- bytes: 3547

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="BC8BFA80E0B905304D1AE67DB52454587629D79605B074D83CC7565D62DD52FF92604256E63A401E7F0386E11CF7E752B9538053AFC832ADF7FEBF6A22C6BD72" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="23.0.0.2171" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2171" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2171" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/EnvoyManagement" OldestCompatibleVersion="5.0.0.0" Version="5.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2171" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemDiagram" OldestCompatibleVersion="8.0.0.49152" Version="8.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2171" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemModelCore" OldestCompatibleVersion="5.1.0.5" Version="5.2.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.2171" Name="MeasurementLink UI Editor" Version="23.0.0.2171" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="31e8f33f280f42eb99620eee6564f7b3" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="a4ca11716edf418bbeb9792924bc4ecd" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<EmbeddedDefinitionReference Id="e9e79f49b5d642388fca03d9baadc351" ModelDefinitionType="NationalInstruments.SystemDesigner.SystemDiagram.SystemDiagramDefinition" Name="SystemDiagram">
			<SystemDiagram Id="90ea4d01eed1424e998680dc2da42e3e" SystemDiagramVersion="75" xmlns="http://www.ni.com/SystemDesigner/SystemDiagram">
				<EnvoySuperimpositionContainer Id="69ab69b1ff8343189d99511e4e89a890" xmlns="http://www.ni.com/SystemDesigner/EnvoyManagement">
					<MappingManager Id="4a726ecdef7b4947b20f6072d516e191" xmlns="http://www.ni.com/SystemDesigner/SystemModelCore">
						<Superimposition Id="1db8e70ca9cb4c64b13133d4b234008a" Name="Root Superimposition" />
					</MappingManager>
				</EnvoySuperimpositionContainer>
				<SystemDiagramRootDiagram Id="5fde857173f442d18776893f1d0e903d" />
			</SystemDiagram>
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="83bdf6353f18496aad809944af0b81dc" ModelDefinitionType="NullTarget" Name="NullTarget">
			<NullTarget />
		</NameScopingEnvoy>
		<NameScopingEnvoy Id="ec73c62cc57043248dff173143fb18a3" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Id="ed88988cedad40a683137bad2c3ebd0c" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="SampleMeasurement.measui" StoragePath="SampleMeasurement.measui" />
			<SourceFileReference Id="79a495070374e03a250fbfc39957002" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="SampleAllParameters.measui" StoragePath="SampleAllParameters.measui" />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/SampleMeasurement.measui sha256=72abf5d4c76518eefa2d4745b0ea5b3cd01339bb922f0ed11cb5f3482821b706 bytes=15139 -->
## FILE: examples/sample_measurement/SampleMeasurement.measui

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/SampleMeasurement.measui`
- sha256: `72abf5d4c76518eefa2d4745b0ea5b3cd01339bb922f0ed11cb5f3482821b706`
- bytes: 15139

````json
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="BF3A4D3B8F63CD67E21808758935710E168D72CF135C2BB5E51066A90F63832154A4210DA5E78840A928A505E8224EE116152426906494ECF649C04592BEB594" Timestamp="1D9B41F1346B243" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.9.0.2752" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="9.8.1.49152" />
		<ParsableNamespace AssemblyFileVersion="9.9.0.2752" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="23.5.0.2752" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.9.0.2752" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.9.0.2752" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.5.0.2752" Name="MeasurementLink UI Editor" Version="23.5.0.2752" />
	</SourceModelFeatureSet>
	<Screen ClientId="{abd0ec1b-8a8a-46a1-9b11-1bcb569d1849}" DisplayName="Sample Measurement (Py)" Id="20c496a981bb4f73bea9d243756baab5" ServiceClass="ni.examples.SampleMeasurement_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
		<ScreenSurface BackgroundColor="[SMSolidColorBrush]#00ffffff" Height="[float]584" Id="c47bc3494c0244bab74b59853ae5087f" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]520" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
			<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]433" Id="fffb5b06943547a396f235c6ca5ecec0" Label="[UIModel]d888986072c24f82b8e05e2ec57eb3f9" Left="[float]40" Top="[float]40" Width="[float]200">
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{abd0ec1b-8a8a-46a1-9b11-1bcb569d1849}/Configuration/Float In" Enabled="[bool]True" Height="[float]24" Id="ac8d5d6abc13430eba5b9b5008242f2e" Interval="[float]1" Label="[UIModel]b16b7fdf2cd2444aaba612c28dff288c" Left="[float]20" Top="[float]36" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=5:DigitDisplayType=SignificantDigits:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Single" Width="[float]160" />
				<ChannelCheckBox BaseName="[string]Checkbox" Channel="[string]{abd0ec1b-8a8a-46a1-9b11-1bcb569d1849}/Configuration/Bool In" Content="[string]Off/On" Enabled="[bool]True" Height="[float]16" Id="50072f6dacfc4f4cbbcf875d6d8483cd" Label="[UIModel]72b5606765b48f6a03e01d0505d78c9" Left="[float]20" MinHeight="[float]16" MinWidth="[float]16" Top="[float]86" Width="[float]59" />
				<ChannelStringControl AcceptsReturn="[bool]False" BaseName="[string]String" Channel="[string]{abd0ec1b-8a8a-46a1-9b11-1bcb569d1849}/Configuration/String In" Enabled="[bool]True" Height="[float]24" HorizontalScrollBarVisibility="[ScrollBarVisibility]Hidden" Id="344fe1d909e0448ca0923ced1bcdcb12" Label="[UIModel]4b4dcad2a0248e58564c645943b0c7f" Left="[float]20" Text="[string]" Top="[float]136" VerticalScrollBarVisibility="[ScrollBarVisibility]Auto" Width="[float]160" />
				<ChannelArrayViewer AdaptsToType="[bool]True" ArrayElement="[UIModel]4e1d7f76fed3408c879928fcf2039e63" BaseName="[string]Numeric Array Input" Channel="[string]{abd0ec1b-8a8a-46a1-9b11-1bcb569d1849}/Configuration/Double Array In" Columns="[int]1" Dimensions="[int]1" Enabled="[bool]True" Height="[float]120" Id="2d88c55ec56e4ee58ddb2acd0bee73b0" IndexVisibility="[Visibility]Collapsed" IsFixedSize="[bool]False" Label="[UIModel]3d3aa154901d4d738857fa48bddcef45" Left="[float]20" Orientation="[SMOrientation]Vertical" Rows="[int]4" Top="[float]189" VerticalScrollBarVisibility="[ScrollBarVisibility]Visible" Width="[float]161">
					<p.DefaultElementValue>0x0</p.DefaultElementValue>
					<ChannelArrayNumericText BaseName="[string]Numeric" Height="[float]24" Id="4e1d7f76fed3408c879928fcf2039e63" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]129" />
				</ChannelArrayViewer>
				<Label Height="[float]16" Id="b16b7fdf2cd2444aaba612c28dff288c" LabelOwner="[UIModel]ac8d5d6abc13430eba5b9b5008242f2e" Left="[float]20" Text="[string]Float In" Top="[float]16" Width="[float]39" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="72b5606765b48f6a03e01d0505d78c9" LabelOwner="[UIModel]50072f6dacfc4f4cbbcf875d6d8483cd" Left="[float]20" Text="[string]Bool In" Top="[float]66" Width="[float]37" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="4b4dcad2a0248e58564c645943b0c7f" LabelOwner="[UIModel]344fe1d909e0448ca0923ced1bcdcb12" Left="[float]20" Text="[string]String In" Top="[float]116" Width="[float]44" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="3d3aa154901d4d738857fa48bddcef45" LabelOwner="[UIModel]2d88c55ec56e4ee58ddb2acd0bee73b0" Left="[float]20" Text="[string]Double Array In" Top="[float]169" Width="[float]83" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{abd0ec1b-8a8a-46a1-9b11-1bcb569d1849}/Configuration/Enum In" Enabled="[bool]True" Height="[float]24" Id="33e5cf243ae245539701fc21c46efa41" Label="[UIModel]c182b2b570bd4e6493cae1b9ca0c48da" Left="[float]20" Top="[float]338" Value="[int]3" Width="[float]136" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
					<RingSelectorInfo DisplayValue="[string]NONE" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]RED" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]GREEN" IsEnabled="[bool]True" Value="[int]2" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]BLUE" IsEnabled="[bool]True" Value="[int]3" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</ChannelEnumSelector>
				<Label Height="[float]16" Id="c182b2b570bd4e6493cae1b9ca0c48da" LabelOwner="[UIModel]33e5cf243ae245539701fc21c46efa41" Left="[float]20" Text="[string]Enum In" Top="[float]318" Width="[float]43" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{abd0ec1b-8a8a-46a1-9b11-1bcb569d1849}/Configuration/Protobuf Enum In" Height="[float]24" Id="c2d051529074418c86df329f1f219acf" Label="[UIModel]f57dbfc67ccd40b79df5a0889c80ff6e" Left="[float]20" Top="[float]391" Value="[int]2" Width="[float]136" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
					<RingSelectorInfo DisplayValue="[string]NONE" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]PINK" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]WHITE" IsEnabled="[bool]True" Value="[int]2" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]BLACK" IsEnabled="[bool]True" Value="[int]3" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</ChannelEnumSelector>
				<Label Height="[float]16" Id="f57dbfc67ccd40b79df5a0889c80ff6e" LabelOwner="[UIModel]c2d051529074418c86df329f1f219acf" Left="[float]20" Text="[string]Protobuf Enum In" Top="[float]371" Width="[float]93" xmlns="http://www.ni.com/PanelCommon" />
			</ScreenSurfaceCanvas>
			<Label Height="[float]16" Id="d888986072c24f82b8e05e2ec57eb3f9" LabelOwner="[UIModel]fffb5b06943547a396f235c6ca5ecec0" Left="[float]40" Text="[string]Measurement Configurations" Top="[float]20" Width="[float]154" xmlns="http://www.ni.com/PanelCommon" />
			<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]433" Id="4529f322894b4776bfb6b3225510bece" Label="[UIModel]ad9e246b917f444084b85d7ef2cc0b0e" Left="[float]280" Top="[float]40" Width="[float]200">
				<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{abd0ec1b-8a8a-46a1-9b11-1bcb569d1849}/Output/Float out" Height="[float]24" Id="560b0851e24b4be1957fc505ed62f5db" Interval="[float]1" IsReadOnly="[bool]True" Label="[UIModel]a73c7bd96aae4a3792867b1f471247cc" Left="[float]20" Top="[float]36" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=5:DigitDisplayType=SignificantDigits:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Single" Width="[float]160" />
				<ChannelStringControl AcceptsReturn="[bool]False" BaseName="[string]String" Channel="[string]{abd0ec1b-8a8a-46a1-9b11-1bcb569d1849}/Output/String out" Height="[float]24" HorizontalScrollBarVisibility="[ScrollBarVisibility]Hidden" Id="fa35489e33a34b0183b746fffa2ced9d" IsReadOnly="[bool]True" Label="[UIModel]94b2b204aefb4bc7b509f1c49eae0c18" Left="[float]20" Top="[float]136" VerticalScrollBarVisibility="[ScrollBarVisibility]Auto" Width="[float]160" />
				<ChannelArrayViewer AdaptsToType="[bool]True" ArrayElement="[UIModel]9845cec681cb4828a587b9fd395fa78c" BaseName="[string]Numeric Array Output" Channel="[string]{abd0ec1b-8a8a-46a1-9b11-1bcb569d1849}/Output/Double Array out" Columns="[int]1" Dimensions="[int]1" Height="[float]120" Id="13707da33a16404e92bf506121dc2dbc" IndexVisibility="[Visibility]Collapsed" IsFixedSize="[bool]False" Label="[UIModel]4d641544433e4a3ab6f691b85e44d2d2" Left="[float]20" Orientation="[SMOrientation]Vertical" Rows="[int]4" Top="[float]189" VerticalScrollBarVisibility="[ScrollBarVisibility]Visible" Width="[float]160">
					<p.DefaultElementValue>0x0</p.DefaultElementValue>
					<ChannelArrayNumericText BaseName="[string]Numeric" Height="[float]24" Id="9845cec681cb4828a587b9fd395fa78c" IsReadOnly="[bool]True" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]128" />
				</ChannelArrayViewer>
				<Label Height="[float]16" Id="a73c7bd96aae4a3792867b1f471247cc" LabelOwner="[UIModel]560b0851e24b4be1957fc505ed62f5db" Left="[float]20" Text="[string]Float out" Top="[float]16" Width="[float]47" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="94b2b204aefb4bc7b509f1c49eae0c18" LabelOwner="[UIModel]fa35489e33a34b0183b746fffa2ced9d" Left="[float]20" Text="[string]String out" Top="[float]116" Width="[float]52" xmlns="http://www.ni.com/PanelCommon" />
				<Label Height="[float]16" Id="4d641544433e4a3ab6f691b85e44d2d2" LabelOwner="[UIModel]13707da33a16404e92bf506121dc2dbc" Left="[float]20" Text="[string]Double Array out" Top="[float]169" Width="[float]91" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelLED BaseName="[string]Round LED" Channel="[string]{abd0ec1b-8a8a-46a1-9b11-1bcb569d1849}/Output/Bool out" ContentVisibility="[Visibility]Collapsed" FalseBackground="[SMSolidColorBrush]#ffe0e0e0" FalseContent="[string]Off" Height="[float]20" Id="529587ea90ea4255aec8f53606bc99b9" IsReadOnly="[bool]True" Label="[UIModel]aff1aad914904ce6a6fb6756cba2c866" Left="[float]20" MinHeight="[float]20" MinWidth="[float]20" Shape="[LEDShape]Round" Top="[float]86" TrueContent="[string]On" Width="[float]20" />
				<Label Height="[float]16" Id="aff1aad914904ce6a6fb6756cba2c866" LabelOwner="[UIModel]529587ea90ea4255aec8f53606bc99b9" Left="[float]20" Text="[string]Bool out" Top="[float]66" Width="[float]45" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{abd0ec1b-8a8a-46a1-9b11-1bcb569d1849}/Output/Enum out" Height="[float]24" Id="7bf69cb592c94751994034c3bf82f3ec" InteractionMode="[SelectorInteractionModes]ReadOnly" Label="[UIModel]10e555f297064f69a8592ac81056f258" Left="[float]20" Top="[float]338" Width="[float]136" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
					<RingSelectorInfo DisplayValue="[string]NONE" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]RED" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]GREEN" IsEnabled="[bool]True" Value="[int]2" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]BLUE" IsEnabled="[bool]True" Value="[int]3" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</ChannelEnumSelector>
				<Label Height="[float]16" Id="10e555f297064f69a8592ac81056f258" LabelOwner="[UIModel]7bf69cb592c94751994034c3bf82f3ec" Left="[float]20" Text="[string]Enum out" Top="[float]318" Width="[float]51" xmlns="http://www.ni.com/PanelCommon" />
				<ChannelEnumSelector AdaptsToType="[bool]True" AllowNonSequentialValues="[bool]True" BaseName="[string]Enum" Channel="[string]{abd0ec1b-8a8a-46a1-9b11-1bcb569d1849}/Output/Protobuf Enum out" Height="[float]24" Id="7ef80156f0c24fdb8f396dce29e4ce08" InteractionMode="[SelectorInteractionModes]ReadOnly" Label="[UIModel]6218206692554da9b8943b1841d33307" Left="[float]20" Top="[float]391" Width="[float]136" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
					<RingSelectorInfo DisplayValue="[string]NONE" IsEnabled="[bool]True" Value="[int]0" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]PINK" IsEnabled="[bool]True" Value="[int]1" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]WHITE" IsEnabled="[bool]True" Value="[int]2" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
					<RingSelectorInfo DisplayValue="[string]BLACK" IsEnabled="[bool]True" Value="[int]3" xmlns="http://www.ni.com/Controls.LabVIEW.Design" />
				</ChannelEnumSelector>
				<Label Height="[float]16" Id="6218206692554da9b8943b1841d33307" LabelOwner="[UIModel]7ef80156f0c24fdb8f396dce29e4ce08" Left="[float]20" Text="[string]Protobuf Enum out" Top="[float]371" Width="[float]101" xmlns="http://www.ni.com/PanelCommon" />
			</ScreenSurfaceCanvas>
			<Label Height="[float]16" Id="ad9e246b917f444084b85d7ef2cc0b0e" LabelOwner="[UIModel]4529f322894b4776bfb6b3225510bece" Left="[float]280" Text="[string]Measurement Results" Top="[float]20" Width="[float]113" xmlns="http://www.ni.com/PanelCommon" />
		</ScreenSurface>
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/SampleMeasurement.serviceconfig sha256=e6785967d636973a282d618b1601b04a04ff34b8a6d7071d089c2cc50cceafe8 bytes=686 -->
## FILE: examples/sample_measurement/SampleMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/SampleMeasurement.serviceconfig`
- sha256: `e6785967d636973a282d618b1601b04a04ff34b8a6d7071d089c2cc50cceafe8`
- bytes: 686

````json
{
  "services": [
    {
      "displayName": "Sample Measurement (Py)",
      "version": "1.0.0",
      "serviceClass": "ni.examples.SampleMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "installPath": "install.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in example that performs a loopback measurement with various data types.",
        "ni/service.collection": "NI.Examples",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/SampleMeasurement.sfp sha256=801b2a5f2cd808d89517bb042318bdd5a6e94eb5965fccf78013d00dbb5645d3 bytes=12875 -->
## FILE: examples/sample_measurement/SampleMeasurement.sfp

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/SampleMeasurement.sfp`
- sha256: `801b2a5f2cd808d89517bb042318bdd5a6e94eb5965fccf78013d00dbb5645d3`
- bytes: 12875

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="DA513D6DFD9A4B1396714E129B2FE7577C3B644A815E2FE81E1CABF934CAC2252DCA9A9C4B8FF546FFAFA79FC153B5A3901385BD84DB42E40ADB75BC8818441C" Timestamp="1D909E13862C143" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.7.0.2317" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="6.3.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2317" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="23.0.0.2317" FeatureSetName="UnifiedTask" Name="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" Version="1.0.0.0" />
		<ParsableNamespace AssemblyFileVersion="23.0.0.2317" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="22.1.0.1" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2317" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.7.0.2317" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="23.0.0.2317" Name="InstrumentStudio" PersistenceVersion="22.1.0.0" Version="23.0.0.2317" />
	</SourceModelFeatureSet>
	<UnifiedTask Id="9b5cc1f1d3284e55bee48a0e661dde7d" LayoutInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0,&quot;Layout Information&quot;:{&quot;Sections&quot;:[{&quot;Columns Progressive Count&quot;:1,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Columns&quot;:[{&quot;Containers Progressive Count&quot;:1,&quot;Layout Information Index&quot;:0,&quot;Containers&quot;:[{&quot;Container Model Defition&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Container Assignment State&quot;:&quot;Available&quot;,&quot;Container Identifier&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen.task&quot;,&quot;Container Instrument Name&quot;:&quot;Sample Measurement (Py)&quot;,&quot;Layout Information Name&quot;:&quot;Sample Measurement (Py) 1&quot;,&quot;Layout Information Index&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationWithVisualization&quot;,&quot;Items&quot;:[{&quot;Identification Number&quot;:4294963201,&quot;Model Definition Type&quot;:&quot;{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen&quot;,&quot;Parent Or Group Name&quot;:&quot;Measurements&quot;,&quot;Panel Type&quot;:&quot;Sample Measurement (Py)&quot;,&quot;Layout Information Name&quot;:&quot;ni.examples.SampleMeasurement_Python&quot;,&quot;Layout Information Index&quot;:0}]}]}]},{&quot;Columns Progressive Count&quot;:0,&quot;Layout Information Presentation&quot;:&quot;ConfigurationOnly&quot;}]}}" PinAwareInformation="{&quot;Format Version&quot;:1,&quot;Application Format Version&quot;:23.0}" xmlns="http://www.ni.com/InstrumentFramework/Document/SourceModel/UnifiedSoftFrontPanel" />
	<EnvoyManagerFile Id="9844183c1b73437496caa985ccce05b7" xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="587dd68141d94bffb14d6455393cd4d7" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<NameScopingEnvoy AutomaticallyResolveUp="True" Id="d2536d9c87714778b469fd5b8f60ef7f" Name="SampleMeasurement.sfp" NameTracksFileName="True" />
		<EmbeddedDefinitionReference Id="858d52f78c104f92a91bf484da3014a8" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="{http\://www.ni.com/InstrumentFramework/ScreenDocument}Screen.task">
			<Screen ClientId="{c67a0b30-2590-499f-9b92-dbd2ef02233c}" ConfigurationParameters="{&quot;@type&quot;:&quot;type.googleapis.com/ni.measurementlink.measurement.v1.MeasurementConfigurations&quot;,&quot;float in&quot;:0.06,&quot;double array in&quot;:[0.1,0.2,0.3],&quot;bool in&quot;:false,&quot;string in&quot;:&quot;sample string&quot;,&quot;string array in&quot;:[&quot;String1&quot;,&quot;String2&quot;]}" DisplayName="Sample Measurement (Py)" Id="2d74334dc63b4ff29830a334f7fa9511" PanelPresentation="ConfigurationWithVisualization" ServiceClass="ni.examples.SampleMeasurement_Python" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
				<ScreenSurface BackgroundColor="[SMSolidColorBrush]#00ffffff" Height="[float]400" Id="bbf34c790d12482a9040e3dbe4d1f036" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]520" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
					<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]325" Id="63f3c0b3d765416388045a501a5fdf9a" Label="[UIModel]9412b3f43074f3ea937b4563f375d43" Left="[float]40" Top="[float]40" Width="[float]200">
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{c67a0b30-2590-499f-9b92-dbd2ef02233c}/Configuration/Float In" Height="[float]24" Id="d74366e5c4c4b8fbfa8c86319abe6d9" Interval="[float]1" Label="[UIModel]5995c9e2752d4d3c934e7a3cd2353dde" Left="[float]20" Top="[float]36" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=5:DigitDisplayType=SignificantDigits:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Single" Width="[float]160" />
						<ChannelCheckBox BaseName="[string]Checkbox" Channel="[string]{c67a0b30-2590-499f-9b92-dbd2ef02233c}/Configuration/Bool In" Content="[string]Off/On" Height="[float]16" Id="1f8b4ebd6ca2473dbac7ab26eb83aba0" Label="[UIModel]220695e27b984640a119da4b84d6712a" Left="[float]20" MinHeight="[float]16" MinWidth="[float]16" Top="[float]86" Width="[float]59" />
						<ChannelStringControl AcceptsReturn="[bool]False" BaseName="[string]String" Channel="[string]{c67a0b30-2590-499f-9b92-dbd2ef02233c}/Configuration/String In" Height="[float]24" HorizontalScrollBarVisibility="[ScrollBarVisibility]Hidden" Id="9dd1b793357746f1b131952bdb8e174c" Label="[UIModel]5d6753bf525c434cbdc4538d704076b2" Left="[float]20" Text="[string]" Top="[float]136" VerticalScrollBarVisibility="[ScrollBarVisibility]Auto" Width="[float]160" />
						<ChannelArrayViewer AdaptsToType="[bool]True" ArrayElement="[UIModel]539b39e7d145433cb9e72ccb8bf6174c" BaseName="[string]Numeric Array Input" Channel="[string]{c67a0b30-2590-499f-9b92-dbd2ef02233c}/Configuration/Double Array In" Columns="[int]1" Dimensions="[int]1" Height="[float]120" Id="d475dea1a458444aab63bb997b511e28" IndexVisibility="[Visibility]Collapsed" Label="[UIModel]1eaa99e5e4104d7096dc335f652423e3" Left="[float]20" Orientation="[SMOrientation]Vertical" Rows="[int]4" Top="[float]189" VerticalScrollBarVisibility="[ScrollBarVisibility]Visible" Width="[float]161">
							<p.DefaultElementValue>0x0</p.DefaultElementValue>
							<ChannelArrayNumericText BaseName="[string]Numeric" Height="[float]24" Id="539b39e7d145433cb9e72ccb8bf6174c" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]129" />
						</ChannelArrayViewer>
						<Label Height="[float]16" Id="5995c9e2752d4d3c934e7a3cd2353dde" LabelOwner="[UIModel]d74366e5c4c4b8fbfa8c86319abe6d9" Left="[float]20" Text="[string]Float In" Top="[float]16" Width="[float]39" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="220695e27b984640a119da4b84d6712a" LabelOwner="[UIModel]1f8b4ebd6ca2473dbac7ab26eb83aba0" Left="[float]20" Text="[string]Bool In" Top="[float]66" Width="[float]37" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="5d6753bf525c434cbdc4538d704076b2" LabelOwner="[UIModel]9dd1b793357746f1b131952bdb8e174c" Left="[float]20" Text="[string]String In" Top="[float]116" Width="[float]44" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="1eaa99e5e4104d7096dc335f652423e3" LabelOwner="[UIModel]d475dea1a458444aab63bb997b511e28" Left="[float]20" Text="[string]Double Array In" Top="[float]169" Width="[float]83" xmlns="http://www.ni.com/PanelCommon" />
					</ScreenSurfaceCanvas>
					<Label Height="[float]16" Id="9412b3f43074f3ea937b4563f375d43" LabelOwner="[UIModel]63f3c0b3d765416388045a501a5fdf9a" Left="[float]40" Text="[string]Measurement Configurations" Top="[float]20" Width="[float]154" xmlns="http://www.ni.com/PanelCommon" />
					<ScreenSurfaceCanvas Background="[SMSolidColorBrush]#80808080" BackgroundColor="[SMSolidColorBrush]#ffe0e0e0" BaseName="[string]Canvas" Height="[float]325" Id="d101d0129cee4bc6bbe2849c36ad13c3" Label="[UIModel]1a64390e7e694ed88f7a8970307ba409" Left="[float]280" Top="[float]40" Width="[float]200">
						<ChannelNumericText AdaptsToType="[bool]True" BaseName="[string]Numeric" Channel="[string]{c67a0b30-2590-499f-9b92-dbd2ef02233c}/Output/Float out" Height="[float]24" Id="8ae999990fe6404eb70f626b631f0f49" Interval="[float]1" IsReadOnly="[bool]True" Label="[UIModel]72458802075f48aaa19f11d10ccaacdb" Left="[float]20" Top="[float]36" UnitAnnotation="[string]" ValueFormatter="[string]DisplayFormat=Automatic:Digits=5:DigitDisplayType=SignificantDigits:MinimumFieldWidth=0:AlwaysShowSign=False:ShowThousandsSeparator=False" ValueType="[Type]Single" Width="[float]160" />
						<ChannelStringControl AcceptsReturn="[bool]False" BaseName="[string]String" Channel="[string]{c67a0b30-2590-499f-9b92-dbd2ef02233c}/Output/String out" Height="[float]24" HorizontalScrollBarVisibility="[ScrollBarVisibility]Hidden" Id="ba5235530ad24e239541183c30f7e00f" IsReadOnly="[bool]True" Label="[UIModel]cd6c220c4acf4480a00b792c83e3009d" Left="[float]20" Top="[float]136" VerticalScrollBarVisibility="[ScrollBarVisibility]Auto" Width="[float]160" />
						<ChannelArrayViewer AdaptsToType="[bool]True" ArrayElement="[UIModel]7f88ce737b34080a6a5ff80e3ac2b9c" BaseName="[string]Numeric Array Output" Channel="[string]{c67a0b30-2590-499f-9b92-dbd2ef02233c}/Output/Double Array out" Columns="[int]1" Dimensions="[int]1" Height="[float]120" Id="acbe7b94c544d3abbb5028bd9c5f942" IndexVisibility="[Visibility]Collapsed" Label="[UIModel]90f456db88de4898b68eea00672453e1" Left="[float]20" Orientation="[SMOrientation]Vertical" Rows="[int]4" Top="[float]189" VerticalScrollBarVisibility="[ScrollBarVisibility]Visible" Width="[float]160">
							<p.DefaultElementValue>0x0</p.DefaultElementValue>
							<ChannelArrayNumericText BaseName="[string]Numeric" Height="[float]24" Id="7f88ce737b34080a6a5ff80e3ac2b9c" IsReadOnly="[bool]True" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]128" />
						</ChannelArrayViewer>
						<Label Height="[float]16" Id="72458802075f48aaa19f11d10ccaacdb" LabelOwner="[UIModel]8ae999990fe6404eb70f626b631f0f49" Left="[float]20" Text="[string]Float out" Top="[float]16" Width="[float]47" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="cd6c220c4acf4480a00b792c83e3009d" LabelOwner="[UIModel]ba5235530ad24e239541183c30f7e00f" Left="[float]20" Text="[string]String out" Top="[float]116" Width="[float]52" xmlns="http://www.ni.com/PanelCommon" />
						<Label Height="[float]16" Id="90f456db88de4898b68eea00672453e1" LabelOwner="[UIModel]acbe7b94c544d3abbb5028bd9c5f942" Left="[float]20" Text="[string]Double Array out" Top="[float]169" Width="[float]91" xmlns="http://www.ni.com/PanelCommon" />
						<ChannelLED BaseName="[string]Round LED" Channel="[string]{c67a0b30-2590-499f-9b92-dbd2ef02233c}/Output/Bool out" ContentVisibility="[Visibility]Collapsed" FalseBackground="[SMSolidColorBrush]#ffe0e0e0" FalseContent="[string]Off" Height="[float]20" Id="c6793b706c0646759068d476a001d5e0" IsReadOnly="[bool]True" Label="[UIModel]47ae485834304551b34fdd2a842b3665" Left="[float]20" MinHeight="[float]20" MinWidth="[float]20" Shape="[LEDShape]Round" Top="[float]86" TrueContent="[string]On" Width="[float]20" />
						<Label Height="[float]16" Id="47ae485834304551b34fdd2a842b3665" LabelOwner="[UIModel]c6793b706c0646759068d476a001d5e0" Left="[float]20" Text="[string]Bool out" Top="[float]66" Width="[float]45" xmlns="http://www.ni.com/PanelCommon" />
					</ScreenSurfaceCanvas>
					<Label Height="[float]16" Id="1a64390e7e694ed88f7a8970307ba409" LabelOwner="[UIModel]d101d0129cee4bc6bbe2849c36ad13c3" Left="[float]280" Text="[string]Measurement Results" Top="[float]20" Width="[float]113" xmlns="http://www.ni.com/PanelCommon" />
				</ScreenSurface>
			</Screen>
		</EmbeddedDefinitionReference>
	</EnvoyManagerFile>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=examples/sample_measurement/start.bat sha256=bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851 bytes=253 -->
## FILE: examples/sample_measurement/start.bat

- repository: `ni/measurement-plugin-python`
- source_path: `examples/sample_measurement/start.bat`
- sha256: `bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851`
- bytes: 253

````batch
@echo off
REM The discovery service uses this script to start the measurement service.
REM You can customize this script for your Python setup. The -v option logs
REM messages with level INFO and above.

.venv\Scripts\python.exe measurement.py -v
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=LICENSE sha256=dc3be6f9a41cc094419bf22fda26abba350bedd49238727e156a8d297adce9f7 bytes=1091 -->
## FILE: LICENSE

- repository: `ni/measurement-plugin-python`
- source_path: `LICENSE`
- sha256: `dc3be6f9a41cc094419bf22fda26abba350bedd49238727e156a8d297adce9f7`
- bytes: 1091

````text
Copyright (c) 2021, National Instruments Corp.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/__init__.py sha256=f5cf145224c9dfd5c00d0cfc2b030362857d8705d85f1f6cfb1884d03b420b65 bytes=47 -->
## FILE: packages/generator/ni_measurement_plugin_sdk_generator/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/ni_measurement_plugin_sdk_generator/__init__.py`
- sha256: `f5cf145224c9dfd5c00d0cfc2b030362857d8705d85f1f6cfb1884d03b420b65`
- bytes: 47

````python
"""Measurement Plug-In SDK Code Generator."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/client/__init__.py sha256=e7e1952867323db85bacc3b5664d69f79afdd16c7b588bd955f0baafdf9ed713 bytes=12507 -->
## FILE: packages/generator/ni_measurement_plugin_sdk_generator/client/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/ni_measurement_plugin_sdk_generator/client/__init__.py`
- sha256: `e7e1952867323db85bacc3b5664d69f79afdd16c7b588bd955f0baafdf9ed713`
- bytes: 12507

````python
"""Utilizes command line args to create a Measurement Plug-In Client using template files."""

from __future__ import annotations

import logging
import pathlib
from enum import Enum
from typing import Any

import black
import click
from click_option_group import RequiredMutuallyExclusiveOptionGroup, optgroup
from mako.template import Template
from ni.measurementlink.discovery.v1.client import DiscoveryClient
from ni.measurementlink.measurement.v2 import (
    measurement_service_pb2 as v2_measurement_service_pb2,
)
from ni_grpc_extensions.channelpool import GrpcChannelPool

from ni_measurement_plugin_sdk_generator.client._support import (
    create_class_name,
    create_module_name,
    extract_base_service_class,
    get_all_registered_measurement_info,
    get_configuration_and_output_metadata_by_index,
    get_configuration_parameters_with_type_and_default_values,
    get_measurement_service_stub_and_version,
    get_output_parameters_with_type,
    get_selected_measurement_service_class,
    resolve_output_directory,
    to_ordered_set,
    validate_identifier,
    validate_measurement_service_classes,
)

_CLIENT_CREATION_ERROR_MESSAGE = "Client creation failed for '{}'. Possible reason(s): {}"


def _render_template(template_name: str, **template_args: Any) -> bytes:
    file_path = str(pathlib.Path(__file__).parent / "templates" / template_name)
    template = Template(filename=file_path, input_encoding="utf-8", output_encoding="utf-8")
    return template.render(**template_args)


def _create_file(
    template_name: str, file_name: str, directory_out: pathlib.Path, **template_args: Any
) -> None:
    output_file = directory_out / file_name

    output = _render_template(template_name, **template_args).decode("utf-8")
    formatted_output = black.format_str(
        src_contents=output,
        mode=black.Mode(line_length=100),
    )

    with output_file.open("w", encoding="utf-8") as file:
        file.write(formatted_output)


def _create_client(
    discovery_client: DiscoveryClient,
    channel_pool: GrpcChannelPool,
    measurement_service_class: str,
    module_name: str,
    class_name: str,
    directory_out: pathlib.Path,
    generated_modules: list[str],
) -> None:
    built_in_import_modules: list[str] = []
    custom_import_modules: list[str] = []
    enum_values_by_type: dict[type[Enum], dict[str, int]] = {}
    type_url_prefix = "type.googleapis.com/"

    measurement_service_stub, measurement_version = get_measurement_service_stub_and_version(
        discovery_client, channel_pool, measurement_service_class
    )
    metadata = measurement_service_stub.GetMetadata(v2_measurement_service_pb2.GetMetadataRequest())
    configuration_metadata, output_metadata = get_configuration_and_output_metadata_by_index(
        metadata, measurement_service_class, enum_values_by_type
    )

    configuration_parameters_with_type_and_default_values, measure_api_parameters = (
        get_configuration_parameters_with_type_and_default_values(
            configuration_metadata, built_in_import_modules, enum_values_by_type
        )
    )
    output_parameters_with_type = get_output_parameters_with_type(
        output_metadata, built_in_import_modules, custom_import_modules, enum_values_by_type
    )
    custom_import_modules.sort()

    _create_file(
        template_name="measurement_plugin_client.py.mako",
        file_name=f"{module_name}.py",
        directory_out=directory_out,
        class_name=class_name,
        display_name=metadata.measurement_details.display_name,
        version=measurement_version,
        configuration_metadata=configuration_metadata,
        output_metadata=output_metadata,
        service_class=measurement_service_class,
        configuration_parameters_with_type_and_default_values=configuration_parameters_with_type_and_default_values,
        measure_api_parameters=measure_api_parameters,
        output_parameters_with_type=output_parameters_with_type,
        built_in_import_modules=to_ordered_set(built_in_import_modules),
        custom_import_modules=to_ordered_set(custom_import_modules),
        enum_by_class_name=enum_values_by_type,
        configuration_parameters_type_url=type_url_prefix
        + metadata.measurement_signature.configuration_parameters_message_type,
        outputs_message_type=metadata.measurement_signature.outputs_message_type,
    )

    generated_modules.append(module_name)
    print(
        f"The measurement plug-in client for the service class '{measurement_service_class}' has been successfully created as '{module_name}.py'."
    )


def _create_all_clients(directory_out: str | None) -> None:
    channel_pool = GrpcChannelPool()
    discovery_client = DiscoveryClient(grpc_channel_pool=channel_pool)

    generated_modules: list[str] = []
    errors: list[str] = []
    directory_out_path = resolve_output_directory(directory_out)
    measurement_service_classes, _ = get_all_registered_measurement_info(discovery_client)
    validate_measurement_service_classes(measurement_service_classes)

    for service_class in measurement_service_classes:
        try:
            base_service_class = extract_base_service_class(service_class)
            module_name = create_module_name(base_service_class, generated_modules)
            class_name = create_class_name(base_service_class)
            validate_identifier(module_name, "module")
            validate_identifier(class_name, "class")

            _create_client(
                channel_pool=channel_pool,
                discovery_client=discovery_client,
                measurement_service_class=service_class,
                module_name=module_name,
                class_name=class_name,
                directory_out=directory_out_path,
                generated_modules=generated_modules,
            )
        except Exception as e:
            errors.append(_CLIENT_CREATION_ERROR_MESSAGE.format(service_class, e))

    if len(errors) == 1:
        raise click.ClickException(errors[0])
    elif len(errors) > 1:
        raise click.ClickException(
            "Client creation failed for multiple measurement plug-ins:\n\n{}".format(
                "\n\n".join(errors)
            )
        )


def _create_clients_interactively() -> None:
    print("Creating the Python Measurement Plug-In Client in interactive mode...")
    generated_modules: list[str] = []
    channel_pool = GrpcChannelPool()
    discovery_client = DiscoveryClient(grpc_channel_pool=channel_pool)
    directory_out_path = resolve_output_directory()

    while True:
        measurement_service_classes, measurement_display_names = (
            get_all_registered_measurement_info(discovery_client)
        )
        validate_measurement_service_classes(measurement_service_classes)

        print("\nList of registered measurements:")
        for index, display_name in enumerate(measurement_display_names, start=1):
            print(f"{index}. {display_name}")

        selection = click.prompt(
            "\nSelect a measurement to generate a client (x to exit)",
            type=str,
        )
        if selection.lower() == "x":
            break
        service_class = get_selected_measurement_service_class(
            int(selection), measurement_service_classes
        )

        try:
            base_service_class = extract_base_service_class(service_class)
            default_module_name = create_module_name(base_service_class, generated_modules)
            module_name = click.prompt(
                "Enter a name for the Python client module, or press Enter to use the default name.",
                type=str,
                default=default_module_name,
            )
            validate_identifier(module_name, "module")
            default_class_name = create_class_name(base_service_class)
            class_name = click.prompt(
                "Enter a name for the Python client class, or press Enter to use the default name.",
                type=str,
                default=default_class_name,
            )
            validate_identifier(class_name, "class")

            _create_client(
                channel_pool=channel_pool,
                discovery_client=discovery_client,
                measurement_service_class=service_class,
                module_name=module_name,
                class_name=class_name,
                directory_out=directory_out_path,
                generated_modules=generated_modules,
            )
        except Exception as e:
            click.echo(_CLIENT_CREATION_ERROR_MESSAGE.format(service_class, e))


def _create_clients(
    measurement_service_classes: list[str],
    module_name: str | None,
    class_name: str | None,
    directory_out: str | None,
) -> None:
    generated_modules: list[str] = []
    channel_pool = GrpcChannelPool()
    discovery_client = DiscoveryClient(grpc_channel_pool=channel_pool)
    directory_out_path = resolve_output_directory(directory_out)

    has_multiple_service_classes = len(measurement_service_classes) > 1
    for service_class in measurement_service_classes:
        base_service_class = extract_base_service_class(service_class)
        if has_multiple_service_classes or module_name is None:
            module_name = create_module_name(base_service_class, generated_modules)
        if has_multiple_service_classes or class_name is None:
            class_name = create_class_name(base_service_class)
        validate_identifier(module_name, "module")
        validate_identifier(class_name, "class")

        _create_client(
            channel_pool=channel_pool,
            discovery_client=discovery_client,
            measurement_service_class=service_class,
            module_name=module_name,
            class_name=class_name,
            directory_out=directory_out_path,
            generated_modules=generated_modules,
        )


@click.command()
@optgroup.group(
    "all-modes",
    cls=RequiredMutuallyExclusiveOptionGroup,
    help="The different modes to create Python measurement client.",
)
@optgroup.option(
    "-s",
    "--measurement-service-class",
    help="Creates Python Measurement Plug-In Client for the given measurement service classes.",
    multiple=True,
)
@optgroup.option(
    "-a",
    "--all",
    is_flag=True,
    help="Creates Python Measurement Plug-In Clients for all registered measurement services.",
)
@optgroup.option(
    "-i",
    "--interactive",
    is_flag=True,
    help="Creates Python Measurement Plug-In Clients interactively.",
)
@optgroup.group(
    "optional parameters",
    help="Recommended parameters when using measurement service class mode.",
)
@optgroup.option(
    "-m",
    "--module-name",
    help="Name for the Python Measurement Plug-In Client module.",
)
@optgroup.option(
    "-c",
    "--class-name",
    help="Name for the Python Measurement Plug-In Client Class in the generated module.",
)
@optgroup.option(
    "-o",
    "--directory-out",
    help="Output directory for Measurement Plug-In Client files. Default: '<current_directory>/<module_name>'",
)
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Enable verbose logging. Repeat to increase verbosity.",
)
def create_client(
    measurement_service_class: list[str],
    all: bool,
    interactive: bool,
    module_name: str | None,
    class_name: str | None,
    directory_out: str | None,
    verbose: int,
) -> None:
    """Generates a Python Measurement Plug-In Client module for the measurement service.

    You can use the generated module to interact with the corresponding measurement service.
    """
    if verbose > 1:
        level = logging.DEBUG
    elif verbose == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=level)

    if all:
        _create_all_clients(directory_out)
    elif interactive:
        _create_clients_interactively()
    else:
        _create_clients(
            measurement_service_classes=measurement_service_class,
            module_name=module_name,
            class_name=class_name,
            directory_out=directory_out,
        )
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/client/__main__.py sha256=455e68b33ada62972738a96d1751d90afd17c24e1f9ead6b0dc8ac1596ad8c85 bytes=155 -->
## FILE: packages/generator/ni_measurement_plugin_sdk_generator/client/__main__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/ni_measurement_plugin_sdk_generator/client/__main__.py`
- sha256: `455e68b33ada62972738a96d1751d90afd17c24e1f9ead6b0dc8ac1596ad8c85`
- bytes: 155

````python
"""Creates a measurement client through use of __init__.py."""

from ni_measurement_plugin_sdk_generator.client import create_client

create_client()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/client/_support.py sha256=2a992b79cffaee4bca771aacc66b19c8a6c3f38214cffc02886ffd45a7021d4f bytes=21547 -->
## FILE: packages/generator/ni_measurement_plugin_sdk_generator/client/_support.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/ni_measurement_plugin_sdk_generator/client/_support.py`
- sha256: `2a992b79cffaee4bca771aacc66b19c8a6c3f38214cffc02886ffd45a7021d4f`
- bytes: 21547

````python
"""Support functions for the Measurement Plug-In Client generator."""

from __future__ import annotations

import json
import keyword
import pathlib
import re
from collections.abc import Iterable
from enum import Enum
from typing import AbstractSet, TypeVar

import click
import grpc
from google.protobuf import descriptor_pool
from google.protobuf.descriptor_pb2 import FieldDescriptorProto
from google.protobuf.type_pb2 import Field
from ni.measurementlink.discovery.v1.client import DiscoveryClient
from ni.measurementlink.measurement.v2 import (
    measurement_service_pb2 as v2_measurement_service_pb2,
    measurement_service_pb2_grpc as v2_measurement_service_pb2_grpc,
)
from ni_grpc_extensions.channelpool import GrpcChannelPool
from ni_measurement_plugin_sdk_service._internal.grpc_servicer import (
    frame_metadata_dict,
)
from ni_measurement_plugin_sdk_service.measurement.client_support import (
    ParameterMetadata,
    create_file_descriptor,
    deserialize_parameters,
)

_V2_MEASUREMENT_SERVICE_INTERFACE = "ni.measurementlink.measurement.v2.MeasurementService"

_INVALID_CHARS = "`~!@#$%^&*()-+={}[]\\|:;',<>.?/ \n"

_XY_DATA_IMPORT = "from ni.protobuf.types.xydata_pb2 import DoubleXYData"
_DOUBLE2DARRAY_DATA_IMPORT = "from ni.protobuf.types.array_pb2 import Double2DArray"
_STRING2DARRAY_DATA_IMPORT = "from ni.protobuf.types.array_pb2 import String2DArray"
_PATH_IMPORT = "import pathlib"

_PROTO_DATATYPE_TO_PYTYPE_LOOKUP = {
    Field.TYPE_INT32: int,
    Field.TYPE_INT64: int,
    Field.TYPE_UINT32: int,
    Field.TYPE_UINT64: int,
    Field.TYPE_SINT32: int,
    Field.TYPE_SINT64: int,
    Field.TYPE_FIXED32: int,
    Field.TYPE_FIXED64: int,
    Field.TYPE_SFIXED32: int,
    Field.TYPE_SFIXED64: int,
    Field.TYPE_FLOAT: float,
    Field.TYPE_DOUBLE: float,
    Field.TYPE_BOOL: bool,
    Field.TYPE_STRING: str,
    Field.TYPE_ENUM: int,
    Field.TYPE_MESSAGE: str,
}

_T = TypeVar("_T")

# List of regex patterns to convert camel case to snake case
_CAMEL_TO_SNAKE_CASE_REGEXES = [
    re.compile("([^_\n])([A-Z][a-z]+)"),
    re.compile("([a-z])([A-Z])"),
    re.compile("([0-9])([^_0-9])"),
    re.compile("([^_0-9])([0-9])"),
]


def get_measurement_service_stub_and_version(
    discovery_client: DiscoveryClient,
    channel_pool: GrpcChannelPool,
    service_class: str,
) -> tuple[v2_measurement_service_pb2_grpc.MeasurementServiceStub, str]:
    """Returns the measurement service stub and version of the given service class."""
    try:
        service_location, service_info = discovery_client.resolve_service_with_information(
            _V2_MEASUREMENT_SERVICE_INTERFACE, service_class
        )
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.NOT_FOUND:
            raise click.ClickException(
                f"Could not find any registered measurement with the service class: '{service_class}'."
            )
        elif e.code() == grpc.StatusCode.UNIMPLEMENTED:
            raise click.ClickException(
                "The Measurement Plug-In Client generator requires InstrumentStudio Professional version 2024 Q4 or higher."
            )
        else:
            raise
    channel = channel_pool.get_channel(service_location.insecure_address)

    if not service_info.versions:
        raise click.ClickException(
            "The Measurement Plug-In Client generator requires InstrumentStudio Professional version 2024 Q4 or higher."
        )

    return (
        v2_measurement_service_pb2_grpc.MeasurementServiceStub(channel),
        service_info.versions[0],
    )


def get_all_registered_measurement_info(
    discovery_client: DiscoveryClient,
) -> tuple[list[str], list[str]]:
    """Returns the service classes and display names of all the registered measurement services."""
    registered_measurement_services = discovery_client.enumerate_services(
        _V2_MEASUREMENT_SERVICE_INTERFACE
    )
    measurement_service_classes = [
        measurement_service.service_class for measurement_service in registered_measurement_services
    ]
    measurement_display_names = [
        measurement_service.display_name for measurement_service in registered_measurement_services
    ]
    return measurement_service_classes, measurement_display_names


def get_configuration_and_output_metadata_by_index(
    metadata: v2_measurement_service_pb2.GetMetadataResponse,
    service_class: str,
    enum_values_by_type: dict[type[Enum], dict[str, int]] = {},
) -> tuple[dict[int, ParameterMetadata], dict[int, ParameterMetadata]]:
    """Returns the configuration and output metadata of the measurement."""
    configuration_parameter_list = []
    for configuration in metadata.measurement_signature.configuration_parameters:
        if configuration.message_type:
            raise click.ClickException(
                f"Measurement configurations do not support message data types ({configuration.message_type} is unsupported)."
            )

        annotations_dict = dict(configuration.annotations.items())
        if _is_enum_param(configuration.type):
            annotations_dict["ni/enum.values"] = _validate_and_transform_enum_annotations(
                configuration.annotations["ni/enum.values"]
            )

        # In Python 3.13 and earlier, the ConfigurationParameter message sorted the annotation
        # keys, but in Python 3.14, it started preserving order. Sort to keep tests passing.
        annotations_dict = dict(sorted(annotations_dict.items()))

        configuration_parameter_list.append(
            ParameterMetadata.initialize(
                display_name=configuration.name,
                type=configuration.type,
                repeated=configuration.repeated,
                default_value=None,
                annotations=annotations_dict,
                message_type=configuration.message_type,
                enum_type=(
                    _get_enum_type(
                        configuration.name, annotations_dict["ni/enum.values"], enum_values_by_type
                    )
                    if _is_enum_param(configuration.type)
                    else None
                ),
            )
        )

    output_parameter_list = []
    for output in metadata.measurement_signature.outputs:
        if output.message_type and output.message_type not in [
            "ni.protobuf.types.DoubleXYData",
            "ni.protobuf.types.Double2DArray",
            "ni.protobuf.types.String2DArray",
        ]:
            raise click.ClickException(
                f"Measurement outputs do not support {output.message_type}. DoubleXYData, Double2DArray and String2DArray message types are supported."
            )

        annotations_dict = dict(output.annotations.items())
        if _is_enum_param(output.type):
            annotations_dict["ni/enum.values"] = _validate_and_transform_enum_annotations(
                output.annotations["ni/enum.values"]
            )

        # In Python 3.13 and earlier, the ConfigurationParameter message sorted the annotation
        # keys, but in Python 3.14, it started preserving order. Sort to keep tests passing.
        annotations_dict = dict(sorted(annotations_dict.items()))

        output_parameter_list.append(
            ParameterMetadata.initialize(
                display_name=output.name,
                type=output.type,
                repeated=output.repeated,
                default_value=None,
                annotations=annotations_dict,
                message_type=output.message_type,
                enum_type=(
                    _get_enum_type(
                        output.name, annotations_dict["ni/enum.values"], enum_values_by_type
                    )
                    if _is_enum_param(output.type)
                    else None
                ),
            )
        )

    create_file_descriptor(
        input_metadata=configuration_parameter_list,
        output_metadata=output_parameter_list,
        service_name=service_class,
        pool=descriptor_pool.Default(),
    )
    configuration_metadata = frame_metadata_dict(configuration_parameter_list)
    output_metadata = frame_metadata_dict(output_parameter_list)

    # Disable path conversion to avoid normalizing path separators and eliminate the need to
    # convert Path objects to strings.
    default_values = deserialize_parameters(
        configuration_metadata,
        metadata.measurement_signature.configuration_defaults.value,
        f"{service_class}.Configurations",
        convert_paths=False,
    )

    for id, default_value in enumerate(default_values, start=1):
        if isinstance(default_value, Enum):
            default_value = default_value.value
        elif isinstance(default_value, list) and any(isinstance(e, Enum) for e in default_value):
            default_value = [e.value for e in default_value]
        configuration_metadata[id] = configuration_metadata[id]._replace(
            default_value=default_value
        )

    return configuration_metadata, output_metadata


def get_configuration_parameters_with_type_and_default_values(
    configuration_metadata: dict[int, ParameterMetadata],
    built_in_import_modules: list[str],
    enum_values_by_type: dict[type[Enum], dict[str, int]] = {},
) -> tuple[str, str]:
    """Returns configuration parameters of the measurement with type and default values."""
    configuration_parameters = []
    parameter_names = []

    for metadata in configuration_metadata.values():
        parameter_name = _get_python_identifier(metadata.display_name)
        parameter_names.append(parameter_name)

        default_value = metadata.default_value
        parameter_type = _get_configuration_python_type_as_str(metadata.type, metadata.repeated)
        if isinstance(default_value, str):
            default_value = repr(default_value)

        if metadata.annotations and metadata.annotations.get("ni/type_specialization") == "path":
            parameter_type = "pathlib.PurePath"
            built_in_import_modules.append(_PATH_IMPORT)
            if metadata.repeated:
                formatted_value = ", ".join(
                    f"pathlib.PurePath({repr(value)})" for value in default_value
                )
                default_value = f"[{formatted_value}]"
                parameter_type = f"typing.Iterable[{parameter_type}]"
            else:
                default_value = f"pathlib.PurePath({default_value})"

        if metadata.annotations and metadata.annotations.get("ni/type_specialization") == "enum":
            enum_type = _get_enum_type(
                metadata.display_name, metadata.annotations["ni/enum.values"], enum_values_by_type
            )
            parameter_type = enum_type.__name__
            if metadata.repeated:
                values = []
                for val in default_value:
                    enum_value = next((e.name for e in enum_type if e.value == val), None)
                    values.append(f"{parameter_type}.{enum_value}")
                concatenated_default_value = ", ".join(values)
                concatenated_default_value = f"[{concatenated_default_value}]"

                parameter_type = f"typing.Iterable[{parameter_type}]"
                default_value = concatenated_default_value
            else:
                enum_value = next((e.name for e in enum_type if e.value == default_value), None)
                default_value = f"{parameter_type}.{enum_value}"

        configuration_parameters.append(f"{parameter_name}: {parameter_type} = {default_value}")

    configuration_parameters_with_type_and_value = f", ".join(configuration_parameters)
    parameter_names_as_str = ", ".join(parameter_names)

    return (configuration_parameters_with_type_and_value, parameter_names_as_str)


def get_output_parameters_with_type(
    output_metadata: dict[int, ParameterMetadata],
    built_in_import_modules: list[str],
    custom_import_modules: list[str],
    enum_values_by_type: dict[type[Enum], dict[str, int]] = {},
) -> list[str]:
    """Returns the output parameters of the measurement with type."""
    output_parameters_with_type: list[str] = []
    for metadata in output_metadata.values():
        parameter_name = _get_python_identifier(metadata.display_name)
        parameter_type = _get_output_python_type_as_str(metadata.type, metadata.repeated)

        if metadata.annotations and metadata.annotations.get("ni/type_specialization") == "path":
            parameter_type = "pathlib.Path"
            built_in_import_modules.append(_PATH_IMPORT)

            if metadata.repeated:
                parameter_type = f"typing.Sequence[{parameter_type}]"

        if metadata.message_type and metadata.message_type == "ni.protobuf.types.DoubleXYData":
            parameter_type = "DoubleXYData"
            custom_import_modules.append(_XY_DATA_IMPORT)

            if metadata.repeated:
                parameter_type = f"typing.Sequence[{parameter_type}]"

        if metadata.message_type and metadata.message_type == "ni.protobuf.types.Double2DArray":
            parameter_type = "Double2DArray"
            custom_import_modules.append(_DOUBLE2DARRAY_DATA_IMPORT)

            if metadata.repeated:
                raise click.ClickException(
                    f"Repeated Double 2D Array are not supported for output parameter "
                    f"'{parameter_name}'. Please contact the measurement developer."
                )

        if metadata.message_type and metadata.message_type == "ni.protobuf.types.String2DArray":
            parameter_type = "String2DArray"
            custom_import_modules.append(_STRING2DARRAY_DATA_IMPORT)

            if metadata.repeated:
                raise click.ClickException(
                    f"Repeated String 2D Array are not supported for output parameter "
                    f"'{parameter_name}'. Please contact the measurement developer."
                )

        if metadata.annotations and metadata.annotations.get("ni/type_specialization") == "enum":
            enum_type_name = _get_enum_type(
                metadata.display_name, metadata.annotations["ni/enum.values"], enum_values_by_type
            ).__name__
            parameter_type = (
                f"typing.Sequence[{enum_type_name}]" if metadata.repeated else enum_type_name
            )

        output_parameters_with_type.append(f"{parameter_name}: {parameter_type}")

    return output_parameters_with_type


def to_ordered_set(values: Iterable[_T]) -> AbstractSet[_T]:
    """Converts an iterable to an ordered set."""
    return dict.fromkeys(values).keys()


def resolve_output_directory(directory_out: str | None = None) -> pathlib.Path:
    """Returns the validated directory output path."""
    if directory_out is None:
        directory_out_path = pathlib.Path.cwd()
    else:
        directory_out_path = pathlib.Path(directory_out)

    if not directory_out_path.exists():
        raise click.ClickException(f"The specified directory '{directory_out}' was not found.")

    return directory_out_path


def validate_identifier(name: str, name_type: str) -> None:
    """Validates whether the given string is a valid Python identifier."""
    if not _is_python_identifier(name):
        raise click.ClickException(
            f"The {name_type} name '{name}' is not a valid Python identifier."
        )


def extract_base_service_class(service_class: str) -> str:
    """Creates a base service class from the measurement service class."""
    base_service_class = service_class.split(".")[-1]
    base_service_class = _remove_suffix(base_service_class)

    if not base_service_class.isidentifier():
        raise click.ClickException(
            f"Client creation failed for '{service_class}'.\nEither provide a module name or update the measurement with a valid service class."
        )
    if not any(ch.isupper() for ch in base_service_class):
        print(
            f"Warning: The service class '{service_class}' does not adhere to the recommended format."
        )
    return base_service_class


def create_module_name(base_service_class: str, generated_modules: list[str]) -> str:
    """Creates a unique module name using the base service class."""
    base_module_name = _camel_to_snake_case(base_service_class) + "_client"
    module_name = base_module_name
    counter = 2

    while module_name in generated_modules:
        module_name = f"{base_module_name}{counter}"
        counter += 1

    return module_name


def create_class_name(base_service_class: str) -> str:
    """Creates a class name using base service class."""
    return base_service_class.replace("_", "") + "Client"


def get_selected_measurement_service_class(
    selection: int, measurement_service_classes: list[str]
) -> str:
    """Returns the selected measurement service class."""
    if not (1 <= selection <= len(measurement_service_classes)):
        raise click.ClickException(
            f"Input {selection} is not invalid. Please try again by selecting a valid measurement from the list."
        )
    return measurement_service_classes[selection - 1]


def validate_measurement_service_classes(measurement_service_classes: list[str]) -> None:
    """Validates whether the given measurement service classes list is empty."""
    if len(measurement_service_classes) == 0:
        raise click.ClickException("No registered measurements.")


def _get_python_identifier(input_string: str) -> str:
    valid_identifier = input_string.lower()
    if not valid_identifier.isidentifier():
        for invalid_char in _INVALID_CHARS:
            valid_identifier = valid_identifier.replace(invalid_char, "_")

    if valid_identifier[0].isdigit() or keyword.iskeyword(valid_identifier):
        valid_identifier = f"_{valid_identifier}"
    return valid_identifier


def _get_configuration_python_type_as_str(type: Field.Kind.ValueType, is_array: bool) -> str:
    python_type = _PROTO_DATATYPE_TO_PYTYPE_LOOKUP.get(type)

    if python_type is None:
        raise TypeError(f"Invalid data type: '{type}'.")

    if is_array:
        return f"typing.Iterable[{python_type.__name__}]"
    return python_type.__name__


def _get_output_python_type_as_str(type: Field.Kind.ValueType, is_array: bool) -> str:
    python_type = _PROTO_DATATYPE_TO_PYTYPE_LOOKUP.get(type)

    if python_type is None:
        raise TypeError(f"Invalid data type: '{type}'.")

    if is_array:
        return f"typing.Sequence[{python_type.__name__}]"
    return python_type.__name__


def _camel_to_snake_case(camel_case_string: str) -> str:
    partial = camel_case_string
    for regex in _CAMEL_TO_SNAKE_CASE_REGEXES:
        partial = regex.sub(r"\1_\2", partial)

    return partial.lower()


def _remove_suffix(string: str) -> str:
    suffixes = ["_Python", "_LabVIEW", "_NET"]
    for suffix in suffixes:
        if string.endswith(suffix):
            return string.removesuffix(suffix)
    return string


def _is_python_identifier(input_string: str | None) -> bool:
    if input_string is None:
        return False
    pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
    return re.fullmatch(pattern, input_string) is not None


def _is_enum_param(parameter_type: int) -> bool:
    return parameter_type == FieldDescriptorProto.TYPE_ENUM


def _get_enum_type(
    parameter_name: str,
    enum_annotations: str,
    enum_values_by_type: dict[type[Enum], dict[str, int]],
) -> type[Enum]:
    enum_values = dict(json.loads(enum_annotations))
    for existing_enum_type, existing_enum_values in enum_values_by_type.items():
        if existing_enum_values == enum_values:
            return existing_enum_type

    new_enum_type_name = _get_enum_class_name(parameter_name)
    # MyPy error: Enum() expects a string literal as the first argument.
    # Ignoring this error because MyPy cannot validate dynamic Enum creation statically.
    new_enum_type = Enum(new_enum_type_name, enum_values)  # type: ignore[misc]
    enum_values_by_type[new_enum_type] = enum_values
    return new_enum_type


def _get_enum_class_name(name: str) -> str:
    name = re.sub(r"[^\w\s]", "", name).replace("_", " ")
    split_string = name.split()
    if len(split_string) > 1:
        name = "".join(s.capitalize() for s in split_string)
    else:
        name = name[0].upper() + name[1:]
    return f"{name}Enum"


def _validate_and_transform_enum_annotations(enum_annotations: str) -> str:
    enum_values = dict(json.loads(enum_annotations))
    transformed_enum_annotations = {}
    for enum_value, value in enum_values.items():
        original_enum_value = enum_value

        enum_value = re.sub(r"\W+", "_", enum_value)
        if enum_value[0].isdigit():
            enum_value = f"k_{enum_value}"

        # Check for enum values that are only special characters.
        if not enum_value.strip("_"):
            raise click.ClickException(f"The enum value '{original_enum_value}' is invalid.")

        transformed_enum_annotations[enum_value] = value

    return json.dumps(transformed_enum_annotations)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/client/templates/measurement_plugin_client.py.mako sha256=2984800a45738f01e81cef2d18ee1804a98005d28e5fcea32ce8bee862ab2d1b bytes=12904 -->
## FILE: packages/generator/ni_measurement_plugin_sdk_generator/client/templates/measurement_plugin_client.py.mako

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/ni_measurement_plugin_sdk_generator/client/templates/measurement_plugin_client.py.mako`
- sha256: `2984800a45738f01e81cef2d18ee1804a98005d28e5fcea32ce8bee862ab2d1b`
- bytes: 12904

````mako
<%!
import re
from typing import Any
%>\
\
<%page args="class_name, display_name, version, configuration_metadata, output_metadata, service_class, configuration_parameters_with_type_and_default_values, measure_api_parameters, output_parameters_with_type, built_in_import_modules, custom_import_modules, enum_by_class_name, configuration_parameters_type_url, outputs_message_type"/>\
\
<%
    def _format_default_value(value: Any) -> Any:
        if isinstance(value, str):
            return repr(value)
        else:
            return value
%>\
\

"""Generated client API for the ${display_name | repr} measurement plug-in."""

from __future__ import annotations

import logging
import pathlib
import threading
import typing
% if output_metadata:
import warnings
% endif
% if len(enum_by_class_name):
from enum import Enum
% endif

import grpc
from google.protobuf import any_pb2, descriptor_pool
from google.protobuf.type_pb2 import Field
from ni.measurementlink.measurement.v2 import (
    measurement_service_pb2 as v2_measurement_service_pb2,
    measurement_service_pb2_grpc as v2_measurement_service_pb2_grpc,
)
% for module in custom_import_modules:
${module}
% endfor
from ni_grpc_extensions.channelpool import GrpcChannelPool
from ni.measurementlink.discovery.v1.client import DiscoveryClient
from ni.measurementlink.sessionmanagement.v1.client import PinMapContext
% if output_metadata:
from ni_measurement_plugin_sdk_service.measurement import WrongMessageTypeWarning
% endif
from ni_measurement_plugin_sdk_service.measurement.client_support import (
    ParameterMetadata,
    create_file_descriptor,
% if output_metadata:
    deserialize_parameters,
% endif
    serialize_parameters,
)
from ni.measurementlink.pinmap.v1.client import PinMapClient

_logger = logging.getLogger(__name__)

_V2_MEASUREMENT_SERVICE_INTERFACE = "ni.measurementlink.measurement.v2.MeasurementService"

% for enum_name, enum_value in enum_by_class_name.items():

class ${enum_name.__name__}(Enum):
    """${enum_name.__name__} used for enum-typed measurement configs and outputs."""

    % for key, val in enum_value.items():
    ${key} = ${val}
    % endfor
% endfor

<% output_type = "None" %>\
% if output_metadata:

class Outputs(typing.NamedTuple):
    """Outputs for the ${display_name | repr} measurement plug-in."""

    % for output_parameter in output_parameters_with_type:
    ${output_parameter}
    % endfor
<% output_type = "Outputs" %>\
% endif


class ${class_name}:
    """Client for the ${display_name | repr} measurement plug-in."""
     
    def __init__(
        self,
        *,
        discovery_client: DiscoveryClient | None = None,
        pin_map_client: PinMapClient | None = None,
        grpc_channel: grpc.Channel | None = None,
        grpc_channel_pool: GrpcChannelPool | None = None,
    ):
        """Initialize the Measurement Plug-In Client.

        Args:
            discovery_client: An optional discovery client.

            pin_map_client: An optional pin map client.

            grpc_channel: An optional gRPC channel targeting a measurement service.

            grpc_channel_pool: An optional gRPC channel pool.
        """
        self._initialization_lock = threading.RLock()
        self._service_class = ${service_class | repr}
        self._version = ${version | repr}
        self._grpc_channel_pool = grpc_channel_pool
        self._discovery_client = discovery_client
        self._pin_map_client = pin_map_client
        self._stub: v2_measurement_service_pb2_grpc.MeasurementServiceStub | None = None
        self._measure_response: None | (
            grpc._CallIterator[v2_measurement_service_pb2.MeasureResponse]
        ) = None
        self._configuration_metadata = {
            % for key, value in configuration_metadata.items():
            ${key}: ParameterMetadata(
                display_name=${value.display_name | repr},
                type=Field.Kind.ValueType(${value.type}),
                repeated=${value.repeated},
                default_value=${_format_default_value(value.default_value)},
                annotations=${value.annotations | n, repr},
                message_type=${value.message_type | repr},
                field_name=${value.field_name | repr},
                % if value.enum_type:
                enum_type=${value.enum_type.__name__}
                % else:
                enum_type=${value.enum_type}
                % endif
            ),  
            % endfor
        }
        self._output_metadata = {
            % for key, value in output_metadata.items():
            ${key}: ParameterMetadata(
                display_name=${value.display_name | repr},
                type=Field.Kind.ValueType(${value.type}),
                repeated=${value.repeated},
                default_value=${value.default_value},
                annotations=${value.annotations | n, repr},
                message_type=${value.message_type | repr},
                field_name=${value.field_name | repr},
                % if value.enum_type:
                enum_type=${value.enum_type.__name__}
                % else:
                enum_type=${value.enum_type}
                % endif
            ),  
            % endfor
        }
        if grpc_channel is not None:
            self._stub = v2_measurement_service_pb2_grpc.MeasurementServiceStub(grpc_channel)
        self._create_file_descriptor()
        self._pin_map_context: PinMapContext = PinMapContext(pin_map_id="", sites=[0])

    @property
    def pin_map_context(self) -> PinMapContext:
        """The pin map context for the measurement."""
        return self._pin_map_context

    @pin_map_context.setter
    def pin_map_context(self, val: PinMapContext) -> None:
        if not isinstance(val, PinMapContext):
            raise TypeError(
                f"Invalid type {type(val)}: The given value must be an instance of PinMapContext."
            )
        self._pin_map_context = val

    @property
    def sites(self) -> list[int] | None:
        """The sites where the measurement must be executed."""
        return self._pin_map_context.sites

    @sites.setter
    def sites(self, val: list[int]) -> None:
        if self._pin_map_context is None:
            raise AttributeError(
                "Cannot set sites because the pin map context is None. Please provide a pin map context or register a pin map before setting sites."
            )
        self._pin_map_context = self._pin_map_context._replace(sites=val)

    def _get_stub(self) -> v2_measurement_service_pb2_grpc.MeasurementServiceStub:
        if self._stub is None:
            with self._initialization_lock:
                if self._stub is None:
                    service_location = self._get_discovery_client().resolve_service(
                        provided_interface=_V2_MEASUREMENT_SERVICE_INTERFACE,
                        service_class=self._service_class,
                        version=self._version,
                    )
                    channel = self._get_grpc_channel_pool().get_channel(service_location.insecure_address)
                    self._stub = v2_measurement_service_pb2_grpc.MeasurementServiceStub(channel)
        return self._stub

    def _get_discovery_client(self) -> DiscoveryClient:
        if self._discovery_client is None:
            with self._initialization_lock:
                if self._discovery_client is None:
                    self._discovery_client = DiscoveryClient(
                        grpc_channel_pool=self._get_grpc_channel_pool(),
                    )
        return self._discovery_client

    def _get_grpc_channel_pool(self) -> GrpcChannelPool:
        if self._grpc_channel_pool is None:
            with self._initialization_lock:
                if self._grpc_channel_pool is None:
                    self._grpc_channel_pool = GrpcChannelPool()
        return self._grpc_channel_pool

    def _get_pin_map_client(self) -> PinMapClient:
        if self._pin_map_client is None:
            with self._initialization_lock:
                if self._pin_map_client is None:
                    self._pin_map_client = PinMapClient(
                        discovery_client=self._get_discovery_client(), 
                        grpc_channel_pool=self._get_grpc_channel_pool(),
                    )
        return self._pin_map_client

    def _create_file_descriptor(self) -> None:
        create_file_descriptor(
            input_metadata=list(self._configuration_metadata.values()),
            output_metadata=list(self._output_metadata.values()),
            service_name=self._service_class,
            pool=descriptor_pool.Default(),
        )

    def _create_measure_request(
        self, parameter_values: list[typing.Any]
    ) -> v2_measurement_service_pb2.MeasureRequest:
        serialized_configuration = any_pb2.Any(
            type_url=${configuration_parameters_type_url | repr},
            value=serialize_parameters(
                self._configuration_metadata,
                parameter_values,
                f"{self._service_class}.Configurations",
            )
        )
        return v2_measurement_service_pb2.MeasureRequest(
            configuration_parameters=serialized_configuration,
            pin_map_context=self._pin_map_context._to_grpc(),
        )

    % if output_metadata:
    def _deserialize_response(
        self, response: v2_measurement_service_pb2.MeasureResponse
    ) -> Outputs:
        self._validate_response(response)
        return Outputs._make(
            deserialize_parameters(
                self._output_metadata,
                response.outputs.value,
                f"{self._service_class}.Outputs",
            )
        )

    def _validate_response(self, response: v2_measurement_service_pb2.MeasureResponse) -> None:
        expected_type = "type.googleapis.com/" + ${outputs_message_type | repr}
        actual_type = response.outputs.type_url
        if actual_type != expected_type:
            warnings.warn(
                f"Wrong message type. Expected {expected_type!r} but got {actual_type!r}",
                WrongMessageTypeWarning,
            )
    % endif

    def measure(
        self,
        ${configuration_parameters_with_type_and_default_values}
    ) -> ${output_type} :
        """Perform a single measurement.

        Returns:
            Measurement outputs.
        """
        stream_measure_response = self.stream_measure(
            ${measure_api_parameters}
        )
        for response in stream_measure_response:
        % if output_metadata:
            result = response
        return result
        % else:
            pass
        % endif

    def stream_measure(
        self,
        ${configuration_parameters_with_type_and_default_values}
    ) -> typing.Generator[${output_type}] :
        """Perform a streaming measurement.

        Returns:
            Stream of measurement outputs.
        """
        parameter_values = [${measure_api_parameters}]
        with self._initialization_lock:
            if self._measure_response is not None:
                raise RuntimeError(
                    "A measurement is currently in progress. To make concurrent measurement requests, please create a new client instance."
                )
            request = self._create_measure_request(parameter_values)
            self._measure_response = self._get_stub().Measure(request)

        try:
            for response in self._measure_response:
                % if output_metadata:
                yield self._deserialize_response(response)
                % else:
                yield
                % endif
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.CANCELLED:
                _logger.debug("The measurement is canceled.")
            raise
        finally:
            with self._initialization_lock:
                self._measure_response = None

    def cancel(self) -> bool:
        """Cancels the active measurement call."""
        with self._initialization_lock:
            if self._measure_response:
                return self._measure_response.cancel()
            else:
                return False

    def register_pin_map(self, pin_map_path: pathlib.Path) -> None:
        """Registers the pin map with the pin map service.

        Args:
            pin_map_path: Absolute path of the pin map file.
        """
        pin_map_id = self._get_pin_map_client().update_pin_map(pin_map_path)
        self._pin_map_context = self._pin_map_context._replace(pin_map_id=pin_map_id)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/plugin/__init__.py sha256=d9c900ca1df3a29a90c0a42c6b9a1378d587f549521e354088c1d048971f34e7 bytes=6726 -->
## FILE: packages/generator/ni_measurement_plugin_sdk_generator/plugin/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/ni_measurement_plugin_sdk_generator/plugin/__init__.py`
- sha256: `d9c900ca1df3a29a90c0a42c6b9a1378d587f549521e354088c1d048971f34e7`
- bytes: 6726

````python
"""Utilizes command line args to create a measurement using template files."""

from __future__ import annotations

import logging
import pathlib
import re
from typing import Any, Optional, Tuple

import click
from mako import exceptions
from mako.template import Template

_logger = logging.getLogger(__name__)


def _render_template(template_name: str, **template_args: Any) -> bytes:
    file_path = str(pathlib.Path(__file__).parent / "templates" / template_name)

    template = Template(filename=file_path, input_encoding="utf-8", output_encoding="utf-8")
    try:
        return template.render(**template_args)
    except Exception as e:
        _logger.error(exceptions.text_error_template().render())
        raise click.ClickException(
            f'An error occurred while rendering template "{template_name}".'
        ) from e


def _create_file(
    template_name: str, file_name: str, directory_out: pathlib.Path, **template_args: Any
) -> None:
    output_file = directory_out / file_name

    output = _render_template(template_name, **template_args)

    with output_file.open("wb") as fout:
        fout.write(output)


def _check_version(ctx: click.Context, param: click.Parameter, version: str) -> str:
    pattern = r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$"
    if re.match(pattern, version):
        return version
    raise click.BadParameter(f"Invalid version '{version}'.")


def _check_ui_file(ctx: click.Context, param: click.Parameter, ui_file: str | None) -> str | None:
    if ui_file is not None:
        _ = _get_ui_type(ui_file)
    return ui_file


def _get_ui_type(ui_file: str) -> str:
    ext = pathlib.Path(ui_file).suffix
    if ext == ".measui":
        return "MeasurementUI"
    elif ext == ".vi":
        return "LabVIEW"
    else:
        raise click.BadParameter(
            f"Unsupported extension '{ext}'. Supported extensions: '.measui', '.vi'"
        )


def _resolve_ui_file(ui_file: str | None, display_name_for_filenames: str) -> str:
    if ui_file is None:
        return f"{display_name_for_filenames}.measui"
    else:
        return ui_file


def _resolve_service_class(service_class: str, display_name: str) -> str:
    if service_class is None:
        return f"{display_name}_Python"
    else:
        return service_class


@click.command()
@click.argument("display_name")
@click.option(
    "--measurement-version",
    callback=_check_version,
    help="Version number in the form 'x.y.z.q'. Default: '1.0.0.0'",
    default="1.0.0.0",
)
@click.option(
    "-u",
    "--ui-file",
    callback=_check_ui_file,
    help="Name of the UI File. Default: '<display_name>.measui'",
)
@click.option(
    "-s",
    "--service-class",
    help="Service Class that the measurement belongs to. Default: '<display_name>_Python'",
)
@click.option(
    "-D",
    "--description",
    default="",
    help="Short description of the measurement",
)
@click.option(
    "-d",
    "--description-url",
    default="",
    help="Description URL that links to a web page containing information about the measurement.",
)
@click.option(
    "-o",
    "--directory-out",
    help="Output directory for measurement files. Default: '<current_directory>/<display_name>'",
)
@click.option(
    "-c",
    "--collection",
    default="",
    help="\b\nThe collection that this measurement belongs to. Collection names are specified"
    "using a period-delimited namespace hierarchy and are case-insensitive."
    "\nExample: 'CurrentTests.Inrush'",
)
@click.option(
    "-t",
    "--tags",
    default=[],
    multiple=True,
    help="\b\nTags describing the measurement. This option may be repeated to specify multiple tags. Tags are case-insensitive."
    "\nExample: '-t test -t Internal'",
)
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Enable verbose logging. Repeat to increase verbosity.",
)
def create_measurement(
    display_name: str,
    measurement_version: str,
    ui_file: str | None,
    service_class: str,
    description_url: str,
    directory_out: str | None,
    description: str,
    collection: str,
    tags: tuple[str, ...],
    verbose: int,
) -> None:
    """Generate a Python measurement service from a template.

    You can use this to get started writing your own measurement plug-ins.

    DISPLAY_NAME: The measurement display name for client to display to user.
    The created .serviceconfig file will take this as its file name.
    """
    if verbose > 1:
        level = logging.DEBUG
    elif verbose == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=level)

    service_class = _resolve_service_class(service_class, display_name)
    display_name_for_filenames = re.sub(r"\s+", "", display_name)
    ui_file = _resolve_ui_file(ui_file, display_name_for_filenames)
    ui_file_type = _get_ui_type(ui_file)
    serviceconfig_file = f"{display_name_for_filenames}.serviceconfig"
    if directory_out is None:
        directory_out_path = pathlib.Path.cwd() / display_name_for_filenames
    else:
        directory_out_path = pathlib.Path(directory_out)

    directory_out_path.mkdir(exist_ok=True, parents=True)

    _create_file(
        "measurement.py.mako",
        "measurement.py",
        directory_out_path,
        display_name=display_name,
        ui_file=ui_file,
        ui_file_type=ui_file_type,
        service_class=service_class,
        description_url=description_url,
        serviceconfig_file=serviceconfig_file,
    )
    _create_file(
        "measurement.serviceconfig.mako",
        serviceconfig_file,
        directory_out_path,
        display_name=display_name,
        service_class=service_class,
        description_url=description_url,
        ui_file_type=ui_file_type,
        description=description,
        collection=collection,
        version=measurement_version,
        tags=list(tags),
    )
    if ui_file_type == "MeasurementUI":
        _create_file(
            "measurement.measui.mako",
            ui_file,
            directory_out_path,
            display_name=display_name,
            service_class=service_class,
        )
        _create_file(
            "measurement.measproj.mako",
            f"{display_name_for_filenames}.measproj",
            directory_out_path,
            ui_file=ui_file,
        )
    _create_file("start.bat.mako", "start.bat", directory_out_path)
    _create_file("_helpers.py.mako", "_helpers.py", directory_out_path)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/plugin/__main__.py sha256=2c36f240ddc573e1a9622273055f02fe42f15e2f4de38497f7b13e8dca76c720 bytes=158 -->
## FILE: packages/generator/ni_measurement_plugin_sdk_generator/plugin/__main__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/ni_measurement_plugin_sdk_generator/plugin/__main__.py`
- sha256: `2c36f240ddc573e1a9622273055f02fe42f15e2f4de38497f7b13e8dca76c720`
- bytes: 158

````python
"""Creates a measurement through use of __init__.py."""

from ni_measurement_plugin_sdk_generator.plugin import create_measurement

create_measurement()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/plugin/templates/_helpers.py.mako sha256=0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426 bytes=2920 -->
## FILE: packages/generator/ni_measurement_plugin_sdk_generator/plugin/templates/_helpers.py.mako

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/ni_measurement_plugin_sdk_generator/plugin/templates/_helpers.py.mako`
- sha256: `0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426`
- bytes: 2920

````mako
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

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/plugin/templates/measurement.measproj.mako sha256=73f9889f58f96717b8fa9cd8cb0d968545f6c2a6c08a0c0434ee078b2cf2f58c bytes=3340 -->
## FILE: packages/generator/ni_measurement_plugin_sdk_generator/plugin/templates/measurement.measproj.mako

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/ni_measurement_plugin_sdk_generator/plugin/templates/measurement.measproj.mako`
- sha256: `73f9889f58f96717b8fa9cd8cb0d968545f6c2a6c08a0c0434ee078b2cf2f58c`
- bytes: 3340

````mako
<%page args="ui_file"/>\
\
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="45C379C12E21531099FA05BA0133A871C1484C2D21AE60D19E992798D99A4020F84B7105887E5560BD63521128915683E687C64C7E275FA176574FC5AEB48A6E" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="24.8.0.49911" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="24.8.0.0" />
		<ParsableNamespace AssemblyFileVersion="9.14.0.49911" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.14.0.49911" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/EnvoyManagement" OldestCompatibleVersion="5.0.0.0" Version="5.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.14.0.49911" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemDiagram" OldestCompatibleVersion="8.0.0.49152" Version="8.0.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.14.0.49911" FeatureSetName="SystemDesigner" Name="http://www.ni.com/SystemDesigner/SystemModelCore" OldestCompatibleVersion="5.1.0.5" Version="5.2.0.49152" />
		<ApplicationVersionInfo Build="24.8.0.49911" Name="Measurement Plug-In UI Editor" Version="24.8.0.49911" />
	</SourceModelFeatureSet>
	<Project xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="dd27c2d5c720415eb15215bd545c9daa" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="89d719e01a084206ad23639db4b2f56f" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="595eaf9348434a23ae9cd79306a9f1cb" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<SourceFileReference Id="82b9ddbcdf2948238df082fc48b602b7" ModelDefinitionType="{http://www.ni.com/InstrumentFramework/ScreenDocument}Screen" Name="${ui_file}" StoragePath="${ui_file}" />
		</NameScopingEnvoy>
		<EmbeddedDefinitionReference Id="e346ab41c93c4c81b47bf6d0522b5deb" ModelDefinitionType="NationalInstruments.SystemDesigner.SystemDiagram.SystemDiagramDefinition" Name="SystemDiagram">
			<SystemDiagram Id="1a63510b9b8443258bb044b34b362c63" SystemDiagramVersion="75" xmlns="http://www.ni.com/SystemDesigner/SystemDiagram">
				<EnvoySuperimpositionContainer Id="403e8b77a2104c37bbedb0ae13460459" xmlns="http://www.ni.com/SystemDesigner/EnvoyManagement">
					<MappingManager Id="9e777b028f4b469b8549ceadb6957a0a" xmlns="http://www.ni.com/SystemDesigner/SystemModelCore">
						<Superimposition Id="89235b0c03b1429dbc3dacc6a88e6f61" Name="Root Superimposition" />
					</MappingManager>
				</EnvoySuperimpositionContainer>
				<SystemDiagramRootDiagram Id="5a0c562a2db249768b0a8ecb33fd3041" />
			</SystemDiagram>
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="99031b5a162c4ef0ba572fcd38a9e9ef" ModelDefinitionType="NullTarget" Name="NullTarget">
			<NullTarget />
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/plugin/templates/measurement.measui.mako sha256=995f29417b6d1a413b2925f8d11aeafe8378da78b1c62b7e26bc6e1a28c8e448 bytes=4307 -->
## FILE: packages/generator/ni_measurement_plugin_sdk_generator/plugin/templates/measurement.measui.mako

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/ni_measurement_plugin_sdk_generator/plugin/templates/measurement.measui.mako`
- sha256: `995f29417b6d1a413b2925f8d11aeafe8378da78b1c62b7e26bc6e1a28c8e448`
- bytes: 4307

````mako
<%page args="display_name, service_class"/>\
\
<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="C68495BACA801D17201A400444BA8E57096D877C220B005C9CC754DDBC96D7FF74F6512D245FAE462DBE92AF734E428F52FD46C680D4C1315BDAFF8C1B569796" Timestamp="1DB3B1ED4C5A7FD" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.14.0.49911" FeatureSetName="Configuration Based Software Core" Name="http://www.ni.com/ConfigurationBasedSoftware.Core" OldestCompatibleVersion="6.3.0.49152" Version="9.8.1.49152" />
		<ParsableNamespace AssemblyFileVersion="9.14.0.49911" FeatureSetName="LabVIEW Controls" Name="http://www.ni.com/Controls.LabVIEW.Design" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="24.8.0.49911" FeatureSetName="InstrumentStudio Measurement UI" Name="http://www.ni.com/InstrumentFramework/ScreenDocument" OldestCompatibleVersion="22.1.0.1" Version="24.8.0.0" />
		<ParsableNamespace AssemblyFileVersion="9.14.0.49911" FeatureSetName="Editor" Name="http://www.ni.com/PanelCommon" OldestCompatibleVersion="6.1.0.0" Version="6.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.14.0.49911" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ApplicationVersionInfo Build="24.8.0.49911" Name="Measurement Plug-In UI Editor" Version="24.8.0.49911" />
	</SourceModelFeatureSet>
	<Screen DisplayName="${display_name}" Id="3656de7c9d6a42cfb27ea41494f0ed46" ServiceClass="${service_class}" xmlns="http://www.ni.com/InstrumentFramework/ScreenDocument">
		<ScreenSurface BackgroundColor="[SMSolidColorBrush]#ffffffff" Height="[float]400" Id="5c1b8cc5eaf94b12b2be341f38937113" Left="[float]0" PanelSizeMode="Fixed" Top="[float]0" Width="[float]800" xmlns="http://www.ni.com/ConfigurationBasedSoftware.Core">
			<ChannelArrayViewer AdaptsToType="[bool]True" ArrayElement="[UIModel]6f8ab70f7a984a76ab50c8963cdebdfc" BaseName="[string]Numeric Array Input" Channel="[string]{5541d3fb-67cf-41cb-af53-b51b5b84fe2c}/Configuration/Array in" Columns="[int]1" Dimensions="[int]1" Height="[float]120" Id="4c034db32a2a40ce8ce645cda760a0bc" IndexVisibility="[Visibility]Collapsed" IsFixedSize="[bool]False" Label="[UIModel]1eff9af8bfcd427b919b514abb7494d9" Left="[float]34" Orientation="[SMOrientation]Vertical" Rows="[int]4" TabIndex="[int]0" Top="[float]50" VerticalScrollBarVisibility="[ScrollBarVisibility]Visible" Width="[float]104">
				<p.DefaultElementValue>0x0</p.DefaultElementValue>
				<ChannelArrayNumericText BaseName="[string]Numeric" Height="[float]24" Id="6f8ab70f7a984a76ab50c8963cdebdfc" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]72" />
			</ChannelArrayViewer>
			<Label Height="[float]16" Id="1eff9af8bfcd427b919b514abb7494d9" LabelOwner="[UIModel]4c034db32a2a40ce8ce645cda760a0bc" Left="[float]34" Text="[string]Array in" Top="[float]30" Width="[float]41" xmlns="http://www.ni.com/PanelCommon" />
			<ChannelArrayViewer AdaptsToType="[bool]True" ArrayElement="[UIModel]2601f80845974011b1488c655006560d" BaseName="[string]Numeric Array Output" Channel="[string]{5541d3fb-67cf-41cb-af53-b51b5b84fe2c}/Output/Array out" Columns="[int]1" Dimensions="[int]1" Height="[float]120" Id="48aa4906df6b47cf9e0404db2300ea9f" IndexVisibility="[Visibility]Collapsed" IsFixedSize="[bool]False" Label="[UIModel]107983d1f11646ee84e5159106f36b81" Left="[float]202" Orientation="[SMOrientation]Vertical" Rows="[int]4" TabIndex="[int]1" Top="[float]50" VerticalScrollBarVisibility="[ScrollBarVisibility]Visible" Width="[float]104">
				<p.DefaultElementValue>0x0</p.DefaultElementValue>
				<ChannelArrayNumericText BaseName="[string]Numeric" Height="[float]24" Id="2601f80845974011b1488c655006560d" IsReadOnly="[bool]True" UnitAnnotation="[string]" ValueFormatter="[string]LV:G5" ValueType="[Type]Double" Width="[float]72" />
			</ChannelArrayViewer>
			<Label Height="[float]16" Id="107983d1f11646ee84e5159106f36b81" LabelOwner="[UIModel]48aa4906df6b47cf9e0404db2300ea9f" Left="[float]202" Text="[string]Array out" Top="[float]30" Width="[float]49" xmlns="http://www.ni.com/PanelCommon" />
		</ScreenSurface>
	</Screen>
</SourceFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/plugin/templates/measurement.py.mako sha256=bbf6df3926c6b1643588c69c1e34f11a7e3bcbef3c3bba31641b8ea4c054d242 bytes=1590 -->
## FILE: packages/generator/ni_measurement_plugin_sdk_generator/plugin/templates/measurement.py.mako

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/ni_measurement_plugin_sdk_generator/plugin/templates/measurement.py.mako`
- sha256: `bbf6df3926c6b1643588c69c1e34f11a7e3bcbef3c3bba31641b8ea4c054d242`
- bytes: 1590

````mako
<%page args="display_name, ui_file, ui_file_type, service_class, description_url, serviceconfig_file"/>\
\
"""A default measurement with an array in and out."""

import logging
import pathlib
import sys

import click
import ni_measurement_plugin_sdk_service as nims

script_or_exe = sys.executable if getattr(sys, "frozen", False) else __file__
service_directory = pathlib.Path(script_or_exe).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "${serviceconfig_file}",
    ui_file_paths=[service_directory / "${ui_file}"],
)


@measurement_service.register_measurement
@measurement_service.configuration("Array in", nims.DataType.DoubleArray1D, [0.0])
@measurement_service.output("Array out", nims.DataType.DoubleArray1D)
def measure(array_input):
    """TODO: replace the following line with your own measurement logic."""
    array_output = array_input
    return (array_output,)


@click.command
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Enable verbose logging. Repeat to increase verbosity.",
)
def main(verbose: int) -> None:
    """Host the ${display_name} service."""
    if verbose > 1:
        level = logging.DEBUG
    elif verbose == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=level)

    with measurement_service.host_service():
        input("Press enter to close the measurement service.\n")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/plugin/templates/measurement.serviceconfig.mako sha256=1a84da29b777efd1bee78a9737a3a74b1f55836cffb0b5a96e1190f0961d3c4d bytes=883 -->
## FILE: packages/generator/ni_measurement_plugin_sdk_generator/plugin/templates/measurement.serviceconfig.mako

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/ni_measurement_plugin_sdk_generator/plugin/templates/measurement.serviceconfig.mako`
- sha256: `1a84da29b777efd1bee78a9737a3a74b1f55836cffb0b5a96e1190f0961d3c4d`
- bytes: 883

````mako
<%page args="display_name, service_class, description_url, description, collection, version, tags"/>\
<%
    import json

    service_config = {
      "services": [
          {
              "displayName": display_name,
              "serviceClass": service_class,
              "descriptionUrl": description_url,
              "providedInterfaces": [
                  "ni.measurementlink.measurement.v1.MeasurementService",
                  "ni.measurementlink.measurement.v2.MeasurementService",
              ],
              "path": "start.bat",
              "version": version,
              "annotations": {
                  "ni/service.description": description,
                  "ni/service.collection": collection,
                  "ni/service.tags": tags
              },
          }
       ]
    }
%>\
${json.dumps(service_config, indent=2)}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/plugin/templates/start.bat.mako sha256=bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851 bytes=253 -->
## FILE: packages/generator/ni_measurement_plugin_sdk_generator/plugin/templates/start.bat.mako

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/ni_measurement_plugin_sdk_generator/plugin/templates/start.bat.mako`
- sha256: `bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851`
- bytes: 253

````mako
@echo off
REM The discovery service uses this script to start the measurement service.
REM You can customize this script for your Python setup. The -v option logs
REM messages with level INFO and above.

.venv\Scripts\python.exe measurement.py -v
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/py.typed sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: packages/generator/ni_measurement_plugin_sdk_generator/py.typed

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/ni_measurement_plugin_sdk_generator/py.typed`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````text

````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/poetry.lock sha256=78abfabec1e4fc85ad24b25696e61c82cbad22e3091b444b0b747d2c0a4dea90 bytes=197643 -->
## FILE: packages/generator/poetry.lock

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/poetry.lock`
- sha256: `78abfabec1e4fc85ad24b25696e61c82cbad22e3091b444b0b747d2c0a4dea90`
- bytes: 197643

````text
# This file is automatically @generated by Poetry 2.4.1 and should not be changed by hand.

[[package]]
name = "bandit"
version = "1.9.4"
description = "Security oriented static analyser for python code."
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "bandit-1.9.4-py3-none-any.whl", hash = "sha256:f89ffa663767f5a0585ea075f01020207e966a9c0f2b9ef56a57c7963a3f6f8e"},
    {file = "bandit-1.9.4.tar.gz", hash = "sha256:b589e5de2afe70bd4d53fa0c1da6199f4085af666fde00e8a034f152a52cd628"},
]

[package.dependencies]
colorama = {version = ">=0.3.9", markers = "platform_system == \"Windows\""}
PyYAML = ">=5.3.1"
rich = "*"
stevedore = ">=1.20.0"
tomli = {version = ">=1.1.0", optional = true, markers = "python_version < \"3.11\" and extra == \"toml\""}

[package.extras]
baseline = ["GitPython (>=3.1.30)"]
sarif = ["jschema-to-python (>=1.2.3)", "sarif-om (>=1.0.4)"]
test = ["beautifulsoup4 (>=4.8.0)", "coverage (>=4.5.4)", "fixtures (>=3.0.0)", "flake8 (>=4.0.0)", "pylint (==1.9.4)", "stestr (>=2.5.0)", "testscenarios (>=0.5.0)", "testtools (>=2.3.0)"]
toml = ["tomli (>=1.1.0) ; python_version < \"3.11\""]
yaml = ["PyYAML"]

[[package]]
name = "better-diff"
version = "0.1.4"
description = "A simple library for printing better diffs based on the stdlib unified_diff format."
optional = false
python-versions = "<4.0,>=3.8"
groups = ["dev"]
files = [
    {file = "better_diff-0.1.4-py3-none-any.whl", hash = "sha256:06e63358b2047ae2695abd96316f47c6d3c38b9e641f53012279878d66d8792e"},
    {file = "better_diff-0.1.4.tar.gz", hash = "sha256:920ca76bdbcd2f0c361fa5d9a2d4727624a3545d6cb467b1b6616cad8a634de7"},
]

[[package]]
name = "black"
version = "25.12.0"
description = "The uncompromising code formatter."
optional = false
python-versions = ">=3.10"
groups = ["main", "dev"]
files = [
    {file = "black-25.12.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:f85ba1ad15d446756b4ab5f3044731bf68b777f8f9ac9cdabd2425b97cd9c4e8"},
    {file = "black-25.12.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:546eecfe9a3a6b46f9d69d8a642585a6eaf348bcbbc4d87a19635570e02d9f4a"},
    {file = "black-25.12.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:17dcc893da8d73d8f74a596f64b7c98ef5239c2cd2b053c0f25912c4494bf9ea"},
    {file = "black-25.12.0-cp310-cp310-win_amd64.whl", hash = "sha256:09524b0e6af8ba7a3ffabdfc7a9922fb9adef60fed008c7cd2fc01f3048e6e6f"},
    {file = "black-25.12.0-cp310-cp310-win_arm64.whl", hash = "sha256:b162653ed89eb942758efeb29d5e333ca5bb90e5130216f8369857db5955a7da"},
    {file = "black-25.12.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:d0cfa263e85caea2cff57d8f917f9f51adae8e20b610e2b23de35b5b11ce691a"},
    {file = "black-25.12.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:1a2f578ae20c19c50a382286ba78bfbeafdf788579b053d8e4980afb079ab9be"},
    {file = "black-25.12.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d3e1b65634b0e471d07ff86ec338819e2ef860689859ef4501ab7ac290431f9b"},
    {file = "black-25.12.0-cp311-cp311-win_amd64.whl", hash = "sha256:a3fa71e3b8dd9f7c6ac4d818345237dfb4175ed3bf37cd5a581dbc4c034f1ec5"},
    {file = "black-25.12.0-cp311-cp311-win_arm64.whl", hash = "sha256:51e267458f7e650afed8445dc7edb3187143003d52a1b710c7321aef22aa9655"},
    {file = "black-25.12.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:31f96b7c98c1ddaeb07dc0f56c652e25bdedaac76d5b68a059d998b57c55594a"},
    {file = "black-25.12.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:05dd459a19e218078a1f98178c13f861fe6a9a5f88fc969ca4d9b49eb1809783"},
    {file = "black-25.12.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c1f68c5eff61f226934be6b5b80296cf6939e5d2f0c2f7d543ea08b204bfaf59"},
    {file = "black-25.12.0-cp312-cp312-win_amd64.whl", hash = "sha256:274f940c147ddab4442d316b27f9e332ca586d39c85ecf59ebdea82cc9ee8892"},
    {file = "black-25.12.0-cp312-cp312-win_arm64.whl", hash = "sha256:169506ba91ef21e2e0591563deda7f00030cb466e747c4b09cb0a9dae5db2f43"},
    {file = "black-25.12.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:a05ddeb656534c3e27a05a29196c962877c83fa5503db89e68857d1161ad08a5"},
    {file = "black-25.12.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:9ec77439ef3e34896995503865a85732c94396edcc739f302c5673a2315e1e7f"},
    {file = "black-25.12.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0e509c858adf63aa61d908061b52e580c40eae0dfa72415fa47ac01b12e29baf"},
    {file = "black-25.12.0-cp313-cp313-win_amd64.whl", hash = "sha256:252678f07f5bac4ff0d0e9b261fbb029fa530cfa206d0a636a34ab445ef8ca9d"},
    {file = "black-25.12.0-cp313-cp313-win_arm64.whl", hash = "sha256:bc5b1c09fe3c931ddd20ee548511c64ebf964ada7e6f0763d443947fd1c603ce"},
    {file = "black-25.12.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:0a0953b134f9335c2434864a643c842c44fba562155c738a2a37a4d61f00cad5"},
    {file = "black-25.12.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:2355bbb6c3b76062870942d8cc450d4f8ac71f9c93c40122762c8784df49543f"},
    {file = "black-25.12.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9678bd991cc793e81d19aeeae57966ee02909877cb65838ccffef24c3ebac08f"},
    {file = "black-25.12.0-cp314-cp314-win_amd64.whl", hash = "sha256:97596189949a8aad13ad12fcbb4ae89330039b96ad6742e6f6b45e75ad5cfd83"},
    {file = "black-25.12.0-cp314-cp314-win_arm64.whl", hash = "sha256:778285d9ea197f34704e3791ea9404cd6d07595745907dd2ce3da7a13627b29b"},
    {file = "black-25.12.0-py3-none-any.whl", hash = "sha256:48ceb36c16dbc84062740049eef990bb2ce07598272e673c17d1a7720c71c828"},
    {file = "black-25.12.0.tar.gz", hash = "sha256:8d3dd9cea14bff7ddc0eb243c811cdb1a011ebb4800a5f0335a01a68654796a7"},
]

[package.dependencies]
click = ">=8.0.0"
mypy-extensions = ">=0.4.3"
packaging = ">=22.0"
pathspec = ">=0.9.0"
platformdirs = ">=2"
pytokens = ">=0.3.0"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}
typing-extensions = {version = ">=4.0.1", markers = "python_version < \"3.11\""}

[package.extras]
colorama = ["colorama (>=0.4.3)"]
d = ["aiohttp (>=3.10)"]
jupyter = ["ipython (>=7.8.0)", "tokenize-rt (>=3.2.0)"]
uvloop = ["uvloop (>=0.15.2)"]

[[package]]
name = "cachetools"
version = "7.0.6"
description = "Extensible memoizing collections and decorators"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "cachetools-7.0.6-py3-none-any.whl", hash = "sha256:4e94956cfdd3086f12042cdd29318f5ced3893014f7d0d059bf3ead3f85b7f8b"},
    {file = "cachetools-7.0.6.tar.gz", hash = "sha256:e5d524d36d65703a87243a26ff08ad84f73352adbeafb1cde81e207b456aaf24"},
]

[[package]]
name = "click"
version = "8.4.2"
description = "Composable command line interface toolkit"
optional = false
python-versions = ">=3.10"
groups = ["main", "dev"]
files = [
    {file = "click-8.4.2-py3-none-any.whl", hash = "sha256:e6f9f66136c816745b9d65817da91d61d957fb16e02e4dcd0552553c5a197b76"},
    {file = "click-8.4.2.tar.gz", hash = "sha256:9a6cea6e60b17ebe0a44c5cc636d94f09bd66142c1cd7d8b4cd731c4917a15f6"},
]

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}

[[package]]
name = "click-option-group"
version = "0.5.9"
description = "Option groups missing in Click"
optional = false
python-versions = ">=3.7"
groups = ["main"]
files = [
    {file = "click_option_group-0.5.9-py3-none-any.whl", hash = "sha256:ad2599248bd373e2e19bec5407967c3eec1d0d4fc4a5e77b08a0481e75991080"},
    {file = "click_option_group-0.5.9.tar.gz", hash = "sha256:f94ed2bc4cf69052e0f29592bd1e771a1789bd7bfc482dd0bc482134aff95823"},
]

[package.dependencies]
click = ">=7.0"

[package.extras]
dev = ["pre-commit", "pytest"]
docs = ["m2r2", "pallets-sphinx-themes", "sphinx"]
test = ["pytest"]
test-cov = ["pytest", "pytest-cov"]

[[package]]
name = "colorama"
version = "0.4.6"
description = "Cross-platform colored terminal text."
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"
groups = ["main", "dev"]
files = [
    {file = "colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"},
    {file = "colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"},
]
markers = {main = "platform_system == \"Windows\""}

[[package]]
name = "coverage"
version = "7.13.2"
description = "Code coverage measurement for Python"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "coverage-7.13.2-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:f4af3b01763909f477ea17c962e2cca8f39b350a4e46e3a30838b2c12e31b81b"},
    {file = "coverage-7.13.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:36393bd2841fa0b59498f75466ee9bdec4f770d3254f031f23e8fd8e140ffdd2"},
    {file = "coverage-7.13.2-cp310-cp310-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:9cc7573518b7e2186bd229b1a0fe24a807273798832c27032c4510f47ffdb896"},
    {file = "coverage-7.13.2-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:ca9566769b69a5e216a4e176d54b9df88f29d750c5b78dbb899e379b4e14b30c"},
    {file = "coverage-7.13.2-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:9c9bdea644e94fd66d75a6f7e9a97bb822371e1fe7eadae2cacd50fcbc28e4dc"},
    {file = "coverage-7.13.2-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:5bd447332ec4f45838c1ad42268ce21ca87c40deb86eabd59888859b66be22a5"},
    {file = "coverage-7.13.2-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:7c79ad5c28a16a1277e1187cf83ea8dafdcc689a784228a7d390f19776db7c31"},
    {file = "coverage-7.13.2-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:76e06ccacd1fb6ada5d076ed98a8c6f66e2e6acd3df02819e2ee29fd637b76ad"},
    {file = "coverage-7.13.2-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:49d49e9a5e9f4dc3d3dac95278a020afa6d6bdd41f63608a76fa05a719d5b66f"},
    {file = "coverage-7.13.2-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:ed2bce0e7bfa53f7b0b01c722da289ef6ad4c18ebd52b1f93704c21f116360c8"},
    {file = "coverage-7.13.2-cp310-cp310-win32.whl", hash = "sha256:1574983178b35b9af4db4a9f7328a18a14a0a0ce76ffaa1c1bacb4cc82089a7c"},
    {file = "coverage-7.13.2-cp310-cp310-win_amd64.whl", hash = "sha256:a360a8baeb038928ceb996f5623a4cd508728f8f13e08d4e96ce161702f3dd99"},
    {file = "coverage-7.13.2-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:060ebf6f2c51aff5ba38e1f43a2095e087389b1c69d559fde6049a4b0001320e"},
    {file = "coverage-7.13.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:c1ea8ca9db5e7469cd364552985e15911548ea5b69c48a17291f0cac70484b2e"},
    {file = "coverage-7.13.2-cp311-cp311-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:b780090d15fd58f07cf2011943e25a5f0c1c894384b13a216b6c86c8a8a7c508"},
    {file = "coverage-7.13.2-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:88a800258d83acb803c38175b4495d293656d5fac48659c953c18e5f539a274b"},
    {file = "coverage-7.13.2-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6326e18e9a553e674d948536a04a80d850a5eeefe2aae2e6d7cf05d54046c01b"},
    {file = "coverage-7.13.2-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:59562de3f797979e1ff07c587e2ac36ba60ca59d16c211eceaa579c266c5022f"},
    {file = "coverage-7.13.2-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:27ba1ed6f66b0e2d61bfa78874dffd4f8c3a12f8e2b5410e515ab345ba7bc9c3"},
    {file = "coverage-7.13.2-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:8be48da4d47cc68754ce643ea50b3234557cbefe47c2f120495e7bd0a2756f2b"},
    {file = "coverage-7.13.2-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:2a47a4223d3361b91176aedd9d4e05844ca67d7188456227b6bf5e436630c9a1"},
    {file = "coverage-7.13.2-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:c6f141b468740197d6bd38f2b26ade124363228cc3f9858bd9924ab059e00059"},
    {file = "coverage-7.13.2-cp311-cp311-win32.whl", hash = "sha256:89567798404af067604246e01a49ef907d112edf2b75ef814b1364d5ce267031"},
    {file = "coverage-7.13.2-cp311-cp311-win_amd64.whl", hash = "sha256:21dd57941804ae2ac7e921771a5e21bbf9aabec317a041d164853ad0a96ce31e"},
    {file = "coverage-7.13.2-cp311-cp311-win_arm64.whl", hash = "sha256:10758e0586c134a0bafa28f2d37dd2cdb5e4a90de25c0fc0c77dabbad46eca28"},
    {file = "coverage-7.13.2-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:f106b2af193f965d0d3234f3f83fc35278c7fb935dfbde56ae2da3dd2c03b84d"},
    {file = "coverage-7.13.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:78f45d21dc4d5d6bd29323f0320089ef7eae16e4bef712dff79d184fa7330af3"},
    {file = "coverage-7.13.2-cp312-cp312-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:fae91dfecd816444c74531a9c3d6ded17a504767e97aa674d44f638107265b99"},
    {file = "coverage-7.13.2-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:264657171406c114787b441484de620e03d8f7202f113d62fcd3d9688baa3e6f"},
    {file = "coverage-7.13.2-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ae47d8dcd3ded0155afbb59c62bd8ab07ea0fd4902e1c40567439e6db9dcaf2f"},
    {file = "coverage-7.13.2-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:8a0b33e9fd838220b007ce8f299114d406c1e8edb21336af4c97a26ecfd185aa"},
    {file = "coverage-7.13.2-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:b3becbea7f3ce9a2d4d430f223ec15888e4deb31395840a79e916368d6004cce"},
    {file = "coverage-7.13.2-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:f819c727a6e6eeb8711e4ce63d78c620f69630a2e9d53bc95ca5379f57b6ba94"},
    {file = "coverage-7.13.2-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:4f7b71757a3ab19f7ba286e04c181004c1d61be921795ee8ba6970fd0ec91da5"},
    {file = "coverage-7.13.2-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:b7fc50d2afd2e6b4f6f2f403b70103d280a8e0cb35320cbbe6debcda02a1030b"},
    {file = "coverage-7.13.2-cp312-cp312-win32.whl", hash = "sha256:292250282cf9bcf206b543d7608bda17ca6fc151f4cbae949fc7e115112fbd41"},
    {file = "coverage-7.13.2-cp312-cp312-win_amd64.whl", hash = "sha256:eeea10169fac01549a7921d27a3e517194ae254b542102267bef7a93ed38c40e"},
    {file = "coverage-7.13.2-cp312-cp312-win_arm64.whl", hash = "sha256:2a5b567f0b635b592c917f96b9a9cb3dbd4c320d03f4bf94e9084e494f2e8894"},
    {file = "coverage-7.13.2-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:ed75de7d1217cf3b99365d110975f83af0528c849ef5180a12fd91b5064df9d6"},
    {file = "coverage-7.13.2-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:97e596de8fa9bada4d88fde64a3f4d37f1b6131e4faa32bad7808abc79887ddc"},
    {file = "coverage-7.13.2-cp313-cp313-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:68c86173562ed4413345410c9480a8d64864ac5e54a5cda236748031e094229f"},
    {file = "coverage-7.13.2-cp313-cp313-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:7be4d613638d678b2b3773b8f687537b284d7074695a43fe2fbbfc0e31ceaed1"},
    {file = "coverage-7.13.2-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d7f63ce526a96acd0e16c4af8b50b64334239550402fb1607ce6a584a6d62ce9"},
    {file = "coverage-7.13.2-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:406821f37f864f968e29ac14c3fccae0fec9fdeba48327f0341decf4daf92d7c"},
    {file = "coverage-7.13.2-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:ee68e5a4e3e5443623406b905db447dceddffee0dceb39f4e0cd9ec2a35004b5"},
    {file = "coverage-7.13.2-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:2ee0e58cca0c17dd9c6c1cdde02bb705c7b3fbfa5f3b0b5afeda20d4ebff8ef4"},
    {file = "coverage-7.13.2-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:6e5bbb5018bf76a56aabdb64246b5288d5ae1b7d0dd4d0534fe86df2c2992d1c"},
    {file = "coverage-7.13.2-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:a55516c68ef3e08e134e818d5e308ffa6b1337cc8b092b69b24287bf07d38e31"},
    {file = "coverage-7.13.2-cp313-cp313-win32.whl", hash = "sha256:5b20211c47a8abf4abc3319d8ce2464864fa9f30c5fcaf958a3eed92f4f1fef8"},
    {file = "coverage-7.13.2-cp313-cp313-win_amd64.whl", hash = "sha256:14f500232e521201cf031549fb1ebdfc0a40f401cf519157f76c397e586c3beb"},
    {file = "coverage-7.13.2-cp313-cp313-win_arm64.whl", hash = "sha256:9779310cb5a9778a60c899f075a8514c89fa6d10131445c2207fc893e0b14557"},
    {file = "coverage-7.13.2-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:e64fa5a1e41ce5df6b547cbc3d3699381c9e2c2c369c67837e716ed0f549d48e"},
    {file = "coverage-7.13.2-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:b01899e82a04085b6561eb233fd688474f57455e8ad35cd82286463ba06332b7"},
    {file = "coverage-7.13.2-cp313-cp313t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:838943bea48be0e2768b0cf7819544cdedc1bbb2f28427eabb6eb8c9eb2285d3"},
    {file = "coverage-7.13.2-cp313-cp313t-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:93d1d25ec2b27e90bcfef7012992d1f5121b51161b8bffcda756a816cf13c2c3"},
    {file = "coverage-7.13.2-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:93b57142f9621b0d12349c43fc7741fe578e4bc914c1e5a54142856cfc0bf421"},
    {file = "coverage-7.13.2-cp313-cp313t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:f06799ae1bdfff7ccb8665d75f8291c69110ba9585253de254688aa8a1ccc6c5"},
    {file = "coverage-7.13.2-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:7f9405ab4f81d490811b1d91c7a20361135a2df4c170e7f0b747a794da5b7f23"},
    {file = "coverage-7.13.2-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:f9ab1d5b86f8fbc97a5b3cd6280a3fd85fef3b028689d8a2c00918f0d82c728c"},
    {file = "coverage-7.13.2-cp313-cp313t-musllinux_1_2_riscv64.whl", hash = "sha256:f674f59712d67e841525b99e5e2b595250e39b529c3bda14764e4f625a3fa01f"},
    {file = "coverage-7.13.2-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:c6cadac7b8ace1ba9144feb1ae3cb787a6065ba6d23ffc59a934b16406c26573"},
    {file = "coverage-7.13.2-cp313-cp313t-win32.whl", hash = "sha256:14ae4146465f8e6e6253eba0cccd57423e598a4cb925958b240c805300918343"},
    {file = "coverage-7.13.2-cp313-cp313t-win_amd64.whl", hash = "sha256:9074896edd705a05769e3de0eac0a8388484b503b68863dd06d5e473f874fd47"},
    {file = "coverage-7.13.2-cp313-cp313t-win_arm64.whl", hash = "sha256:69e526e14f3f854eda573d3cf40cffd29a1a91c684743d904c33dbdcd0e0f3e7"},
    {file = "coverage-7.13.2-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:387a825f43d680e7310e6f325b2167dd093bc8ffd933b83e9aa0983cf6e0a2ef"},
    {file = "coverage-7.13.2-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:f0d7fea9d8e5d778cd5a9e8fc38308ad688f02040e883cdc13311ef2748cb40f"},
    {file = "coverage-7.13.2-cp314-cp314-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:e080afb413be106c95c4ee96b4fffdc9e2fa56a8bbf90b5c0918e5c4449412f5"},
    {file = "coverage-7.13.2-cp314-cp314-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:a7fc042ba3c7ce25b8a9f097eb0f32a5ce1ccdb639d9eec114e26def98e1f8a4"},
    {file = "coverage-7.13.2-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d0ba505e021557f7f8173ee8cd6b926373d8653e5ff7581ae2efce1b11ef4c27"},
    {file = "coverage-7.13.2-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:7de326f80e3451bd5cc7239ab46c73ddb658fe0b7649476bc7413572d36cd548"},
    {file = "coverage-7.13.2-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:abaea04f1e7e34841d4a7b343904a3f59481f62f9df39e2cd399d69a187a9660"},
    {file = "coverage-7.13.2-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:9f93959ee0c604bccd8e0697be21de0887b1f73efcc3aa73a3ec0fd13feace92"},
    {file = "coverage-7.13.2-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:13fe81ead04e34e105bf1b3c9f9cdf32ce31736ee5d90a8d2de02b9d3e1bcb82"},
    {file = "coverage-7.13.2-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:d6d16b0f71120e365741bca2cb473ca6fe38930bc5431c5e850ba949f708f892"},
    {file = "coverage-7.13.2-cp314-cp314-win32.whl", hash = "sha256:9b2f4714bb7d99ba3790ee095b3b4ac94767e1347fe424278a0b10acb3ff04fe"},
    {file = "coverage-7.13.2-cp314-cp314-win_amd64.whl", hash = "sha256:e4121a90823a063d717a96e0a0529c727fb31ea889369a0ee3ec00ed99bf6859"},
    {file = "coverage-7.13.2-cp314-cp314-win_arm64.whl", hash = "sha256:6873f0271b4a15a33e7590f338d823f6f66f91ed147a03938d7ce26efd04eee6"},
    {file = "coverage-7.13.2-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:f61d349f5b7cd95c34017f1927ee379bfbe9884300d74e07cf630ccf7a610c1b"},
    {file = "coverage-7.13.2-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:a43d34ce714f4ca674c0d90beb760eb05aad906f2c47580ccee9da8fe8bfb417"},
    {file = "coverage-7.13.2-cp314-cp314t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:bff1b04cb9d4900ce5c56c4942f047dc7efe57e2608cb7c3c8936e9970ccdbee"},
    {file = "coverage-7.13.2-cp314-cp314t-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:6ae99e4560963ad8e163e819e5d77d413d331fd00566c1e0856aa252303552c1"},
    {file = "coverage-7.13.2-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:e79a8c7d461820257d9aa43716c4efc55366d7b292e46b5b37165be1d377405d"},
    {file = "coverage-7.13.2-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:060ee84f6a769d40c492711911a76811b4befb6fba50abb450371abb720f5bd6"},
    {file = "coverage-7.13.2-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:3bca209d001fd03ea2d978f8a4985093240a355c93078aee3f799852c23f561a"},
    {file = "coverage-7.13.2-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:6b8092aa38d72f091db61ef83cb66076f18f02da3e1a75039a4f218629600e04"},
    {file = "coverage-7.13.2-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:4a3158dc2dcce5200d91ec28cd315c999eebff355437d2765840555d765a6e5f"},
    {file = "coverage-7.13.2-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:3973f353b2d70bd9796cc12f532a05945232ccae966456c8ed7034cb96bbfd6f"},
    {file = "coverage-7.13.2-cp314-cp314t-win32.whl", hash = "sha256:79f6506a678a59d4ded048dc72f1859ebede8ec2b9a2d509ebe161f01c2879d3"},
    {file = "coverage-7.13.2-cp314-cp314t-win_amd64.whl", hash = "sha256:196bfeabdccc5a020a57d5a368c681e3a6ceb0447d153aeccc1ab4d70a5032ba"},
    {file = "coverage-7.13.2-cp314-cp314t-win_arm64.whl", hash = "sha256:69269ab58783e090bfbf5b916ab3d188126e22d6070bbfc93098fdd474ef937c"},
    {file = "coverage-7.13.2-py3-none-any.whl", hash = "sha256:40ce1ea1e25125556d8e76bd0b61500839a07944cc287ac21d5626f3e620cad5"},
    {file = "coverage-7.13.2.tar.gz", hash = "sha256:044c6951ec37146b72a50cc81ef02217d27d4c3640efd2640311393cbbf143d3"},
]

[package.dependencies]
tomli = {version = "*", optional = true, markers = "python_full_version <= \"3.11.0a6\" and extra == \"toml\""}

[package.extras]
toml = ["tomli ; python_full_version <= \"3.11.0a6\""]

[[package]]
name = "deprecation"
version = "2.1.0"
description = "A library to handle automated deprecations"
optional = false
python-versions = "*"
groups = ["main", "dev"]
files = [
    {file = "deprecation-2.1.0-py2.py3-none-any.whl", hash = "sha256:a10811591210e1fb0e768a8c25517cabeabcba6f0bf96564f8ff45189f90b14a"},
    {file = "deprecation-2.1.0.tar.gz", hash = "sha256:72b3bde64e5d778694b0cf68178aed03d15e15477116add3fb773e581f9518ff"},
]

[package.dependencies]
packaging = "*"

[[package]]
name = "distlib"
version = "0.4.0"
description = "Distribution utilities"
optional = false
python-versions = "*"
groups = ["dev"]
files = [
    {file = "distlib-0.4.0-py2.py3-none-any.whl", hash = "sha256:9659f7d87e46584a30b5780e43ac7a2143098441670ff0a49d5f9034c54a6c16"},
    {file = "distlib-0.4.0.tar.gz", hash = "sha256:feec40075be03a04501a973d81f633735b4b69f98b05450592310c0f401a4e0d"},
]

[[package]]
name = "exceptiongroup"
version = "1.3.1"
description = "Backport of PEP 654 (exception groups)"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
markers = "python_version == \"3.10\""
files = [
    {file = "exceptiongroup-1.3.1-py3-none-any.whl", hash = "sha256:a7a39a3bd276781e98394987d3a5701d0c4edffb633bb7a5144577f82c773598"},
    {file = "exceptiongroup-1.3.1.tar.gz", hash = "sha256:8b412432c6055b0b7d14c310000ae93352ed6754f70fa8f7c34141f91c4e3219"},
]

[package.dependencies]
typing-extensions = {version = ">=4.6.0", markers = "python_version < \"3.13\""}

[package.extras]
test = ["pytest (>=6)"]

[[package]]
name = "filelock"
version = "3.29.0"
description = "A platform independent file lock."
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "filelock-3.29.0-py3-none-any.whl", hash = "sha256:96f5f6344709aa1572bbf631c640e4ebeeb519e08da902c39a001882f30ac258"},
    {file = "filelock-3.29.0.tar.gz", hash = "sha256:69974355e960702e789734cb4871f884ea6fe50bd8404051a3530bc07809cf90"},
]

[[package]]
name = "flake8"
version = "5.0.4"
description = "the modular source code checker: pep8 pyflakes and co"
optional = false
python-versions = ">=3.6.1"
groups = ["dev"]
markers = "python_version < \"3.12\""
files = [
    {file = "flake8-5.0.4-py2.py3-none-any.whl", hash = "sha256:7a1cf6b73744f5806ab95e526f6f0d8c01c66d7bbe349562d22dfca20610b248"},
    {file = "flake8-5.0.4.tar.gz", hash = "sha256:6fbe320aad8d6b95cec8b8e47bc933004678dc63095be98528b7bdd2a9f510db"},
]

[package.dependencies]
mccabe = ">=0.7.0,<0.8.0"
pycodestyle = ">=2.9.0,<2.10.0"
pyflakes = ">=2.5.0,<2.6.0"

[[package]]
name = "flake8"
version = "6.1.0"
description = "the modular source code checker: pep8 pyflakes and co"
optional = false
python-versions = ">=3.8.1"
groups = ["dev"]
markers = "python_version >= \"3.12\""
files = [
    {file = "flake8-6.1.0-py2.py3-none-any.whl", hash = "sha256:ffdfce58ea94c6580c77888a86506937f9a1a227dfcd15f245d694ae20a6b6e5"},
    {file = "flake8-6.1.0.tar.gz", hash = "sha256:d5b3857f07c030bdb5bf41c7f53799571d75c4491748a3adcd47de929e34cd23"},
]

[package.dependencies]
mccabe = ">=0.7.0,<0.8.0"
pycodestyle = ">=2.11.0,<2.12.0"
pyflakes = ">=3.1.0,<3.2.0"

[[package]]
name = "flake8-black"
version = "0.4.0"
description = "flake8 plugin to call black as a code style validator"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "flake8_black-0.4.0-py3-none-any.whl", hash = "sha256:288762d0c9ea065782d87eeecbcc20c69079d17fe1d0f0445f0eb0b0ffb80c39"},
    {file = "flake8_black-0.4.0.tar.gz", hash = "sha256:bf226868f695dee48d55ff6d7747e900709bfd6f605b7a378c70e711e3fc26cb"},
]

[package.dependencies]
black = ">=22.1.0"
flake8 = ">=3"
tomli = {version = "*", markers = "python_version < \"3.11\""}

[package.extras]
develop = ["build", "twine"]

[[package]]
name = "flake8-docstrings"
version = "1.7.0"
description = "Extension for flake8 which uses pydocstyle to check docstrings"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "flake8_docstrings-1.7.0-py2.py3-none-any.whl", hash = "sha256:51f2344026da083fc084166a9353f5082b01f72901df422f74b4d953ae88ac75"},
    {file = "flake8_docstrings-1.7.0.tar.gz", hash = "sha256:4c8cc748dc16e6869728699e5d0d685da9a10b0ea718e090b1ba088e67a941af"},
]

[package.dependencies]
flake8 = ">=3"
pydocstyle = ">=2.1"

[[package]]
name = "flake8-import-order"
version = "0.18.2"
description = "Flake8 and pylama plugin that checks the ordering of import statements."
optional = false
python-versions = "*"
groups = ["dev"]
files = [
    {file = "flake8-import-order-0.18.2.tar.gz", hash = "sha256:e23941f892da3e0c09d711babbb0c73bc735242e9b216b726616758a920d900e"},
    {file = "flake8_import_order-0.18.2-py2.py3-none-any.whl", hash = "sha256:82ed59f1083b629b030ee9d3928d9e06b6213eb196fe745b3a7d4af2168130df"},
]

[package.dependencies]
pycodestyle = "*"
setuptools = "*"

[[package]]
name = "flake8-tidy-imports"
version = "4.12.0"
description = "A flake8 plugin that helps you write tidier imports."
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "flake8_tidy_imports-4.12.0-py3-none-any.whl", hash = "sha256:ab1e31a5ce07518a31c0a34cd92551f4c27639ae2c35a21364680a0318da312e"},
    {file = "flake8_tidy_imports-4.12.0.tar.gz", hash = "sha256:9254788c3b6862c2fcec0250d2dc9af089afebff9c5b8a8ac8b9525b059b06db"},
]

[package.dependencies]
flake8 = ">=3.8"

[[package]]
name = "grpcio"
version = "1.81.1"
description = "HTTP/2-based RPC framework"
optional = false
python-versions = ">=3.10"
groups = ["main", "dev"]
files = [
    {file = "grpcio-1.81.1-cp310-cp310-linux_armv7l.whl", hash = "sha256:6f9a0c9c1cc15c112d1c053064fd032b64917062292c3d70aea280e02ae10b77"},
    {file = "grpcio-1.81.1-cp310-cp310-macosx_11_0_universal2.whl", hash = "sha256:69ef28e54fc85397f91b8c19592b8ef3d81952080366914823bd8572a2958120"},
    {file = "grpcio-1.81.1-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:15641444eca4a29358107b3dceb74c1c6305c55c822fd199b458aaea4068a7fb"},
    {file = "grpcio-1.81.1-cp310-cp310-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:d4b2dddfc219f54f956ccd53cf76a1d338ffe68fc7f2849ec9c7feb9927ff692"},
    {file = "grpcio-1.81.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:ca1cc11d82677b9662082e5478b7528e2b7db7beaa6bdff42bd62789d81be399"},
    {file = "grpcio-1.81.1-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:aa2ba7d2ad6df4d80127cea65e5b8d5e2c3adbf153ff4804452836328aca7c54"},
    {file = "grpcio-1.81.1-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:592b5fee597faa91cce2dd294dd7d9a1c83d76c4dbf877e33ec1adb866b2fbed"},
    {file = "grpcio-1.81.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:62481553b1793a27e9b9c3cf9e5bd483ef045ca72462592074b46d42b0c4d9b9"},
    {file = "grpcio-1.81.1-cp310-cp310-win32.whl", hash = "sha256:bb693b1e3d9a2f3fd228e2110daf4b5aeedb36761ca1e4282f74725f6d89f611"},
    {file = "grpcio-1.81.1-cp310-cp310-win_amd64.whl", hash = "sha256:88268ca418cacea64cecb0d1d600d3c6b3a8038fcba02e1e205178c5b1f47661"},
    {file = "grpcio-1.81.1-cp311-cp311-linux_armv7l.whl", hash = "sha256:d71d30f2d92f67d944631c523713934fee37292469e182ebcd2c1dd8a64ce53f"},
    {file = "grpcio-1.81.1-cp311-cp311-macosx_11_0_universal2.whl", hash = "sha256:b137f4bf3ada9dc44d411478decc6ff09a79ed30b306cd2abaa98408c3588137"},
    {file = "grpcio-1.81.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:a3acb384427816dd5d470f47e62137b87f74da694faa8a50147012cf40df276a"},
    {file = "grpcio-1.81.1-cp311-cp311-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:f9a0ebbe45c29b5e5866593c12b78bd9035f0f0f0d4bc8361680cd580d99db49"},
    {file = "grpcio-1.81.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:0a37165cc80b1a368384b383e63a4c38116a10467ae44c904d2d7468c4470ec2"},
    {file = "grpcio-1.81.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:6282caffb41ec326d4cb67ca9cf53b739d1b2f975a2acb498c7418e9f7d9a416"},
    {file = "grpcio-1.81.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:a35009284d0d3d5c2c9601c164a911b8b4331608d98a9a66d47d97bb2f522b70"},
    {file = "grpcio-1.81.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:1b22c80559854b789a01fd89e8929b3798a156c0829b5282a8939f33ad4115ad"},
    {file = "grpcio-1.81.1-cp311-cp311-win32.whl", hash = "sha256:428bec0161b48d8cf583c068591bc0016d0d9cfff52462b72b3884861ea768c5"},
    {file = "grpcio-1.81.1-cp311-cp311-win_amd64.whl", hash = "sha256:30e825f6848d9f18bba350ed6c75c1b02a0b5184474a31db9a32b1fa66fd8c79"},
    {file = "grpcio-1.81.1-cp312-cp312-linux_armv7l.whl", hash = "sha256:8b39472beafc0bdcafc4c8c73ad082ebfdb449d566897a61e7acb4fa88089115"},
    {file = "grpcio-1.81.1-cp312-cp312-macosx_11_0_universal2.whl", hash = "sha256:12b7524c88d4026d3dcb7b0ebe16b6714f3b4af402ddd0f0639ab064a00c87c3"},
    {file = "grpcio-1.81.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:1e123f9b37edb8375fd74130d1f69c944bbf0a7b06761ae7211154b8759e94d2"},
    {file = "grpcio-1.81.1-cp312-cp312-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:2c2e2ae6867c2966b8daccc836d54a13218e0007e9a490aeb81dd05be64d22d7"},
    {file = "grpcio-1.81.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:766bc7c9a9c340342f4c864ccbda8e78111e4751f13b895812b9c148fb79e9d0"},
    {file = "grpcio-1.81.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:b259a04a737cb3496be0901328eb8b7552ed8df4865d8c8f1cf1bffcfc0776a3"},
    {file = "grpcio-1.81.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:85b10a45b8993d195c4f3ff57025b8d1e11834909ee475c403bfa60cb4caefaf"},
    {file = "grpcio-1.81.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:8ea1936c26b99999b27479853039a7f34713f56c49375ad52b38535ec93a796c"},
    {file = "grpcio-1.81.1-cp312-cp312-win32.whl", hash = "sha256:a185a04039df6cae8648bc8ab6d6fde7bf94f7188ecf7828e76ac52eef1e41d6"},
    {file = "grpcio-1.81.1-cp312-cp312-win_amd64.whl", hash = "sha256:3ad74f8bb1a18963914c5452d289422830b39459e8776ebbcd207be1fbfb1d94"},
    {file = "grpcio-1.81.1-cp313-cp313-linux_armv7l.whl", hash = "sha256:b10e1ff4756ed27d5a29d7fc79cfce7ef1ff56ad20025b89bac7cf79e09abbbe"},
    {file = "grpcio-1.81.1-cp313-cp313-macosx_11_0_universal2.whl", hash = "sha256:819edbdcb42ab8598b494bcf0222684bbb7a3c772bd1b1f0be7e029a6063c28e"},
    {file = "grpcio-1.81.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:c5bf2dc311127d91230cc79b92188c082634a06cf66c5234db49a43b910183b0"},
    {file = "grpcio-1.81.1-cp313-cp313-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:e8ca6a1fcdb2943c9cbc1804a1baf3acb6071d72a471591678ded84218006e14"},
    {file = "grpcio-1.81.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:e64dd101d380a115cc5a0c7856788adb535f1a4e21fc543775602f8be95180ae"},
    {file = "grpcio-1.81.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:98a07f9bf591e3a8919797bee1c53f026ba4acd587e5a4404c8e57c9ec36b2a5"},
    {file = "grpcio-1.81.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:c261d74b1a945cf895a9d6eccd1685a8e837531beaab782da4d630a8d12deffb"},
    {file = "grpcio-1.81.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:58ad1131c300d3c9b933802b3cc4dc69d380822935ba50b28703156ea826fbf7"},
    {file = "grpcio-1.81.1-cp313-cp313-win32.whl", hash = "sha256:78e29211f26da2fdd0e9c6d2b79f489476140cf7029b6a64808ade7ca4156a42"},
    {file = "grpcio-1.81.1-cp313-cp313-win_amd64.whl", hash = "sha256:edb59506291b647a30884b1d51a599d605f40b20af4a7dc3d33786a47a31de60"},
    {file = "grpcio-1.81.1-cp314-cp314-linux_armv7l.whl", hash = "sha256:506f48f2f9c29b143fca3dad7b0d518c188b6c9648c75a2ae6e2d9f2c13a060b"},
    {file = "grpcio-1.81.1-cp314-cp314-macosx_11_0_universal2.whl", hash = "sha256:d865db4a6318e1c1bea83292e0ed231090538fc4ca45425b0f0480eb338bbc6e"},
    {file = "grpcio-1.81.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:e2aa72e3ce1770317ef534f63d397b55e130725f5149bd36077c3b539019db27"},
    {file = "grpcio-1.81.1-cp314-cp314-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:0490c30c261eded63f3f354979f9dc4502a9fb944cccb60cd9dc85f5a7349854"},
    {file = "grpcio-1.81.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:410482da976329fe5f4067270401b12cf2bd552ff8020f054ecfaddb5475f9d6"},
    {file = "grpcio-1.81.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:e3657301562ac3cb8018d30d0d3ebfa39932239f7b5703422057ef14b69949f5"},
    {file = "grpcio-1.81.1-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:24c8e57504c8f45b237e40b99262d181071e5099a07053695b75d97bb53053a0"},
    {file = "grpcio-1.81.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:b427c19380991a4eaab2f6144b64b99b412043314c6bf4ab544f97bb31ee4190"},
    {file = "grpcio-1.81.1-cp314-cp314-win32.whl", hash = "sha256:61233fe8951e5c85dff81c2458b6528624760166946b5b47ea150a589168411f"},
    {file = "grpcio-1.81.1-cp314-cp314-win_amd64.whl", hash = "sha256:3768a5ff1b2125e6f552e561b6b2dca0e64982d8949689b4df145cf8b98d7821"},
    {file = "grpcio-1.81.1.tar.gz", hash = "sha256:6fa10a767143a5e82e8eaab53918af0cd8909a57a27f8cb2288b80a613ac671b"},
]

[package.dependencies]
typing-extensions = ">=4.12,<5.0"

[package.extras]
protobuf = ["grpcio-tools (>=1.81.1)"]

[[package]]
name = "grpcio-tools"
version = "1.49.1"
description = "Protobuf code generator for gRPC"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
markers = "python_version < \"3.12\""
files = [
    {file = "grpcio-tools-1.49.1.tar.gz", hash = "sha256:84cc64e5b46bad43d5d7bd2fd772b656eba0366961187a847e908e2cb735db91"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-linux_armv7l.whl", hash = "sha256:2dfb6c7ece84d46bd690b23d3e060d18115c8bc5047d2e8a33e6747ed323a348"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-macosx_10_10_x86_64.whl", hash = "sha256:8f452a107c054a04db2570f7851a07f060313c6e841b0d394ce6030d598290e6"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-manylinux_2_17_aarch64.whl", hash = "sha256:6a198871b582287213c4d70792bf275e1d7cf34eed1d019f534ddf4cd15ab039"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:a0cca67a7d0287bdc855d81fdd38dc949c4273273a74f832f9e520abe4f20bc6"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:bdaff4c89eecb37c247b93025410db68114d97fa093cbb028e9bd7cda5912473"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:bb8773118ad315db317d7b22b5ff75d649ca20931733281209e7cbd8c0fad53e"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:7cc5534023735b8a8f56760b7c533918f874ce5a9064d7c5456d2709ae2b31f9"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-win32.whl", hash = "sha256:d277642acbe305f5586f9597b78fb9970d6633eb9f89c61e429c92c296c37129"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-win_amd64.whl", hash = "sha256:eed599cf08fc1a06c72492d3c5750c32f58de3750eddd984af1f257c14326701"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-linux_armv7l.whl", hash = "sha256:9e5c13809ab2f245398e8446c4c3b399a62d591db651e46806cccf52a700452e"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-macosx_10_10_x86_64.whl", hash = "sha256:ab3d0ee9623720ee585fdf3753b3755d3144a4a8ae35bca8e3655fa2f41056be"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:6ba87e3512bc91d78bf9febcfb522eadda171d2d4ddaf886066b0f01aa4929ad"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:13e13b3643e7577a3ec13b79689eb4d7548890b1e104c04b9ed6557a3c3dd452"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-musllinux_1_1_i686.whl", hash = "sha256:324f67d9cb4b7058b6ce45352fb64c20cc1fa04c34d97ad44772cfe6a4ae0cf5"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:a64bab81b220c50033f584f57978ebbea575f09c1ccee765cd5c462177988098"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-win32.whl", hash = "sha256:f632d376f92f23e5931697a3acf1b38df7eb719774213d93c52e02acd2d529ac"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-win_amd64.whl", hash = "sha256:28ff2b978d9509474928b9c096a0cce4eaa9c8f7046136aee1545f6211ed8126"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-linux_armv7l.whl", hash = "sha256:46afd3cb7e555187451a5d283f108cdef397952a662cb48680afc615b158864a"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-macosx_10_10_x86_64.whl", hash = "sha256:9284568b728e41fa8f7e9c2e7399545d605f75d8072ef0e9aa2a05655cb679eb"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-manylinux_2_17_aarch64.whl", hash = "sha256:aa34442cf787732cb41f2aa6172007e24f480b8b9d3dc5166de80d63e9072ea4"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:3b8c9eb5a4250905414cd53a68caea3eb8f0c515aadb689e6e81b71ebe9ab5c6"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ab15db024051bf21feb21c29cb2c3ea0a2e4f5cf341d46ef76e17fcf6aaef164"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-musllinux_1_1_i686.whl", hash = "sha256:502084b622f758bef620a9107c2db9fcdf66d26c7e0e481d6bb87db4dc917d70"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-musllinux_1_1_x86_64.whl", hash = "sha256:4085890b77c640085f82bf1e90a0ea166ce48000bc2f5180914b974783c9c0a8"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-win32.whl", hash = "sha256:da0edb984699769ce02e18e3392d54b59a7a3f93acd285a68043f5bde4fc028e"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-win_amd64.whl", hash = "sha256:9887cd622770271101a7dd1832845d64744c3f88fd11ccb2620394079197a42e"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-linux_armv7l.whl", hash = "sha256:8440fe7dae6a40c279e3a24b82793735babd38ecbb0d07bb712ff9c8963185d9"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-macosx_10_10_x86_64.whl", hash = "sha256:b5de2bb7dd6b6231da9b1556ade981513330b740e767f1d902c71ceee0a7d196"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-manylinux_2_17_aarch64.whl", hash = "sha256:1e6f06a763aea7836b63d9c117347f2bf7038008ceef72758815c9e09c5fb1fc"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:e31562f90120318c5395aabec0f2f69ad8c14b6676996b7730d9d2eaf9415d57"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:49ef9a4e389a618157a9daa9fafdfeeaef1ece9adda7f50f85db928f24d4b3e8"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-musllinux_1_1_i686.whl", hash = "sha256:b384cb8e8d9bcb55ee8f9b064374561c7a1a05d848249581403d36fc7060032f"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:73732f77943ac3e898879cbb29c27253aa3c47566b8a59780fd24c6a54de1b66"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-win32.whl", hash = "sha256:b594b2745a5ba9e7a76ce561bc5ab40bc65bb44743c505529b1e4f12af29104d"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-win_amd64.whl", hash = "sha256:680fbc88f8709ddcabb88f86749f2d8e429160890cff2c70680880a6970d4eef"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-linux_armv7l.whl", hash = "sha256:e8c3869121860f6767eedb7d24fc54dfd71e737fdfbb26e1334684606f3274fd"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-macosx_10_10_x86_64.whl", hash = "sha256:73e9d7c886ba10e20c97d1dab0ff961ba5800757ae5e31be21b1cda8130c52f8"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-manylinux_2_17_aarch64.whl", hash = "sha256:1760de2dd2c4f08de87b039043a4797f3c17193656e7e3eb84e92f0517083c0c"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:cd4b1e216dd04d9245ee8f4e601a1f98c25e6e417ea5cf8d825c50589a8b447e"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c1c28751ab5955cae563d07677e799233f0fe1c0fc49d9cbd61ff1957e83617f"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:c24239c3ee9ed16314c14b4e24437b5079ebc344f343f33629a582f8699f583b"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:892d3dacf1942820f0b7a868a30e6fbcdf5bec08543b682c7274b0101cee632d"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-win32.whl", hash = "sha256:704d21509ec06efc9d034dbe70e7152715aac004941f4f0f553cf3a0aff15bd5"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-win_amd64.whl", hash = "sha256:1efa0c221c719433f441ac0e026fc3c4dbc9a1a08a552ecdc707775e2f2fbbae"},
]

[package.dependencies]
grpcio = ">=1.49.1"
protobuf = ">=4.21.3,<5.0.dev0"
setuptools = "*"

[[package]]
name = "grpcio-tools"
version = "1.59.0"
description = "Protobuf code generator for gRPC"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
markers = "python_version == \"3.12\""
files = [
    {file = "grpcio-tools-1.59.0.tar.gz", hash = "sha256:aa4018f2d8662ac4d9830445d3d253a11b3e096e8afe20865547137aa1160e93"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-linux_armv7l.whl", hash = "sha256:882b809b42b5464bee55288f4e60837297f9618e53e69ae3eea6d61b05ce48fa"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-macosx_12_0_universal2.whl", hash = "sha256:4499d4bc5aa9c7b645018d8b0db4bebd663d427aabcd7bee7777046cb1bcbca7"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-manylinux_2_17_aarch64.whl", hash = "sha256:f381ae3ad6a5eb27aad8d810438937d8228977067c54e0bd456fce7e11fdbf3d"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:f1c684c0d9226d04cadafced620a46ab38c346d0780eaac7448da96bf12066a3"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:40cbf712769242c2ba237745285ef789114d7fcfe8865fc4817d87f20015e99a"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:1df755951f204e65bf9232a9cac5afe7d6b8e4c87ac084d3ecd738fdc7aa4174"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:de156c18b0c638aaee3be6ad650c8ba7dec94ed4bac26403aec3dce95ffe9407"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-win32.whl", hash = "sha256:9af7e138baa9b2895cf1f3eb718ac96fc5ae2f8e31fca405e21e0e5cd1643c52"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-win_amd64.whl", hash = "sha256:f14a6e4f700dfd30ff8f0e6695f944affc16ae5a1e738666b3fae4e44b65637e"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-linux_armv7l.whl", hash = "sha256:db030140d0da2368319e2f23655df3baec278c7e0078ecbe051eaf609a69382c"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-macosx_10_10_universal2.whl", hash = "sha256:eeed386971bb8afc3ec45593df6a1154d680d87be1209ef8e782e44f85f47e64"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-manylinux_2_17_aarch64.whl", hash = "sha256:962d1a3067129152cee3e172213486cb218a6bad703836991f46f216caefcf00"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:26eb2eebf150a33ebf088e67c1acf37eb2ac4133d9bfccbaa011ad2148c08b42"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:5b2d6da553980c590487f2e7fd3ec9c1ad8805ff2ec77977b92faa7e3ca14e1f"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-musllinux_1_1_i686.whl", hash = "sha256:335e2f355a0c544a88854e2c053aff8a3f398b84a263a96fa19d063ca1fe513a"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:204e08f807b1d83f5f0efea30c4e680afe26a43dec8ba614a45fa698a7ef0a19"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-win32.whl", hash = "sha256:05bf7b3ed01c8a562bb7e840f864c58acedbd6924eb616367c0bd0a760bdf483"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-win_amd64.whl", hash = "sha256:df85096fcac7cea8aa5bd84b7a39c4cdbf556b93669bb4772eb96aacd3222a4e"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-linux_armv7l.whl", hash = "sha256:240a7a3c2c54f77f1f66085a635bca72003d02f56a670e7db19aec531eda8f78"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-macosx_10_10_universal2.whl", hash = "sha256:6119f62c462d119c63227b9534210f0f13506a888151b9bf586f71e7edf5088b"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-manylinux_2_17_aarch64.whl", hash = "sha256:387662bee8e4c0b52cc0f61eaaca0ca583f5b227103f685b76083a3590a71a3e"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:8f0da5861ee276ca68493b217daef358960e8527cc63c7cb292ca1c9c54939af"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:d0f0806de1161c7f248e4c183633ee7a58dfe45c2b77ddf0136e2e7ad0650b1b"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-musllinux_1_1_i686.whl", hash = "sha256:c683be38a9bf4024c223929b4cd2f0a0858c94e9dc8b36d7eaa5a48ce9323a6f"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:f965707da2b48a33128615bcfebedd215a3a30e346447e885bb3da37a143177a"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-win32.whl", hash = "sha256:2ee960904dde12a7fa48e1591a5b3eeae054bdce57bacf9fd26685a98138f5bf"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-win_amd64.whl", hash = "sha256:71cc6db1d66da3bc3730d9937bddc320f7b1f1dfdff6342bcb5741515fe4110b"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-linux_armv7l.whl", hash = "sha256:f6263b85261b62471cb97b7505df72d72b8b62e5e22d8184924871a6155b4dbf"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-macosx_10_10_universal2.whl", hash = "sha256:b8e95d921cc2a1521d4750eedefec9f16031457920a6677edebe9d1b2ad6ae60"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-manylinux_2_17_aarch64.whl", hash = "sha256:cb63055739808144b541986291679d643bae58755d0eb082157c4d4c04443905"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:8c4634b3589efa156a8d5860c0a2547315bd5c9e52d14c960d716fe86e0927be"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2d970aa26854f535ffb94ea098aa8b43de020d9a14682e4a15dcdaeac7801b27"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-musllinux_1_1_i686.whl", hash = "sha256:821dba464d84ebbcffd9d420302404db2fa7a40c7ff4c4c4c93726f72bfa2769"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-musllinux_1_1_x86_64.whl", hash = "sha256:0548e901894399886ff4a4cd808cb850b60c021feb4a8977a0751f14dd7e55d9"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-win_amd64.whl", hash = "sha256:bb87158dbbb9e5a79effe78d54837599caa16df52d8d35366e06a91723b587ae"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-linux_armv7l.whl", hash = "sha256:1d551ff42962c7c333c3da5c70d5e617a87dee581fa2e2c5ae2d5137c8886779"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-macosx_10_10_universal2.whl", hash = "sha256:4ee443abcd241a5befb05629013fbf2eac637faa94aaa3056351aded8a31c1bc"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-manylinux_2_17_aarch64.whl", hash = "sha256:520c0c83ea79d14b0679ba43e19c64ca31d30926b26ad2ca7db37cbd89c167e2"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:9fc02a6e517c34dcf885ff3b57260b646551083903e3d2c780b4971ce7d4ab7c"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6aec8a4ed3808b7dfc1276fe51e3e24bec0eeaf610d395bcd42934647cf902a3"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-musllinux_1_1_i686.whl", hash = "sha256:99b3bde646720bbfb77f263f5ba3e1a0de50632d43c38d405a0ef9c7e94373cd"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:51d9595629998d8b519126c5a610f15deb0327cd6325ed10796b47d1d292e70b"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-win32.whl", hash = "sha256:bfa4b2b7d21c5634b62e5f03462243bd705adc1a21806b5356b8ce06d902e160"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-win_amd64.whl", hash = "sha256:9ed05197c5ab071e91bcef28901e97ca168c4ae94510cb67a14cb4931b94255a"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-linux_armv7l.whl", hash = "sha256:498e7be0b14385980efa681444ba481349c131fc5ec88003819f5d929646947c"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-macosx_10_10_universal2.whl", hash = "sha256:b519f2ecde9a579cad2f4a7057d5bb4e040ad17caab8b5e691ed7a13b9db0be9"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-manylinux_2_17_aarch64.whl", hash = "sha256:ef3e8aca2261f7f07436d4e2111556c1fb9bf1f9cfcdf35262743ccdee1b6ce9"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:27a7f226b741b2ebf7e2d0779d2c9b17f446d1b839d59886c1619e62cc2ae472"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:784aa52965916fec5afa1a28eeee6f0073bb43a2a1d7fedf963393898843077a"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:e312ddc2d8bec1a23306a661ad52734f984c9aad5d8f126ebb222a778d95407d"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:868892ad9e00651a38dace3e4924bae82fc4fd4df2c65d37b74381570ee8deb1"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-win32.whl", hash = "sha256:a4f6cae381f21fee1ef0a5cbbbb146680164311157ae618edf3061742d844383"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-win_amd64.whl", hash = "sha256:4a10e59cca462208b489478340b52a96d64e8b8b6f1ac097f3e8cb211d3f66c0"},
]

[package.dependencies]
grpcio = ">=1.59.0"
protobuf = ">=4.21.6,<5.0.dev0"
setuptools = "*"

[[package]]
name = "grpcio-tools"
version = "1.67.0"
description = "Protobuf code generator for gRPC"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
markers = "python_version == \"3.13\""
files = [
    {file = "grpcio_tools-1.67.0-cp310-cp310-linux_armv7l.whl", hash = "sha256:12aa38af76b5ef00a55808c7c374ed18d5dc7cc8081b717e56da3c50df1776e2"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-macosx_12_0_universal2.whl", hash = "sha256:b0b03d055127bbc7c629454804b53b5cad2cedfcf904576d159a8a04c22b8e66"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-manylinux_2_17_aarch64.whl", hash = "sha256:02b0b50c59a8f7428326197027a2f586d216c46138c547f861533c46bff78bfe"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:b2afdfe151ed9edbd4a3fd646716f83b58010769c57f9c0aa1cf4c3bfb1240a8"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fc3eeb87575b2b360c5ef5aef22eb76cfdd6a255d2f628a48ab0e5a61a0039fb"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:ead78089c4771605a1ff8894e47f2267440693f1beeee06fd5a788aede83370f"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:0671dcdccef09ca4eb415c1d6f470a857c6486733c146676f6810a3ade1d42cb"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-win32.whl", hash = "sha256:a7398d90b8c7da479aec8f853d3664d5a93c209f8ac3bd41cb7ae4e8677a45c6"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-win_amd64.whl", hash = "sha256:f7e7d70a74df7e07be7cceaa694b7e8e5f3bef8e0299906f60885ecf7a40adb4"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-linux_armv7l.whl", hash = "sha256:655716bf931a22a090134d87953710033640996d31e36f5f9b0106ff5f552d8e"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:484ae782f9d3ff58e0bbb2f4cad14d5f5d9132fc701835b1dffd2c2a06f73ba6"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-manylinux_2_17_aarch64.whl", hash = "sha256:f3e34de876efe1273f91e25ef241e449ed7f9411472dd9ff56d2039618017c30"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:d8301719edde2c3d388995703cdd962f558b76e9750405f772dce61402e4c3d0"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1629ea246044ccd473d9ac4c9f137a440d830b5e08d35225e1b354dbbb15b75d"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-musllinux_1_1_i686.whl", hash = "sha256:d77a3c5cec0065267ca1a0b2589ececd1277ce25aa67f13ec50c816ee6f26f7f"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:c9bf992bcc7d9e6eaa20705056e1b955593092a38cec1746fef389d873ab2056"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-win32.whl", hash = "sha256:7e6e3db119c38629e0767cdb2ee18726ecc87e2249117d4c9e7ce06ea8c894ea"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-win_amd64.whl", hash = "sha256:c6c27aec301a0e6cf231f9ee1c467c64002af51170fa7c0f3bb10bbfcd03fee7"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-linux_armv7l.whl", hash = "sha256:dca7f053cbdb26a587d4410ddb893877c585fb60a31f22fdd128e4f7c4dab27c"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-macosx_10_9_universal2.whl", hash = "sha256:de8c4f68ffa690769d84329c17c7fdd5fbe4c61b8f8a0de03f1ad8ef8bb06963"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-manylinux_2_17_aarch64.whl", hash = "sha256:6e4ecb24c27a78f09fead45d4ed873805d6026124ccb6793b6fb93a490b78ddf"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:004d6ef1b5f724480f05c0bdc904bf8c78c43d633c537d99abe51b52ce0cadeb"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9dd257072c86eb9b36791b3674a513a215ba76bbdd38fc228f0e8c6dc5ce3524"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-musllinux_1_1_i686.whl", hash = "sha256:a8cca551317ed26e17d13b6ee27b2bd62f5fe9b3842b4e88389deb984f995848"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:a7ac3b4f837c693142f6688b629d1f6408f6ab250d927159b572555f5339fe25"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-win32.whl", hash = "sha256:95feec33388e2a8f72c360a68efe6f0bfed9c771e94d21b7f2359d0010f60219"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-win_amd64.whl", hash = "sha256:50a31d035193ebe7154181eac84734e25bdcdb36adba849d3b2adf1c3b0c382b"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-linux_armv7l.whl", hash = "sha256:9ecb7c2e5da052a3feaeaa83d8f2a946a8feec8a50751b0e6175da982b49ebb1"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:3c52164f2b9d41c6d75464bb45f45737dcb421e92e98d85d94fda100c67a24d8"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-manylinux_2_17_aarch64.whl", hash = "sha256:471f58b919767290260d427dd9b760796e6208ee5fcda2f76bb8bd585ff842ec"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:72c6bcdf38f672721c093c92b1fb1f9a02a365acc5bd42e1c69fe6e904b26081"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:833b1eb9c03d28a798294523f75294055eff78fa897adf797876337b901afeb9"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-musllinux_1_1_i686.whl", hash = "sha256:1db92ad6ade1946fc5705eb04956fcfdb3a0a4682de8dc3fce31cb97b6e4fcb8"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:38128310ded818e1044c0cd0979d76f7c0d3c3946a526a8aa39cd258624c3bf3"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-win32.whl", hash = "sha256:db57930dc20ab678311727883bdb9f122daf06c14f3fd3067c9ccedb7eb056c3"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-win_amd64.whl", hash = "sha256:7de44d8d3bb920a4973a559f2950d03382fa4aed4880306416ffa73d24838477"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-linux_armv7l.whl", hash = "sha256:793896648734aad3ad8f26795dcdd6040aecd35efef43fcbb67d221373e6379a"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-macosx_10_9_universal2.whl", hash = "sha256:941418cba6a8adfcac3ff7ff3bdef00b55a44d673634c15bddcfa7778e49239e"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-manylinux_2_17_aarch64.whl", hash = "sha256:0d63ff6be6f3d0294249fc7a21f26f06c9cc209130c5328907cd678406d7d232"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:af80ced3ba49377ef7bec93e9ccbfa357875460e9a624ed12d9a7d5348741a76"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:e3c3fbb4a6d10764295540579492397bc7a3334e1a92dd17a4bc7b69159cf70a"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-musllinux_1_1_i686.whl", hash = "sha256:a05c10fb783f609d16e1f754ebad9bb432a1adbfc46139d154e8fd6b15f59988"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:ea8af001f08c678ab59e2bf2614d8b09d62210e540f7af1129c172fe4fd330c7"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-win32.whl", hash = "sha256:004d329aee385fa874979196e5359a967c370d31813f61eba88043ccaa2e06d8"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-win_amd64.whl", hash = "sha256:fc43593bd051abb73a5d130fc041923144089ac459fb01165960106ebb686fd0"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-linux_armv7l.whl", hash = "sha256:d285c036ddfc2618c4db60b584409dd8313d41473bd46177c763ea22ed9aeb1f"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:623fdad489447e1565d0ba5a818d54b4e74cd73800b6a32c4c009601c7f7a36c"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-manylinux_2_17_aarch64.whl", hash = "sha256:24536af8a5f8e532fbd996c1763eff51526d1d1563f9499ff5ffffb9a08811f3"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:bd64a9a8eb675dd2aa59cb4b2ab025a3b02ae1bb9e483c7fb518ffa0f0755cda"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f94378bc90fb008b0a56237748aa42c787fd86c392e7df3d65f0fe7fcd93844a"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:d0f39a9d860a6768574cd77b5d9ad81513fa1c575d3a050d4e72e6d79dcd62f3"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:c578f1306bfd0dd0668e24f8c04d61529928de2660217022a947a56be177bc2d"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-win32.whl", hash = "sha256:0c2cf8d09bdc05e0550ad413e0bc0d552500bb7f98d36079b7b9d38e064e02f7"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-win_amd64.whl", hash = "sha256:cc570bcd9c9681bb011f746ea90cc50559be629227aaaaae9fde8549525f0287"},
    {file = "grpcio_tools-1.67.0.tar.gz", hash = "sha256:181b3d4e61b83142c182ec366f3079b0023509743986e54c9465ca38cac255f8"},
]

[package.dependencies]
grpcio = ">=1.67.0"
protobuf = ">=5.26.1,<6.0.dev0"
setuptools = "*"

[[package]]
name = "grpcio-tools"
version = "1.75.1"
description = "Protobuf code generator for gRPC"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
markers = "python_version >= \"3.14\""
files = [
    {file = "grpcio_tools-1.75.1-cp310-cp310-linux_armv7l.whl", hash = "sha256:ae0f04d5ec8b8e13476bf516a08fc1de4e58c6bf79f99123a6b964ca7d02c790"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-macosx_11_0_universal2.whl", hash = "sha256:24a881ad7292e904fc256892b647da17d9137ef2e72faf8b7c8e515314ad1377"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:1b5810ace274dba12ecfac69ac32c8047c6ee0200a23274cb4885ed4187271f8"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:ab33993288b97b1180e092fa447a8ce00fbc8c59d67b23553245b88d14fe36bb"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:4cac693621043ef11d3ab2318e811d919779f8cd5011ba8e37f44c178c831d94"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:a09cd5d267b296af67116fe098633ad770bc8c19831a5f3c896f65fad90c1064"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:dff4bcb4d16cf9ef745c1984394ed15187e6c23d73d71377377deaf443d11358"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:16d5986b37e2a9203f85e456c7ff8705b932718021d408adfe4a79e0f4d95949"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-win32.whl", hash = "sha256:3fbac14998bfadc6b9140b6339dbc5f673700ebb4d45ba0c4d4fbe0ffb8559a9"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-win_amd64.whl", hash = "sha256:b56e495844eb899de721eb77d9e077192bdeb40842f598481d32a8f6de3db124"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-linux_armv7l.whl", hash = "sha256:f0635231feb70a9d551452829943a1a5fa651283e7a300aadc22df5ea5da696f"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-macosx_11_0_universal2.whl", hash = "sha256:626293296ef7e2d87ab1a80b81a55eef91883c65b59a97576099a28b9535100b"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:071339d90f1faab332ce4919c815a10b9c3ed2c09473f550f686bf9cc148579f"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:44195f58c052fa935b78c7438c85cbcd4b273dd685028e4f6d4d7b30d47daad1"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:860fafdb85726029d646c99859ff7bdca5aae61b5ff038c3bd355fc1ec6b2764"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:4559547a0cb3d3db1b982eea87d4656036339b400f48127fef932210672fb59e"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:9af65a310807d7f36a8f7cddea142fe97d6dffba74444f38870272f2e5a3a06b"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:8c1de31aefc0585d2f915a7cd0994d153547495b8d79c44c58048a3ede0b65be"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-win32.whl", hash = "sha256:efaf95fcaa5d3ac1bcfe44ceed9e2512eb95b5c8c476569bdbbe2bee4b59c8a9"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-win_amd64.whl", hash = "sha256:7cefe76fc35c825f0148d60d2294a527053d0f5dd6a60352419214a8c53223c9"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-linux_armv7l.whl", hash = "sha256:49b68936cf212052eeafa50b824e17731b78d15016b235d36e0d32199000b14c"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-macosx_11_0_universal2.whl", hash = "sha256:08cb6e568e58b76a2178ad3b453845ff057131fff00f634d7e15dcd015cd455b"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:168402ad29a249092673079cf46266936ec2fb18d4f854d96e9c5fa5708efa39"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:bbae11c29fcf450730f021bfc14b12279f2f985e2e493ccc2f133108728261db"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:38c6c7d5d4800f636ee691cd073db1606d1a6a76424ca75c9b709436c9c20439"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:626f6a61a8f141dde9a657775854d1c0d99509f9a2762b82aa401a635f6ec73d"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:f61a8334ae38d4f98c744a732b89527e5af339d17180e25fff0676060f8709b7"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:bd0c3fb40d89a1e24a41974e77c7331e80396ab7cde39bc396a13d6b5e2a750b"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-win32.whl", hash = "sha256:004bc5327593eea48abd03be3188e757c3ca0039079587a6aac24275127cac20"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-win_amd64.whl", hash = "sha256:23952692160b5fe7900653dfdc9858dc78c2c42e15c27e19ee780c8917ba6028"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-linux_armv7l.whl", hash = "sha256:ca9e116aab0ecf4365fc2980f2e8ae1b22273c3847328b9a8e05cbd14345b397"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-macosx_11_0_universal2.whl", hash = "sha256:9fe87a926b65eb7f41f8738b6d03677cc43185ff77a9d9b201bdb2f673f3fa1e"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:45503a6094f91b3fd31c3d9adef26ac514f102086e2a37de797e220a6791ee87"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:b01b60b3de67be531a39fd869d7613fa8f178aff38c05e4d8bc2fc530fa58cb5"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:09e2b9b9488735514777d44c1e4eda813122d2c87aad219f98d5d49b359a8eab"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:55e60300e62b220fabe6f062fe69f143abaeff3335f79b22b56d86254f3c3c80"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:49ce00fcc6facbbf52bf376e55b8e08810cecd03dab0b3a2986d73117c6f6ee4"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:71e95479aea868f8c8014d9dc4267f26ee75388a0d8a552e1648cfa0b53d24b4"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-win32.whl", hash = "sha256:fff9d2297416eae8861e53154ccf70a19994e5935e6c8f58ebf431f81cbd8d12"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-win_amd64.whl", hash = "sha256:1849ddd508143eb48791e81d42ddc924c554d1b4900e06775a927573a8d4267f"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-linux_armv7l.whl", hash = "sha256:f281b594489184b1f9a337cdfed1fc1ddb8428f41c4b4023de81527e90b38e1e"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-macosx_11_0_universal2.whl", hash = "sha256:becf8332f391abc62bf4eea488b63be063d76a7cf2ef00b2e36c617d9ee9216b"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:a08330f24e5cd7b39541882a95a8ba04ffb4df79e2984aa0cd01ed26dcdccf49"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:6bf3742bd8f102630072ed317d1496f31c454cd85ad19d37a68bd85bf9d5f8b9"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:f26028949474feb380460ce52d9d090d00023940c65236294a66c42ac5850e8b"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:1bd68fb98bf08f11b6c3210834a14eefe585bad959bdba38e78b4ae3b04ba5bd"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:f1496e21586193da62c3a73cd16f9c63c5b3efd68ff06dab96dbdfefa90d40bf"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:14a78b1e36310cdb3516cdf9ee2726107875e0b247e2439d62fc8dc38cf793c1"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-win32.whl", hash = "sha256:0e6f916daf222002fb98f9a6f22de0751959e7e76a24941985cc8e43cea77b50"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-win_amd64.whl", hash = "sha256:878c3b362264588c45eba57ce088755f8b2b54893d41cc4a68cdeea62996da5c"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-linux_armv7l.whl", hash = "sha256:eca28a90020fc1596f48cf51b02e56bc3d285f7f9ebaf0493144160d69c2cae7"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-macosx_11_0_universal2.whl", hash = "sha256:6744a14983f82e04cfd799ed779d06ee92035bb497f2d0fa84e81921a6c9c985"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:2a59120f17d36de6e16a058d88f2fcd255bafaccb487fea0613860a5287f77c6"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:02b0c237882e45247570afdc34717ce80831184882186ef47afca9f8cac2f71c"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:4999ada9721ce2a0eae66bf7f2793bc6fe7a473eef4e38bb542d1e5c6d9f7d91"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:dd13f0d87605eb34f8b8868e3ad9202b90e9e58417276db79c3298538d0d60e3"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:9555db0d2eb22850b7e9a27c0476627d483c114fcdf40d29b03aef446f5e4c43"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:a35800ce3ecea4aaad511bc18daccd37b1560132694f30b606f2044f1242c9a0"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-win32.whl", hash = "sha256:8e7f2c1a37a5c8db92c5cba4034c370598f7458b275606f7a2a114f8c25c0326"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-win_amd64.whl", hash = "sha256:0de3a82ee33d960f117ab66da51254cccd8bda9118d11ec3379f954cfbf6bc39"},
    {file = "grpcio_tools-1.75.1.tar.gz", hash = "sha256:bb78960cf3d58941e1fec70cbdaccf255918beed13c34112a6915a6d8facebd1"},
]

[package.dependencies]
grpcio = ">=1.75.1"
protobuf = ">=6.31.1,<7.0.0"
setuptools = "*"

[[package]]
name = "hightime"
version = "1.0.0"
description = "Hightime Python API"
optional = false
python-versions = "<4.0,>=3.9"
groups = ["main", "dev"]
files = [
    {file = "hightime-1.0.0-py3-none-any.whl", hash = "sha256:ba86d42976c36451b14e11c736e61f296f9f00dbb79c8488e18d70c6b2dbb395"},
    {file = "hightime-1.0.0.tar.gz", hash = "sha256:480d2a03e2c3ed44916d2406d40ab6d10a276ed7f101619fc3fcc1e00c46aacf"},
]

[[package]]
name = "iniconfig"
version = "2.3.0"
description = "brain-dead simple config-ini parsing"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "iniconfig-2.3.0-py3-none-any.whl", hash = "sha256:f631c04d2c48c52b84d0d0549c99ff3859c98df65b3101406327ecc7d53fbf12"},
    {file = "iniconfig-2.3.0.tar.gz", hash = "sha256:c76315c77db068650d49c5b56314774a7804df16fee4402c1f19d6d15d8c4730"},
]

[[package]]
name = "isort"
version = "7.0.0"
description = "A Python utility / library to sort Python imports."
optional = false
python-versions = ">=3.10.0"
groups = ["dev"]
files = [
    {file = "isort-7.0.0-py3-none-any.whl", hash = "sha256:1bcabac8bc3c36c7fb7b98a76c8abb18e0f841a3ba81decac7691008592499c1"},
    {file = "isort-7.0.0.tar.gz", hash = "sha256:5513527951aadb3ac4292a41a16cbc50dd1642432f5e8c20057d414bdafb4187"},
]

[package.extras]
colors = ["colorama"]
plugins = ["setuptools"]

[[package]]
name = "librt"
version = "0.9.0"
description = "Mypyc runtime library"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
markers = "platform_python_implementation != \"PyPy\""
files = [
    {file = "librt-0.9.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:2f8e12706dcb8ff6b3ed57514a19e45c49ad00bcd423e87b2b2e4b5f64578443"},
    {file = "librt-0.9.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:4e3dda8345307fd7306db0ed0cb109a63a2c85ba780eb9dc2d09b2049a931f9c"},
    {file = "librt-0.9.0-cp310-cp310-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:de7dac64e3eb832ffc7b840eb8f52f76420cde1b845be51b2a0f6b870890645e"},
    {file = "librt-0.9.0-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:22a904cbdb678f7cb348c90d543d3c52f581663d687992fee47fd566dcbf5285"},
    {file = "librt-0.9.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:224b9727eb8bc188bc3bcf29d969dba0cd61b01d9bac80c41575520cc4baabb2"},
    {file = "librt-0.9.0-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:e94cbc6ad9a6aeea46d775cbb11f361022f778a9cc8cc90af653d3a594b057ce"},
    {file = "librt-0.9.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:7bc30ad339f4e1a01d4917d645e522a0bc0030644d8973f6346397c93ba1503f"},
    {file = "librt-0.9.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:56d65b583cf43b8cf4c8fbe1e1da20fa3076cc32a1149a141507af1062718236"},
    {file = "librt-0.9.0-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:0a1be03168b2691ba61927e299b352a6315189199ca18a57b733f86cb3cc8d38"},
    {file = "librt-0.9.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:63c12efcd160e1d14da11af0c46c0217473e1e0d2ae1acbccc83f561ea4c2a7b"},
    {file = "librt-0.9.0-cp310-cp310-win32.whl", hash = "sha256:e9002e98dcb1c0a66723592520decd86238ddcef168b37ff6cfb559200b4b774"},
    {file = "librt-0.9.0-cp310-cp310-win_amd64.whl", hash = "sha256:9fcb461fbf70654a52a7cc670e606f04449e2374c199b1825f754e16dacfedd8"},
    {file = "librt-0.9.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:90904fac73c478f4b83f4ed96c99c8208b75e6f9a8a1910548f69a00f1eaa671"},
    {file = "librt-0.9.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:789fff71757facc0738e8d89e3b84e4f0251c1c975e85e81b152cdaca927cc2d"},
    {file = "librt-0.9.0-cp311-cp311-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:1bf465d1e5b0a27713862441f6467b5ab76385f4ecf8f1f3a44f8aa3c695b4b6"},
    {file = "librt-0.9.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f819e0c6413e259a17a7c0d49f97f405abadd3c2a316a3b46c6440b7dbbedbb1"},
    {file = "librt-0.9.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e0785c2fb4a81e1aece366aa3e2e039f4a4d7d21aaaded5227d7f3c703427882"},
    {file = "librt-0.9.0-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:80b25c7b570a86c03b5da69e665809deb39265476e8e21d96a9328f9762f9990"},
    {file = "librt-0.9.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:d4d16b608a1c43d7e33142099a75cd93af482dadce0bf82421e91cad077157f4"},
    {file = "librt-0.9.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:194fc1a32e1e21fe809d38b5faea66cc65eaa00217c8901fbdb99866938adbdb"},
    {file = "librt-0.9.0-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:8c6bc1384d9738781cfd41d09ad7f6e8af13cfea2c75ece6bd6d2566cdea2076"},
    {file = "librt-0.9.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:15cb151e52a044f06e54ac7f7b47adbfc89b5c8e2b63e1175a9d587c43e8942a"},
    {file = "librt-0.9.0-cp311-cp311-win32.whl", hash = "sha256:f100bfe2acf8a3689af9d0cc660d89f17286c9c795f9f18f7b62dd1a6b247ae6"},
    {file = "librt-0.9.0-cp311-cp311-win_amd64.whl", hash = "sha256:0b73e4266307e51c95e09c0750b7ec383c561d2e97d58e473f6f6a209952fbb8"},
    {file = "librt-0.9.0-cp311-cp311-win_arm64.whl", hash = "sha256:bc5518873822d2faa8ebdd2c1a4d7c8ef47b01a058495ab7924cb65bdbf5fc9a"},
    {file = "librt-0.9.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:9b3e3bc363f71bda1639a4ee593cb78f7fbfeacc73411ec0d4c92f00730010a4"},
    {file = "librt-0.9.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:0a09c2f5869649101738653a9b7ab70cf045a1105ac66cbb8f4055e61df78f2d"},
    {file = "librt-0.9.0-cp312-cp312-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:5ca8e133d799c948db2ab1afc081c333a825b5540475164726dcbf73537e5c2f"},
    {file = "librt-0.9.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:603138ee838ee1583f1b960b62d5d0007845c5c423feb68e44648b1359014e27"},
    {file = "librt-0.9.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f4003f70c56a5addd6aa0897f200dd59afd3bf7bcd5b3cce46dd21f925743bc2"},
    {file = "librt-0.9.0-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:78042f6facfd98ecb25e9829c7e37cce23363d9d7c83bc5f72702c5059eb082b"},
    {file = "librt-0.9.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:a361c9434a64d70a7dbb771d1de302c0cc9f13c0bffe1cf7e642152814b35265"},
    {file = "librt-0.9.0-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:dd2c7e082b0b92e1baa4da28163a808672485617bc855cc22a2fd06978fa9084"},
    {file = "librt-0.9.0-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:7e6274fd33fc5b2a14d41c9119629d3ff395849d8bcbc80cf637d9e8d2034da8"},
    {file = "librt-0.9.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:5093043afb226ecfa1400120d1ebd4442b4f99977783e4f4f7248879009b227f"},
    {file = "librt-0.9.0-cp312-cp312-win32.whl", hash = "sha256:9edcc35d1cae9fd5320171b1a838c7da8a5c968af31e82ecc3dff30b4be0957f"},
    {file = "librt-0.9.0-cp312-cp312-win_amd64.whl", hash = "sha256:3cc2917258e131ae5f958a4d872e07555b51cb7466a43433218061c74ef33745"},
    {file = "librt-0.9.0-cp312-cp312-win_arm64.whl", hash = "sha256:90e6d5420fc8a300518d4d2288154ff45005e920425c22cbbfe8330f3f754bd9"},
    {file = "librt-0.9.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:f29b68cd9714531672db62cc54f6e8ff981900f824d13fa0e00749189e13778e"},
    {file = "librt-0.9.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:7d5c8a5929ac325729f6119802070b561f4db793dffc45e9ac750992a4ed4d22"},
    {file = "librt-0.9.0-cp313-cp313-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:756775d25ec8345b837ab52effee3ad2f3b2dfd6bbee3e3f029c517bd5d8f05a"},
    {file = "librt-0.9.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:2b8f5d00b49818f4e2b1667db994488b045835e0ac16fe2f924f3871bd2b8ac5"},
    {file = "librt-0.9.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c81aef782380f0f13ead670aae01825eb653b44b046aa0e5ebbb79f76ed4aa11"},
    {file = "librt-0.9.0-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:66b58fed90a545328e80d575467244de3741e088c1af928f0b489ebec3ef3858"},
    {file = "librt-0.9.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:e78fb7419e07d98c2af4b8567b72b3eaf8cb05caad642e9963465569c8b2d87e"},
    {file = "librt-0.9.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:2c3786f0f4490a5cd87f1ed6cefae833ad6b1060d52044ce0434a2e85893afd0"},
    {file = "librt-0.9.0-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:8494cfc61e03542f2d381e71804990b3931175a29b9278fdb4a5459948778dc2"},
    {file = "librt-0.9.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:07cf11f769831186eeac424376e6189f20ace4f7263e2134bdb9757340d84d4d"},
    {file = "librt-0.9.0-cp313-cp313-win32.whl", hash = "sha256:850d6d03177e52700af605fd60db7f37dcb89782049a149674d1a9649c2138fd"},
    {file = "librt-0.9.0-cp313-cp313-win_amd64.whl", hash = "sha256:a5af136bfba820d592f86c67affcef9b3ff4d4360ac3255e341e964489b48519"},
    {file = "librt-0.9.0-cp313-cp313-win_arm64.whl", hash = "sha256:4c4d0440a3a8e31d962340c3e1cc3fc9ee7febd34c8d8f770d06adb947779ea5"},
    {file = "librt-0.9.0-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:3f05d145df35dca5056a8bc3838e940efebd893a54b3e19b2dda39ceaa299bcb"},
    {file = "librt-0.9.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:1c587494461ebd42229d0f1739f3aa34237dd9980623ecf1be8d3bcba79f4499"},
    {file = "librt-0.9.0-cp314-cp314-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:b0a2040f801406b93657a70b72fa12311063a319fee72ce98e1524da7200171f"},
    {file = "librt-0.9.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f38bc489037eca88d6ebefc9c4d41a4e07c8e8b4de5188a9e6d290273ad7ebb1"},
    {file = "librt-0.9.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f3fd278f5e6bf7c75ccd6d12344eb686cc020712683363b66f46ac79d37c799f"},
    {file = "librt-0.9.0-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:fcbdf2a9ca24e87bbebb47f1fe34e531ef06f104f98c9ccfc953a3f3344c567a"},
    {file = "librt-0.9.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:e306d956cfa027fe041585f02a1602c32bfa6bb8ebea4899d373383295a6c62f"},
    {file = "librt-0.9.0-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:465814ab157986acb9dfa5ccd7df944be5eefc0d08d31ec6e8d88bc71251d845"},
    {file = "librt-0.9.0-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:703f4ae36d6240bfe24f542bac784c7e4194ec49c3ba5a994d02891649e2d85b"},
    {file = "librt-0.9.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:3be322a15ee5e70b93b7a59cfd074614f22cc8c9ff18bd27f474e79137ea8d3b"},
    {file = "librt-0.9.0-cp314-cp314-win32.whl", hash = "sha256:b8da9f8035bb417770b1e1610526d87ad4fc58a2804dc4d79c53f6d2cf5a6eb9"},
    {file = "librt-0.9.0-cp314-cp314-win_amd64.whl", hash = "sha256:b8bd70d5d816566a580d193326912f4a76ec2d28a97dc4cd4cc831c0af8e330e"},
    {file = "librt-0.9.0-cp314-cp314-win_arm64.whl", hash = "sha256:fc5758e2b7a56532dc33e3c544d78cbaa9ecf0a0f2a2da2df882c1d6b99a317f"},
    {file = "librt-0.9.0-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:f24b90b0e0c8cc9491fb1693ae91fe17cb7963153a1946395acdbdd5818429a4"},
    {file = "librt-0.9.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:3fe56e80badb66fdcde06bef81bbaa5bfcf6fbd7aefb86222d9e369c38c6b228"},
    {file = "librt-0.9.0-cp314-cp314t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:527b5b820b47a09e09829051452bb0d1dd2122261254e2a6f674d12f1d793d54"},
    {file = "librt-0.9.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7d429bdd4ac0ab17c8e4a8af0ed2a7440b16eba474909ab357131018fe8c7e71"},
    {file = "librt-0.9.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:7202bdcac47d3a708271c4304a474a8605a4a9a4a709e954bf2d3241140aa938"},
    {file = "librt-0.9.0-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:c0d620e74897f8c2613b3c4e2e9c1e422eb46d2ddd07df540784d44117836af3"},
    {file = "librt-0.9.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:d69fc39e627908f4c03297d5a88d9284b73f4d90b424461e32e8c2485e21c283"},
    {file = "librt-0.9.0-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:c2640e23d2b7c98796f123ffd95cf2022c7777aa8a4a3b98b36c570d37e85eee"},
    {file = "librt-0.9.0-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:451daa98463b7695b0a30aa56bf637831ea559e7b8101ac2ef6382e8eb15e29c"},
    {file = "librt-0.9.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:928bd06eca2c2bbf4349e5b817f837509b0604342e65a502de1d50a7570afd15"},
    {file = "librt-0.9.0-cp314-cp314t-win32.whl", hash = "sha256:a9c63e04d003bc0fb6a03b348018b9a3002f98268200e22cc80f146beac5dc40"},
    {file = "librt-0.9.0-cp314-cp314t-win_amd64.whl", hash = "sha256:f162af66a2ed3f7d1d161a82ca584efd15acd9c1cff190a373458c32f7d42118"},
    {file = "librt-0.9.0-cp314-cp314t-win_arm64.whl", hash = "sha256:a4b25c6c25cac5d0d9d6d6da855195b254e0021e513e0249f0e3b444dc6e0e61"},
    {file = "librt-0.9.0-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:5112c2fb7c2eefefaeaf5c97fec81343ef44ee86a30dcfaa8223822fba6467b4"},
    {file = "librt-0.9.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:a81eea9b999b985e4bacc650c4312805ea7008fd5e45e1bf221310176a7bcb3a"},
    {file = "librt-0.9.0-cp39-cp39-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:eea1b54943475f51698f85fa230c65ccac769f1e603b981be060ac5763d90927"},
    {file = "librt-0.9.0-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:81107843ed1836874b46b310f9b1816abcb89912af627868522461c3b7333c0f"},
    {file = "librt-0.9.0-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:aa95738a68cedd3a6f5492feddc513e2e166b50602958139e47bbdd82da0f5a7"},
    {file = "librt-0.9.0-cp39-cp39-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:6788207daa0c19955d2b668f3294a368d19f67d9b5f274553fd073c1260cbb9f"},
    {file = "librt-0.9.0-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:f48c963a76d71b9d7927eb817b543d0dccd52ab6648b99d37bd54f4cd475d856"},
    {file = "librt-0.9.0-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:42ff8a962554c350d4a83cf47d9b7b78b0e6ff7943e87df7cdfc97c07f3c016f"},
    {file = "librt-0.9.0-cp39-cp39-musllinux_1_2_riscv64.whl", hash = "sha256:657f8ba7b9eaaa82759a104137aed2a3ef7bc46ccfd43e0d89b04005b3e0a4cc"},
    {file = "librt-0.9.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:2d03fa4fd277a7974c1978c92c374c57f44edeee163d147b477b143446ad1bf6"},
    {file = "librt-0.9.0-cp39-cp39-win32.whl", hash = "sha256:d9da80e5b04acce03ced8ba6479a71c2a2edf535c2acc0d09c80d2f80f3bad15"},
    {file = "librt-0.9.0-cp39-cp39-win_amd64.whl", hash = "sha256:54d412e47c21b85865676ed0724e37a89e9593c2eee1e7367adf85bfad56ffb1"},
    {file = "librt-0.9.0.tar.gz", hash = "sha256:a0951822531e7aee6e0dfb556b30d5ee36bbe234faf60c20a16c01be3530869d"},
]

[[package]]
name = "mako"
version = "1.3.12"
description = "A super-fast templating language that borrows the best ideas from the existing templating languages."
optional = false
python-versions = ">=3.8"
groups = ["main"]
files = [
    {file = "mako-1.3.12-py3-none-any.whl", hash = "sha256:8f61569480282dbf557145ce441e4ba888be453c30989f879f0d652e39f53ea9"},
    {file = "mako-1.3.12.tar.gz", hash = "sha256:9f778e93289bd410bb35daadeb4fc66d95a746f0b75777b942088b7fd7af550a"},
]

[package.dependencies]
MarkupSafe = ">=0.9.2"

[package.extras]
babel = ["Babel"]
lingua = ["lingua"]
testing = ["pytest"]

[[package]]
name = "markdown-it-py"
version = "4.0.0"
description = "Python port of markdown-it. Markdown parsing, done right!"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "markdown_it_py-4.0.0-py3-none-any.whl", hash = "sha256:87327c59b172c5011896038353a81343b6754500a08cd7a4973bb48c6d578147"},
    {file = "markdown_it_py-4.0.0.tar.gz", hash = "sha256:cb0a2b4aa34f932c007117b194e945bd74e0ec24133ceb5bac59009cda1cb9f3"},
]

[package.dependencies]
mdurl = ">=0.1,<1.0"

[package.extras]
benchmarking = ["psutil", "pytest", "pytest-benchmark"]
compare = ["commonmark (>=0.9,<1.0)", "markdown (>=3.4,<4.0)", "markdown-it-pyrs", "mistletoe (>=1.0,<2.0)", "mistune (>=3.0,<4.0)", "panflute (>=2.3,<3.0)"]
linkify = ["linkify-it-py (>=1,<3)"]
plugins = ["mdit-py-plugins (>=0.5.0)"]
profiling = ["gprof2dot"]
rtd = ["ipykernel", "jupyter_sphinx", "mdit-py-plugins (>=0.5.0)", "myst-parser", "pyyaml", "sphinx", "sphinx-book-theme (>=1.0,<2.0)", "sphinx-copybutton", "sphinx-design"]
testing = ["coverage", "pytest", "pytest-cov", "pytest-regressions", "requests"]

[[package]]
name = "markupsafe"
version = "3.0.3"
description = "Safely add untrusted strings to HTML/XML markup."
optional = false
python-versions = ">=3.9"
groups = ["main"]
files = [
    {file = "markupsafe-3.0.3-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:2f981d352f04553a7171b8e44369f2af4055f888dfb147d55e42d29e29e74559"},
    {file = "markupsafe-3.0.3-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:e1c1493fb6e50ab01d20a22826e57520f1284df32f2d8601fdd90b6304601419"},
    {file = "markupsafe-3.0.3-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1ba88449deb3de88bd40044603fafffb7bc2b055d626a330323a9ed736661695"},
    {file = "markupsafe-3.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f42d0984e947b8adf7dd6dde396e720934d12c506ce84eea8476409563607591"},
    {file = "markupsafe-3.0.3-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:c0c0b3ade1c0b13b936d7970b1d37a57acde9199dc2aecc4c336773e1d86049c"},
    {file = "markupsafe-3.0.3-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:0303439a41979d9e74d18ff5e2dd8c43ed6c6001fd40e5bf2e43f7bd9bbc523f"},
    {file = "markupsafe-3.0.3-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:d2ee202e79d8ed691ceebae8e0486bd9a2cd4794cec4824e1c99b6f5009502f6"},
    {file = "markupsafe-3.0.3-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:177b5253b2834fe3678cb4a5f0059808258584c559193998be2601324fdeafb1"},
    {file = "markupsafe-3.0.3-cp310-cp310-win32.whl", hash = "sha256:2a15a08b17dd94c53a1da0438822d70ebcd13f8c3a95abe3a9ef9f11a94830aa"},
    {file = "markupsafe-3.0.3-cp310-cp310-win_amd64.whl", hash = "sha256:c4ffb7ebf07cfe8931028e3e4c85f0357459a3f9f9490886198848f4fa002ec8"},
    {file = "markupsafe-3.0.3-cp310-cp310-win_arm64.whl", hash = "sha256:e2103a929dfa2fcaf9bb4e7c091983a49c9ac3b19c9061b6d5427dd7d14d81a1"},
    {file = "markupsafe-3.0.3-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:1cc7ea17a6824959616c525620e387f6dd30fec8cb44f649e31712db02123dad"},
    {file = "markupsafe-3.0.3-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:4bd4cd07944443f5a265608cc6aab442e4f74dff8088b0dfc8238647b8f6ae9a"},
    {file = "markupsafe-3.0.3-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6b5420a1d9450023228968e7e6a9ce57f65d148ab56d2313fcd589eee96a7a50"},
    {file = "markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0bf2a864d67e76e5c9a34dc26ec616a66b9888e25e7b9460e1c76d3293bd9dbf"},
    {file = "markupsafe-3.0.3-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:bc51efed119bc9cfdf792cdeaa4d67e8f6fcccab66ed4bfdd6bde3e59bfcbb2f"},
    {file = "markupsafe-3.0.3-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:068f375c472b3e7acbe2d5318dea141359e6900156b5b2ba06a30b169086b91a"},
    {file = "markupsafe-3.0.3-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:7be7b61bb172e1ed687f1754f8e7484f1c8019780f6f6b0786e76bb01c2ae115"},
    {file = "markupsafe-3.0.3-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:f9e130248f4462aaa8e2552d547f36ddadbeaa573879158d721bbd33dfe4743a"},
    {file = "markupsafe-3.0.3-cp311-cp311-win32.whl", hash = "sha256:0db14f5dafddbb6d9208827849fad01f1a2609380add406671a26386cdf15a19"},
    {file = "markupsafe-3.0.3-cp311-cp311-win_amd64.whl", hash = "sha256:de8a88e63464af587c950061a5e6a67d3632e36df62b986892331d4620a35c01"},
    {file = "markupsafe-3.0.3-cp311-cp311-win_arm64.whl", hash = "sha256:3b562dd9e9ea93f13d53989d23a7e775fdfd1066c33494ff43f5418bc8c58a5c"},
    {file = "markupsafe-3.0.3-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:d53197da72cc091b024dd97249dfc7794d6a56530370992a5e1a08983ad9230e"},
    {file = "markupsafe-3.0.3-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:1872df69a4de6aead3491198eaf13810b565bdbeec3ae2dc8780f14458ec73ce"},
    {file = "markupsafe-3.0.3-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:3a7e8ae81ae39e62a41ec302f972ba6ae23a5c5396c8e60113e9066ef893da0d"},
    {file = "markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d6dd0be5b5b189d31db7cda48b91d7e0a9795f31430b7f271219ab30f1d3ac9d"},
    {file = "markupsafe-3.0.3-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:94c6f0bb423f739146aec64595853541634bde58b2135f27f61c1ffd1cd4d16a"},
    {file = "markupsafe-3.0.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:be8813b57049a7dc738189df53d69395eba14fb99345e0a5994914a3864c8a4b"},
    {file = "markupsafe-3.0.3-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:83891d0e9fb81a825d9a6d61e3f07550ca70a076484292a70fde82c4b807286f"},
    {file = "markupsafe-3.0.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:77f0643abe7495da77fb436f50f8dab76dbc6e5fd25d39589a0f1fe6548bfa2b"},
    {file = "markupsafe-3.0.3-cp312-cp312-win32.whl", hash = "sha256:d88b440e37a16e651bda4c7c2b930eb586fd15ca7406cb39e211fcff3bf3017d"},
    {file = "markupsafe-3.0.3-cp312-cp312-win_amd64.whl", hash = "sha256:26a5784ded40c9e318cfc2bdb30fe164bdb8665ded9cd64d500a34fb42067b1c"},
    {file = "markupsafe-3.0.3-cp312-cp312-win_arm64.whl", hash = "sha256:35add3b638a5d900e807944a078b51922212fb3dedb01633a8defc4b01a3c85f"},
    {file = "markupsafe-3.0.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:e1cf1972137e83c5d4c136c43ced9ac51d0e124706ee1c8aa8532c1287fa8795"},
    {file = "markupsafe-3.0.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:116bb52f642a37c115f517494ea5feb03889e04df47eeff5b130b1808ce7c219"},
    {file = "markupsafe-3.0.3-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:133a43e73a802c5562be9bbcd03d090aa5a1fe899db609c29e8c8d815c5f6de6"},
    {file = "markupsafe-3.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:ccfcd093f13f0f0b7fdd0f198b90053bf7b2f02a3927a30e63f3ccc9df56b676"},
    {file = "markupsafe-3.0.3-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:509fa21c6deb7a7a273d629cf5ec029bc209d1a51178615ddf718f5918992ab9"},
    {file = "markupsafe-3.0.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:a4afe79fb3de0b7097d81da19090f4df4f8d3a2b3adaa8764138aac2e44f3af1"},
    {file = "markupsafe-3.0.3-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:795e7751525cae078558e679d646ae45574b47ed6e7771863fcc079a6171a0fc"},
    {file = "markupsafe-3.0.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:8485f406a96febb5140bfeca44a73e3ce5116b2501ac54fe953e488fb1d03b12"},
    {file = "markupsafe-3.0.3-cp313-cp313-win32.whl", hash = "sha256:bdd37121970bfd8be76c5fb069c7751683bdf373db1ed6c010162b2a130248ed"},
    {file = "markupsafe-3.0.3-cp313-cp313-win_amd64.whl", hash = "sha256:9a1abfdc021a164803f4d485104931fb8f8c1efd55bc6b748d2f5774e78b62c5"},
    {file = "markupsafe-3.0.3-cp313-cp313-win_arm64.whl", hash = "sha256:7e68f88e5b8799aa49c85cd116c932a1ac15caaa3f5db09087854d218359e485"},
    {file = "markupsafe-3.0.3-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:218551f6df4868a8d527e3062d0fb968682fe92054e89978594c28e642c43a73"},
    {file = "markupsafe-3.0.3-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:3524b778fe5cfb3452a09d31e7b5adefeea8c5be1d43c4f810ba09f2ceb29d37"},
    {file = "markupsafe-3.0.3-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:4e885a3d1efa2eadc93c894a21770e4bc67899e3543680313b09f139e149ab19"},
    {file = "markupsafe-3.0.3-cp313-cp313t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:8709b08f4a89aa7586de0aadc8da56180242ee0ada3999749b183aa23df95025"},
    {file = "markupsafe-3.0.3-cp313-cp313t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:b8512a91625c9b3da6f127803b166b629725e68af71f8184ae7e7d54686a56d6"},
    {file = "markupsafe-3.0.3-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:9b79b7a16f7fedff2495d684f2b59b0457c3b493778c9eed31111be64d58279f"},
    {file = "markupsafe-3.0.3-cp313-cp313t-musllinux_1_2_riscv64.whl", hash = "sha256:12c63dfb4a98206f045aa9563db46507995f7ef6d83b2f68eda65c307c6829eb"},
    {file = "markupsafe-3.0.3-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:8f71bc33915be5186016f675cd83a1e08523649b0e33efdb898db577ef5bb009"},
    {file = "markupsafe-3.0.3-cp313-cp313t-win32.whl", hash = "sha256:69c0b73548bc525c8cb9a251cddf1931d1db4d2258e9599c28c07ef3580ef354"},
    {file = "markupsafe-3.0.3-cp313-cp313t-win_amd64.whl", hash = "sha256:1b4b79e8ebf6b55351f0d91fe80f893b4743f104bff22e90697db1590e47a218"},
    {file = "markupsafe-3.0.3-cp313-cp313t-win_arm64.whl", hash = "sha256:ad2cf8aa28b8c020ab2fc8287b0f823d0a7d8630784c31e9ee5edea20f406287"},
    {file = "markupsafe-3.0.3-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:eaa9599de571d72e2daf60164784109f19978b327a3910d3e9de8c97b5b70cfe"},
    {file = "markupsafe-3.0.3-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:c47a551199eb8eb2121d4f0f15ae0f923d31350ab9280078d1e5f12b249e0026"},
    {file = "markupsafe-3.0.3-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f34c41761022dd093b4b6896d4810782ffbabe30f2d443ff5f083e0cbbb8c737"},
    {file = "markupsafe-3.0.3-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:457a69a9577064c05a97c41f4e65148652db078a3a509039e64d3467b9e7ef97"},
    {file = "markupsafe-3.0.3-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:e8afc3f2ccfa24215f8cb28dcf43f0113ac3c37c2f0f0806d8c70e4228c5cf4d"},
    {file = "markupsafe-3.0.3-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:ec15a59cf5af7be74194f7ab02d0f59a62bdcf1a537677ce67a2537c9b87fcda"},
    {file = "markupsafe-3.0.3-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:0eb9ff8191e8498cca014656ae6b8d61f39da5f95b488805da4bb029cccbfbaf"},
    {file = "markupsafe-3.0.3-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:2713baf880df847f2bece4230d4d094280f4e67b1e813eec43b4c0e144a34ffe"},
    {file = "markupsafe-3.0.3-cp314-cp314-win32.whl", hash = "sha256:729586769a26dbceff69f7a7dbbf59ab6572b99d94576a5592625d5b411576b9"},
    {file = "markupsafe-3.0.3-cp314-cp314-win_amd64.whl", hash = "sha256:bdc919ead48f234740ad807933cdf545180bfbe9342c2bb451556db2ed958581"},
    {file = "markupsafe-3.0.3-cp314-cp314-win_arm64.whl", hash = "sha256:5a7d5dc5140555cf21a6fefbdbf8723f06fcd2f63ef108f2854de715e4422cb4"},
    {file = "markupsafe-3.0.3-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:1353ef0c1b138e1907ae78e2f6c63ff67501122006b0f9abad68fda5f4ffc6ab"},
    {file = "markupsafe-3.0.3-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:1085e7fbddd3be5f89cc898938f42c0b3c711fdcb37d75221de2666af647c175"},
    {file = "markupsafe-3.0.3-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1b52b4fb9df4eb9ae465f8d0c228a00624de2334f216f178a995ccdcf82c4634"},
    {file = "markupsafe-3.0.3-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:fed51ac40f757d41b7c48425901843666a6677e3e8eb0abcff09e4ba6e664f50"},
    {file = "markupsafe-3.0.3-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:f190daf01f13c72eac4efd5c430a8de82489d9cff23c364c3ea822545032993e"},
    {file = "markupsafe-3.0.3-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:e56b7d45a839a697b5eb268c82a71bd8c7f6c94d6fd50c3d577fa39a9f1409f5"},
    {file = "markupsafe-3.0.3-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:f3e98bb3798ead92273dc0e5fd0f31ade220f59a266ffd8a4f6065e0a3ce0523"},
    {file = "markupsafe-3.0.3-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:5678211cb9333a6468fb8d8be0305520aa073f50d17f089b5b4b477ea6e67fdc"},
    {file = "markupsafe-3.0.3-cp314-cp314t-win32.whl", hash = "sha256:915c04ba3851909ce68ccc2b8e2cd691618c4dc4c4232fb7982bca3f41fd8c3d"},
    {file = "markupsafe-3.0.3-cp314-cp314t-win_amd64.whl", hash = "sha256:4faffd047e07c38848ce017e8725090413cd80cbc23d86e55c587bf979e579c9"},
    {file = "markupsafe-3.0.3-cp314-cp314t-win_arm64.whl", hash = "sha256:32001d6a8fc98c8cb5c947787c5d08b0a50663d139f1305bac5885d98d9b40fa"},
    {file = "markupsafe-3.0.3-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:15d939a21d546304880945ca1ecb8a039db6b4dc49b2c5a400387cdae6a62e26"},
    {file = "markupsafe-3.0.3-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:f71a396b3bf33ecaa1626c255855702aca4d3d9fea5e051b41ac59a9c1c41edc"},
    {file = "markupsafe-3.0.3-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0f4b68347f8c5eab4a13419215bdfd7f8c9b19f2b25520968adfad23eb0ce60c"},
    {file = "markupsafe-3.0.3-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e8fc20152abba6b83724d7ff268c249fa196d8259ff481f3b1476383f8f24e42"},
    {file = "markupsafe-3.0.3-cp39-cp39-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:949b8d66bc381ee8b007cd945914c721d9aba8e27f71959d750a46f7c282b20b"},
    {file = "markupsafe-3.0.3-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:3537e01efc9d4dccdf77221fb1cb3b8e1a38d5428920e0657ce299b20324d758"},
    {file = "markupsafe-3.0.3-cp39-cp39-musllinux_1_2_riscv64.whl", hash = "sha256:591ae9f2a647529ca990bc681daebdd52c8791ff06c2bfa05b65163e28102ef2"},
    {file = "markupsafe-3.0.3-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:a320721ab5a1aba0a233739394eb907f8c8da5c98c9181d1161e77a0c8e36f2d"},
    {file = "markupsafe-3.0.3-cp39-cp39-win32.whl", hash = "sha256:df2449253ef108a379b8b5d6b43f4b1a8e81a061d6537becd5582fba5f9196d7"},
    {file = "markupsafe-3.0.3-cp39-cp39-win_amd64.whl", hash = "sha256:7c3fb7d25180895632e5d3148dbdc29ea38ccb7fd210aa27acbd1201a1902c6e"},
    {file = "markupsafe-3.0.3-cp39-cp39-win_arm64.whl", hash = "sha256:38664109c14ffc9e7437e86b4dceb442b0096dfe3541d7864d9cbe1da4cf36c8"},
    {file = "markupsafe-3.0.3.tar.gz", hash = "sha256:722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698"},
]

[[package]]
name = "mccabe"
version = "0.7.0"
description = "McCabe checker, plugin for flake8"
optional = false
python-versions = ">=3.6"
groups = ["dev"]
files = [
    {file = "mccabe-0.7.0-py2.py3-none-any.whl", hash = "sha256:6c2d30ab6be0e4a46919781807b4f0d834ebdd6c6e3dca0bda5a15f863427b6e"},
    {file = "mccabe-0.7.0.tar.gz", hash = "sha256:348e0240c33b60bbdf4e523192ef919f28cb2c3d7d5c7794f74009290f236325"},
]

[[package]]
name = "mdurl"
version = "0.1.2"
description = "Markdown URL utilities"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "mdurl-0.1.2-py3-none-any.whl", hash = "sha256:84008a41e51615a49fc9966191ff91509e3c40b939176e643fd50a5c2196b8f8"},
    {file = "mdurl-0.1.2.tar.gz", hash = "sha256:bb413d29f5eea38f31dd4754dd7377d4465116fb207585f97bf925588687c1ba"},
]

[[package]]
name = "mypy"
version = "1.20.2"
description = "Optional static typing for Python"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "mypy-1.20.2-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:cf5a4db6dca263010e2c7bff081c89383c72d187ba2cf4c44759aac970e2f0c4"},
    {file = "mypy-1.20.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:7b0e817b518bff7facd7f85ea05b643ad8bdcce684cf29784987b0a7c8e1f997"},
    {file = "mypy-1.20.2-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:97d7b9a485b40f8ca425460e89bf1da2814625b2da627c0dcc6aa46c92631d14"},
    {file = "mypy-1.20.2-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1e1c12f6d2db3d78b909b5f77513c11eb7f2dd2782b96a3ab6dffc7d44575c99"},
    {file = "mypy-1.20.2-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:89dce27e142d25ffbc154c1819383b69f2e9234dc4ed4766f42e0e8cb264ab5c"},
    {file = "mypy-1.20.2-cp310-cp310-win_amd64.whl", hash = "sha256:f376e37f9bf2a946872fc5fd1199c99310748e3c26c7a26683f13f8bdb756cbd"},
    {file = "mypy-1.20.2-cp310-cp310-win_arm64.whl", hash = "sha256:6e2b469efd811707bc530fd1effef0f5d6eebcb7fe376affae69025da4b979a2"},
    {file = "mypy-1.20.2-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:4077797a273e56e8843d001e9dfe4ba10e33323d6ade647ff260e5cd97d9758c"},
    {file = "mypy-1.20.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:cdecf62abcc4292500d7858aeae87a1f8f1150f4c4dd08fb0b336ee79b2a6df3"},
    {file = "mypy-1.20.2-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c566c3a88b6ece59b3d70f65bedef17304f48eb52ff040a6a18214e1917b3254"},
    {file = "mypy-1.20.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0deb80d062b2479f2c87ae568f89845afc71d11bc41b04179e58165fd9f31e98"},
    {file = "mypy-1.20.2-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:bba9ad231e92a3e424b3e56b65aa17704993425bba97e302c832f9466bb85bac"},
    {file = "mypy-1.20.2-cp311-cp311-win_amd64.whl", hash = "sha256:baf593f2765fa3a6b1ef95807dbaa3d25b594f6a52adcc506a6b9cb115e1be67"},
    {file = "mypy-1.20.2-cp311-cp311-win_arm64.whl", hash = "sha256:20175a1c0f49863946ec20b7f63255768058ac4f07d2b9ded6a6b46cfb5a9100"},
    {file = "mypy-1.20.2-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:4dbfcf869f6b0517f70cf0030ba6ea1d6645e132337a7d5204a18d8d5636c02b"},
    {file = "mypy-1.20.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:4b6481b228d072315b053210b01ac320e1be243dc17f9e5887ef167f23f5fae4"},
    {file = "mypy-1.20.2-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:34397cdced6b90b836e38182076049fdb41424322e0b0728c946b0939ebdf9f6"},
    {file = "mypy-1.20.2-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a5da6976f20cae27059ea8d0c86e7cef3de720e04c4bb9ee18e3690fdb792066"},
    {file = "mypy-1.20.2-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:56908d7e08318d39f85b1f0c6cfd47b0cac1a130da677630dac0de3e0623e102"},
    {file = "mypy-1.20.2-cp312-cp312-win_amd64.whl", hash = "sha256:d52ad8d78522da1d308789df651ee5379088e77c76cb1994858d40a426b343b9"},
    {file = "mypy-1.20.2-cp312-cp312-win_arm64.whl", hash = "sha256:785b08db19c9f214dc37d65f7c165d19a30fcecb48abfa30f31b01b5acaabb58"},
    {file = "mypy-1.20.2-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:edfbfca868cdd6bd8d974a60f8a3682f5565d3f5c99b327640cedd24c4264026"},
    {file = "mypy-1.20.2-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:e2877a02380adfcdbc69071a0f74d6e9dbbf593c0dc9d174e1f223ffd5281943"},
    {file = "mypy-1.20.2-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7488448de6007cd5177c6cea0517ac33b4c0f5ee9b5e9f2be51ce75511a85517"},
    {file = "mypy-1.20.2-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:bb9c2fa06887e21d6a3a868762acb82aec34e2c6fd0174064f27c93ede68ad15"},
    {file = "mypy-1.20.2-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:9d56a78b646f2e3daa865bc70cd5ec5a46c50045801ca8ff17a0c43abc97e3ee"},
    {file = "mypy-1.20.2-cp313-cp313-win_amd64.whl", hash = "sha256:2a4102b03bb7481d9a91a6da8d174740c9c8c4401024684b9ca3b7cc5e49852f"},
    {file = "mypy-1.20.2-cp313-cp313-win_arm64.whl", hash = "sha256:a95a9248b0c6fd933a442c03c3b113c3b61320086b88e2c444676d3fd1ca3330"},
    {file = "mypy-1.20.2-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:419413398fe250aae057fd2fe50166b61077083c9b82754c341cf4fd73038f30"},
    {file = "mypy-1.20.2-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:e73c07f23009962885c197ccb9b41356a30cc0e5a1d0c2ea8fd8fb1362d7f924"},
    {file = "mypy-1.20.2-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0c64e5973df366b747646fc98da921f9d6eba9716d57d1db94a83c026a08e0fb"},
    {file = "mypy-1.20.2-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5a65aa591af023864fd08a97da9974e919452cfe19cb146c8a5dc692626445dc"},
    {file = "mypy-1.20.2-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:4fef51b01e638974a6e69885687e9bd40c8d1e09a6cd291cca0619625cf1f558"},
    {file = "mypy-1.20.2-cp314-cp314-win_amd64.whl", hash = "sha256:913485a03f1bcf5d279409a9d2b9ed565c151f61c09f29991e5faa14033da4c8"},
    {file = "mypy-1.20.2-cp314-cp314-win_arm64.whl", hash = "sha256:c3bae4f855d965b5453784300c12ffc63a548304ac7f99e55d4dc7c898673aa3"},
    {file = "mypy-1.20.2-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:2de3dcea53babc1c3237a19002bc3d228ce1833278f093b8d619e06e7cc79609"},
    {file = "mypy-1.20.2-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:52b176444e2e5054dfcbcb8c75b0b719865c96247b37407184bbfca5c353f2c2"},
    {file = "mypy-1.20.2-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:688c3312e5dadb573a2c69c82af3a298d43ecf9e6d264e0f95df960b5f6ac19c"},
    {file = "mypy-1.20.2-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:29752dbbf8cc53f89f6ac096d363314333045c257c9c75cbd189ca2de0455744"},
    {file = "mypy-1.20.2-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:803203d2b6ea644982c644895c2f78b28d0e208bba7b27d9b921e0ec5eb207c6"},
    {file = "mypy-1.20.2-cp314-cp314t-win_amd64.whl", hash = "sha256:9bcb8aa397ff0093c824182fd76a935a9ba7ad097fcbef80ae89bf6c1731d8ec"},
    {file = "mypy-1.20.2-cp314-cp314t-win_arm64.whl", hash = "sha256:e061b58443f1736f8a37c48978d7ab581636d6ab03e3d4f99e3fa90463bb9382"},
    {file = "mypy-1.20.2-py3-none-any.whl", hash = "sha256:a94c5a76ab46c5e6257c7972b6c8cff0574201ca7dc05647e33e795d78680563"},
    {file = "mypy-1.20.2.tar.gz", hash = "sha256:e8222c26daaafd9e8626dec58ae36029f82585890589576f769a650dd20fd665"},
]

[package.dependencies]
librt = {version = ">=0.8.0", markers = "platform_python_implementation != \"PyPy\""}
mypy_extensions = ">=1.0.0"
pathspec = ">=1.0.0"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}
typing_extensions = [
    {version = ">=4.6.0", markers = "python_version < \"3.15\""},
    {version = ">=4.14.0", markers = "python_version >= \"3.15\""},
]

[package.extras]
dmypy = ["psutil (>=4.0)"]
faster-cache = ["orjson"]
install-types = ["pip"]
mypyc = ["setuptools (>=50)"]
native-parser = ["ast-serialize (>=0.1.1,<1.0.0)"]
reports = ["lxml"]

[[package]]
name = "mypy-extensions"
version = "1.1.0"
description = "Type system extensions for programs checked with the mypy type checker."
optional = false
python-versions = ">=3.8"
groups = ["main", "dev"]
files = [
    {file = "mypy_extensions-1.1.0-py3-none-any.whl", hash = "sha256:1be4cccdb0f2482337c4743e60421de3a356cd97508abadd57d47403e94f5505"},
    {file = "mypy_extensions-1.1.0.tar.gz", hash = "sha256:52e68efc3284861e772bbcd66823fde5ae21fd2fdb51c62a211403730b916558"},
]

[[package]]
name = "mypy-protobuf"
version = "3.6.0"
description = "Generate mypy stub files from protobuf specs"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
markers = "python_version < \"3.14\""
files = [
    {file = "mypy-protobuf-3.6.0.tar.gz", hash = "sha256:02f242eb3409f66889f2b1a3aa58356ec4d909cdd0f93115622e9e70366eca3c"},
    {file = "mypy_protobuf-3.6.0-py3-none-any.whl", hash = "sha256:56176e4d569070e7350ea620262478b49b7efceba4103d468448f1d21492fd6c"},
]

[package.dependencies]
protobuf = ">=4.25.3"
types-protobuf = ">=4.24"

[[package]]
name = "mypy-protobuf"
version = "5.0.0"
description = "Generate mypy stub files from protobuf specs"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
markers = "python_version >= \"3.14\""
files = [
    {file = "mypy_protobuf-5.0.0-py3-none-any.whl", hash = "sha256:3a7dd753ef3e3b8783a824eb51f07983f62812f9ec066e4fbb1b22d6c5dc36d0"},
    {file = "mypy_protobuf-5.0.0.tar.gz", hash = "sha256:6fdd1cfdbb4419c713291d800a332d4bba6510dbd1341ed95e0bcc82fcadb6b5"},
]

[package.dependencies]
protobuf = ">=4.25.3"
types-protobuf = ">=4.24"

[[package]]
name = "ni-grpc-extensions"
version = "1.1.0"
description = "gRPC Extensions"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_grpc_extensions-1.1.0-py3-none-any.whl", hash = "sha256:db0357acd244854f4acccf202c89fe6462b4283d264ed639f4e248e6cc86bc9b"},
    {file = "ni_grpc_extensions-1.1.0.tar.gz", hash = "sha256:028ea33e5c5234bc050bf5dc99f5b61611531de8f012293e9d4c6985b7b37afb"},
]

[package.dependencies]
grpcio = ">=1.49.0,<2.0"
traceloggingdynamic = {version = ">=1.0", markers = "sys_platform == \"win32\""}

[[package]]
name = "ni-grpcdevice-v1-proto"
version = "1.1.0"
description = "Protobuf generated code for the nidevice_grpc gRPC API"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_grpcdevice_v1_proto-1.1.0-py3-none-any.whl", hash = "sha256:2784c4b3e64a9c1e6b743d26847b7a44bf781ab46a9e19b02b379c1e0bc6dcfb"},
    {file = "ni_grpcdevice_v1_proto-1.1.0.tar.gz", hash = "sha256:ad14ab44e456a67d50a8fc38329e01dccae1732eab22a529c96eb3d5cb46370c"},
]

[package.dependencies]
grpcio = ">=1.49.0,<2.0"
protobuf = ">=4.21"

[[package]]
name = "ni-measurement-plugin-sdk-service"
version = "3.2.0.dev0"
description = "Measurement Plug-In Support for Python"
optional = false
python-versions = "^3.10"
groups = ["main", "dev"]
files = []
develop = true

[package.dependencies]
deprecation = ">=2.1"
grpcio = "^1.49.1"
ni-grpc-extensions = "^1.0.0"
ni-measurementlink-discovery-v1-client = "^1.0.0"
ni-measurementlink-measurement-v1-proto = "^1.0.0"
ni-measurementlink-measurement-v2-proto = "^1.0.0"
ni-measurementlink-pinmap-v1-client = "^1.0.0"
ni-measurementlink-sessionmanagement-v1-client = "^1.0.0"
ni-protobuf-types = "^1.0.0"
protobuf = ">=4.21"
python-decouple = ">=3.8"
pywin32 = {version = ">=303", markers = "sys_platform == \"win32\""}

[package.extras]
drivers = ["nidaqmx[grpc] (>=0.8.0)", "nidcpower[grpc] (>=1.4.4)", "nidigital[grpc] (>=1.4.4)", "nidmm[grpc] (>=1.4.4)", "nifgen[grpc] (>=1.4.4)", "niscope[grpc] (>=1.4.4)", "niswitch[grpc] (>=1.4.4)"]
nidaqmx = ["nidaqmx[grpc] (>=0.8.0)"]
nidcpower = ["nidcpower[grpc] (>=1.4.4)"]
nidigital = ["nidigital[grpc] (>=1.4.4)"]
nidmm = ["nidmm[grpc] (>=1.4.4)"]
nifgen = ["nifgen[grpc] (>=1.4.4)"]
niscope = ["niscope[grpc] (>=1.4.4)"]
niswitch = ["niswitch[grpc] (>=1.4.4)"]

[package.source]
type = "directory"
url = "../service"

[[package]]
name = "ni-measurementlink-discovery-v1-client"
version = "1.1.0"
description = "gRPC Client for NI Discovery Service"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_measurementlink_discovery_v1_client-1.1.0-py3-none-any.whl", hash = "sha256:366dcc3b93627ed1ede488955637e0768b29cb7a375e59ac1020f4c53892d00c"},
    {file = "ni_measurementlink_discovery_v1_client-1.1.0.tar.gz", hash = "sha256:831b6145cf8def0021cb00579b08a2ad1da5a19fdeedea4522a3cb4a30978c48"},
]

[package.dependencies]
grpcio = ">=1.49.0,<2.0"
ni-grpc-extensions = ">=1.1.0"
ni-measurementlink-discovery-v1-proto = ">=1.1.0"
pywin32 = {version = ">=303", markers = "sys_platform == \"win32\""}

[[package]]
name = "ni-measurementlink-discovery-v1-proto"
version = "1.1.0"
description = "Protobuf data types for NI discovery gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_measurementlink_discovery_v1_proto-1.1.0-py3-none-any.whl", hash = "sha256:6a3061ca858d3ee887987dc5130074fc439ce6c2b26fe6b3f9401da023461d43"},
    {file = "ni_measurementlink_discovery_v1_proto-1.1.0.tar.gz", hash = "sha256:f9a9b4572ac5d169fad21ab56e2639abdb77979cf0dc3a88cdb71b2c783d009c"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-measurementlink-measurement-v1-proto"
version = "1.1.1"
description = "Protobuf data types for NI measurement gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_measurementlink_measurement_v1_proto-1.1.1-py3-none-any.whl", hash = "sha256:cb0e1e26f8d08829de46f5707061aacbbb6e42248811bac7eababbdd524f0196"},
    {file = "ni_measurementlink_measurement_v1_proto-1.1.1.tar.gz", hash = "sha256:81b1d321d78b2f15e2cbd41316314f39a9446866928f29a69ed501bd911be6f7"},
]

[package.dependencies]
ni-measurementlink-proto = ">=1.1.0"
protobuf = ">=4.21"

[[package]]
name = "ni-measurementlink-measurement-v2-proto"
version = "1.1.1"
description = "Protobuf data types for NI measurement gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_measurementlink_measurement_v2_proto-1.1.1-py3-none-any.whl", hash = "sha256:2776adb4402f58ad6fc23436349989eb92b74a718dcbb084aab65fcce3b43b51"},
    {file = "ni_measurementlink_measurement_v2_proto-1.1.1.tar.gz", hash = "sha256:de236b4b02a03730be6d94b362edba01c1b11fb803436bd2a65fdb7bc95bf605"},
]

[package.dependencies]
ni-measurementlink-proto = ">=1.0.0"
protobuf = ">=4.21"

[[package]]
name = "ni-measurementlink-pinmap-v1-client"
version = "1.1.0"
description = "gRPC Client for NI Pin Map Service"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_measurementlink_pinmap_v1_client-1.1.0-py3-none-any.whl", hash = "sha256:2d758aa15addd78fde63e57a69e4c4cbb25e1689c4ce2e5d7b456c22c1b3607e"},
    {file = "ni_measurementlink_pinmap_v1_client-1.1.0.tar.gz", hash = "sha256:ae5b406781544071ea46a5afb862daeb29e989ce67beb80972f88fb80135bc4f"},
]

[package.dependencies]
grpcio = ">=1.49.0,<2.0"
ni-grpc-extensions = ">=1.1.0"
ni-measurementlink-discovery-v1-client = ">=1.1.0"
ni-measurementlink-measurement-v1-proto = ">=1.1.1"
ni-measurementlink-measurement-v2-proto = ">=1.1.1"
ni-measurementlink-pinmap-v1-proto = ">=1.1.0"
ni-measurementlink-sessionmanagement-v1-client = ">=1.1.0"

[[package]]
name = "ni-measurementlink-pinmap-v1-proto"
version = "1.1.0"
description = "Protobuf data types for NI pinmap gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_measurementlink_pinmap_v1_proto-1.1.0-py3-none-any.whl", hash = "sha256:c2334d2ffe4e11f776b0087ad25184b504faa63fa57ec3c7eb87e1a3234dd686"},
    {file = "ni_measurementlink_pinmap_v1_proto-1.1.0.tar.gz", hash = "sha256:db6cef7969c6423349e6560850983008a269a3de0ca7dd623795d7153ede64c1"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-measurementlink-proto"
version = "1.1.0"
description = "Protobuf data types for NI gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_measurementlink_proto-1.1.0-py3-none-any.whl", hash = "sha256:b7fb6c7b6c36a80d0a1e67fd47d2fa6cccfed993dd5047aa720b04f07c5a546e"},
    {file = "ni_measurementlink_proto-1.1.0.tar.gz", hash = "sha256:4fca44af39715f8501d711944f4d6bae11f1b9ffa059a6995eb69770872c3fa5"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-measurementlink-sessionmanagement-v1-client"
version = "1.1.0"
description = "Client gRPC APIs for the session management service"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_measurementlink_sessionmanagement_v1_client-1.1.0-py3-none-any.whl", hash = "sha256:90ddf2561f82c8b32d9e86908326c8e50c388f6e74c1ea2bac758f4e10553a3f"},
    {file = "ni_measurementlink_sessionmanagement_v1_client-1.1.0.tar.gz", hash = "sha256:53348004828452fe0de3cae89e0aed4952a120254beb346b8764428373116038"},
]

[package.dependencies]
deprecation = ">=2.1"
ni-grpc-extensions = ">=1.1.0"
ni-grpcdevice-v1-proto = ">=1.1.0"
ni-measurementlink-discovery-v1-client = ">=1.1.0"
ni-measurementlink-pinmap-v1-proto = ">=1.1.0"
ni-measurementlink-proto = ">=1.1.0"
ni-measurementlink-sessionmanagement-v1-proto = ">=1.1.0"
protobuf = ">=4.21"
python-decouple = ">=3.8"
pywin32 = {version = ">=303", markers = "sys_platform == \"win32\""}
traceloggingdynamic = {version = ">=1.0", markers = "sys_platform == \"win32\""}

[package.extras]
drivers = ["nidaqmx[grpc] (>=0.8.0)", "nidcpower[grpc] (>=1.4.4)", "nidigital[grpc] (>=1.4.4)", "nidmm[grpc] (>=1.4.4)", "nifgen[grpc] (>=1.4.4)", "niscope[grpc] (>=1.4.4)", "niswitch[grpc] (>=1.4.4)"]
nidaqmx = ["nidaqmx[grpc] (>=0.8.0)"]
nidcpower = ["nidcpower[grpc] (>=1.4.4)"]
nidigital = ["nidigital[grpc] (>=1.4.4)"]
nidmm = ["nidmm[grpc] (>=1.4.4)"]
nifgen = ["nifgen[grpc] (>=1.4.4)"]
niscope = ["niscope[grpc] (>=1.4.4)"]
niswitch = ["niswitch[grpc] (>=1.4.4)"]

[[package]]
name = "ni-measurementlink-sessionmanagement-v1-proto"
version = "1.1.0"
description = "Protobuf data types for NI session management gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_measurementlink_sessionmanagement_v1_proto-1.1.0-py3-none-any.whl", hash = "sha256:e88d8beaf141e85f83daba1858a8b372df9d2c2671b3c4b0bb3b50e745e14585"},
    {file = "ni_measurementlink_sessionmanagement_v1_proto-1.1.0.tar.gz", hash = "sha256:cedc461b7990bc496ac87a932ca32f7b9f6f1c73c8eb5bda71f5e60709ef76e1"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-protobuf-types"
version = "1.2.0"
description = "Protobuf data types for NI gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_protobuf_types-1.2.0-py3-none-any.whl", hash = "sha256:461c4825571d0054fd5427664403c3d69fcd180c9c00868ac1911693dd9bf901"},
    {file = "ni_protobuf_types-1.2.0.tar.gz", hash = "sha256:e8226f8ef44b104ffb1b1f6e416511c416be4d91bf5c2633db7ab58294e037bb"},
]

[package.dependencies]
nitypes = ">=1.1.0"
protobuf = ">=4.21"

[[package]]
name = "ni-python-styleguide"
version = "0.5.0"
description = "NI's internal and external Python linter rules and plugins"
optional = false
python-versions = "<4.0,>=3.9"
groups = ["dev"]
files = [
    {file = "ni_python_styleguide-0.5.0-py3-none-any.whl", hash = "sha256:66784d97bc2898552386ca8e0667a11fa5f712820130585df7709d08836f6bc0"},
    {file = "ni_python_styleguide-0.5.0.tar.gz", hash = "sha256:66bd05f7d9fc98a87e5e85319faa752efd54549c979938ed1bb64e2d1f412630"},
]

[package.dependencies]
better-diff = ">=0.1.3,<0.2.0"
black = ">=23.1,<26.0"
click = ">=7.1.2"
flake8 = [
    {version = ">=6.1,<7.0", markers = "python_version >= \"3.12\" and python_version < \"4.0\""},
    {version = ">=5.0,<6.0", markers = "python_version >= \"3.8\" and python_version < \"3.12\""},
]
flake8-black = ">=0.2.1"
flake8-docstrings = ">=1.5.0"
flake8-import-order = ">=0.18.1,<0.19.0"
flake8-tidy-imports = ">=4.11.0"
isort = ">=5.10"
pathspec = ">=0.11.1"
pep8-naming = ">=0.11.1"
pycodestyle = [
    {version = ">=2.11,<3.0", markers = "python_version >= \"3.12\" and python_version < \"4.0\""},
    {version = ">=2.9,<3.0", markers = "python_version >= \"3.8\" and python_version < \"3.12\""},
]
setuptools = "<82"
toml = ">=0.10.1"

[[package]]
name = "nitypes"
version = "1.1.0"
description = "Data types for NI Python APIs"
optional = false
python-versions = "<4.0,>=3.9"
groups = ["main", "dev"]
files = [
    {file = "nitypes-1.1.0-py3-none-any.whl", hash = "sha256:b43ac7027e1cceeca7ceffa58f31ffadd03feeb1788ca5cb8f9d105e73893b14"},
    {file = "nitypes-1.1.0.tar.gz", hash = "sha256:f273b5131ef0d5b848c37a0a63452626caf5c2938f7744c324f7991b76fa0b60"},
]

[package.dependencies]
hightime = ">=0.2.2"
numpy = [
    {version = ">=2.1", markers = "python_version >= \"3.13\" and python_version < \"4.0\""},
    {version = ">=1.22", markers = "python_version >= \"3.9\" and python_version < \"3.13\""},
]
typing-extensions = ">=4.13.2"

[[package]]
name = "numpy"
version = "2.2.6"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.10"
groups = ["main", "dev"]
markers = "python_version < \"3.12\""
files = [
    {file = "numpy-2.2.6-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:b412caa66f72040e6d268491a59f2c43bf03eb6c96dd8f0307829feb7fa2b6fb"},
    {file = "numpy-2.2.6-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:8e41fd67c52b86603a91c1a505ebaef50b3314de0213461c7a6e99c9a3beff90"},
    {file = "numpy-2.2.6-cp310-cp310-macosx_14_0_arm64.whl", hash = "sha256:37e990a01ae6ec7fe7fa1c26c55ecb672dd98b19c3d0e1d1f326fa13cb38d163"},
    {file = "numpy-2.2.6-cp310-cp310-macosx_14_0_x86_64.whl", hash = "sha256:5a6429d4be8ca66d889b7cf70f536a397dc45ba6faeb5f8c5427935d9592e9cf"},
    {file = "numpy-2.2.6-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:efd28d4e9cd7d7a8d39074a4d44c63eda73401580c5c76acda2ce969e0a38e83"},
    {file = "numpy-2.2.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fc7b73d02efb0e18c000e9ad8b83480dfcd5dfd11065997ed4c6747470ae8915"},
    {file = "numpy-2.2.6-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:74d4531beb257d2c3f4b261bfb0fc09e0f9ebb8842d82a7b4209415896adc680"},
    {file = "numpy-2.2.6-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:8fc377d995680230e83241d8a96def29f204b5782f371c532579b4f20607a289"},
    {file = "numpy-2.2.6-cp310-cp310-win32.whl", hash = "sha256:b093dd74e50a8cba3e873868d9e93a85b78e0daf2e98c6797566ad8044e8363d"},
    {file = "numpy-2.2.6-cp310-cp310-win_amd64.whl", hash = "sha256:f0fd6321b839904e15c46e0d257fdd101dd7f530fe03fd6359c1ea63738703f3"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:f9f1adb22318e121c5c69a09142811a201ef17ab257a1e66ca3025065b7f53ae"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:c820a93b0255bc360f53eca31a0e676fd1101f673dda8da93454a12e23fc5f7a"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:3d70692235e759f260c3d837193090014aebdf026dfd167834bcba43e30c2a42"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:481b49095335f8eed42e39e8041327c05b0f6f4780488f61286ed3c01368d491"},
    {file = "numpy-2.2.6-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b64d8d4d17135e00c8e346e0a738deb17e754230d7e0810ac5012750bbd85a5a"},
    {file = "numpy-2.2.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ba10f8411898fc418a521833e014a77d3ca01c15b0c6cdcce6a0d2897e6dbbdf"},
    {file = "numpy-2.2.6-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:bd48227a919f1bafbdda0583705e547892342c26fb127219d60a5c36882609d1"},
    {file = "numpy-2.2.6-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:9551a499bf125c1d4f9e250377c1ee2eddd02e01eac6644c080162c0c51778ab"},
    {file = "numpy-2.2.6-cp311-cp311-win32.whl", hash = "sha256:0678000bb9ac1475cd454c6b8c799206af8107e310843532b04d49649c717a47"},
    {file = "numpy-2.2.6-cp311-cp311-win_amd64.whl", hash = "sha256:e8213002e427c69c45a52bbd94163084025f533a55a59d6f9c5b820774ef3303"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:41c5a21f4a04fa86436124d388f6ed60a9343a6f767fced1a8a71c3fbca038ff"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:de749064336d37e340f640b05f24e9e3dd678c57318c7289d222a8a2f543e90c"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:894b3a42502226a1cac872f840030665f33326fc3dac8e57c607905773cdcde3"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:71594f7c51a18e728451bb50cc60a3ce4e6538822731b2933209a1f3614e9282"},
    {file = "numpy-2.2.6-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f2618db89be1b4e05f7a1a847a9c1c0abd63e63a1607d892dd54668dd92faf87"},
    {file = "numpy-2.2.6-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fd83c01228a688733f1ded5201c678f0c53ecc1006ffbc404db9f7a899ac6249"},
    {file = "numpy-2.2.6-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:37c0ca431f82cd5fa716eca9506aefcabc247fb27ba69c5062a6d3ade8cf8f49"},
    {file = "numpy-2.2.6-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:fe27749d33bb772c80dcd84ae7e8df2adc920ae8297400dabec45f0dedb3f6de"},
    {file = "numpy-2.2.6-cp312-cp312-win32.whl", hash = "sha256:4eeaae00d789f66c7a25ac5f34b71a7035bb474e679f410e5e1a94deb24cf2d4"},
    {file = "numpy-2.2.6-cp312-cp312-win_amd64.whl", hash = "sha256:c1f9540be57940698ed329904db803cf7a402f3fc200bfe599334c9bd84a40b2"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:0811bb762109d9708cca4d0b13c4f67146e3c3b7cf8d34018c722adb2d957c84"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:287cc3162b6f01463ccd86be154f284d0893d2b3ed7292439ea97eafa8170e0b"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:f1372f041402e37e5e633e586f62aa53de2eac8d98cbfb822806ce4bbefcb74d"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:55a4d33fa519660d69614a9fad433be87e5252f4b03850642f88993f7b2ca566"},
    {file = "numpy-2.2.6-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f92729c95468a2f4f15e9bb94c432a9229d0d50de67304399627a943201baa2f"},
    {file = "numpy-2.2.6-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1bc23a79bfabc5d056d106f9befb8d50c31ced2fbc70eedb8155aec74a45798f"},
    {file = "numpy-2.2.6-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:e3143e4451880bed956e706a3220b4e5cf6172ef05fcc397f6f36a550b1dd868"},
    {file = "numpy-2.2.6-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:b4f13750ce79751586ae2eb824ba7e1e8dba64784086c98cdbbcc6a42112ce0d"},
    {file = "numpy-2.2.6-cp313-cp313-win32.whl", hash = "sha256:5beb72339d9d4fa36522fc63802f469b13cdbe4fdab4a288f0c441b74272ebfd"},
    {file = "numpy-2.2.6-cp313-cp313-win_amd64.whl", hash = "sha256:b0544343a702fa80c95ad5d3d608ea3599dd54d4632df855e4c8d24eb6ecfa1c"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:0bca768cd85ae743b2affdc762d617eddf3bcf8724435498a1e80132d04879e6"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:fc0c5673685c508a142ca65209b4e79ed6740a4ed6b2267dbba90f34b0b3cfda"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_14_0_arm64.whl", hash = "sha256:5bd4fc3ac8926b3819797a7c0e2631eb889b4118a9898c84f585a54d475b7e40"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_14_0_x86_64.whl", hash = "sha256:fee4236c876c4e8369388054d02d0e9bb84821feb1a64dd59e137e6511a551f8"},
    {file = "numpy-2.2.6-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e1dda9c7e08dc141e0247a5b8f49cf05984955246a327d4c48bda16821947b2f"},
    {file = "numpy-2.2.6-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f447e6acb680fd307f40d3da4852208af94afdfab89cf850986c3ca00562f4fa"},
    {file = "numpy-2.2.6-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:389d771b1623ec92636b0786bc4ae56abafad4a4c513d36a55dce14bd9ce8571"},
    {file = "numpy-2.2.6-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:8e9ace4a37db23421249ed236fdcdd457d671e25146786dfc96835cd951aa7c1"},
    {file = "numpy-2.2.6-cp313-cp313t-win32.whl", hash = "sha256:038613e9fb8c72b0a41f025a7e4c3f0b7a1b5d768ece4796b674c8f3fe13efff"},
    {file = "numpy-2.2.6-cp313-cp313t-win_amd64.whl", hash = "sha256:6031dd6dfecc0cf9f668681a37648373bddd6421fff6c66ec1624eed0180ee06"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-macosx_10_15_x86_64.whl", hash = "sha256:0b605b275d7bd0c640cad4e5d30fa701a8d59302e127e5f79138ad62762c3e3d"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-macosx_14_0_x86_64.whl", hash = "sha256:7befc596a7dc9da8a337f79802ee8adb30a552a94f792b9c9d18c840055907db"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ce47521a4754c8f4593837384bd3424880629f718d87c5d44f8ed763edd63543"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:d042d24c90c41b54fd506da306759e06e568864df8ec17ccc17e9e884634fd00"},
    {file = "numpy-2.2.6.tar.gz", hash = "sha256:e29554e2bef54a90aa5cc07da6ce955accb83f21ab5de01a62c8478897b264fd"},
]

[[package]]
name = "numpy"
version = "2.4.1"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.11"
groups = ["main", "dev"]
markers = "python_version >= \"3.12\""
files = [
    {file = "numpy-2.4.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:0cce2a669e3c8ba02ee563c7835f92c153cf02edff1ae05e1823f1dde21b16a5"},
    {file = "numpy-2.4.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:899d2c18024984814ac7e83f8f49d8e8180e2fbe1b2e252f2e7f1d06bea92425"},
    {file = "numpy-2.4.1-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:09aa8a87e45b55a1c2c205d42e2808849ece5c484b2aab11fecabec3841cafba"},
    {file = "numpy-2.4.1-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:edee228f76ee2dab4579fad6f51f6a305de09d444280109e0f75df247ff21501"},
    {file = "numpy-2.4.1-cp311-cp311-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:a92f227dbcdc9e4c3e193add1a189a9909947d4f8504c576f4a732fd0b54240a"},
    {file = "numpy-2.4.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:538bf4ec353709c765ff75ae616c34d3c3dca1a68312727e8f2676ea644f8509"},
    {file = "numpy-2.4.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:ac08c63cb7779b85e9d5318e6c3518b424bc1f364ac4cb2c6136f12e5ff2dccc"},
    {file = "numpy-2.4.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:4f9c360ecef085e5841c539a9a12b883dff005fbd7ce46722f5e9cef52634d82"},
    {file = "numpy-2.4.1-cp311-cp311-win32.whl", hash = "sha256:0f118ce6b972080ba0758c6087c3617b5ba243d806268623dc34216d69099ba0"},
    {file = "numpy-2.4.1-cp311-cp311-win_amd64.whl", hash = "sha256:18e14c4d09d55eef39a6ab5b08406e84bc6869c1e34eef45564804f90b7e0574"},
    {file = "numpy-2.4.1-cp311-cp311-win_arm64.whl", hash = "sha256:6461de5113088b399d655d45c3897fa188766415d0f568f175ab071c8873bd73"},
    {file = "numpy-2.4.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:d3703409aac693fa82c0aee023a1ae06a6e9d065dba10f5e8e80f642f1e9d0a2"},
    {file = "numpy-2.4.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:7211b95ca365519d3596a1d8688a95874cc94219d417504d9ecb2df99fa7bfa8"},
    {file = "numpy-2.4.1-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:5adf01965456a664fc727ed69cc71848f28d063217c63e1a0e200a118d5eec9a"},
    {file = "numpy-2.4.1-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:26f0bcd9c79a00e339565b303badc74d3ea2bd6d52191eeca5f95936cad107d0"},
    {file = "numpy-2.4.1-cp312-cp312-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0093e85df2960d7e4049664b26afc58b03236e967fb942354deef3208857a04c"},
    {file = "numpy-2.4.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:7ad270f438cbdd402c364980317fb6b117d9ec5e226fff5b4148dd9aa9fc6e02"},
    {file = "numpy-2.4.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:297c72b1b98100c2e8f873d5d35fb551fce7040ade83d67dd51d38c8d42a2162"},
    {file = "numpy-2.4.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:cf6470d91d34bf669f61d515499859fa7a4c2f7c36434afb70e82df7217933f9"},
    {file = "numpy-2.4.1-cp312-cp312-win32.whl", hash = "sha256:b6bcf39112e956594b3331316d90c90c90fb961e39696bda97b89462f5f3943f"},
    {file = "numpy-2.4.1-cp312-cp312-win_amd64.whl", hash = "sha256:e1a27bb1b2dee45a2a53f5ca6ff2d1a7f135287883a1689e930d44d1ff296c87"},
    {file = "numpy-2.4.1-cp312-cp312-win_arm64.whl", hash = "sha256:0e6e8f9d9ecf95399982019c01223dc130542960a12edfa8edd1122dfa66a8a8"},
    {file = "numpy-2.4.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:d797454e37570cfd61143b73b8debd623c3c0952959adb817dd310a483d58a1b"},
    {file = "numpy-2.4.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:82c55962006156aeef1629b953fd359064aa47e4d82cfc8e67f0918f7da3344f"},
    {file = "numpy-2.4.1-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:71abbea030f2cfc3092a0ff9f8c8fdefdc5e0bf7d9d9c99663538bb0ecdac0b9"},
    {file = "numpy-2.4.1-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:5b55aa56165b17aaf15520beb9cbd33c9039810e0d9643dd4379e44294c7303e"},
    {file = "numpy-2.4.1-cp313-cp313-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c0faba4a331195bfa96f93dd9dfaa10b2c7aa8cda3a02b7fd635e588fe821bf5"},
    {file = "numpy-2.4.1-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d3e3087f53e2b4428766b54932644d148613c5a595150533ae7f00dab2f319a8"},
    {file = "numpy-2.4.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:49e792ec351315e16da54b543db06ca8a86985ab682602d90c60ef4ff4db2a9c"},
    {file = "numpy-2.4.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:79e9e06c4c2379db47f3f6fc7a8652e7498251789bf8ff5bd43bf478ef314ca2"},
    {file = "numpy-2.4.1-cp313-cp313-win32.whl", hash = "sha256:3d1a100e48cb266090a031397863ff8a30050ceefd798f686ff92c67a486753d"},
    {file = "numpy-2.4.1-cp313-cp313-win_amd64.whl", hash = "sha256:92a0e65272fd60bfa0d9278e0484c2f52fe03b97aedc02b357f33fe752c52ffb"},
    {file = "numpy-2.4.1-cp313-cp313-win_arm64.whl", hash = "sha256:20d4649c773f66cc2fc36f663e091f57c3b7655f936a4c681b4250855d1da8f5"},
    {file = "numpy-2.4.1-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:f93bc6892fe7b0663e5ffa83b61aab510aacffd58c16e012bb9352d489d90cb7"},
    {file = "numpy-2.4.1-cp313-cp313t-macosx_14_0_arm64.whl", hash = "sha256:178de8f87948163d98a4c9ab5bee4ce6519ca918926ec8df195af582de28544d"},
    {file = "numpy-2.4.1-cp313-cp313t-macosx_14_0_x86_64.whl", hash = "sha256:98b35775e03ab7f868908b524fc0a84d38932d8daf7b7e1c3c3a1b6c7a2c9f15"},
    {file = "numpy-2.4.1-cp313-cp313t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:941c2a93313d030f219f3a71fd3d91a728b82979a5e8034eb2e60d394a2b83f9"},
    {file = "numpy-2.4.1-cp313-cp313t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:529050522e983e00a6c1c6b67411083630de8b57f65e853d7b03d9281b8694d2"},
    {file = "numpy-2.4.1-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:2302dc0224c1cbc49bb94f7064f3f923a971bfae45c33870dcbff63a2a550505"},
    {file = "numpy-2.4.1-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:9171a42fcad32dcf3fa86f0a4faa5e9f8facefdb276f54b8b390d90447cff4e2"},
    {file = "numpy-2.4.1-cp313-cp313t-win32.whl", hash = "sha256:382ad67d99ef49024f11d1ce5dcb5ad8432446e4246a4b014418ba3a1175a1f4"},
    {file = "numpy-2.4.1-cp313-cp313t-win_amd64.whl", hash = "sha256:62fea415f83ad8fdb6c20840578e5fbaf5ddd65e0ec6c3c47eda0f69da172510"},
    {file = "numpy-2.4.1-cp313-cp313t-win_arm64.whl", hash = "sha256:a7870e8c5fc11aef57d6fea4b4085e537a3a60ad2cdd14322ed531fdca68d261"},
    {file = "numpy-2.4.1-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:3869ea1ee1a1edc16c29bbe3a2f2a4e515cc3a44d43903ad41e0cacdbaf733dc"},
    {file = "numpy-2.4.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:e867df947d427cdd7a60e3e271729090b0f0df80f5f10ab7dd436f40811699c3"},
    {file = "numpy-2.4.1-cp314-cp314-macosx_14_0_arm64.whl", hash = "sha256:e3bd2cb07841166420d2fa7146c96ce00cb3410664cbc1a6be028e456c4ee220"},
    {file = "numpy-2.4.1-cp314-cp314-macosx_14_0_x86_64.whl", hash = "sha256:f0a90aba7d521e6954670550e561a4cb925713bd944445dbe9e729b71f6cabee"},
    {file = "numpy-2.4.1-cp314-cp314-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5d558123217a83b2d1ba316b986e9248a1ed1971ad495963d555ccd75dcb1556"},
    {file = "numpy-2.4.1-cp314-cp314-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:2f44de05659b67d20499cbc96d49f2650769afcb398b79b324bb6e297bfe3844"},
    {file = "numpy-2.4.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:69e7419c9012c4aaf695109564e3387f1259f001b4326dfa55907b098af082d3"},
    {file = "numpy-2.4.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:2ffd257026eb1b34352e749d7cc1678b5eeec3e329ad8c9965a797e08ccba205"},
    {file = "numpy-2.4.1-cp314-cp314-win32.whl", hash = "sha256:727c6c3275ddefa0dc078524a85e064c057b4f4e71ca5ca29a19163c607be745"},
    {file = "numpy-2.4.1-cp314-cp314-win_amd64.whl", hash = "sha256:7d5d7999df434a038d75a748275cd6c0094b0ecdb0837342b332a82defc4dc4d"},
    {file = "numpy-2.4.1-cp314-cp314-win_arm64.whl", hash = "sha256:ce9ce141a505053b3c7bce3216071f3bf5c182b8b28930f14cd24d43932cd2df"},
    {file = "numpy-2.4.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:4e53170557d37ae404bf8d542ca5b7c629d6efa1117dac6a83e394142ea0a43f"},
    {file = "numpy-2.4.1-cp314-cp314t-macosx_14_0_arm64.whl", hash = "sha256:a73044b752f5d34d4232f25f18160a1cc418ea4507f5f11e299d8ac36875f8a0"},
    {file = "numpy-2.4.1-cp314-cp314t-macosx_14_0_x86_64.whl", hash = "sha256:fb1461c99de4d040666ca0444057b06541e5642f800b71c56e6ea92d6a853a0c"},
    {file = "numpy-2.4.1-cp314-cp314t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:423797bdab2eeefbe608d7c1ec7b2b4fd3c58d51460f1ee26c7500a1d9c9ee93"},
    {file = "numpy-2.4.1-cp314-cp314t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:52b5f61bdb323b566b528899cc7db2ba5d1015bda7ea811a8bcf3c89c331fa42"},
    {file = "numpy-2.4.1-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:42d7dd5fa36d16d52a84f821eb96031836fd405ee6955dd732f2023724d0aa01"},
    {file = "numpy-2.4.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:e7b6b5e28bbd47b7532698e5db2fe1db693d84b58c254e4389d99a27bb9b8f6b"},
    {file = "numpy-2.4.1-cp314-cp314t-win32.whl", hash = "sha256:5de60946f14ebe15e713a6f22850c2372fa72f4ff9a432ab44aa90edcadaa65a"},
    {file = "numpy-2.4.1-cp314-cp314t-win_amd64.whl", hash = "sha256:8f085da926c0d491ffff3096f91078cc97ea67e7e6b65e490bc8dcda65663be2"},
    {file = "numpy-2.4.1-cp314-cp314t-win_arm64.whl", hash = "sha256:6436cffb4f2bf26c974344439439c95e152c9a527013f26b3577be6c2ca64295"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-macosx_10_15_x86_64.whl", hash = "sha256:8ad35f20be147a204e28b6a0575fbf3540c5e5f802634d4258d55b1ff5facce1"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:8097529164c0f3e32bb89412a0905d9100bf434d9692d9fc275e18dcf53c9344"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-macosx_14_0_arm64.whl", hash = "sha256:ea66d2b41ca4a1630aae5507ee0a71647d3124d1741980138aa8f28f44dac36e"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-macosx_14_0_x86_64.whl", hash = "sha256:d3f8f0df9f4b8be57b3bf74a1d087fec68f927a2fab68231fdb442bf2c12e426"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:2023ef86243690c2791fd6353e5b4848eedaa88ca8a2d129f462049f6d484696"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:8361ea4220d763e54cff2fbe7d8c93526b744f7cd9ddab47afeff7e14e8503be"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-win_amd64.whl", hash = "sha256:4f1b68ff47680c2925f8063402a693ede215f0257f02596b1318ecdfb1d79e33"},
    {file = "numpy-2.4.1.tar.gz", hash = "sha256:a1ceafc5042451a858231588a104093474c6a5c57dcc724841f5c888d237d690"},
]

[[package]]
name = "packaging"
version = "26.0"
description = "Core utilities for Python packages"
optional = false
python-versions = ">=3.8"
groups = ["main", "dev"]
files = [
    {file = "packaging-26.0-py3-none-any.whl", hash = "sha256:b36f1fef9334a5588b4166f8bcd26a14e521f2b55e6b9de3aaa80d3ff7a37529"},
    {file = "packaging-26.0.tar.gz", hash = "sha256:00243ae351a257117b6a241061796684b084ed1c516a08c48a3f7e147a9d80b4"},
]

[[package]]
name = "pathspec"
version = "1.0.3"
description = "Utility library for gitignore style pattern matching of file paths."
optional = false
python-versions = ">=3.9"
groups = ["main", "dev"]
files = [
    {file = "pathspec-1.0.3-py3-none-any.whl", hash = "sha256:e80767021c1cc524aa3fb14bedda9c34406591343cc42797b386ce7b9354fb6c"},
    {file = "pathspec-1.0.3.tar.gz", hash = "sha256:bac5cf97ae2c2876e2d25ebb15078eb04d76e4b98921ee31c6f85ade8b59444d"},
]

[package.extras]
hyperscan = ["hyperscan (>=0.7)"]
optional = ["typing-extensions (>=4)"]
re2 = ["google-re2 (>=1.1)"]
tests = ["pytest (>=9)", "typing-extensions (>=4.15)"]

[[package]]
name = "pep8-naming"
version = "0.15.1"
description = "Check PEP-8 naming conventions, plugin for flake8"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "pep8_naming-0.15.1-py3-none-any.whl", hash = "sha256:eb63925e7fd9e028c7f7ee7b1e413ec03d1ee5de0e627012102ee0222c273c86"},
    {file = "pep8_naming-0.15.1.tar.gz", hash = "sha256:f6f4a499aba2deeda93c1f26ccc02f3da32b035c8b2db9696b730ef2c9639d29"},
]

[package.dependencies]
flake8 = ">=5.0.0"

[[package]]
name = "platformdirs"
version = "4.9.6"
description = "A small Python package for determining appropriate platform-specific dirs, e.g. a `user data dir`."
optional = false
python-versions = ">=3.10"
groups = ["main", "dev"]
files = [
    {file = "platformdirs-4.9.6-py3-none-any.whl", hash = "sha256:e61adb1d5e5cb3441b4b7710bea7e4c12250ca49439228cc1021c00dcfac0917"},
    {file = "platformdirs-4.9.6.tar.gz", hash = "sha256:3bfa75b0ad0db84096ae777218481852c0ebc6c727b3168c1b9e0118e458cf0a"},
]

[[package]]
name = "pluggy"
version = "1.6.0"
description = "plugin and hook calling mechanisms for python"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "pluggy-1.6.0-py3-none-any.whl", hash = "sha256:e920276dd6813095e9377c0bc5566d94c932c33b27a3e3945d8389c374dd4746"},
    {file = "pluggy-1.6.0.tar.gz", hash = "sha256:7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3"},
]

[package.extras]
dev = ["pre-commit", "tox"]
testing = ["coverage", "pytest", "pytest-benchmark"]

[[package]]
name = "protobuf"
version = "4.25.9"
description = ""
optional = false
python-versions = ">=3.8"
groups = ["main", "dev"]
markers = "python_version <= \"3.12\""
files = [
    {file = "protobuf-4.25.9-cp310-abi3-win32.whl", hash = "sha256:bde396f568b0b46fc8fbfe9f02facf25b6755b2578a3b8ac61e74b9d69499e03"},
    {file = "protobuf-4.25.9-cp310-abi3-win_amd64.whl", hash = "sha256:3683c05154252206f7cb2d371626514b3708199d9bcf683b503dabf3a2e38e06"},
    {file = "protobuf-4.25.9-cp37-abi3-macosx_10_9_universal2.whl", hash = "sha256:9560813560e6ee72c11ca8873878bdb7ee003c96a57ebb013245fe84e2540904"},
    {file = "protobuf-4.25.9-cp37-abi3-manylinux2014_aarch64.whl", hash = "sha256:999146ef02e7fa6a692477badd1528bcd7268df211852a3df2d834ba2b480791"},
    {file = "protobuf-4.25.9-cp37-abi3-manylinux2014_x86_64.whl", hash = "sha256:438c636de8fb706a0de94a12a268ef1ae8f5ba5ae655a7671fcda5968ba3c9be"},
    {file = "protobuf-4.25.9-cp38-cp38-win32.whl", hash = "sha256:7f7c1abcea3fc215918fba67a2d2a80fbcccc0f84159610eb187e9bbe6f939ee"},
    {file = "protobuf-4.25.9-cp38-cp38-win_amd64.whl", hash = "sha256:79faf4e5a80b231d94dcf3a0a2917ccbacf0f586f12c9b9c91794b41b913a853"},
    {file = "protobuf-4.25.9-cp39-cp39-win32.whl", hash = "sha256:9481e80e8cffb1c492c68e7c4e6726f4ad02eebc4fa97ead7beebeaa3639511d"},
    {file = "protobuf-4.25.9-cp39-cp39-win_amd64.whl", hash = "sha256:b1d467352de666dc1b6d5740b6319d9c08cab7b21b452501e4ee5b0ac5156780"},
    {file = "protobuf-4.25.9-py3-none-any.whl", hash = "sha256:d49b615e7c935194ac161f0965699ac84df6112c378e05ec53da65d2e4cbb6d4"},
    {file = "protobuf-4.25.9.tar.gz", hash = "sha256:b0dc7e7c68de8b1ce831dacb12fb407e838edbb8b6cc0dc3a2a6b4cbf6de9cff"},
]

[[package]]
name = "protobuf"
version = "5.29.6"
description = ""
optional = false
python-versions = ">=3.8"
groups = ["main", "dev"]
markers = "python_version == \"3.13\""
files = [
    {file = "protobuf-5.29.6-cp310-abi3-win32.whl", hash = "sha256:62e8a3114992c7c647bce37dcc93647575fc52d50e48de30c6fcb28a6a291eb1"},
    {file = "protobuf-5.29.6-cp310-abi3-win_amd64.whl", hash = "sha256:7e6ad413275be172f67fdee0f43484b6de5a904cc1c3ea9804cb6fe2ff366eda"},
    {file = "protobuf-5.29.6-cp38-abi3-macosx_10_9_universal2.whl", hash = "sha256:b5a169e664b4057183a34bdc424540e86eea47560f3c123a0d64de4e137f9269"},
    {file = "protobuf-5.29.6-cp38-abi3-manylinux2014_aarch64.whl", hash = "sha256:a8866b2cff111f0f863c1b3b9e7572dc7eaea23a7fae27f6fc613304046483e6"},
    {file = "protobuf-5.29.6-cp38-abi3-manylinux2014_x86_64.whl", hash = "sha256:e3387f44798ac1106af0233c04fb8abf543772ff241169946f698b3a9a3d3ab9"},
    {file = "protobuf-5.29.6-cp38-cp38-win32.whl", hash = "sha256:36ade6ff88212e91aef4e687a971a11d7d24d6948a66751abc1b3238648f5d05"},
    {file = "protobuf-5.29.6-cp38-cp38-win_amd64.whl", hash = "sha256:831e2da16b6cc9d8f1654c041dd594eda43391affd3c03a91bea7f7f6da106d6"},
    {file = "protobuf-5.29.6-cp39-cp39-win32.whl", hash = "sha256:cb4c86de9cd8a7f3a256b9744220d87b847371c6b2f10bde87768918ef33ba49"},
    {file = "protobuf-5.29.6-cp39-cp39-win_amd64.whl", hash = "sha256:76e07e6567f8baf827137e8d5b8204b6c7b6488bbbff1bf0a72b383f77999c18"},
    {file = "protobuf-5.29.6-py3-none-any.whl", hash = "sha256:6b9edb641441b2da9fa8f428760fc136a49cf97a52076010cf22a2ff73438a86"},
    {file = "protobuf-5.29.6.tar.gz", hash = "sha256:da9ee6a5424b6b30fd5e45c5ea663aef540ca95f9ad99d1e887e819cdf9b8723"},
]

[[package]]
name = "protobuf"
version = "6.33.6"
description = ""
optional = false
python-versions = ">=3.9"
groups = ["main", "dev"]
markers = "python_version >= \"3.14\""
files = [
    {file = "protobuf-6.33.6-cp310-abi3-win32.whl", hash = "sha256:7d29d9b65f8afef196f8334e80d6bc1d5d4adedb449971fefd3723824e6e77d3"},
    {file = "protobuf-6.33.6-cp310-abi3-win_amd64.whl", hash = "sha256:0cd27b587afca21b7cfa59a74dcbd48a50f0a6400cfb59391340ad729d91d326"},
    {file = "protobuf-6.33.6-cp39-abi3-macosx_10_9_universal2.whl", hash = "sha256:9720e6961b251bde64edfdab7d500725a2af5280f3f4c87e57c0208376aa8c3a"},
    {file = "protobuf-6.33.6-cp39-abi3-manylinux2014_aarch64.whl", hash = "sha256:e2afbae9b8e1825e3529f88d514754e094278bb95eadc0e199751cdd9a2e82a2"},
    {file = "protobuf-6.33.6-cp39-abi3-manylinux2014_s390x.whl", hash = "sha256:c96c37eec15086b79762ed265d59ab204dabc53056e3443e702d2681f4b39ce3"},
    {file = "protobuf-6.33.6-cp39-abi3-manylinux2014_x86_64.whl", hash = "sha256:e9db7e292e0ab79dd108d7f1a94fe31601ce1ee3f7b79e0692043423020b0593"},
    {file = "protobuf-6.33.6-cp39-cp39-win32.whl", hash = "sha256:bd56799fb262994b2c2faa1799693c95cc2e22c62f56fb43af311cae45d26f0e"},
    {file = "protobuf-6.33.6-cp39-cp39-win_amd64.whl", hash = "sha256:f443a394af5ed23672bc6c486be138628fbe5c651ccbc536873d7da23d1868cf"},
    {file = "protobuf-6.33.6-py3-none-any.whl", hash = "sha256:77179e006c476e69bf8e8ce866640091ec42e1beb80b213c3900006ecfba6901"},
    {file = "protobuf-6.33.6.tar.gz", hash = "sha256:a6768d25248312c297558af96a9f9c929e8c4cee0659cb07e780731095f38135"},
]

[[package]]
name = "pycodestyle"
version = "2.9.1"
description = "Python style guide checker"
optional = false
python-versions = ">=3.6"
groups = ["dev"]
markers = "python_version < \"3.12\""
files = [
    {file = "pycodestyle-2.9.1-py2.py3-none-any.whl", hash = "sha256:d1735fc58b418fd7c5f658d28d943854f8a849b01a5d0a1e6f3f3fdd0166804b"},
    {file = "pycodestyle-2.9.1.tar.gz", hash = "sha256:2c9607871d58c76354b697b42f5d57e1ada7d261c261efac224b664affdc5785"},
]

[[package]]
name = "pycodestyle"
version = "2.11.1"
description = "Python style guide checker"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
markers = "python_version >= \"3.12\""
files = [
    {file = "pycodestyle-2.11.1-py2.py3-none-any.whl", hash = "sha256:44fe31000b2d866f2e41841b18528a505fbd7fef9017b04eff4e2648a0fadc67"},
    {file = "pycodestyle-2.11.1.tar.gz", hash = "sha256:41ba0e7afc9752dfb53ced5489e89f8186be00e599e712660695b7a75ff2663f"},
]

[[package]]
name = "pydocstyle"
version = "6.3.0"
description = "Python docstring style checker"
optional = false
python-versions = ">=3.6"
groups = ["dev"]
files = [
    {file = "pydocstyle-6.3.0-py3-none-any.whl", hash = "sha256:118762d452a49d6b05e194ef344a55822987a462831ade91ec5c06fd2169d019"},
    {file = "pydocstyle-6.3.0.tar.gz", hash = "sha256:7ce43f0c0ac87b07494eb9c0b462c0b73e6ff276807f204d6b53edc72b7e44e1"},
]

[package.dependencies]
snowballstemmer = ">=2.2.0"

[package.extras]
toml = ["tomli (>=1.2.3) ; python_version < \"3.11\""]

[[package]]
name = "pyflakes"
version = "2.5.0"
description = "passive checker of Python programs"
optional = false
python-versions = ">=3.6"
groups = ["dev"]
markers = "python_version < \"3.12\""
files = [
    {file = "pyflakes-2.5.0-py2.py3-none-any.whl", hash = "sha256:4579f67d887f804e67edb544428f264b7b24f435b263c4614f384135cea553d2"},
    {file = "pyflakes-2.5.0.tar.gz", hash = "sha256:491feb020dca48ccc562a8c0cbe8df07ee13078df59813b83959cbdada312ea3"},
]

[[package]]
name = "pyflakes"
version = "3.1.0"
description = "passive checker of Python programs"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
markers = "python_version >= \"3.12\""
files = [
    {file = "pyflakes-3.1.0-py2.py3-none-any.whl", hash = "sha256:4132f6d49cb4dae6819e5379898f2b8cce3c5f23994194c24b77d5da2e36f774"},
    {file = "pyflakes-3.1.0.tar.gz", hash = "sha256:a0aae034c444db0071aa077972ba4768d40c830d9539fd45bf4cd3f8f6992efc"},
]

[[package]]
name = "pygments"
version = "2.19.2"
description = "Pygments is a syntax highlighting package written in Python."
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "pygments-2.19.2-py3-none-any.whl", hash = "sha256:86540386c03d588bb81d44bc3928634ff26449851e99741617ecb9037ee5ec0b"},
    {file = "pygments-2.19.2.tar.gz", hash = "sha256:636cb2477cec7f8952536970bc533bc43743542f70392ae026374600add5b887"},
]

[package.extras]
windows-terminal = ["colorama (>=0.4.6)"]

[[package]]
name = "pyproject-api"
version = "1.10.0"
description = "API to interact with the python pyproject.toml based projects"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "pyproject_api-1.10.0-py3-none-any.whl", hash = "sha256:8757c41a79c0f4ab71b99abed52b97ecf66bd20b04fa59da43b5840bac105a09"},
    {file = "pyproject_api-1.10.0.tar.gz", hash = "sha256:40c6f2d82eebdc4afee61c773ed208c04c19db4c4a60d97f8d7be3ebc0bbb330"},
]

[package.dependencies]
packaging = ">=25"
tomli = {version = ">=2.3", markers = "python_version < \"3.11\""}

[package.extras]
docs = ["furo (>=2025.9.25)", "sphinx-autodoc-typehints (>=3.5.1)"]
testing = ["covdefaults (>=2.3)", "pytest (>=8.4.2)", "pytest-cov (>=7)", "pytest-mock (>=3.15.1)", "setuptools (>=80.9)"]

[[package]]
name = "pytest"
version = "9.1.1"
description = "pytest: simple powerful testing with Python"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "pytest-9.1.1-py3-none-any.whl", hash = "sha256:37a86b45efb9a47a61a36449063e8e18d0cab3161329fc099eb21783169c4f0c"},
    {file = "pytest-9.1.1.tar.gz", hash = "sha256:1088fbde8f2b49d95a549a195707afa7a76a3ce9bcadc26b6d71f0ffda5fe313"},
]

[package.dependencies]
colorama = {version = ">=0.4", markers = "sys_platform == \"win32\""}
exceptiongroup = {version = ">=1", markers = "python_version < \"3.11\""}
iniconfig = ">=1.0.1"
packaging = ">=22"
pluggy = ">=1.5,<2"
pygments = ">=2.7.2"
tomli = {version = ">=1", markers = "python_version < \"3.11\""}

[package.extras]
dev = ["argcomplete", "attrs (>=19.2)", "hypothesis (>=3.56)", "mock", "requests", "setuptools", "xmlschema"]

[[package]]
name = "pytest-cov"
version = "7.1.0"
description = "Pytest plugin for measuring coverage."
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "pytest_cov-7.1.0-py3-none-any.whl", hash = "sha256:a0461110b7865f9a271aa1b51e516c9a95de9d696734a2f71e3e78f46e1d4678"},
    {file = "pytest_cov-7.1.0.tar.gz", hash = "sha256:30674f2b5f6351aa09702a9c8c364f6a01c27aae0c1366ae8016160d1efc56b2"},
]

[package.dependencies]
coverage = {version = ">=7.10.6", extras = ["toml"]}
pluggy = ">=1.2"
pytest = ">=7"

[package.extras]
testing = ["process-tests", "pytest-xdist", "virtualenv"]

[[package]]
name = "python-decouple"
version = "3.8"
description = "Strict separation of settings from code."
optional = false
python-versions = "*"
groups = ["main", "dev"]
files = [
    {file = "python-decouple-3.8.tar.gz", hash = "sha256:ba6e2657d4f376ecc46f77a3a615e058d93ba5e465c01bbe57289bfb7cce680f"},
    {file = "python_decouple-3.8-py3-none-any.whl", hash = "sha256:d0d45340815b25f4de59c974b855bb38d03151d81b037d9e3f463b0c9f8cbd66"},
]

[[package]]
name = "python-discovery"
version = "1.2.2"
description = "Python interpreter discovery"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "python_discovery-1.2.2-py3-none-any.whl", hash = "sha256:e1ae95d9af875e78f15e19aed0c6137ab1bb49c200f21f5061786490c9585c7a"},
    {file = "python_discovery-1.2.2.tar.gz", hash = "sha256:876e9c57139eb757cb5878cbdd9ae5379e5d96266c99ef731119e04fffe533bb"},
]

[package.dependencies]
filelock = ">=3.15.4"
platformdirs = ">=4.3.6,<5"

[package.extras]
docs = ["furo (>=2025.12.19)", "sphinx (>=9.1)", "sphinx-autodoc-typehints (>=3.6.3)", "sphinxcontrib-mermaid (>=2)"]
testing = ["covdefaults (>=2.3)", "coverage (>=7.5.4)", "pytest (>=8.3.5)", "pytest-mock (>=3.14)", "setuptools (>=75.1)"]

[[package]]
name = "pytokens"
version = "0.4.0"
description = "A Fast, spec compliant Python 3.14+ tokenizer that runs on older Pythons."
optional = false
python-versions = ">=3.8"
groups = ["main", "dev"]
files = [
    {file = "pytokens-0.4.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:af0c3166aea367a9e755a283171befb92dd3043858b94ae9b3b7efbe9def26a3"},
    {file = "pytokens-0.4.0-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:daae524ed14ca459932cbf51d74325bea643701ba8a8b0cc2d10f7cd4b3e2b63"},
    {file = "pytokens-0.4.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e95cb158c44d642ed62f555bf8136bbe780dbd64d2fb0b9169e11ffb944664c3"},
    {file = "pytokens-0.4.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:df58d44630eaf25f587540e94bdf1fc50b4e6d5f212c786de0fb024bfcb8753a"},
    {file = "pytokens-0.4.0-cp310-cp310-win_amd64.whl", hash = "sha256:55efcc36f9a2e0e930cfba0ce7f83445306b02f8326745585ed5551864eba73a"},
    {file = "pytokens-0.4.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:92eb3ef88f27c22dc9dbab966ace4d61f6826e02ba04dac8e2d65ea31df56c8e"},
    {file = "pytokens-0.4.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f4b77858a680635ee9904306f54b0ee4781effb89e211ba0a773d76539537165"},
    {file = "pytokens-0.4.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:25cacc20c2ad90acb56f3739d87905473c54ca1fa5967ffcd675463fe965865e"},
    {file = "pytokens-0.4.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:628fab535ebc9079e4db35cd63cb401901c7ce8720a9834f9ad44b9eb4e0f1d4"},
    {file = "pytokens-0.4.0-cp311-cp311-win_amd64.whl", hash = "sha256:4d0f568d7e82b7e96be56d03b5081de40e43c904eb6492bf09aaca47cd55f35b"},
    {file = "pytokens-0.4.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:cd8da894e5a29ba6b6da8be06a4f7589d7220c099b5e363cb0643234b9b38c2a"},
    {file = "pytokens-0.4.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:237ba7cfb677dbd3b01b09860810aceb448871150566b93cd24501d5734a04b1"},
    {file = "pytokens-0.4.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:01d1a61e36812e4e971cfe2c0e4c1f2d66d8311031dac8bf168af8a249fa04dd"},
    {file = "pytokens-0.4.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:e47e2ef3ec6ee86909e520d79f965f9b23389fda47460303cf715d510a6fe544"},
    {file = "pytokens-0.4.0-cp312-cp312-win_amd64.whl", hash = "sha256:3d36954aba4557fd5a418a03cf595ecbb1cdcce119f91a49b19ef09d691a22ae"},
    {file = "pytokens-0.4.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:73eff3bdd8ad08da679867992782568db0529b887bed4c85694f84cdf35eafc6"},
    {file = "pytokens-0.4.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d97cc1f91b1a8e8ebccf31c367f28225699bea26592df27141deade771ed0afb"},
    {file = "pytokens-0.4.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a2c8952c537cb73a1a74369501a83b7f9d208c3cf92c41dd88a17814e68d48ce"},
    {file = "pytokens-0.4.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:5dbf56f3c748aed9310b310d5b8b14e2c96d3ad682ad5a943f381bdbbdddf753"},
    {file = "pytokens-0.4.0-cp313-cp313-win_amd64.whl", hash = "sha256:e131804513597f2dff2b18f9911d9b6276e21ef3699abeffc1c087c65a3d975e"},
    {file = "pytokens-0.4.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:0d7374c917197106d3c4761374718bc55ea2e9ac0fb94171588ef5840ee1f016"},
    {file = "pytokens-0.4.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0cd3fa1caf9e47a72ee134a29ca6b5bea84712724bba165d6628baa190c6ea5b"},
    {file = "pytokens-0.4.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9c6986576b7b07fe9791854caa5347923005a80b079d45b63b0be70d50cce5f1"},
    {file = "pytokens-0.4.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:9940f7c2e2f54fb1cb5fe17d0803c54da7a2bf62222704eb4217433664a186a7"},
    {file = "pytokens-0.4.0-cp314-cp314-win_amd64.whl", hash = "sha256:54691cf8f299e7efabcc25adb4ce715d3cef1491e1c930eaf555182f898ef66a"},
    {file = "pytokens-0.4.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:94ff5db97a0d3cd7248a5b07ba2167bd3edc1db92f76c6db00137bbaf068ddf8"},
    {file = "pytokens-0.4.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d0dd6261cd9cc95fae1227b1b6ebee023a5fd4a4b6330b071c73a516f5f59b63"},
    {file = "pytokens-0.4.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0cdca8159df407dbd669145af4171a0d967006e0be25f3b520896bc7068f02c4"},
    {file = "pytokens-0.4.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:4b5770abeb2a24347380a1164a558f0ebe06e98aedbd54c45f7929527a5fb26e"},
    {file = "pytokens-0.4.0-cp314-cp314t-win_amd64.whl", hash = "sha256:74500d72c561dad14c037a9e86a657afd63e277dd5a3bb7570932ab7a3b12551"},
    {file = "pytokens-0.4.0-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:e368e0749e4e9d86a6e08763310dc92bc69ad73d9b6db5243b30174c71a8a534"},
    {file = "pytokens-0.4.0-cp38-cp38-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:865cc65c75c8f2e9e0d8330338f649b12bfd9442561900ebaf58c596a72107d2"},
    {file = "pytokens-0.4.0-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:dbb9338663b3538f31c4ca7afe4f38d9b9b3a16a8be18a273a5704a1bc7a2367"},
    {file = "pytokens-0.4.0-cp38-cp38-musllinux_1_2_x86_64.whl", hash = "sha256:658f870523ac1a5f4733d7db61ce9af61a0c23b2aeea3d03d1800c93f760e15f"},
    {file = "pytokens-0.4.0-cp38-cp38-win_amd64.whl", hash = "sha256:d69a2491190a74e4b6f87f3b9dfce7a6873de3f3bf330d20083d374380becac0"},
    {file = "pytokens-0.4.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:8cd795191c4127fcb3d7b76d84006a07748c390226f47657869235092eedbc05"},
    {file = "pytokens-0.4.0-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ef2bcbddb73ac18599a86c8c549d5145130f2cd9d83dc2b5482fd8322b7806cd"},
    {file = "pytokens-0.4.0-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:06ac081c1187389762b58823d90d6339e6880ce0df912f71fb9022d81d7fd429"},
    {file = "pytokens-0.4.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:278129d54573efdc79e75c6082e73ebd19858e22a2e848359f93629323186ca6"},
    {file = "pytokens-0.4.0-cp39-cp39-win_amd64.whl", hash = "sha256:9380fb6d96fa5ab83ed606ebad27b6171930cc14a8a8d215f6adb187ba428690"},
    {file = "pytokens-0.4.0-py3-none-any.whl", hash = "sha256:0508d11b4de157ee12063901603be87fb0253e8f4cb9305eb168b1202ab92068"},
    {file = "pytokens-0.4.0.tar.gz", hash = "sha256:6b0b03e6ea7c9f9d47c5c61164b69ad30f4f0d70a5d9fe7eac4d19f24f77af2d"},
]

[package.extras]
dev = ["black", "build", "mypy", "pytest", "pytest-cov", "setuptools", "tox", "twine", "wheel"]

[[package]]
name = "pywin32"
version = "311"
description = "Python for Window Extensions"
optional = false
python-versions = "*"
groups = ["main", "dev"]
markers = "sys_platform == \"win32\""
files = [
    {file = "pywin32-311-cp310-cp310-win32.whl", hash = "sha256:d03ff496d2a0cd4a5893504789d4a15399133fe82517455e78bad62efbb7f0a3"},
    {file = "pywin32-311-cp310-cp310-win_amd64.whl", hash = "sha256:797c2772017851984b97180b0bebe4b620bb86328e8a884bb626156295a63b3b"},
    {file = "pywin32-311-cp310-cp310-win_arm64.whl", hash = "sha256:0502d1facf1fed4839a9a51ccbcc63d952cf318f78ffc00a7e78528ac27d7a2b"},
    {file = "pywin32-311-cp311-cp311-win32.whl", hash = "sha256:184eb5e436dea364dcd3d2316d577d625c0351bf237c4e9a5fabbcfa5a58b151"},
    {file = "pywin32-311-cp311-cp311-win_amd64.whl", hash = "sha256:3ce80b34b22b17ccbd937a6e78e7225d80c52f5ab9940fe0506a1a16f3dab503"},
    {file = "pywin32-311-cp311-cp311-win_arm64.whl", hash = "sha256:a733f1388e1a842abb67ffa8e7aad0e70ac519e09b0f6a784e65a136ec7cefd2"},
    {file = "pywin32-311-cp312-cp312-win32.whl", hash = "sha256:750ec6e621af2b948540032557b10a2d43b0cee2ae9758c54154d711cc852d31"},
    {file = "pywin32-311-cp312-cp312-win_amd64.whl", hash = "sha256:b8c095edad5c211ff31c05223658e71bf7116daa0ecf3ad85f3201ea3190d067"},
    {file = "pywin32-311-cp312-cp312-win_arm64.whl", hash = "sha256:e286f46a9a39c4a18b319c28f59b61de793654af2f395c102b4f819e584b5852"},
    {file = "pywin32-311-cp313-cp313-win32.whl", hash = "sha256:f95ba5a847cba10dd8c4d8fefa9f2a6cf283b8b88ed6178fa8a6c1ab16054d0d"},
    {file = "pywin32-311-cp313-cp313-win_amd64.whl", hash = "sha256:718a38f7e5b058e76aee1c56ddd06908116d35147e133427e59a3983f703a20d"},
    {file = "pywin32-311-cp313-cp313-win_arm64.whl", hash = "sha256:7b4075d959648406202d92a2310cb990fea19b535c7f4a78d3f5e10b926eeb8a"},
    {file = "pywin32-311-cp314-cp314-win32.whl", hash = "sha256:b7a2c10b93f8986666d0c803ee19b5990885872a7de910fc460f9b0c2fbf92ee"},
    {file = "pywin32-311-cp314-cp314-win_amd64.whl", hash = "sha256:3aca44c046bd2ed8c90de9cb8427f581c479e594e99b5c0bb19b29c10fd6cb87"},
    {file = "pywin32-311-cp314-cp314-win_arm64.whl", hash = "sha256:a508e2d9025764a8270f93111a970e1d0fbfc33f4153b388bb649b7eec4f9b42"},
    {file = "pywin32-311-cp38-cp38-win32.whl", hash = "sha256:6c6f2969607b5023b0d9ce2541f8d2cbb01c4f46bc87456017cf63b73f1e2d8c"},
    {file = "pywin32-311-cp38-cp38-win_amd64.whl", hash = "sha256:c8015b09fb9a5e188f83b7b04de91ddca4658cee2ae6f3bc483f0b21a77ef6cd"},
    {file = "pywin32-311-cp39-cp39-win32.whl", hash = "sha256:aba8f82d551a942cb20d4a83413ccbac30790b50efb89a75e4f586ac0bb8056b"},
    {file = "pywin32-311-cp39-cp39-win_amd64.whl", hash = "sha256:e0c4cfb0621281fe40387df582097fd796e80430597cb9944f0ae70447bacd91"},
    {file = "pywin32-311-cp39-cp39-win_arm64.whl", hash = "sha256:62ea666235135fee79bb154e695f3ff67370afefd71bd7fea7512fc70ef31e3d"},
]

[[package]]
name = "pyyaml"
version = "6.0.3"
description = "YAML parser and emitter for Python"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "PyYAML-6.0.3-cp38-cp38-macosx_10_13_x86_64.whl", hash = "sha256:c2514fceb77bc5e7a2f7adfaa1feb2fb311607c9cb518dbc378688ec73d8292f"},
    {file = "PyYAML-6.0.3-cp38-cp38-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:9c57bb8c96f6d1808c030b1687b9b5fb476abaa47f0db9c0101f5e9f394e97f4"},
    {file = "PyYAML-6.0.3-cp38-cp38-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:efd7b85f94a6f21e4932043973a7ba2613b059c4a000551892ac9f1d11f5baf3"},
    {file = "PyYAML-6.0.3-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:22ba7cfcad58ef3ecddc7ed1db3409af68d023b7f940da23c6c2a1890976eda6"},
    {file = "PyYAML-6.0.3-cp38-cp38-musllinux_1_2_x86_64.whl", hash = "sha256:6344df0d5755a2c9a276d4473ae6b90647e216ab4757f8426893b5dd2ac3f369"},
    {file = "PyYAML-6.0.3-cp38-cp38-win32.whl", hash = "sha256:3ff07ec89bae51176c0549bc4c63aa6202991da2d9a6129d7aef7f1407d3f295"},
    {file = "PyYAML-6.0.3-cp38-cp38-win_amd64.whl", hash = "sha256:5cf4e27da7e3fbed4d6c3d8e797387aaad68102272f8f9752883bc32d61cb87b"},
    {file = "pyyaml-6.0.3-cp310-cp310-macosx_10_13_x86_64.whl", hash = "sha256:214ed4befebe12df36bcc8bc2b64b396ca31be9304b8f59e25c11cf94a4c033b"},
    {file = "pyyaml-6.0.3-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:02ea2dfa234451bbb8772601d7b8e426c2bfa197136796224e50e35a78777956"},
    {file = "pyyaml-6.0.3-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:b30236e45cf30d2b8e7b3e85881719e98507abed1011bf463a8fa23e9c3e98a8"},
    {file = "pyyaml-6.0.3-cp310-cp310-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:66291b10affd76d76f54fad28e22e51719ef9ba22b29e1d7d03d6777a9174198"},
    {file = "pyyaml-6.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9c7708761fccb9397fe64bbc0395abcae8c4bf7b0eac081e12b809bf47700d0b"},
    {file = "pyyaml-6.0.3-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:418cf3f2111bc80e0933b2cd8cd04f286338bb88bdc7bc8e6dd775ebde60b5e0"},
    {file = "pyyaml-6.0.3-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:5e0b74767e5f8c593e8c9b5912019159ed0533c70051e9cce3e8b6aa699fcd69"},
    {file = "pyyaml-6.0.3-cp310-cp310-win32.whl", hash = "sha256:28c8d926f98f432f88adc23edf2e6d4921ac26fb084b028c733d01868d19007e"},
    {file = "pyyaml-6.0.3-cp310-cp310-win_amd64.whl", hash = "sha256:bdb2c67c6c1390b63c6ff89f210c8fd09d9a1217a465701eac7316313c915e4c"},
    {file = "pyyaml-6.0.3-cp311-cp311-macosx_10_13_x86_64.whl", hash = "sha256:44edc647873928551a01e7a563d7452ccdebee747728c1080d881d68af7b997e"},
    {file = "pyyaml-6.0.3-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:652cb6edd41e718550aad172851962662ff2681490a8a711af6a4d288dd96824"},
    {file = "pyyaml-6.0.3-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:10892704fc220243f5305762e276552a0395f7beb4dbf9b14ec8fd43b57f126c"},
    {file = "pyyaml-6.0.3-cp311-cp311-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:850774a7879607d3a6f50d36d04f00ee69e7fc816450e5f7e58d7f17f1ae5c00"},
    {file = "pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:b8bb0864c5a28024fac8a632c443c87c5aa6f215c0b126c449ae1a150412f31d"},
    {file = "pyyaml-6.0.3-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:1d37d57ad971609cf3c53ba6a7e365e40660e3be0e5175fa9f2365a379d6095a"},
    {file = "pyyaml-6.0.3-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:37503bfbfc9d2c40b344d06b2199cf0e96e97957ab1c1b546fd4f87e53e5d3e4"},
    {file = "pyyaml-6.0.3-cp311-cp311-win32.whl", hash = "sha256:8098f252adfa6c80ab48096053f512f2321f0b998f98150cea9bd23d83e1467b"},
    {file = "pyyaml-6.0.3-cp311-cp311-win_amd64.whl", hash = "sha256:9f3bfb4965eb874431221a3ff3fdcddc7e74e3b07799e0e84ca4a0f867d449bf"},
    {file = "pyyaml-6.0.3-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:7f047e29dcae44602496db43be01ad42fc6f1cc0d8cd6c83d342306c32270196"},
    {file = "pyyaml-6.0.3-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:fc09d0aa354569bc501d4e787133afc08552722d3ab34836a80547331bb5d4a0"},
    {file = "pyyaml-6.0.3-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:9149cad251584d5fb4981be1ecde53a1ca46c891a79788c0df828d2f166bda28"},
    {file = "pyyaml-6.0.3-cp312-cp312-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:5fdec68f91a0c6739b380c83b951e2c72ac0197ace422360e6d5a959d8d97b2c"},
    {file = "pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:ba1cc08a7ccde2d2ec775841541641e4548226580ab850948cbfda66a1befcdc"},
    {file = "pyyaml-6.0.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:8dc52c23056b9ddd46818a57b78404882310fb473d63f17b07d5c40421e47f8e"},
    {file = "pyyaml-6.0.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:41715c910c881bc081f1e8872880d3c650acf13dfa8214bad49ed4cede7c34ea"},
    {file = "pyyaml-6.0.3-cp312-cp312-win32.whl", hash = "sha256:96b533f0e99f6579b3d4d4995707cf36df9100d67e0c8303a0c55b27b5f99bc5"},
    {file = "pyyaml-6.0.3-cp312-cp312-win_amd64.whl", hash = "sha256:5fcd34e47f6e0b794d17de1b4ff496c00986e1c83f7ab2fb8fcfe9616ff7477b"},
    {file = "pyyaml-6.0.3-cp312-cp312-win_arm64.whl", hash = "sha256:64386e5e707d03a7e172c0701abfb7e10f0fb753ee1d773128192742712a98fd"},
    {file = "pyyaml-6.0.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:8da9669d359f02c0b91ccc01cac4a67f16afec0dac22c2ad09f46bee0697eba8"},
    {file = "pyyaml-6.0.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:2283a07e2c21a2aa78d9c4442724ec1eb15f5e42a723b99cb3d822d48f5f7ad1"},
    {file = "pyyaml-6.0.3-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ee2922902c45ae8ccada2c5b501ab86c36525b883eff4255313a253a3160861c"},
    {file = "pyyaml-6.0.3-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:a33284e20b78bd4a18c8c2282d549d10bc8408a2a7ff57653c0cf0b9be0afce5"},
    {file = "pyyaml-6.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0f29edc409a6392443abf94b9cf89ce99889a1dd5376d94316ae5145dfedd5d6"},
    {file = "pyyaml-6.0.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:f7057c9a337546edc7973c0d3ba84ddcdf0daa14533c2065749c9075001090e6"},
    {file = "pyyaml-6.0.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:eda16858a3cab07b80edaf74336ece1f986ba330fdb8ee0d6c0d68fe82bc96be"},
    {file = "pyyaml-6.0.3-cp313-cp313-win32.whl", hash = "sha256:d0eae10f8159e8fdad514efdc92d74fd8d682c933a6dd088030f3834bc8e6b26"},
    {file = "pyyaml-6.0.3-cp313-cp313-win_amd64.whl", hash = "sha256:79005a0d97d5ddabfeeea4cf676af11e647e41d81c9a7722a193022accdb6b7c"},
    {file = "pyyaml-6.0.3-cp313-cp313-win_arm64.whl", hash = "sha256:5498cd1645aa724a7c71c8f378eb29ebe23da2fc0d7a08071d89469bf1d2defb"},
    {file = "pyyaml-6.0.3-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:8d1fab6bb153a416f9aeb4b8763bc0f22a5586065f86f7664fc23339fc1c1fac"},
    {file = "pyyaml-6.0.3-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:34d5fcd24b8445fadc33f9cf348c1047101756fd760b4dacb5c3e99755703310"},
    {file = "pyyaml-6.0.3-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:501a031947e3a9025ed4405a168e6ef5ae3126c59f90ce0cd6f2bfc477be31b7"},
    {file = "pyyaml-6.0.3-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:b3bc83488de33889877a0f2543ade9f70c67d66d9ebb4ac959502e12de895788"},
    {file = "pyyaml-6.0.3-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c458b6d084f9b935061bc36216e8a69a7e293a2f1e68bf956dcd9e6cbcd143f5"},
    {file = "pyyaml-6.0.3-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:7c6610def4f163542a622a73fb39f534f8c101d690126992300bf3207eab9764"},
    {file = "pyyaml-6.0.3-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:5190d403f121660ce8d1d2c1bb2ef1bd05b5f68533fc5c2ea899bd15f4399b35"},
    {file = "pyyaml-6.0.3-cp314-cp314-win_amd64.whl", hash = "sha256:4a2e8cebe2ff6ab7d1050ecd59c25d4c8bd7e6f400f5f82b96557ac0abafd0ac"},
    {file = "pyyaml-6.0.3-cp314-cp314-win_arm64.whl", hash = "sha256:93dda82c9c22deb0a405ea4dc5f2d0cda384168e466364dec6255b293923b2f3"},
    {file = "pyyaml-6.0.3-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:02893d100e99e03eda1c8fd5c441d8c60103fd175728e23e431db1b589cf5ab3"},
    {file = "pyyaml-6.0.3-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:c1ff362665ae507275af2853520967820d9124984e0f7466736aea23d8611fba"},
    {file = "pyyaml-6.0.3-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6adc77889b628398debc7b65c073bcb99c4a0237b248cacaf3fe8a557563ef6c"},
    {file = "pyyaml-6.0.3-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:a80cb027f6b349846a3bf6d73b5e95e782175e52f22108cfa17876aaeff93702"},
    {file = "pyyaml-6.0.3-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:00c4bdeba853cc34e7dd471f16b4114f4162dc03e6b7afcc2128711f0eca823c"},
    {file = "pyyaml-6.0.3-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:66e1674c3ef6f541c35191caae2d429b967b99e02040f5ba928632d9a7f0f065"},
    {file = "pyyaml-6.0.3-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:16249ee61e95f858e83976573de0f5b2893b3677ba71c9dd36b9cf8be9ac6d65"},
    {file = "pyyaml-6.0.3-cp314-cp314t-win_amd64.whl", hash = "sha256:4ad1906908f2f5ae4e5a8ddfce73c320c2a1429ec52eafd27138b7f1cbe341c9"},
    {file = "pyyaml-6.0.3-cp314-cp314t-win_arm64.whl", hash = "sha256:ebc55a14a21cb14062aa4162f906cd962b28e2e9ea38f9b4391244cd8de4ae0b"},
    {file = "pyyaml-6.0.3-cp39-cp39-macosx_10_13_x86_64.whl", hash = "sha256:b865addae83924361678b652338317d1bd7e79b1f4596f96b96c77a5a34b34da"},
    {file = "pyyaml-6.0.3-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:c3355370a2c156cffb25e876646f149d5d68f5e0a3ce86a5084dd0b64a994917"},
    {file = "pyyaml-6.0.3-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:3c5677e12444c15717b902a5798264fa7909e41153cdf9ef7ad571b704a63dd9"},
    {file = "pyyaml-6.0.3-cp39-cp39-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:5ed875a24292240029e4483f9d4a4b8a1ae08843b9c54f43fcc11e404532a8a5"},
    {file = "pyyaml-6.0.3-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0150219816b6a1fa26fb4699fb7daa9caf09eb1999f3b70fb6e786805e80375a"},
    {file = "pyyaml-6.0.3-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:fa160448684b4e94d80416c0fa4aac48967a969efe22931448d853ada8baf926"},
    {file = "pyyaml-6.0.3-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:27c0abcb4a5dac13684a37f76e701e054692a9b2d3064b70f5e4eb54810553d7"},
    {file = "pyyaml-6.0.3-cp39-cp39-win32.whl", hash = "sha256:1ebe39cb5fc479422b83de611d14e2c0d3bb2a18bbcb01f229ab3cfbd8fee7a0"},
    {file = "pyyaml-6.0.3-cp39-cp39-win_amd64.whl", hash = "sha256:2e71d11abed7344e42a8849600193d15b6def118602c4c176f748e4583246007"},
    {file = "pyyaml-6.0.3.tar.gz", hash = "sha256:d76623373421df22fb4cf8817020cbb7ef15c725b9d5e45f17e189bfc384190f"},
]

[[package]]
name = "rich"
version = "14.3.1"
description = "Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal"
optional = false
python-versions = ">=3.8.0"
groups = ["dev"]
files = [
    {file = "rich-14.3.1-py3-none-any.whl", hash = "sha256:da750b1aebbff0b372557426fb3f35ba56de8ef954b3190315eb64076d6fb54e"},
    {file = "rich-14.3.1.tar.gz", hash = "sha256:b8c5f568a3a749f9290ec6bddedf835cec33696bfc1e48bcfecb276c7386e4b8"},
]

[package.dependencies]
markdown-it-py = ">=2.2.0"
pygments = ">=2.13.0,<3.0.0"

[package.extras]
jupyter = ["ipywidgets (>=7.5.1,<9)"]

[[package]]
name = "setuptools"
version = "80.10.1"
description = "Easily download, build, install, upgrade, and uninstall Python packages"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "setuptools-80.10.1-py3-none-any.whl", hash = "sha256:fc30c51cbcb8199a219c12cc9c281b5925a4978d212f84229c909636d9f6984e"},
    {file = "setuptools-80.10.1.tar.gz", hash = "sha256:bf2e513eb8144c3298a3bd28ab1a5edb739131ec5c22e045ff93cd7f5319703a"},
]

[package.extras]
check = ["pytest-checkdocs (>=2.4)", "pytest-ruff (>=0.2.1) ; sys_platform != \"cygwin\"", "ruff (>=0.8.0) ; sys_platform != \"cygwin\""]
core = ["importlib_metadata (>=6) ; python_version < \"3.10\"", "jaraco.functools (>=4)", "jaraco.text (>=3.7)", "more_itertools", "more_itertools (>=8.8)", "packaging (>=24.2)", "platformdirs (>=4.2.2)", "tomli (>=2.0.1) ; python_version < \"3.11\"", "wheel (>=0.43.0)"]
cover = ["pytest-cov"]
doc = ["furo", "jaraco.packaging (>=9.3)", "jaraco.tidelift (>=1.4)", "pygments-github-lexers (==0.0.5)", "pyproject-hooks (!=1.1)", "rst.linker (>=1.9)", "sphinx (>=3.5)", "sphinx-favicon", "sphinx-inline-tabs", "sphinx-lint", "sphinx-notfound-page (>=1,<2)", "sphinx-reredirects", "sphinxcontrib-towncrier", "towncrier (<24.7)"]
enabler = ["pytest-enabler (>=2.2)"]
test = ["build[virtualenv] (>=1.0.3)", "filelock (>=3.4.0)", "ini2toml[lite] (>=0.14)", "jaraco.develop (>=7.21) ; python_version >= \"3.9\" and sys_platform != \"cygwin\"", "jaraco.envs (>=2.2)", "jaraco.path (>=3.7.2)", "jaraco.test (>=5.5)", "packaging (>=24.2)", "pip (>=19.1)", "pyobjc (<12) ; sys_platform == \"darwin\" and python_version <= \"3.9\"", "pyproject-hooks (!=1.1)", "pytest (>=6,!=8.1.*)", "pytest-home (>=0.5)", "pytest-perf ; sys_platform != \"cygwin\"", "pytest-subprocess", "pytest-timeout", "pytest-xdist (>=3)", "tomli-w (>=1.0.0)", "virtualenv (>=13.0.0)", "wheel (>=0.44.0)"]
type = ["importlib_metadata (>=7.0.2) ; python_version < \"3.10\"", "jaraco.develop (>=7.21) ; sys_platform != \"cygwin\"", "mypy (==1.14.*)", "pytest-mypy"]

[[package]]
name = "snowballstemmer"
version = "3.0.1"
description = "This package provides 32 stemmers for 30 languages generated from Snowball algorithms."
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*"
groups = ["dev"]
files = [
    {file = "snowballstemmer-3.0.1-py3-none-any.whl", hash = "sha256:6cd7b3897da8d6c9ffb968a6781fa6532dce9c3618a4b127d920dab764a19064"},
    {file = "snowballstemmer-3.0.1.tar.gz", hash = "sha256:6d5eeeec8e9f84d4d56b847692bacf79bc2c8e90c7f80ca4444ff8b6f2e52895"},
]

[[package]]
name = "stevedore"
version = "5.6.0"
description = "Manage dynamic plugins for Python applications"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "stevedore-5.6.0-py3-none-any.whl", hash = "sha256:4a36dccefd7aeea0c70135526cecb7766c4c84c473b1af68db23d541b6dc1820"},
    {file = "stevedore-5.6.0.tar.gz", hash = "sha256:f22d15c6ead40c5bbfa9ca54aa7e7b4a07d59b36ae03ed12ced1a54cf0b51945"},
]

[[package]]
name = "toml"
version = "0.10.2"
description = "Python Library for Tom's Obvious, Minimal Language"
optional = false
python-versions = ">=2.6, !=3.0.*, !=3.1.*, !=3.2.*"
groups = ["dev"]
files = [
    {file = "toml-0.10.2-py2.py3-none-any.whl", hash = "sha256:806143ae5bfb6a3c6e736a764057db0e6a0e05e338b5630894a5f779cabb4f9b"},
    {file = "toml-0.10.2.tar.gz", hash = "sha256:b3bda1d108d5dd99f4a20d24d9c348e91c4db7ab1b749200bded2f839ccbe68f"},
]

[[package]]
name = "tomli"
version = "2.4.0"
description = "A lil' TOML parser"
optional = false
python-versions = ">=3.8"
groups = ["main", "dev"]
files = [
    {file = "tomli-2.4.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:b5ef256a3fd497d4973c11bf142e9ed78b150d36f5773f1ca6088c230ffc5867"},
    {file = "tomli-2.4.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:5572e41282d5268eb09a697c89a7bee84fae66511f87533a6f88bd2f7b652da9"},
    {file = "tomli-2.4.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:551e321c6ba03b55676970b47cb1b73f14a0a4dce6a3e1a9458fd6d921d72e95"},
    {file = "tomli-2.4.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5e3f639a7a8f10069d0e15408c0b96a2a828cfdec6fca05296ebcdcc28ca7c76"},
    {file = "tomli-2.4.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:1b168f2731796b045128c45982d3a4874057626da0e2ef1fdd722848b741361d"},
    {file = "tomli-2.4.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:133e93646ec4300d651839d382d63edff11d8978be23da4cc106f5a18b7d0576"},
    {file = "tomli-2.4.0-cp311-cp311-win32.whl", hash = "sha256:b6c78bdf37764092d369722d9946cb65b8767bfa4110f902a1b2542d8d173c8a"},
    {file = "tomli-2.4.0-cp311-cp311-win_amd64.whl", hash = "sha256:d3d1654e11d724760cdb37a3d7691f0be9db5fbdaef59c9f532aabf87006dbaa"},
    {file = "tomli-2.4.0-cp311-cp311-win_arm64.whl", hash = "sha256:cae9c19ed12d4e8f3ebf46d1a75090e4c0dc16271c5bce1c833ac168f08fb614"},
    {file = "tomli-2.4.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:920b1de295e72887bafa3ad9f7a792f811847d57ea6b1215154030cf131f16b1"},
    {file = "tomli-2.4.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:7d6d9a4aee98fac3eab4952ad1d73aee87359452d1c086b5ceb43ed02ddb16b8"},
    {file = "tomli-2.4.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:36b9d05b51e65b254ea6c2585b59d2c4cb91c8a3d91d0ed0f17591a29aaea54a"},
    {file = "tomli-2.4.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1c8a885b370751837c029ef9bc014f27d80840e48bac415f3412e6593bbc18c1"},
    {file = "tomli-2.4.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:8768715ffc41f0008abe25d808c20c3d990f42b6e2e58305d5da280ae7d1fa3b"},
    {file = "tomli-2.4.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:7b438885858efd5be02a9a133caf5812b8776ee0c969fea02c45e8e3f296ba51"},
    {file = "tomli-2.4.0-cp312-cp312-win32.whl", hash = "sha256:0408e3de5ec77cc7f81960c362543cbbd91ef883e3138e81b729fc3eea5b9729"},
    {file = "tomli-2.4.0-cp312-cp312-win_amd64.whl", hash = "sha256:685306e2cc7da35be4ee914fd34ab801a6acacb061b6a7abca922aaf9ad368da"},
    {file = "tomli-2.4.0-cp312-cp312-win_arm64.whl", hash = "sha256:5aa48d7c2356055feef06a43611fc401a07337d5b006be13a30f6c58f869e3c3"},
    {file = "tomli-2.4.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:84d081fbc252d1b6a982e1870660e7330fb8f90f676f6e78b052ad4e64714bf0"},
    {file = "tomli-2.4.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:9a08144fa4cba33db5255f9b74f0b89888622109bd2776148f2597447f92a94e"},
    {file = "tomli-2.4.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c73add4bb52a206fd0c0723432db123c0c75c280cbd67174dd9d2db228ebb1b4"},
    {file = "tomli-2.4.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1fb2945cbe303b1419e2706e711b7113da57b7db31ee378d08712d678a34e51e"},
    {file = "tomli-2.4.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:bbb1b10aa643d973366dc2cb1ad94f99c1726a02343d43cbc011edbfac579e7c"},
    {file = "tomli-2.4.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:4cbcb367d44a1f0c2be408758b43e1ffb5308abe0ea222897d6bfc8e8281ef2f"},
    {file = "tomli-2.4.0-cp313-cp313-win32.whl", hash = "sha256:7d49c66a7d5e56ac959cb6fc583aff0651094ec071ba9ad43df785abc2320d86"},
    {file = "tomli-2.4.0-cp313-cp313-win_amd64.whl", hash = "sha256:3cf226acb51d8f1c394c1b310e0e0e61fecdd7adcb78d01e294ac297dd2e7f87"},
    {file = "tomli-2.4.0-cp313-cp313-win_arm64.whl", hash = "sha256:d20b797a5c1ad80c516e41bc1fb0443ddb5006e9aaa7bda2d71978346aeb9132"},
    {file = "tomli-2.4.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:26ab906a1eb794cd4e103691daa23d95c6919cc2fa9160000ac02370cc9dd3f6"},
    {file = "tomli-2.4.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:20cedb4ee43278bc4f2fee6cb50daec836959aadaf948db5172e776dd3d993fc"},
    {file = "tomli-2.4.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:39b0b5d1b6dd03684b3fb276407ebed7090bbec989fa55838c98560c01113b66"},
    {file = "tomli-2.4.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a26d7ff68dfdb9f87a016ecfd1e1c2bacbe3108f4e0f8bcd2228ef9a766c787d"},
    {file = "tomli-2.4.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:20ffd184fb1df76a66e34bd1b36b4a4641bd2b82954befa32fe8163e79f1a702"},
    {file = "tomli-2.4.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:75c2f8bbddf170e8effc98f5e9084a8751f8174ea6ccf4fca5398436e0320bc8"},
    {file = "tomli-2.4.0-cp314-cp314-win32.whl", hash = "sha256:31d556d079d72db7c584c0627ff3a24c5d3fb4f730221d3444f3efb1b2514776"},
    {file = "tomli-2.4.0-cp314-cp314-win_amd64.whl", hash = "sha256:43e685b9b2341681907759cf3a04e14d7104b3580f808cfde1dfdb60ada85475"},
    {file = "tomli-2.4.0-cp314-cp314-win_arm64.whl", hash = "sha256:3d895d56bd3f82ddd6faaff993c275efc2ff38e52322ea264122d72729dca2b2"},
    {file = "tomli-2.4.0-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:5b5807f3999fb66776dbce568cc9a828544244a8eb84b84b9bafc080c99597b9"},
    {file = "tomli-2.4.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:c084ad935abe686bd9c898e62a02a19abfc9760b5a79bc29644463eaf2840cb0"},
    {file = "tomli-2.4.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0f2e3955efea4d1cfbcb87bc321e00dc08d2bcb737fd1d5e398af111d86db5df"},
    {file = "tomli-2.4.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0e0fe8a0b8312acf3a88077a0802565cb09ee34107813bba1c7cd591fa6cfc8d"},
    {file = "tomli-2.4.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:413540dce94673591859c4c6f794dfeaa845e98bf35d72ed59636f869ef9f86f"},
    {file = "tomli-2.4.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:0dc56fef0e2c1c470aeac5b6ca8cc7b640bb93e92d9803ddaf9ea03e198f5b0b"},
    {file = "tomli-2.4.0-cp314-cp314t-win32.whl", hash = "sha256:d878f2a6707cc9d53a1be1414bbb419e629c3d6e67f69230217bb663e76b5087"},
    {file = "tomli-2.4.0-cp314-cp314t-win_amd64.whl", hash = "sha256:2add28aacc7425117ff6364fe9e06a183bb0251b03f986df0e78e974047571fd"},
    {file = "tomli-2.4.0-cp314-cp314t-win_arm64.whl", hash = "sha256:2b1e3b80e1d5e52e40e9b924ec43d81570f0e7d09d11081b797bc4692765a3d4"},
    {file = "tomli-2.4.0-py3-none-any.whl", hash = "sha256:1f776e7d669ebceb01dee46484485f43a4048746235e683bcdffacdf1fb4785a"},
    {file = "tomli-2.4.0.tar.gz", hash = "sha256:aa89c3f6c277dd275d8e243ad24f3b5e701491a860d5121f2cdd399fbb31fc9c"},
]
markers = {main = "python_version == \"3.10\"", dev = "python_full_version <= \"3.11.0a6\""}

[[package]]
name = "tomli-w"
version = "1.2.0"
description = "A lil' TOML writer"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "tomli_w-1.2.0-py3-none-any.whl", hash = "sha256:188306098d013b691fcadc011abd66727d3c414c571bb01b1a174ba8c983cf90"},
    {file = "tomli_w-1.2.0.tar.gz", hash = "sha256:2dd14fac5a47c27be9cd4c976af5a12d87fb1f0b4512f81d69cce3b35ae25021"},
]

[[package]]
name = "tox"
version = "4.56.1"
description = "tox is a generic virtualenv management and test command line tool"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "tox-4.56.1-py3-none-any.whl", hash = "sha256:4d06b925c4dd67872099b39c5a46fba79a2169c5f6e32060f95a8b1181f0ef55"},
    {file = "tox-4.56.1.tar.gz", hash = "sha256:db1c2610802553189cf40de251661d066a635ee0ed9bf2a60093b5f1a7f36ef8"},
]

[package.dependencies]
cachetools = ">=7.0.3"
colorama = ">=0.4.6"
filelock = ">=3.25"
packaging = ">=26"
platformdirs = ">=4.9.4"
pluggy = ">=1.6"
pyproject-api = ">=1.10"
python-discovery = ">=1.2.2"
tomli = {version = ">=2.4", markers = "python_version < \"3.11\""}
tomli-w = ">=1.2"
typing-extensions = {version = ">=4.15", markers = "python_version < \"3.11\""}
virtualenv = ">=21.1"

[package.extras]
completion = ["argcomplete (>=3.6.3)"]
testing = ["devpi-process (>=1.1.1)", "pytest (>=9.0.2)", "pytest-mock (>=3.15.1)"]

[[package]]
name = "traceloggingdynamic"
version = "1.0.1"
description = "Generates Event Tracing for Windows events using TraceLogging"
optional = false
python-versions = ">=3.6"
groups = ["main", "dev"]
markers = "sys_platform == \"win32\""
files = [
    {file = "traceloggingdynamic-1.0.1-py3-none-any.whl", hash = "sha256:0e19da491a8960725b3622366487ae35f49d8f595bb2e4e5ce1795eb5928db7c"},
    {file = "traceloggingdynamic-1.0.1.tar.gz", hash = "sha256:d9dd4b291dd04c15e34181eed06f73fdf4ffa7b1f895b78217163def48ab1a52"},
]

[[package]]
name = "types-grpcio"
version = "1.0.0.20260614"
description = "Typing stubs for grpcio"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "types_grpcio-1.0.0.20260614-py3-none-any.whl", hash = "sha256:050472cb4ef329ae8fe20278c62bc0da5b961aad3dd889cc35f6e0c70d368dae"},
    {file = "types_grpcio-1.0.0.20260614.tar.gz", hash = "sha256:e86d1aabb7e7eedae487c3ac10e010a13d5db1fd350e766562053af557366aab"},
]

[[package]]
name = "types-protobuf"
version = "7.34.1.20260518"
description = "Typing stubs for protobuf"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "types_protobuf-7.34.1.20260518-py3-none-any.whl", hash = "sha256:a0a5337413347166439c0e07cbc26c6164d091401c6f01b1dfd8cdb966c4dd8f"},
    {file = "types_protobuf-7.34.1.20260518.tar.gz", hash = "sha256:28cfaded25889cb83ebfb63cfb0a43628f0b6f3785767bec17287dc6468795f2"},
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
description = "Backported and Experimental Type Hints for Python 3.9+"
optional = false
python-versions = ">=3.9"
groups = ["main", "dev"]
files = [
    {file = "typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548"},
    {file = "typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466"},
]

[[package]]
name = "virtualenv"
version = "21.3.0"
description = "Virtual Python Environment builder"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "virtualenv-21.3.0-py3-none-any.whl", hash = "sha256:4d28ee41f6d9ec8f1f00cd472b9ffbcedda1b3d3b9a575b5c94a2d004fd51bd7"},
    {file = "virtualenv-21.3.0.tar.gz", hash = "sha256:733750db978ec95c2d8eb4feadaa57091002bce404cb39ba69899cf7bd28944e"},
]

[package.dependencies]
distlib = ">=0.3.7,<1"
filelock = {version = ">=3.24.2,<4", markers = "python_version >= \"3.10\""}
platformdirs = ">=3.9.1,<5"
python-discovery = ">=1.2.2"
typing-extensions = {version = ">=4.13.2", markers = "python_version < \"3.11\""}

[metadata]
lock-version = "2.1"
python-versions = "^3.10"
content-hash = "b2f64c555e4d71bbceb76c12d54ae0a02d0b3a0e5914005c1929d94dbcd9fb17"
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/poetry.toml sha256=409e7bde0fba7b77ee0d840cc3efd55fd0500e90dd2b962c1a50d043d98d502e bytes=797 -->
## FILE: packages/generator/poetry.toml

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/poetry.toml`
- sha256: `409e7bde0fba7b77ee0d840cc3efd55fd0500e90dd2b962c1a50d043d98d502e`
- bytes: 797

````toml
[virtualenvs]
in-project = true

[solver]
# Set min-release-age to 2 weeks, same as in https://github.com/ni/python-renovate-config
min-release-age = 14
min-release-age-exclude = [
    "hightime",
    "ni-grpc-extensions",
    "ni-grpcdevice-v1-proto",
    "ni-measurement-plugin-sdk-service",
    "ni-measurementlink-discovery-v1-client",
    "ni-measurementlink-discovery-v1-proto",
    "ni-measurementlink-measurement-v1-proto",
    "ni-measurementlink-measurement-v2-proto",
    "ni-measurementlink-pinmap-v1-client",
    "ni-measurementlink-pinmap-v1-proto",
    "ni-measurementlink-proto",
    "ni-measurementlink-sessionmanagement-v1-client",
    "ni-measurementlink-sessionmanagement-v1-proto",
    "ni-protobuf-types",
    "ni-python-styleguide",
    "nitypes",
]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/pyproject.toml sha256=9f289738329e470464ac115f44aaa55cc01a1e14199a835b23859e0f5f83f29e bytes=4006 -->
## FILE: packages/generator/pyproject.toml

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/pyproject.toml`
- sha256: `9f289738329e470464ac115f44aaa55cc01a1e14199a835b23859e0f5f83f29e`
- bytes: 4006

````toml
[tool.poetry]
name = "ni_measurement_plugin_sdk_generator"
version = "3.2.0.dev0"
description = "Measurement Plug-In Code Generator for Python"
authors = ["NI <opensource@ni.com>"]
readme = "README.md"
repository = "https://github.com/ni/measurement-plugin-python/"
license = "MIT"
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: Manufacturing",
    "Intended Audience :: Science/Research",
    "Operating System :: Microsoft :: Windows",
    # Poetry automatically adds classifiers for the license and the supported Python versions.
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Scientific/Engineering",
    "Topic :: System :: Hardware",
]

[tool.poetry.dependencies]
python = "^3.10"
Mako = "^1.2.1"
click = ">=8.1.3"
grpcio = "^1.49.1"
protobuf = ">=4.21"
black = ">=24.8.0"
click-option-group = ">=0.5.6"
ni-grpc-extensions =  { version = "^1.0.0" }
ni-grpcdevice-v1-proto = { version = "^1.0.0" }
ni-measurement-plugin-sdk-service = { version = ">=2.2.0" }
ni-measurementlink-discovery-v1-client = { version = "^1.0.0" }
ni-measurementlink-pinmap-v1-client = { version = "^1.0.0" }
ni-protobuf-types = { version = "^1.0.0" }

[tool.poetry.group.dev.dependencies]
pytest = ">=7.2.0"
pytest-cov = ">=3.0.0"
ni-python-styleguide = ">=0.4.1"
mypy = ">=1.0"
# mypy-protobuf 3.6 is the last version that supports protobuf v4.
mypy-protobuf = [
  # requires protobuf v4 or later
  {version = ">=3.4,<3.7", python = ">=3.10,<3.14"},
  # requires protobuf v6 or later
  {version = ">=3.4", python = "^3.14"}
]
types-protobuf = ">=4.21"
types-grpcio = ">=1.0"
# During development, use file paths to reference the latest source for packages
# in the same Git repository.
ni-measurement-plugin-sdk-service = {path = "../../packages/service", develop = true}
bandit = { version = ">=1.7", extras = ["toml"] }
tox = ">=4.0"
grpcio-tools = [
  # requires protobuf v4 or later
  {version = "1.49.1", python = ">=3.10,<3.12"},
  {version = "1.59.0", python = ">=3.12,<3.13"},
  # requires protobuf v5 or later
  {version = "1.67.0", python = ">=3.13,<3.14"},
  # requires protobuf v6 or later
  {version = "1.75.1", python = "^3.14"},
]
# NumPy dropped support for Python 3.8 before adding support for Python 3.12, so
# we need to include multiple NumPy versions in poetry.lock.
numpy = [
  { version = ">=1.22", python = ">=3.10,<3.12"},
  { version = ">=1.26", python = ">=3.12,<3.13"},
  { version = ">=2.1", python = "^3.13"},
]
ni-measurementlink-proto = { version = "^1.0.0" }

[tool.poetry.scripts]
ni-measurement-plugin-generator = "ni_measurement_plugin_sdk_generator.plugin:create_measurement"
ni-measurement-plugin-client-generator = "ni_measurement_plugin_sdk_generator.client:create_client"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.black]
extend_exclude = '\.tox/|_pb2(_grpc)?\.(py|pyi)$'
line-length = 100

[tool.ni-python-styleguide]
extend_exclude = 'tests/test_assets/example_renders/,.tox/,*_pb2_grpc.py,*_pb2_grpc.pyi,*_pb2.py,*_pb2.pyi'

[tool.mypy]
files = "ni_measurement_plugin_sdk_generator/,tests/"
exclude = "^tests/test_assets/"
disallow_untyped_defs = true
namespace_packages = true
warn_redundant_casts = true
warn_unused_configs = true
warn_unused_ignores = true

[[tool.mypy.overrides]]
module = "mako.*"
ignore_missing_imports = true

[[tool.mypy.overrides]]
# mypy-protobuf codegen has some unused ignores.
module = "tests.utilities.measurements.non_streaming_data_measurement._stubs.*"
warn_unused_ignores = false

[tool.pytest.ini_options]
addopts = "--doctest-modules --ignore tests/test_assets --strict-markers"
filterwarnings = ["always::ImportWarning", "always::ResourceWarning"]
testpaths = ["tests"]

[tool.bandit]
skips = [
  "B101", # assert_used
  "B702", # use_of_mako_templates
]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/README.md sha256=31826d8353a392a8fd684b9d1f3cbd9abbcddf47c793b93dcd42ffd64f821b0b bytes=7104 -->
## FILE: packages/generator/README.md

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/README.md`
- sha256: `31826d8353a392a8fd684b9d1f3cbd9abbcddf47c793b93dcd42ffd64f821b0b`
- bytes: 7104

````markdown
# Measurement Plug-In SDK Generator for Python

- [Measurement Plug-In SDK Generator for Python](#measurement-plug-in-sdk-generator-for-python)
  - [Introduction](#introduction)
  - [Dependencies](#dependencies)
  - [Developing Measurements: Quick Start](#developing-measurements-quick-start)
  - [Generating Measurement Clients: Quick Start](#generating-measurement-clients-quick-start)
    - [Installation](#installation)
    - [Generating a Minimal Python Measurement Client](#generating-a-minimal-python-measurement-client)
  - [Steps to Run/Debug the Measurement Client](#steps-to-rundebug-the-measurement-client)

---

## Introduction

Measurement Plug-In SDK Generator for Python (`ni-measurement-plugin-sdk-generator`) is a Python package containing tools for generating reusable measurement plug-ins and clients.

- `ni-measurement-plugin-generator` is a command for generating measurement plug-ins using gRPC services.
- `ni-measurement-plugin-client-generator` is a command for generating plug-in clients to interact with the measurement plug-ins.

---

## Dependencies

- [Python >= 3.10](https://www.python.org/downloads/release/python-3100/)
- [mako >= 1.2.1, < 2.x](https://pypi.org/project/Mako/1.2.1/)
- [click >= 8.1.3](https://pypi.org/project/click/8.1.3/)

---

## Developing Measurements: Quick Start

For installation and usage, see [Measurement Plug-In SDK Service for Python - Developing Measurements: Quick Start](https://pypi.org/project/ni_measurement_plugin_sdk_service/#developing-measurements-quick-start) section.

---

## Generating Measurement Clients: Quick Start

This section provides instructions to generate custom measurement clients in Python using Measurement Plug-In SDK for Python.

### Installation

Make sure the system has the recommended Python version installed. Install Measurement Plug-In SDK for Python using [pip](https://pip.pypa.io/).

``` cmd
REM Activate the required virtual environment if any.
pip install ni-measurement-plugin-sdk
```

Check if you have installed the expected version of Measurement Plug-In SDK for Python installed by running the below command:

```cmd
pip show ni-measurement-plugin-sdk
```

### Generating a Minimal Python Measurement Client

Run the `ni-measurement-plugin-client-generator` tool.

1. To create measurement clients for specific measurements, use this command with optional arguments:

    ```ni-measurement-plugin-client-generator --measurement-service-class "ni.examples.SampleMeasurement_Python" [--module-name "sample_measurement_client"]  [--class-name "SampleMeasurementClient"] [--directory-out <new_path_for_created_files>]```

    - `--measurement-service-class` specifies the measurement service class for which the client is being generated.

    - Optional arguments:
        - `--module-name` and `--class-name` define the module and class names of the generated client. If not specified, they are derived from the measurement service class name.

        - `--directory-out` specifies the output directory for the generated files. If not specified, files are placed in the current directory.
        
    > **Note**: When generating multiple measurement clients, `--module-name` and `--class-name` are ignored and derived from the service class of each measurement. So, ensure that the measurement service class name adheres to proper naming conventions.

2. To create measurement clients for all registered measurements, use this command:

    `ni-measurement-plugin-client-generator --all [--directory-out <new_path_for_created_files>]`

3. To interactively create measurement clients for any registered measurements, use this command:

    `ni-measurement-plugin-client-generator --interactive`

The generated client includes four APIs: `measure`, `stream_measure`, `register_pin_map`, and `cancel`. The usage of these APIs is discussed in the ["Steps to Run/Debug the Measurement Client"](#steps-to-rundebug-the-measurement-client) section.

> **Note**:
> - The Measurement Plug-In Client is compatible with all datatypes supported by the Measurement Plug-In.
> - The Double XY datatype is not supported for measurement configurations (inputs).
> - For Enum datatypes, the generated enum class names will be the measurement parameter name suffixed with 'Enum'. For instance, if the measurement parameter name is 'Enum In', the generated enum in the client will be `EnumInEnum'.
> - Ring control in LabVIEW measurements will be represented as numeric datatypes in the generated client.

---

## Steps to Run/Debug the Measurement Client

1. Make sure the required measurement service is running before interacting with it via the client.

2. Use the client APIs from the ["Generating a Minimal Python Measurement Client"](#generating-a-minimal-python-measurement-client) section.

    1. For non-streaming measurements, use the `measure` method.

        ``` python
        from sample_measurement_client import SampleMeasurementClient
        
        client = SampleMeasurementClient()
        outputs = client.measure()
        print(outputs)
        ```

    2. For streaming measurements, use the `stream_measure` method.

        ``` python
        from sample_measurement_client import SampleMeasurementClient
        
        client = SampleMeasurementClient()
        outputs_itr = client.stream_measure()
        for index, outputs in enumerate(outputs_itr):
            print(f"outputs[{index}] = {outputs}")
        ```

    3. If a measurement requires a pin map, it can be registered using the `register_pin_map` method. By default, `sites` is set to [0].

        ``` python
        from sample_measurement_client import SampleMeasurementClient
        
        client = SampleMeasurementClient()
        client.register_pin_map(pin_map_path)
        outputs = client.measure()
        print(outputs)
        ```
        - Alternatively, when calling a measurement service from another measurement, you can pass the first measurement's pin map context to the second measurement's pin map context through the `pin_map_context` property. Sites can also be provided through the `sites` property.

        ``` python
        from sample_measurement_client import SampleMeasurementClient
        
        client = SampleMeasurementClient()
        client.pin_map_context = available_pin_map_context
        client.sites = [0, 1]
        outputs = client.measure()
        print(outputs)
        ```

    4. Cancel an ongoing `measure` or `stream_measure` call using the `cancel` method.

        ``` python
        from concurrent.futures import ThreadPoolExecutor
        from sample_measurement_client import SampleMeasurementClient
        
        client = SampleMeasurementClient()
        with ThreadPoolExecutor() as executor:
            future = executor.submit(client.measure)
            client.cancel()
            outputs = future.result()  # Raises grpc.RpcException with status code "CANCELLED" 
        ```

---
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/scripts/generate_grpc_stubs.py sha256=f6759171343204f61a70f1ae08e720d54d061e10d1a51211efd51fa4186b4a5c bytes=3261 -->
## FILE: packages/generator/scripts/generate_grpc_stubs.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/scripts/generate_grpc_stubs.py`
- sha256: `f6759171343204f61a70f1ae08e720d54d061e10d1a51211efd51fa4186b4a5c`
- bytes: 3261

````python
#!/usr/bin/env python3
"""Generates gRPC Python stubs from proto files."""

import pathlib
from collections.abc import Sequence

import grpc_tools.protoc
import pkg_resources

STUBS_NAMESPACE = "tests.utilities.measurements.non_streaming_data_measurement._stubs"
PROTO_PARENT_NAMESPACES = ["ni.measurementlink", "nidevice_grpc", "ni.protobuf.types"]
STUBS_PATH = pathlib.Path(__file__).parent.parent / STUBS_NAMESPACE.replace(".", "/")
STUBS_PROTO_PATH = STUBS_PATH
STUBS_PROTO_FILES = list(STUBS_PROTO_PATH.rglob("*.proto"))


def main():
    """Generate and fixup gRPC Python stubs."""
    generate_python_files(STUBS_PATH, STUBS_PROTO_PATH, STUBS_PROTO_FILES)
    fix_import_paths(STUBS_PROTO_PATH, STUBS_PATH, STUBS_NAMESPACE, PROTO_PARENT_NAMESPACES)


def generate_python_files(
    stubs_path: pathlib.Path,
    proto_path: pathlib.Path,
    proto_files: Sequence[pathlib.Path],
):
    """Generate python files from .proto files with protoc."""
    arguments = [
        "protoc",
        f"--proto_path={str(proto_path)}",
        f"--proto_path={pkg_resources.resource_filename('grpc_tools', '_proto')}",
        f"--python_out={str(stubs_path)}",
        f"--mypy_out={str(stubs_path)}",
        f"--grpc_python_out={str(stubs_path)}",
        f"--mypy_grpc_out={str(stubs_path)}",
    ]

    arguments += [str(path.relative_to(proto_path)).replace("\\", "/") for path in proto_files]

    grpc_tools.protoc.main(arguments)


def fix_import_paths(
    protos_path: pathlib.Path,
    stubs_path: pathlib.Path,
    stubs_namespace: str,
    proto_parent_namespaces: Sequence[str],
):
    """Fix import paths of generated files."""
    print("Fixing import paths")
    grpc_codegened_file_paths = list(protos_path.rglob("*pb2*py"))
    stubs_codegened_file_paths = list(stubs_path.rglob("*pb2*py"))
    imports_to_fix = [path.stem for path in stubs_codegened_file_paths if path.parent == stubs_path]
    imports_to_alias = [
        ".".join(path.relative_to(stubs_path).with_suffix("").parts)
        for path in stubs_codegened_file_paths
        if path.stem not in imports_to_fix
    ]
    grpc_codegened_file_paths.extend(protos_path.rglob("*pb2*pyi"))
    for path in grpc_codegened_file_paths:
        print(f"Processing {path}")
        data = path.read_bytes()
        for name in imports_to_fix:
            data = data.replace(
                f"import {name}".encode(), f"from {stubs_namespace} import {name}".encode()
            )
        for namespace in proto_parent_namespaces:
            data = data.replace(
                f"from {namespace}".encode(),
                f"from {stubs_namespace}.{namespace}".encode(),
            )
        if path.suffix == ".pyi":
            for name in imports_to_alias:
                alias = name.replace(".", "_")
                data = data.replace(
                    f"import {name}\n".encode(),
                    f"import {stubs_namespace}.{name} as {alias}\n".encode(),
                )
                data = data.replace(
                    f"{name}.".encode(),
                    f"{alias}.".encode(),
                )
        path.write_bytes(data)


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/__init__.py sha256=14a272de191ef5de47d1830c42c5fc79bdb7eaeab8b953e425ddf03e5d7c269a bytes=14 -->
## FILE: packages/generator/tests/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/__init__.py`
- sha256: `14a272de191ef5de47d1830c42c5fc79bdb7eaeab8b953e425ddf03e5d7c269a`
- bytes: 14

````python
"""Tests."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/acceptance/test_client_generator.py sha256=74173297fa58fe45d674c40f553b845a3922e17ba14348820e3f33ca4563e1e1 bytes=9597 -->
## FILE: packages/generator/tests/acceptance/test_client_generator.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/acceptance/test_client_generator.py`
- sha256: `74173297fa58fe45d674c40f553b845a3922e17ba14348820e3f33ca4563e1e1`
- bytes: 9597

````python
import os
import pathlib
import re
import sys
from collections.abc import Generator

import mypy.api
import pytest
from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService

from tests.conftest import CliRunnerFunction
from tests.utilities.discovery_service_process import DiscoveryServiceProcess
from tests.utilities.measurements import (
    non_streaming_data_measurement,
    streaming_data_measurement,
    void_measurement,
    localized_measurement,
)


def test___non_streaming_measurement___create_client___render_without_error(
    create_client: CliRunnerFunction,
    test_assets_directory: pathlib.Path,
    tmp_path_factory: pytest.TempPathFactory,
    non_streaming_measurement_service: MeasurementService,
) -> None:
    temp_directory = tmp_path_factory.mktemp("measurement_plugin_client_files")
    module_name = "non_streaming_data_measurement_client"
    golden_path = test_assets_directory / "example_renders" / "measurement_plugin_client"
    filename = f"{module_name}.py"

    result = create_client(
        [
            "--measurement-service-class",
            "ni.tests.NonStreamingDataMeasurement_Python",
            "--module-name",
            module_name,
            "--class-name",
            "NonStreamingDataMeasurementClient",
            "--directory-out",
            str(temp_directory),
        ]
    )

    assert result.exit_code == 0
    _assert_equal(
        golden_path / filename,
        temp_directory / filename,
    )


def test___void_measurement___create_client___render_without_error(
    create_client: CliRunnerFunction,
    test_assets_directory: pathlib.Path,
    tmp_path_factory: pytest.TempPathFactory,
    void_measurement_service: MeasurementService,
) -> None:
    temp_directory = tmp_path_factory.mktemp("measurement_plugin_client_files")
    module_name = "void_measurement_client"
    golden_path = test_assets_directory / "example_renders" / "measurement_plugin_client"
    filename = f"{module_name}.py"

    result = create_client(
        [
            "--measurement-service-class",
            "ni.tests.VoidMeasurement_Python",
            "--module-name",
            module_name,
            "--class-name",
            "VoidMeasurementClient",
            "--directory-out",
            str(temp_directory),
        ]
    )

    assert result.exit_code == 0
    _assert_equal(
        golden_path / filename,
        temp_directory / filename,
    )


def test___localized_measurement___create_client___render_without_error(
    create_client: CliRunnerFunction,
    test_assets_directory: pathlib.Path,
    tmp_path_factory: pytest.TempPathFactory,
    localized_measurement_service: MeasurementService,
) -> None:
    temp_directory = tmp_path_factory.mktemp("measurement_plugin_client_files")
    module_name = "localized_measurement_client"
    golden_path = test_assets_directory / "example_renders" / "measurement_plugin_client"
    filename = f"{module_name}.py"

    result = create_client(
        [
            "--measurement-service-class",
            "ni.tests.LocalizedMeasurement_Python",
            "--module-name",
            module_name,
            "--class-name",
            "LocalizedMeasurementClient",
            "--directory-out",
            str(temp_directory),
        ]
    )

    assert result.exit_code == 0
    _assert_equal(
        golden_path / filename,
        temp_directory / filename,
    )


def test___all_registered_measurements___create_client___renders_without_error(
    create_client: CliRunnerFunction,
    tmp_path_factory: pytest.TempPathFactory,
    multiple_measurement_service: MeasurementService,
) -> None:
    temp_directory = tmp_path_factory.mktemp("measurement_plugin_client_files")

    result = create_client(
        [
            "--all",
            "--directory-out",
            str(temp_directory),
        ]
    )

    expected_modules = [
        "non_streaming_data_measurement_client.py",
        "streaming_data_measurement_client.py",
    ]
    actual_modules = os.listdir(temp_directory)
    assert all(
        [
            result.exit_code == 0,
            len(actual_modules) == 2,
            expected_modules == actual_modules,
        ]
    )


def test___interactive_mode_with_registered_measurements___create_client___renders_without_error(
    create_client: CliRunnerFunction,
    test_assets_directory: pathlib.Path,
    tmp_path_factory: pytest.TempPathFactory,
    non_streaming_measurement_service: MeasurementService,
) -> None:
    temp_directory = tmp_path_factory.mktemp("measurement_plugin_client_files")
    golden_path = test_assets_directory / "example_renders" / "measurement_plugin_client"
    filename = "non_streaming_data_measurement_client.py"
    inputs = [
        "1",
        "non_streaming_data_measurement_client",
        "NonStreamingDataMeasurementClient",
        "x",
    ]
    os.chdir(temp_directory)

    result = create_client(["--interactive"], input="\n".join(inputs))

    assert result.exit_code == 0
    _assert_equal(
        golden_path / filename,
        temp_directory / filename,
    )


def test___interactive_mode_without_registered_measurements___create_client___raises_exception(
    create_client: CliRunnerFunction,
) -> None:
    result = create_client(["--interactive"])
    assert result.exit_code == 1
    assert "No registered measurements." in str(result.exception)


def test___non_streaming_measurement___create_client___render_with_proper_line_ending(
    create_client: CliRunnerFunction,
    tmp_path_factory: pytest.TempPathFactory,
    non_streaming_measurement_service: MeasurementService,
) -> None:
    temp_directory = tmp_path_factory.mktemp("measurement_plugin_client_files")
    module_name = "non_streaming_data_measurement_client"
    filename = f"{module_name}.py"

    result = create_client(
        [
            "--measurement-service-class",
            "ni.tests.NonStreamingDataMeasurement_Python",
            "--module-name",
            module_name,
            "--class-name",
            "NonStreamingDataMeasurementClient",
            "--directory-out",
            str(temp_directory),
        ]
    )

    assert result.exit_code == 0
    _assert_line_ending(temp_directory / filename)


def test___non_streaming_measurement___create_client___render_without_mypy_error(
    create_client: CliRunnerFunction,
    tmp_path_factory: pytest.TempPathFactory,
    non_streaming_measurement_service: MeasurementService,
) -> None:
    temp_directory = tmp_path_factory.mktemp("measurement_plugin_client_files")
    module_name = "non_streaming_data_measurement_client"
    filename = f"{module_name}.py"

    result = create_client(
        [
            "--measurement-service-class",
            "ni.tests.NonStreamingDataMeasurement_Python",
            "--module-name",
            module_name,
            "--class-name",
            "NonStreamingDataMeasurementClient",
            "--directory-out",
            str(temp_directory),
        ]
    )

    mypy_result = mypy.api.run([str(temp_directory / filename)])
    mypy_exit_status = mypy_result[2]
    assert result.exit_code == 0
    assert mypy_exit_status == 0


def _assert_equal(expected_path: pathlib.Path, result_path: pathlib.Path) -> None:
    expected = expected_path.read_text(encoding="utf-8")
    result = result_path.read_text(encoding="utf-8")

    assert expected == result


def _assert_line_ending(file_path: pathlib.Path) -> None:
    content = file_path.read_bytes()
    if sys.platform == "win32":
        pattern = re.compile(rb"(\r?\n)+")
        matches = pattern.findall(content)
        for match in matches:
            assert match == b"\r\n"
    else:
        pattern = re.compile(rb"\r?\n")
        matches = pattern.findall(content)
        for match in matches:
            assert match == b"\n"


@pytest.fixture
def non_streaming_measurement_service(
    discovery_service_process: DiscoveryServiceProcess,
) -> Generator[MeasurementService, None, None]:
    """Test fixture that creates and hosts a non streaming Measurement Plug-In Service."""
    with non_streaming_data_measurement.measurement_service.host_service() as service:
        yield service


@pytest.fixture
def void_measurement_service(
    discovery_service_process: DiscoveryServiceProcess,
) -> Generator[MeasurementService, None, None]:
    """Test fixture that creates and hosts a void Measurement Plug-In Service."""
    with void_measurement.measurement_service.host_service() as service:
        yield service


@pytest.fixture
def localized_measurement_service(
    discovery_service_process: DiscoveryServiceProcess,
) -> Generator[MeasurementService, None, None]:
    """Test fixture that creates and hosts a localized Measurement Plug-In Service."""
    with localized_measurement.measurement_service.host_service() as service:
        yield service


@pytest.fixture
def multiple_measurement_service(
    discovery_service_process: DiscoveryServiceProcess,
) -> Generator[MeasurementService, None, None]:
    """Test fixture that creates and hosts a Measurement Plug-In Service."""
    with non_streaming_data_measurement.measurement_service.host_service(), streaming_data_measurement.measurement_service.host_service() as services:
        yield services
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/acceptance/test_non_streaming_measurement_client.py sha256=1448de29d261d62e633db7553273f537f68f82c171872da2816d2befddd169ed bytes=9808 -->
## FILE: packages/generator/tests/acceptance/test_non_streaming_measurement_client.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/acceptance/test_non_streaming_measurement_client.py`
- sha256: `1448de29d261d62e633db7553273f537f68f82c171872da2816d2befddd169ed`
- bytes: 9808

````python
from __future__ import annotations

import importlib.util
import pathlib
from collections.abc import Generator, Sequence
from enum import Enum
from types import ModuleType
from typing import Any

import pytest
from ni.protobuf.types import array_pb2
from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService

from tests.conftest import CliRunnerFunction
from tests.utilities.discovery_service_process import DiscoveryServiceProcess
from tests.utilities.measurements import non_streaming_data_measurement


class EnumInEnum(Enum):
    """EnumInEnum used for enum-typed measurement configs and outputs."""

    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3


class ProtobufEnumInEnum(Enum):
    """ProtobufEnumInEnum used for enum-typed measurement configs and outputs."""

    NONE = 0
    PINK = 1
    WHITE = 2
    BLACK = 3


def test___measurement_plugin_client___measure___returns_output(
    measurement_plugin_client_module: ModuleType,
) -> None:
    test_measurement_client_type = getattr(measurement_plugin_client_module, "TestMeasurement")
    output_type = getattr(measurement_plugin_client_module, "Outputs")
    expected_output = output_type(
        float_out=0.05999999865889549,
        double_array_out=[0.1, 0.2, 0.3],
        bool_out=False,
        string_out="sample string",
        string_array_out=[
            "string with /forwardslash",
            "string with \\backslash",
            "string with 'single quotes'",
            'string with "double quotes"',
            "string with \ttabspace",
            "string with \nnewline",
        ],
        path_out=pathlib.Path("sample\\path\\for\\test"),
        path_array_out=[
            pathlib.Path("path\\with\\forward\\slash"),
            pathlib.Path("path\\with\\backslash"),
            pathlib.Path("path with 'single quotes'"),
            pathlib.Path('path with "double quotes"'),
            pathlib.Path("path\twith\ttabs"),
            pathlib.Path("path\nwith\nnewlines"),
        ],
        io_out="resource",
        io_array_out=["resource1", "resource2"],
        integer_out=10,
        xy_data_out=None,
        enum_out=EnumInEnum.BLUE,
        enum_array_out=[EnumInEnum.RED, EnumInEnum.GREEN],
        protobuf_enum_out=ProtobufEnumInEnum.BLACK,
        double_2d_array_out=array_pb2.Double2DArray(
            rows=2, columns=3, data=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
        ),
        string_2d_array_out=array_pb2.String2DArray(
            rows=2, columns=3, data=["ABC", "DEF", "GHI", "JKL", "MNO", "PQR"]
        ),
    )
    measurement_plugin_client = test_measurement_client_type()

    response = measurement_plugin_client.measure()

    # Enum values are not comparable due to differing imports.
    # So comparing values by converting them to string.
    assert str(response) == str(expected_output)


def test___measurement_plugin_client___measure___converts_output_types(
    measurement_plugin_client_module: ModuleType,
) -> None:
    test_measurement_client_type = getattr(measurement_plugin_client_module, "TestMeasurement")
    measurement_plugin_client = test_measurement_client_type()

    response = measurement_plugin_client.measure()

    _verify_output_types(response, measurement_plugin_client_module)


def test___measurement_plugin_client___stream_measure___returns_output(
    measurement_plugin_client_module: ModuleType,
) -> None:
    test_measurement_client_type = getattr(measurement_plugin_client_module, "TestMeasurement")
    output_type = getattr(measurement_plugin_client_module, "Outputs")
    expected_output = output_type(
        float_out=0.05999999865889549,
        double_array_out=[0.1, 0.2, 0.3],
        bool_out=False,
        string_out="sample string",
        string_array_out=[
            "string with /forwardslash",
            "string with \\backslash",
            "string with 'single quotes'",
            'string with "double quotes"',
            "string with \ttabspace",
            "string with \nnewline",
        ],
        path_out=pathlib.Path("sample\\path\\for\\test"),
        path_array_out=[
            pathlib.Path("path\\with\\forward\\slash"),
            pathlib.Path("path\\with\\backslash"),
            pathlib.Path("path with 'single quotes'"),
            pathlib.Path('path with "double quotes"'),
            pathlib.Path("path\twith\ttabs"),
            pathlib.Path("path\nwith\nnewlines"),
        ],
        io_out="resource",
        io_array_out=["resource1", "resource2"],
        integer_out=10,
        xy_data_out=None,
        enum_out=EnumInEnum.BLUE,
        enum_array_out=[EnumInEnum.RED, EnumInEnum.GREEN],
        protobuf_enum_out=ProtobufEnumInEnum.BLACK,
        double_2d_array_out=array_pb2.Double2DArray(
            rows=2, columns=3, data=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
        ),
        string_2d_array_out=array_pb2.String2DArray(
            rows=2, columns=3, data=["ABC", "DEF", "GHI", "JKL", "MNO", "PQR"]
        ),
    )
    measurement_plugin_client = test_measurement_client_type()

    response_iterator = measurement_plugin_client.stream_measure()

    responses = [response for response in response_iterator]
    assert len(responses) == 1
    # Enum values are not comparable due to differing imports.
    # So comparing values by converting them to string.
    assert str(responses[0]) == str(expected_output)


def test___measurement_plugin_client___stream_measure___converts_output_types(
    measurement_plugin_client_module: ModuleType,
) -> None:
    test_measurement_client_type = getattr(measurement_plugin_client_module, "TestMeasurement")
    measurement_plugin_client = test_measurement_client_type()

    response_iterator = measurement_plugin_client.stream_measure()

    responses = [response for response in response_iterator]
    assert len(responses) == 1
    _verify_output_types(responses[0], measurement_plugin_client_module)


@pytest.fixture(scope="module")
def measurement_client_directory(
    create_client: CliRunnerFunction,
    tmp_path_factory: pytest.TempPathFactory,
    measurement_service: MeasurementService,
) -> pathlib.Path:
    """Test fixture that creates a Measurement Plug-In Client."""
    temp_directory = tmp_path_factory.mktemp("measurement_plugin_client_files")
    module_name = "test_measurement_client"

    create_client(
        [
            "--measurement-service-class",
            "ni.tests.NonStreamingDataMeasurement_Python",
            "--module-name",
            module_name,
            "--class-name",
            "TestMeasurement",
            "--directory-out",
            str(temp_directory),
        ]
    )

    return temp_directory


@pytest.fixture(scope="module")
def measurement_plugin_client_module(
    measurement_client_directory: pathlib.Path,
) -> ModuleType:
    """Test fixture that imports the generated Measurement Plug-In Client module."""
    module_path = measurement_client_directory / "test_measurement_client.py"
    spec = importlib.util.spec_from_file_location("test_measurement_client.py", module_path)
    if spec is not None:
        imported_module = importlib.util.module_from_spec(spec)
        if spec.loader is not None:
            spec.loader.exec_module(imported_module)
            return imported_module
    pytest.fail("The module specification cannot be None.")


@pytest.fixture(scope="module")
def measurement_service(
    discovery_service_process: DiscoveryServiceProcess,
) -> Generator[MeasurementService]:
    """Test fixture that creates and hosts a Measurement Plug-In Service."""
    with non_streaming_data_measurement.measurement_service.host_service() as service:
        yield service


def _verify_output_types(outputs: Any, measurement_plugin_client_module: ModuleType) -> None:
    output_type = getattr(measurement_plugin_client_module, "Outputs")
    enum_type = getattr(measurement_plugin_client_module, "EnumInEnum")
    protobuf_enum_type = getattr(measurement_plugin_client_module, "ProtobufEnumInEnum")

    _assert_type(outputs, output_type)
    _assert_type(outputs.float_out, float)
    _assert_collection_type(outputs.double_array_out, Sequence, float)
    _assert_type(outputs.bool_out, bool)
    _assert_type(outputs.string_out, str)
    _assert_collection_type(outputs.string_array_out, Sequence, str)
    _assert_type(outputs.path_out, pathlib.Path)
    _assert_collection_type(outputs.path_array_out, Sequence, pathlib.Path)
    _assert_type(outputs.io_out, str)
    _assert_collection_type(outputs.io_array_out, Sequence, str)
    _assert_type(outputs.integer_out, int)
    _assert_type(outputs.xy_data_out, type(None))
    _assert_type(outputs.io_out, str)
    _assert_collection_type(outputs.io_array_out, Sequence, str)
    _assert_type(outputs.enum_out, enum_type)
    _assert_collection_type(outputs.enum_array_out, Sequence, enum_type)
    _assert_type(outputs.protobuf_enum_out, protobuf_enum_type)
    _assert_type(outputs.double_2d_array_out, array_pb2.Double2DArray)
    _assert_type(outputs.string_2d_array_out, array_pb2.String2DArray)


def _assert_type(value: Any, expected_type: type[Any] | tuple[type[Any], ...]) -> None:
    assert isinstance(
        value, expected_type
    ), f"{value!r} has type {type(value)}, expected {expected_type}"


def _assert_collection_type(
    value: Any,
    expected_type: type[Any] | tuple[type[Any], ...],
    expected_element_type: type[Any] | tuple[type[Any], ...],
) -> None:
    _assert_type(value, expected_type)
    for element in value:
        _assert_type(element, expected_element_type)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/acceptance/test_pin_aware_measurement_client.py sha256=4d6dac6c6aca3b8ae0bc920a62a78d1a430fc5460668c42f7746fb2d424e2c08 bytes=8327 -->
## FILE: packages/generator/tests/acceptance/test_pin_aware_measurement_client.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/acceptance/test_pin_aware_measurement_client.py`
- sha256: `4d6dac6c6aca3b8ae0bc920a62a78d1a430fc5460668c42f7746fb2d424e2c08`
- bytes: 8327

````python
import importlib.util
import pathlib
from collections.abc import Generator
from types import ModuleType

import grpc
import pytest
from ni.measurementlink.sessionmanagement.v1.client import PinMapContext
from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService

from tests.conftest import CliRunnerFunction
from tests.utilities.discovery_service_process import DiscoveryServiceProcess
from tests.utilities.measurements import pin_aware_measurement


def test___measurement_plugin_client___measure_with_pin_map_registration___returns_output(
    measurement_plugin_client_module: ModuleType,
    pin_map_directory: pathlib.Path,
) -> None:
    pin_map_path = pin_map_directory / "1Smu1ChannelGroup1Pin1Site.pinmap"
    output_type = getattr(measurement_plugin_client_module, "Outputs")
    expected_output = output_type(
        pin_map_id=str(pin_map_path),
        sites=[0],
        session_names=["DCPower1/0"],
        resource_names=["DCPower1/0"],
        channel_lists=["DCPower1/0"],
    )
    test_measurement_client_type = getattr(measurement_plugin_client_module, "TestMeasurement")
    measurement_plugin_client = test_measurement_client_type()

    measurement_plugin_client.register_pin_map(pin_map_path)
    output = measurement_plugin_client.measure()

    assert output == expected_output


def test___measurement_plugin_client___measure_without_pin_map_registration___raises_no_sessions_error(
    measurement_plugin_client_module: ModuleType,
) -> None:
    test_measurement_client_type = getattr(measurement_plugin_client_module, "TestMeasurement")
    measurement_plugin_client = test_measurement_client_type()

    with pytest.raises(grpc.RpcError) as exc_info:
        _ = measurement_plugin_client.measure()

    assert exc_info.value.code() == grpc.StatusCode.UNKNOWN
    assert "No sessions reserved." in (exc_info.value.details() or "")


def test___measurement_plugin_client___register_pin_map_without_pin_map_context___creates_pin_map_context_with_pin_map_id_and_sites(
    measurement_plugin_client_module: ModuleType,
    pin_map_directory: pathlib.Path,
) -> None:
    pin_map_path = pin_map_directory / "1Smu1ChannelGroup2Pin2Site.pinmap"
    test_measurement_client_type = getattr(measurement_plugin_client_module, "TestMeasurement")
    measurement_plugin_client = test_measurement_client_type()

    measurement_plugin_client.register_pin_map(pin_map_path)

    expected_pin_map_context = PinMapContext(pin_map_id=str(pin_map_path), sites=[0])
    assert measurement_plugin_client.pin_map_context == expected_pin_map_context


def test___measurement_plugin_client___register_pin_map_with_pin_map_context___updates_pin_map_context_with_pin_map_id(
    measurement_plugin_client_module: ModuleType,
    pin_map_directory: pathlib.Path,
) -> None:
    pin_map_path = pin_map_directory / "1Smu1ChannelGroup2Pin2Site.pinmap"
    test_measurement_client_type = getattr(measurement_plugin_client_module, "TestMeasurement")
    measurement_plugin_client = test_measurement_client_type()
    measurement_plugin_client.pin_map_context = PinMapContext(pin_map_id="", sites=[0, 1])

    measurement_plugin_client.register_pin_map(pin_map_path)

    expected_pin_map_context = PinMapContext(pin_map_id=str(pin_map_path), sites=[0, 1])
    assert measurement_plugin_client.pin_map_context == expected_pin_map_context


def test___measurement_plugin_client___measure_with_default_site_selection___returns_selected_site(
    measurement_plugin_client_module: ModuleType,
    pin_map_directory: pathlib.Path,
) -> None:
    pin_map_path = pin_map_directory / "1Smu1ChannelGroup1Pin1Site.pinmap"
    test_measurement_client_type = getattr(measurement_plugin_client_module, "TestMeasurement")
    measurement_plugin_client = test_measurement_client_type()
    measurement_plugin_client.register_pin_map(pin_map_path)

    output = measurement_plugin_client.measure()

    assert output.sites == [0]


def test___measurement_plugin_client___measure_with_multiple_sites_selection___returns_selected_sites(
    measurement_plugin_client_module: ModuleType,
    pin_map_directory: pathlib.Path,
) -> None:
    pin_map_path = pin_map_directory / "1Smu1ChannelGroup2Pin2Site.pinmap"
    test_measurement_client_type = getattr(measurement_plugin_client_module, "TestMeasurement")
    measurement_plugin_client = test_measurement_client_type()
    measurement_plugin_client.register_pin_map(pin_map_path)

    measurement_plugin_client.sites = [0, 1]
    output = measurement_plugin_client.measure()

    assert output.sites == [0, 1]


def test___measurement_plugin_client___measure_with_invalid_sites_selection___raises_invalid_sites_error(
    measurement_plugin_client_module: ModuleType,
    pin_map_directory: pathlib.Path,
) -> None:
    pin_map_path = pin_map_directory / "1Smu1ChannelGroup1Pin1Site.pinmap"
    test_measurement_client_type = getattr(measurement_plugin_client_module, "TestMeasurement")
    measurement_plugin_client = test_measurement_client_type()
    measurement_plugin_client.register_pin_map(pin_map_path)

    with pytest.raises(grpc.RpcError) as exc_info:
        measurement_plugin_client.sites = [0, 1]
        _ = measurement_plugin_client.measure()

    assert exc_info.value.code() == grpc.StatusCode.UNKNOWN
    assert 'Pin map does not contain site numbers: "1"' in (exc_info.value.details() or "")


def test___measurement_plugin_client___measure_with_pin_map_context___returns_output(
    measurement_plugin_client_module: ModuleType,
    pin_map_directory: pathlib.Path,
) -> None:
    pin_map_path = pin_map_directory / "1Smu1ChannelGroup2Pin2Site.pinmap"
    output_type = getattr(measurement_plugin_client_module, "Outputs")
    expected_output = output_type(
        pin_map_id=str(pin_map_path),
        sites=[0, 1],
        session_names=["DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3"],
        resource_names=["DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3"],
        channel_lists=["DCPower1/0, DCPower1/2"],
    )
    test_measurement_client_type = getattr(measurement_plugin_client_module, "TestMeasurement")
    measurement_plugin_client = test_measurement_client_type()

    measurement_plugin_client.pin_map_context = PinMapContext(
        pin_map_id=str(pin_map_path), sites=[0, 1]
    )
    output = measurement_plugin_client.measure()

    assert output == expected_output


@pytest.fixture(scope="module")
def measurement_client_directory(
    create_client: CliRunnerFunction,
    tmp_path_factory: pytest.TempPathFactory,
    measurement_service: MeasurementService,
) -> pathlib.Path:
    """Test fixture that creates a Measurement Plug-In Client."""
    temp_directory = tmp_path_factory.mktemp("measurement_plugin_client_files")
    module_name = "test_measurement_client"

    create_client(
        [
            "--measurement-service-class",
            "ni.tests.PinAwareMeasurement_Python",
            "--module-name",
            module_name,
            "--class-name",
            "TestMeasurement",
            "--directory-out",
            str(temp_directory),
        ]
    )

    return temp_directory


@pytest.fixture(scope="module")
def measurement_plugin_client_module(
    measurement_client_directory: pathlib.Path,
) -> ModuleType:
    """Test fixture that imports the generated Measurement Plug-In Client module."""
    module_path = measurement_client_directory / "test_measurement_client.py"
    spec = importlib.util.spec_from_file_location("test_measurement_client.py", module_path)
    if spec is not None:
        imported_module = importlib.util.module_from_spec(spec)
        if spec.loader is not None:
            spec.loader.exec_module(imported_module)
            return imported_module
    pytest.fail("The module specification cannot be None.")


@pytest.fixture(scope="module")
def measurement_service(
    discovery_service_process: DiscoveryServiceProcess,
) -> Generator[MeasurementService, None, None]:
    """Test fixture that creates and hosts a Measurement Plug-In Service."""
    with pin_aware_measurement.measurement_service.host_service() as service:
        yield service
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/acceptance/test_plugin_generator.py sha256=bfa521f8f7b880c1c3f7a4e10d94af93e400a66c062906a12fe72bbcbedb6319 bytes=2787 -->
## FILE: packages/generator/tests/acceptance/test_plugin_generator.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/acceptance/test_plugin_generator.py`
- sha256: `bfa521f8f7b880c1c3f7a4e10d94af93e400a66c062906a12fe72bbcbedb6319`
- bytes: 2787

````python
import pathlib

import pytest

from tests.conftest import CliRunnerFunction


def test___command_line_args___create_measurement___render_without_error(
    create_measurement: CliRunnerFunction,
    test_assets_directory: pathlib.Path,
    tmp_path_factory: pytest.TempPathFactory,
) -> None:
    temp_directory = tmp_path_factory.mktemp("measurement_files")
    golden_path = test_assets_directory / "example_renders" / "measurement"
    filenames = ["measurement.py", "SampleMeasurement.serviceconfig", "start.bat", "_helpers.py"]

    result = create_measurement(
        [
            "Sample Measurement",
            "--measurement-version",
            "1.2.3.4",
            "--ui-file",
            "MeasurementUI.measui",
            "--service-class",
            "SampleMeasurement_Python",
            "--description-url",
            "https://www.example.com/SampleMeasurement.html",
            "--directory-out",
            str(temp_directory),
        ]
    )

    assert result.exit_code == 0
    for filename in filenames:
        _assert_equal(
            golden_path / filename,
            temp_directory / filename,
        )


def test___command_line_args___create_measurement_with_annotations___render_without_error(
    create_measurement: CliRunnerFunction,
    test_assets_directory: pathlib.Path,
    tmp_path_factory: pytest.TempPathFactory,
) -> None:
    temp_directory = tmp_path_factory.mktemp("measurement_files")

    result = create_measurement(
        [
            "Sample Measurement",
            "--measurement-version",
            "1.2.3.4",
            "--ui-file",
            "MeasurementUI.measui",
            "--service-class",
            "SampleMeasurement_Python",
            "-D",
            "Measurement description",
            "--description-url",
            "https://www.example.com/SampleMeasurement.html",
            "--directory-out",
            str(temp_directory),
            "--collection",
            "Measurement.Collection",
            "--tags",
            "M1",
            "--tags",
            "M2",
            "--tags",
            "M3",
        ]
    )

    golden_path = test_assets_directory / "example_renders" / "measurement_with_annotations"

    filenames = ["measurement.py", "SampleMeasurement.serviceconfig", "start.bat", "_helpers.py"]
    assert result.exit_code == 0
    for filename in filenames:
        _assert_equal(
            golden_path / filename,
            temp_directory / filename,
        )


def _assert_equal(expected_path: pathlib.Path, result_path: pathlib.Path) -> None:
    expected = expected_path.read_text()
    result = result_path.read_text()

    assert expected == result
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/acceptance/test_streaming_measurement_client.py sha256=767f5e07a5bc61916b5142e5898fa34e6f052f65516e01fefc5e1711a349b321 bytes=6656 -->
## FILE: packages/generator/tests/acceptance/test_streaming_measurement_client.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/acceptance/test_streaming_measurement_client.py`
- sha256: `767f5e07a5bc61916b5142e5898fa34e6f052f65516e01fefc5e1711a349b321`
- bytes: 6656

````python
import concurrent.futures
import importlib.util
import pathlib
from collections.abc import Generator
from types import ModuleType

import grpc
import pytest
from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService

from tests.conftest import CliRunnerFunction
from tests.utilities.discovery_service_process import DiscoveryServiceProcess
from tests.utilities.measurements import streaming_data_measurement


def test___measurement_plugin_client___measure___returns_output(
    measurement_plugin_client_module: ModuleType,
) -> None:
    test_measurement_client_type = getattr(measurement_plugin_client_module, "TestMeasurement")
    output_type = getattr(measurement_plugin_client_module, "Outputs")
    expected_output = output_type(
        name="<Name>",
        index=9,
        data=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    )
    measurement_plugin_client = test_measurement_client_type()

    response = measurement_plugin_client.measure()

    assert response == expected_output


def test___measurement_plugin_client___stream_measure___returns_output(
    measurement_plugin_client_module: ModuleType,
) -> None:
    test_measurement_client_type = getattr(measurement_plugin_client_module, "TestMeasurement")
    output_type = getattr(measurement_plugin_client_module, "Outputs")
    measurement_plugin_client = test_measurement_client_type()

    response_iterator = measurement_plugin_client.stream_measure()

    responses = [response for response in response_iterator]
    expected_output = [
        output_type(
            name="<Name>",
            index=index,
            data=[data for data in range(index + 1)],
        )
        for index in range(10)
    ]
    assert responses == expected_output


def test___measurement_plugin_client___invoke_measure_from_two_threads___initiates_first_measure_and_rejects_second_measure(
    measurement_plugin_client_module: ModuleType,
) -> None:
    test_measurement_client_type = getattr(measurement_plugin_client_module, "TestMeasurement")
    measurement_plugin_client = test_measurement_client_type()

    with pytest.raises(RuntimeError) as exc_info:
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            future_measure_1 = executor.submit(measurement_plugin_client.measure)
            future_measure_2 = executor.submit(measurement_plugin_client.measure)
            future_measure_1.result()
            future_measure_2.result()

    expected_error_message = "A measurement is currently in progress. To make concurrent measurement requests, please create a new client instance."
    assert expected_error_message in exc_info.value.args[0]


def test___non_streaming_measurement_execution___cancel___cancels_measurement(
    measurement_plugin_client_module: ModuleType,
) -> None:
    test_measurement_client_type = getattr(measurement_plugin_client_module, "TestMeasurement")
    measurement_plugin_client = test_measurement_client_type()
    streaming_data_measurement.measurement_started_event.clear()
    is_canceled = False

    with pytest.raises(grpc.RpcError) as exc_info:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            measure = executor.submit(measurement_plugin_client.measure)
            streaming_data_measurement.measurement_started_event.wait()
            is_canceled = measurement_plugin_client.cancel()
            measure.result()

    assert is_canceled
    assert exc_info.value.code() == grpc.StatusCode.CANCELLED


def test___streaming_measurement_execution___cancel___cancels_measurement(
    measurement_plugin_client_module: ModuleType,
) -> None:
    test_measurement_client_type = getattr(measurement_plugin_client_module, "TestMeasurement")
    measurement_plugin_client = test_measurement_client_type()
    streaming_data_measurement.measurement_started_event.clear()
    is_canceled = False

    with pytest.raises(grpc.RpcError) as exc_info:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            measure = executor.submit(lambda: list(measurement_plugin_client.stream_measure()))
            streaming_data_measurement.measurement_started_event.wait()
            is_canceled = measurement_plugin_client.cancel()
            measure.result()

    assert is_canceled
    assert exc_info.value.code() == grpc.StatusCode.CANCELLED


def test___measurement_client___cancel_without_measure___returns_false(
    measurement_plugin_client_module: ModuleType,
) -> None:
    test_measurement_client_type = getattr(measurement_plugin_client_module, "TestMeasurement")
    measurement_plugin_client = test_measurement_client_type()

    is_canceled = measurement_plugin_client.cancel()

    assert not is_canceled


@pytest.fixture(scope="module")
def measurement_client_directory(
    create_client: CliRunnerFunction,
    tmp_path_factory: pytest.TempPathFactory,
    measurement_service: MeasurementService,
) -> pathlib.Path:
    """Test fixture that creates a Measurement Plug-In Client."""
    temp_directory = tmp_path_factory.mktemp("measurement_plugin_client_files")
    module_name = "test_measurement_client"

    create_client(
        [
            "--measurement-service-class",
            "ni.tests.StreamingDataMeasurement_Python",
            "--module-name",
            module_name,
            "--class-name",
            "TestMeasurement",
            "--directory-out",
            str(temp_directory),
        ]
    )

    return temp_directory


@pytest.fixture(scope="module")
def measurement_plugin_client_module(
    measurement_client_directory: pathlib.Path,
) -> ModuleType:
    """Test fixture that imports the generated Measurement Plug-In Client module."""
    module_path = measurement_client_directory / "test_measurement_client.py"
    spec = importlib.util.spec_from_file_location("test_measurement_client.py", module_path)
    if spec is not None:
        imported_module = importlib.util.module_from_spec(spec)
        if spec.loader is not None:
            spec.loader.exec_module(imported_module)
            return imported_module
    pytest.fail("The module specification cannot be None.")


@pytest.fixture(scope="module")
def measurement_service(
    discovery_service_process: DiscoveryServiceProcess,
) -> Generator[MeasurementService, None, None]:
    """Test fixture that creates and hosts a Measurement Plug-In Service."""
    with streaming_data_measurement.measurement_service.host_service() as service:
        yield service
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/conftest.py sha256=47546fd7846d3dfa53e2c84335632880c0f1e9f6dcbb5bdf0c849fd8d5259ab7 bytes=2925 -->
## FILE: packages/generator/tests/conftest.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/conftest.py`
- sha256: `47546fd7846d3dfa53e2c84335632880c0f1e9f6dcbb5bdf0c849fd8d5259ab7`
- bytes: 2925

````python
"""Shared fixtures for ni-measurement-plugin-sdk-generator tests."""

from __future__ import annotations

import functools
import importlib.metadata
import pathlib
import sys
from collections.abc import Generator, Sequence
from typing import Any, Protocol

import pytest
from click.testing import CliRunner, Result
from ni.measurementlink.discovery.v1.client._support import (
    _get_registration_json_file_path,
)
from packaging.version import Version

import ni_measurement_plugin_sdk_generator.client as client_generator
import ni_measurement_plugin_sdk_generator.plugin as plugin_generator
from tests.utilities.discovery_service_process import DiscoveryServiceProcess


class CliRunnerFunction(Protocol):
    """Protocol for a callable that executes a CLI command using Click's CliRunner."""

    def __call__(self, args: Sequence[str], input: str | None = None) -> Result:
        """Execute the CLI command with the provided arguments."""


@pytest.fixture
def test_assets_directory() -> pathlib.Path:
    """Gets path to test_assets directory."""
    return pathlib.Path(__file__).parent / "test_assets"


@pytest.fixture(scope="session")
def discovery_service_process() -> Generator[DiscoveryServiceProcess]:
    """Test fixture that creates discovery service process."""
    if sys.platform != "win32":
        pytest.skip(f"Platform {sys.platform} is not supported for discovery service tests.")

    try:
        registration_json_file_exists = _get_registration_json_file_path().exists()
    except FileNotFoundError:  # registry key not found
        registration_json_file_exists = False
    if not registration_json_file_exists:
        pytest.skip("Registration file not found. Ensure the Measurement Plug-In SDK is installed.")

    with DiscoveryServiceProcess() as proc:
        yield proc


@pytest.fixture
def pin_map_directory(test_assets_directory: pathlib.Path) -> pathlib.Path:
    """Test fixture that returns the pin map directory."""
    return test_assets_directory / "pin_map"


@pytest.fixture(scope="session")
def create_client() -> Generator[CliRunnerFunction]:
    """Test fixture for calling client generator cli."""
    runner = _create_clirunner()
    yield functools.partial(runner.invoke, client_generator.create_client, standalone_mode=False)


@pytest.fixture(scope="session")
def create_measurement() -> Generator[CliRunnerFunction]:
    """Test fixture for calling plugin generator cli."""
    runner = _create_clirunner()
    yield functools.partial(
        runner.invoke, plugin_generator.create_measurement, standalone_mode=False
    )


def _create_clirunner() -> CliRunner:
    kwargs: dict[str, Any] = {}
    if Version(importlib.metadata.version("click")) < Version("8.2.0"):
        # mix_stderr was removed in click 8.2.
        kwargs["mix_stderr"] = False
    return CliRunner(**kwargs)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/test_assets/example_renders/measurement/_helpers.py sha256=0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426 bytes=2920 -->
## FILE: packages/generator/tests/test_assets/example_renders/measurement/_helpers.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/test_assets/example_renders/measurement/_helpers.py`
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

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/test_assets/example_renders/measurement/measurement.py sha256=42f666429e52e0da3741a45ac9eeffd395b21fb2ebf9e34bacbe4102ee53f59c bytes=1504 -->
## FILE: packages/generator/tests/test_assets/example_renders/measurement/measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/test_assets/example_renders/measurement/measurement.py`
- sha256: `42f666429e52e0da3741a45ac9eeffd395b21fb2ebf9e34bacbe4102ee53f59c`
- bytes: 1504

````python
"""A default measurement with an array in and out."""

import logging
import pathlib
import sys

import click
import ni_measurement_plugin_sdk_service as nims

script_or_exe = sys.executable if getattr(sys, "frozen", False) else __file__
service_directory = pathlib.Path(script_or_exe).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "SampleMeasurement.serviceconfig",
    ui_file_paths=[service_directory / "MeasurementUI.measui"],
)


@measurement_service.register_measurement
@measurement_service.configuration("Array in", nims.DataType.DoubleArray1D, [0.0])
@measurement_service.output("Array out", nims.DataType.DoubleArray1D)
def measure(array_input):
    """TODO: replace the following line with your own measurement logic."""
    array_output = array_input
    return (array_output,)


@click.command
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Enable verbose logging. Repeat to increase verbosity.",
)
def main(verbose: int) -> None:
    """Host the Sample Measurement service."""
    if verbose > 1:
        level = logging.DEBUG
    elif verbose == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=level)

    with measurement_service.host_service():
        input("Press enter to close the measurement service.\n")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/test_assets/example_renders/measurement/SampleMeasurement.serviceconfig sha256=f5271c0f285eed9521cb81ea5dc0e73732a0e3d81ee25466eed700fbc4823d2b bytes=578 -->
## FILE: packages/generator/tests/test_assets/example_renders/measurement/SampleMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/test_assets/example_renders/measurement/SampleMeasurement.serviceconfig`
- sha256: `f5271c0f285eed9521cb81ea5dc0e73732a0e3d81ee25466eed700fbc4823d2b`
- bytes: 578

````json
{
  "services": [
    {
      "displayName": "Sample Measurement",
      "serviceClass": "SampleMeasurement_Python",
      "descriptionUrl": "https://www.example.com/SampleMeasurement.html",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "version": "1.2.3.4",
      "annotations": {
        "ni/service.description": "",
        "ni/service.collection": "",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/test_assets/example_renders/measurement/start.bat sha256=bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851 bytes=253 -->
## FILE: packages/generator/tests/test_assets/example_renders/measurement/start.bat

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/test_assets/example_renders/measurement/start.bat`
- sha256: `bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851`
- bytes: 253

````batch
@echo off
REM The discovery service uses this script to start the measurement service.
REM You can customize this script for your Python setup. The -v option logs
REM messages with level INFO and above.

.venv\Scripts\python.exe measurement.py -v
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/test_assets/example_renders/measurement_plugin_client/localized_measurement_client.py sha256=c4a106bded48eea2291475642bf673df0a4618c31480502457a0c4d2b70abcb1 bytes=25740 -->
## FILE: packages/generator/tests/test_assets/example_renders/measurement_plugin_client/localized_measurement_client.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/test_assets/example_renders/measurement_plugin_client/localized_measurement_client.py`
- sha256: `c4a106bded48eea2291475642bf673df0a4618c31480502457a0c4d2b70abcb1`
- bytes: 25740

````python
"""Generated client API for the '本地化测量（Py）' measurement plug-in."""

from __future__ import annotations

import logging
import pathlib
import threading
import typing
import warnings
from enum import Enum

import grpc
from google.protobuf import any_pb2, descriptor_pool
from google.protobuf.type_pb2 import Field
from ni.measurementlink.measurement.v2 import (
    measurement_service_pb2 as v2_measurement_service_pb2,
    measurement_service_pb2_grpc as v2_measurement_service_pb2_grpc,
)
from ni.protobuf.types.array_pb2 import Double2DArray
from ni.protobuf.types.array_pb2 import String2DArray
from ni.protobuf.types.xydata_pb2 import DoubleXYData
from ni_grpc_extensions.channelpool import GrpcChannelPool
from ni.measurementlink.discovery.v1.client import DiscoveryClient
from ni.measurementlink.sessionmanagement.v1.client import PinMapContext
from ni_measurement_plugin_sdk_service.measurement import WrongMessageTypeWarning
from ni_measurement_plugin_sdk_service.measurement.client_support import (
    ParameterMetadata,
    create_file_descriptor,
    deserialize_parameters,
    serialize_parameters,
)
from ni.measurementlink.pinmap.v1.client import PinMapClient

_logger = logging.getLogger(__name__)

_V2_MEASUREMENT_SERVICE_INTERFACE = "ni.measurementlink.measurement.v2.MeasurementService"


class EnumInEnum(Enum):
    """EnumInEnum used for enum-typed measurement configs and outputs."""

    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3


class Outputs(typing.NamedTuple):
    """Outputs for the '本地化测量（Py）' measurement plug-in."""

    float_out: float
    double_array_out: typing.Sequence[float]
    bool_out: bool
    string_out: str
    string_array_out: typing.Sequence[str]
    path_out: pathlib.Path
    path_array_out: typing.Sequence[pathlib.Path]
    io_out: str
    io_array_out: typing.Sequence[str]
    integer_out: int
    xy_data_out: DoubleXYData
    enum_out: EnumInEnum
    enum_array_out: typing.Sequence[EnumInEnum]
    double_2d_array_out: Double2DArray
    string_2d_array_out: String2DArray


class LocalizedMeasurementClient:
    """Client for the '本地化测量（Py）' measurement plug-in."""

    def __init__(
        self,
        *,
        discovery_client: DiscoveryClient | None = None,
        pin_map_client: PinMapClient | None = None,
        grpc_channel: grpc.Channel | None = None,
        grpc_channel_pool: GrpcChannelPool | None = None,
    ):
        """Initialize the Measurement Plug-In Client.

        Args:
            discovery_client: An optional discovery client.

            pin_map_client: An optional pin map client.

            grpc_channel: An optional gRPC channel targeting a measurement service.

            grpc_channel_pool: An optional gRPC channel pool.
        """
        self._initialization_lock = threading.RLock()
        self._service_class = "ni.tests.LocalizedMeasurement_Python"
        self._version = "0.1.0.0"
        self._grpc_channel_pool = grpc_channel_pool
        self._discovery_client = discovery_client
        self._pin_map_client = pin_map_client
        self._stub: v2_measurement_service_pb2_grpc.MeasurementServiceStub | None = None
        self._measure_response: None | (
            grpc._CallIterator[v2_measurement_service_pb2.MeasureResponse]
        ) = None
        self._configuration_metadata = {
            1: ParameterMetadata(
                display_name="Float In",
                type=Field.Kind.ValueType(2),
                repeated=False,
                default_value=0.05999999865889549,
                annotations={},
                message_type="",
                field_name="Float_In",
                enum_type=None,
            ),
            2: ParameterMetadata(
                display_name="Double Array In",
                type=Field.Kind.ValueType(1),
                repeated=True,
                default_value=[0.1, 0.2, 0.3],
                annotations={},
                message_type="",
                field_name="Double_Array_In",
                enum_type=None,
            ),
            3: ParameterMetadata(
                display_name="Bool In",
                type=Field.Kind.ValueType(8),
                repeated=False,
                default_value=False,
                annotations={},
                message_type="",
                field_name="Bool_In",
                enum_type=None,
            ),
            4: ParameterMetadata(
                display_name="String In",
                type=Field.Kind.ValueType(9),
                repeated=False,
                default_value="示例字符串",
                annotations={},
                message_type="",
                field_name="String_In",
                enum_type=None,
            ),
            5: ParameterMetadata(
                display_name="String Array In",
                type=Field.Kind.ValueType(9),
                repeated=True,
                default_value=[
                    "带有/正斜杠的字符串",
                    "带有\\反斜杠的字符串",
                    "带有'单引号'的字符串",
                    '带有"双引号"的字符串',
                    "带有\t制表符的字符串",
                    "带有\n换行符的字符串",
                ],
                annotations={},
                message_type="",
                field_name="String_Array_In",
                enum_type=None,
            ),
            6: ParameterMetadata(
                display_name="Path In",
                type=Field.Kind.ValueType(9),
                repeated=False,
                default_value="示例\\路径\\用于\\测试",
                annotations={"ni/type_specialization": "path"},
                message_type="",
                field_name="Path_In",
                enum_type=None,
            ),
            7: ParameterMetadata(
                display_name="Path Array In",
                type=Field.Kind.ValueType(9),
                repeated=True,
                default_value=[
                    "路径/带有/正斜杠",
                    "路径\\带有\\反斜杠",
                    "路径 带有 '单引号'",
                    '路径 带有 "双引号"',
                    "路径\t带有\t制表符",
                    "路径\n带有\n换行符",
                ],
                annotations={"ni/type_specialization": "path"},
                message_type="",
                field_name="Path_Array_In",
                enum_type=None,
            ),
            8: ParameterMetadata(
                display_name="IO In",
                type=Field.Kind.ValueType(9),
                repeated=False,
                default_value="资源",
                annotations={
                    "ni/ioresource.instrument_type": "",
                    "ni/type_specialization": "ioresource",
                },
                message_type="",
                field_name="IO_In",
                enum_type=None,
            ),
            9: ParameterMetadata(
                display_name="IO Array In",
                type=Field.Kind.ValueType(9),
                repeated=True,
                default_value=["资源1", "资源2"],
                annotations={
                    "ni/ioresource.instrument_type": "",
                    "ni/type_specialization": "ioresource",
                },
                message_type="",
                field_name="IO_Array_In",
                enum_type=None,
            ),
            10: ParameterMetadata(
                display_name="Integer In",
                type=Field.Kind.ValueType(5),
                repeated=False,
                default_value=10,
                annotations={},
                message_type="",
                field_name="Integer_In",
                enum_type=None,
            ),
            11: ParameterMetadata(
                display_name="Enum In",
                type=Field.Kind.ValueType(14),
                repeated=False,
                default_value=3,
                annotations={
                    "ni/enum.values": '{"NONE": 0, "RED": 1, "GREEN": 2, "BLUE": 3}',
                    "ni/type_specialization": "enum",
                },
                message_type="",
                field_name="Enum_In",
                enum_type=EnumInEnum,
            ),
            12: ParameterMetadata(
                display_name="Enum Array In",
                type=Field.Kind.ValueType(14),
                repeated=True,
                default_value=[1, 2],
                annotations={
                    "ni/enum.values": '{"NONE": 0, "RED": 1, "GREEN": 2, "BLUE": 3}',
                    "ni/type_specialization": "enum",
                },
                message_type="",
                field_name="Enum_Array_In",
                enum_type=EnumInEnum,
            ),
        }
        self._output_metadata = {
            1: ParameterMetadata(
                display_name="Float out",
                type=Field.Kind.ValueType(2),
                repeated=False,
                default_value=None,
                annotations={},
                message_type="",
                field_name="Float_out",
                enum_type=None,
            ),
            2: ParameterMetadata(
                display_name="Double Array out",
                type=Field.Kind.ValueType(1),
                repeated=True,
                default_value=None,
                annotations={},
                message_type="",
                field_name="Double_Array_out",
                enum_type=None,
            ),
            3: ParameterMetadata(
                display_name="Bool out",
                type=Field.Kind.ValueType(8),
                repeated=False,
                default_value=None,
                annotations={},
                message_type="",
                field_name="Bool_out",
                enum_type=None,
            ),
            4: ParameterMetadata(
                display_name="String out",
                type=Field.Kind.ValueType(9),
                repeated=False,
                default_value=None,
                annotations={},
                message_type="",
                field_name="String_out",
                enum_type=None,
            ),
            5: ParameterMetadata(
                display_name="String Array out",
                type=Field.Kind.ValueType(9),
                repeated=True,
                default_value=None,
                annotations={},
                message_type="",
                field_name="String_Array_out",
                enum_type=None,
            ),
            6: ParameterMetadata(
                display_name="Path Out",
                type=Field.Kind.ValueType(9),
                repeated=False,
                default_value=None,
                annotations={"ni/type_specialization": "path"},
                message_type="",
                field_name="Path_Out",
                enum_type=None,
            ),
            7: ParameterMetadata(
                display_name="Path Array Out",
                type=Field.Kind.ValueType(9),
                repeated=True,
                default_value=None,
                annotations={"ni/type_specialization": "path"},
                message_type="",
                field_name="Path_Array_Out",
                enum_type=None,
            ),
            8: ParameterMetadata(
                display_name="IO Out",
                type=Field.Kind.ValueType(9),
                repeated=False,
                default_value=None,
                annotations={
                    "ni/ioresource.instrument_type": "",
                    "ni/type_specialization": "ioresource",
                },
                message_type="",
                field_name="IO_Out",
                enum_type=None,
            ),
            9: ParameterMetadata(
                display_name="IO Array Out",
                type=Field.Kind.ValueType(9),
                repeated=True,
                default_value=None,
                annotations={
                    "ni/ioresource.instrument_type": "",
                    "ni/type_specialization": "ioresource",
                },
                message_type="",
                field_name="IO_Array_Out",
                enum_type=None,
            ),
            10: ParameterMetadata(
                display_name="Integer Out",
                type=Field.Kind.ValueType(5),
                repeated=False,
                default_value=None,
                annotations={},
                message_type="",
                field_name="Integer_Out",
                enum_type=None,
            ),
            11: ParameterMetadata(
                display_name="XY Data Out",
                type=Field.Kind.ValueType(11),
                repeated=False,
                default_value=None,
                annotations={},
                message_type="ni.protobuf.types.DoubleXYData",
                field_name="XY_Data_Out",
                enum_type=None,
            ),
            12: ParameterMetadata(
                display_name="Enum Out",
                type=Field.Kind.ValueType(14),
                repeated=False,
                default_value=None,
                annotations={
                    "ni/enum.values": '{"NONE": 0, "RED": 1, "GREEN": 2, "BLUE": 3}',
                    "ni/type_specialization": "enum",
                },
                message_type="",
                field_name="Enum_Out",
                enum_type=EnumInEnum,
            ),
            13: ParameterMetadata(
                display_name="Enum Array Out",
                type=Field.Kind.ValueType(14),
                repeated=True,
                default_value=None,
                annotations={
                    "ni/enum.values": '{"NONE": 0, "RED": 1, "GREEN": 2, "BLUE": 3}',
                    "ni/type_specialization": "enum",
                },
                message_type="",
                field_name="Enum_Array_Out",
                enum_type=EnumInEnum,
            ),
            14: ParameterMetadata(
                display_name="Double 2D Array out",
                type=Field.Kind.ValueType(11),
                repeated=False,
                default_value=None,
                annotations={},
                message_type="ni.protobuf.types.Double2DArray",
                field_name="Double_2D_Array_out",
                enum_type=None,
            ),
            15: ParameterMetadata(
                display_name="String 2D Array out",
                type=Field.Kind.ValueType(11),
                repeated=False,
                default_value=None,
                annotations={},
                message_type="ni.protobuf.types.String2DArray",
                field_name="String_2D_Array_out",
                enum_type=None,
            ),
        }
        if grpc_channel is not None:
            self._stub = v2_measurement_service_pb2_grpc.MeasurementServiceStub(grpc_channel)
        self._create_file_descriptor()
        self._pin_map_context: PinMapContext = PinMapContext(pin_map_id="", sites=[0])

    @property
    def pin_map_context(self) -> PinMapContext:
        """The pin map context for the measurement."""
        return self._pin_map_context

    @pin_map_context.setter
    def pin_map_context(self, val: PinMapContext) -> None:
        if not isinstance(val, PinMapContext):
            raise TypeError(
                f"Invalid type {type(val)}: The given value must be an instance of PinMapContext."
            )
        self._pin_map_context = val

    @property
    def sites(self) -> list[int] | None:
        """The sites where the measurement must be executed."""
        return self._pin_map_context.sites

    @sites.setter
    def sites(self, val: list[int]) -> None:
        if self._pin_map_context is None:
            raise AttributeError(
                "Cannot set sites because the pin map context is None. Please provide a pin map context or register a pin map before setting sites."
            )
        self._pin_map_context = self._pin_map_context._replace(sites=val)

    def _get_stub(self) -> v2_measurement_service_pb2_grpc.MeasurementServiceStub:
        if self._stub is None:
            with self._initialization_lock:
                if self._stub is None:
                    service_location = self._get_discovery_client().resolve_service(
                        provided_interface=_V2_MEASUREMENT_SERVICE_INTERFACE,
                        service_class=self._service_class,
                        version=self._version,
                    )
                    channel = self._get_grpc_channel_pool().get_channel(
                        service_location.insecure_address
                    )
                    self._stub = v2_measurement_service_pb2_grpc.MeasurementServiceStub(channel)
        return self._stub

    def _get_discovery_client(self) -> DiscoveryClient:
        if self._discovery_client is None:
            with self._initialization_lock:
                if self._discovery_client is None:
                    self._discovery_client = DiscoveryClient(
                        grpc_channel_pool=self._get_grpc_channel_pool(),
                    )
        return self._discovery_client

    def _get_grpc_channel_pool(self) -> GrpcChannelPool:
        if self._grpc_channel_pool is None:
            with self._initialization_lock:
                if self._grpc_channel_pool is None:
                    self._grpc_channel_pool = GrpcChannelPool()
        return self._grpc_channel_pool

    def _get_pin_map_client(self) -> PinMapClient:
        if self._pin_map_client is None:
            with self._initialization_lock:
                if self._pin_map_client is None:
                    self._pin_map_client = PinMapClient(
                        discovery_client=self._get_discovery_client(),
                        grpc_channel_pool=self._get_grpc_channel_pool(),
                    )
        return self._pin_map_client

    def _create_file_descriptor(self) -> None:
        create_file_descriptor(
            input_metadata=list(self._configuration_metadata.values()),
            output_metadata=list(self._output_metadata.values()),
            service_name=self._service_class,
            pool=descriptor_pool.Default(),
        )

    def _create_measure_request(
        self, parameter_values: list[typing.Any]
    ) -> v2_measurement_service_pb2.MeasureRequest:
        serialized_configuration = any_pb2.Any(
            type_url="type.googleapis.com/ni.tests.LocalizedMeasurement_Python.Configurations",
            value=serialize_parameters(
                self._configuration_metadata,
                parameter_values,
                f"{self._service_class}.Configurations",
            ),
        )
        return v2_measurement_service_pb2.MeasureRequest(
            configuration_parameters=serialized_configuration,
            pin_map_context=self._pin_map_context._to_grpc(),
        )

    def _deserialize_response(
        self, response: v2_measurement_service_pb2.MeasureResponse
    ) -> Outputs:
        self._validate_response(response)
        return Outputs._make(
            deserialize_parameters(
                self._output_metadata,
                response.outputs.value,
                f"{self._service_class}.Outputs",
            )
        )

    def _validate_response(self, response: v2_measurement_service_pb2.MeasureResponse) -> None:
        expected_type = "type.googleapis.com/" + "ni.tests.LocalizedMeasurement_Python.Outputs"
        actual_type = response.outputs.type_url
        if actual_type != expected_type:
            warnings.warn(
                f"Wrong message type. Expected {expected_type!r} but got {actual_type!r}",
                WrongMessageTypeWarning,
            )

    def measure(
        self,
        float_in: float = 0.05999999865889549,
        double_array_in: typing.Iterable[float] = [0.1, 0.2, 0.3],
        bool_in: bool = False,
        string_in: str = "示例字符串",
        string_array_in: typing.Iterable[str] = [
            "带有/正斜杠的字符串",
            "带有\\反斜杠的字符串",
            "带有'单引号'的字符串",
            '带有"双引号"的字符串',
            "带有\t制表符的字符串",
            "带有\n换行符的字符串",
        ],
        path_in: pathlib.PurePath = pathlib.PurePath("示例\\路径\\用于\\测试"),
        path_array_in: typing.Iterable[pathlib.PurePath] = [
            pathlib.PurePath("路径/带有/正斜杠"),
            pathlib.PurePath("路径\\带有\\反斜杠"),
            pathlib.PurePath("路径 带有 '单引号'"),
            pathlib.PurePath('路径 带有 "双引号"'),
            pathlib.PurePath("路径\t带有\t制表符"),
            pathlib.PurePath("路径\n带有\n换行符"),
        ],
        io_in: str = "资源",
        io_array_in: typing.Iterable[str] = ["资源1", "资源2"],
        integer_in: int = 10,
        enum_in: EnumInEnum = EnumInEnum.BLUE,
        enum_array_in: typing.Iterable[EnumInEnum] = [EnumInEnum.RED, EnumInEnum.GREEN],
    ) -> Outputs:
        """Perform a single measurement.

        Returns:
            Measurement outputs.
        """
        stream_measure_response = self.stream_measure(
            float_in,
            double_array_in,
            bool_in,
            string_in,
            string_array_in,
            path_in,
            path_array_in,
            io_in,
            io_array_in,
            integer_in,
            enum_in,
            enum_array_in,
        )
        for response in stream_measure_response:
            result = response
        return result

    def stream_measure(
        self,
        float_in: float = 0.05999999865889549,
        double_array_in: typing.Iterable[float] = [0.1, 0.2, 0.3],
        bool_in: bool = False,
        string_in: str = "示例字符串",
        string_array_in: typing.Iterable[str] = [
            "带有/正斜杠的字符串",
            "带有\\反斜杠的字符串",
            "带有'单引号'的字符串",
            '带有"双引号"的字符串',
            "带有\t制表符的字符串",
            "带有\n换行符的字符串",
        ],
        path_in: pathlib.PurePath = pathlib.PurePath("示例\\路径\\用于\\测试"),
        path_array_in: typing.Iterable[pathlib.PurePath] = [
            pathlib.PurePath("路径/带有/正斜杠"),
            pathlib.PurePath("路径\\带有\\反斜杠"),
            pathlib.PurePath("路径 带有 '单引号'"),
            pathlib.PurePath('路径 带有 "双引号"'),
            pathlib.PurePath("路径\t带有\t制表符"),
            pathlib.PurePath("路径\n带有\n换行符"),
        ],
        io_in: str = "资源",
        io_array_in: typing.Iterable[str] = ["资源1", "资源2"],
        integer_in: int = 10,
        enum_in: EnumInEnum = EnumInEnum.BLUE,
        enum_array_in: typing.Iterable[EnumInEnum] = [EnumInEnum.RED, EnumInEnum.GREEN],
    ) -> typing.Generator[Outputs]:
        """Perform a streaming measurement.

        Returns:
            Stream of measurement outputs.
        """
        parameter_values = [
            float_in,
            double_array_in,
            bool_in,
            string_in,
            string_array_in,
            path_in,
            path_array_in,
            io_in,
            io_array_in,
            integer_in,
            enum_in,
            enum_array_in,
        ]
        with self._initialization_lock:
            if self._measure_response is not None:
                raise RuntimeError(
                    "A measurement is currently in progress. To make concurrent measurement requests, please create a new client instance."
                )
            request = self._create_measure_request(parameter_values)
            self._measure_response = self._get_stub().Measure(request)
        try:
            for response in self._measure_response:
                yield self._deserialize_response(response)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.CANCELLED:
                _logger.debug("The measurement is canceled.")
            raise
        finally:
            with self._initialization_lock:
                self._measure_response = None

    def cancel(self) -> bool:
        """Cancels the active measurement call."""
        with self._initialization_lock:
            if self._measure_response:
                return self._measure_response.cancel()
            else:
                return False

    def register_pin_map(self, pin_map_path: pathlib.Path) -> None:
        """Registers the pin map with the pin map service.

        Args:
            pin_map_path: Absolute path of the pin map file.
        """
        pin_map_id = self._get_pin_map_client().update_pin_map(pin_map_path)
        self._pin_map_context = self._pin_map_context._replace(pin_map_id=pin_map_id)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/test_assets/example_renders/measurement_plugin_client/non_streaming_data_measurement_client.py sha256=4c1e0ff9838882eecb5daaf96889d28fc931d7da2d6704dc0d4bb15481f609bf bytes=27203 -->
## FILE: packages/generator/tests/test_assets/example_renders/measurement_plugin_client/non_streaming_data_measurement_client.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/test_assets/example_renders/measurement_plugin_client/non_streaming_data_measurement_client.py`
- sha256: `4c1e0ff9838882eecb5daaf96889d28fc931d7da2d6704dc0d4bb15481f609bf`
- bytes: 27203

````python
"""Generated client API for the 'Non-Streaming Data Measurement (Py)' measurement plug-in."""

from __future__ import annotations

import logging
import pathlib
import threading
import typing
import warnings
from enum import Enum

import grpc
from google.protobuf import any_pb2, descriptor_pool
from google.protobuf.type_pb2 import Field
from ni.measurementlink.measurement.v2 import (
    measurement_service_pb2 as v2_measurement_service_pb2,
    measurement_service_pb2_grpc as v2_measurement_service_pb2_grpc,
)
from ni.protobuf.types.array_pb2 import Double2DArray
from ni.protobuf.types.array_pb2 import String2DArray
from ni.protobuf.types.xydata_pb2 import DoubleXYData
from ni_grpc_extensions.channelpool import GrpcChannelPool
from ni.measurementlink.discovery.v1.client import DiscoveryClient
from ni.measurementlink.sessionmanagement.v1.client import PinMapContext
from ni_measurement_plugin_sdk_service.measurement import WrongMessageTypeWarning
from ni_measurement_plugin_sdk_service.measurement.client_support import (
    ParameterMetadata,
    create_file_descriptor,
    deserialize_parameters,
    serialize_parameters,
)
from ni.measurementlink.pinmap.v1.client import PinMapClient

_logger = logging.getLogger(__name__)

_V2_MEASUREMENT_SERVICE_INTERFACE = "ni.measurementlink.measurement.v2.MeasurementService"


class EnumInEnum(Enum):
    """EnumInEnum used for enum-typed measurement configs and outputs."""

    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3


class ProtobufEnumInEnum(Enum):
    """ProtobufEnumInEnum used for enum-typed measurement configs and outputs."""

    NONE = 0
    PINK = 1
    WHITE = 2
    BLACK = 3


class Outputs(typing.NamedTuple):
    """Outputs for the 'Non-Streaming Data Measurement (Py)' measurement plug-in."""

    float_out: float
    double_array_out: typing.Sequence[float]
    bool_out: bool
    string_out: str
    string_array_out: typing.Sequence[str]
    path_out: pathlib.Path
    path_array_out: typing.Sequence[pathlib.Path]
    io_out: str
    io_array_out: typing.Sequence[str]
    integer_out: int
    xy_data_out: DoubleXYData
    enum_out: EnumInEnum
    enum_array_out: typing.Sequence[EnumInEnum]
    protobuf_enum_out: ProtobufEnumInEnum
    double_2d_array_out: Double2DArray
    string_2d_array_out: String2DArray


class NonStreamingDataMeasurementClient:
    """Client for the 'Non-Streaming Data Measurement (Py)' measurement plug-in."""

    def __init__(
        self,
        *,
        discovery_client: DiscoveryClient | None = None,
        pin_map_client: PinMapClient | None = None,
        grpc_channel: grpc.Channel | None = None,
        grpc_channel_pool: GrpcChannelPool | None = None,
    ):
        """Initialize the Measurement Plug-In Client.

        Args:
            discovery_client: An optional discovery client.

            pin_map_client: An optional pin map client.

            grpc_channel: An optional gRPC channel targeting a measurement service.

            grpc_channel_pool: An optional gRPC channel pool.
        """
        self._initialization_lock = threading.RLock()
        self._service_class = "ni.tests.NonStreamingDataMeasurement_Python"
        self._version = "0.1.0.0"
        self._grpc_channel_pool = grpc_channel_pool
        self._discovery_client = discovery_client
        self._pin_map_client = pin_map_client
        self._stub: v2_measurement_service_pb2_grpc.MeasurementServiceStub | None = None
        self._measure_response: None | (
            grpc._CallIterator[v2_measurement_service_pb2.MeasureResponse]
        ) = None
        self._configuration_metadata = {
            1: ParameterMetadata(
                display_name="Float In",
                type=Field.Kind.ValueType(2),
                repeated=False,
                default_value=0.05999999865889549,
                annotations={},
                message_type="",
                field_name="Float_In",
                enum_type=None,
            ),
            2: ParameterMetadata(
                display_name="Double Array In",
                type=Field.Kind.ValueType(1),
                repeated=True,
                default_value=[0.1, 0.2, 0.3],
                annotations={},
                message_type="",
                field_name="Double_Array_In",
                enum_type=None,
            ),
            3: ParameterMetadata(
                display_name="Bool In",
                type=Field.Kind.ValueType(8),
                repeated=False,
                default_value=False,
                annotations={},
                message_type="",
                field_name="Bool_In",
                enum_type=None,
            ),
            4: ParameterMetadata(
                display_name="String In",
                type=Field.Kind.ValueType(9),
                repeated=False,
                default_value="sample string",
                annotations={},
                message_type="",
                field_name="String_In",
                enum_type=None,
            ),
            5: ParameterMetadata(
                display_name="String Array In",
                type=Field.Kind.ValueType(9),
                repeated=True,
                default_value=[
                    "string with /forwardslash",
                    "string with \\backslash",
                    "string with 'single quotes'",
                    'string with "double quotes"',
                    "string with \ttabspace",
                    "string with \nnewline",
                ],
                annotations={},
                message_type="",
                field_name="String_Array_In",
                enum_type=None,
            ),
            6: ParameterMetadata(
                display_name="Path In",
                type=Field.Kind.ValueType(9),
                repeated=False,
                default_value="sample\\path\\for\\test",
                annotations={"ni/type_specialization": "path"},
                message_type="",
                field_name="Path_In",
                enum_type=None,
            ),
            7: ParameterMetadata(
                display_name="Path Array In",
                type=Field.Kind.ValueType(9),
                repeated=True,
                default_value=[
                    "path/with/forward/slash",
                    "path\\with\\backslash",
                    "path with 'single quotes'",
                    'path with "double quotes"',
                    "path\twith\ttabs",
                    "path\nwith\nnewlines",
                ],
                annotations={"ni/type_specialization": "path"},
                message_type="",
                field_name="Path_Array_In",
                enum_type=None,
            ),
            8: ParameterMetadata(
                display_name="IO In",
                type=Field.Kind.ValueType(9),
                repeated=False,
                default_value="resource",
                annotations={
                    "ni/ioresource.instrument_type": "",
                    "ni/type_specialization": "ioresource",
                },
                message_type="",
                field_name="IO_In",
                enum_type=None,
            ),
            9: ParameterMetadata(
                display_name="IO Array In",
                type=Field.Kind.ValueType(9),
                repeated=True,
                default_value=["resource1", "resource2"],
                annotations={
                    "ni/ioresource.instrument_type": "",
                    "ni/type_specialization": "ioresource",
                },
                message_type="",
                field_name="IO_Array_In",
                enum_type=None,
            ),
            10: ParameterMetadata(
                display_name="Integer In",
                type=Field.Kind.ValueType(5),
                repeated=False,
                default_value=10,
                annotations={},
                message_type="",
                field_name="Integer_In",
                enum_type=None,
            ),
            11: ParameterMetadata(
                display_name="Enum In",
                type=Field.Kind.ValueType(14),
                repeated=False,
                default_value=3,
                annotations={
                    "ni/enum.values": '{"NONE": 0, "RED": 1, "GREEN": 2, "BLUE": 3}',
                    "ni/type_specialization": "enum",
                },
                message_type="",
                field_name="Enum_In",
                enum_type=EnumInEnum,
            ),
            12: ParameterMetadata(
                display_name="Enum Array In",
                type=Field.Kind.ValueType(14),
                repeated=True,
                default_value=[1, 2],
                annotations={
                    "ni/enum.values": '{"NONE": 0, "RED": 1, "GREEN": 2, "BLUE": 3}',
                    "ni/type_specialization": "enum",
                },
                message_type="",
                field_name="Enum_Array_In",
                enum_type=EnumInEnum,
            ),
            13: ParameterMetadata(
                display_name="Protobuf Enum In",
                type=Field.Kind.ValueType(14),
                repeated=False,
                default_value=3,
                annotations={
                    "ni/enum.values": '{"NONE": 0, "PINK": 1, "WHITE": 2, "BLACK": 3}',
                    "ni/type_specialization": "enum",
                },
                message_type="",
                field_name="Protobuf_Enum_In",
                enum_type=ProtobufEnumInEnum,
            ),
        }
        self._output_metadata = {
            1: ParameterMetadata(
                display_name="Float out",
                type=Field.Kind.ValueType(2),
                repeated=False,
                default_value=None,
                annotations={},
                message_type="",
                field_name="Float_out",
                enum_type=None,
            ),
            2: ParameterMetadata(
                display_name="Double Array out",
                type=Field.Kind.ValueType(1),
                repeated=True,
                default_value=None,
                annotations={},
                message_type="",
                field_name="Double_Array_out",
                enum_type=None,
            ),
            3: ParameterMetadata(
                display_name="Bool out",
                type=Field.Kind.ValueType(8),
                repeated=False,
                default_value=None,
                annotations={},
                message_type="",
                field_name="Bool_out",
                enum_type=None,
            ),
            4: ParameterMetadata(
                display_name="String out",
                type=Field.Kind.ValueType(9),
                repeated=False,
                default_value=None,
                annotations={},
                message_type="",
                field_name="String_out",
                enum_type=None,
            ),
            5: ParameterMetadata(
                display_name="String Array out",
                type=Field.Kind.ValueType(9),
                repeated=True,
                default_value=None,
                annotations={},
                message_type="",
                field_name="String_Array_out",
                enum_type=None,
            ),
            6: ParameterMetadata(
                display_name="Path Out",
                type=Field.Kind.ValueType(9),
                repeated=False,
                default_value=None,
                annotations={"ni/type_specialization": "path"},
                message_type="",
                field_name="Path_Out",
                enum_type=None,
            ),
            7: ParameterMetadata(
                display_name="Path Array Out",
                type=Field.Kind.ValueType(9),
                repeated=True,
                default_value=None,
                annotations={"ni/type_specialization": "path"},
                message_type="",
                field_name="Path_Array_Out",
                enum_type=None,
            ),
            8: ParameterMetadata(
                display_name="IO Out",
                type=Field.Kind.ValueType(9),
                repeated=False,
                default_value=None,
                annotations={
                    "ni/ioresource.instrument_type": "",
                    "ni/type_specialization": "ioresource",
                },
                message_type="",
                field_name="IO_Out",
                enum_type=None,
            ),
            9: ParameterMetadata(
                display_name="IO Array Out",
                type=Field.Kind.ValueType(9),
                repeated=True,
                default_value=None,
                annotations={
                    "ni/ioresource.instrument_type": "",
                    "ni/type_specialization": "ioresource",
                },
                message_type="",
                field_name="IO_Array_Out",
                enum_type=None,
            ),
            10: ParameterMetadata(
                display_name="Integer Out",
                type=Field.Kind.ValueType(5),
                repeated=False,
                default_value=None,
                annotations={},
                message_type="",
                field_name="Integer_Out",
                enum_type=None,
            ),
            11: ParameterMetadata(
                display_name="XY Data Out",
                type=Field.Kind.ValueType(11),
                repeated=False,
                default_value=None,
                annotations={},
                message_type="ni.protobuf.types.DoubleXYData",
                field_name="XY_Data_Out",
                enum_type=None,
            ),
            12: ParameterMetadata(
                display_name="Enum Out",
                type=Field.Kind.ValueType(14),
                repeated=False,
                default_value=None,
                annotations={
                    "ni/enum.values": '{"NONE": 0, "RED": 1, "GREEN": 2, "BLUE": 3}',
                    "ni/type_specialization": "enum",
                },
                message_type="",
                field_name="Enum_Out",
                enum_type=EnumInEnum,
            ),
            13: ParameterMetadata(
                display_name="Enum Array Out",
                type=Field.Kind.ValueType(14),
                repeated=True,
                default_value=None,
                annotations={
                    "ni/enum.values": '{"NONE": 0, "RED": 1, "GREEN": 2, "BLUE": 3}',
                    "ni/type_specialization": "enum",
                },
                message_type="",
                field_name="Enum_Array_Out",
                enum_type=EnumInEnum,
            ),
            14: ParameterMetadata(
                display_name="Protobuf Enum out",
                type=Field.Kind.ValueType(14),
                repeated=False,
                default_value=None,
                annotations={
                    "ni/enum.values": '{"NONE": 0, "PINK": 1, "WHITE": 2, "BLACK": 3}',
                    "ni/type_specialization": "enum",
                },
                message_type="",
                field_name="Protobuf_Enum_out",
                enum_type=ProtobufEnumInEnum,
            ),
            15: ParameterMetadata(
                display_name="Double 2D Array out",
                type=Field.Kind.ValueType(11),
                repeated=False,
                default_value=None,
                annotations={},
                message_type="ni.protobuf.types.Double2DArray",
                field_name="Double_2D_Array_out",
                enum_type=None,
            ),
            16: ParameterMetadata(
                display_name="String 2D Array out",
                type=Field.Kind.ValueType(11),
                repeated=False,
                default_value=None,
                annotations={},
                message_type="ni.protobuf.types.String2DArray",
                field_name="String_2D_Array_out",
                enum_type=None,
            ),
        }
        if grpc_channel is not None:
            self._stub = v2_measurement_service_pb2_grpc.MeasurementServiceStub(grpc_channel)
        self._create_file_descriptor()
        self._pin_map_context: PinMapContext = PinMapContext(pin_map_id="", sites=[0])

    @property
    def pin_map_context(self) -> PinMapContext:
        """The pin map context for the measurement."""
        return self._pin_map_context

    @pin_map_context.setter
    def pin_map_context(self, val: PinMapContext) -> None:
        if not isinstance(val, PinMapContext):
            raise TypeError(
                f"Invalid type {type(val)}: The given value must be an instance of PinMapContext."
            )
        self._pin_map_context = val

    @property
    def sites(self) -> list[int] | None:
        """The sites where the measurement must be executed."""
        return self._pin_map_context.sites

    @sites.setter
    def sites(self, val: list[int]) -> None:
        if self._pin_map_context is None:
            raise AttributeError(
                "Cannot set sites because the pin map context is None. Please provide a pin map context or register a pin map before setting sites."
            )
        self._pin_map_context = self._pin_map_context._replace(sites=val)

    def _get_stub(self) -> v2_measurement_service_pb2_grpc.MeasurementServiceStub:
        if self._stub is None:
            with self._initialization_lock:
                if self._stub is None:
                    service_location = self._get_discovery_client().resolve_service(
                        provided_interface=_V2_MEASUREMENT_SERVICE_INTERFACE,
                        service_class=self._service_class,
                        version=self._version,
                    )
                    channel = self._get_grpc_channel_pool().get_channel(
                        service_location.insecure_address
                    )
                    self._stub = v2_measurement_service_pb2_grpc.MeasurementServiceStub(channel)
        return self._stub

    def _get_discovery_client(self) -> DiscoveryClient:
        if self._discovery_client is None:
            with self._initialization_lock:
                if self._discovery_client is None:
                    self._discovery_client = DiscoveryClient(
                        grpc_channel_pool=self._get_grpc_channel_pool(),
                    )
        return self._discovery_client

    def _get_grpc_channel_pool(self) -> GrpcChannelPool:
        if self._grpc_channel_pool is None:
            with self._initialization_lock:
                if self._grpc_channel_pool is None:
                    self._grpc_channel_pool = GrpcChannelPool()
        return self._grpc_channel_pool

    def _get_pin_map_client(self) -> PinMapClient:
        if self._pin_map_client is None:
            with self._initialization_lock:
                if self._pin_map_client is None:
                    self._pin_map_client = PinMapClient(
                        discovery_client=self._get_discovery_client(),
                        grpc_channel_pool=self._get_grpc_channel_pool(),
                    )
        return self._pin_map_client

    def _create_file_descriptor(self) -> None:
        create_file_descriptor(
            input_metadata=list(self._configuration_metadata.values()),
            output_metadata=list(self._output_metadata.values()),
            service_name=self._service_class,
            pool=descriptor_pool.Default(),
        )

    def _create_measure_request(
        self, parameter_values: list[typing.Any]
    ) -> v2_measurement_service_pb2.MeasureRequest:
        serialized_configuration = any_pb2.Any(
            type_url="type.googleapis.com/ni.tests.NonStreamingDataMeasurement_Python.Configurations",
            value=serialize_parameters(
                self._configuration_metadata,
                parameter_values,
                f"{self._service_class}.Configurations",
            ),
        )
        return v2_measurement_service_pb2.MeasureRequest(
            configuration_parameters=serialized_configuration,
            pin_map_context=self._pin_map_context._to_grpc(),
        )

    def _deserialize_response(
        self, response: v2_measurement_service_pb2.MeasureResponse
    ) -> Outputs:
        self._validate_response(response)
        return Outputs._make(
            deserialize_parameters(
                self._output_metadata,
                response.outputs.value,
                f"{self._service_class}.Outputs",
            )
        )

    def _validate_response(self, response: v2_measurement_service_pb2.MeasureResponse) -> None:
        expected_type = (
            "type.googleapis.com/" + "ni.tests.NonStreamingDataMeasurement_Python.Outputs"
        )
        actual_type = response.outputs.type_url
        if actual_type != expected_type:
            warnings.warn(
                f"Wrong message type. Expected {expected_type!r} but got {actual_type!r}",
                WrongMessageTypeWarning,
            )

    def measure(
        self,
        float_in: float = 0.05999999865889549,
        double_array_in: typing.Iterable[float] = [0.1, 0.2, 0.3],
        bool_in: bool = False,
        string_in: str = "sample string",
        string_array_in: typing.Iterable[str] = [
            "string with /forwardslash",
            "string with \\backslash",
            "string with 'single quotes'",
            'string with "double quotes"',
            "string with \ttabspace",
            "string with \nnewline",
        ],
        path_in: pathlib.PurePath = pathlib.PurePath("sample\\path\\for\\test"),
        path_array_in: typing.Iterable[pathlib.PurePath] = [
            pathlib.PurePath("path/with/forward/slash"),
            pathlib.PurePath("path\\with\\backslash"),
            pathlib.PurePath("path with 'single quotes'"),
            pathlib.PurePath('path with "double quotes"'),
            pathlib.PurePath("path\twith\ttabs"),
            pathlib.PurePath("path\nwith\nnewlines"),
        ],
        io_in: str = "resource",
        io_array_in: typing.Iterable[str] = ["resource1", "resource2"],
        integer_in: int = 10,
        enum_in: EnumInEnum = EnumInEnum.BLUE,
        enum_array_in: typing.Iterable[EnumInEnum] = [EnumInEnum.RED, EnumInEnum.GREEN],
        protobuf_enum_in: ProtobufEnumInEnum = ProtobufEnumInEnum.BLACK,
    ) -> Outputs:
        """Perform a single measurement.

        Returns:
            Measurement outputs.
        """
        stream_measure_response = self.stream_measure(
            float_in,
            double_array_in,
            bool_in,
            string_in,
            string_array_in,
            path_in,
            path_array_in,
            io_in,
            io_array_in,
            integer_in,
            enum_in,
            enum_array_in,
            protobuf_enum_in,
        )
        for response in stream_measure_response:
            result = response
        return result

    def stream_measure(
        self,
        float_in: float = 0.05999999865889549,
        double_array_in: typing.Iterable[float] = [0.1, 0.2, 0.3],
        bool_in: bool = False,
        string_in: str = "sample string",
        string_array_in: typing.Iterable[str] = [
            "string with /forwardslash",
            "string with \\backslash",
            "string with 'single quotes'",
            'string with "double quotes"',
            "string with \ttabspace",
            "string with \nnewline",
        ],
        path_in: pathlib.PurePath = pathlib.PurePath("sample\\path\\for\\test"),
        path_array_in: typing.Iterable[pathlib.PurePath] = [
            pathlib.PurePath("path/with/forward/slash"),
            pathlib.PurePath("path\\with\\backslash"),
            pathlib.PurePath("path with 'single quotes'"),
            pathlib.PurePath('path with "double quotes"'),
            pathlib.PurePath("path\twith\ttabs"),
            pathlib.PurePath("path\nwith\nnewlines"),
        ],
        io_in: str = "resource",
        io_array_in: typing.Iterable[str] = ["resource1", "resource2"],
        integer_in: int = 10,
        enum_in: EnumInEnum = EnumInEnum.BLUE,
        enum_array_in: typing.Iterable[EnumInEnum] = [EnumInEnum.RED, EnumInEnum.GREEN],
        protobuf_enum_in: ProtobufEnumInEnum = ProtobufEnumInEnum.BLACK,
    ) -> typing.Generator[Outputs]:
        """Perform a streaming measurement.

        Returns:
            Stream of measurement outputs.
        """
        parameter_values = [
            float_in,
            double_array_in,
            bool_in,
            string_in,
            string_array_in,
            path_in,
            path_array_in,
            io_in,
            io_array_in,
            integer_in,
            enum_in,
            enum_array_in,
            protobuf_enum_in,
        ]
        with self._initialization_lock:
            if self._measure_response is not None:
                raise RuntimeError(
                    "A measurement is currently in progress. To make concurrent measurement requests, please create a new client instance."
                )
            request = self._create_measure_request(parameter_values)
            self._measure_response = self._get_stub().Measure(request)
        try:
            for response in self._measure_response:
                yield self._deserialize_response(response)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.CANCELLED:
                _logger.debug("The measurement is canceled.")
            raise
        finally:
            with self._initialization_lock:
                self._measure_response = None

    def cancel(self) -> bool:
        """Cancels the active measurement call."""
        with self._initialization_lock:
            if self._measure_response:
                return self._measure_response.cancel()
            else:
                return False

    def register_pin_map(self, pin_map_path: pathlib.Path) -> None:
        """Registers the pin map with the pin map service.

        Args:
            pin_map_path: Absolute path of the pin map file.
        """
        pin_map_id = self._get_pin_map_client().update_pin_map(pin_map_path)
        self._pin_map_context = self._pin_map_context._replace(pin_map_id=pin_map_id)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/test_assets/example_renders/measurement_plugin_client/void_measurement_client.py sha256=b2349f82bf18204cfe687b62104f3d42140de2271386c1b31332349740b24cb6 bytes=9007 -->
## FILE: packages/generator/tests/test_assets/example_renders/measurement_plugin_client/void_measurement_client.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/test_assets/example_renders/measurement_plugin_client/void_measurement_client.py`
- sha256: `b2349f82bf18204cfe687b62104f3d42140de2271386c1b31332349740b24cb6`
- bytes: 9007

````python
"""Generated client API for the 'Void Measurement (Py)' measurement plug-in."""

from __future__ import annotations

import logging
import pathlib
import threading
import typing

import grpc
from google.protobuf import any_pb2, descriptor_pool
from google.protobuf.type_pb2 import Field
from ni.measurementlink.measurement.v2 import (
    measurement_service_pb2 as v2_measurement_service_pb2,
    measurement_service_pb2_grpc as v2_measurement_service_pb2_grpc,
)
from ni_grpc_extensions.channelpool import GrpcChannelPool
from ni.measurementlink.discovery.v1.client import DiscoveryClient
from ni.measurementlink.sessionmanagement.v1.client import PinMapContext
from ni_measurement_plugin_sdk_service.measurement.client_support import (
    ParameterMetadata,
    create_file_descriptor,
    serialize_parameters,
)
from ni.measurementlink.pinmap.v1.client import PinMapClient

_logger = logging.getLogger(__name__)

_V2_MEASUREMENT_SERVICE_INTERFACE = "ni.measurementlink.measurement.v2.MeasurementService"


class VoidMeasurementClient:
    """Client for the 'Void Measurement (Py)' measurement plug-in."""

    def __init__(
        self,
        *,
        discovery_client: DiscoveryClient | None = None,
        pin_map_client: PinMapClient | None = None,
        grpc_channel: grpc.Channel | None = None,
        grpc_channel_pool: GrpcChannelPool | None = None,
    ):
        """Initialize the Measurement Plug-In Client.

        Args:
            discovery_client: An optional discovery client.

            pin_map_client: An optional pin map client.

            grpc_channel: An optional gRPC channel targeting a measurement service.

            grpc_channel_pool: An optional gRPC channel pool.
        """
        self._initialization_lock = threading.RLock()
        self._service_class = "ni.tests.VoidMeasurement_Python"
        self._version = "0.1.0.0"
        self._grpc_channel_pool = grpc_channel_pool
        self._discovery_client = discovery_client
        self._pin_map_client = pin_map_client
        self._stub: v2_measurement_service_pb2_grpc.MeasurementServiceStub | None = None
        self._measure_response: None | (
            grpc._CallIterator[v2_measurement_service_pb2.MeasureResponse]
        ) = None
        self._configuration_metadata = {
            1: ParameterMetadata(
                display_name="Integer In",
                type=Field.Kind.ValueType(5),
                repeated=False,
                default_value=10,
                annotations={},
                message_type="",
                field_name="Integer_In",
                enum_type=None,
            ),
        }
        self._output_metadata = {}
        if grpc_channel is not None:
            self._stub = v2_measurement_service_pb2_grpc.MeasurementServiceStub(grpc_channel)
        self._create_file_descriptor()
        self._pin_map_context: PinMapContext = PinMapContext(pin_map_id="", sites=[0])

    @property
    def pin_map_context(self) -> PinMapContext:
        """The pin map context for the measurement."""
        return self._pin_map_context

    @pin_map_context.setter
    def pin_map_context(self, val: PinMapContext) -> None:
        if not isinstance(val, PinMapContext):
            raise TypeError(
                f"Invalid type {type(val)}: The given value must be an instance of PinMapContext."
            )
        self._pin_map_context = val

    @property
    def sites(self) -> list[int] | None:
        """The sites where the measurement must be executed."""
        return self._pin_map_context.sites

    @sites.setter
    def sites(self, val: list[int]) -> None:
        if self._pin_map_context is None:
            raise AttributeError(
                "Cannot set sites because the pin map context is None. Please provide a pin map context or register a pin map before setting sites."
            )
        self._pin_map_context = self._pin_map_context._replace(sites=val)

    def _get_stub(self) -> v2_measurement_service_pb2_grpc.MeasurementServiceStub:
        if self._stub is None:
            with self._initialization_lock:
                if self._stub is None:
                    service_location = self._get_discovery_client().resolve_service(
                        provided_interface=_V2_MEASUREMENT_SERVICE_INTERFACE,
                        service_class=self._service_class,
                        version=self._version,
                    )
                    channel = self._get_grpc_channel_pool().get_channel(
                        service_location.insecure_address
                    )
                    self._stub = v2_measurement_service_pb2_grpc.MeasurementServiceStub(channel)
        return self._stub

    def _get_discovery_client(self) -> DiscoveryClient:
        if self._discovery_client is None:
            with self._initialization_lock:
                if self._discovery_client is None:
                    self._discovery_client = DiscoveryClient(
                        grpc_channel_pool=self._get_grpc_channel_pool(),
                    )
        return self._discovery_client

    def _get_grpc_channel_pool(self) -> GrpcChannelPool:
        if self._grpc_channel_pool is None:
            with self._initialization_lock:
                if self._grpc_channel_pool is None:
                    self._grpc_channel_pool = GrpcChannelPool()
        return self._grpc_channel_pool

    def _get_pin_map_client(self) -> PinMapClient:
        if self._pin_map_client is None:
            with self._initialization_lock:
                if self._pin_map_client is None:
                    self._pin_map_client = PinMapClient(
                        discovery_client=self._get_discovery_client(),
                        grpc_channel_pool=self._get_grpc_channel_pool(),
                    )
        return self._pin_map_client

    def _create_file_descriptor(self) -> None:
        create_file_descriptor(
            input_metadata=list(self._configuration_metadata.values()),
            output_metadata=list(self._output_metadata.values()),
            service_name=self._service_class,
            pool=descriptor_pool.Default(),
        )

    def _create_measure_request(
        self, parameter_values: list[typing.Any]
    ) -> v2_measurement_service_pb2.MeasureRequest:
        serialized_configuration = any_pb2.Any(
            type_url="type.googleapis.com/ni.tests.VoidMeasurement_Python.Configurations",
            value=serialize_parameters(
                self._configuration_metadata,
                parameter_values,
                f"{self._service_class}.Configurations",
            ),
        )
        return v2_measurement_service_pb2.MeasureRequest(
            configuration_parameters=serialized_configuration,
            pin_map_context=self._pin_map_context._to_grpc(),
        )

    def measure(self, integer_in: int = 10) -> None:
        """Perform a single measurement.

        Returns:
            Measurement outputs.
        """
        stream_measure_response = self.stream_measure(integer_in)
        for response in stream_measure_response:
            pass

    def stream_measure(self, integer_in: int = 10) -> typing.Generator[None]:
        """Perform a streaming measurement.

        Returns:
            Stream of measurement outputs.
        """
        parameter_values = [integer_in]
        with self._initialization_lock:
            if self._measure_response is not None:
                raise RuntimeError(
                    "A measurement is currently in progress. To make concurrent measurement requests, please create a new client instance."
                )
            request = self._create_measure_request(parameter_values)
            self._measure_response = self._get_stub().Measure(request)
        try:
            for response in self._measure_response:
                yield
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.CANCELLED:
                _logger.debug("The measurement is canceled.")
            raise
        finally:
            with self._initialization_lock:
                self._measure_response = None

    def cancel(self) -> bool:
        """Cancels the active measurement call."""
        with self._initialization_lock:
            if self._measure_response:
                return self._measure_response.cancel()
            else:
                return False

    def register_pin_map(self, pin_map_path: pathlib.Path) -> None:
        """Registers the pin map with the pin map service.

        Args:
            pin_map_path: Absolute path of the pin map file.
        """
        pin_map_id = self._get_pin_map_client().update_pin_map(pin_map_path)
        self._pin_map_context = self._pin_map_context._replace(pin_map_id=pin_map_id)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/test_assets/example_renders/measurement_with_annotations/_helpers.py sha256=0b6eb9115ad502973ae4caac7dca9f4387d0510dc6967769e9968e9ada149426 bytes=2920 -->
## FILE: packages/generator/tests/test_assets/example_renders/measurement_with_annotations/_helpers.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/test_assets/example_renders/measurement_with_annotations/_helpers.py`
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

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/test_assets/example_renders/measurement_with_annotations/measurement.py sha256=42f666429e52e0da3741a45ac9eeffd395b21fb2ebf9e34bacbe4102ee53f59c bytes=1504 -->
## FILE: packages/generator/tests/test_assets/example_renders/measurement_with_annotations/measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/test_assets/example_renders/measurement_with_annotations/measurement.py`
- sha256: `42f666429e52e0da3741a45ac9eeffd395b21fb2ebf9e34bacbe4102ee53f59c`
- bytes: 1504

````python
"""A default measurement with an array in and out."""

import logging
import pathlib
import sys

import click
import ni_measurement_plugin_sdk_service as nims

script_or_exe = sys.executable if getattr(sys, "frozen", False) else __file__
service_directory = pathlib.Path(script_or_exe).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "SampleMeasurement.serviceconfig",
    ui_file_paths=[service_directory / "MeasurementUI.measui"],
)


@measurement_service.register_measurement
@measurement_service.configuration("Array in", nims.DataType.DoubleArray1D, [0.0])
@measurement_service.output("Array out", nims.DataType.DoubleArray1D)
def measure(array_input):
    """TODO: replace the following line with your own measurement logic."""
    array_output = array_input
    return (array_output,)


@click.command
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Enable verbose logging. Repeat to increase verbosity.",
)
def main(verbose: int) -> None:
    """Host the Sample Measurement service."""
    if verbose > 1:
        level = logging.DEBUG
    elif verbose == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=level)

    with measurement_service.host_service():
        input("Press enter to close the measurement service.\n")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/test_assets/example_renders/measurement_with_annotations/SampleMeasurement.serviceconfig sha256=e3bb9b8b56f3691f57105a257bdc833abd85ad154c61afa8e66233e2f548b2ce bytes=683 -->
## FILE: packages/generator/tests/test_assets/example_renders/measurement_with_annotations/SampleMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/test_assets/example_renders/measurement_with_annotations/SampleMeasurement.serviceconfig`
- sha256: `e3bb9b8b56f3691f57105a257bdc833abd85ad154c61afa8e66233e2f548b2ce`
- bytes: 683

````json
{
  "services": [
    {
      "displayName": "Sample Measurement",
      "serviceClass": "SampleMeasurement_Python",
      "descriptionUrl": "https://www.example.com/SampleMeasurement.html",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "version": "1.2.3.4",
      "annotations": {
        "ni/service.description": "Measurement description",
        "ni/service.collection": "Measurement.Collection",
        "ni/service.tags": [
          "M1",
          "M2",
          "M3"
        ]
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/test_assets/example_renders/measurement_with_annotations/start.bat sha256=bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851 bytes=253 -->
## FILE: packages/generator/tests/test_assets/example_renders/measurement_with_annotations/start.bat

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/test_assets/example_renders/measurement_with_annotations/start.bat`
- sha256: `bc3f7db64fca775105c409147e122fa2870c3861f95c8238bbc0340d97251851`
- bytes: 253

````batch
@echo off
REM The discovery service uses this script to start the measurement service.
REM You can customize this script for your Python setup. The -v option logs
REM messages with level INFO and above.

.venv\Scripts\python.exe measurement.py -v
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/test_assets/pin_map/1Smu1ChannelGroup1Pin1Site.pinmap sha256=3bfd0e7dbb4bec1f88d9bf3bfd1c11b655c2850a7a73e0259cdc99d9b17646e3 bytes=605 -->
## FILE: packages/generator/tests/test_assets/pin_map/1Smu1ChannelGroup1Pin1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/test_assets/pin_map/1Smu1ChannelGroup1Pin1Site.pinmap`
- sha256: `3bfd0e7dbb4bec1f88d9bf3bfd1c11b655c2850a7a73e0259cdc99d9b17646e3`
- bytes: 605

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.6">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="CommonDCPowerChannelGroup" />
		</NIDCPowerInstrument>
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="DCPower1" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/test_assets/pin_map/1Smu1ChannelGroup2Pin2Site.pinmap sha256=af0472e6543663b5894964008c800014a544f43ef88531aca5f91226189b18da bytes=892 -->
## FILE: packages/generator/tests/test_assets/pin_map/1Smu1ChannelGroup2Pin2Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/test_assets/pin_map/1Smu1ChannelGroup2Pin2Site.pinmap`
- sha256: `af0472e6543663b5894964008c800014a544f43ef88531aca5f91226189b18da`
- bytes: 892

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.6">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="CommonDCPowerChannelGroup" />
		</NIDCPowerInstrument>
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
		<DUTPin name="Pin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="DCPower1" channel="0" />
		<Connection pin="Pin2" siteNumber="0" instrument="DCPower1" channel="1" />
		<Connection pin="Pin1" siteNumber="1" instrument="DCPower1" channel="2" />
		<Connection pin="Pin2" siteNumber="1" instrument="DCPower1" channel="3" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/unit/test_measurement_client.py sha256=47d7aa7200539fb8d98972883800dfeb0f1a63ab832ae25d612f97ec4ba1cc91 bytes=1294 -->
## FILE: packages/generator/tests/unit/test_measurement_client.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/unit/test_measurement_client.py`
- sha256: `47d7aa7200539fb8d98972883800dfeb0f1a63ab832ae25d612f97ec4ba1cc91`
- bytes: 1294

````python
import pytest
from click import ClickException

from ni_measurement_plugin_sdk_generator.client._support import (
    _validate_and_transform_enum_annotations,
)


@pytest.mark.parametrize(
    "enum_annotations, expected_enum_annotations",
    [
        ('{"NONE": 0, "RED": 1, "GREEN": 2}', '{"NONE": 0, "RED": 1, "GREEN": 2}'),
        (
            '{"DC Volts": 0, "2-Wire Resistance": 1, "5 1/2": 2}',
            '{"DC_Volts": 0, "k_2_Wire_Resistance": 1, "k_5_1_2": 2}',
        ),
    ],
)
def test___enum_annotations___validate_and_transform_enum_annotations___returns_expected_enum_annotations(
    enum_annotations: str, expected_enum_annotations: str
) -> None:
    actual_enum_annotations = _validate_and_transform_enum_annotations(enum_annotations)

    assert actual_enum_annotations == expected_enum_annotations


def test___invalid_enum_annotations___validate_and_transform_enum_annotations___raises_invalid_enum_value_error() -> (
    None
):
    enum_annotations = '{"DC Volts": 0, "*": 1}'
    expected_error_message = "The enum value '*' is invalid."

    with pytest.raises(ClickException) as exc_info:
        _ = _validate_and_transform_enum_annotations(enum_annotations)

    assert exc_info.value.message == expected_error_message
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/utilities/discovery_service_process.py sha256=e0a3fcb5518025d0c8a0b0c79b25f3d702b91a17f0fc3c7664b2c64d200b9db3 bytes=1594 -->
## FILE: packages/generator/tests/utilities/discovery_service_process.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/utilities/discovery_service_process.py`
- sha256: `e0a3fcb5518025d0c8a0b0c79b25f3d702b91a17f0fc3c7664b2c64d200b9db3`
- bytes: 1594

````python
"""Class to create and terminate Discovery Service instance."""

from __future__ import annotations

from types import TracebackType

from ni.measurementlink.discovery.v1.client._support import (
    _get_discovery_service_location,
    _get_key_file_path,
    _service_already_running,
    _start_service,
)
from typing_extensions import Self


class DiscoveryServiceProcess:
    """Maintains the processes involved in creating and terminating discovery service."""

    def __init__(self) -> None:
        """Creates a DiscoveryServiceProcess instance."""
        try:
            self._proc = None
            key_file_path = _get_key_file_path()
            if _service_already_running(key_file_path):
                return
            self._proc = _start_service(_get_discovery_service_location(), key_file_path)
        except Exception:
            self._close_discovery_service()
            raise

    def __enter__(self: Self) -> Self:
        """Returns the DiscoveryServiceProcess instance."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Closes the DiscoveryServiceProcess instance."""
        self._close_discovery_service()

    def _close_discovery_service(self) -> None:
        if self._proc is not None:
            self._proc.kill()
            # Use communicate() to close the stdout pipe and wait for the server process to exit.
            self._proc.communicate()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/localized_measurement/__init__.py sha256=a9264d31cc39bc525206a6ce04fdcf16e31dc96448be661d009f0c7e515fbb96 bytes=5442 -->
## FILE: packages/generator/tests/utilities/measurements/localized_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/utilities/measurements/localized_measurement/__init__.py`
- sha256: `a9264d31cc39bc525206a6ce04fdcf16e31dc96448be661d009f0c7e515fbb96`
- bytes: 5442

````python
"""Contains utility functions to test loopback measurement service with non-ASCII characters."""

from collections.abc import Iterable
from enum import Enum
from pathlib import Path

import ni_measurement_plugin_sdk_service as nims
from ni.protobuf.types import array_pb2, xydata_pb2

from tests.utilities.measurements.non_streaming_data_measurement._stubs import color_pb2

service_directory = Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "LocalizedMeasurement.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


class Color(Enum):
    """用于示例枚举类型配置和输出的主要颜色."""

    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3


@measurement_service.register_measurement
@measurement_service.configuration("Float In", nims.DataType.Float, 0.06)
@measurement_service.configuration("Double Array In", nims.DataType.DoubleArray1D, [0.1, 0.2, 0.3])
@measurement_service.configuration("Bool In", nims.DataType.Boolean, False)
@measurement_service.configuration("String In", nims.DataType.String, "示例字符串")
@measurement_service.configuration(
    "String Array In",
    nims.DataType.StringArray1D,
    [
        "带有/正斜杠的字符串",
        "带有\\反斜杠的字符串",
        "带有'单引号'的字符串",
        '带有"双引号"的字符串',
        "带有\t制表符的字符串",
        "带有\n换行符的字符串",
    ],
)
@measurement_service.configuration("Path In", nims.DataType.Path, "示例\\路径\\用于\\测试")
@measurement_service.configuration(
    "Path Array In",
    nims.DataType.PathArray1D,
    [
        "路径/带有/正斜杠",
        "路径\\带有\\反斜杠",
        "路径 带有 '单引号'",
        '路径 带有 "双引号"',
        "路径\t带有\t制表符",
        "路径\n带有\n换行符",
    ],
)
@measurement_service.configuration("IO In", nims.DataType.IOResource, "资源")
@measurement_service.configuration(
    "IO Array In", nims.DataType.IOResourceArray1D, ["资源1", "资源2"]
)
@measurement_service.configuration("Integer In", nims.DataType.Int32, 10)
@measurement_service.configuration("Enum In", nims.DataType.Enum, Color.BLUE, enum_type=Color)
@measurement_service.configuration(
    "Enum Array In", nims.DataType.EnumArray1D, [1, 2], enum_type=Color
)
@measurement_service.output("Float out", nims.DataType.Float)
@measurement_service.output("Double Array out", nims.DataType.DoubleArray1D)
@measurement_service.output("Bool out", nims.DataType.Boolean)
@measurement_service.output("String out", nims.DataType.String)
@measurement_service.output("String Array out", nims.DataType.StringArray1D)
@measurement_service.output("Path Out", nims.DataType.Path)
@measurement_service.output("Path Array Out", nims.DataType.PathArray1D)
@measurement_service.output("IO Out", nims.DataType.IOResource)
@measurement_service.output("IO Array Out", nims.DataType.IOResourceArray1D)
@measurement_service.output("Integer Out", nims.DataType.Int32)
@measurement_service.output("XY Data Out", nims.DataType.DoubleXYData)
@measurement_service.output("Enum Out", nims.DataType.Enum, enum_type=Color)
@measurement_service.output("Enum Array Out", nims.DataType.EnumArray1D, enum_type=Color)
@measurement_service.output("Double 2D Array out", nims.DataType.Double2DArray)
@measurement_service.output("String 2D Array out", nims.DataType.String2DArray)
def measure(
    float_input: float,
    double_array_input: Iterable[float],
    bool_input: bool,
    string_input: str,
    string_array_input: Iterable[str],
    path_input: Path,
    path_array_input: Iterable[Path],
    io_input: str,
    io_array_input: Iterable[str],
    integer_input: int,
    enum_input: Color,
    enum_array_input: Iterable[Color],
) -> tuple[
    float,
    Iterable[float],
    bool,
    str,
    Iterable[str],
    Path,
    Iterable[Path],
    str,
    Iterable[str],
    int,
    xydata_pb2.DoubleXYData,
    Color,
    Iterable[Color],
    array_pb2.Double2DArray,
    array_pb2.String2DArray,
]:
    """使用各种数据类型执行环回测量."""
    float_output = float_input
    float_array_output = double_array_input
    bool_output = bool_input
    string_output = string_input
    string_array_output = string_array_input
    path_output = path_input
    path_array_output = path_array_input
    io_output = io_input
    io_array_output = io_array_input
    integer_output = integer_input
    xy_data_output = xydata_pb2.DoubleXYData()
    enum_output = enum_input
    enum_array_output = enum_array_input
    double_2d_array_output = array_pb2.Double2DArray(
        rows=2, columns=3, data=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    )
    string_2d_array_output = array_pb2.String2DArray(
        rows=2, columns=3, data=["你好", "世界", "测试", "中文", "本地化", "字符串"]
    )

    return (
        float_output,
        float_array_output,
        bool_output,
        string_output,
        string_array_output,
        path_output,
        path_array_output,
        io_output,
        io_array_output,
        integer_output,
        xy_data_output,
        enum_output,
        enum_array_output,
        double_2d_array_output,
        string_2d_array_output,
    )
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/localized_measurement/LocalizedMeasurement.serviceconfig sha256=460be402695b33f3cd35d4fff29d09b3dc86f742ed3f76e86f1ae8345e99d711 bytes=616 -->
## FILE: packages/generator/tests/utilities/measurements/localized_measurement/LocalizedMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/utilities/measurements/localized_measurement/LocalizedMeasurement.serviceconfig`
- sha256: `460be402695b33f3cd35d4fff29d09b3dc86f742ed3f76e86f1ae8345e99d711`
- bytes: 616

````json
{
  "services": [
    {
      "displayName": "本地化测量（Py）",
      "version": "0.1.0.0",
      "serviceClass": "ni.tests.LocalizedMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "本地化测量插件测试服务，执行回环测量。",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/non_streaming_data_measurement/__init__.py sha256=fdd7a23e7a2eeaa3c344f4642cf31f2cb1951186cebe824783ad2a7c94660d34 bytes=5891 -->
## FILE: packages/generator/tests/utilities/measurements/non_streaming_data_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/utilities/measurements/non_streaming_data_measurement/__init__.py`
- sha256: `fdd7a23e7a2eeaa3c344f4642cf31f2cb1951186cebe824783ad2a7c94660d34`
- bytes: 5891

````python
"""Contains utility functions to test loopback measurement service."""

from __future__ import annotations

from collections.abc import Iterable
from enum import Enum
from pathlib import Path
from typing import Tuple

import ni_measurement_plugin_sdk_service as nims
from ni.protobuf.types import array_pb2, xydata_pb2

from tests.utilities.measurements.non_streaming_data_measurement._stubs import color_pb2

service_directory = Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "NonStreamingDataMeasurement.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


class Color(Enum):
    """Primary colors used for example enum-typed config and output."""

    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3


@measurement_service.register_measurement
@measurement_service.configuration("Float In", nims.DataType.Float, 0.06)
@measurement_service.configuration("Double Array In", nims.DataType.DoubleArray1D, [0.1, 0.2, 0.3])
@measurement_service.configuration("Bool In", nims.DataType.Boolean, False)
@measurement_service.configuration("String In", nims.DataType.String, "sample string")
@measurement_service.configuration(
    "String Array In",
    nims.DataType.StringArray1D,
    [
        "string with /forwardslash",
        "string with \\backslash",
        "string with 'single quotes'",
        'string with "double quotes"',
        "string with \ttabspace",
        "string with \nnewline",
    ],
)
@measurement_service.configuration("Path In", nims.DataType.Path, "sample\\path\\for\\test")
@measurement_service.configuration(
    "Path Array In",
    nims.DataType.PathArray1D,
    [
        "path/with/forward/slash",
        "path\\with\\backslash",
        "path with 'single quotes'",
        'path with "double quotes"',
        "path\twith\ttabs",
        "path\nwith\nnewlines",
    ],
)
@measurement_service.configuration("IO In", nims.DataType.IOResource, "resource")
@measurement_service.configuration(
    "IO Array In", nims.DataType.IOResourceArray1D, ["resource1", "resource2"]
)
@measurement_service.configuration("Integer In", nims.DataType.Int32, 10)
@measurement_service.configuration("Enum In", nims.DataType.Enum, Color.BLUE, enum_type=Color)
@measurement_service.configuration(
    "Enum Array In", nims.DataType.EnumArray1D, [1, 2], enum_type=Color
)
@measurement_service.configuration(
    "Protobuf Enum In",
    nims.DataType.Enum,
    color_pb2.ProtobufColor.BLACK,
    enum_type=color_pb2.ProtobufColor,
)
@measurement_service.output("Float out", nims.DataType.Float)
@measurement_service.output("Double Array out", nims.DataType.DoubleArray1D)
@measurement_service.output("Bool out", nims.DataType.Boolean)
@measurement_service.output("String out", nims.DataType.String)
@measurement_service.output("String Array out", nims.DataType.StringArray1D)
@measurement_service.output("Path Out", nims.DataType.Path)
@measurement_service.output("Path Array Out", nims.DataType.PathArray1D)
@measurement_service.output("IO Out", nims.DataType.IOResource)
@measurement_service.output("IO Array Out", nims.DataType.IOResourceArray1D)
@measurement_service.output("Integer Out", nims.DataType.Int32)
@measurement_service.output("XY Data Out", nims.DataType.DoubleXYData)
@measurement_service.output("Enum Out", nims.DataType.Enum, enum_type=Color)
@measurement_service.output("Enum Array Out", nims.DataType.EnumArray1D, enum_type=Color)
@measurement_service.output(
    "Protobuf Enum out", nims.DataType.Enum, enum_type=color_pb2.ProtobufColor
)
@measurement_service.output("Double 2D Array out", nims.DataType.Double2DArray)
@measurement_service.output("String 2D Array out", nims.DataType.String2DArray)
def measure(
    float_input: float,
    double_array_input: Iterable[float],
    bool_input: bool,
    string_input: str,
    string_array_input: Iterable[str],
    path_input: Path,
    path_array_input: Iterable[Path],
    io_input: str,
    io_array_input: Iterable[str],
    integer_input: int,
    enum_input: Color,
    enum_array_input: Iterable[Color],
    protobuf_enum_input: color_pb2.ProtobufColor.ValueType,
) -> tuple[
    float,
    Iterable[float],
    bool,
    str,
    Iterable[str],
    Path,
    Iterable[Path],
    str,
    Iterable[str],
    int,
    xydata_pb2.DoubleXYData,
    Color,
    Iterable[Color],
    color_pb2.ProtobufColor.ValueType,
    array_pb2.Double2DArray,
    array_pb2.String2DArray,
]:
    """Perform a loopback measurement with various data types."""
    float_output = float_input
    float_array_output = double_array_input
    bool_output = bool_input
    string_output = string_input
    string_array_output = string_array_input
    path_output = path_input
    path_array_output = path_array_input
    io_output = io_input
    io_array_output = io_array_input
    integer_output = integer_input
    xy_data_output = xydata_pb2.DoubleXYData()
    enum_output = enum_input
    enum_array_output = enum_array_input
    protobuf_enum_output = protobuf_enum_input
    double_2d_array_output = array_pb2.Double2DArray(
        rows=2, columns=3, data=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    )
    string_2d_array_output = array_pb2.String2DArray(
        rows=2, columns=3, data=["ABC", "DEF", "GHI", "JKL", "MNO", "PQR"]
    )

    return (
        float_output,
        float_array_output,
        bool_output,
        string_output,
        string_array_output,
        path_output,
        path_array_output,
        io_output,
        io_array_output,
        integer_output,
        xy_data_output,
        enum_output,
        enum_array_output,
        protobuf_enum_output,
        double_2d_array_output,
        string_2d_array_output,
    )
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/__init__.py sha256=7432987a39c6c36036f5401206d52e5390319f6bfc79dadb64ec540ff44ac965 bytes=62 -->
## FILE: packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/__init__.py`
- sha256: `7432987a39c6c36036f5401206d52e5390319f6bfc79dadb64ec540ff44ac965`
- bytes: 62

````python
"""Stubs for non_streaming_data_measurement's color enum."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color.proto sha256=78c3dcffcecdd02c675ae625472a2f9081916570dc5173bd35862c81d7e89568 bytes=623 -->
## FILE: packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color.proto

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color.proto`
- sha256: `78c3dcffcecdd02c675ae625472a2f9081916570dc5173bd35862c81d7e89568`
- bytes: 623

````protobuf
//---------------------------------------------------------------------
//---------------------------------------------------------------------
syntax = "proto3";

//---------------------------------------------------------------------
//---------------------------------------------------------------------
package ni.measurementlink.measurement.non_streaming_data_measurement.v1;

//---------------------------------------------------------------------
//---------------------------------------------------------------------

enum ProtobufColor{
    NONE = 0;
    PINK = 1;
    WHITE = 2;
    BLACK = 3;
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color_pb2.py sha256=01c4ebb62fde5a4d21f7acf429cdc03c2b1ecb5675322bf1093ef8021e775986 bytes=1105 -->
## FILE: packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color_pb2.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color_pb2.py`
- sha256: `01c4ebb62fde5a4d21f7acf429cdc03c2b1ecb5675322bf1093ef8021e775986`
- bytes: 1105

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: color.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x63olor.proto\x12@ni.measurementlink.measurement.non_streaming_data_measurement.v1*9\n\rProtobufColor\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04PINK\x10\x01\x12\t\n\x05WHITE\x10\x02\x12\t\n\x05\x42LACK\x10\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'color_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PROTOBUFCOLOR._serialized_start=81
  _PROTOBUFCOLOR._serialized_end=138
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color_pb2.pyi sha256=0018723c67f5ea819a98b86fd71600f740a97598f0032755ffdd9e9b0b3fb866 bytes=1453 -->
## FILE: packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color_pb2.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color_pb2.pyi`
- sha256: `0018723c67f5ea819a98b86fd71600f740a97598f0032755ffdd9e9b0b3fb866`
- bytes: 1453

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
---------------------------------------------------------------------
---------------------------------------------------------------------
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ProtobufColor:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ProtobufColorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ProtobufColor.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NONE: _ProtobufColor.ValueType  # 0
    PINK: _ProtobufColor.ValueType  # 1
    WHITE: _ProtobufColor.ValueType  # 2
    BLACK: _ProtobufColor.ValueType  # 3

class ProtobufColor(_ProtobufColor, metaclass=_ProtobufColorEnumTypeWrapper):
    """---------------------------------------------------------------------
    ---------------------------------------------------------------------
    """

NONE: ProtobufColor.ValueType  # 0
PINK: ProtobufColor.ValueType  # 1
WHITE: ProtobufColor.ValueType  # 2
BLACK: ProtobufColor.ValueType  # 3
global___ProtobufColor = ProtobufColor
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color_pb2_grpc.py sha256=fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb bytes=163 -->
## FILE: packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color_pb2_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color_pb2_grpc.py`
- sha256: `fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb`
- bytes: 163

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color_pb2_grpc.pyi sha256=bcc6cd9c21fc28773cccb72f78f3002ad2f44b48aef1bdcc218758ec4a42f6ba bytes=572 -->
## FILE: packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color_pb2_grpc.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color_pb2_grpc.pyi`
- sha256: `bcc6cd9c21fc28773cccb72f78f3002ad2f44b48aef1bdcc218758ec4a42f6ba`
- bytes: 572

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
---------------------------------------------------------------------
---------------------------------------------------------------------
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/non_streaming_data_measurement/NonStreamingDataMeasurement.serviceconfig sha256=36f696da90c56dd721538c68bf3bcbfb5c546c812d42dd0d8865ec4699fea009 bytes=650 -->
## FILE: packages/generator/tests/utilities/measurements/non_streaming_data_measurement/NonStreamingDataMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/utilities/measurements/non_streaming_data_measurement/NonStreamingDataMeasurement.serviceconfig`
- sha256: `36f696da90c56dd721538c68bf3bcbfb5c546c812d42dd0d8865ec4699fea009`
- bytes: 650

````json
{
  "services": [
    {
      "displayName": "Non-Streaming Data Measurement (Py)",
      "version": "0.1.0.0",
      "serviceClass": "ni.tests.NonStreamingDataMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in test service that performs a loopback measurement.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }

    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/pin_aware_measurement/__init__.py sha256=b339fab2c2d6808f567d49e9f5cbdace7729cc415fe710f4f9a156397c486740 bytes=2171 -->
## FILE: packages/generator/tests/utilities/measurements/pin_aware_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/utilities/measurements/pin_aware_measurement/__init__.py`
- sha256: `b339fab2c2d6808f567d49e9f5cbdace7729cc415fe710f4f9a156397c486740`
- bytes: 2171

````python
"""Pin-aware measurement plug-in test service."""

from __future__ import annotations

import pathlib
from collections.abc import Iterable
from typing import Tuple

import ni_measurement_plugin_sdk_service as nims

service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "PinAwareMeasurement.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


@measurement_service.register_measurement
@measurement_service.configuration("pin_names", nims.DataType.IOResourceArray1D, ["Pin1"])
@measurement_service.configuration("multi_session", nims.DataType.Boolean, False)
@measurement_service.output("pin_map_id", nims.DataType.String)
@measurement_service.output("sites", nims.DataType.Int32Array1D)
@measurement_service.output("session_names", nims.DataType.StringArray1D)
@measurement_service.output("resource_names", nims.DataType.StringArray1D)
@measurement_service.output("channel_lists", nims.DataType.StringArray1D)
def measure(
    pin_names: Iterable[str],
    multi_session: bool,
) -> tuple[str, Iterable[int], Iterable[str], Iterable[str], Iterable[str]]:
    """Pin-aware measurement plug-in test service."""
    pin_map_context = measurement_service.context.pin_map_context
    if multi_session:
        with measurement_service.context.reserve_sessions(pin_names) as reservation:
            return (
                pin_map_context.pin_map_id,
                pin_map_context.sites or [],
                [s.session_name for s in reservation.session_info],
                [s.resource_name for s in reservation.session_info],
                [s.channel_list for s in reservation.session_info],
            )
    else:
        with measurement_service.context.reserve_session(pin_names) as reservation:
            return (
                pin_map_context.pin_map_id,
                pin_map_context.sites or [],
                [reservation.session_info.resource_name],
                [reservation.session_info.resource_name],
                [reservation.session_info.channel_list],
            )
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/pin_aware_measurement/PinAwareMeasurement.serviceconfig sha256=66864110578f9fac200eb7583ac5f127336f89b753e5caec74f7c6f942e92fc8 bytes=606 -->
## FILE: packages/generator/tests/utilities/measurements/pin_aware_measurement/PinAwareMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/utilities/measurements/pin_aware_measurement/PinAwareMeasurement.serviceconfig`
- sha256: `66864110578f9fac200eb7583ac5f127336f89b753e5caec74f7c6f942e92fc8`
- bytes: 606

````json
{
  "services": [
    {
      "displayName": "Pin Aware Measurement (Py)",
      "version": "0.1.0.0",
      "serviceClass": "ni.tests.PinAwareMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "Pin-aware measurement plug-in test service.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }

    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/streaming_data_measurement/__init__.py sha256=6e431293a723ede2734cd2809af9d16a8c199ae1b54fc61920b5e51d6261b8bc bytes=2678 -->
## FILE: packages/generator/tests/utilities/measurements/streaming_data_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/utilities/measurements/streaming_data_measurement/__init__.py`
- sha256: `6e431293a723ede2734cd2809af9d16a8c199ae1b54fc61920b5e51d6261b8bc`
- bytes: 2678

````python
"""Contains utility functions to test a v2 measurement service that streams data."""

from __future__ import annotations

import pathlib
import threading
import time
from collections.abc import Generator

import grpc
import ni_measurement_plugin_sdk_service as nims

service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "StreamingDataMeasurement.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


Outputs = tuple[str, int, list[int]]

measurement_started_event = threading.Event()


@measurement_service.register_measurement
@measurement_service.configuration("name", nims.DataType.String, "<Name>")
@measurement_service.configuration("num_responses", nims.DataType.Int32, 10)
@measurement_service.configuration("data_size", nims.DataType.Int32, 1)
@measurement_service.configuration("cumulative_data", nims.DataType.Boolean, True)
@measurement_service.configuration("response_interval_in_ms", nims.DataType.Int32, 1000)
@measurement_service.configuration("error_on_index", nims.DataType.Int32, -1)
@measurement_service.output("name", nims.DataType.String)
@measurement_service.output("index", nims.DataType.Int32)
@measurement_service.output("data", nims.DataType.Int32Array1D)
def measure(
    name: str,
    num_responses: int,
    data_size: int,
    cumulative_data: bool,
    response_interval_in_ms: int,
    error_on_index: int,
) -> Generator[Outputs]:
    """Returns the number of responses requested at the requested interval."""
    measurement_started_event.set()

    cancellation_event = threading.Event()
    measurement_service.context.add_cancel_callback(cancellation_event.set)

    data: list[int] = []

    response_interval_in_seconds = response_interval_in_ms / 1000.0

    for index in range(0, num_responses):
        update_time = time.monotonic()

        if index == error_on_index:
            measurement_service.context.abort(
                grpc.StatusCode.UNKNOWN,
                f"Errored at index {error_on_index}",
            )

        if not cumulative_data:
            data.clear()

        data.extend(index for i in range(data_size))

        yield (name, index, data)

        # Delay for the remaining portion of the requested interval and check for cancellation.
        delay = max(0.0, response_interval_in_seconds - (time.monotonic() - update_time))
        if cancellation_event.wait(delay):
            measurement_service.context.abort(
                grpc.StatusCode.CANCELLED, "Client requested cancellation."
            )
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/streaming_data_measurement/StreamingDataMeasurement.serviceconfig sha256=85ddc6ae90c80f8da705f8a63ff64b572786936d68f2152cc469cea93cef4849 bytes=583 -->
## FILE: packages/generator/tests/utilities/measurements/streaming_data_measurement/StreamingDataMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/utilities/measurements/streaming_data_measurement/StreamingDataMeasurement.serviceconfig`
- sha256: `85ddc6ae90c80f8da705f8a63ff64b572786936d68f2152cc469cea93cef4849`
- bytes: 583

````json
{
  "services": [
    {
      "displayName": "Streaming Data Measurement (Py)",
      "version": "0.1.0.0",
      "serviceClass": "ni.tests.StreamingDataMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in test service that generates a predictable stream of data.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/void_measurement/__init__.py sha256=b44f6a26eed4aa93296b83109493ac39ef56af82e3753f2631bbe7c30cabbdae bytes=1389 -->
## FILE: packages/generator/tests/utilities/measurements/void_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/utilities/measurements/void_measurement/__init__.py`
- sha256: `b44f6a26eed4aa93296b83109493ac39ef56af82e3753f2631bbe7c30cabbdae`
- bytes: 1389

````python
"""Contains utility functions to test void measurement service."""

from __future__ import annotations

import threading
import time
from pathlib import Path

import grpc
import ni_measurement_plugin_sdk_service as nims

service_directory = Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "VoidMeasurement.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


@measurement_service.register_measurement
@measurement_service.configuration("Integer In", nims.DataType.Int32, 10)
def measure(
    integer_input: int,
) -> tuple[()]:
    """Perform a measurement with no output."""
    cancellation_event = threading.Event()
    measurement_service.context.add_cancel_callback(cancellation_event.set)

    response_interval_in_seconds = 1
    data: list[int] = []

    for index in range(0, integer_input):
        update_time = time.monotonic()
        data.append(index)

        # Delay for the remaining portion of the requested interval and check for cancellation.
        delay = max(0.0, response_interval_in_seconds - (time.monotonic() - update_time))
        if cancellation_event.wait(delay):
            measurement_service.context.abort(
                grpc.StatusCode.CANCELLED, "Client requested cancellation."
            )

    return ()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/void_measurement/VoidMeasurement.serviceconfig sha256=7330103f4277d8a85985540beb3edc1789e35e4cde5b006f26b4a25e956c8e4c bytes=628 -->
## FILE: packages/generator/tests/utilities/measurements/void_measurement/VoidMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tests/utilities/measurements/void_measurement/VoidMeasurement.serviceconfig`
- sha256: `7330103f4277d8a85985540beb3edc1789e35e4cde5b006f26b4a25e956c8e4c`
- bytes: 628

````json
{
  "services": [
    {
      "displayName": "Void Measurement (Py)",
      "version": "0.1.0.0",
      "serviceClass": "ni.tests.VoidMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in test service that performs a measurement without output.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/generator/tox.ini sha256=40d39c5da07ecc40ee8c1317121b9332875e81b0df578592a3c18e23b8a4d5fd bytes=851 -->
## FILE: packages/generator/tox.ini

- repository: `ni/measurement-plugin-python`
- source_path: `packages/generator/tox.ini`
- sha256: `40d39c5da07ecc40ee8c1317121b9332875e81b0df578592a3c18e23b8a4d5fd`
- bytes: 851

````ini
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox" from this directory.

[tox]
isolated_build = true
envlist = clean, py{310,311,312,313,314}, py310-{pb4,pb5,pb6}

[testenv]
skip_install = true
allowlist_externals = poetry
passenv = RUNNER_NAME
commands =
   poetry run python --version
   poetry install -v
   pb4: poetry run pip install protobuf==4.25.6
   pb5: poetry run pip install protobuf==5.29.3
   pb6: poetry run pip install protobuf==6.30.0
   poetry run pytest -v --cov=ni_measurement_plugin_sdk_generator --cov-append --cov-report= --junitxml=test_results/nimg-{env:RUNNER_NAME}-{envname}.xml

[testenv:clean]
commands = poetry run coverage erase
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/sdk/ni_measurement_plugin_sdk/__init__.py sha256=c79ff09ac65a7bfa3dd5ab4bb8b83bde94edf2ce7f0ab0bac0ee6174536f3e32 bytes=43 -->
## FILE: packages/sdk/ni_measurement_plugin_sdk/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/sdk/ni_measurement_plugin_sdk/__init__.py`
- sha256: `c79ff09ac65a7bfa3dd5ab4bb8b83bde94edf2ce7f0ab0bac0ee6174536f3e32`
- bytes: 43

````python
"""Measurement Plug-In SDK for Python."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/sdk/poetry.lock sha256=c7b57331aa045c63df41c3d2306e2de5b1f4d4490ccb5a079557778f669429d5 bytes=86041 -->
## FILE: packages/sdk/poetry.lock

- repository: `ni/measurement-plugin-python`
- source_path: `packages/sdk/poetry.lock`
- sha256: `c7b57331aa045c63df41c3d2306e2de5b1f4d4490ccb5a079557778f669429d5`
- bytes: 86041

````text
# This file is automatically @generated by Poetry 2.4.1 and should not be changed by hand.

[[package]]
name = "black"
version = "26.1.0"
description = "The uncompromising code formatter."
optional = false
python-versions = ">=3.10"
groups = ["main", "dev"]
files = [
    {file = "black-26.1.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:ca699710dece84e3ebf6e92ee15f5b8f72870ef984bf944a57a777a48357c168"},
    {file = "black-26.1.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:5e8e75dabb6eb83d064b0db46392b25cabb6e784ea624219736e8985a6b3675d"},
    {file = "black-26.1.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:eb07665d9a907a1a645ee41a0df8a25ffac8ad9c26cdb557b7b88eeeeec934e0"},
    {file = "black-26.1.0-cp310-cp310-win_amd64.whl", hash = "sha256:7ed300200918147c963c87700ccf9966dceaefbbb7277450a8d646fc5646bf24"},
    {file = "black-26.1.0-cp310-cp310-win_arm64.whl", hash = "sha256:c5b7713daea9bf943f79f8c3b46f361cc5229e0e604dcef6a8bb6d1c37d9df89"},
    {file = "black-26.1.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:3cee1487a9e4c640dc7467aaa543d6c0097c391dc8ac74eb313f2fbf9d7a7cb5"},
    {file = "black-26.1.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:d62d14ca31c92adf561ebb2e5f2741bf8dea28aef6deb400d49cca011d186c68"},
    {file = "black-26.1.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:fb1dafbbaa3b1ee8b4550a84425aac8874e5f390200f5502cf3aee4a2acb2f14"},
    {file = "black-26.1.0-cp311-cp311-win_amd64.whl", hash = "sha256:101540cb2a77c680f4f80e628ae98bd2bd8812fb9d72ade4f8995c5ff019e82c"},
    {file = "black-26.1.0-cp311-cp311-win_arm64.whl", hash = "sha256:6f3977a16e347f1b115662be07daa93137259c711e526402aa444d7a88fdc9d4"},
    {file = "black-26.1.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:6eeca41e70b5f5c84f2f913af857cf2ce17410847e1d54642e658e078da6544f"},
    {file = "black-26.1.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:dd39eef053e58e60204f2cdf059e2442e2eb08f15989eefe259870f89614c8b6"},
    {file = "black-26.1.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9459ad0d6cd483eacad4c6566b0f8e42af5e8b583cee917d90ffaa3778420a0a"},
    {file = "black-26.1.0-cp312-cp312-win_amd64.whl", hash = "sha256:a19915ec61f3a8746e8b10adbac4a577c6ba9851fa4a9e9fbfbcf319887a5791"},
    {file = "black-26.1.0-cp312-cp312-win_arm64.whl", hash = "sha256:643d27fb5facc167c0b1b59d0315f2674a6e950341aed0fc05cf307d22bf4954"},
    {file = "black-26.1.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:ba1d768fbfb6930fc93b0ecc32a43d8861ded16f47a40f14afa9bb04ab93d304"},
    {file = "black-26.1.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:2b807c240b64609cb0e80d2200a35b23c7df82259f80bef1b2c96eb422b4aac9"},
    {file = "black-26.1.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1de0f7d01cc894066a1153b738145b194414cc6eeaad8ef4397ac9abacf40f6b"},
    {file = "black-26.1.0-cp313-cp313-win_amd64.whl", hash = "sha256:91a68ae46bf07868963671e4d05611b179c2313301bd756a89ad4e3b3db2325b"},
    {file = "black-26.1.0-cp313-cp313-win_arm64.whl", hash = "sha256:be5e2fe860b9bd9edbf676d5b60a9282994c03fbbd40fe8f5e75d194f96064ca"},
    {file = "black-26.1.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:9dc8c71656a79ca49b8d3e2ce8103210c9481c57798b48deeb3a8bb02db5f115"},
    {file = "black-26.1.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:b22b3810451abe359a964cc88121d57f7bce482b53a066de0f1584988ca36e79"},
    {file = "black-26.1.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:53c62883b3f999f14e5d30b5a79bd437236658ad45b2f853906c7cbe79de00af"},
    {file = "black-26.1.0-cp314-cp314-win_amd64.whl", hash = "sha256:f016baaadc423dc960cdddf9acae679e71ee02c4c341f78f3179d7e4819c095f"},
    {file = "black-26.1.0-cp314-cp314-win_arm64.whl", hash = "sha256:66912475200b67ef5a0ab665011964bf924745103f51977a78b4fb92a9fc1bf0"},
    {file = "black-26.1.0-py3-none-any.whl", hash = "sha256:1054e8e47ebd686e078c0bb0eaf31e6ce69c966058d122f2c0c950311f9f3ede"},
    {file = "black-26.1.0.tar.gz", hash = "sha256:d294ac3340eef9c9eb5d29288e96dc719ff269a88e27b396340459dd85da4c58"},
]

[package.dependencies]
click = ">=8.0.0"
mypy-extensions = ">=0.4.3"
packaging = ">=22.0"
pathspec = ">=1.0.0"
platformdirs = ">=2"
pytokens = ">=0.3.0"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}
typing-extensions = {version = ">=4.0.1", markers = "python_version < \"3.11\""}

[package.extras]
colorama = ["colorama (>=0.4.3)"]
d = ["aiohttp (>=3.10)"]
jupyter = ["ipython (>=7.8.0)", "tokenize-rt (>=3.2.0)"]
uvloop = ["uvloop (>=0.15.2)"]

[[package]]
name = "click"
version = "8.3.1"
description = "Composable command line interface toolkit"
optional = false
python-versions = ">=3.10"
groups = ["main", "dev"]
files = [
    {file = "click-8.3.1-py3-none-any.whl", hash = "sha256:981153a64e25f12d547d3426c367a4857371575ee7ad18df2a6183ab0545b2a6"},
    {file = "click-8.3.1.tar.gz", hash = "sha256:12ff4785d337a1bb490bb7e9c2b1ee5da3112e94a8622f26a6c77f5d2fc6842a"},
]

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}

[[package]]
name = "click-option-group"
version = "0.5.9"
description = "Option groups missing in Click"
optional = false
python-versions = ">=3.7"
groups = ["main", "dev"]
files = [
    {file = "click_option_group-0.5.9-py3-none-any.whl", hash = "sha256:ad2599248bd373e2e19bec5407967c3eec1d0d4fc4a5e77b08a0481e75991080"},
    {file = "click_option_group-0.5.9.tar.gz", hash = "sha256:f94ed2bc4cf69052e0f29592bd1e771a1789bd7bfc482dd0bc482134aff95823"},
]

[package.dependencies]
click = ">=7.0"

[package.extras]
dev = ["pre-commit", "pytest"]
docs = ["m2r2", "pallets-sphinx-themes", "sphinx"]
test = ["pytest"]
test-cov = ["pytest", "pytest-cov"]

[[package]]
name = "colorama"
version = "0.4.6"
description = "Cross-platform colored terminal text."
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"
groups = ["main", "dev"]
markers = "platform_system == \"Windows\""
files = [
    {file = "colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"},
    {file = "colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"},
]

[[package]]
name = "deprecation"
version = "2.1.0"
description = "A library to handle automated deprecations"
optional = false
python-versions = "*"
groups = ["main", "dev"]
files = [
    {file = "deprecation-2.1.0-py2.py3-none-any.whl", hash = "sha256:a10811591210e1fb0e768a8c25517cabeabcba6f0bf96564f8ff45189f90b14a"},
    {file = "deprecation-2.1.0.tar.gz", hash = "sha256:72b3bde64e5d778694b0cf68178aed03d15e15477116add3fb773e581f9518ff"},
]

[package.dependencies]
packaging = "*"

[[package]]
name = "grpcio"
version = "1.76.0"
description = "HTTP/2-based RPC framework"
optional = false
python-versions = ">=3.9"
groups = ["main", "dev"]
files = [
    {file = "grpcio-1.76.0-cp310-cp310-linux_armv7l.whl", hash = "sha256:65a20de41e85648e00305c1bb09a3598f840422e522277641145a32d42dcefcc"},
    {file = "grpcio-1.76.0-cp310-cp310-macosx_11_0_universal2.whl", hash = "sha256:40ad3afe81676fd9ec6d9d406eda00933f218038433980aa19d401490e46ecde"},
    {file = "grpcio-1.76.0-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:035d90bc79eaa4bed83f524331d55e35820725c9fbb00ffa1904d5550ed7ede3"},
    {file = "grpcio-1.76.0-cp310-cp310-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:4215d3a102bd95e2e11b5395c78562967959824156af11fa93d18fdd18050990"},
    {file = "grpcio-1.76.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:49ce47231818806067aea3324d4bf13825b658ad662d3b25fada0bdad9b8a6af"},
    {file = "grpcio-1.76.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:8cc3309d8e08fd79089e13ed4819d0af72aa935dd8f435a195fd152796752ff2"},
    {file = "grpcio-1.76.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:971fd5a1d6e62e00d945423a567e42eb1fa678ba89072832185ca836a94daaa6"},
    {file = "grpcio-1.76.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:9d9adda641db7207e800a7f089068f6f645959f2df27e870ee81d44701dd9db3"},
    {file = "grpcio-1.76.0-cp310-cp310-win32.whl", hash = "sha256:063065249d9e7e0782d03d2bca50787f53bd0fb89a67de9a7b521c4a01f1989b"},
    {file = "grpcio-1.76.0-cp310-cp310-win_amd64.whl", hash = "sha256:a6ae758eb08088d36812dd5d9af7a9859c05b1e0f714470ea243694b49278e7b"},
    {file = "grpcio-1.76.0-cp311-cp311-linux_armv7l.whl", hash = "sha256:2e1743fbd7f5fa713a1b0a8ac8ebabf0ec980b5d8809ec358d488e273b9cf02a"},
    {file = "grpcio-1.76.0-cp311-cp311-macosx_11_0_universal2.whl", hash = "sha256:a8c2cf1209497cf659a667d7dea88985e834c24b7c3b605e6254cbb5076d985c"},
    {file = "grpcio-1.76.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:08caea849a9d3c71a542827d6df9d5a69067b0a1efbea8a855633ff5d9571465"},
    {file = "grpcio-1.76.0-cp311-cp311-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:f0e34c2079d47ae9f6188211db9e777c619a21d4faba6977774e8fa43b085e48"},
    {file = "grpcio-1.76.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:8843114c0cfce61b40ad48df65abcfc00d4dba82eae8718fab5352390848c5da"},
    {file = "grpcio-1.76.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:8eddfb4d203a237da6f3cc8a540dad0517d274b5a1e9e636fd8d2c79b5c1d397"},
    {file = "grpcio-1.76.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:32483fe2aab2c3794101c2a159070584e5db11d0aa091b2c0ea9c4fc43d0d749"},
    {file = "grpcio-1.76.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:dcfe41187da8992c5f40aa8c5ec086fa3672834d2be57a32384c08d5a05b4c00"},
    {file = "grpcio-1.76.0-cp311-cp311-win32.whl", hash = "sha256:2107b0c024d1b35f4083f11245c0e23846ae64d02f40b2b226684840260ed054"},
    {file = "grpcio-1.76.0-cp311-cp311-win_amd64.whl", hash = "sha256:522175aba7af9113c48ec10cc471b9b9bd4f6ceb36aeb4544a8e2c80ed9d252d"},
    {file = "grpcio-1.76.0-cp312-cp312-linux_armv7l.whl", hash = "sha256:81fd9652b37b36f16138611c7e884eb82e0cec137c40d3ef7c3f9b3ed00f6ed8"},
    {file = "grpcio-1.76.0-cp312-cp312-macosx_11_0_universal2.whl", hash = "sha256:04bbe1bfe3a68bbfd4e52402ab7d4eb59d72d02647ae2042204326cf4bbad280"},
    {file = "grpcio-1.76.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:d388087771c837cdb6515539f43b9d4bf0b0f23593a24054ac16f7a960be16f4"},
    {file = "grpcio-1.76.0-cp312-cp312-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:9f8f757bebaaea112c00dba718fc0d3260052ce714e25804a03f93f5d1c6cc11"},
    {file = "grpcio-1.76.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:980a846182ce88c4f2f7e2c22c56aefd515daeb36149d1c897f83cf57999e0b6"},
    {file = "grpcio-1.76.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:f92f88e6c033db65a5ae3d97905c8fea9c725b63e28d5a75cb73b49bda5024d8"},
    {file = "grpcio-1.76.0-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:4baf3cbe2f0be3289eb68ac8ae771156971848bb8aaff60bad42005539431980"},
    {file = "grpcio-1.76.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:615ba64c208aaceb5ec83bfdce7728b80bfeb8be97562944836a7a0a9647d882"},
    {file = "grpcio-1.76.0-cp312-cp312-win32.whl", hash = "sha256:45d59a649a82df5718fd9527ce775fd66d1af35e6d31abdcdc906a49c6822958"},
    {file = "grpcio-1.76.0-cp312-cp312-win_amd64.whl", hash = "sha256:c088e7a90b6017307f423efbb9d1ba97a22aa2170876223f9709e9d1de0b5347"},
    {file = "grpcio-1.76.0-cp313-cp313-linux_armv7l.whl", hash = "sha256:26ef06c73eb53267c2b319f43e6634c7556ea37672029241a056629af27c10e2"},
    {file = "grpcio-1.76.0-cp313-cp313-macosx_11_0_universal2.whl", hash = "sha256:45e0111e73f43f735d70786557dc38141185072d7ff8dc1829d6a77ac1471468"},
    {file = "grpcio-1.76.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:83d57312a58dcfe2a3a0f9d1389b299438909a02db60e2f2ea2ae2d8034909d3"},
    {file = "grpcio-1.76.0-cp313-cp313-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:3e2a27c89eb9ac3d81ec8835e12414d73536c6e620355d65102503064a4ed6eb"},
    {file = "grpcio-1.76.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:61f69297cba3950a524f61c7c8ee12e55c486cb5f7db47ff9dcee33da6f0d3ae"},
    {file = "grpcio-1.76.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:6a15c17af8839b6801d554263c546c69c4d7718ad4321e3166175b37eaacca77"},
    {file = "grpcio-1.76.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:25a18e9810fbc7e7f03ec2516addc116a957f8cbb8cbc95ccc80faa072743d03"},
    {file = "grpcio-1.76.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:931091142fd8cc14edccc0845a79248bc155425eee9a98b2db2ea4f00a235a42"},
    {file = "grpcio-1.76.0-cp313-cp313-win32.whl", hash = "sha256:5e8571632780e08526f118f74170ad8d50fb0a48c23a746bef2a6ebade3abd6f"},
    {file = "grpcio-1.76.0-cp313-cp313-win_amd64.whl", hash = "sha256:f9f7bd5faab55f47231ad8dba7787866b69f5e93bc306e3915606779bbfb4ba8"},
    {file = "grpcio-1.76.0-cp314-cp314-linux_armv7l.whl", hash = "sha256:ff8a59ea85a1f2191a0ffcc61298c571bc566332f82e5f5be1b83c9d8e668a62"},
    {file = "grpcio-1.76.0-cp314-cp314-macosx_11_0_universal2.whl", hash = "sha256:06c3d6b076e7b593905d04fdba6a0525711b3466f43b3400266f04ff735de0cd"},
    {file = "grpcio-1.76.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:fd5ef5932f6475c436c4a55e4336ebbe47bd3272be04964a03d316bbf4afbcbc"},
    {file = "grpcio-1.76.0-cp314-cp314-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:b331680e46239e090f5b3cead313cc772f6caa7d0fc8de349337563125361a4a"},
    {file = "grpcio-1.76.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:2229ae655ec4e8999599469559e97630185fdd53ae1e8997d147b7c9b2b72cba"},
    {file = "grpcio-1.76.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:490fa6d203992c47c7b9e4a9d39003a0c2bcc1c9aa3c058730884bbbb0ee9f09"},
    {file = "grpcio-1.76.0-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:479496325ce554792dba6548fae3df31a72cef7bad71ca2e12b0e58f9b336bfc"},
    {file = "grpcio-1.76.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:1c9b93f79f48b03ada57ea24725d83a30284a012ec27eab2cf7e50a550cbbbcc"},
    {file = "grpcio-1.76.0-cp314-cp314-win32.whl", hash = "sha256:747fa73efa9b8b1488a95d0ba1039c8e2dca0f741612d80415b1e1c560febf4e"},
    {file = "grpcio-1.76.0-cp314-cp314-win_amd64.whl", hash = "sha256:922fa70ba549fce362d2e2871ab542082d66e2aaf0c19480ea453905b01f384e"},
    {file = "grpcio-1.76.0-cp39-cp39-linux_armv7l.whl", hash = "sha256:8ebe63ee5f8fa4296b1b8cfc743f870d10e902ca18afc65c68cf46fd39bb0783"},
    {file = "grpcio-1.76.0-cp39-cp39-macosx_11_0_universal2.whl", hash = "sha256:3bf0f392c0b806905ed174dcd8bdd5e418a40d5567a05615a030a5aeddea692d"},
    {file = "grpcio-1.76.0-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:0b7604868b38c1bfd5cf72d768aedd7db41d78cb6a4a18585e33fb0f9f2363fd"},
    {file = "grpcio-1.76.0-cp39-cp39-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:e6d1db20594d9daba22f90da738b1a0441a7427552cc6e2e3d1297aeddc00378"},
    {file = "grpcio-1.76.0-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:d099566accf23d21037f18a2a63d323075bebace807742e4b0ac210971d4dd70"},
    {file = "grpcio-1.76.0-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:ebea5cc3aa8ea72e04df9913492f9a96d9348db876f9dda3ad729cfedf7ac416"},
    {file = "grpcio-1.76.0-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:0c37db8606c258e2ee0c56b78c62fc9dee0e901b5dbdcf816c2dd4ad652b8b0c"},
    {file = "grpcio-1.76.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:ebebf83299b0cb1721a8859ea98f3a77811e35dce7609c5c963b9ad90728f886"},
    {file = "grpcio-1.76.0-cp39-cp39-win32.whl", hash = "sha256:0aaa82d0813fd4c8e589fac9b65d7dd88702555f702fb10417f96e2a2a6d4c0f"},
    {file = "grpcio-1.76.0-cp39-cp39-win_amd64.whl", hash = "sha256:acab0277c40eff7143c2323190ea57b9ee5fd353d8190ee9652369fae735668a"},
    {file = "grpcio-1.76.0.tar.gz", hash = "sha256:7be78388d6da1a25c0d5ec506523db58b18be22d9c37d8d3a32c08be4987bd73"},
]

[package.dependencies]
typing-extensions = ">=4.12,<5.0"

[package.extras]
protobuf = ["grpcio-tools (>=1.76.0)"]

[[package]]
name = "hightime"
version = "1.0.0"
description = "Hightime Python API"
optional = false
python-versions = "<4.0,>=3.9"
groups = ["main", "dev"]
files = [
    {file = "hightime-1.0.0-py3-none-any.whl", hash = "sha256:ba86d42976c36451b14e11c736e61f296f9f00dbb79c8488e18d70c6b2dbb395"},
    {file = "hightime-1.0.0.tar.gz", hash = "sha256:480d2a03e2c3ed44916d2406d40ab6d10a276ed7f101619fc3fcc1e00c46aacf"},
]

[[package]]
name = "mako"
version = "1.3.10"
description = "A super-fast templating language that borrows the best ideas from the existing templating languages."
optional = false
python-versions = ">=3.8"
groups = ["main", "dev"]
files = [
    {file = "mako-1.3.10-py3-none-any.whl", hash = "sha256:baef24a52fc4fc514a0887ac600f9f1cff3d82c61d4d700a1fa84d597b88db59"},
    {file = "mako-1.3.10.tar.gz", hash = "sha256:99579a6f39583fa7e5630a28c3c1f440e4e97a414b80372649c0ce338da2ea28"},
]

[package.dependencies]
MarkupSafe = ">=0.9.2"

[package.extras]
babel = ["Babel"]
lingua = ["lingua"]
testing = ["pytest"]

[[package]]
name = "markupsafe"
version = "3.0.3"
description = "Safely add untrusted strings to HTML/XML markup."
optional = false
python-versions = ">=3.9"
groups = ["main", "dev"]
files = [
    {file = "markupsafe-3.0.3-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:2f981d352f04553a7171b8e44369f2af4055f888dfb147d55e42d29e29e74559"},
    {file = "markupsafe-3.0.3-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:e1c1493fb6e50ab01d20a22826e57520f1284df32f2d8601fdd90b6304601419"},
    {file = "markupsafe-3.0.3-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1ba88449deb3de88bd40044603fafffb7bc2b055d626a330323a9ed736661695"},
    {file = "markupsafe-3.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f42d0984e947b8adf7dd6dde396e720934d12c506ce84eea8476409563607591"},
    {file = "markupsafe-3.0.3-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:c0c0b3ade1c0b13b936d7970b1d37a57acde9199dc2aecc4c336773e1d86049c"},
    {file = "markupsafe-3.0.3-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:0303439a41979d9e74d18ff5e2dd8c43ed6c6001fd40e5bf2e43f7bd9bbc523f"},
    {file = "markupsafe-3.0.3-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:d2ee202e79d8ed691ceebae8e0486bd9a2cd4794cec4824e1c99b6f5009502f6"},
    {file = "markupsafe-3.0.3-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:177b5253b2834fe3678cb4a5f0059808258584c559193998be2601324fdeafb1"},
    {file = "markupsafe-3.0.3-cp310-cp310-win32.whl", hash = "sha256:2a15a08b17dd94c53a1da0438822d70ebcd13f8c3a95abe3a9ef9f11a94830aa"},
    {file = "markupsafe-3.0.3-cp310-cp310-win_amd64.whl", hash = "sha256:c4ffb7ebf07cfe8931028e3e4c85f0357459a3f9f9490886198848f4fa002ec8"},
    {file = "markupsafe-3.0.3-cp310-cp310-win_arm64.whl", hash = "sha256:e2103a929dfa2fcaf9bb4e7c091983a49c9ac3b19c9061b6d5427dd7d14d81a1"},
    {file = "markupsafe-3.0.3-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:1cc7ea17a6824959616c525620e387f6dd30fec8cb44f649e31712db02123dad"},
    {file = "markupsafe-3.0.3-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:4bd4cd07944443f5a265608cc6aab442e4f74dff8088b0dfc8238647b8f6ae9a"},
    {file = "markupsafe-3.0.3-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6b5420a1d9450023228968e7e6a9ce57f65d148ab56d2313fcd589eee96a7a50"},
    {file = "markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0bf2a864d67e76e5c9a34dc26ec616a66b9888e25e7b9460e1c76d3293bd9dbf"},
    {file = "markupsafe-3.0.3-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:bc51efed119bc9cfdf792cdeaa4d67e8f6fcccab66ed4bfdd6bde3e59bfcbb2f"},
    {file = "markupsafe-3.0.3-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:068f375c472b3e7acbe2d5318dea141359e6900156b5b2ba06a30b169086b91a"},
    {file = "markupsafe-3.0.3-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:7be7b61bb172e1ed687f1754f8e7484f1c8019780f6f6b0786e76bb01c2ae115"},
    {file = "markupsafe-3.0.3-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:f9e130248f4462aaa8e2552d547f36ddadbeaa573879158d721bbd33dfe4743a"},
    {file = "markupsafe-3.0.3-cp311-cp311-win32.whl", hash = "sha256:0db14f5dafddbb6d9208827849fad01f1a2609380add406671a26386cdf15a19"},
    {file = "markupsafe-3.0.3-cp311-cp311-win_amd64.whl", hash = "sha256:de8a88e63464af587c950061a5e6a67d3632e36df62b986892331d4620a35c01"},
    {file = "markupsafe-3.0.3-cp311-cp311-win_arm64.whl", hash = "sha256:3b562dd9e9ea93f13d53989d23a7e775fdfd1066c33494ff43f5418bc8c58a5c"},
    {file = "markupsafe-3.0.3-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:d53197da72cc091b024dd97249dfc7794d6a56530370992a5e1a08983ad9230e"},
    {file = "markupsafe-3.0.3-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:1872df69a4de6aead3491198eaf13810b565bdbeec3ae2dc8780f14458ec73ce"},
    {file = "markupsafe-3.0.3-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:3a7e8ae81ae39e62a41ec302f972ba6ae23a5c5396c8e60113e9066ef893da0d"},
    {file = "markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d6dd0be5b5b189d31db7cda48b91d7e0a9795f31430b7f271219ab30f1d3ac9d"},
    {file = "markupsafe-3.0.3-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:94c6f0bb423f739146aec64595853541634bde58b2135f27f61c1ffd1cd4d16a"},
    {file = "markupsafe-3.0.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:be8813b57049a7dc738189df53d69395eba14fb99345e0a5994914a3864c8a4b"},
    {file = "markupsafe-3.0.3-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:83891d0e9fb81a825d9a6d61e3f07550ca70a076484292a70fde82c4b807286f"},
    {file = "markupsafe-3.0.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:77f0643abe7495da77fb436f50f8dab76dbc6e5fd25d39589a0f1fe6548bfa2b"},
    {file = "markupsafe-3.0.3-cp312-cp312-win32.whl", hash = "sha256:d88b440e37a16e651bda4c7c2b930eb586fd15ca7406cb39e211fcff3bf3017d"},
    {file = "markupsafe-3.0.3-cp312-cp312-win_amd64.whl", hash = "sha256:26a5784ded40c9e318cfc2bdb30fe164bdb8665ded9cd64d500a34fb42067b1c"},
    {file = "markupsafe-3.0.3-cp312-cp312-win_arm64.whl", hash = "sha256:35add3b638a5d900e807944a078b51922212fb3dedb01633a8defc4b01a3c85f"},
    {file = "markupsafe-3.0.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:e1cf1972137e83c5d4c136c43ced9ac51d0e124706ee1c8aa8532c1287fa8795"},
    {file = "markupsafe-3.0.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:116bb52f642a37c115f517494ea5feb03889e04df47eeff5b130b1808ce7c219"},
    {file = "markupsafe-3.0.3-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:133a43e73a802c5562be9bbcd03d090aa5a1fe899db609c29e8c8d815c5f6de6"},
    {file = "markupsafe-3.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:ccfcd093f13f0f0b7fdd0f198b90053bf7b2f02a3927a30e63f3ccc9df56b676"},
    {file = "markupsafe-3.0.3-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:509fa21c6deb7a7a273d629cf5ec029bc209d1a51178615ddf718f5918992ab9"},
    {file = "markupsafe-3.0.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:a4afe79fb3de0b7097d81da19090f4df4f8d3a2b3adaa8764138aac2e44f3af1"},
    {file = "markupsafe-3.0.3-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:795e7751525cae078558e679d646ae45574b47ed6e7771863fcc079a6171a0fc"},
    {file = "markupsafe-3.0.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:8485f406a96febb5140bfeca44a73e3ce5116b2501ac54fe953e488fb1d03b12"},
    {file = "markupsafe-3.0.3-cp313-cp313-win32.whl", hash = "sha256:bdd37121970bfd8be76c5fb069c7751683bdf373db1ed6c010162b2a130248ed"},
    {file = "markupsafe-3.0.3-cp313-cp313-win_amd64.whl", hash = "sha256:9a1abfdc021a164803f4d485104931fb8f8c1efd55bc6b748d2f5774e78b62c5"},
    {file = "markupsafe-3.0.3-cp313-cp313-win_arm64.whl", hash = "sha256:7e68f88e5b8799aa49c85cd116c932a1ac15caaa3f5db09087854d218359e485"},
    {file = "markupsafe-3.0.3-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:218551f6df4868a8d527e3062d0fb968682fe92054e89978594c28e642c43a73"},
    {file = "markupsafe-3.0.3-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:3524b778fe5cfb3452a09d31e7b5adefeea8c5be1d43c4f810ba09f2ceb29d37"},
    {file = "markupsafe-3.0.3-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:4e885a3d1efa2eadc93c894a21770e4bc67899e3543680313b09f139e149ab19"},
    {file = "markupsafe-3.0.3-cp313-cp313t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:8709b08f4a89aa7586de0aadc8da56180242ee0ada3999749b183aa23df95025"},
    {file = "markupsafe-3.0.3-cp313-cp313t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:b8512a91625c9b3da6f127803b166b629725e68af71f8184ae7e7d54686a56d6"},
    {file = "markupsafe-3.0.3-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:9b79b7a16f7fedff2495d684f2b59b0457c3b493778c9eed31111be64d58279f"},
    {file = "markupsafe-3.0.3-cp313-cp313t-musllinux_1_2_riscv64.whl", hash = "sha256:12c63dfb4a98206f045aa9563db46507995f7ef6d83b2f68eda65c307c6829eb"},
    {file = "markupsafe-3.0.3-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:8f71bc33915be5186016f675cd83a1e08523649b0e33efdb898db577ef5bb009"},
    {file = "markupsafe-3.0.3-cp313-cp313t-win32.whl", hash = "sha256:69c0b73548bc525c8cb9a251cddf1931d1db4d2258e9599c28c07ef3580ef354"},
    {file = "markupsafe-3.0.3-cp313-cp313t-win_amd64.whl", hash = "sha256:1b4b79e8ebf6b55351f0d91fe80f893b4743f104bff22e90697db1590e47a218"},
    {file = "markupsafe-3.0.3-cp313-cp313t-win_arm64.whl", hash = "sha256:ad2cf8aa28b8c020ab2fc8287b0f823d0a7d8630784c31e9ee5edea20f406287"},
    {file = "markupsafe-3.0.3-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:eaa9599de571d72e2daf60164784109f19978b327a3910d3e9de8c97b5b70cfe"},
    {file = "markupsafe-3.0.3-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:c47a551199eb8eb2121d4f0f15ae0f923d31350ab9280078d1e5f12b249e0026"},
    {file = "markupsafe-3.0.3-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f34c41761022dd093b4b6896d4810782ffbabe30f2d443ff5f083e0cbbb8c737"},
    {file = "markupsafe-3.0.3-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:457a69a9577064c05a97c41f4e65148652db078a3a509039e64d3467b9e7ef97"},
    {file = "markupsafe-3.0.3-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:e8afc3f2ccfa24215f8cb28dcf43f0113ac3c37c2f0f0806d8c70e4228c5cf4d"},
    {file = "markupsafe-3.0.3-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:ec15a59cf5af7be74194f7ab02d0f59a62bdcf1a537677ce67a2537c9b87fcda"},
    {file = "markupsafe-3.0.3-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:0eb9ff8191e8498cca014656ae6b8d61f39da5f95b488805da4bb029cccbfbaf"},
    {file = "markupsafe-3.0.3-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:2713baf880df847f2bece4230d4d094280f4e67b1e813eec43b4c0e144a34ffe"},
    {file = "markupsafe-3.0.3-cp314-cp314-win32.whl", hash = "sha256:729586769a26dbceff69f7a7dbbf59ab6572b99d94576a5592625d5b411576b9"},
    {file = "markupsafe-3.0.3-cp314-cp314-win_amd64.whl", hash = "sha256:bdc919ead48f234740ad807933cdf545180bfbe9342c2bb451556db2ed958581"},
    {file = "markupsafe-3.0.3-cp314-cp314-win_arm64.whl", hash = "sha256:5a7d5dc5140555cf21a6fefbdbf8723f06fcd2f63ef108f2854de715e4422cb4"},
    {file = "markupsafe-3.0.3-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:1353ef0c1b138e1907ae78e2f6c63ff67501122006b0f9abad68fda5f4ffc6ab"},
    {file = "markupsafe-3.0.3-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:1085e7fbddd3be5f89cc898938f42c0b3c711fdcb37d75221de2666af647c175"},
    {file = "markupsafe-3.0.3-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1b52b4fb9df4eb9ae465f8d0c228a00624de2334f216f178a995ccdcf82c4634"},
    {file = "markupsafe-3.0.3-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:fed51ac40f757d41b7c48425901843666a6677e3e8eb0abcff09e4ba6e664f50"},
    {file = "markupsafe-3.0.3-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:f190daf01f13c72eac4efd5c430a8de82489d9cff23c364c3ea822545032993e"},
    {file = "markupsafe-3.0.3-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:e56b7d45a839a697b5eb268c82a71bd8c7f6c94d6fd50c3d577fa39a9f1409f5"},
    {file = "markupsafe-3.0.3-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:f3e98bb3798ead92273dc0e5fd0f31ade220f59a266ffd8a4f6065e0a3ce0523"},
    {file = "markupsafe-3.0.3-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:5678211cb9333a6468fb8d8be0305520aa073f50d17f089b5b4b477ea6e67fdc"},
    {file = "markupsafe-3.0.3-cp314-cp314t-win32.whl", hash = "sha256:915c04ba3851909ce68ccc2b8e2cd691618c4dc4c4232fb7982bca3f41fd8c3d"},
    {file = "markupsafe-3.0.3-cp314-cp314t-win_amd64.whl", hash = "sha256:4faffd047e07c38848ce017e8725090413cd80cbc23d86e55c587bf979e579c9"},
    {file = "markupsafe-3.0.3-cp314-cp314t-win_arm64.whl", hash = "sha256:32001d6a8fc98c8cb5c947787c5d08b0a50663d139f1305bac5885d98d9b40fa"},
    {file = "markupsafe-3.0.3-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:15d939a21d546304880945ca1ecb8a039db6b4dc49b2c5a400387cdae6a62e26"},
    {file = "markupsafe-3.0.3-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:f71a396b3bf33ecaa1626c255855702aca4d3d9fea5e051b41ac59a9c1c41edc"},
    {file = "markupsafe-3.0.3-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0f4b68347f8c5eab4a13419215bdfd7f8c9b19f2b25520968adfad23eb0ce60c"},
    {file = "markupsafe-3.0.3-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e8fc20152abba6b83724d7ff268c249fa196d8259ff481f3b1476383f8f24e42"},
    {file = "markupsafe-3.0.3-cp39-cp39-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:949b8d66bc381ee8b007cd945914c721d9aba8e27f71959d750a46f7c282b20b"},
    {file = "markupsafe-3.0.3-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:3537e01efc9d4dccdf77221fb1cb3b8e1a38d5428920e0657ce299b20324d758"},
    {file = "markupsafe-3.0.3-cp39-cp39-musllinux_1_2_riscv64.whl", hash = "sha256:591ae9f2a647529ca990bc681daebdd52c8791ff06c2bfa05b65163e28102ef2"},
    {file = "markupsafe-3.0.3-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:a320721ab5a1aba0a233739394eb907f8c8da5c98c9181d1161e77a0c8e36f2d"},
    {file = "markupsafe-3.0.3-cp39-cp39-win32.whl", hash = "sha256:df2449253ef108a379b8b5d6b43f4b1a8e81a061d6537becd5582fba5f9196d7"},
    {file = "markupsafe-3.0.3-cp39-cp39-win_amd64.whl", hash = "sha256:7c3fb7d25180895632e5d3148dbdc29ea38ccb7fd210aa27acbd1201a1902c6e"},
    {file = "markupsafe-3.0.3-cp39-cp39-win_arm64.whl", hash = "sha256:38664109c14ffc9e7437e86b4dceb442b0096dfe3541d7864d9cbe1da4cf36c8"},
    {file = "markupsafe-3.0.3.tar.gz", hash = "sha256:722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698"},
]

[[package]]
name = "mypy-extensions"
version = "1.1.0"
description = "Type system extensions for programs checked with the mypy type checker."
optional = false
python-versions = ">=3.8"
groups = ["main", "dev"]
files = [
    {file = "mypy_extensions-1.1.0-py3-none-any.whl", hash = "sha256:1be4cccdb0f2482337c4743e60421de3a356cd97508abadd57d47403e94f5505"},
    {file = "mypy_extensions-1.1.0.tar.gz", hash = "sha256:52e68efc3284861e772bbcd66823fde5ae21fd2fdb51c62a211403730b916558"},
]

[[package]]
name = "ni-grpc-extensions"
version = "1.1.0"
description = "gRPC Extensions"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_grpc_extensions-1.1.0-py3-none-any.whl", hash = "sha256:db0357acd244854f4acccf202c89fe6462b4283d264ed639f4e248e6cc86bc9b"},
    {file = "ni_grpc_extensions-1.1.0.tar.gz", hash = "sha256:028ea33e5c5234bc050bf5dc99f5b61611531de8f012293e9d4c6985b7b37afb"},
]

[package.dependencies]
grpcio = ">=1.49.0,<2.0"
traceloggingdynamic = {version = ">=1.0", markers = "sys_platform == \"win32\""}

[[package]]
name = "ni-grpcdevice-v1-proto"
version = "1.1.0"
description = "Protobuf generated code for the nidevice_grpc gRPC API"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_grpcdevice_v1_proto-1.1.0-py3-none-any.whl", hash = "sha256:2784c4b3e64a9c1e6b743d26847b7a44bf781ab46a9e19b02b379c1e0bc6dcfb"},
    {file = "ni_grpcdevice_v1_proto-1.1.0.tar.gz", hash = "sha256:ad14ab44e456a67d50a8fc38329e01dccae1732eab22a529c96eb3d5cb46370c"},
]

[package.dependencies]
grpcio = ">=1.49.0,<2.0"
protobuf = ">=4.21"

[[package]]
name = "ni-measurement-plugin-sdk-generator"
version = "3.2.0.dev0"
description = "Measurement Plug-In Code Generator for Python"
optional = false
python-versions = "^3.10"
groups = ["main", "dev"]
files = []
develop = true

[package.dependencies]
black = ">=24.8.0"
click = ">=8.1.3"
click-option-group = ">=0.5.6"
grpcio = "^1.49.1"
Mako = "^1.2.1"
ni-grpc-extensions = "^1.0.0"
ni-grpcdevice-v1-proto = "^1.0.0"
ni-measurement-plugin-sdk-service = ">=2.2.0"
ni-measurementlink-discovery-v1-client = "^1.0.0"
ni-measurementlink-pinmap-v1-client = "^1.0.0"
ni-protobuf-types = "^1.0.0"
protobuf = ">=4.21"

[package.source]
type = "directory"
url = "../generator"

[[package]]
name = "ni-measurement-plugin-sdk-service"
version = "3.2.0.dev0"
description = "Measurement Plug-In Support for Python"
optional = false
python-versions = "^3.10"
groups = ["main", "dev"]
files = []
develop = true

[package.dependencies]
deprecation = ">=2.1"
grpcio = "^1.49.1"
ni-grpc-extensions = "^1.0.0"
ni-measurementlink-discovery-v1-client = "^1.0.0"
ni-measurementlink-measurement-v1-proto = "^1.0.0"
ni-measurementlink-measurement-v2-proto = "^1.0.0"
ni-measurementlink-pinmap-v1-client = "^1.0.0"
ni-measurementlink-sessionmanagement-v1-client = "^1.0.0"
ni-protobuf-types = "^1.0.0"
protobuf = ">=4.21"
python-decouple = ">=3.8"
pywin32 = {version = ">=303", markers = "sys_platform == \"win32\""}

[package.extras]
drivers = ["nidaqmx[grpc] (>=0.8.0)", "nidcpower[grpc] (>=1.4.4)", "nidigital[grpc] (>=1.4.4)", "nidmm[grpc] (>=1.4.4)", "nifgen[grpc] (>=1.4.4)", "niscope[grpc] (>=1.4.4)", "niswitch[grpc] (>=1.4.4)"]
nidaqmx = ["nidaqmx[grpc] (>=0.8.0)"]
nidcpower = ["nidcpower[grpc] (>=1.4.4)"]
nidigital = ["nidigital[grpc] (>=1.4.4)"]
nidmm = ["nidmm[grpc] (>=1.4.4)"]
nifgen = ["nifgen[grpc] (>=1.4.4)"]
niscope = ["niscope[grpc] (>=1.4.4)"]
niswitch = ["niswitch[grpc] (>=1.4.4)"]

[package.source]
type = "directory"
url = "../service"

[[package]]
name = "ni-measurementlink-discovery-v1-client"
version = "1.1.0"
description = "gRPC Client for NI Discovery Service"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_measurementlink_discovery_v1_client-1.1.0-py3-none-any.whl", hash = "sha256:366dcc3b93627ed1ede488955637e0768b29cb7a375e59ac1020f4c53892d00c"},
    {file = "ni_measurementlink_discovery_v1_client-1.1.0.tar.gz", hash = "sha256:831b6145cf8def0021cb00579b08a2ad1da5a19fdeedea4522a3cb4a30978c48"},
]

[package.dependencies]
grpcio = ">=1.49.0,<2.0"
ni-grpc-extensions = ">=1.1.0"
ni-measurementlink-discovery-v1-proto = ">=1.1.0"
pywin32 = {version = ">=303", markers = "sys_platform == \"win32\""}

[[package]]
name = "ni-measurementlink-discovery-v1-proto"
version = "1.1.0"
description = "Protobuf data types for NI discovery gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_measurementlink_discovery_v1_proto-1.1.0-py3-none-any.whl", hash = "sha256:6a3061ca858d3ee887987dc5130074fc439ce6c2b26fe6b3f9401da023461d43"},
    {file = "ni_measurementlink_discovery_v1_proto-1.1.0.tar.gz", hash = "sha256:f9a9b4572ac5d169fad21ab56e2639abdb77979cf0dc3a88cdb71b2c783d009c"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-measurementlink-measurement-v1-proto"
version = "1.1.1"
description = "Protobuf data types for NI measurement gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_measurementlink_measurement_v1_proto-1.1.1-py3-none-any.whl", hash = "sha256:cb0e1e26f8d08829de46f5707061aacbbb6e42248811bac7eababbdd524f0196"},
    {file = "ni_measurementlink_measurement_v1_proto-1.1.1.tar.gz", hash = "sha256:81b1d321d78b2f15e2cbd41316314f39a9446866928f29a69ed501bd911be6f7"},
]

[package.dependencies]
ni-measurementlink-proto = ">=1.1.0"
protobuf = ">=4.21"

[[package]]
name = "ni-measurementlink-measurement-v2-proto"
version = "1.1.1"
description = "Protobuf data types for NI measurement gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_measurementlink_measurement_v2_proto-1.1.1-py3-none-any.whl", hash = "sha256:2776adb4402f58ad6fc23436349989eb92b74a718dcbb084aab65fcce3b43b51"},
    {file = "ni_measurementlink_measurement_v2_proto-1.1.1.tar.gz", hash = "sha256:de236b4b02a03730be6d94b362edba01c1b11fb803436bd2a65fdb7bc95bf605"},
]

[package.dependencies]
ni-measurementlink-proto = ">=1.0.0"
protobuf = ">=4.21"

[[package]]
name = "ni-measurementlink-pinmap-v1-client"
version = "1.1.0"
description = "gRPC Client for NI Pin Map Service"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_measurementlink_pinmap_v1_client-1.1.0-py3-none-any.whl", hash = "sha256:2d758aa15addd78fde63e57a69e4c4cbb25e1689c4ce2e5d7b456c22c1b3607e"},
    {file = "ni_measurementlink_pinmap_v1_client-1.1.0.tar.gz", hash = "sha256:ae5b406781544071ea46a5afb862daeb29e989ce67beb80972f88fb80135bc4f"},
]

[package.dependencies]
grpcio = ">=1.49.0,<2.0"
ni-grpc-extensions = ">=1.1.0"
ni-measurementlink-discovery-v1-client = ">=1.1.0"
ni-measurementlink-measurement-v1-proto = ">=1.1.1"
ni-measurementlink-measurement-v2-proto = ">=1.1.1"
ni-measurementlink-pinmap-v1-proto = ">=1.1.0"
ni-measurementlink-sessionmanagement-v1-client = ">=1.1.0"

[[package]]
name = "ni-measurementlink-pinmap-v1-proto"
version = "1.1.0"
description = "Protobuf data types for NI pinmap gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_measurementlink_pinmap_v1_proto-1.1.0-py3-none-any.whl", hash = "sha256:c2334d2ffe4e11f776b0087ad25184b504faa63fa57ec3c7eb87e1a3234dd686"},
    {file = "ni_measurementlink_pinmap_v1_proto-1.1.0.tar.gz", hash = "sha256:db6cef7969c6423349e6560850983008a269a3de0ca7dd623795d7153ede64c1"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-measurementlink-proto"
version = "1.1.0"
description = "Protobuf data types for NI gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_measurementlink_proto-1.1.0-py3-none-any.whl", hash = "sha256:b7fb6c7b6c36a80d0a1e67fd47d2fa6cccfed993dd5047aa720b04f07c5a546e"},
    {file = "ni_measurementlink_proto-1.1.0.tar.gz", hash = "sha256:4fca44af39715f8501d711944f4d6bae11f1b9ffa059a6995eb69770872c3fa5"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-measurementlink-sessionmanagement-v1-client"
version = "1.1.0"
description = "Client gRPC APIs for the session management service"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_measurementlink_sessionmanagement_v1_client-1.1.0-py3-none-any.whl", hash = "sha256:90ddf2561f82c8b32d9e86908326c8e50c388f6e74c1ea2bac758f4e10553a3f"},
    {file = "ni_measurementlink_sessionmanagement_v1_client-1.1.0.tar.gz", hash = "sha256:53348004828452fe0de3cae89e0aed4952a120254beb346b8764428373116038"},
]

[package.dependencies]
deprecation = ">=2.1"
ni-grpc-extensions = ">=1.1.0"
ni-grpcdevice-v1-proto = ">=1.1.0"
ni-measurementlink-discovery-v1-client = ">=1.1.0"
ni-measurementlink-pinmap-v1-proto = ">=1.1.0"
ni-measurementlink-proto = ">=1.1.0"
ni-measurementlink-sessionmanagement-v1-proto = ">=1.1.0"
protobuf = ">=4.21"
python-decouple = ">=3.8"
pywin32 = {version = ">=303", markers = "sys_platform == \"win32\""}
traceloggingdynamic = {version = ">=1.0", markers = "sys_platform == \"win32\""}

[package.extras]
drivers = ["nidaqmx[grpc] (>=0.8.0)", "nidcpower[grpc] (>=1.4.4)", "nidigital[grpc] (>=1.4.4)", "nidmm[grpc] (>=1.4.4)", "nifgen[grpc] (>=1.4.4)", "niscope[grpc] (>=1.4.4)", "niswitch[grpc] (>=1.4.4)"]
nidaqmx = ["nidaqmx[grpc] (>=0.8.0)"]
nidcpower = ["nidcpower[grpc] (>=1.4.4)"]
nidigital = ["nidigital[grpc] (>=1.4.4)"]
nidmm = ["nidmm[grpc] (>=1.4.4)"]
nifgen = ["nifgen[grpc] (>=1.4.4)"]
niscope = ["niscope[grpc] (>=1.4.4)"]
niswitch = ["niswitch[grpc] (>=1.4.4)"]

[[package]]
name = "ni-measurementlink-sessionmanagement-v1-proto"
version = "1.1.0"
description = "Protobuf data types for NI session management gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_measurementlink_sessionmanagement_v1_proto-1.1.0-py3-none-any.whl", hash = "sha256:e88d8beaf141e85f83daba1858a8b372df9d2c2671b3c4b0bb3b50e745e14585"},
    {file = "ni_measurementlink_sessionmanagement_v1_proto-1.1.0.tar.gz", hash = "sha256:cedc461b7990bc496ac87a932ca32f7b9f6f1c73c8eb5bda71f5e60709ef76e1"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-protobuf-types"
version = "1.1.0"
description = "Protobuf data types for NI gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main", "dev"]
files = [
    {file = "ni_protobuf_types-1.1.0-py3-none-any.whl", hash = "sha256:0c21c096cf8577483dade081c571305fe8d4cc759ce2c780e7437129a375942c"},
    {file = "ni_protobuf_types-1.1.0.tar.gz", hash = "sha256:98f0583405e219f6e128133c2f6c033f03cd83ebd3ce8098ad74ab99b8a253c1"},
]

[package.dependencies]
nitypes = ">=1.1.0.dev1"
protobuf = ">=4.21"

[[package]]
name = "nitypes"
version = "1.1.0.dev1"
description = "Data types for NI Python APIs"
optional = false
python-versions = "<4.0,>=3.9"
groups = ["main", "dev"]
files = [
    {file = "nitypes-1.1.0.dev1-py3-none-any.whl", hash = "sha256:d98ad6e3f8b92db76b5c1c584431fa27d3e74cce6e20464e43ee0117b02fe089"},
    {file = "nitypes-1.1.0.dev1.tar.gz", hash = "sha256:50b23e00cc6960996656c4c9ef0ca71dd267fc5c9ca481077b682c29190aa2d3"},
]

[package.dependencies]
hightime = ">=0.2.2"
numpy = [
    {version = ">=2.1", markers = "python_version >= \"3.13\" and python_version < \"4.0\""},
    {version = ">=1.22", markers = "python_version >= \"3.9\" and python_version < \"3.13\""},
]
typing-extensions = ">=4.13.2"

[[package]]
name = "numpy"
version = "2.2.6"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.10"
groups = ["main", "dev"]
markers = "python_version < \"3.13\""
files = [
    {file = "numpy-2.2.6-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:b412caa66f72040e6d268491a59f2c43bf03eb6c96dd8f0307829feb7fa2b6fb"},
    {file = "numpy-2.2.6-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:8e41fd67c52b86603a91c1a505ebaef50b3314de0213461c7a6e99c9a3beff90"},
    {file = "numpy-2.2.6-cp310-cp310-macosx_14_0_arm64.whl", hash = "sha256:37e990a01ae6ec7fe7fa1c26c55ecb672dd98b19c3d0e1d1f326fa13cb38d163"},
    {file = "numpy-2.2.6-cp310-cp310-macosx_14_0_x86_64.whl", hash = "sha256:5a6429d4be8ca66d889b7cf70f536a397dc45ba6faeb5f8c5427935d9592e9cf"},
    {file = "numpy-2.2.6-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:efd28d4e9cd7d7a8d39074a4d44c63eda73401580c5c76acda2ce969e0a38e83"},
    {file = "numpy-2.2.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fc7b73d02efb0e18c000e9ad8b83480dfcd5dfd11065997ed4c6747470ae8915"},
    {file = "numpy-2.2.6-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:74d4531beb257d2c3f4b261bfb0fc09e0f9ebb8842d82a7b4209415896adc680"},
    {file = "numpy-2.2.6-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:8fc377d995680230e83241d8a96def29f204b5782f371c532579b4f20607a289"},
    {file = "numpy-2.2.6-cp310-cp310-win32.whl", hash = "sha256:b093dd74e50a8cba3e873868d9e93a85b78e0daf2e98c6797566ad8044e8363d"},
    {file = "numpy-2.2.6-cp310-cp310-win_amd64.whl", hash = "sha256:f0fd6321b839904e15c46e0d257fdd101dd7f530fe03fd6359c1ea63738703f3"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:f9f1adb22318e121c5c69a09142811a201ef17ab257a1e66ca3025065b7f53ae"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:c820a93b0255bc360f53eca31a0e676fd1101f673dda8da93454a12e23fc5f7a"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:3d70692235e759f260c3d837193090014aebdf026dfd167834bcba43e30c2a42"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:481b49095335f8eed42e39e8041327c05b0f6f4780488f61286ed3c01368d491"},
    {file = "numpy-2.2.6-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b64d8d4d17135e00c8e346e0a738deb17e754230d7e0810ac5012750bbd85a5a"},
    {file = "numpy-2.2.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ba10f8411898fc418a521833e014a77d3ca01c15b0c6cdcce6a0d2897e6dbbdf"},
    {file = "numpy-2.2.6-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:bd48227a919f1bafbdda0583705e547892342c26fb127219d60a5c36882609d1"},
    {file = "numpy-2.2.6-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:9551a499bf125c1d4f9e250377c1ee2eddd02e01eac6644c080162c0c51778ab"},
    {file = "numpy-2.2.6-cp311-cp311-win32.whl", hash = "sha256:0678000bb9ac1475cd454c6b8c799206af8107e310843532b04d49649c717a47"},
    {file = "numpy-2.2.6-cp311-cp311-win_amd64.whl", hash = "sha256:e8213002e427c69c45a52bbd94163084025f533a55a59d6f9c5b820774ef3303"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:41c5a21f4a04fa86436124d388f6ed60a9343a6f767fced1a8a71c3fbca038ff"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:de749064336d37e340f640b05f24e9e3dd678c57318c7289d222a8a2f543e90c"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:894b3a42502226a1cac872f840030665f33326fc3dac8e57c607905773cdcde3"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:71594f7c51a18e728451bb50cc60a3ce4e6538822731b2933209a1f3614e9282"},
    {file = "numpy-2.2.6-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f2618db89be1b4e05f7a1a847a9c1c0abd63e63a1607d892dd54668dd92faf87"},
    {file = "numpy-2.2.6-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fd83c01228a688733f1ded5201c678f0c53ecc1006ffbc404db9f7a899ac6249"},
    {file = "numpy-2.2.6-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:37c0ca431f82cd5fa716eca9506aefcabc247fb27ba69c5062a6d3ade8cf8f49"},
    {file = "numpy-2.2.6-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:fe27749d33bb772c80dcd84ae7e8df2adc920ae8297400dabec45f0dedb3f6de"},
    {file = "numpy-2.2.6-cp312-cp312-win32.whl", hash = "sha256:4eeaae00d789f66c7a25ac5f34b71a7035bb474e679f410e5e1a94deb24cf2d4"},
    {file = "numpy-2.2.6-cp312-cp312-win_amd64.whl", hash = "sha256:c1f9540be57940698ed329904db803cf7a402f3fc200bfe599334c9bd84a40b2"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:0811bb762109d9708cca4d0b13c4f67146e3c3b7cf8d34018c722adb2d957c84"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:287cc3162b6f01463ccd86be154f284d0893d2b3ed7292439ea97eafa8170e0b"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:f1372f041402e37e5e633e586f62aa53de2eac8d98cbfb822806ce4bbefcb74d"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:55a4d33fa519660d69614a9fad433be87e5252f4b03850642f88993f7b2ca566"},
    {file = "numpy-2.2.6-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f92729c95468a2f4f15e9bb94c432a9229d0d50de67304399627a943201baa2f"},
    {file = "numpy-2.2.6-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1bc23a79bfabc5d056d106f9befb8d50c31ced2fbc70eedb8155aec74a45798f"},
    {file = "numpy-2.2.6-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:e3143e4451880bed956e706a3220b4e5cf6172ef05fcc397f6f36a550b1dd868"},
    {file = "numpy-2.2.6-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:b4f13750ce79751586ae2eb824ba7e1e8dba64784086c98cdbbcc6a42112ce0d"},
    {file = "numpy-2.2.6-cp313-cp313-win32.whl", hash = "sha256:5beb72339d9d4fa36522fc63802f469b13cdbe4fdab4a288f0c441b74272ebfd"},
    {file = "numpy-2.2.6-cp313-cp313-win_amd64.whl", hash = "sha256:b0544343a702fa80c95ad5d3d608ea3599dd54d4632df855e4c8d24eb6ecfa1c"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:0bca768cd85ae743b2affdc762d617eddf3bcf8724435498a1e80132d04879e6"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:fc0c5673685c508a142ca65209b4e79ed6740a4ed6b2267dbba90f34b0b3cfda"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_14_0_arm64.whl", hash = "sha256:5bd4fc3ac8926b3819797a7c0e2631eb889b4118a9898c84f585a54d475b7e40"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_14_0_x86_64.whl", hash = "sha256:fee4236c876c4e8369388054d02d0e9bb84821feb1a64dd59e137e6511a551f8"},
    {file = "numpy-2.2.6-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e1dda9c7e08dc141e0247a5b8f49cf05984955246a327d4c48bda16821947b2f"},
    {file = "numpy-2.2.6-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f447e6acb680fd307f40d3da4852208af94afdfab89cf850986c3ca00562f4fa"},
    {file = "numpy-2.2.6-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:389d771b1623ec92636b0786bc4ae56abafad4a4c513d36a55dce14bd9ce8571"},
    {file = "numpy-2.2.6-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:8e9ace4a37db23421249ed236fdcdd457d671e25146786dfc96835cd951aa7c1"},
    {file = "numpy-2.2.6-cp313-cp313t-win32.whl", hash = "sha256:038613e9fb8c72b0a41f025a7e4c3f0b7a1b5d768ece4796b674c8f3fe13efff"},
    {file = "numpy-2.2.6-cp313-cp313t-win_amd64.whl", hash = "sha256:6031dd6dfecc0cf9f668681a37648373bddd6421fff6c66ec1624eed0180ee06"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-macosx_10_15_x86_64.whl", hash = "sha256:0b605b275d7bd0c640cad4e5d30fa701a8d59302e127e5f79138ad62762c3e3d"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-macosx_14_0_x86_64.whl", hash = "sha256:7befc596a7dc9da8a337f79802ee8adb30a552a94f792b9c9d18c840055907db"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ce47521a4754c8f4593837384bd3424880629f718d87c5d44f8ed763edd63543"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:d042d24c90c41b54fd506da306759e06e568864df8ec17ccc17e9e884634fd00"},
    {file = "numpy-2.2.6.tar.gz", hash = "sha256:e29554e2bef54a90aa5cc07da6ce955accb83f21ab5de01a62c8478897b264fd"},
]

[[package]]
name = "numpy"
version = "2.4.1"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.11"
groups = ["main", "dev"]
markers = "python_version >= \"3.13\""
files = [
    {file = "numpy-2.4.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:0cce2a669e3c8ba02ee563c7835f92c153cf02edff1ae05e1823f1dde21b16a5"},
    {file = "numpy-2.4.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:899d2c18024984814ac7e83f8f49d8e8180e2fbe1b2e252f2e7f1d06bea92425"},
    {file = "numpy-2.4.1-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:09aa8a87e45b55a1c2c205d42e2808849ece5c484b2aab11fecabec3841cafba"},
    {file = "numpy-2.4.1-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:edee228f76ee2dab4579fad6f51f6a305de09d444280109e0f75df247ff21501"},
    {file = "numpy-2.4.1-cp311-cp311-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:a92f227dbcdc9e4c3e193add1a189a9909947d4f8504c576f4a732fd0b54240a"},
    {file = "numpy-2.4.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:538bf4ec353709c765ff75ae616c34d3c3dca1a68312727e8f2676ea644f8509"},
    {file = "numpy-2.4.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:ac08c63cb7779b85e9d5318e6c3518b424bc1f364ac4cb2c6136f12e5ff2dccc"},
    {file = "numpy-2.4.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:4f9c360ecef085e5841c539a9a12b883dff005fbd7ce46722f5e9cef52634d82"},
    {file = "numpy-2.4.1-cp311-cp311-win32.whl", hash = "sha256:0f118ce6b972080ba0758c6087c3617b5ba243d806268623dc34216d69099ba0"},
    {file = "numpy-2.4.1-cp311-cp311-win_amd64.whl", hash = "sha256:18e14c4d09d55eef39a6ab5b08406e84bc6869c1e34eef45564804f90b7e0574"},
    {file = "numpy-2.4.1-cp311-cp311-win_arm64.whl", hash = "sha256:6461de5113088b399d655d45c3897fa188766415d0f568f175ab071c8873bd73"},
    {file = "numpy-2.4.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:d3703409aac693fa82c0aee023a1ae06a6e9d065dba10f5e8e80f642f1e9d0a2"},
    {file = "numpy-2.4.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:7211b95ca365519d3596a1d8688a95874cc94219d417504d9ecb2df99fa7bfa8"},
    {file = "numpy-2.4.1-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:5adf01965456a664fc727ed69cc71848f28d063217c63e1a0e200a118d5eec9a"},
    {file = "numpy-2.4.1-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:26f0bcd9c79a00e339565b303badc74d3ea2bd6d52191eeca5f95936cad107d0"},
    {file = "numpy-2.4.1-cp312-cp312-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0093e85df2960d7e4049664b26afc58b03236e967fb942354deef3208857a04c"},
    {file = "numpy-2.4.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:7ad270f438cbdd402c364980317fb6b117d9ec5e226fff5b4148dd9aa9fc6e02"},
    {file = "numpy-2.4.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:297c72b1b98100c2e8f873d5d35fb551fce7040ade83d67dd51d38c8d42a2162"},
    {file = "numpy-2.4.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:cf6470d91d34bf669f61d515499859fa7a4c2f7c36434afb70e82df7217933f9"},
    {file = "numpy-2.4.1-cp312-cp312-win32.whl", hash = "sha256:b6bcf39112e956594b3331316d90c90c90fb961e39696bda97b89462f5f3943f"},
    {file = "numpy-2.4.1-cp312-cp312-win_amd64.whl", hash = "sha256:e1a27bb1b2dee45a2a53f5ca6ff2d1a7f135287883a1689e930d44d1ff296c87"},
    {file = "numpy-2.4.1-cp312-cp312-win_arm64.whl", hash = "sha256:0e6e8f9d9ecf95399982019c01223dc130542960a12edfa8edd1122dfa66a8a8"},
    {file = "numpy-2.4.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:d797454e37570cfd61143b73b8debd623c3c0952959adb817dd310a483d58a1b"},
    {file = "numpy-2.4.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:82c55962006156aeef1629b953fd359064aa47e4d82cfc8e67f0918f7da3344f"},
    {file = "numpy-2.4.1-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:71abbea030f2cfc3092a0ff9f8c8fdefdc5e0bf7d9d9c99663538bb0ecdac0b9"},
    {file = "numpy-2.4.1-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:5b55aa56165b17aaf15520beb9cbd33c9039810e0d9643dd4379e44294c7303e"},
    {file = "numpy-2.4.1-cp313-cp313-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c0faba4a331195bfa96f93dd9dfaa10b2c7aa8cda3a02b7fd635e588fe821bf5"},
    {file = "numpy-2.4.1-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d3e3087f53e2b4428766b54932644d148613c5a595150533ae7f00dab2f319a8"},
    {file = "numpy-2.4.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:49e792ec351315e16da54b543db06ca8a86985ab682602d90c60ef4ff4db2a9c"},
    {file = "numpy-2.4.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:79e9e06c4c2379db47f3f6fc7a8652e7498251789bf8ff5bd43bf478ef314ca2"},
    {file = "numpy-2.4.1-cp313-cp313-win32.whl", hash = "sha256:3d1a100e48cb266090a031397863ff8a30050ceefd798f686ff92c67a486753d"},
    {file = "numpy-2.4.1-cp313-cp313-win_amd64.whl", hash = "sha256:92a0e65272fd60bfa0d9278e0484c2f52fe03b97aedc02b357f33fe752c52ffb"},
    {file = "numpy-2.4.1-cp313-cp313-win_arm64.whl", hash = "sha256:20d4649c773f66cc2fc36f663e091f57c3b7655f936a4c681b4250855d1da8f5"},
    {file = "numpy-2.4.1-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:f93bc6892fe7b0663e5ffa83b61aab510aacffd58c16e012bb9352d489d90cb7"},
    {file = "numpy-2.4.1-cp313-cp313t-macosx_14_0_arm64.whl", hash = "sha256:178de8f87948163d98a4c9ab5bee4ce6519ca918926ec8df195af582de28544d"},
    {file = "numpy-2.4.1-cp313-cp313t-macosx_14_0_x86_64.whl", hash = "sha256:98b35775e03ab7f868908b524fc0a84d38932d8daf7b7e1c3c3a1b6c7a2c9f15"},
    {file = "numpy-2.4.1-cp313-cp313t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:941c2a93313d030f219f3a71fd3d91a728b82979a5e8034eb2e60d394a2b83f9"},
    {file = "numpy-2.4.1-cp313-cp313t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:529050522e983e00a6c1c6b67411083630de8b57f65e853d7b03d9281b8694d2"},
    {file = "numpy-2.4.1-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:2302dc0224c1cbc49bb94f7064f3f923a971bfae45c33870dcbff63a2a550505"},
    {file = "numpy-2.4.1-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:9171a42fcad32dcf3fa86f0a4faa5e9f8facefdb276f54b8b390d90447cff4e2"},
    {file = "numpy-2.4.1-cp313-cp313t-win32.whl", hash = "sha256:382ad67d99ef49024f11d1ce5dcb5ad8432446e4246a4b014418ba3a1175a1f4"},
    {file = "numpy-2.4.1-cp313-cp313t-win_amd64.whl", hash = "sha256:62fea415f83ad8fdb6c20840578e5fbaf5ddd65e0ec6c3c47eda0f69da172510"},
    {file = "numpy-2.4.1-cp313-cp313t-win_arm64.whl", hash = "sha256:a7870e8c5fc11aef57d6fea4b4085e537a3a60ad2cdd14322ed531fdca68d261"},
    {file = "numpy-2.4.1-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:3869ea1ee1a1edc16c29bbe3a2f2a4e515cc3a44d43903ad41e0cacdbaf733dc"},
    {file = "numpy-2.4.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:e867df947d427cdd7a60e3e271729090b0f0df80f5f10ab7dd436f40811699c3"},
    {file = "numpy-2.4.1-cp314-cp314-macosx_14_0_arm64.whl", hash = "sha256:e3bd2cb07841166420d2fa7146c96ce00cb3410664cbc1a6be028e456c4ee220"},
    {file = "numpy-2.4.1-cp314-cp314-macosx_14_0_x86_64.whl", hash = "sha256:f0a90aba7d521e6954670550e561a4cb925713bd944445dbe9e729b71f6cabee"},
    {file = "numpy-2.4.1-cp314-cp314-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5d558123217a83b2d1ba316b986e9248a1ed1971ad495963d555ccd75dcb1556"},
    {file = "numpy-2.4.1-cp314-cp314-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:2f44de05659b67d20499cbc96d49f2650769afcb398b79b324bb6e297bfe3844"},
    {file = "numpy-2.4.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:69e7419c9012c4aaf695109564e3387f1259f001b4326dfa55907b098af082d3"},
    {file = "numpy-2.4.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:2ffd257026eb1b34352e749d7cc1678b5eeec3e329ad8c9965a797e08ccba205"},
    {file = "numpy-2.4.1-cp314-cp314-win32.whl", hash = "sha256:727c6c3275ddefa0dc078524a85e064c057b4f4e71ca5ca29a19163c607be745"},
    {file = "numpy-2.4.1-cp314-cp314-win_amd64.whl", hash = "sha256:7d5d7999df434a038d75a748275cd6c0094b0ecdb0837342b332a82defc4dc4d"},
    {file = "numpy-2.4.1-cp314-cp314-win_arm64.whl", hash = "sha256:ce9ce141a505053b3c7bce3216071f3bf5c182b8b28930f14cd24d43932cd2df"},
    {file = "numpy-2.4.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:4e53170557d37ae404bf8d542ca5b7c629d6efa1117dac6a83e394142ea0a43f"},
    {file = "numpy-2.4.1-cp314-cp314t-macosx_14_0_arm64.whl", hash = "sha256:a73044b752f5d34d4232f25f18160a1cc418ea4507f5f11e299d8ac36875f8a0"},
    {file = "numpy-2.4.1-cp314-cp314t-macosx_14_0_x86_64.whl", hash = "sha256:fb1461c99de4d040666ca0444057b06541e5642f800b71c56e6ea92d6a853a0c"},
    {file = "numpy-2.4.1-cp314-cp314t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:423797bdab2eeefbe608d7c1ec7b2b4fd3c58d51460f1ee26c7500a1d9c9ee93"},
    {file = "numpy-2.4.1-cp314-cp314t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:52b5f61bdb323b566b528899cc7db2ba5d1015bda7ea811a8bcf3c89c331fa42"},
    {file = "numpy-2.4.1-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:42d7dd5fa36d16d52a84f821eb96031836fd405ee6955dd732f2023724d0aa01"},
    {file = "numpy-2.4.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:e7b6b5e28bbd47b7532698e5db2fe1db693d84b58c254e4389d99a27bb9b8f6b"},
    {file = "numpy-2.4.1-cp314-cp314t-win32.whl", hash = "sha256:5de60946f14ebe15e713a6f22850c2372fa72f4ff9a432ab44aa90edcadaa65a"},
    {file = "numpy-2.4.1-cp314-cp314t-win_amd64.whl", hash = "sha256:8f085da926c0d491ffff3096f91078cc97ea67e7e6b65e490bc8dcda65663be2"},
    {file = "numpy-2.4.1-cp314-cp314t-win_arm64.whl", hash = "sha256:6436cffb4f2bf26c974344439439c95e152c9a527013f26b3577be6c2ca64295"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-macosx_10_15_x86_64.whl", hash = "sha256:8ad35f20be147a204e28b6a0575fbf3540c5e5f802634d4258d55b1ff5facce1"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:8097529164c0f3e32bb89412a0905d9100bf434d9692d9fc275e18dcf53c9344"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-macosx_14_0_arm64.whl", hash = "sha256:ea66d2b41ca4a1630aae5507ee0a71647d3124d1741980138aa8f28f44dac36e"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-macosx_14_0_x86_64.whl", hash = "sha256:d3f8f0df9f4b8be57b3bf74a1d087fec68f927a2fab68231fdb442bf2c12e426"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:2023ef86243690c2791fd6353e5b4848eedaa88ca8a2d129f462049f6d484696"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:8361ea4220d763e54cff2fbe7d8c93526b744f7cd9ddab47afeff7e14e8503be"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-win_amd64.whl", hash = "sha256:4f1b68ff47680c2925f8063402a693ede215f0257f02596b1318ecdfb1d79e33"},
    {file = "numpy-2.4.1.tar.gz", hash = "sha256:a1ceafc5042451a858231588a104093474c6a5c57dcc724841f5c888d237d690"},
]

[[package]]
name = "packaging"
version = "26.0"
description = "Core utilities for Python packages"
optional = false
python-versions = ">=3.8"
groups = ["main", "dev"]
files = [
    {file = "packaging-26.0-py3-none-any.whl", hash = "sha256:b36f1fef9334a5588b4166f8bcd26a14e521f2b55e6b9de3aaa80d3ff7a37529"},
    {file = "packaging-26.0.tar.gz", hash = "sha256:00243ae351a257117b6a241061796684b084ed1c516a08c48a3f7e147a9d80b4"},
]

[[package]]
name = "pathspec"
version = "1.0.3"
description = "Utility library for gitignore style pattern matching of file paths."
optional = false
python-versions = ">=3.9"
groups = ["main", "dev"]
files = [
    {file = "pathspec-1.0.3-py3-none-any.whl", hash = "sha256:e80767021c1cc524aa3fb14bedda9c34406591343cc42797b386ce7b9354fb6c"},
    {file = "pathspec-1.0.3.tar.gz", hash = "sha256:bac5cf97ae2c2876e2d25ebb15078eb04d76e4b98921ee31c6f85ade8b59444d"},
]

[package.extras]
hyperscan = ["hyperscan (>=0.7)"]
optional = ["typing-extensions (>=4)"]
re2 = ["google-re2 (>=1.1)"]
tests = ["pytest (>=9)", "typing-extensions (>=4.15)"]

[[package]]
name = "platformdirs"
version = "4.5.1"
description = "A small Python package for determining appropriate platform-specific dirs, e.g. a `user data dir`."
optional = false
python-versions = ">=3.10"
groups = ["main", "dev"]
files = [
    {file = "platformdirs-4.5.1-py3-none-any.whl", hash = "sha256:d03afa3963c806a9bed9d5125c8f4cb2fdaf74a55ab60e5d59b3fde758104d31"},
    {file = "platformdirs-4.5.1.tar.gz", hash = "sha256:61d5cdcc6065745cdd94f0f878977f8de9437be93de97c1c12f853c9c0cdcbda"},
]

[package.extras]
docs = ["furo (>=2025.9.25)", "proselint (>=0.14)", "sphinx (>=8.2.3)", "sphinx-autodoc-typehints (>=3.2)"]
test = ["appdirs (==1.4.4)", "covdefaults (>=2.3)", "pytest (>=8.4.2)", "pytest-cov (>=7)", "pytest-mock (>=3.15.1)"]
type = ["mypy (>=1.18.2)"]

[[package]]
name = "protobuf"
version = "6.33.4"
description = ""
optional = false
python-versions = ">=3.9"
groups = ["main", "dev"]
files = [
    {file = "protobuf-6.33.4-cp310-abi3-win32.whl", hash = "sha256:918966612c8232fc6c24c78e1cd89784307f5814ad7506c308ee3cf86662850d"},
    {file = "protobuf-6.33.4-cp310-abi3-win_amd64.whl", hash = "sha256:8f11ffae31ec67fc2554c2ef891dcb561dae9a2a3ed941f9e134c2db06657dbc"},
    {file = "protobuf-6.33.4-cp39-abi3-macosx_10_9_universal2.whl", hash = "sha256:2fe67f6c014c84f655ee06f6f66213f9254b3a8b6bda6cda0ccd4232c73c06f0"},
    {file = "protobuf-6.33.4-cp39-abi3-manylinux2014_aarch64.whl", hash = "sha256:757c978f82e74d75cba88eddec479df9b99a42b31193313b75e492c06a51764e"},
    {file = "protobuf-6.33.4-cp39-abi3-manylinux2014_s390x.whl", hash = "sha256:c7c64f259c618f0bef7bee042075e390debbf9682334be2b67408ec7c1c09ee6"},
    {file = "protobuf-6.33.4-cp39-abi3-manylinux2014_x86_64.whl", hash = "sha256:3df850c2f8db9934de4cf8f9152f8dc2558f49f298f37f90c517e8e5c84c30e9"},
    {file = "protobuf-6.33.4-cp39-cp39-win32.whl", hash = "sha256:955478a89559fa4568f5a81dce77260eabc5c686f9e8366219ebd30debf06aa6"},
    {file = "protobuf-6.33.4-cp39-cp39-win_amd64.whl", hash = "sha256:0f12ddbf96912690c3582f9dffb55530ef32015ad8e678cd494312bd78314c4f"},
    {file = "protobuf-6.33.4-py3-none-any.whl", hash = "sha256:1fe3730068fcf2e595816a6c34fe66eeedd37d51d0400b72fabc848811fdc1bc"},
    {file = "protobuf-6.33.4.tar.gz", hash = "sha256:dc2e61bca3b10470c1912d166fe0af67bfc20eb55971dcef8dfa48ce14f0ed91"},
]

[[package]]
name = "python-decouple"
version = "3.8"
description = "Strict separation of settings from code."
optional = false
python-versions = "*"
groups = ["main", "dev"]
files = [
    {file = "python-decouple-3.8.tar.gz", hash = "sha256:ba6e2657d4f376ecc46f77a3a615e058d93ba5e465c01bbe57289bfb7cce680f"},
    {file = "python_decouple-3.8-py3-none-any.whl", hash = "sha256:d0d45340815b25f4de59c974b855bb38d03151d81b037d9e3f463b0c9f8cbd66"},
]

[[package]]
name = "pytokens"
version = "0.4.0"
description = "A Fast, spec compliant Python 3.14+ tokenizer that runs on older Pythons."
optional = false
python-versions = ">=3.8"
groups = ["main", "dev"]
files = [
    {file = "pytokens-0.4.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:af0c3166aea367a9e755a283171befb92dd3043858b94ae9b3b7efbe9def26a3"},
    {file = "pytokens-0.4.0-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:daae524ed14ca459932cbf51d74325bea643701ba8a8b0cc2d10f7cd4b3e2b63"},
    {file = "pytokens-0.4.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e95cb158c44d642ed62f555bf8136bbe780dbd64d2fb0b9169e11ffb944664c3"},
    {file = "pytokens-0.4.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:df58d44630eaf25f587540e94bdf1fc50b4e6d5f212c786de0fb024bfcb8753a"},
    {file = "pytokens-0.4.0-cp310-cp310-win_amd64.whl", hash = "sha256:55efcc36f9a2e0e930cfba0ce7f83445306b02f8326745585ed5551864eba73a"},
    {file = "pytokens-0.4.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:92eb3ef88f27c22dc9dbab966ace4d61f6826e02ba04dac8e2d65ea31df56c8e"},
    {file = "pytokens-0.4.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f4b77858a680635ee9904306f54b0ee4781effb89e211ba0a773d76539537165"},
    {file = "pytokens-0.4.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:25cacc20c2ad90acb56f3739d87905473c54ca1fa5967ffcd675463fe965865e"},
    {file = "pytokens-0.4.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:628fab535ebc9079e4db35cd63cb401901c7ce8720a9834f9ad44b9eb4e0f1d4"},
    {file = "pytokens-0.4.0-cp311-cp311-win_amd64.whl", hash = "sha256:4d0f568d7e82b7e96be56d03b5081de40e43c904eb6492bf09aaca47cd55f35b"},
    {file = "pytokens-0.4.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:cd8da894e5a29ba6b6da8be06a4f7589d7220c099b5e363cb0643234b9b38c2a"},
    {file = "pytokens-0.4.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:237ba7cfb677dbd3b01b09860810aceb448871150566b93cd24501d5734a04b1"},
    {file = "pytokens-0.4.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:01d1a61e36812e4e971cfe2c0e4c1f2d66d8311031dac8bf168af8a249fa04dd"},
    {file = "pytokens-0.4.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:e47e2ef3ec6ee86909e520d79f965f9b23389fda47460303cf715d510a6fe544"},
    {file = "pytokens-0.4.0-cp312-cp312-win_amd64.whl", hash = "sha256:3d36954aba4557fd5a418a03cf595ecbb1cdcce119f91a49b19ef09d691a22ae"},
    {file = "pytokens-0.4.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:73eff3bdd8ad08da679867992782568db0529b887bed4c85694f84cdf35eafc6"},
    {file = "pytokens-0.4.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d97cc1f91b1a8e8ebccf31c367f28225699bea26592df27141deade771ed0afb"},
    {file = "pytokens-0.4.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a2c8952c537cb73a1a74369501a83b7f9d208c3cf92c41dd88a17814e68d48ce"},
    {file = "pytokens-0.4.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:5dbf56f3c748aed9310b310d5b8b14e2c96d3ad682ad5a943f381bdbbdddf753"},
    {file = "pytokens-0.4.0-cp313-cp313-win_amd64.whl", hash = "sha256:e131804513597f2dff2b18f9911d9b6276e21ef3699abeffc1c087c65a3d975e"},
    {file = "pytokens-0.4.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:0d7374c917197106d3c4761374718bc55ea2e9ac0fb94171588ef5840ee1f016"},
    {file = "pytokens-0.4.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0cd3fa1caf9e47a72ee134a29ca6b5bea84712724bba165d6628baa190c6ea5b"},
    {file = "pytokens-0.4.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9c6986576b7b07fe9791854caa5347923005a80b079d45b63b0be70d50cce5f1"},
    {file = "pytokens-0.4.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:9940f7c2e2f54fb1cb5fe17d0803c54da7a2bf62222704eb4217433664a186a7"},
    {file = "pytokens-0.4.0-cp314-cp314-win_amd64.whl", hash = "sha256:54691cf8f299e7efabcc25adb4ce715d3cef1491e1c930eaf555182f898ef66a"},
    {file = "pytokens-0.4.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:94ff5db97a0d3cd7248a5b07ba2167bd3edc1db92f76c6db00137bbaf068ddf8"},
    {file = "pytokens-0.4.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d0dd6261cd9cc95fae1227b1b6ebee023a5fd4a4b6330b071c73a516f5f59b63"},
    {file = "pytokens-0.4.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0cdca8159df407dbd669145af4171a0d967006e0be25f3b520896bc7068f02c4"},
    {file = "pytokens-0.4.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:4b5770abeb2a24347380a1164a558f0ebe06e98aedbd54c45f7929527a5fb26e"},
    {file = "pytokens-0.4.0-cp314-cp314t-win_amd64.whl", hash = "sha256:74500d72c561dad14c037a9e86a657afd63e277dd5a3bb7570932ab7a3b12551"},
    {file = "pytokens-0.4.0-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:e368e0749e4e9d86a6e08763310dc92bc69ad73d9b6db5243b30174c71a8a534"},
    {file = "pytokens-0.4.0-cp38-cp38-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:865cc65c75c8f2e9e0d8330338f649b12bfd9442561900ebaf58c596a72107d2"},
    {file = "pytokens-0.4.0-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:dbb9338663b3538f31c4ca7afe4f38d9b9b3a16a8be18a273a5704a1bc7a2367"},
    {file = "pytokens-0.4.0-cp38-cp38-musllinux_1_2_x86_64.whl", hash = "sha256:658f870523ac1a5f4733d7db61ce9af61a0c23b2aeea3d03d1800c93f760e15f"},
    {file = "pytokens-0.4.0-cp38-cp38-win_amd64.whl", hash = "sha256:d69a2491190a74e4b6f87f3b9dfce7a6873de3f3bf330d20083d374380becac0"},
    {file = "pytokens-0.4.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:8cd795191c4127fcb3d7b76d84006a07748c390226f47657869235092eedbc05"},
    {file = "pytokens-0.4.0-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ef2bcbddb73ac18599a86c8c549d5145130f2cd9d83dc2b5482fd8322b7806cd"},
    {file = "pytokens-0.4.0-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:06ac081c1187389762b58823d90d6339e6880ce0df912f71fb9022d81d7fd429"},
    {file = "pytokens-0.4.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:278129d54573efdc79e75c6082e73ebd19858e22a2e848359f93629323186ca6"},
    {file = "pytokens-0.4.0-cp39-cp39-win_amd64.whl", hash = "sha256:9380fb6d96fa5ab83ed606ebad27b6171930cc14a8a8d215f6adb187ba428690"},
    {file = "pytokens-0.4.0-py3-none-any.whl", hash = "sha256:0508d11b4de157ee12063901603be87fb0253e8f4cb9305eb168b1202ab92068"},
    {file = "pytokens-0.4.0.tar.gz", hash = "sha256:6b0b03e6ea7c9f9d47c5c61164b69ad30f4f0d70a5d9fe7eac4d19f24f77af2d"},
]

[package.extras]
dev = ["black", "build", "mypy", "pytest", "pytest-cov", "setuptools", "tox", "twine", "wheel"]

[[package]]
name = "pywin32"
version = "311"
description = "Python for Window Extensions"
optional = false
python-versions = "*"
groups = ["main", "dev"]
markers = "sys_platform == \"win32\""
files = [
    {file = "pywin32-311-cp310-cp310-win32.whl", hash = "sha256:d03ff496d2a0cd4a5893504789d4a15399133fe82517455e78bad62efbb7f0a3"},
    {file = "pywin32-311-cp310-cp310-win_amd64.whl", hash = "sha256:797c2772017851984b97180b0bebe4b620bb86328e8a884bb626156295a63b3b"},
    {file = "pywin32-311-cp310-cp310-win_arm64.whl", hash = "sha256:0502d1facf1fed4839a9a51ccbcc63d952cf318f78ffc00a7e78528ac27d7a2b"},
    {file = "pywin32-311-cp311-cp311-win32.whl", hash = "sha256:184eb5e436dea364dcd3d2316d577d625c0351bf237c4e9a5fabbcfa5a58b151"},
    {file = "pywin32-311-cp311-cp311-win_amd64.whl", hash = "sha256:3ce80b34b22b17ccbd937a6e78e7225d80c52f5ab9940fe0506a1a16f3dab503"},
    {file = "pywin32-311-cp311-cp311-win_arm64.whl", hash = "sha256:a733f1388e1a842abb67ffa8e7aad0e70ac519e09b0f6a784e65a136ec7cefd2"},
    {file = "pywin32-311-cp312-cp312-win32.whl", hash = "sha256:750ec6e621af2b948540032557b10a2d43b0cee2ae9758c54154d711cc852d31"},
    {file = "pywin32-311-cp312-cp312-win_amd64.whl", hash = "sha256:b8c095edad5c211ff31c05223658e71bf7116daa0ecf3ad85f3201ea3190d067"},
    {file = "pywin32-311-cp312-cp312-win_arm64.whl", hash = "sha256:e286f46a9a39c4a18b319c28f59b61de793654af2f395c102b4f819e584b5852"},
    {file = "pywin32-311-cp313-cp313-win32.whl", hash = "sha256:f95ba5a847cba10dd8c4d8fefa9f2a6cf283b8b88ed6178fa8a6c1ab16054d0d"},
    {file = "pywin32-311-cp313-cp313-win_amd64.whl", hash = "sha256:718a38f7e5b058e76aee1c56ddd06908116d35147e133427e59a3983f703a20d"},
    {file = "pywin32-311-cp313-cp313-win_arm64.whl", hash = "sha256:7b4075d959648406202d92a2310cb990fea19b535c7f4a78d3f5e10b926eeb8a"},
    {file = "pywin32-311-cp314-cp314-win32.whl", hash = "sha256:b7a2c10b93f8986666d0c803ee19b5990885872a7de910fc460f9b0c2fbf92ee"},
    {file = "pywin32-311-cp314-cp314-win_amd64.whl", hash = "sha256:3aca44c046bd2ed8c90de9cb8427f581c479e594e99b5c0bb19b29c10fd6cb87"},
    {file = "pywin32-311-cp314-cp314-win_arm64.whl", hash = "sha256:a508e2d9025764a8270f93111a970e1d0fbfc33f4153b388bb649b7eec4f9b42"},
    {file = "pywin32-311-cp38-cp38-win32.whl", hash = "sha256:6c6f2969607b5023b0d9ce2541f8d2cbb01c4f46bc87456017cf63b73f1e2d8c"},
    {file = "pywin32-311-cp38-cp38-win_amd64.whl", hash = "sha256:c8015b09fb9a5e188f83b7b04de91ddca4658cee2ae6f3bc483f0b21a77ef6cd"},
    {file = "pywin32-311-cp39-cp39-win32.whl", hash = "sha256:aba8f82d551a942cb20d4a83413ccbac30790b50efb89a75e4f586ac0bb8056b"},
    {file = "pywin32-311-cp39-cp39-win_amd64.whl", hash = "sha256:e0c4cfb0621281fe40387df582097fd796e80430597cb9944f0ae70447bacd91"},
    {file = "pywin32-311-cp39-cp39-win_arm64.whl", hash = "sha256:62ea666235135fee79bb154e695f3ff67370afefd71bd7fea7512fc70ef31e3d"},
]

[[package]]
name = "tomli"
version = "2.4.0"
description = "A lil' TOML parser"
optional = false
python-versions = ">=3.8"
groups = ["main", "dev"]
markers = "python_version == \"3.10\""
files = [
    {file = "tomli-2.4.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:b5ef256a3fd497d4973c11bf142e9ed78b150d36f5773f1ca6088c230ffc5867"},
    {file = "tomli-2.4.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:5572e41282d5268eb09a697c89a7bee84fae66511f87533a6f88bd2f7b652da9"},
    {file = "tomli-2.4.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:551e321c6ba03b55676970b47cb1b73f14a0a4dce6a3e1a9458fd6d921d72e95"},
    {file = "tomli-2.4.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5e3f639a7a8f10069d0e15408c0b96a2a828cfdec6fca05296ebcdcc28ca7c76"},
    {file = "tomli-2.4.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:1b168f2731796b045128c45982d3a4874057626da0e2ef1fdd722848b741361d"},
    {file = "tomli-2.4.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:133e93646ec4300d651839d382d63edff11d8978be23da4cc106f5a18b7d0576"},
    {file = "tomli-2.4.0-cp311-cp311-win32.whl", hash = "sha256:b6c78bdf37764092d369722d9946cb65b8767bfa4110f902a1b2542d8d173c8a"},
    {file = "tomli-2.4.0-cp311-cp311-win_amd64.whl", hash = "sha256:d3d1654e11d724760cdb37a3d7691f0be9db5fbdaef59c9f532aabf87006dbaa"},
    {file = "tomli-2.4.0-cp311-cp311-win_arm64.whl", hash = "sha256:cae9c19ed12d4e8f3ebf46d1a75090e4c0dc16271c5bce1c833ac168f08fb614"},
    {file = "tomli-2.4.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:920b1de295e72887bafa3ad9f7a792f811847d57ea6b1215154030cf131f16b1"},
    {file = "tomli-2.4.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:7d6d9a4aee98fac3eab4952ad1d73aee87359452d1c086b5ceb43ed02ddb16b8"},
    {file = "tomli-2.4.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:36b9d05b51e65b254ea6c2585b59d2c4cb91c8a3d91d0ed0f17591a29aaea54a"},
    {file = "tomli-2.4.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1c8a885b370751837c029ef9bc014f27d80840e48bac415f3412e6593bbc18c1"},
    {file = "tomli-2.4.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:8768715ffc41f0008abe25d808c20c3d990f42b6e2e58305d5da280ae7d1fa3b"},
    {file = "tomli-2.4.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:7b438885858efd5be02a9a133caf5812b8776ee0c969fea02c45e8e3f296ba51"},
    {file = "tomli-2.4.0-cp312-cp312-win32.whl", hash = "sha256:0408e3de5ec77cc7f81960c362543cbbd91ef883e3138e81b729fc3eea5b9729"},
    {file = "tomli-2.4.0-cp312-cp312-win_amd64.whl", hash = "sha256:685306e2cc7da35be4ee914fd34ab801a6acacb061b6a7abca922aaf9ad368da"},
    {file = "tomli-2.4.0-cp312-cp312-win_arm64.whl", hash = "sha256:5aa48d7c2356055feef06a43611fc401a07337d5b006be13a30f6c58f869e3c3"},
    {file = "tomli-2.4.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:84d081fbc252d1b6a982e1870660e7330fb8f90f676f6e78b052ad4e64714bf0"},
    {file = "tomli-2.4.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:9a08144fa4cba33db5255f9b74f0b89888622109bd2776148f2597447f92a94e"},
    {file = "tomli-2.4.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c73add4bb52a206fd0c0723432db123c0c75c280cbd67174dd9d2db228ebb1b4"},
    {file = "tomli-2.4.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1fb2945cbe303b1419e2706e711b7113da57b7db31ee378d08712d678a34e51e"},
    {file = "tomli-2.4.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:bbb1b10aa643d973366dc2cb1ad94f99c1726a02343d43cbc011edbfac579e7c"},
    {file = "tomli-2.4.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:4cbcb367d44a1f0c2be408758b43e1ffb5308abe0ea222897d6bfc8e8281ef2f"},
    {file = "tomli-2.4.0-cp313-cp313-win32.whl", hash = "sha256:7d49c66a7d5e56ac959cb6fc583aff0651094ec071ba9ad43df785abc2320d86"},
    {file = "tomli-2.4.0-cp313-cp313-win_amd64.whl", hash = "sha256:3cf226acb51d8f1c394c1b310e0e0e61fecdd7adcb78d01e294ac297dd2e7f87"},
    {file = "tomli-2.4.0-cp313-cp313-win_arm64.whl", hash = "sha256:d20b797a5c1ad80c516e41bc1fb0443ddb5006e9aaa7bda2d71978346aeb9132"},
    {file = "tomli-2.4.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:26ab906a1eb794cd4e103691daa23d95c6919cc2fa9160000ac02370cc9dd3f6"},
    {file = "tomli-2.4.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:20cedb4ee43278bc4f2fee6cb50daec836959aadaf948db5172e776dd3d993fc"},
    {file = "tomli-2.4.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:39b0b5d1b6dd03684b3fb276407ebed7090bbec989fa55838c98560c01113b66"},
    {file = "tomli-2.4.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a26d7ff68dfdb9f87a016ecfd1e1c2bacbe3108f4e0f8bcd2228ef9a766c787d"},
    {file = "tomli-2.4.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:20ffd184fb1df76a66e34bd1b36b4a4641bd2b82954befa32fe8163e79f1a702"},
    {file = "tomli-2.4.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:75c2f8bbddf170e8effc98f5e9084a8751f8174ea6ccf4fca5398436e0320bc8"},
    {file = "tomli-2.4.0-cp314-cp314-win32.whl", hash = "sha256:31d556d079d72db7c584c0627ff3a24c5d3fb4f730221d3444f3efb1b2514776"},
    {file = "tomli-2.4.0-cp314-cp314-win_amd64.whl", hash = "sha256:43e685b9b2341681907759cf3a04e14d7104b3580f808cfde1dfdb60ada85475"},
    {file = "tomli-2.4.0-cp314-cp314-win_arm64.whl", hash = "sha256:3d895d56bd3f82ddd6faaff993c275efc2ff38e52322ea264122d72729dca2b2"},
    {file = "tomli-2.4.0-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:5b5807f3999fb66776dbce568cc9a828544244a8eb84b84b9bafc080c99597b9"},
    {file = "tomli-2.4.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:c084ad935abe686bd9c898e62a02a19abfc9760b5a79bc29644463eaf2840cb0"},
    {file = "tomli-2.4.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0f2e3955efea4d1cfbcb87bc321e00dc08d2bcb737fd1d5e398af111d86db5df"},
    {file = "tomli-2.4.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0e0fe8a0b8312acf3a88077a0802565cb09ee34107813bba1c7cd591fa6cfc8d"},
    {file = "tomli-2.4.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:413540dce94673591859c4c6f794dfeaa845e98bf35d72ed59636f869ef9f86f"},
    {file = "tomli-2.4.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:0dc56fef0e2c1c470aeac5b6ca8cc7b640bb93e92d9803ddaf9ea03e198f5b0b"},
    {file = "tomli-2.4.0-cp314-cp314t-win32.whl", hash = "sha256:d878f2a6707cc9d53a1be1414bbb419e629c3d6e67f69230217bb663e76b5087"},
    {file = "tomli-2.4.0-cp314-cp314t-win_amd64.whl", hash = "sha256:2add28aacc7425117ff6364fe9e06a183bb0251b03f986df0e78e974047571fd"},
    {file = "tomli-2.4.0-cp314-cp314t-win_arm64.whl", hash = "sha256:2b1e3b80e1d5e52e40e9b924ec43d81570f0e7d09d11081b797bc4692765a3d4"},
    {file = "tomli-2.4.0-py3-none-any.whl", hash = "sha256:1f776e7d669ebceb01dee46484485f43a4048746235e683bcdffacdf1fb4785a"},
    {file = "tomli-2.4.0.tar.gz", hash = "sha256:aa89c3f6c277dd275d8e243ad24f3b5e701491a860d5121f2cdd399fbb31fc9c"},
]

[[package]]
name = "traceloggingdynamic"
version = "1.0.1"
description = "Generates Event Tracing for Windows events using TraceLogging"
optional = false
python-versions = ">=3.6"
groups = ["main", "dev"]
markers = "sys_platform == \"win32\""
files = [
    {file = "traceloggingdynamic-1.0.1-py3-none-any.whl", hash = "sha256:0e19da491a8960725b3622366487ae35f49d8f595bb2e4e5ce1795eb5928db7c"},
    {file = "traceloggingdynamic-1.0.1.tar.gz", hash = "sha256:d9dd4b291dd04c15e34181eed06f73fdf4ffa7b1f895b78217163def48ab1a52"},
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
description = "Backported and Experimental Type Hints for Python 3.9+"
optional = false
python-versions = ">=3.9"
groups = ["main", "dev"]
files = [
    {file = "typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548"},
    {file = "typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466"},
]

[metadata]
lock-version = "2.1"
python-versions = "^3.10"
content-hash = "5f5f8072a62156f3aa6d1b7441a715f6d33b56a8c8b5a8d68c85dbc3eabc0d9e"
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/sdk/poetry.toml sha256=95a373a5c86a875e563cd1d8765d6c10b428a8bfd3621810e5cac4c3132d6f71 bytes=841 -->
## FILE: packages/sdk/poetry.toml

- repository: `ni/measurement-plugin-python`
- source_path: `packages/sdk/poetry.toml`
- sha256: `95a373a5c86a875e563cd1d8765d6c10b428a8bfd3621810e5cac4c3132d6f71`
- bytes: 841

````toml
[virtualenvs]
in-project = true

[solver]
# Set min-release-age to 2 weeks, same as in https://github.com/ni/python-renovate-config
min-release-age = 14
min-release-age-exclude = [
    "hightime",
    "ni-grpc-extensions",
    "ni-grpcdevice-v1-proto",
    "ni-measurement-plugin-sdk-generator",
    "ni-measurement-plugin-sdk-service",
    "ni-measurementlink-discovery-v1-client",
    "ni-measurementlink-discovery-v1-proto",
    "ni-measurementlink-measurement-v1-proto",
    "ni-measurementlink-measurement-v2-proto",
    "ni-measurementlink-pinmap-v1-client",
    "ni-measurementlink-pinmap-v1-proto",
    "ni-measurementlink-proto",
    "ni-measurementlink-sessionmanagement-v1-client",
    "ni-measurementlink-sessionmanagement-v1-proto",
    "ni-protobuf-types",
    "ni-python-styleguide",
    "nitypes",
]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/sdk/pyproject.toml sha256=760db90cf287bd2b38c36094eb6dfc356a8a86895c33019d0ae4210555d0848f bytes=1316 -->
## FILE: packages/sdk/pyproject.toml

- repository: `ni/measurement-plugin-python`
- source_path: `packages/sdk/pyproject.toml`
- sha256: `760db90cf287bd2b38c36094eb6dfc356a8a86895c33019d0ae4210555d0848f`
- bytes: 1316

````toml
[tool.poetry]
name = "ni_measurement_plugin_sdk"
version = "3.2.0.dev0"
description = "Measurement Plug-In SDK for Python"
authors = ["NI <opensource@ni.com>"]
readme = "README.md"
repository = "https://github.com/ni/measurement-plugin-python/"
license = "MIT"
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: Manufacturing",
    "Intended Audience :: Science/Research",
    "Operating System :: Microsoft :: Windows",
    # Poetry automatically adds classifiers for the license and the supported Python versions.
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Scientific/Engineering",
    "Topic :: System :: Hardware",
]

[tool.poetry.dependencies]
python = "^3.10"
ni-measurement-plugin-sdk-service = "*"
ni-measurement-plugin-sdk-generator = "*"

[tool.poetry.group.dev.dependencies]
# During development, use file paths to reference the latest source for packages
# in the same Git repository.
ni-measurement-plugin-sdk-service = {path = "../../packages/service", develop = true}
ni-measurement-plugin-sdk-generator = {path = "../../packages/generator", develop = true}

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/sdk/README.md sha256=2bcda5b1da1246d5212ce84d618a3c30a43d32cc33c50102a1527326188142fa bytes=858 -->
## FILE: packages/sdk/README.md

- repository: `ni/measurement-plugin-python`
- source_path: `packages/sdk/README.md`
- sha256: `2bcda5b1da1246d5212ce84d618a3c30a43d32cc33c50102a1527326188142fa`
- bytes: 858

````markdown
# Measurement Plug-In SDK for Python
---

## Introduction

Measurement Plug-In SDK for Python (`ni-measurement-plugin-sdk`) is a
tool for generating and writing reusable measurement plug-ins using gRPC services.

The purpose of this package is as a meta-package that depends on `ni-measurement-plugin-sdk-generator`
and `ni-measurement-plugin-sdk-service` so as to easily install all the things needed for the
Measurement Plug-In SDK.

For installation and usage, see [Measurement Plug-In SDK Service for Python (`ni-measurement-plugin-sdk-service`)](https://pypi.org/project/ni-measurement-plugin-sdk-service/).

---

## Dependencies

- [Python >= 3.9](https://www.python.org/downloads/release/python-3913/)
- [mako >= 1.2.1, < 2.x](https://pypi.org/project/Mako/1.2.1/)
- [click >= 8.1.3](https://pypi.org/project/click/8.1.3/)

---
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/_docs_source/conf.py sha256=66aa53ae795473ae17d988539f06f6da6af79184a3008e416c1d5c182f8f9dc6 bytes=5459 -->
## FILE: packages/service/_docs_source/conf.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/_docs_source/conf.py`
- sha256: `66aa53ae795473ae17d988539f06f6da6af79184a3008e416c1d5c182f8f9dc6`
- bytes: 5459

````python
"""Sphinx Configuration File."""

import pathlib

import autoapi.extension
import toml

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "autoapi.extension",
    "m2r2",
    "sphinx_click",
    "sphinx.ext.autodoc",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

root_path = pathlib.Path(__file__).parent.parent
pyproj_file = root_path / "pyproject.toml"
proj_config = toml.loads(pyproj_file.read_text())


project = proj_config["tool"]["poetry"]["name"]
company = "National Instruments"
copyright = f"2022-%Y, {company}"


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
version = proj_config["tool"]["poetry"]["version"]
release = ".".join(version.split(".")[:2])
description = proj_config["tool"]["poetry"]["description"]


htmlhelp_basename = f"{project}doc"


# tell autoapi to doc the public options
autoapi_options = list(autoapi.extension._DEFAULT_OPTIONS)
autoapi_options.remove("private-members")  # note: remove this to include "_" members in docs
autoapi_dirs = [root_path / "ni_measurement_plugin_sdk_service"]
autoapi_type = "python"
autodoc_typehints = "description"


# WARNING: more than one target found for cross-reference 'MeasurementInfo':
# ni_measurement_plugin_sdk_service.MeasurementInfo,
# ni_measurement_plugin_sdk_service.measurement.info.MeasurementInfo
#
# TODO: figure out how to make :canonical: work with autoapi
def skip_aliases(app, what, name, obj, skip, options):
    """Skip documentation for classes that are exported from multiple modules."""
    # For names that are defined in a public sub-module and aliased into a
    # public package, hide the alias.
    if name in [
        "ni_measurement_plugin_sdk_service.DataType",
        "ni_measurement_plugin_sdk_service.MeasurementInfo",
        "ni_measurement_plugin_sdk_service.ServiceInfo",
        "ni_measurement_plugin_sdk_service.MeasurementService",
    ]:
        skip = True

    # For names that are defined in a private sub-module and aliased into a
    # public package, hide the definition.
    if name.startswith("ni_measurement_plugin_sdk_service.session_management._constants."):
        skip = True

    return skip


def setup(sphinx):
    """Sphinx setup callback."""
    sphinx.connect("autoapi-skip-member", skip_aliases)


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


intersphinx_mapping = {
    "grpc": ("https://grpc.github.io/grpc/python/", None),
    # Work around https://github.com/ni/ni-apis-python/issues/337 by using latest instead of stable
    "ni_grpc_extensions": ("https://ni-grpc-extensions.readthedocs.io/en/latest/", None),
    "ni.measurementlink.discovery.v1.client": (
        "https://nimeasurementlinkdiscoveryv1client.readthedocs.io/en/latest/",
        None,
    ),
    "ni.measurementlink.discovery.v1.proto": (
        "https://nimeasurementlinkdiscoveryv1proto.readthedocs.io/en/latest/",
        None,
    ),
    "ni.measurementlink.measurement.v1.proto": (
        "https://nimeasurementlinkmeasurementv1proto.readthedocs.io/en/latest/",
        None,
    ),
    "ni.measurementlink.measurement.v2.proto": (
        "https://nimeasurementlinkmeasurementv2proto.readthedocs.io/en/latest/",
        None,
    ),
    "ni.measurementlink.pinmap.v1.client": (
        "https://nimeasurementlinkpinmapv1client.readthedocs.io/en/latest/",
        None,
    ),
    "ni.measurementlink.pinmap.v1.proto": (
        "https://nimeasurementlinkpinmapv1proto.readthedocs.io/en/latest/",
        None,
    ),
    "ni.measurementlink.sessionmanagement.v1.client": (
        "https://nimeasurementlinksessionmanagementclient.readthedocs.io/en/latest/",
        None,
    ),
    "ni.measurementlink.sessionmanagement.v1.proto": (
        "https://nimeasurementlinksessionmanagementv1proto.readthedocs.io/en/latest/",
        None,
    ),
    "ni.protobuf.types": ("https://niprotobuftypes.readthedocs.io/en/latest/", None),
    "nidaqmx": ("https://nidaqmx-python.readthedocs.io/en/stable/", None),
    "nidcpower": ("https://nidcpower.readthedocs.io/en/stable/", None),
    "nidigital": ("https://nidigital.readthedocs.io/en/stable/", None),
    "nidmm": ("https://nidmm.readthedocs.io/en/stable/", None),
    "nifgen": ("https://nifgen.readthedocs.io/en/stable/", None),
    "niscope": ("https://niscope.readthedocs.io/en/stable/", None),
    "niswitch": ("https://niswitch.readthedocs.io/en/stable/", None),
    "protobuf": ("https://googleapis.dev/python/protobuf/latest/", None),
    "python": ("https://docs.python.org/3", None),
}


# -- Options for HTML output ----------------------------------------------


# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation_depth": -1,
}

# Napoleon settings
napoleon_numpy_docstring = False
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/_docs_source/index.rst sha256=312a11af797fd97250efcdd888756ff34f82175bb1829d7147e94d1878a61e57 bytes=185 -->
## FILE: packages/service/_docs_source/index.rst

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/_docs_source/index.rst`
- sha256: `312a11af797fd97250efcdd888756ff34f82175bb1829d7147e94d1878a61e57`
- bytes: 185

````rst
NI Measurement Plug-In SDK
--------------------------
.. toctree::
   :maxdepth: 3

   autoapi/index

Indices and tables
------------------
* :ref:`modindex`
* :ref:`search`
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/__init__.py sha256=18984f6847ac1976ec6ad61d0f0d023331db36e538e80e0b39eab6e09a18a164 bytes=592 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/__init__.py`
- sha256: `18984f6847ac1976ec6ad61d0f0d023331db36e538e80e0b39eab6e09a18a164`
- bytes: 592

````python
"""Measurement Plug-In Support for Python."""

import logging

from ni.measurementlink.discovery.v1.client import ServiceInfo

from ni_measurement_plugin_sdk_service import session_management
from ni_measurement_plugin_sdk_service.measurement.info import DataType, MeasurementInfo
from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService

__all__ = [
    "session_management",
    "DataType",
    "MeasurementInfo",
    "ServiceInfo",
    "MeasurementService",
]

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_annotations.py sha256=8efbafbcdfc8bb5ffa979fd36dbcdb275ebf15a5810d4d176f3286a8d0609b0d bytes=192 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/_annotations.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/_annotations.py`
- sha256: `8efbafbcdfc8bb5ffa979fd36dbcdb275ebf15a5810d4d176f3286a8d0609b0d`
- bytes: 192

````python
"""Constants for annotations."""

ENUM_VALUES_KEY = "ni/enum.values"
TYPE_SPECIALIZATION_KEY = "ni/type_specialization"
SERVICE_PROGRAMMINGLANGUAGE_KEY = "ni/service.programminglanguage"
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_configuration.py sha256=1d430f1273ec4d71bfa2e8acf642df946d40b1590dd65574dc15e43023140136 bytes=3946 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/_configuration.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/_configuration.py`
- sha256: `1d430f1273ec4d71bfa2e8acf642df946d40b1590dd65574dc15e43023140136`
- bytes: 3946

````python
"""Measurement plug-in configuration options."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any, Callable, NamedTuple, TypeVar

from decouple import AutoConfig, Undefined, undefined

from ni_measurement_plugin_sdk_service._dotenvpath import get_dotenv_search_path

if TYPE_CHECKING:
    if sys.version_info >= (3, 11):
        from typing import Self
    else:
        from typing_extensions import Self


_PREFIX = "MEASUREMENT_PLUGIN"

# Work around decouple's lack of type hints.
_T = TypeVar("_T")

if TYPE_CHECKING:

    def _config(
        option: str,
        default: _T | Undefined = undefined,
        cast: Callable[[str], _T] | Undefined = undefined,
    ) -> _T: ...

else:
    _config = AutoConfig(str(get_dotenv_search_path()))


# ----------------------------------------------------------------------
# NI Modular Instrument Driver Options
# ----------------------------------------------------------------------
class MIDriverOptions(NamedTuple):
    """Modular instrument driver options."""

    driver_name: str
    """The driver name."""

    simulate: bool = False
    """Specifies whether to simulate session operations."""

    board_type: str = ""
    """The simulated board type (bus)."""

    model: str = ""
    """The simulated instrument model."""

    def update_from_config(self) -> Self:
        """Read options from the configuration file and return a new options object."""
        prefix = f"{_PREFIX}_{self.driver_name.upper()}"
        return self._replace(
            simulate=_config(f"{prefix}_SIMULATE", default=self.simulate, cast=bool),
            board_type=_config(f"{prefix}_BOARD_TYPE", default=self.board_type),
            model=_config(f"{prefix}_MODEL", default=self.model),
        )

    def to_dict(self) -> dict[str, Any]:
        """Convert options to a dict to pass to nimi-python."""
        options: dict[str, Any] = {}
        if self.simulate:
            options["simulate"] = True
        if self.board_type or self.model:
            options["driver_setup"] = {}
            if self.board_type:
                options["driver_setup"]["BoardType"] = self.board_type
            if self.model:
                options["driver_setup"]["Model"] = self.model
        return options


class NISwitchOptions(NamedTuple):
    """NI-SWITCH driver options."""

    driver_name: str
    """The driver name."""

    simulate: bool = False
    """Specifies whether to simulate session operations."""

    topology: str = "Configured Topology"
    """The default topology."""

    def update_from_config(self) -> Self:
        """Read options from the configuration file and return a new options object."""
        prefix = f"{_PREFIX}_{self.driver_name.upper()}"
        return self._replace(
            simulate=_config(f"{prefix}_SIMULATE", default=self.simulate, cast=bool),
            topology=_config(f"{prefix}_TOPOLOGY", default=self.topology),
        )


NIDCPOWER_OPTIONS = MIDriverOptions("nidcpower").update_from_config()
NIDIGITAL_OPTIONS = MIDriverOptions("nidigital").update_from_config()
NIDMM_OPTIONS = MIDriverOptions("nidmm").update_from_config()
NIFGEN_OPTIONS = MIDriverOptions("nifgen").update_from_config()
NISCOPE_OPTIONS = MIDriverOptions("niscope").update_from_config()
NISWITCH_OPTIONS = NISwitchOptions("niswitch").update_from_config()
NISWITCH_MULTIPLEXER_OPTIONS = NISwitchOptions("niswitch_multiplexer").update_from_config()


# ----------------------------------------------------------------------
# NI gRPC Device Server Configuration
# ----------------------------------------------------------------------
USE_GRPC_DEVICE_SERVER: bool = _config(f"{_PREFIX}_USE_GRPC_DEVICE_SERVER", default=True, cast=bool)
GRPC_DEVICE_SERVER_ADDRESS: str = _config(f"{_PREFIX}_GRPC_DEVICE_SERVER_ADDRESS", default="")
````
