# NI OSS SOURCE SNAPSHOT: niveristand-python

<!--NI_OSS_SNAPSHOT repo=ni/niveristand-python commit=9ced536d3414f04a8b6b9315ce4c71b879d02a96 -->

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/TestModelAPI/TestModelAPI.nivssdf sha256=04545b01c3c92fa50a539ca46db341ae8eb7c2b3eb1ebb20c742c9ebb7073bae bytes=118698 -->
## FILE: tests/testutilities/legacy_files/TestModelAPI/TestModelAPI.nivssdf

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/TestModelAPI/TestModelAPI.nivssdf`
- sha256: `04545b01c3c92fa50a539ca46db341ae8eb7c2b3eb1ebb20c742c9ebb7073bae`
- bytes: 118698

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2013" Minor="0" Fix="0" Build="1" />
	<Content>Definition</Content>
	<Root Name="TestModelAPI" TypeGUID="03D3BA22-1485-13A6-56BD17DA950CCD00">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>TestModelAPI</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.1</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3489580954.2815609</Double>
			</Property>
		</Properties>
		<Errors />
		<TargetSections Name="Targets" TypeGUID="eb379619-68d7-4d81-be90-c0bc511cdc10">
			<Description />
			<Properties />
			<Errors />
			<Target Name="Controller" TypeGUID="775504BB-1485-13A6-56755DBF2C326980">
				<Description />
				<Properties>
					<Property Name="OS">
						<String>PharLap</String>
					</Property>
					<Property Name="IP Address">
						<String />
					</Property>
					<Property Name="Control Loop Processor">
						<I32>-2</I32>
					</Property>
					<Property Name="Secondary Control Loop Processor">
						<I32>-2</I32>
					</Property>
					<Property Name="Stream Rate">
						<I32>1</I32>
					</Property>
					<Property Name="DIO Rate">
						<Double>100</Double>
					</Property>
					<Property Name="Streamed Channels">
						<I32>512</I32>
					</Property>
					<Property Name="Filter DAQ Errors">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Filter Watchdog Errors">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Engine Rate">
						<Double>100</Double>
					</Property>
					<Property Name="TL timeout">
						<Double>120</Double>
					</Property>
					<Property Name="daq timeout">
						<U32>1000</U32>
					</Property>
					<Property Name="TL sleep time">
						<U32>0</U32>
					</Property>
					<Property Name="HS Port">
						<I32>2040</I32>
					</Property>
					<Property Name="LS Port">
						<I32>2050</I32>
					</Property>
					<Property Name="HS Port Timeout">
						<I32>1000</I32>
					</Property>
					<Property Name="LS Port Timeout">
						<I32>1000</I32>
					</Property>
					<Property Name="Deployment Group">
						<I32>0</I32>
					</Property>
					<Property Name="Control Rate">
						<Double>1</Double>
					</Property>
					<Property Name="Input Configuration">
						<U32>0</U32>
					</Property>
					<Property Name="ts">
						<U32>0</U32>
					</Property>
					<Property Name="Warmup Time [ms]">
						<U32>2000</U32>
					</Property>
					<Property Name="Data Rate">
						<Double>15</Double>
					</Property>
					<Property Name="FPGAScanInterfaceMode">
						<U16>0</U16>
					</Property>
				</Properties>
				<Errors />
				<Section Name="Hardware" TypeGUID="775504AB-1485-13A6-560018C1F4E3EEE1">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Chassis" TypeGUID="03D3BACD-1485-13A6-56E99D97B7543BAF">
						<Description />
						<Properties>
							<Property Name="Master type">
								<U32>1</U32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Timing and Sync" TypeGUID="03D3BAED-1485-13A6-56E20B50F6E06D94">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="DAQ" TypeGUID="77550612-1485-13A6-56570AB5032158E9">
							<Description />
							<Properties />
							<Errors />
							<Section Name="Waveform Tasks" TypeGUID="1D6B8779-A957-42D1-B074-82153DB7FF44">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
						<Section Name="FPGA" TypeGUID="03D3B659-1485-13A6-5652D8A07328ECB7">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="NI-XNET" TypeGUID="6b693e6d-67b1-40b8-8108-4a4cc3147721">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
								</Property>
								<Property Name="Decimation">
									<I32>1</I32>
								</Property>
								<Property Name="Driver VI Exec Mode">
									<U32>1</U32>
								</Property>
							</Properties>
							<Errors />
							<Section Name="CAN" TypeGUID="6c5bb91f-0da7-407d-aefc-acbe49c768df">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="FlexRay" TypeGUID="e33fae90-03f1-4f76-b2f1-6eb8fcac2676">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="LIN" TypeGUID="c9c30728-42cb-4dc3-b054-b80e7a54e833">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
						<Section Name="Data Sharing" TypeGUID="d56f3ac1-7b2c-422c-9d11-fd9cc7abf2a5">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
					</Section>
				</Section>
				<Section Name="Custom Devices" TypeGUID="03D3BB79-1485-13A6-5605EB7AFD7405AC">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Simulation Models" TypeGUID="03D3B937-1485-13A6-5600F2871E269F9A">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Models" TypeGUID="03D3B976-1485-13A6-5604255F981010CE">
						<Description />
						<Properties />
						<Errors />
						<Section Name="Custom_current" TypeGUID="03D3B9C4-1485-13A6-561FC9BB21813875">
							<Description />
							<Properties>
								<Property Name="Base Rate">
									<Double>10000</Double>
								</Property>
								<Property Name="DLL Size">
									<I32>16896</I32>
								</Property>
								<Property Name="DLL Timestamp">
									<Double>3489152502.2421064</Double>
								</Property>
								<Property Name="Decimation">
									<I32>1</I32>
								</Property>
								<Property Name="Import Definition ID">
									<I32>0</I32>
								</Property>
								<Property Name="ID">
									<I32>0</I32>
								</Property>
								<Property Name="Model Timestamp">
									<Double>0</Double>
								</Property>
								<Property Name="Processor">
									<I32>-2</I32>
								</Property>
								<Property Name="Show Unnamed Signals">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="User Rate">
									<Double>10000</Double>
								</Property>
								<Property Name="visible">
									<U32>0</U32>
								</Property>
								<Property Name="blocks only">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Segment Vectors">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="MD5">
									<String>2d525d49aaf9c9b5118d3fc243707a03</String>
								</Property>
								<Property Name="NIVeriStandServer Port">
									<U32>6012</U32>
								</Property>
								<Property Name="DLL Path">
									<DependentFile Type="To Common Doc Dir" Path="AutoTestProjects\Test Models\Compiled\Custom\autobuild\custom.dll">
										<Version />
										<ForceDownload>false</ForceDownload>
										<RTDestination>C:\ni-rt\NIVeriStand\Models\custom.dll</RTDestination>
										<SupportedTarget>PharLap &amp; Windows</SupportedTarget>
										<MD5>2d525d49aaf9c9b5118d3fc243707a03</MD5>
									</DependentFile>
								</Property>
								<Property Name="GlobalParameterScopes">
									<I32>0</I32>
								</Property>
							</Properties>
							<Errors />
							<Section Name="Execution" TypeGUID="03D3BA9F-1485-13A6-56E3D5196780015F">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Model Command" TypeGUID="03D3BABE-1485-13A6-56C34B877844B2C1" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description>0: Start
1: Pause
2: Reset
3: Save
4: Restore</Description>
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Model Time" TypeGUID="03D3BAAE-1485-13A6-5606A77AB57A7FC9" RowDim="1" ColDim="1" Units="sec" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Model Status" TypeGUID="03D3BB6A-1485-13A6-5643A7AFDA3A2658" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description>0: Running
1: Paused
2: Resetting
3: Idle
4: Stopped
5: Restoring
6: Saving</Description>
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Time Step Duration" TypeGUID="8e7cc8ad-0a9f-4b63-b5f0-59c025358253" RowDim="1" ColDim="1" Units="usec" BitFields="1">
									<Description>The duration in microseconds of the last model time step.</Description>
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Inports" TypeGUID="03D3B9E3-1485-13A6-56035B19B2245EB3">
								<Description />
								<Properties />
								<Errors />
								<Section Name="Inport_10x1" TypeGUID="cbfdde93-6581-4b7c-83b8-e88484f25b2e">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="Inport_10x1(1,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(2,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(3,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(4,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(5,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(6,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(7,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(8,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(9,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(10,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
								</Section>
								<Section Name="Inport_10x5" TypeGUID="cbfdde93-6581-4b7c-83b8-e88484f25b2e">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="Inport_10x5(1,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(1,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(1,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(1,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(1,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
								</Section>
								<Channel Name="Inport_1x1" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>Inport_1x1</String>
										</Property>
										<Property Name="Index">
											<I32>0</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Outports" TypeGUID="03D3B9F3-1485-13A6-5698C14838D6AA3C">
								<Description />
								<Properties />
								<Errors />
								<Section Name="Outport_10x1" TypeGUID="cbfdde93-6581-4b7c-83b8-e88484f25b2e">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="Outport_10x1(1,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(2,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(3,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(4,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(5,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(6,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(7,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(8,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(9,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(10,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
								</Section>
								<Section Name="Outport_10x5" TypeGUID="cbfdde93-6581-4b7c-83b8-e88484f25b2e">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="Outport_10x5(1,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(1,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(1,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(1,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(1,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
								</Section>
								<Channel Name="Outport_1x1" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>Outport_1x1</String>
										</Property>
										<Property Name="Index">
											<I32>3</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Parameters" TypeGUID="03D3BB0C-1485-13A6-56E10CEFF755E7D3">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Gain_1x1" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>test/Gain_1x1</String>
										</Property>
										<Property Name="Expression">
											<String>Gain_1x1</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>0</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>1</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Offset_1x1" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>test/Offset_1x1</String>
										</Property>
										<Property Name="Expression">
											<String>Offset_1x1</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>1</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>1</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Gain_10x1" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="10" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>test/Gain_10x1</String>
										</Property>
										<Property Name="Expression">
											<String>Gain_10x1</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>2</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Offset_10x1" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="10" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>test/Offset_10x1</String>
										</Property>
										<Property Name="Expression">
											<String>Offset_10x1</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>3</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Gain_10x5" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="10" ColDim="5" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>test/Gain_10x5</String>
										</Property>
										<Property Name="Expression">
											<String>Gain_10x5</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>4</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Offset_10x5" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="10" ColDim="5" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>test/Offset_10x5</String>
										</Property>
										<Property Name="Expression">
											<String>Offset_10x5</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>5</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Signals" TypeGUID="03D3BA31-1485-13A6-567CA69E9D2E71D5">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
					</Section>
					<Section Name="Execution Order" TypeGUID="03D3B966-1485-13A6-569CFF8A449BF90A">
						<Description />
						<Properties />
						<Errors />
					</Section>
				</Section>
				<Section Name="User Channels" TypeGUID="03D3B6B7-1485-13A6-567BE1E1E0DF999A">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Calculated Channels" TypeGUID="03D3B714-1485-13A6-56031C5F1CCB78A9">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Stimulus" TypeGUID="03D3B7FF-1485-13A6-56B2328F9511AC8B">
					<Description />
					<Properties>
						<Property Name="Max Steps">
							<I32>128</I32>
						</Property>
						<Property Name="Max Gen Maps">
							<I32>256</I32>
						</Property>
						<Property Name="Aux Buffer Size">
							<I32>10000</I32>
						</Property>
						<Property Name="Analysis Buffer Size">
							<I32>10000</I32>
						</Property>
						<Property Name="Analysis Result Size">
							<I32>5000</I32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Alarms" TypeGUID="03D3B782-1485-13A6-56F58B35B6CBA484">
					<Description />
					<Properties>
						<Property Name="Alarm Rate">
							<I32>1</I32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Procedures" TypeGUID="03D3B7B1-1485-13A6-56649C7783203F22">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="XNET Databases" TypeGUID="def5630b-577f-4ae9-9682-5f8ee445ee21">
					<Description />
					<Properties>
						<Property Name="CD Status">
							<U32>2</U32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="System Channels" TypeGUID="03D3B753-1485-13A6-56B10ED0820CF410">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="Actual Loop Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Hz" BitFields="1">
						<Description>The execution rate of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Index" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The decimation of the Data Processing Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Time" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>The relative system time of the VeriStand Engine according to the iteration count and Delta T of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="DAQ Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Error Code" BitFields="3">
						<Description>The last reported error code from a DAQmx function call. The value zero indicates no error has occurred.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Delta T" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>The period in seconds of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Compiler Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 1" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 2" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 3" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Resume Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 4" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 5" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 6" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="RT Engine Build" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>A value representing the build number of the NI VeriStand Engine</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Loop Duration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The duration of the Primary Control Loop in nanoseconds</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Loop Duration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The duration of the Data Processing Loop in nanoseconds</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Command" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="3">
						<Description>Internally commands the RT system with the following numeric values:

0: None
1: Restart System
2: Reset System
3: Shut Down System
4: Reboot System</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Streamed Channel Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of channels that the VeriStand Engine is currently streaming to the host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Max Streamed Channels" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The maximum number of channels that the VeriStand Engine can stream to the host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Model Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the models have not completed their execution in time</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Clients" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Maximum GENs" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of stimulus profile generators instantiated by the system</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Generator Engine State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="3">
						<Description>The current state of the stimulus profile generator engine

0: Idle
1: Running
2: Stopped
3: Paused</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Watchdog Timer" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The amount of time in nanoseconds since the Watchdog Timer Loop last executed. The Watchdog Timer Loop is set to execute at a rate of 10Hz.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HS TCP Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the streaming data gets overwritten.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Host IP" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The 32-bit integer IP Address of the connected host. A zero value indicates no host is connected to the VeriStand Engine.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Trace Enabled Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether execution tracing is currently active on the RT Target.  Set to 1 to start tracing.  Set to 0 to stop tracing and send result to host (if no host is present it is logged to disk).  Set to -1 to stop tracing and write result to disk.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Detailed Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether detailed execution tracing is enabled on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="VI Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether VI execution tracing is enabled on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Trace Buffer Size" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Bytes" BitFields="3">
						<Description>Specifies the size in bytes of the execution trace buffer on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>250000</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Thread Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether thread execution tracing is enabled on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Absolute Time" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>Returns the current date and time in seconds relative to 12:00 a.m., Friday, January 1, 1904, Universal Time [01-01-1904 00:00:00]. This value is coerced from a 128-bit value to double precision, which may impact resolution.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Time - Microseconds" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="usec" BitFields="1">
						<Description>The relative system time in microseconds of the VeriStand Engine according to the iteration count and Delta T of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 41" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 42" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 43" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 44" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Iterations" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Min Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Actual Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Failure Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The failure count of current analysis settings</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Analysis State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The state of the analysis sub-system on the RT execution host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="TCP Data Packet Loss" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the VeriStand Engine fails to send a data packet to the host. A non-zero number can indicate data loss in logged data. The value is reset every time a Workspace connects to the VeriStand Engine.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop attempted to write to a waveform read session within the NI VeriStand engine and timed out.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL TCP Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop attempted to write to the TCP loop (for a host waveform stream session) and timed out.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Error Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop encountered an error.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Error Code" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The last error code encountered by the waveform processing loop.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Streamed Waveform Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of waveforms that the VeriStand Engine is currently streaming to the host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 56" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 57" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 58" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 59" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 60" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 61" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 62" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 63" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 64" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 65" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 66" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 67" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 68" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 69" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 70" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 71" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 72" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 73" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 74" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 75" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 76" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 77" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 78" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 79" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 80" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 81" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 82" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 83" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 84" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 85" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 86" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 87" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 88" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 89" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 90" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 91" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="AO1 Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Loop Wakeup Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="1">
						<Description>The wakeup status of the Primary Control Loop.

0: Normal
1: Aborted
2: Asynchronous wakeup
3: Timing source error
4: Timed loop error
5: Timeout</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HD Free Space" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP-LP Overwrite" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Primary Control Loop timed out writing channel data to the Data Processing Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Data Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Data Processing Loop timed out writing channel data to the Communication Send Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Primary Control Loop reported being late</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Data Processing Loop reported being late</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Log Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The state of the logging sub-system on the RT execution host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
				</Section>
			</Target>
		</TargetSections>
		<Section Name="Aliases" TypeGUID="e11f4519-09e6-4fb0-99df-2967c4313d67">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Scales" TypeGUID="032c8aec-ce5b-6d40-06c5-5703bbc7ccee">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="System Mappings" TypeGUID="5691ea13-4544-497e-9bda-cf69dc707663">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Data Sharing Network" TypeGUID="8288dbb9-8c87-4fda-9c66-acec90c46c03">
			<Description />
			<Properties>
				<Property Name="CD Status">
					<U32>2</U32>
				</Property>
				<Property Name="DSN Dynamic Data Size">
					<I32>30</I32>
				</Property>
			</Properties>
			<Errors />
		</Section>
		<Section Name="System Initialization" TypeGUID="773b9311-3758-47fa-842f-b1c1960dabd0">
			<Description />
			<Properties>
				<Property Name="Auto Start">
					<Boolean>false</Boolean>
				</Property>
			</Properties>
			<Errors />
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/TestModelAPI/TestModelAPI_NotImported_AnyAccess.nivssdf sha256=e53b63371d5b436fad3ee8a0f834990da6a88c3b6a52ab3d2a6f36164c8e4a2a bytes=112437 -->
## FILE: tests/testutilities/legacy_files/TestModelAPI/TestModelAPI_NotImported_AnyAccess.nivssdf

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/TestModelAPI/TestModelAPI_NotImported_AnyAccess.nivssdf`
- sha256: `e53b63371d5b436fad3ee8a0f834990da6a88c3b6a52ab3d2a6f36164c8e4a2a`
- bytes: 112437

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2015" Minor="1" Fix="0" Build="0" />
	<Content>Definition</Content>
	<Root Name="TestModelAPI_NotImported_AnyAccess" TypeGUID="03D3BA22-1485-13A6-56BD17DA950CCD00">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>TestModelAPI_NotImported_AnyAccess</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.4</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3489580954.2815609</Double>
			</Property>
		</Properties>
		<Errors />
		<TargetSections Name="Targets" TypeGUID="eb379619-68d7-4d81-be90-c0bc511cdc10">
			<Description />
			<Properties />
			<Errors />
			<Target Name="Controller" TypeGUID="775504BB-1485-13A6-56755DBF2C326980">
				<Description />
				<Properties>
					<Property Name="OS">
						<String>PharLap</String>
					</Property>
					<Property Name="IP Address">
						<String />
					</Property>
					<Property Name="Control Loop Processor">
						<I32>-2</I32>
					</Property>
					<Property Name="Secondary Control Loop Processor">
						<I32>-2</I32>
					</Property>
					<Property Name="Stream Rate">
						<I32>1</I32>
					</Property>
					<Property Name="DIO Rate">
						<Double>100</Double>
					</Property>
					<Property Name="Streamed Channels">
						<I32>512</I32>
					</Property>
					<Property Name="Filter DAQ Errors">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Filter Watchdog Errors">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Engine Rate">
						<Double>100</Double>
					</Property>
					<Property Name="TL timeout">
						<Double>120</Double>
					</Property>
					<Property Name="daq timeout">
						<U32>1000</U32>
					</Property>
					<Property Name="TL sleep time">
						<U32>0</U32>
					</Property>
					<Property Name="HS Port">
						<I32>2040</I32>
					</Property>
					<Property Name="LS Port">
						<I32>2050</I32>
					</Property>
					<Property Name="HS Port Timeout">
						<I32>1000</I32>
					</Property>
					<Property Name="LS Port Timeout">
						<I32>1000</I32>
					</Property>
					<Property Name="Deployment Group">
						<I32>0</I32>
					</Property>
					<Property Name="Control Rate">
						<Double>1</Double>
					</Property>
					<Property Name="Input Configuration">
						<U32>0</U32>
					</Property>
					<Property Name="ts">
						<U32>0</U32>
					</Property>
					<Property Name="Warmup Time [ms]">
						<U32>2000</U32>
					</Property>
					<Property Name="Data Rate">
						<Double>15</Double>
					</Property>
					<Property Name="FPGAScanInterfaceMode">
						<U16>0</U16>
					</Property>
				</Properties>
				<Errors />
				<Section Name="Hardware" TypeGUID="775504AB-1485-13A6-560018C1F4E3EEE1">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Chassis" TypeGUID="03D3BACD-1485-13A6-56E99D97B7543BAF">
						<Description />
						<Properties>
							<Property Name="Master type">
								<U32>1</U32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Timing and Sync" TypeGUID="03D3BAED-1485-13A6-56E20B50F6E06D94">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="DAQ" TypeGUID="77550612-1485-13A6-56570AB5032158E9">
							<Description />
							<Properties />
							<Errors />
							<Section Name="Waveform Tasks" TypeGUID="1D6B8779-A957-42D1-B074-82153DB7FF44">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
						<Section Name="FPGA" TypeGUID="03D3B659-1485-13A6-5652D8A07328ECB7">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="NI-XNET" TypeGUID="6b693e6d-67b1-40b8-8108-4a4cc3147721">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
								</Property>
								<Property Name="Decimation">
									<I32>1</I32>
								</Property>
								<Property Name="Driver VI Exec Mode">
									<U32>1</U32>
								</Property>
							</Properties>
							<Errors />
							<Section Name="CAN" TypeGUID="6c5bb91f-0da7-407d-aefc-acbe49c768df">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="FlexRay" TypeGUID="e33fae90-03f1-4f76-b2f1-6eb8fcac2676">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="LIN" TypeGUID="c9c30728-42cb-4dc3-b054-b80e7a54e833">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
						<Section Name="Data Sharing" TypeGUID="d56f3ac1-7b2c-422c-9d11-fd9cc7abf2a5">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
					</Section>
				</Section>
				<Section Name="Custom Devices" TypeGUID="03D3BB79-1485-13A6-5605EB7AFD7405AC">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Simulation Models" TypeGUID="03D3B937-1485-13A6-5600F2871E269F9A">
					<Description />
					<Properties>
						<Property Name="ParameterAccess">
							<I32>1</I32>
						</Property>
					</Properties>
					<Errors />
					<Section Name="Models" TypeGUID="03D3B976-1485-13A6-5604255F981010CE">
						<Description />
						<Properties />
						<Errors />
						<Section Name="Custom_current" TypeGUID="03D3B9C4-1485-13A6-561FC9BB21813875">
							<Description />
							<Properties>
								<Property Name="Base Rate">
									<Double>10000</Double>
								</Property>
								<Property Name="DLL Size">
									<I32>16896</I32>
								</Property>
								<Property Name="DLL Timestamp">
									<Double>3489152502.2421064</Double>
								</Property>
								<Property Name="Decimation">
									<I32>1</I32>
								</Property>
								<Property Name="Import Definition ID">
									<I32>0</I32>
								</Property>
								<Property Name="ID">
									<I32>0</I32>
								</Property>
								<Property Name="Model Timestamp">
									<Double>0</Double>
								</Property>
								<Property Name="Processor">
									<I32>-2</I32>
								</Property>
								<Property Name="Show Unnamed Signals">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="User Rate">
									<Double>10000</Double>
								</Property>
								<Property Name="visible">
									<U32>0</U32>
								</Property>
								<Property Name="blocks only">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Segment Vectors">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="MD5">
									<String>2d525d49aaf9c9b5118d3fc243707a03</String>
								</Property>
								<Property Name="NIVeriStandServer Port">
									<U32>6012</U32>
								</Property>
								<Property Name="DLL Path">
									<DependentFile Type="To Common Doc Dir" Path="AutoTestProjects\Test Models\Compiled\Custom\autobuild\custom.dll">
										<Version />
										<ForceDownload>false</ForceDownload>
										<RTDestination>C:\ni-rt\NIVeriStand\Models\custom.dll</RTDestination>
										<SupportedTarget>PharLap &amp; Windows</SupportedTarget>
										<MD5>2d525d49aaf9c9b5118d3fc243707a03</MD5>
									</DependentFile>
								</Property>
								<Property Name="GlobalParameterScopes">
									<I32>0</I32>
								</Property>
							</Properties>
							<Errors />
							<Section Name="Execution" TypeGUID="03D3BA9F-1485-13A6-56E3D5196780015F">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Model Command" TypeGUID="03D3BABE-1485-13A6-56C34B877844B2C1" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description>0: Start
1: Pause
2: Reset
3: Save
4: Restore</Description>
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Model Time" TypeGUID="03D3BAAE-1485-13A6-5606A77AB57A7FC9" RowDim="1" ColDim="1" Units="sec" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Model Status" TypeGUID="03D3BB6A-1485-13A6-5643A7AFDA3A2658" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description>0: Running
1: Paused
2: Resetting
3: Idle
4: Stopped
5: Restoring
6: Saving</Description>
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Time Step Duration" TypeGUID="8e7cc8ad-0a9f-4b63-b5f0-59c025358253" RowDim="1" ColDim="1" Units="usec" BitFields="1">
									<Description>The duration in microseconds of the last model time step.</Description>
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Inports" TypeGUID="03D3B9E3-1485-13A6-56035B19B2245EB3">
								<Description />
								<Properties />
								<Errors />
								<Section Name="Inport_10x1" TypeGUID="cbfdde93-6581-4b7c-83b8-e88484f25b2e">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="Inport_10x1(1,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(2,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(3,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(4,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(5,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(6,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(7,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(8,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(9,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(10,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
								</Section>
								<Section Name="Inport_10x5" TypeGUID="cbfdde93-6581-4b7c-83b8-e88484f25b2e">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="Inport_10x5(1,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(1,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(1,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(1,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(1,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
								</Section>
								<Channel Name="Inport_1x1" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>Inport_1x1</String>
										</Property>
										<Property Name="Index">
											<I32>0</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Outports" TypeGUID="03D3B9F3-1485-13A6-5698C14838D6AA3C">
								<Description />
								<Properties />
								<Errors />
								<Section Name="Outport_10x1" TypeGUID="cbfdde93-6581-4b7c-83b8-e88484f25b2e">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="Outport_10x1(1,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(2,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(3,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(4,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(5,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(6,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(7,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(8,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(9,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(10,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
								</Section>
								<Section Name="Outport_10x5" TypeGUID="cbfdde93-6581-4b7c-83b8-e88484f25b2e">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="Outport_10x5(1,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(1,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(1,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(1,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(1,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
								</Section>
								<Channel Name="Outport_1x1" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>Outport_1x1</String>
										</Property>
										<Property Name="Index">
											<I32>3</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Parameters" TypeGUID="03D3BB0C-1485-13A6-56E10CEFF755E7D3">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="Signals" TypeGUID="03D3BA31-1485-13A6-567CA69E9D2E71D5">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
					</Section>
					<Section Name="Execution Order" TypeGUID="03D3B966-1485-13A6-569CFF8A449BF90A">
						<Description />
						<Properties />
						<Errors />
					</Section>
				</Section>
				<Section Name="User Channels" TypeGUID="03D3B6B7-1485-13A6-567BE1E1E0DF999A">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Calculated Channels" TypeGUID="03D3B714-1485-13A6-56031C5F1CCB78A9">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Stimulus" TypeGUID="03D3B7FF-1485-13A6-56B2328F9511AC8B">
					<Description />
					<Properties>
						<Property Name="Max Steps">
							<I32>128</I32>
						</Property>
						<Property Name="Max Gen Maps">
							<I32>256</I32>
						</Property>
						<Property Name="Aux Buffer Size">
							<I32>10000</I32>
						</Property>
						<Property Name="Analysis Buffer Size">
							<I32>10000</I32>
						</Property>
						<Property Name="Analysis Result Size">
							<I32>5000</I32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Alarms" TypeGUID="03D3B782-1485-13A6-56F58B35B6CBA484">
					<Description />
					<Properties>
						<Property Name="Alarm Rate">
							<I32>1</I32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Procedures" TypeGUID="03D3B7B1-1485-13A6-56649C7783203F22">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="XNET Databases" TypeGUID="def5630b-577f-4ae9-9682-5f8ee445ee21">
					<Description />
					<Properties>
						<Property Name="CD Status">
							<U32>2</U32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="System Channels" TypeGUID="03D3B753-1485-13A6-56B10ED0820CF410">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="Actual Loop Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Hz" BitFields="1">
						<Description>The execution rate of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Index" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The decimation of the Data Processing Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Time" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>The relative system time of the VeriStand Engine according to the iteration count and Delta T of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="DAQ Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Error Code" BitFields="3">
						<Description>The last reported error code from a DAQmx function call. The value zero indicates no error has occurred.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Delta T" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>The period in seconds of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Compiler Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 1" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 2" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 3" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Resume Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 4" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 5" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 6" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="RT Engine Build" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>A value representing the build number of the NI VeriStand Engine</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Loop Duration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The duration of the Primary Control Loop in nanoseconds</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Loop Duration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The duration of the Data Processing Loop in nanoseconds</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Command" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="3">
						<Description>Internally commands the RT system with the following numeric values:

0: None
1: Restart System
2: Reset System
3: Shut Down System
4: Reboot System</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Streamed Channel Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of channels that the VeriStand Engine is currently streaming to the host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Max Streamed Channels" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The maximum number of channels that the VeriStand Engine can stream to the host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Model Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the models have not completed their execution in time</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Clients" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Maximum GENs" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of stimulus profile generators instantiated by the system</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Generator Engine State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="3">
						<Description>The current state of the stimulus profile generator engine

0: Idle
1: Running
2: Stopped
3: Paused</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Watchdog Timer" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The amount of time in nanoseconds since the Watchdog Timer Loop last executed. The Watchdog Timer Loop is set to execute at a rate of 10Hz.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HS TCP Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the streaming data gets overwritten.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Host IP" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The 32-bit integer IP Address of the connected host. A zero value indicates no host is connected to the VeriStand Engine.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Trace Enabled Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether execution tracing is currently active on the RT Target.  Set to 1 to start tracing.  Set to 0 to stop tracing and send result to host (if no host is present it is logged to disk).  Set to -1 to stop tracing and write result to disk.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Detailed Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether detailed execution tracing is enabled on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="VI Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether VI execution tracing is enabled on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Trace Buffer Size" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Bytes" BitFields="3">
						<Description>Specifies the size in bytes of the execution trace buffer on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>250000</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Thread Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether thread execution tracing is enabled on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Absolute Time" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>Returns the current date and time in seconds relative to 12:00 a.m., Friday, January 1, 1904, Universal Time [01-01-1904 00:00:00]. This value is coerced from a 128-bit value to double precision, which may impact resolution.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Time - Microseconds" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="usec" BitFields="1">
						<Description>The relative system time in microseconds of the VeriStand Engine according to the iteration count and Delta T of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 41" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 42" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 43" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 44" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Iterations" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Min Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Actual Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Failure Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The failure count of current analysis settings</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Analysis State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The state of the analysis sub-system on the RT execution host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="TCP Data Packet Loss" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the VeriStand Engine fails to send a data packet to the host. A non-zero number can indicate data loss in logged data. The value is reset every time a Workspace connects to the VeriStand Engine.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop attempted to write to a waveform read session within the NI VeriStand engine and timed out.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL TCP Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop attempted to write to the TCP loop (for a host waveform stream session) and timed out.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Error Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop encountered an error.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Error Code" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The last error code encountered by the waveform processing loop.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Streamed Waveform Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of waveforms that the VeriStand Engine is currently streaming to the host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Iteration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The iteration count of the Primary Control Loop.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Last Late Iteration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The iteration count of the Primary Control Loop that last recorded a late count. If the Primary Control Loop has not recorded a late count, this value is -1.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 58" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 59" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Real-Time Sequence Command" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Internally commands the active real-time sequences with the following numeric values:
		
		0: None
		1: Stop All
		2: Abort All</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Real-Time Sequence Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of real-time sequences currently running.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 62" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 63" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 64" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 65" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 66" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 67" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 68" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 69" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 70" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 71" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 72" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 73" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 74" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 75" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 76" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 77" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 78" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 79" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 80" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 81" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 82" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 83" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 84" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 85" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 86" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 87" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 88" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 89" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 90" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 91" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="AO1 Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Loop Wakeup Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="1">
						<Description>The wakeup status of the Primary Control Loop.

0: Normal
1: Aborted
2: Asynchronous wakeup
3: Timing source error
4: Timed loop error
5: Timeout</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HD Free Space" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP-LP Overwrite" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Primary Control Loop timed out writing channel data to the Data Processing Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Data Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Data Processing Loop timed out writing channel data to the Communication Send Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Primary Control Loop reported being late</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Data Processing Loop reported being late</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Log Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The state of the logging sub-system on the RT execution host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
				</Section>
			</Target>
		</TargetSections>
		<Section Name="Aliases" TypeGUID="e11f4519-09e6-4fb0-99df-2967c4313d67">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Scales" TypeGUID="032c8aec-ce5b-6d40-06c5-5703bbc7ccee">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="System Mappings" TypeGUID="5691ea13-4544-497e-9bda-cf69dc707663">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Data Sharing Network" TypeGUID="8288dbb9-8c87-4fda-9c66-acec90c46c03">
			<Description />
			<Properties>
				<Property Name="CD Status">
					<U32>2</U32>
				</Property>
				<Property Name="DSN Dynamic Data Size">
					<I32>30</I32>
				</Property>
			</Properties>
			<Errors />
		</Section>
		<Section Name="System Initialization" TypeGUID="773b9311-3758-47fa-842f-b1c1960dabd0">
			<Description />
			<Properties>
				<Property Name="Auto Start">
					<Boolean>false</Boolean>
				</Property>
			</Properties>
			<Errors />
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/TestModelAPI/TestModelAPI_NotImported_OnlyImportedAccess.nivssdf sha256=90f99fa4faa035baa827f3632ac07fe0a020c33c539f34f7159d78b67a1f245e bytes=112356 -->
## FILE: tests/testutilities/legacy_files/TestModelAPI/TestModelAPI_NotImported_OnlyImportedAccess.nivssdf

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/TestModelAPI/TestModelAPI_NotImported_OnlyImportedAccess.nivssdf`
- sha256: `90f99fa4faa035baa827f3632ac07fe0a020c33c539f34f7159d78b67a1f245e`
- bytes: 112356

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2015" Minor="1" Fix="0" Build="0" />
	<Content>Definition</Content>
	<Root Name="TestModelAPI_NotImported_OnlyImportedAccess" TypeGUID="03D3BA22-1485-13A6-56BD17DA950CCD00">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>TestModelAPI_NotImported_OnlyImportedAccess</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.2</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3489580954.2815609</Double>
			</Property>
		</Properties>
		<Errors />
		<TargetSections Name="Targets" TypeGUID="eb379619-68d7-4d81-be90-c0bc511cdc10">
			<Description />
			<Properties />
			<Errors />
			<Target Name="Controller" TypeGUID="775504BB-1485-13A6-56755DBF2C326980">
				<Description />
				<Properties>
					<Property Name="OS">
						<String>PharLap</String>
					</Property>
					<Property Name="IP Address">
						<String />
					</Property>
					<Property Name="Control Loop Processor">
						<I32>-2</I32>
					</Property>
					<Property Name="Secondary Control Loop Processor">
						<I32>-2</I32>
					</Property>
					<Property Name="Stream Rate">
						<I32>1</I32>
					</Property>
					<Property Name="DIO Rate">
						<Double>100</Double>
					</Property>
					<Property Name="Streamed Channels">
						<I32>512</I32>
					</Property>
					<Property Name="Filter DAQ Errors">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Filter Watchdog Errors">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Engine Rate">
						<Double>100</Double>
					</Property>
					<Property Name="TL timeout">
						<Double>120</Double>
					</Property>
					<Property Name="daq timeout">
						<U32>1000</U32>
					</Property>
					<Property Name="TL sleep time">
						<U32>0</U32>
					</Property>
					<Property Name="HS Port">
						<I32>2040</I32>
					</Property>
					<Property Name="LS Port">
						<I32>2050</I32>
					</Property>
					<Property Name="HS Port Timeout">
						<I32>1000</I32>
					</Property>
					<Property Name="LS Port Timeout">
						<I32>1000</I32>
					</Property>
					<Property Name="Deployment Group">
						<I32>0</I32>
					</Property>
					<Property Name="Control Rate">
						<Double>1</Double>
					</Property>
					<Property Name="Input Configuration">
						<U32>0</U32>
					</Property>
					<Property Name="ts">
						<U32>0</U32>
					</Property>
					<Property Name="Warmup Time [ms]">
						<U32>2000</U32>
					</Property>
					<Property Name="Data Rate">
						<Double>15</Double>
					</Property>
					<Property Name="FPGAScanInterfaceMode">
						<U16>0</U16>
					</Property>
				</Properties>
				<Errors />
				<Section Name="Hardware" TypeGUID="775504AB-1485-13A6-560018C1F4E3EEE1">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Chassis" TypeGUID="03D3BACD-1485-13A6-56E99D97B7543BAF">
						<Description />
						<Properties>
							<Property Name="Master type">
								<U32>1</U32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Timing and Sync" TypeGUID="03D3BAED-1485-13A6-56E20B50F6E06D94">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="DAQ" TypeGUID="77550612-1485-13A6-56570AB5032158E9">
							<Description />
							<Properties />
							<Errors />
							<Section Name="Waveform Tasks" TypeGUID="1D6B8779-A957-42D1-B074-82153DB7FF44">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
						<Section Name="FPGA" TypeGUID="03D3B659-1485-13A6-5652D8A07328ECB7">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="NI-XNET" TypeGUID="6b693e6d-67b1-40b8-8108-4a4cc3147721">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
								</Property>
								<Property Name="Decimation">
									<I32>1</I32>
								</Property>
								<Property Name="Driver VI Exec Mode">
									<U32>1</U32>
								</Property>
							</Properties>
							<Errors />
							<Section Name="CAN" TypeGUID="6c5bb91f-0da7-407d-aefc-acbe49c768df">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="FlexRay" TypeGUID="e33fae90-03f1-4f76-b2f1-6eb8fcac2676">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="LIN" TypeGUID="c9c30728-42cb-4dc3-b054-b80e7a54e833">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
						<Section Name="Data Sharing" TypeGUID="d56f3ac1-7b2c-422c-9d11-fd9cc7abf2a5">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
					</Section>
				</Section>
				<Section Name="Custom Devices" TypeGUID="03D3BB79-1485-13A6-5605EB7AFD7405AC">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Simulation Models" TypeGUID="03D3B937-1485-13A6-5600F2871E269F9A">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Models" TypeGUID="03D3B976-1485-13A6-5604255F981010CE">
						<Description />
						<Properties />
						<Errors />
						<Section Name="Custom_current" TypeGUID="03D3B9C4-1485-13A6-561FC9BB21813875">
							<Description />
							<Properties>
								<Property Name="Base Rate">
									<Double>10000</Double>
								</Property>
								<Property Name="DLL Size">
									<I32>16896</I32>
								</Property>
								<Property Name="DLL Timestamp">
									<Double>3489152502.2421064</Double>
								</Property>
								<Property Name="Decimation">
									<I32>1</I32>
								</Property>
								<Property Name="Import Definition ID">
									<I32>0</I32>
								</Property>
								<Property Name="ID">
									<I32>0</I32>
								</Property>
								<Property Name="Model Timestamp">
									<Double>0</Double>
								</Property>
								<Property Name="Processor">
									<I32>-2</I32>
								</Property>
								<Property Name="Show Unnamed Signals">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="User Rate">
									<Double>10000</Double>
								</Property>
								<Property Name="visible">
									<U32>0</U32>
								</Property>
								<Property Name="blocks only">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Segment Vectors">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="MD5">
									<String>2d525d49aaf9c9b5118d3fc243707a03</String>
								</Property>
								<Property Name="NIVeriStandServer Port">
									<U32>6012</U32>
								</Property>
								<Property Name="DLL Path">
									<DependentFile Type="To Common Doc Dir" Path="AutoTestProjects\Test Models\Compiled\Custom\autobuild\custom.dll">
										<Version />
										<ForceDownload>false</ForceDownload>
										<RTDestination>C:\ni-rt\NIVeriStand\Models\custom.dll</RTDestination>
										<SupportedTarget>PharLap &amp; Windows</SupportedTarget>
										<MD5>2d525d49aaf9c9b5118d3fc243707a03</MD5>
									</DependentFile>
								</Property>
								<Property Name="GlobalParameterScopes">
									<I32>0</I32>
								</Property>
							</Properties>
							<Errors />
							<Section Name="Execution" TypeGUID="03D3BA9F-1485-13A6-56E3D5196780015F">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Model Command" TypeGUID="03D3BABE-1485-13A6-56C34B877844B2C1" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description>0: Start
1: Pause
2: Reset
3: Save
4: Restore</Description>
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Model Time" TypeGUID="03D3BAAE-1485-13A6-5606A77AB57A7FC9" RowDim="1" ColDim="1" Units="sec" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Model Status" TypeGUID="03D3BB6A-1485-13A6-5643A7AFDA3A2658" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description>0: Running
1: Paused
2: Resetting
3: Idle
4: Stopped
5: Restoring
6: Saving</Description>
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Time Step Duration" TypeGUID="8e7cc8ad-0a9f-4b63-b5f0-59c025358253" RowDim="1" ColDim="1" Units="usec" BitFields="1">
									<Description>The duration in microseconds of the last model time step.</Description>
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Inports" TypeGUID="03D3B9E3-1485-13A6-56035B19B2245EB3">
								<Description />
								<Properties />
								<Errors />
								<Section Name="Inport_10x1" TypeGUID="cbfdde93-6581-4b7c-83b8-e88484f25b2e">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="Inport_10x1(1,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(2,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(3,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(4,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(5,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(6,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(7,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(8,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(9,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(10,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
								</Section>
								<Section Name="Inport_10x5" TypeGUID="cbfdde93-6581-4b7c-83b8-e88484f25b2e">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="Inport_10x5(1,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(1,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(1,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(1,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(1,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
								</Section>
								<Channel Name="Inport_1x1" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>Inport_1x1</String>
										</Property>
										<Property Name="Index">
											<I32>0</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Outports" TypeGUID="03D3B9F3-1485-13A6-5698C14838D6AA3C">
								<Description />
								<Properties />
								<Errors />
								<Section Name="Outport_10x1" TypeGUID="cbfdde93-6581-4b7c-83b8-e88484f25b2e">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="Outport_10x1(1,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(2,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(3,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(4,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(5,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(6,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(7,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(8,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(9,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(10,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
								</Section>
								<Section Name="Outport_10x5" TypeGUID="cbfdde93-6581-4b7c-83b8-e88484f25b2e">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="Outport_10x5(1,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(1,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(1,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(1,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(1,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
								</Section>
								<Channel Name="Outport_1x1" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>Outport_1x1</String>
										</Property>
										<Property Name="Index">
											<I32>3</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Parameters" TypeGUID="03D3BB0C-1485-13A6-56E10CEFF755E7D3">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="Signals" TypeGUID="03D3BA31-1485-13A6-567CA69E9D2E71D5">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
					</Section>
					<Section Name="Execution Order" TypeGUID="03D3B966-1485-13A6-569CFF8A449BF90A">
						<Description />
						<Properties />
						<Errors />
					</Section>
				</Section>
				<Section Name="User Channels" TypeGUID="03D3B6B7-1485-13A6-567BE1E1E0DF999A">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Calculated Channels" TypeGUID="03D3B714-1485-13A6-56031C5F1CCB78A9">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Stimulus" TypeGUID="03D3B7FF-1485-13A6-56B2328F9511AC8B">
					<Description />
					<Properties>
						<Property Name="Max Steps">
							<I32>128</I32>
						</Property>
						<Property Name="Max Gen Maps">
							<I32>256</I32>
						</Property>
						<Property Name="Aux Buffer Size">
							<I32>10000</I32>
						</Property>
						<Property Name="Analysis Buffer Size">
							<I32>10000</I32>
						</Property>
						<Property Name="Analysis Result Size">
							<I32>5000</I32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Alarms" TypeGUID="03D3B782-1485-13A6-56F58B35B6CBA484">
					<Description />
					<Properties>
						<Property Name="Alarm Rate">
							<I32>1</I32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Procedures" TypeGUID="03D3B7B1-1485-13A6-56649C7783203F22">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="XNET Databases" TypeGUID="def5630b-577f-4ae9-9682-5f8ee445ee21">
					<Description />
					<Properties>
						<Property Name="CD Status">
							<U32>2</U32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="System Channels" TypeGUID="03D3B753-1485-13A6-56B10ED0820CF410">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="Actual Loop Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Hz" BitFields="1">
						<Description>The execution rate of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Index" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The decimation of the Data Processing Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Time" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>The relative system time of the VeriStand Engine according to the iteration count and Delta T of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="DAQ Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Error Code" BitFields="3">
						<Description>The last reported error code from a DAQmx function call. The value zero indicates no error has occurred.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Delta T" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>The period in seconds of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Compiler Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 1" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 2" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 3" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Resume Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 4" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 5" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 6" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="RT Engine Build" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>A value representing the build number of the NI VeriStand Engine</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Loop Duration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The duration of the Primary Control Loop in nanoseconds</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Loop Duration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The duration of the Data Processing Loop in nanoseconds</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Command" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="3">
						<Description>Internally commands the RT system with the following numeric values:

0: None
1: Restart System
2: Reset System
3: Shut Down System
4: Reboot System</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Streamed Channel Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of channels that the VeriStand Engine is currently streaming to the host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Max Streamed Channels" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The maximum number of channels that the VeriStand Engine can stream to the host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Model Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the models have not completed their execution in time</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Clients" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Maximum GENs" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of stimulus profile generators instantiated by the system</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Generator Engine State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="3">
						<Description>The current state of the stimulus profile generator engine

0: Idle
1: Running
2: Stopped
3: Paused</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Watchdog Timer" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The amount of time in nanoseconds since the Watchdog Timer Loop last executed. The Watchdog Timer Loop is set to execute at a rate of 10Hz.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HS TCP Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the streaming data gets overwritten.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Host IP" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The 32-bit integer IP Address of the connected host. A zero value indicates no host is connected to the VeriStand Engine.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Trace Enabled Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether execution tracing is currently active on the RT Target.  Set to 1 to start tracing.  Set to 0 to stop tracing and send result to host (if no host is present it is logged to disk).  Set to -1 to stop tracing and write result to disk.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Detailed Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether detailed execution tracing is enabled on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="VI Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether VI execution tracing is enabled on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Trace Buffer Size" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Bytes" BitFields="3">
						<Description>Specifies the size in bytes of the execution trace buffer on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>250000</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Thread Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether thread execution tracing is enabled on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Absolute Time" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>Returns the current date and time in seconds relative to 12:00 a.m., Friday, January 1, 1904, Universal Time [01-01-1904 00:00:00]. This value is coerced from a 128-bit value to double precision, which may impact resolution.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Time - Microseconds" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="usec" BitFields="1">
						<Description>The relative system time in microseconds of the VeriStand Engine according to the iteration count and Delta T of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 41" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 42" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 43" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 44" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Iterations" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Min Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Actual Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Failure Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The failure count of current analysis settings</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Analysis State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The state of the analysis sub-system on the RT execution host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="TCP Data Packet Loss" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the VeriStand Engine fails to send a data packet to the host. A non-zero number can indicate data loss in logged data. The value is reset every time a Workspace connects to the VeriStand Engine.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop attempted to write to a waveform read session within the NI VeriStand engine and timed out.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL TCP Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop attempted to write to the TCP loop (for a host waveform stream session) and timed out.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Error Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop encountered an error.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Error Code" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The last error code encountered by the waveform processing loop.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Streamed Waveform Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of waveforms that the VeriStand Engine is currently streaming to the host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Iteration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The iteration count of the Primary Control Loop.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Last Late Iteration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The iteration count of the Primary Control Loop that last recorded a late count. If the Primary Control Loop has not recorded a late count, this value is -1.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 58" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 59" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Real-Time Sequence Command" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Internally commands the active real-time sequences with the following numeric values:
		
		0: None
		1: Stop All
		2: Abort All</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Real-Time Sequence Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of real-time sequences currently running.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 62" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 63" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 64" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 65" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 66" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 67" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 68" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 69" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 70" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 71" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 72" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 73" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 74" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 75" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 76" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 77" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 78" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 79" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 80" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 81" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 82" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 83" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 84" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 85" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 86" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 87" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 88" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 89" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 90" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 91" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="AO1 Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Loop Wakeup Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="1">
						<Description>The wakeup status of the Primary Control Loop.

0: Normal
1: Aborted
2: Asynchronous wakeup
3: Timing source error
4: Timed loop error
5: Timeout</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HD Free Space" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP-LP Overwrite" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Primary Control Loop timed out writing channel data to the Data Processing Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Data Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Data Processing Loop timed out writing channel data to the Communication Send Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Primary Control Loop reported being late</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Data Processing Loop reported being late</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Log Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The state of the logging sub-system on the RT execution host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
				</Section>
			</Target>
		</TargetSections>
		<Section Name="Aliases" TypeGUID="e11f4519-09e6-4fb0-99df-2967c4313d67">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Scales" TypeGUID="032c8aec-ce5b-6d40-06c5-5703bbc7ccee">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="System Mappings" TypeGUID="5691ea13-4544-497e-9bda-cf69dc707663">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Data Sharing Network" TypeGUID="8288dbb9-8c87-4fda-9c66-acec90c46c03">
			<Description />
			<Properties>
				<Property Name="CD Status">
					<U32>2</U32>
				</Property>
				<Property Name="DSN Dynamic Data Size">
					<I32>30</I32>
				</Property>
			</Properties>
			<Errors />
		</Section>
		<Section Name="System Initialization" TypeGUID="773b9311-3758-47fa-842f-b1c1960dabd0">
			<Description />
			<Properties>
				<Property Name="Auto Start">
					<Boolean>false</Boolean>
				</Property>
			</Properties>
			<Errors />
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/TestModelAPI/TestModelAPI_NotImportedParams.nivssdf sha256=2f20d5eb9709159810654a40b51987be7856f5320a78762fdd33923b9bff31ce bytes=115817 -->
## FILE: tests/testutilities/legacy_files/TestModelAPI/TestModelAPI_NotImportedParams.nivssdf

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/TestModelAPI/TestModelAPI_NotImportedParams.nivssdf`
- sha256: `2f20d5eb9709159810654a40b51987be7856f5320a78762fdd33923b9bff31ce`
- bytes: 115817

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2015" Minor="1" Fix="0" Build="0" />
	<Content>Definition</Content>
	<Root Name="TestModelAPI_NotImportedParams" TypeGUID="03D3BA22-1485-13A6-56BD17DA950CCD00">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>TestModelAPI_NotImportedParams</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.5</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3543918078.7694049</Double>
			</Property>
		</Properties>
		<Errors />
		<TargetSections Name="Targets" TypeGUID="eb379619-68d7-4d81-be90-c0bc511cdc10">
			<Description />
			<Properties />
			<Errors />
			<Target Name="Controller" TypeGUID="775504BB-1485-13A6-56755DBF2C326980">
				<Description />
				<Properties>
					<Property Name="OS">
						<String>PharLap</String>
					</Property>
					<Property Name="IP Address">
						<String />
					</Property>
					<Property Name="Control Loop Processor">
						<I32>-2</I32>
					</Property>
					<Property Name="Secondary Control Loop Processor">
						<I32>-2</I32>
					</Property>
					<Property Name="Stream Rate">
						<I32>1</I32>
					</Property>
					<Property Name="DIO Rate">
						<Double>100</Double>
					</Property>
					<Property Name="Streamed Channels">
						<I32>512</I32>
					</Property>
					<Property Name="Filter DAQ Errors">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Filter Watchdog Errors">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Engine Rate">
						<Double>100</Double>
					</Property>
					<Property Name="TL timeout">
						<Double>120</Double>
					</Property>
					<Property Name="daq timeout">
						<U32>1000</U32>
					</Property>
					<Property Name="TL sleep time">
						<U32>0</U32>
					</Property>
					<Property Name="HS Port">
						<I32>2040</I32>
					</Property>
					<Property Name="LS Port">
						<I32>2050</I32>
					</Property>
					<Property Name="HS Port Timeout">
						<I32>1000</I32>
					</Property>
					<Property Name="LS Port Timeout">
						<I32>1000</I32>
					</Property>
					<Property Name="Deployment Group">
						<I32>0</I32>
					</Property>
					<Property Name="Control Rate">
						<Double>1</Double>
					</Property>
					<Property Name="Input Configuration">
						<U32>0</U32>
					</Property>
					<Property Name="ts">
						<U32>0</U32>
					</Property>
					<Property Name="Warmup Time [ms]">
						<U32>2000</U32>
					</Property>
					<Property Name="Data Rate">
						<Double>15</Double>
					</Property>
					<Property Name="FPGAScanInterfaceMode">
						<U16>0</U16>
					</Property>
				</Properties>
				<Errors />
				<Section Name="Hardware" TypeGUID="775504AB-1485-13A6-560018C1F4E3EEE1">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Chassis" TypeGUID="03D3BACD-1485-13A6-56E99D97B7543BAF">
						<Description />
						<Properties>
							<Property Name="Master type">
								<U32>1</U32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Timing and Sync" TypeGUID="03D3BAED-1485-13A6-56E20B50F6E06D94">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="DAQ" TypeGUID="77550612-1485-13A6-56570AB5032158E9">
							<Description />
							<Properties />
							<Errors />
							<Section Name="Waveform Tasks" TypeGUID="1D6B8779-A957-42D1-B074-82153DB7FF44">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
						<Section Name="FPGA" TypeGUID="03D3B659-1485-13A6-5652D8A07328ECB7">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="NI-XNET" TypeGUID="6b693e6d-67b1-40b8-8108-4a4cc3147721">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
								</Property>
								<Property Name="Decimation">
									<I32>1</I32>
								</Property>
								<Property Name="Driver VI Exec Mode">
									<U32>1</U32>
								</Property>
							</Properties>
							<Errors />
							<Section Name="CAN" TypeGUID="6c5bb91f-0da7-407d-aefc-acbe49c768df">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="FlexRay" TypeGUID="e33fae90-03f1-4f76-b2f1-6eb8fcac2676">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="LIN" TypeGUID="c9c30728-42cb-4dc3-b054-b80e7a54e833">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
						<Section Name="Data Sharing" TypeGUID="d56f3ac1-7b2c-422c-9d11-fd9cc7abf2a5">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
					</Section>
				</Section>
				<Section Name="Custom Devices" TypeGUID="03D3BB79-1485-13A6-5605EB7AFD7405AC">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Simulation Models" TypeGUID="03D3B937-1485-13A6-5600F2871E269F9A">
					<Description />
					<Properties>
						<Property Name="ParameterAccess">
							<I32>1</I32>
						</Property>
					</Properties>
					<Errors />
					<Section Name="Models" TypeGUID="03D3B976-1485-13A6-5604255F981010CE">
						<Description />
						<Properties />
						<Errors />
						<Section Name="Custom_current" TypeGUID="03D3B9C4-1485-13A6-561FC9BB21813875">
							<Description />
							<Properties>
								<Property Name="Base Rate">
									<Double>10000</Double>
								</Property>
								<Property Name="DLL Size">
									<I32>16896</I32>
								</Property>
								<Property Name="DLL Timestamp">
									<Double>3489152502.2421064</Double>
								</Property>
								<Property Name="Decimation">
									<I32>1</I32>
								</Property>
								<Property Name="Import Definition ID">
									<I32>0</I32>
								</Property>
								<Property Name="ID">
									<I32>0</I32>
								</Property>
								<Property Name="Model Timestamp">
									<Double>0</Double>
								</Property>
								<Property Name="Processor">
									<I32>-2</I32>
								</Property>
								<Property Name="Show Unnamed Signals">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="User Rate">
									<Double>10000</Double>
								</Property>
								<Property Name="visible">
									<U32>0</U32>
								</Property>
								<Property Name="blocks only">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Segment Vectors">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="MD5">
									<String>2d525d49aaf9c9b5118d3fc243707a03</String>
								</Property>
								<Property Name="NIVeriStandServer Port">
									<U32>6012</U32>
								</Property>
								<Property Name="DLL Path">
									<DependentFile Type="To Common Doc Dir" Path="AutoTestProjects\Test Models\Compiled\Custom\autobuild\custom.dll">
										<Version />
										<ForceDownload>false</ForceDownload>
										<RTDestination>C:\ni-rt\NIVeriStand\Models\custom.dll</RTDestination>
										<SupportedTarget>PharLap &amp; Windows</SupportedTarget>
										<MD5>2d525d49aaf9c9b5118d3fc243707a03</MD5>
									</DependentFile>
								</Property>
								<Property Name="GlobalParameterScopes">
									<I32>0</I32>
								</Property>
							</Properties>
							<Errors />
							<Section Name="Execution" TypeGUID="03D3BA9F-1485-13A6-56E3D5196780015F">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Model Command" TypeGUID="03D3BABE-1485-13A6-56C34B877844B2C1" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description>0: Start
1: Pause
2: Reset
3: Save
4: Restore</Description>
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Model Time" TypeGUID="03D3BAAE-1485-13A6-5606A77AB57A7FC9" RowDim="1" ColDim="1" Units="sec" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Model Status" TypeGUID="03D3BB6A-1485-13A6-5643A7AFDA3A2658" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description>0: Running
1: Paused
2: Resetting
3: Idle
4: Stopped
5: Restoring
6: Saving</Description>
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Time Step Duration" TypeGUID="8e7cc8ad-0a9f-4b63-b5f0-59c025358253" RowDim="1" ColDim="1" Units="usec" BitFields="1">
									<Description>The duration in microseconds of the last model time step.</Description>
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Inports" TypeGUID="03D3B9E3-1485-13A6-56035B19B2245EB3">
								<Description />
								<Properties />
								<Errors />
								<Section Name="Inport_10x1" TypeGUID="cbfdde93-6581-4b7c-83b8-e88484f25b2e">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="Inport_10x1(1,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(2,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(3,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(4,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(5,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(6,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(7,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(8,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(9,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x1(10,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>1</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
								</Section>
								<Section Name="Inport_10x5" TypeGUID="cbfdde93-6581-4b7c-83b8-e88484f25b2e">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="Inport_10x5(1,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(1,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(1,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(1,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(1,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(2,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(3,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(4,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(5,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(6,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(7,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(8,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(9,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,1)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,2)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,3)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,4)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Inport_10x5(10,5)" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Inport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>2</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
								</Section>
								<Channel Name="Inport_1x1" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>Inport_1x1</String>
										</Property>
										<Property Name="Index">
											<I32>0</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Outports" TypeGUID="03D3B9F3-1485-13A6-5698C14838D6AA3C">
								<Description />
								<Properties />
								<Errors />
								<Section Name="Outport_10x1" TypeGUID="cbfdde93-6581-4b7c-83b8-e88484f25b2e">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="Outport_10x1(1,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(2,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(3,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(4,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(5,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(6,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(7,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(8,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(9,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x1(10,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x1</String>
											</Property>
											<Property Name="Index">
												<I32>4</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
								</Section>
								<Section Name="Outport_10x5" TypeGUID="cbfdde93-6581-4b7c-83b8-e88484f25b2e">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="Outport_10x5(1,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(1,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(1,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(1,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(1,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(2,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(3,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(4,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(5,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(6,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(7,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(8,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(9,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,1)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,2)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,3)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,4)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
									<Channel Name="Outport_10x5(10,5)" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
										<Description />
										<Properties>
											<Property Name="Model Path">
												<String>Outport_10x5</String>
											</Property>
											<Property Name="Index">
												<I32>5</I32>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>0</Elem>
										</DefaultValue>
									</Channel>
								</Section>
								<Channel Name="Outport_1x1" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>Outport_1x1</String>
										</Property>
										<Property Name="Index">
											<I32>3</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Parameters" TypeGUID="03D3BB0C-1485-13A6-56E10CEFF755E7D3">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Offset_1x1" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>test/Offset_1x1</String>
										</Property>
										<Property Name="Expression">
											<String>Offset_1x1</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>1</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>1</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Offset_10x1" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="10" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>test/Offset_10x1</String>
										</Property>
										<Property Name="Expression">
											<String>Offset_10x1</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>3</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Offset_10x5" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="10" ColDim="5" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>test/Offset_10x5</String>
										</Property>
										<Property Name="Expression">
											<String>Offset_10x5</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>5</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
										<Elem>1</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Signals" TypeGUID="03D3BA31-1485-13A6-567CA69E9D2E71D5">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
					</Section>
					<Section Name="Execution Order" TypeGUID="03D3B966-1485-13A6-569CFF8A449BF90A">
						<Description />
						<Properties />
						<Errors />
					</Section>
				</Section>
				<Section Name="User Channels" TypeGUID="03D3B6B7-1485-13A6-567BE1E1E0DF999A">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Calculated Channels" TypeGUID="03D3B714-1485-13A6-56031C5F1CCB78A9">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Stimulus" TypeGUID="03D3B7FF-1485-13A6-56B2328F9511AC8B">
					<Description />
					<Properties>
						<Property Name="Max Steps">
							<I32>128</I32>
						</Property>
						<Property Name="Max Gen Maps">
							<I32>256</I32>
						</Property>
						<Property Name="Aux Buffer Size">
							<I32>10000</I32>
						</Property>
						<Property Name="Analysis Buffer Size">
							<I32>10000</I32>
						</Property>
						<Property Name="Analysis Result Size">
							<I32>5000</I32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Alarms" TypeGUID="03D3B782-1485-13A6-56F58B35B6CBA484">
					<Description />
					<Properties>
						<Property Name="Alarm Rate">
							<I32>1</I32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Procedures" TypeGUID="03D3B7B1-1485-13A6-56649C7783203F22">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="XNET Databases" TypeGUID="def5630b-577f-4ae9-9682-5f8ee445ee21">
					<Description />
					<Properties>
						<Property Name="CD Status">
							<U32>2</U32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="System Channels" TypeGUID="03D3B753-1485-13A6-56B10ED0820CF410">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="Actual Loop Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Hz" BitFields="1">
						<Description>The execution rate of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Index" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The decimation of the Data Processing Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Time" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>The relative system time of the VeriStand Engine according to the iteration count and Delta T of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="DAQ Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Error Code" BitFields="3">
						<Description>The last reported error code from a DAQmx function call. The value zero indicates no error has occurred.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Delta T" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>The period in seconds of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Compiler Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 1" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 2" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 3" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Resume Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 4" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 5" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 6" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="RT Engine Build" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>A value representing the build number of the NI VeriStand Engine</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Loop Duration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The duration of the Primary Control Loop in nanoseconds</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Loop Duration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The duration of the Data Processing Loop in nanoseconds</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Command" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="3">
						<Description>Internally commands the RT system with the following numeric values:

0: None
1: Restart System
2: Reset System
3: Shut Down System
4: Reboot System</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Streamed Channel Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of channels that the VeriStand Engine is currently streaming to the host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Max Streamed Channels" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The maximum number of channels that the VeriStand Engine can stream to the host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Model Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the models have not completed their execution in time</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Clients" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Maximum GENs" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of stimulus profile generators instantiated by the system</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Generator Engine State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="3">
						<Description>The current state of the stimulus profile generator engine

0: Idle
1: Running
2: Stopped
3: Paused</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Watchdog Timer" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The amount of time in nanoseconds since the Watchdog Timer Loop last executed. The Watchdog Timer Loop is set to execute at a rate of 10Hz.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HS TCP Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the streaming data gets overwritten.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Host IP" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The 32-bit integer IP Address of the connected host. A zero value indicates no host is connected to the VeriStand Engine.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Trace Enabled Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether execution tracing is currently active on the RT Target.  Set to 1 to start tracing.  Set to 0 to stop tracing and send result to host (if no host is present it is logged to disk).  Set to -1 to stop tracing and write result to disk.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Detailed Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether detailed execution tracing is enabled on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="VI Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether VI execution tracing is enabled on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Trace Buffer Size" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Bytes" BitFields="3">
						<Description>Specifies the size in bytes of the execution trace buffer on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>250000</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Thread Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether thread execution tracing is enabled on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Absolute Time" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>Returns the current date and time in seconds relative to 12:00 a.m., Friday, January 1, 1904, Universal Time [01-01-1904 00:00:00]. This value is coerced from a 128-bit value to double precision, which may impact resolution.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Time - Microseconds" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="usec" BitFields="1">
						<Description>The relative system time in microseconds of the VeriStand Engine according to the iteration count and Delta T of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 41" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 42" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 43" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 44" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Iterations" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Min Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Actual Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Failure Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The failure count of current analysis settings</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Analysis State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The state of the analysis sub-system on the RT execution host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="TCP Data Packet Loss" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the VeriStand Engine fails to send a data packet to the host. A non-zero number can indicate data loss in logged data. The value is reset every time a Workspace connects to the VeriStand Engine.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop attempted to write to a waveform read session within the NI VeriStand engine and timed out.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL TCP Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop attempted to write to the TCP loop (for a host waveform stream session) and timed out.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Error Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop encountered an error.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Error Code" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The last error code encountered by the waveform processing loop.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Streamed Waveform Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of waveforms that the VeriStand Engine is currently streaming to the host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Iteration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The iteration count of the Primary Control Loop.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Last Late Iteration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The iteration count of the Primary Control Loop that last recorded a late count. If the Primary Control Loop has not recorded a late count, this value is -1.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 58" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 59" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Real-Time Sequence Command" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Internally commands the active real-time sequences with the following numeric values:
		
		0: None
		1: Stop All
		2: Abort All</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Real-Time Sequence Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of real-time sequences currently running.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 62" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 63" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 64" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 65" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 66" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 67" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 68" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 69" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 70" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 71" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 72" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 73" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 74" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 75" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 76" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 77" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 78" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 79" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 80" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 81" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 82" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 83" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 84" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 85" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 86" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 87" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 88" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 89" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 90" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 91" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="AO1 Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Loop Wakeup Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="1">
						<Description>The wakeup status of the Primary Control Loop.

0: Normal
1: Aborted
2: Asynchronous wakeup
3: Timing source error
4: Timed loop error
5: Timeout</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HD Free Space" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP-LP Overwrite" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Primary Control Loop timed out writing channel data to the Data Processing Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Data Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Data Processing Loop timed out writing channel data to the Communication Send Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Primary Control Loop reported being late</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Data Processing Loop reported being late</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Log Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The state of the logging sub-system on the RT execution host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
				</Section>
			</Target>
		</TargetSections>
		<Section Name="Aliases" TypeGUID="e11f4519-09e6-4fb0-99df-2967c4313d67">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Scales" TypeGUID="032c8aec-ce5b-6d40-06c5-5703bbc7ccee">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="System Mappings" TypeGUID="5691ea13-4544-497e-9bda-cf69dc707663">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Data Sharing Network" TypeGUID="8288dbb9-8c87-4fda-9c66-acec90c46c03">
			<Description />
			<Properties>
				<Property Name="CD Status">
					<U32>2</U32>
				</Property>
				<Property Name="DSN Dynamic Data Size">
					<I32>30</I32>
				</Property>
			</Properties>
			<Errors />
		</Section>
		<Section Name="System Initialization" TypeGUID="773b9311-3758-47fa-842f-b1c1960dabd0">
			<Description />
			<Properties>
				<Property Name="Auto Start">
					<Boolean>false</Boolean>
				</Property>
			</Properties>
			<Errors />
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/TestStimulusAPI/AutoStepTestStimulusAPI.nivstest sha256=8b7bf643dc0bfc355d5751087bd4e3db2e96d53f45ad22d5e118f07b91e04109 bytes=4595 -->
## FILE: tests/testutilities/legacy_files/TestStimulusAPI/AutoStepTestStimulusAPI.nivstest

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/TestStimulusAPI/AutoStepTestStimulusAPI.nivstest`
- sha256: `8b7bf643dc0bfc355d5751087bd4e3db2e96d53f45ad22d5e118f07b91e04109`
- bytes: 4595

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2010" Minor="0" Fix="0" Build="0" />
	<Content>Definition</Content>
	<Root Name="Stimulus Profile" TypeGUID="f24abe4b-0f2c-46f6-adfa-8336e534294d">
		<Properties>
			<Property Name="Data Logging">
				<Variant>
					<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
					<Data>AAADSwkAgAAAAAAUABJAMv////8JRmlsZSBQYXRoABRAMP////8LRGVzY3JpcHRpb24AcQDxAAAAAAAAAAIiTklfVlMgV29ya3NwYWNlIEV4ZWN1dGlvbkFQSS5sdmxpYhZMb2dGaWxlVHJpZ2dlclR5cGUuY3RsAC9AFgADBE5vbmUJSW4gTGltaXRzDU91dCBvZiBMaW1pdHMAAARUeXBlAAAWQDD/////DENoYW5uZWwgUGF0aAAAEUAKAApIaWdoIExpbWl0AAAPQAoACUxvdyBMaW1pdABlAPEAAAAAAAAAAiJOSV9WUyBXb3Jrc3BhY2UgRXhlY3V0aW9uQVBJLmx2bGliH0xvZ0ZpbGVUcmlnZ2VyQ29uZmlndXJhdGlvbi5jdGwAGkBQAAQAAgADAAQABQdUcmlnZ2VyABJAIQxSZXBsYWNlIEZpbGUAABFAAwAKRGVjaW1hdGlvbgAADkAw/////wROYW1lAAAOQDD/////BVZhbHVlAFMA8QAAAAAAAAACIk5JX1ZTIFdvcmtzcGFjZSBFeGVjdXRpb25BUEkubHZsaWIPTG9nUHJvcGVydHkuY3RsABhAUAACAAkACghQcm9wZXJ0eQAAHEBAAAH/////AAsPRmlsZSBQcm9wZXJ0aWVzABRAMP////8LQ3VzdG9tIE5hbWUAFkAw/////wxDdXN0b20gR3JvdXAAABhAQAAB/////wALClByb3BlcnRpZXMAAGkA8QAAAAAAAAACIk5JX1ZTIFdvcmtzcGFjZSBFeGVjdXRpb25BUEkubHZsaWIbTG9nQ2hhbm5lbENvbmZpZ3VyYXRpb24uY3RsACJAUAAEAAMADQAOAA8OTG9nQ2hhbm5lbEluZm8AABZAQAAB/////wAQCENoYW5uZWxzAAByAPEAAAAAAAAAAiJOSV9WUyBXb3Jrc3BhY2UgRXhlY3V0aW9uQVBJLmx2bGliGExvZ0ZpbGVDb25maWd1cmF0aW9uLmN0bAAuQFAABwAAAAEABgAHAAgADAARFExvZ0ZpbGVDb25maWd1cmF0aW9uAAAkQEAAAf////8AEhZMb2dnaW5nIENvbmZpZ3VyYXRpb25zAAABABMAAAAAAAAAAA==</Data>
				</Variant>
			</Property>
			<Property Name="Header Subpanel VI">
				<DependentFile Type="Relative" Path="Stimulus Profile Editor Headers\Stimulus Profile Template Header.vi">
					<Version />
					<RTDestination />
					<SupportedTarget />
					<MD5 />
				</DependentFile>
			</Property>
			<Property Name="Ignore Calibration Errors">
				<Boolean>false</Boolean>
			</Property>
		</Properties>
		<Errors />
		<Section Name="Controller/GEN001" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray>
						<Elem>User0</Elem>
					</StringArray>
				</Property>
				<Property Name="Execution Target">
					<String>Controller</String>
				</Property>
			</Properties>
			<Errors />
			<Section Name="Ramp 0" TypeGUID="d3a0c118-0577-4aae-9d76-9fdcf7c75eb6">
				<Description>Ramp to 19.0 TBD at 1.0 TBD / sec</Description>
				<Properties>
					<Property Name="Step Type">
						<String>Ramp</String>
					</Property>
					<Property Name="End Point">
						<Double>19</Double>
					</Property>
					<Property Name="Mode">
						<String>Rate</String>
					</Property>
					<Property Name="Rate">
						<Double>1</Double>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Dwell 1" TypeGUID="376cd3a2-af99-4855-a664-842d3500812d">
				<Description>Dwell for [00:00:10.000] seconds</Description>
				<Properties>
					<Property Name="Step Type">
						<String>Dwell</String>
					</Property>
					<Property Name="Time">
						<Double>10</Double>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Controller/GEN002" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String>Controller</String>
				</Property>
			</Properties>
			<Errors />
		</Section>
		<Section Name="Controller/GEN003" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String>Controller</String>
				</Property>
			</Properties>
			<Errors />
		</Section>
		<Section Name="Controller/GEN004" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String>Controller</String>
				</Property>
			</Properties>
			<Errors />
		</Section>
		<Section Name="Controller/GEN005" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String>Controller</String>
				</Property>
			</Properties>
			<Errors />
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/TestStimulusAPI/TestStimulusAPI.nivsproj sha256=553153b8fa2e34945ed0b8d493ac330c50ae81dee034dde1d79f2fef778faf5d bytes=11600 -->
## FILE: tests/testutilities/legacy_files/TestStimulusAPI/TestStimulusAPI.nivsproj

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/TestStimulusAPI/TestStimulusAPI.nivsproj`
- sha256: `553153b8fa2e34945ed0b8d493ac330c50ae81dee034dde1d79f2fef778faf5d`
- bytes: 11600

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2012" Minor="0" Fix="0" Build="1" />
	<Content>Definition</Content>
	<Root Name="TestStimulusAPI" TypeGUID="d9313aae-3554-45e5-93f3-86454275d4f2">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>TestStimulusAPI</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.0</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3351079555.6588254</Double>
			</Property>
		</Properties>
		<Errors />
		<Section Name="System Definition File" TypeGUID="b9227a5b-2770-4a62-8621-ac414d4124fb">
			<Description />
			<Properties />
			<Errors />
			<Section Name="TestStimulusAPI.nivssdf" TypeGUID="3a41ca74-36ec-4aff-9219-9d05c8f91208">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="TestStimulusAPI.nivssdf">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5>344d525fd2179a022ade62bf8cb3fe97</MD5>
						</DependentFile>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Workspace" TypeGUID="bc98486f-7b49-4949-9504-949cbe254c85">
			<Description />
			<Properties>
				<Property Name="User Accounts">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAAAzwkAgAAAAAAFAA5AMP////8ETmFtZQAAEkAw/////whQYXNzd29yZAAADkAw/////wVHcm91cABMAPEAAAAAAAAAAhhTZWMgQWRtaW5pc3RyYXRpb24ubHZsaWIMVXNlclR5cGUuY3RsAB5AUAADAAAAAQACDFVzZXIgQWNjb3VudAAAGkBAAAH/////AAMNVXNlciBBY2NvdW50cwABAAQAAAABAAAADUFkbWluaXN0cmF0b3IAAAAAAAAADkFkbWluaXN0cmF0aW9uAAAAAA==</Data>
					</Variant>
				</Property>
				<Property Name="Group Accounts">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAAA7QkAgAAAAAAFAA5AMP////8ETmFtZQAADEAhB0Jvb2xlYW4AGEBAAAH/////AAELUGVybWlzc2lvbnMASwDxAAAAAAAAAAIYU2VjIEFkbWluaXN0cmF0aW9uLmx2bGliDUdyb3VwVHlwZS5jdGwAHEBQAAIAAAACDUdyb3VwIEFjY291bnQAHEBAAAH/////AAMOR3JvdXAgQWNjb3VudHMAAAEABAAAAAIAAAAOQWRtaW5pc3RyYXRpb24AAAANAQEBAQEBAQEBAQEBAQAAAAhPcGVyYXRvcgAAAA0BAAAAAQABAQAAAAAAAAAAAA==</Data>
					</Variant>
				</Property>
				<Property Name="Tools Menu Items">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAAD2AkAgAAAAAAIAA5AMP////8ETmFtZQAAEkAw/////whGdW5jdGlvbgAAYQDxAAAAAAAAAAETVG9vbGJhciBCdXR0b25zLmN0bABFQBYAAwROb25lF1N0aW11bHVzIFByb2ZpbGUgRWRpdG9yC0RhdGEgVmlld2VyAAAOVG9vbGJhciBCdXR0b24AAVMA8QAAAAAAAAABH2VudW1fVXNlciBBZG1pbiBQZXJtaXNzaW9ucy5jdGwBK0AWAA0HRGVmYXVsdA5BZG1pbmlzdHJhdGlvbhdDaGFubmVsIFNjYWxpbmcgVXRpbGl0eRFBZGQgRGlzcGxheSBJdGVtcxNDaGFuZ2UgVXNlciBQcm9maWxlI0VkaXQgU3RpbXVsdXMgUHJvZmlsZSBFZGl0b3IgSGVhZGVyGkVkaXQgRGlzcGxheSBJdGVtIFNldHRpbmdzG01vZGVsIFBhcmFtZXRlciBDYWxpYnJhdGlvbhJSdW50aW1lIEFsYXJtIEVkaXQPRWRpdCBUb29scyBNZW51FkVkaXQgRW5naW5lIENvbXBvbmVudHMaQ29uZmlndXJlIFZpc2libGUgQ2hhbm5lbHMNRmF1bHQgTWFuYWdlcgAAClBlcm1pc3Npb24AABpAMv////8QQ3VzdG9tIFRvb2wgUGF0aAAAaQDxxyxnxAAAAAIRTklWU19TaGFyZWQubHZsaWINUGF0aCB0eXBlLmN0bABBQBYAAwhBYnNvbHV0ZQhSZWxhdGl2ZQxUb0FwcERhdGFEaXIAABVDdXN0b20gVG9vbCBQYXRoIFR5cGUAYwDxAAAAAAAAAAIaTklWU1Byb2pfRmlsZW1hbmFnZXIubHZsaWIZVG9vbHMgTWVudSBJdGVtcyBUeXBlLmN0bAAmQFAABgAAAAEAAgADAAQABQ9Ub29scyBNZW51IEl0ZW0AHkBAAAH/////AAYQVG9vbHMgTWVudSBJdGVtcwAAAQAHAAAAAwAAAB5TdGltdWx1cyBQcm9maWxlIEVkaXRvciAtIFN0ZXAAAAAVVGVzdCBFZGl0b3IgKFN0ZXApLnZpAAEAAFBUSDAAAAAEAAAAAAAAAAAAH1N0aW11bHVzIFByb2ZpbGUgRWRpdG9yIC0gVGFibGUAAAAWVGVzdCBFZGl0b3IgKFRhYmxlKS52aQAAAABQVEgwAAAABAAAAAAAAAAAACBTdGltdWx1cyBQcm9maWxlIFNlcXVlbmNlIEVkaXRvcgAAABZUZXN0IEVkaXRvciAoQmF0Y2gpLnZpAAAAAFBUSDAAAAAEAAAAAAAAAAAAAA==</Data>
					</Variant>
				</Property>
				<Property Name="Engine Components">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAABfgkAgAAAAAAIABJAMP////8IRnVuY3Rpb24AAA5AIQlTaG93SXRlbT8AL0AWAAMETm9uZQxXYWl0Q29tcGxldGUIV2FpdFN5bmMAAApMYXVuY2hUeXBlAAARQAMAC1N5bmNUaW1lb3V0ABpAMv////8QQ3VzdG9tIFRvb2wgUGF0aAAAaQDxxyxnxAAAAAIRTklWU19TaGFyZWQubHZsaWINUGF0aCB0eXBlLmN0bABBQBYAAwhBYnNvbHV0ZQhSZWxhdGl2ZQxUb0FwcERhdGFEaXIAABVDdXN0b20gVG9vbCBQYXRoIFR5cGUAaQDxAAAAAAAAAAIaTklWU1Byb2pfRmlsZW1hbmFnZXIubHZsaWIZRW5naW5lIENvbXBvbmVudCBUeXBlLmN0bAAsQFAABgAAAAEAAgADAAQABRVFbmdpbmUgQ29tcG9uZW50IEl0ZW0AHkBAAAH/////AAYRRW5naW5lIENvbXBvbmVudHMAAQAHAAAAAAAAAAA=</Data>
					</Variant>
				</Property>
				<Property Name="Hidden Channels">
					<StringArray />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Screens" TypeGUID="cdfadfe0-c84a-4268-a677-4f2f3525465e">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="TestStimulusAPI.nivsscreen">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5>5186d85ed828ac5084ab41b98274d80b</MD5>
						</DependentFile>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Services" TypeGUID="736a951c-d9c8-457f-96a9-cd0ef16011a5">
			<Description />
			<Properties />
			<Errors />
			<Section Name="Model Parameter Manager" TypeGUID="cc686646-9933-410d-a553-6308e6e06897">
				<Description />
				<Properties>
					<Property Name="Function">
						<String>Model Parameter Manager.vi</String>
					</Property>
					<Property Name="Path">
						<DependentFile Type="Absolute" Path="">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
						</DependentFile>
					</Property>
					<Property Name="Sync Options">
						<String>WaitSync</String>
					</Property>
					<Property Name="Sync Timeout">
						<I32>10000</I32>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Profiles" TypeGUID="c3bd79ec-3336-4b06-868e-3217c640edd5">
			<Description />
			<Properties />
			<Errors />
			<Section Name="AutoStepTestStimulusAPI.nivstest" TypeGUID="abf90cfe-5857-440d-9231-18a95fb3d451">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="AutoStepTestStimulusAPI.nivstest">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5>c7b8ec8453fc69d8d8b72a76181e003d</MD5>
						</DependentFile>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Calibration" TypeGUID="38433223-24A0-4b32-9339-370EC5AA31B4">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Alarm Responses" TypeGUID="3b1ab560-d77a-41f2-adb4-0c0250b010b3">
			<Description />
			<Properties />
			<Errors />
			<Section Name="Response High" TypeGUID="99267DF5-8C59-4AAC-B020-7591F4886206">
				<Description />
				<Properties>
					<Property Name="Show Dialog">
						<Boolean>true</Boolean>
					</Property>
					<Property Name="Play Sound">
						<String>Disabled</String>
					</Property>
					<Property Name="Wave File">
						<DependentFile Type="Absolute" Path="">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
						</DependentFile>
					</Property>
					<Property Name="Log Alarms">
						<String>Enabled</String>
					</Property>
					<Property Name="Log File">
						<String>Logs\Alarm Log.txt</String>
					</Property>
					<Property Name="Max Priority">
						<U32>10</U32>
					</Property>
					<Property Name="Min Priority">
						<U32>0</U32>
					</Property>
					<Property Name="Enable Response">
						<Boolean>true</Boolean>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Response Med" TypeGUID="99267DF5-8C59-4AAC-B020-7591F4886206">
				<Description />
				<Properties>
					<Property Name="Show Dialog">
						<Boolean>true</Boolean>
					</Property>
					<Property Name="Play Sound">
						<String>Disabled</String>
					</Property>
					<Property Name="Wave File">
						<DependentFile Type="Absolute" Path="">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
						</DependentFile>
					</Property>
					<Property Name="Log Alarms">
						<String>Enabled</String>
					</Property>
					<Property Name="Log File">
						<String>Logs\Alarm Log.txt</String>
					</Property>
					<Property Name="Max Priority">
						<U32>21</U32>
					</Property>
					<Property Name="Min Priority">
						<U32>11</U32>
					</Property>
					<Property Name="Enable Response">
						<Boolean>true</Boolean>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Response Low" TypeGUID="99267DF5-8C59-4AAC-B020-7591F4886206">
				<Description />
				<Properties>
					<Property Name="Show Dialog">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Play Sound">
						<String>Disabled</String>
					</Property>
					<Property Name="Wave File">
						<DependentFile Type="Absolute" Path="">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
						</DependentFile>
					</Property>
					<Property Name="Log Alarms">
						<String>Enabled</String>
					</Property>
					<Property Name="Log File">
						<String>Logs\Alarm Log.txt</String>
					</Property>
					<Property Name="Max Priority">
						<U32>31</U32>
					</Property>
					<Property Name="Min Priority">
						<U32>22</U32>
					</Property>
					<Property Name="Enable Response">
						<Boolean>true</Boolean>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Custom Files" TypeGUID="9e2cb626-3583-4345-aeb6-b9fead6ec565">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Dependencies" TypeGUID="e5b093fa-a709-4df2-807e-a403422ba675">
			<Description />
			<Properties />
			<Errors />
			<Section Name="TestStimulusAPI.nivssdf [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\TestStimulusAPI\TestStimulusAPI.nivssdf]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\TestStimulusAPI\TestStimulusAPI.nivssdf</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="TestStimulusAPI.nivsscreen [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\TestStimulusAPI\TestStimulusAPI.nivsscreen]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\TestStimulusAPI\TestStimulusAPI.nivsscreen</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="AutoStepTestStimulusAPI.nivstest [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\TestStimulusAPI\AutoStepTestStimulusAPI.nivstest]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\TestStimulusAPI\AutoStepTestStimulusAPI.nivstest</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/TestStimulusAPI/TestStimulusAPI.nivsscreen sha256=e5faa43f52874e34e38f6c5a5d60cd7d436af3a64d906e3a268baf5dd9e2caa8 bytes=6504 -->
## FILE: tests/testutilities/legacy_files/TestStimulusAPI/TestStimulusAPI.nivsscreen

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/TestStimulusAPI/TestStimulusAPI.nivsscreen`
- sha256: `e5faa43f52874e34e38f6c5a5d60cd7d436af3a64d906e3a268baf5dd9e2caa8`
- bytes: 6504

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2010" Minor="0" Fix="0" Build="0" />
	<Content>Definition</Content>
	<Root Name="WorkspaceScreen" TypeGUID="2e39a440-e372-11de-8a39-0800200c9a66">
		<Properties>
			<Property Name="Screen Data">
				<Variant>
					<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
					<Data>AAAPiwkAgAAAAABYABRAMP////8LVGVtcGxhdGUgVkkAEUADAApQb3NpdGlvbiBYAAARQAMAClBvc2l0aW9uIFkAABBAMP////8GQ3VzdG9tAAAUQCEOU2hvdyBUaXRsZSBCYXIAAAlAAwACSUQAABJAIQ1BbHdheXMgT24gVG9wABJAIQxBbGxvdyBSZXNpemUAABRAIQ5BbGxvdyBNaW5pbWl6ZQAAEEAhC0FsbG93IENsb3NlABRAIQ5TaXplIHRvIFNjcmVlbgAAD0ADAAlTY3JlZW4uSUQAGUAWAAIGTm9ybWFsA05ldwAABVN0YXRlAA5AMP////8FVGl0bGUACUACAANbMF0ACUACAANbMV0ACUACAANbMl0ACUACAANbM10AHEBQAAQADgAPABAAEQ1XaW5kb3cgQm91bmRzABFACAALQ2hhbm5lbCBSZWYADkAw/////wRVbml0AAAUQCEORGVmYXVsdCBVbml0cz8AABJAIQxGbGFzaCBMaW1pdD8AAA1ABwAHQ29sb3IgMQANQAcAB0NvbG9yIDIADUAHAAdDb2xvciAzAA1ABwAHQ29sb3IgNAAPQAcACUJjayBDb2xvcgARQAcACkZvcmUgQ29sb3IAAA1ACgAHTGltaXQgMQANQAoAB0xpbWl0IDIADUAKAAdMaW1pdCAzAA1ACgAHTGltaXQgNAATQAMADExpbWl0IE1vZGUgMQAAE0ADAAxMaW1pdCBNb2RlIDIAABNAAwAMTGltaXQgTW9kZSAzAAATQAMADExpbWl0IE1vZGUgNAAAFUADAA9TY2FsZSBQcmVjaXNpb24AD0AKAAlTY2FsZSBNaW4AD0AKAAlTY2FsZSBNYXgADUADAAZGb3JtYXQAAA9AAwAJUHJlY2lzaW9uABVAAwAPQmFja2dyb3VuZCBUeXBlABFAAwALVmFyaWFibGUgSUQAEEBAAAH/////ACsDSURzABRAMP////8LVmFyaWFibGUgSUQAEkBAAAH/////AC0FVW5pdHMAFEBAAAH/////AC0GTGFiZWxzAAATQAoADFNjYWxlIEZhY3RvcgAAE0AKAAxTY2FsZSBPZmZzZXQAABFABwALVmFyaWFibGUgSUQAGkBAAAH/////ADIMWVNjYWxlIEluZGV4AAANQAUABkZvcm1hdAAAD0AFAAlQcmVjaXNpb24ACUAFAANGaXQADkAw/////wVMYWJlbAAWQCERVXNlIERlZmF1bHQgTGFiZWwAEkAhDUxhYmVsIFZpc2libGUACUAKAANNaW4ACUAKAANNYXgASwDxAAAAAAAAAAEgY2x1c3Rlcl9HcmFwaCBTY2FsZSBTZXR0aW5ncy5jdGwAIkBQAAgANAA1ADYANwA4ADkAOgA7BlhTY2FsZQAAFEBAAAH/////ADwHWVNjYWxlcwAPQAUACUJhciBTdHlsZQANQAIAB0ZpbGwgVG8AE0AHAAxGaWxsL1B0Q29sb3IAABFABQAKTGluZSBTdHlsZQAAEUAFAApMaW5lIFdpZHRoAAALQAcABUNvbG9yAA1ABQAGSW50ZXJwAAARQAUAC1BvaW50IFN0eWxlAEgA8QAAAAAAAAABH2NsdXN0ZXJfR3JhcGggUGxvdCBTZXR0aW5ncy5jdGwAIEBQAAgAPgA/AEAAQQBCAEMARABFBFBsb3QAABJAQAAB/////wBGBVBsb3RzABNACgANVXBkYXRlIFBlcmlvZAAVQAoADkhpc3RvcnkgTGVuZ3RoAAAUQHAACAAAAAIAAAZNeS5SZWYAABBAIQtJcyBDb250cm9sPwAWQDD/////DENoYW5uZWwgUGF0aAAAGkBAAAH/////AEwNQ2hhbm5lbCBQYXRocwAQQFMLQ3VzdG9tIERhdGEAqwDxxieWWAAAAAEgY2x1c3Rlcl9TY3JlZW4gSXRlbSBTZXR0aW5ncy5jdGwAgkBQADYAAAABAAIAAwAEAAUABgAHAAgACQAKAAsADAANABIAEwAUABUAFgAXABgAGQAaABsAHAAdAB4AHwAgACEAIgAjACQAJQAmACcAKAApACoALAAuAC8AMAAxADMAPAA9AEcASABJAEoASwBNAE4LU2NyZWVuIEl0ZW0AEkBAAAH/////AE8FSXRlbXMADkAw/////wROYW1lAAAUQDD/////C0Rlc2NyaXB0aW9uAVMA8QAAAAAAAAABH2VudW1fVXNlciBBZG1pbiBQZXJtaXNzaW9ucy5jdGwBK0AWAA0HRGVmYXVsdA5BZG1pbmlzdHJhdGlvbhdDaGFubmVsIFNjYWxpbmcgVXRpbGl0eRFBZGQgRGlzcGxheSBJdGVtcxNDaGFuZ2UgVXNlciBQcm9maWxlI0VkaXQgU3RpbXVsdXMgUHJvZmlsZSBFZGl0b3IgSGVhZGVyGkVkaXQgRGlzcGxheSBJdGVtIFNldHRpbmdzG01vZGVsIFBhcmFtZXRlciBDYWxpYnJhdGlvbhJSdW50aW1lIEFsYXJtIEVkaXQPRWRpdCBUb29scyBNZW51FkVkaXQgRW5naW5lIENvbXBvbmVudHMaQ29uZmlndXJlIFZpc2libGUgQ2hhbm5lbHMNRmF1bHQgTWFuYWdlcgAAClBlcm1pc3Npb24AAAxAIQdMb2FkZWQ/ABRAIQ9BbHdheXMgVmlzaWJsZT8AVwDxAAAAAAAAAAEkY2x1c3Rlcl9FbnRpcmUgU2NyZWVuIERlZmluaXRpb24uY3RsACpAUAAKAFAAUQBSAAUAAQACAAYAUwBUAFULU2NyZWVuLkRhdGEAJkBAAAH/////AFYZU2NyZWVuIEl0ZW0gQ2x1c3RlciBBcnJheQABAFcAAAABAAAABQAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAABkEAAAAAAAAAAU+AAAAAAALU3lzdGVtIFRpbWUCgAGGA0gBwwAAABAAAAXmAAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACpgADRAAAAAAEAAAAmQ29udHJvbGxlci9TeXN0ZW0gQ2hhbm5lbHMvU3lzdGVtIFRpbWUJAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAAA+cAAAAAAAAAAU+AAAAAAAWR2VuZXJhdG9yIEVuZ2luZSBTdGF0ZQG4AYYCgAHDAAAAKwABe8IAAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKngASMAAAAAAQAAADFDb250cm9sbGVyL1N5c3RlbSBDaGFubmVscy9HZW5lcmF0b3IgRW5naW5lIFN0YXRlCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAbTnVtZXJpYyBDb250cm9sIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAAADgBAAAAAAAABT4AAAAAAAhDaGFubmVsQgDwAYYBuAHDAAAAhQABicEAAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKoQAUIBAAAAAQAAAAhDaGFubmVsQgkAgAAAAAABAAQAAAABAAAAAAAAAAAAG051bWVyaWMgQ29udHJvbCAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAAAJ0AQAAAAAAAAU+AAAAAAAIQ2hhbm5lbEEAHgGGAOYBwwAAAIQAAYnAAAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACqkAGYAQAAAAEAAAAIQ2hhbm5lbEEJAIAAAAAAAQAEAAAAAQAAAAAAAAAAABFHcmFwaCAtIFNpbXBsZS52aQAAAAAAAAAAAAAAAAAAAA0dAQEAAAAAAAU+AAAAAAAFR3JhcGgAHgBQAtABh///////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQFkAAAAAAAAAAAAAAAAAAQAAAAAAAAACAAAA0gAAANMAAAACAAAAAAAAAAAAAAACAAAACENoYW5uZWxBAAAACENoYW5uZWxCP/AAAAAAAAAAAAAAAAAAAAAAAAAGAAIAAAAAAAAAAAAAAAAAAEA0AAAAAAAAAAAAAQkAAgAAAAAAAMAQ4ml8yK70QDHHZaDN1EMAAAACAP//AP/2AAABAP/2AAIBAP//AP9CQgAAAP9CQgICP8mZmZmZmZpANAAAAAAAAKrwAMoAAAAAAgAAAAhDaGFubmVsQQAAAAhDaGFubmVsQgkAgAAAAAABAAQAAAABAAAAAAAAAAAADEVtcHR5IFNjcmVlbgAAAAAAAAU+AAAAAAAAAAAAAAABAAAAAAA=</Data>
				</Variant>
			</Property>
			<Property Name="Screen Order">
				<I32Array>
					<Elem>1342</Elem>
				</I32Array>
			</Property>
			<Property Name="EscapeEnabled">
				<Boolean>false</Boolean>
			</Property>
			<Property Name="ShowPropPageOnDrop">
				<Boolean>true</Boolean>
			</Property>
			<Property Name="Workspace Loc and Size Left">
				<U16>138</U16>
			</Property>
			<Property Name="Workspace Loc and Size Top">
				<U16>114</U16>
			</Property>
			<Property Name="Workspace Loc and Size Right">
				<U16>1126</U16>
			</Property>
			<Property Name="Workspace Loc and Size Bottom">
				<U16>774</U16>
			</Property>
		</Properties>
		<Errors />
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/TestStimulusAPI/TestStimulusAPI.nivssdf sha256=d6b7ef363fe91e8f53611bf4cf11709112e6b26734d44ec48ae1736a7e7c3650 bytes=98027 -->
## FILE: tests/testutilities/legacy_files/TestStimulusAPI/TestStimulusAPI.nivssdf

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/TestStimulusAPI/TestStimulusAPI.nivssdf`
- sha256: `d6b7ef363fe91e8f53611bf4cf11709112e6b26734d44ec48ae1736a7e7c3650`
- bytes: 98027

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2010" Minor="0" Fix="0" Build="4" />
	<Content>Definition</Content>
	<Root Name="TestStimulusAPI" TypeGUID="03D3BA22-1485-13A6-56BD17DA950CCD00">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>TestStimulusAPI</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.9</String>
			</Property>
			<Property Name="Creator">
				<String>Administrator</String>
			</Property>
			<Property Name="Creation Date">
				<Double>3324568431.140625</Double>
			</Property>
		</Properties>
		<Errors />
		<TargetSections Name="Targets Section" TypeGUID="eb379619-68d7-4d81-be90-c0bc511cdc10">
			<Description />
			<Properties />
			<Errors />
			<Target Name="Controller" TypeGUID="775504BB-1485-13A6-56755DBF2C326980">
				<Description />
				<Properties>
					<Property Name="IP Address">
						<String>localhost</String>
					</Property>
					<Property Name="Control Rate">
						<Double>1</Double>
					</Property>
					<Property Name="HS Port">
						<I32>2040</I32>
					</Property>
					<Property Name="LS Port">
						<I32>2050</I32>
					</Property>
					<Property Name="HS Port Timeout">
						<I32>1000</I32>
					</Property>
					<Property Name="LS Port Timeout">
						<I32>1000</I32>
					</Property>
					<Property Name="Control Loop Processor">
						<I32>-2</I32>
					</Property>
					<Property Name="Streamed Channels">
						<I32>512</I32>
					</Property>
					<Property Name="Stream Rate">
						<I32>1</I32>
					</Property>
					<Property Name="Secondary Control Loop Processor">
						<I32>-2</I32>
					</Property>
					<Property Name="OS">
						<String>Windows</String>
					</Property>
					<Property Name="Engine Rate">
						<Double>100</Double>
					</Property>
					<Property Name="Execution Mode">
						<U32>0</U32>
					</Property>
					<Property Name="TS_Custom_Dev">
						<String />
					</Property>
					<Property Name="daq">
						<Variant>
							<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
							<Data>AAAAYwkAgAAAAAADABRAMP////8KREFRIERldmljZQAAJ0AHACBQcmltYXJ5IENvbnRyb2wgTG9vcCByYXRlICh1c2VjKQAAEEBQAAIAAAABBGRhdGEAAAEAAgAAAAAAACcQAAAAAA==</Data>
						</Variant>
					</Property>
					<Property Name="Filter Watchdog Errors">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Filter DAQ Errors">
						<Boolean>false</Boolean>
					</Property>
				</Properties>
				<Errors />
				<Section Name="System Channels" TypeGUID="03D3B753-1485-13A6-56B10ED0820CF410">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="Actual Loop Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Hz" BitFields="1">
						<Description>The execution rate of the Primary Control Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100000</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Index" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>The compiled index of the current procedure step</Description>
						<Properties>
							<Property Name="ID">
								<I32>100001</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The decimation of the Data Processing Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100002</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Time" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>The relative system time of the VeriStand Engine according to the iteration count and Delta T of the Primary Control Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100003</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100004</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="DAQ Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The last reported error code from a DAQmx function call. The value zero indicates no error has occurred.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100005</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Delta T" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>The period in seconds of the Primary Control Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100006</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Compiler Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100007</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 1" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>An internal register used by procedures to maintain the stack location when a procedure is preempted by a higher priorty procedure</Description>
						<Properties>
							<Property Name="ID">
								<I32>100008</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 2" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>An internal register used by procedures to maintain the stack location when a procedure is preempted by a higher priorty procedure</Description>
						<Properties>
							<Property Name="ID">
								<I32>100009</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 3" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>An internal register used by procedures to maintain the stack location when a procedure is preempted by a higher priorty procedure</Description>
						<Properties>
							<Property Name="ID">
								<I32>100010</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Resume Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100011</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 4" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>An internal register used by procedures to maintain the stack location when a procedure is preempted by a higher priorty procedure</Description>
						<Properties>
							<Property Name="ID">
								<I32>100012</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 5" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>An internal register used by procedures to maintain the stack location when a procedure is preempted by a higher priorty procedure</Description>
						<Properties>
							<Property Name="ID">
								<I32>100013</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 6" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>An internal register used by procedures to maintain the stack location when a procedure is preempted by a higher priorty procedure</Description>
						<Properties>
							<Property Name="ID">
								<I32>100014</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>The ID of the alarm that has tripped</Description>
						<Properties>
							<Property Name="ID">
								<I32>100015</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>The ID of the alarm that has tripped</Description>
						<Properties>
							<Property Name="ID">
								<I32>100016</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>The ID of the alarm that has tripped</Description>
						<Properties>
							<Property Name="ID">
								<I32>100017</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>The value of the channel that tripped the alarm</Description>
						<Properties>
							<Property Name="ID">
								<I32>100018</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>The value of the channel that tripped the alarm</Description>
						<Properties>
							<Property Name="ID">
								<I32>100019</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>The value of the channel that tripped the alarm</Description>
						<Properties>
							<Property Name="ID">
								<I32>100020</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="RT Engine Build" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>A value representing the build number of the NI VeriStand Engine</Description>
						<Properties>
							<Property Name="ID">
								<I32>100021</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Loop Duration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The duration of the Primary Control Loop in nanoseconds</Description>
						<Properties>
							<Property Name="ID">
								<I32>100022</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Loop Duration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The duration of the Data Processing Loop in nanoseconds</Description>
						<Properties>
							<Property Name="ID">
								<I32>100023</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Command" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="3">
						<Description>Internally commands the RT system with the following numeric values:

0: None
1: Restart System
2: Reset System
3: Shut Down System
4: Reboot System</Description>
						<Properties>
							<Property Name="ID">
								<I32>100024</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Streamed Channel Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of channels that the VeriStand Engine is currently streaming to the host</Description>
						<Properties>
							<Property Name="ID">
								<I32>100025</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Max Streamed Channels" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The maximum number of channels that the VeriStand Engine can stream to the host</Description>
						<Properties>
							<Property Name="ID">
								<I32>100026</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Model Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the models have not completed their execution in time</Description>
						<Properties>
							<Property Name="ID">
								<I32>100027</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Clients" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100028</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Maximum GENs" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of stimulus profile generators instantiated by the system</Description>
						<Properties>
							<Property Name="ID">
								<I32>100029</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Generator Engine State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The current state of the stimulus profile generator engine

0: Idle
1: Running
2: Stopped
3: Paused</Description>
						<Properties>
							<Property Name="ID">
								<I32>100030</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Watchdog Timer" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The amount of time in nanoseconds since the Watchdog Timer Loop last executed. The Watchdog Timer Loop is set to execute at a rate of 10Hz.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100031</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HS TCP Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the streaming data gets overwritten.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100032</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Host IP" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The 32-bit integer IP Address of the connected host. A zero value indicates no host is connected to the VeriStand Engine.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100033</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Trace Enabled Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100034</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Detailed Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100035</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="VI Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100036</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Trace Buffer Size" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100037</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Thread Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100038</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 39" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100039</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 40" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100040</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 41" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100041</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 42" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100042</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 43" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100043</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 44" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100044</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Iterations" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100045</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Min Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100046</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Actual Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100047</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Failure Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The failure count of current analysis settings</Description>
						<Properties>
							<Property Name="ID">
								<I32>100048</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Analysis State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The state of the analysis sub-system on the RT execution host</Description>
						<Properties>
							<Property Name="ID">
								<I32>100049</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="TCP Data Packet Loss" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the VeriStand Engine fails to send a data packet to the host. A non-zero number can indicate data loss in logged data. The value is reset every time a Workspace connects to the VeriStand Engine.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100050</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 51" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100051</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 52" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100052</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 53" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100053</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 54" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100054</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 55" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100055</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 56" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100056</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 57" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100057</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 58" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100058</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 59" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100059</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 60" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100060</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 61" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100061</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 62" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100062</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 63" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100063</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 64" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100064</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 65" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100065</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 66" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100066</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 67" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100067</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 68" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100068</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 69" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100069</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 70" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100070</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 71" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100071</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 72" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100072</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 73" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100073</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 74" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100074</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 75" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100075</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 76" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100076</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 77" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100077</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 78" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100078</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 79" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100079</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 80" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100080</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 81" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100081</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 82" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100082</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 83" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100083</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 84" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100084</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 85" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100085</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 86" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100086</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 87" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100087</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 88" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100088</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 89" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100089</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 90" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100090</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 91" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100091</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="AO1 Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100092</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Loop Wakeup Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="1">
						<Description>The wakeup status of the Primary Control Loop.

0: Normal
1: Aborted
2: Asynchronous wakeup
3: Timing source error
4: Timed loop error
5: Timeout</Description>
						<Properties>
							<Property Name="ID">
								<I32>100093</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HD Free Space" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100094</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP-LP Overwrite" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Primary Control Loop timed out writing channel data to the Data Processing Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100095</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Data Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Data Processing Loop timed out writing channel data to the Communication Send Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100096</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Primary Control Loop reported being late</Description>
						<Properties>
							<Property Name="ID">
								<I32>100097</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Data Processing Loop reported being late</Description>
						<Properties>
							<Property Name="ID">
								<I32>100098</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Log Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>The state of the logging sub-system on the RT execution host</Description>
						<Properties>
							<Property Name="ID">
								<I32>100099</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
				</Section>
				<Section Name="Hardware" TypeGUID="775504AB-1485-13A6-560018C1F4E3EEE1">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Chassis" TypeGUID="03D3BACD-1485-13A6-56E99D97B7543BAF">
						<Description />
						<Properties>
							<Property Name="Chassis master active edge">
								<I32>0</I32>
							</Property>
							<Property Name="Chassis master clock source">
								<I32>0</I32>
							</Property>
							<Property Name="Chassis master export clock on line">
								<I32>0</I32>
							</Property>
							<Property Name="Chassis master export sample clock">
								<I32>0</I32>
							</Property>
							<Property Name="Chassis master slope">
								<I32>0</I32>
							</Property>
							<Property Name="Chassis master trigger line">
								<I32>0</I32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Timing and Sync" TypeGUID="03D3BAED-1485-13A6-56E20B50F6E06D94">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="DAQ" TypeGUID="77550612-1485-13A6-56570AB5032158E9">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="FPGA" TypeGUID="03D3B659-1485-13A6-5652D8A07328ECB7">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="Data Sharing" TypeGUID="d56f3ac1-7b2c-422c-9d11-fd9cc7abf2a5">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="XNET" TypeGUID="6b693e6d-67b1-40b8-8108-4a4cc3147721">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
								</Property>
							</Properties>
							<Errors />
							<Section Name="LIN" TypeGUID="c9c30728-42cb-4dc3-b054-b80e7a54e833">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="FlexRay" TypeGUID="e33fae90-03f1-4f76-b2f1-6eb8fcac2676">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="CAN" TypeGUID="6c5bb91f-0da7-407d-aefc-acbe49c768df">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
					</Section>
				</Section>
				<Section Name="Stimulus" TypeGUID="03D3B7FF-1485-13A6-56B2328F9511AC8B">
					<Description />
					<Properties>
						<Property Name="Analysis Buffer Size">
							<I32>10000</I32>
						</Property>
						<Property Name="Analysis Result Size">
							<I32>5000</I32>
						</Property>
						<Property Name="Aux Buffer Size">
							<I32>20000</I32>
						</Property>
						<Property Name="Max Gen Maps">
							<I32>256</I32>
						</Property>
						<Property Name="Max Steps">
							<I32>128</I32>
						</Property>
					</Properties>
					<Errors />
					<Section Name="GEN001" TypeGUID="03D3B80E-1485-13A6-56528B60DC00DC89">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="GEN001 State" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100100</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100101</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100102</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100103</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100104</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100105</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100106</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100107</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100108</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100109</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100110</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100111</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100112</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100113</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100114</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100115</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100116</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100117</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100118</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100119</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
					</Section>
					<Section Name="GEN002" TypeGUID="03D3B80E-1485-13A6-56528B60DC00DC89">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="GEN002 State" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100120</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100121</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100122</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100123</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100124</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100125</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100126</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100127</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100128</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100129</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100130</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100131</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100132</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100133</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100134</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100135</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100136</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100137</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100138</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100139</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
					</Section>
					<Section Name="GEN003" TypeGUID="03D3B80E-1485-13A6-56528B60DC00DC89">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="GEN003 State" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100140</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100141</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100142</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100143</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100144</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100145</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100146</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100147</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100148</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100149</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100150</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100151</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100152</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100153</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100154</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100155</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100156</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100157</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100158</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100159</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
					</Section>
					<Section Name="GEN004" TypeGUID="03D3B80E-1485-13A6-56528B60DC00DC89">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="GEN004 State" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100160</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100161</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100162</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100163</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100164</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100165</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100166</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100167</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100168</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100169</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100170</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100171</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100172</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100173</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100174</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100175</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100176</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100177</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100178</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100179</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
					</Section>
					<Section Name="GEN005" TypeGUID="03D3B80E-1485-13A6-56528B60DC00DC89">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="GEN005 State" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100180</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100181</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100182</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100183</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100184</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100185</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100186</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100187</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100188</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100189</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100190</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100191</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100192</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100193</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100194</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100195</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100196</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100197</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100198</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100199</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
					</Section>
				</Section>
				<Section Name="Simulation Models" TypeGUID="03D3B937-1485-13A6-5600F2871E269F9A">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Models" TypeGUID="03D3B976-1485-13A6-5604255F981010CE">
						<Description />
						<Properties />
						<Errors />
					</Section>
					<Section Name="Execution Order" TypeGUID="03D3B966-1485-13A6-569CFF8A449BF90A">
						<Description />
						<Properties />
						<Errors />
					</Section>
				</Section>
				<Section Name="Alarms" TypeGUID="03D3B782-1485-13A6-56F58B35B6CBA484">
					<Description />
					<Properties>
						<Property Name="Alarm Rate">
							<I32>1</I32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Procedures" TypeGUID="03D3B7B1-1485-13A6-56649C7783203F22">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Custom Devices" TypeGUID="03D3BB79-1485-13A6-5605EB7AFD7405AC">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="User Channel" TypeGUID="03D3B6B7-1485-13A6-567BE1E1E0DF999A">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="User0" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User1" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User2" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User3" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User4" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User5" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User6" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User7" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User8" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User9" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="ChannelA" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>1</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="ChannelB" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>2</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="TEST_ID" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>3</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>123213</Elem>
						</DefaultValue>
					</Channel>
				</Section>
				<Section Name="Calculated Channels" TypeGUID="03D3B714-1485-13A6-56031C5F1CCB78A9">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="XNET Databases" TypeGUID="def5630b-577f-4ae9-9682-5f8ee445ee21">
					<Description />
					<Properties />
					<Errors />
				</Section>
			</Target>
		</TargetSections>
		<Section Name="Aliases" TypeGUID="e11f4519-09e6-4fb0-99df-2967c4313d67">
			<Description />
			<Properties />
			<Errors />
			<Alias Name="User0" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/User0" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/User1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/User2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User3" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/User3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User4" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/User4" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User5" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/User5" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User6" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/User6" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User7" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/User7" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User8" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/User8" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User9" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/User9" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="ChannelA" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/ChannelA" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="ChannelB" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/ChannelB" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="TEST_ID" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/TEST_ID" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
		</Section>
		<Section Name="Data Sharing Network" TypeGUID="8288dbb9-8c87-4fda-9c66-acec90c46c03">
			<Description />
			<Properties>
				<Property Name="CD Status">
					<U32>2</U32>
				</Property>
			</Properties>
			<Errors />
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/TestWorkspaceAPI/TargetStateEventTest.nivssdf sha256=712ec15b49623e3aa4a3e927c6d0abb785da62e13da485084256c810df07f0dc bytes=84908 -->
## FILE: tests/testutilities/legacy_files/TestWorkspaceAPI/TargetStateEventTest.nivssdf

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/TestWorkspaceAPI/TargetStateEventTest.nivssdf`
- sha256: `712ec15b49623e3aa4a3e927c6d0abb785da62e13da485084256c810df07f0dc`
- bytes: 84908

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2015" Minor="0" Fix="0" Build="3" />
	<Content>Definition</Content>
	<Root Name="TargetStateEventTest" TypeGUID="03D3BA22-1485-13A6-56BD17DA950CCD00">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>TargetStateEventTest</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.5</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3501063739.1351175</Double>
			</Property>
		</Properties>
		<Errors />
		<TargetSections Name="Targets" TypeGUID="eb379619-68d7-4d81-be90-c0bc511cdc10">
			<Description />
			<Properties />
			<Errors />
			<Target Name="Controller" TypeGUID="775504BB-1485-13A6-56755DBF2C326980">
				<Description />
				<Properties>
					<Property Name="OS">
						<String>PharLap</String>
					</Property>
					<Property Name="IP Address">
						<String />
					</Property>
					<Property Name="Control Loop Processor">
						<I32>-2</I32>
					</Property>
					<Property Name="Secondary Control Loop Processor">
						<I32>-2</I32>
					</Property>
					<Property Name="Stream Rate">
						<I32>1</I32>
					</Property>
					<Property Name="DIO Rate">
						<Double>100</Double>
					</Property>
					<Property Name="Streamed Channels">
						<I32>512</I32>
					</Property>
					<Property Name="Filter DAQ Errors">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Filter Watchdog Errors">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Engine Rate">
						<Double>100</Double>
					</Property>
					<Property Name="TL timeout">
						<Double>120</Double>
					</Property>
					<Property Name="daq timeout">
						<U32>1000</U32>
					</Property>
					<Property Name="TL sleep time">
						<U32>0</U32>
					</Property>
					<Property Name="HS Port">
						<I32>2040</I32>
					</Property>
					<Property Name="LS Port">
						<I32>2050</I32>
					</Property>
					<Property Name="HS Port Timeout">
						<I32>1000</I32>
					</Property>
					<Property Name="LS Port Timeout">
						<I32>1000</I32>
					</Property>
					<Property Name="Deployment Group">
						<I32>0</I32>
					</Property>
					<Property Name="Control Rate">
						<Double>1</Double>
					</Property>
					<Property Name="Input Configuration">
						<U32>0</U32>
					</Property>
					<Property Name="ts">
						<U32>0</U32>
					</Property>
					<Property Name="Warmup Time [ms]">
						<U32>2000</U32>
					</Property>
					<Property Name="Data Rate">
						<Double>15</Double>
					</Property>
					<Property Name="FPGAScanInterfaceMode">
						<U16>0</U16>
					</Property>
				</Properties>
				<Errors />
				<Section Name="Hardware" TypeGUID="775504AB-1485-13A6-560018C1F4E3EEE1">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Chassis" TypeGUID="03D3BACD-1485-13A6-56E99D97B7543BAF">
						<Description />
						<Properties>
							<Property Name="Master type">
								<U32>1</U32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Timing and Sync" TypeGUID="03D3BAED-1485-13A6-56E20B50F6E06D94">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="DAQ" TypeGUID="77550612-1485-13A6-56570AB5032158E9">
							<Description />
							<Properties />
							<Errors />
							<Section Name="Waveform Tasks" TypeGUID="1D6B8779-A957-42D1-B074-82153DB7FF44">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
						<Section Name="FPGA" TypeGUID="03D3B659-1485-13A6-5652D8A07328ECB7">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="NI-XNET" TypeGUID="6b693e6d-67b1-40b8-8108-4a4cc3147721">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
								</Property>
								<Property Name="Decimation">
									<I32>1</I32>
								</Property>
								<Property Name="Driver VI Exec Mode">
									<U32>1</U32>
								</Property>
							</Properties>
							<Errors />
							<Section Name="CAN" TypeGUID="6c5bb91f-0da7-407d-aefc-acbe49c768df">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="FlexRay" TypeGUID="e33fae90-03f1-4f76-b2f1-6eb8fcac2676">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="LIN" TypeGUID="c9c30728-42cb-4dc3-b054-b80e7a54e833">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
						<Section Name="Data Sharing" TypeGUID="d56f3ac1-7b2c-422c-9d11-fd9cc7abf2a5">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
					</Section>
				</Section>
				<Section Name="Custom Devices" TypeGUID="03D3BB79-1485-13A6-5605EB7AFD7405AC">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Simulation Models" TypeGUID="03D3B937-1485-13A6-5600F2871E269F9A">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Models" TypeGUID="03D3B976-1485-13A6-5604255F981010CE">
						<Description />
						<Properties />
						<Errors />
					</Section>
					<Section Name="Execution Order" TypeGUID="03D3B966-1485-13A6-569CFF8A449BF90A">
						<Description />
						<Properties />
						<Errors />
					</Section>
				</Section>
				<Section Name="User Channels" TypeGUID="03D3B6B7-1485-13A6-567BE1E1E0DF999A">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Calculated Channels" TypeGUID="03D3B714-1485-13A6-56031C5F1CCB78A9">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Stimulus" TypeGUID="03D3B7FF-1485-13A6-56B2328F9511AC8B">
					<Description />
					<Properties>
						<Property Name="Max Steps">
							<I32>128</I32>
						</Property>
						<Property Name="Max Gen Maps">
							<I32>256</I32>
						</Property>
						<Property Name="Aux Buffer Size">
							<I32>10000</I32>
						</Property>
						<Property Name="Analysis Buffer Size">
							<I32>10000</I32>
						</Property>
						<Property Name="Analysis Result Size">
							<I32>5000</I32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Alarms" TypeGUID="03D3B782-1485-13A6-56F58B35B6CBA484">
					<Description />
					<Properties>
						<Property Name="Alarm Rate">
							<I32>1</I32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Procedures" TypeGUID="03D3B7B1-1485-13A6-56649C7783203F22">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="XNET Databases" TypeGUID="def5630b-577f-4ae9-9682-5f8ee445ee21">
					<Description />
					<Properties>
						<Property Name="CD Status">
							<U32>2</U32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="System Channels" TypeGUID="03D3B753-1485-13A6-56B10ED0820CF410">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="Actual Loop Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Hz" BitFields="1">
						<Description>The execution rate of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Index" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The decimation of the Data Processing Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Time" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>The relative system time of the VeriStand Engine according to the iteration count and Delta T of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="DAQ Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Error Code" BitFields="3">
						<Description>The last reported error code from a DAQmx function call. The value zero indicates no error has occurred.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Delta T" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>The period in seconds of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Compiler Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 1" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 2" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 3" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Resume Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 4" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 5" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 6" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="RT Engine Build" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>A value representing the build number of the NI VeriStand Engine</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Loop Duration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The duration of the Primary Control Loop in nanoseconds</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Loop Duration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The duration of the Data Processing Loop in nanoseconds</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Command" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="3">
						<Description>Internally commands the RT system with the following numeric values:

0: None
1: Restart System
2: Reset System
3: Shut Down System
4: Reboot System</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Streamed Channel Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of channels that the VeriStand Engine is currently streaming to the host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Max Streamed Channels" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The maximum number of channels that the VeriStand Engine can stream to the host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Model Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the models have not completed their execution in time</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Clients" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Maximum GENs" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of stimulus profile generators instantiated by the system</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Generator Engine State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="3">
						<Description>The current state of the stimulus profile generator engine

0: Idle
1: Running
2: Stopped
3: Paused</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Watchdog Timer" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The amount of time in nanoseconds since the Watchdog Timer Loop last executed. The Watchdog Timer Loop is set to execute at a rate of 10Hz.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HS TCP Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the streaming data gets overwritten.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Host IP" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The 32-bit integer IP Address of the connected host. A zero value indicates no host is connected to the VeriStand Engine.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Trace Enabled Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether execution tracing is currently active on the RT Target.  Set to 1 to start tracing.  Set to 0 to stop tracing and send result to host (if no host is present it is logged to disk).  Set to -1 to stop tracing and write result to disk.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Detailed Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether detailed execution tracing is enabled on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="VI Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether VI execution tracing is enabled on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Trace Buffer Size" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Bytes" BitFields="3">
						<Description>Specifies the size in bytes of the execution trace buffer on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>250000</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Thread Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether thread execution tracing is enabled on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Absolute Time" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>Returns the current date and time in seconds relative to 12:00 a.m., Friday, January 1, 1904, Universal Time [01-01-1904 00:00:00]. This value is coerced from a 128-bit value to double precision, which may impact resolution.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Time - Microseconds" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="usec" BitFields="1">
						<Description>The relative system time in microseconds of the VeriStand Engine according to the iteration count and Delta T of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 41" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 42" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 43" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 44" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Iterations" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Min Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Actual Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Failure Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The failure count of current analysis settings</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Analysis State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The state of the analysis sub-system on the RT execution host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="TCP Data Packet Loss" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the VeriStand Engine fails to send a data packet to the host. A non-zero number can indicate data loss in logged data. The value is reset every time a Workspace connects to the VeriStand Engine.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop attempted to write to a waveform read session within the NI VeriStand engine and timed out.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL TCP Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop attempted to write to the TCP loop (for a host waveform stream session) and timed out.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Error Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop encountered an error.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Error Code" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The last error code encountered by the waveform processing loop.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Streamed Waveform Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of waveforms that the VeriStand Engine is currently streaming to the host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Iteration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The iteration count of the Primary Control Loop.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Last Late Iteration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The iteration count of the Primary Control Loop that last recorded a late count. If the Primary Control Loop has not recorded a late count, this value is -1.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 58" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 59" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Real-Time Sequence Command" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Internally commands the active real-time sequences with the following numeric values:
		
		0: None
		1: Stop All
		2: Abort All</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Real-Time Sequence Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of real-time sequences currently running.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 62" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 63" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 64" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 65" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 66" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 67" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 68" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 69" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 70" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 71" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 72" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 73" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 74" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 75" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 76" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 77" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 78" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 79" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 80" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 81" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 82" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 83" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 84" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 85" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 86" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 87" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 88" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 89" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 90" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 91" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="AO1 Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Loop Wakeup Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="1">
						<Description>The wakeup status of the Primary Control Loop.

0: Normal
1: Aborted
2: Asynchronous wakeup
3: Timing source error
4: Timed loop error
5: Timeout</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HD Free Space" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP-LP Overwrite" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Primary Control Loop timed out writing channel data to the Data Processing Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Data Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Data Processing Loop timed out writing channel data to the Communication Send Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Primary Control Loop reported being late</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Data Processing Loop reported being late</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Log Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The state of the logging sub-system on the RT execution host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
				</Section>
			</Target>
			<Target Name="NIVeriStand-AutoTest-PXI1" TypeGUID="775504BB-1485-13A6-56755DBF2C326980">
				<Description />
				<Properties>
					<Property Name="OS">
						<String>PharLap</String>
					</Property>
					<Property Name="IP Address">
						<String>NIVeriStand-AutoTest-PXI1</String>
					</Property>
					<Property Name="Control Loop Processor">
						<I32>-2</I32>
					</Property>
					<Property Name="Secondary Control Loop Processor">
						<I32>-2</I32>
					</Property>
					<Property Name="Stream Rate">
						<I32>1</I32>
					</Property>
					<Property Name="DIO Rate">
						<Double>100</Double>
					</Property>
					<Property Name="Streamed Channels">
						<I32>512</I32>
					</Property>
					<Property Name="Filter DAQ Errors">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Filter Watchdog Errors">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Engine Rate">
						<Double>100</Double>
					</Property>
					<Property Name="TL timeout">
						<Double>120</Double>
					</Property>
					<Property Name="daq timeout">
						<U32>1000</U32>
					</Property>
					<Property Name="TL sleep time">
						<U32>0</U32>
					</Property>
					<Property Name="HS Port">
						<I32>2040</I32>
					</Property>
					<Property Name="LS Port">
						<I32>2050</I32>
					</Property>
					<Property Name="HS Port Timeout">
						<I32>1000</I32>
					</Property>
					<Property Name="LS Port Timeout">
						<I32>1000</I32>
					</Property>
					<Property Name="Deployment Group">
						<I32>0</I32>
					</Property>
					<Property Name="Control Rate">
						<Double>1</Double>
					</Property>
					<Property Name="Input Configuration">
						<U32>0</U32>
					</Property>
					<Property Name="ts">
						<U32>0</U32>
					</Property>
					<Property Name="Warmup Time [ms]">
						<U32>2000</U32>
					</Property>
					<Property Name="Data Rate">
						<Double>15</Double>
					</Property>
					<Property Name="FPGAScanInterfaceMode">
						<U16>0</U16>
					</Property>
					<Property Name="Timing Source Settings">
						<U16>0</U16>
					</Property>
				</Properties>
				<Errors />
				<Section Name="Hardware" TypeGUID="775504AB-1485-13A6-560018C1F4E3EEE1">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Chassis" TypeGUID="03D3BACD-1485-13A6-56E99D97B7543BAF">
						<Description />
						<Properties>
							<Property Name="Master type">
								<U32>1</U32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Timing and Sync" TypeGUID="03D3BAED-1485-13A6-56E20B50F6E06D94">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="DAQ" TypeGUID="77550612-1485-13A6-56570AB5032158E9">
							<Description />
							<Properties />
							<Errors />
							<Section Name="Waveform Tasks" TypeGUID="1D6B8779-A957-42D1-B074-82153DB7FF44">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
						<Section Name="FPGA" TypeGUID="03D3B659-1485-13A6-5652D8A07328ECB7">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="NI-XNET" TypeGUID="6b693e6d-67b1-40b8-8108-4a4cc3147721">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
								</Property>
								<Property Name="Decimation">
									<I32>1</I32>
								</Property>
								<Property Name="Driver VI Exec Mode">
									<U32>1</U32>
								</Property>
							</Properties>
							<Errors />
							<Section Name="CAN" TypeGUID="6c5bb91f-0da7-407d-aefc-acbe49c768df">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="FlexRay" TypeGUID="e33fae90-03f1-4f76-b2f1-6eb8fcac2676">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="LIN" TypeGUID="c9c30728-42cb-4dc3-b054-b80e7a54e833">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
						<Section Name="Data Sharing" TypeGUID="d56f3ac1-7b2c-422c-9d11-fd9cc7abf2a5">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
					</Section>
				</Section>
				<Section Name="Custom Devices" TypeGUID="03D3BB79-1485-13A6-5605EB7AFD7405AC">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Simulation Models" TypeGUID="03D3B937-1485-13A6-5600F2871E269F9A">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Models" TypeGUID="03D3B976-1485-13A6-5604255F981010CE">
						<Description />
						<Properties />
						<Errors />
					</Section>
					<Section Name="Execution Order" TypeGUID="03D3B966-1485-13A6-569CFF8A449BF90A">
						<Description />
						<Properties />
						<Errors />
					</Section>
				</Section>
				<Section Name="User Channels" TypeGUID="03D3B6B7-1485-13A6-567BE1E1E0DF999A">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="User Channel 0" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 1" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 2" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 3" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 4" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
				</Section>
				<Section Name="Calculated Channels" TypeGUID="03D3B714-1485-13A6-56031C5F1CCB78A9">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Stimulus" TypeGUID="03D3B7FF-1485-13A6-56B2328F9511AC8B">
					<Description />
					<Properties>
						<Property Name="Max Steps">
							<I32>128</I32>
						</Property>
						<Property Name="Max Gen Maps">
							<I32>256</I32>
						</Property>
						<Property Name="Aux Buffer Size">
							<I32>10000</I32>
						</Property>
						<Property Name="Analysis Buffer Size">
							<I32>10000</I32>
						</Property>
						<Property Name="Analysis Result Size">
							<I32>5000</I32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Alarms" TypeGUID="03D3B782-1485-13A6-56F58B35B6CBA484">
					<Description />
					<Properties>
						<Property Name="Alarm Rate">
							<I32>1</I32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Procedures" TypeGUID="03D3B7B1-1485-13A6-56649C7783203F22">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="XNET Databases" TypeGUID="def5630b-577f-4ae9-9682-5f8ee445ee21">
					<Description />
					<Properties>
						<Property Name="CD Status">
							<U32>2</U32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="System Channels" TypeGUID="03D3B753-1485-13A6-56B10ED0820CF410">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="Actual Loop Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Hz" BitFields="1">
						<Description>The execution rate of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Index" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The decimation of the Data Processing Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Time" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>The relative system time of the VeriStand Engine according to the iteration count and Delta T of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="DAQ Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Error Code" BitFields="3">
						<Description>The last reported error code from a DAQmx function call. The value zero indicates no error has occurred.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Delta T" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>The period in seconds of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Compiler Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 1" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 2" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 3" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Resume Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 4" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 5" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 6" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="RT Engine Build" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>A value representing the build number of the NI VeriStand Engine</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Loop Duration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The duration of the Primary Control Loop in nanoseconds</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Loop Duration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The duration of the Data Processing Loop in nanoseconds</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Command" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="3">
						<Description>Internally commands the RT system with the following numeric values:

0: None
1: Restart System
2: Reset System
3: Shut Down System
4: Reboot System</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Streamed Channel Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of channels that the VeriStand Engine is currently streaming to the host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Max Streamed Channels" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The maximum number of channels that the VeriStand Engine can stream to the host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Model Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the models have not completed their execution in time</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Clients" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Maximum GENs" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of stimulus profile generators instantiated by the system</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Generator Engine State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="3">
						<Description>The current state of the stimulus profile generator engine

0: Idle
1: Running
2: Stopped
3: Paused</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Watchdog Timer" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The amount of time in nanoseconds since the Watchdog Timer Loop last executed. The Watchdog Timer Loop is set to execute at a rate of 10Hz.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HS TCP Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the streaming data gets overwritten.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Host IP" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The 32-bit integer IP Address of the connected host. A zero value indicates no host is connected to the VeriStand Engine.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Trace Enabled Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether execution tracing is currently active on the RT Target.  Set to 1 to start tracing.  Set to 0 to stop tracing and send result to host (if no host is present it is logged to disk).  Set to -1 to stop tracing and write result to disk.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Detailed Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether detailed execution tracing is enabled on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="VI Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether VI execution tracing is enabled on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Trace Buffer Size" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Bytes" BitFields="3">
						<Description>Specifies the size in bytes of the execution trace buffer on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>250000</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Thread Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Specifies whether thread execution tracing is enabled on the RT Target.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Absolute Time" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>Returns the current date and time in seconds relative to 12:00 a.m., Friday, January 1, 1904, Universal Time [01-01-1904 00:00:00]. This value is coerced from a 128-bit value to double precision, which may impact resolution.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Time - Microseconds" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="usec" BitFields="1">
						<Description>The relative system time in microseconds of the VeriStand Engine according to the iteration count and Delta T of the Primary Control Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 41" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 42" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 43" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 44" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Iterations" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Min Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Actual Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Failure Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The failure count of current analysis settings</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Analysis State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The state of the analysis sub-system on the RT execution host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="TCP Data Packet Loss" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the VeriStand Engine fails to send a data packet to the host. A non-zero number can indicate data loss in logged data. The value is reset every time a Workspace connects to the VeriStand Engine.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop attempted to write to a waveform read session within the NI VeriStand engine and timed out.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL TCP Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop attempted to write to the TCP loop (for a host waveform stream session) and timed out.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Error Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop encountered an error.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Error Code" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The last error code encountered by the waveform processing loop.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Streamed Waveform Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of waveforms that the VeriStand Engine is currently streaming to the host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Iteration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The iteration count of the Primary Control Loop.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Last Late Iteration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The iteration count of the Primary Control Loop that last recorded a late count. If the Primary Control Loop has not recorded a late count, this value is -1.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 58" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 59" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Real-Time Sequence Command" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Internally commands the active real-time sequences with the following numeric values:
		
		0: None
		1: Stop All
		2: Abort All</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Real-Time Sequence Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of real-time sequences currently running.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 62" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 63" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 64" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 65" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 66" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 67" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 68" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 69" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 70" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 71" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 72" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 73" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 74" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 75" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 76" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 77" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 78" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 79" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 80" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 81" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 82" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 83" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 84" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 85" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 86" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 87" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 88" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 89" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 90" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 91" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="AO1 Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Loop Wakeup Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="1">
						<Description>The wakeup status of the Primary Control Loop.

0: Normal
1: Aborted
2: Asynchronous wakeup
3: Timing source error
4: Timed loop error
5: Timeout</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HD Free Space" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP-LP Overwrite" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Primary Control Loop timed out writing channel data to the Data Processing Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Data Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Data Processing Loop timed out writing channel data to the Communication Send Loop</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Primary Control Loop reported being late</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Data Processing Loop reported being late</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Log Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The state of the logging sub-system on the RT execution host</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
				</Section>
			</Target>
		</TargetSections>
		<Section Name="Aliases" TypeGUID="e11f4519-09e6-4fb0-99df-2967c4313d67">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Scales" TypeGUID="032c8aec-ce5b-6d40-06c5-5703bbc7ccee">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="System Mappings" TypeGUID="5691ea13-4544-497e-9bda-cf69dc707663">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Data Sharing Network" TypeGUID="8288dbb9-8c87-4fda-9c66-acec90c46c03">
			<Description />
			<Properties>
				<Property Name="CD Status">
					<U32>2</U32>
				</Property>
				<Property Name="DSN Dynamic Data Size">
					<I32>30</I32>
				</Property>
			</Properties>
			<Errors />
		</Section>
		<Section Name="System Initialization" TypeGUID="773b9311-3758-47fa-842f-b1c1960dabd0">
			<Description />
			<Properties>
				<Property Name="Auto Start">
					<Boolean>true</Boolean>
				</Property>
			</Properties>
			<Errors />
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/TestWorkspaceAPI/TestWorkspaceAPI.nivsprj sha256=c26b4591c691d02a91f552ea25f3d84727062e6aba1964e3b05b2831761d2edb bytes=2647 -->
## FILE: tests/testutilities/legacy_files/TestWorkspaceAPI/TestWorkspaceAPI.nivsprj

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/TestWorkspaceAPI/TestWorkspaceAPI.nivsprj`
- sha256: `c26b4591c691d02a91f552ea25f3d84727062e6aba1964e3b05b2831761d2edb`
- bytes: 2647

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="FCEE3C48768D90DE7DA2406C6769F97A067B82775F50FE817D7387F9D1BDEE0FFE09A4BC6072C865C2F39D040582B071EB03BF96C667D7448FDFAAF74C4CBBDD" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.6.0.49854" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.6.0.49854" FeatureSetName="VeriStand Core Components" Name="http://www.ni.com/VeriStand" OldestCompatibleVersion="9.0.0.49152" Version="9.0.0.49152" />
		<ApplicationVersionInfo Build="9.3.0.49854" Name="VeriStand" Version="9.6.0.49854" />
	</SourceModelFeatureSet>
	<Project p2:ProjectVersion="1.0.0.0" xmlns:p2="http://www.ni.com/VeriStand" xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="27453b99a96241daa593968d0d26b210" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="f5c62124fce842a9a723bd809b8296f6" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="7166ff77dac440de8818d4fae690a333" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<FileReference Bindings=".nivsproj" Id="81dcf592cad64f04a0f8b8f1d7965af6" ModelDefinitionType="{http://www.ni.com/PlatformFramework}ExternalFile" Name="TestWorkspaceAPI.nivsproj" StoragePath="TestWorkspaceAPI.nivsproj" />
			<SourceFileReference Bindings="EnvoyManager" Id="9777b8139ad44fe99b03b1cc0ff02a4f" ModelDefinitionType="{http://www.ni.com/VeriStand}SystemDefinition" Name="TestWorkspaceAPI.nivssdf" StoragePath="TestWorkspaceAPI.nivssdf" />
			<FileReference Bindings=".nivsscreen" Id="db8381cb61234100a32a7f746bd39861" ModelDefinitionType="{http://www.ni.com/PlatformFramework}ExternalFile" Name="TestWorkspaceAPI.nivsscreen" StoragePath="TestWorkspaceAPI.nivsscreen" />
			<EmbeddedDefinitionReference Id="b9feadc137f43d7a84b6e4211c7f46d" ModelDefinitionType="SdfFilePath" Name="SdfPath" Reparentable="False">
				<p2:SdfFilePath SdfPath="TestWorkspaceAPI.nivssdf" />
			</EmbeddedDefinitionReference>
			<EmbeddedDefinitionReference Id="f33e4e98714f426fb5a1856a0a3fcb59" ModelDefinitionType="GatewayDefinition" Name="Gateway" Reparentable="False">
				<p2:GatewayDefinition />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/TestWorkspaceAPI/TestWorkspaceAPI.nivsproj sha256=1a28af2372431f4c85983e4ce640e00797b4481519cf2f7ca38042e1c31113c4 bytes=11534 -->
## FILE: tests/testutilities/legacy_files/TestWorkspaceAPI/TestWorkspaceAPI.nivsproj

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/TestWorkspaceAPI/TestWorkspaceAPI.nivsproj`
- sha256: `1a28af2372431f4c85983e4ce640e00797b4481519cf2f7ca38042e1c31113c4`
- bytes: 11534

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2012" Minor="0" Fix="0" Build="1" />
	<Content>Definition</Content>
	<Root Name="TestWorkspaceAPI" TypeGUID="d9313aae-3554-45e5-93f3-86454275d4f2">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>TestWorkspaceAPI</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.0</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3351079557.3305616</Double>
			</Property>
		</Properties>
		<Errors />
		<Section Name="System Definition File" TypeGUID="b9227a5b-2770-4a62-8621-ac414d4124fb">
			<Description />
			<Properties />
			<Errors />
			<Section Name="TestWorkspaceAPI.nivssdf" TypeGUID="3a41ca74-36ec-4aff-9219-9d05c8f91208">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="TestWorkspaceAPI.nivssdf">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5>b14db381a882beb3806e80a53b9e7173</MD5>
						</DependentFile>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Workspace" TypeGUID="bc98486f-7b49-4949-9504-949cbe254c85">
			<Description />
			<Properties>
				<Property Name="User Accounts">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAAAzwkAgAAAAAAFAA5AMP////8ETmFtZQAAEkAw/////whQYXNzd29yZAAADkAw/////wVHcm91cABMAPEAAAAAAAAAAhhTZWMgQWRtaW5pc3RyYXRpb24ubHZsaWIMVXNlclR5cGUuY3RsAB5AUAADAAAAAQACDFVzZXIgQWNjb3VudAAAGkBAAAH/////AAMNVXNlciBBY2NvdW50cwABAAQAAAABAAAADUFkbWluaXN0cmF0b3IAAAAAAAAADkFkbWluaXN0cmF0aW9uAAAAAA==</Data>
					</Variant>
				</Property>
				<Property Name="Group Accounts">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAAA7QkAgAAAAAAFAA5AMP////8ETmFtZQAADEAhB0Jvb2xlYW4AGEBAAAH/////AAELUGVybWlzc2lvbnMASwDxAAAAAAAAAAIYU2VjIEFkbWluaXN0cmF0aW9uLmx2bGliDUdyb3VwVHlwZS5jdGwAHEBQAAIAAAACDUdyb3VwIEFjY291bnQAHEBAAAH/////AAMOR3JvdXAgQWNjb3VudHMAAAEABAAAAAIAAAAOQWRtaW5pc3RyYXRpb24AAAANAQEBAQEBAQEBAQEBAQAAAAhPcGVyYXRvcgAAAA0BAAAAAQABAQAAAAAAAAAAAA==</Data>
					</Variant>
				</Property>
				<Property Name="Tools Menu Items">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAAEygkAgAAAAAAIAA5AMP////8ETmFtZQAAEkAw/////whGdW5jdGlvbgAAYQDxAAAAAAAAAAETVG9vbGJhciBCdXR0b25zLmN0bABFQBYAAwROb25lF1N0aW11bHVzIFByb2ZpbGUgRWRpdG9yC0RhdGEgVmlld2VyAAAOVG9vbGJhciBCdXR0b24AAVMA8QAAAAAAAAABH2VudW1fVXNlciBBZG1pbiBQZXJtaXNzaW9ucy5jdGwBK0AWAA0HRGVmYXVsdA5BZG1pbmlzdHJhdGlvbhdDaGFubmVsIFNjYWxpbmcgVXRpbGl0eRFBZGQgRGlzcGxheSBJdGVtcxNDaGFuZ2UgVXNlciBQcm9maWxlI0VkaXQgU3RpbXVsdXMgUHJvZmlsZSBFZGl0b3IgSGVhZGVyGkVkaXQgRGlzcGxheSBJdGVtIFNldHRpbmdzG01vZGVsIFBhcmFtZXRlciBDYWxpYnJhdGlvbhJSdW50aW1lIEFsYXJtIEVkaXQPRWRpdCBUb29scyBNZW51FkVkaXQgRW5naW5lIENvbXBvbmVudHMaQ29uZmlndXJlIFZpc2libGUgQ2hhbm5lbHMNRmF1bHQgTWFuYWdlcgAAClBlcm1pc3Npb24AABpAMv////8QQ3VzdG9tIFRvb2wgUGF0aAAAaQDxxyxnxAAAAAIRTklWU19TaGFyZWQubHZsaWINUGF0aCB0eXBlLmN0bABBQBYAAwhBYnNvbHV0ZQhSZWxhdGl2ZQxUb0FwcERhdGFEaXIAABVDdXN0b20gVG9vbCBQYXRoIFR5cGUAYwDxAAAAAAAAAAIaTklWU1Byb2pfRmlsZW1hbmFnZXIubHZsaWIZVG9vbHMgTWVudSBJdGVtcyBUeXBlLmN0bAAmQFAABgAAAAEAAgADAAQABQ9Ub29scyBNZW51IEl0ZW0AHkBAAAH/////AAYQVG9vbHMgTWVudSBJdGVtcwAAAQAHAAAACAAAABdNb2RlbCBQYXJhbWV0ZXIgTWFuYWdlcgAAABpNb2RlbCBQYXJhbWV0ZXIgTWFuYWdlci52aQAAAABQVEgwAAAABAAAAAAAAAAAAAEtAAAAAS0AAAAAUFRIMAAAAAQAAAAAAAAAAAAeU3RpbXVsdXMgUHJvZmlsZSBFZGl0b3IgLSBTdGVwAAAAFVRlc3QgRWRpdG9yIChTdGVwKS52aQABAABQVEgwAAAABAAAAAAAAAAAACBTdGltdWx1cyBQcm9maWxlIFNlcXVlbmNlIEVkaXRvcgAAABZUZXN0IEVkaXRvciAoQmF0Y2gpLnZpAAAAAFBUSDAAAAAEAAAAAAAAAAAAEFRETVMgRmlsZSBWaWV3ZXIAAAAXc2NyX1RETVMgRGF0YSBWaWV3ZXIudmkAAgAAUFRIMAAAAAQAAAAAAAAAAAABLQAAAAEtAAAAAFBUSDAAAAAEAAAAAAAAAAAAE0NoYW5uZWwgRGF0YSBWaWV3ZXIAAAAWQ2hhbm5lbCBEYXRhIFZpZXdlci52aQAAAABQVEgwAAAABAAAAAAAAAAAAA5Db25zb2xlIFZpZXdlcgAAABJWaWV3IFJUIENvbnNvbGUudmkAAAAAUFRIMAAAAAQAAAAAAAAAAAAA</Data>
					</Variant>
				</Property>
				<Property Name="Engine Components">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAAB3AkAgAAAAAAIABJAMP////8IRnVuY3Rpb24AAA5AIQlTaG93SXRlbT8AL0AWAAMETm9uZQxXYWl0Q29tcGxldGUIV2FpdFN5bmMAAApMYXVuY2hUeXBlAAARQAMAC1N5bmNUaW1lb3V0ABpAMv////8QQ3VzdG9tIFRvb2wgUGF0aAAAaQDxxyxnxAAAAAIRTklWU19TaGFyZWQubHZsaWINUGF0aCB0eXBlLmN0bABBQBYAAwhBYnNvbHV0ZQhSZWxhdGl2ZQxUb0FwcERhdGFEaXIAABVDdXN0b20gVG9vbCBQYXRoIFR5cGUAaQDxAAAAAAAAAAIaTklWU1Byb2pfRmlsZW1hbmFnZXIubHZsaWIZRW5naW5lIENvbXBvbmVudCBUeXBlLmN0bAAsQFAABgAAAAEAAgADAAQABRVFbmdpbmUgQ29tcG9uZW50IEl0ZW0AHkBAAAH/////AAYRRW5naW5lIENvbXBvbmVudHMAAQAHAAAAAgAAABJzdWJfQ2FsaWJyYXRpb24udmkAAAAAAAAAUFRIMAAAAAQAAAAAAAAAAAAaTW9kZWwgUGFyYW1ldGVyIE1hbmFnZXIudmkAAAAAAAAAUFRIMAAAAAQAAAAAAAAAAAAA</Data>
					</Variant>
				</Property>
				<Property Name="Hidden Channels">
					<StringArray />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Screens" TypeGUID="cdfadfe0-c84a-4268-a677-4f2f3525465e">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="TestWorkspaceAPI.nivsscreen">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5>5186d85ed828ac5084ab41b98274d80b</MD5>
						</DependentFile>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Services" TypeGUID="736a951c-d9c8-457f-96a9-cd0ef16011a5">
			<Description />
			<Properties />
			<Errors />
			<Section Name="Model Parameter Manager" TypeGUID="cc686646-9933-410d-a553-6308e6e06897">
				<Description />
				<Properties>
					<Property Name="Function">
						<String>Model Parameter Manager.vi</String>
					</Property>
					<Property Name="Path">
						<DependentFile Type="Absolute" Path="">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
						</DependentFile>
					</Property>
					<Property Name="Sync Options">
						<String>WaitSync</String>
					</Property>
					<Property Name="Sync Timeout">
						<I32>10000</I32>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Profiles" TypeGUID="c3bd79ec-3336-4b06-868e-3217c640edd5">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Calibration" TypeGUID="38433223-24A0-4b32-9339-370EC5AA31B4">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Alarm Responses" TypeGUID="3b1ab560-d77a-41f2-adb4-0c0250b010b3">
			<Description />
			<Properties />
			<Errors />
			<Section Name="Response High" TypeGUID="99267DF5-8C59-4AAC-B020-7591F4886206">
				<Description />
				<Properties>
					<Property Name="Show Dialog">
						<Boolean>true</Boolean>
					</Property>
					<Property Name="Play Sound">
						<String>Disabled</String>
					</Property>
					<Property Name="Wave File">
						<DependentFile Type="Absolute" Path="">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
						</DependentFile>
					</Property>
					<Property Name="Log Alarms">
						<String>Enabled</String>
					</Property>
					<Property Name="Log File">
						<String>Logs\Alarm Log.txt</String>
					</Property>
					<Property Name="Max Priority">
						<U32>10</U32>
					</Property>
					<Property Name="Min Priority">
						<U32>0</U32>
					</Property>
					<Property Name="Enable Response">
						<Boolean>true</Boolean>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Response Med" TypeGUID="99267DF5-8C59-4AAC-B020-7591F4886206">
				<Description />
				<Properties>
					<Property Name="Show Dialog">
						<Boolean>true</Boolean>
					</Property>
					<Property Name="Play Sound">
						<String>Disabled</String>
					</Property>
					<Property Name="Wave File">
						<DependentFile Type="Absolute" Path="">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
						</DependentFile>
					</Property>
					<Property Name="Log Alarms">
						<String>Enabled</String>
					</Property>
					<Property Name="Log File">
						<String>Logs\Alarm Log.txt</String>
					</Property>
					<Property Name="Max Priority">
						<U32>21</U32>
					</Property>
					<Property Name="Min Priority">
						<U32>11</U32>
					</Property>
					<Property Name="Enable Response">
						<Boolean>true</Boolean>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Response Low" TypeGUID="99267DF5-8C59-4AAC-B020-7591F4886206">
				<Description />
				<Properties>
					<Property Name="Show Dialog">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Play Sound">
						<String>Disabled</String>
					</Property>
					<Property Name="Wave File">
						<DependentFile Type="Absolute" Path="">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
						</DependentFile>
					</Property>
					<Property Name="Log Alarms">
						<String>Enabled</String>
					</Property>
					<Property Name="Log File">
						<String>Logs\Alarm Log.txt</String>
					</Property>
					<Property Name="Max Priority">
						<U32>31</U32>
					</Property>
					<Property Name="Min Priority">
						<U32>22</U32>
					</Property>
					<Property Name="Enable Response">
						<Boolean>true</Boolean>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Custom Files" TypeGUID="9e2cb626-3583-4345-aeb6-b9fead6ec565">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Dependencies" TypeGUID="e5b093fa-a709-4df2-807e-a403422ba675">
			<Description />
			<Properties />
			<Errors />
			<Section Name="TestWorkspaceAPI.nivssdf [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\TestWorkspaceAPI\TestWorkspaceAPI.nivssdf]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\TestWorkspaceAPI\TestWorkspaceAPI.nivssdf</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="TestWorkspaceAPI.nivsscreen [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\TestWorkspaceAPI\TestWorkspaceAPI.nivsscreen]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\TestWorkspaceAPI\TestWorkspaceAPI.nivsscreen</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="sinewave.dll [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\TestWorkspaceAPI\sinewave.dll]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\TestWorkspaceAPI\sinewave.dll</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/TestWorkspaceAPI/TestWorkspaceAPI.nivsscreen sha256=3a03c3dc5f1be2a21c5c31fa14ae2612b56a8fa3d6e8fa6e1336224ed1b3d9dd bytes=4123 -->
## FILE: tests/testutilities/legacy_files/TestWorkspaceAPI/TestWorkspaceAPI.nivsscreen

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/TestWorkspaceAPI/TestWorkspaceAPI.nivsscreen`
- sha256: `3a03c3dc5f1be2a21c5c31fa14ae2612b56a8fa3d6e8fa6e1336224ed1b3d9dd`
- bytes: 4123

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2010" Minor="0" Fix="0" Build="0" />
	<Content>Definition</Content>
	<Root Name="WorkspaceScreen" TypeGUID="2e39a440-e372-11de-8a39-0800200c9a66">
		<Properties>
			<Property Name="Screen Data">
				<Variant>
					<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
					<Data>AAAIlgkAgAAAAABYABRAMP////8LVGVtcGxhdGUgVkkAEUADAApQb3NpdGlvbiBYAAARQAMAClBvc2l0aW9uIFkAABBAMP////8GQ3VzdG9tAAAUQCEOU2hvdyBUaXRsZSBCYXIAAAlAAwACSUQAABJAIQ1BbHdheXMgT24gVG9wABJAIQxBbGxvdyBSZXNpemUAABRAIQ5BbGxvdyBNaW5pbWl6ZQAAEEAhC0FsbG93IENsb3NlABRAIQ5TaXplIHRvIFNjcmVlbgAAD0ADAAlTY3JlZW4uSUQAGUAWAAIGTm9ybWFsA05ldwAABVN0YXRlAA5AMP////8FVGl0bGUACUACAANbMF0ACUACAANbMV0ACUACAANbMl0ACUACAANbM10AHEBQAAQADgAPABAAEQ1XaW5kb3cgQm91bmRzABFACAALQ2hhbm5lbCBSZWYADkAw/////wRVbml0AAAUQCEORGVmYXVsdCBVbml0cz8AABJAIQxGbGFzaCBMaW1pdD8AAA1ABwAHQ29sb3IgMQANQAcAB0NvbG9yIDIADUAHAAdDb2xvciAzAA1ABwAHQ29sb3IgNAAPQAcACUJjayBDb2xvcgARQAcACkZvcmUgQ29sb3IAAA1ACgAHTGltaXQgMQANQAoAB0xpbWl0IDIADUAKAAdMaW1pdCAzAA1ACgAHTGltaXQgNAATQAMADExpbWl0IE1vZGUgMQAAE0ADAAxMaW1pdCBNb2RlIDIAABNAAwAMTGltaXQgTW9kZSAzAAATQAMADExpbWl0IE1vZGUgNAAAFUADAA9TY2FsZSBQcmVjaXNpb24AD0AKAAlTY2FsZSBNaW4AD0AKAAlTY2FsZSBNYXgADUADAAZGb3JtYXQAAA9AAwAJUHJlY2lzaW9uABVAAwAPQmFja2dyb3VuZCBUeXBlABFAAwALVmFyaWFibGUgSUQAEEBAAAH/////ACsDSURzABRAMP////8LVmFyaWFibGUgSUQAEkBAAAH/////AC0FVW5pdHMAFEBAAAH/////AC0GTGFiZWxzAAATQAoADFNjYWxlIEZhY3RvcgAAE0AKAAxTY2FsZSBPZmZzZXQAABFABwALVmFyaWFibGUgSUQAGkBAAAH/////ADIMWVNjYWxlIEluZGV4AAANQAUABkZvcm1hdAAAD0AFAAlQcmVjaXNpb24ACUAFAANGaXQADkAw/////wVMYWJlbAAWQCERVXNlIERlZmF1bHQgTGFiZWwAEkAhDUxhYmVsIFZpc2libGUACUAKAANNaW4ACUAKAANNYXgASwDxAAAAAAAAAAEgY2x1c3Rlcl9HcmFwaCBTY2FsZSBTZXR0aW5ncy5jdGwAIkBQAAgANAA1ADYANwA4ADkAOgA7BlhTY2FsZQAAFEBAAAH/////ADwHWVNjYWxlcwAPQAUACUJhciBTdHlsZQANQAIAB0ZpbGwgVG8AE0AHAAxGaWxsL1B0Q29sb3IAABFABQAKTGluZSBTdHlsZQAAEUAFAApMaW5lIFdpZHRoAAALQAcABUNvbG9yAA1ABQAGSW50ZXJwAAARQAUAC1BvaW50IFN0eWxlAEgA8QAAAAAAAAABH2NsdXN0ZXJfR3JhcGggUGxvdCBTZXR0aW5ncy5jdGwAIEBQAAgAPgA/AEAAQQBCAEMARABFBFBsb3QAABJAQAAB/////wBGBVBsb3RzABNACgANVXBkYXRlIFBlcmlvZAAVQAoADkhpc3RvcnkgTGVuZ3RoAAAUQHAACAAAAAIAAAZNeS5SZWYAABBAIQtJcyBDb250cm9sPwAWQDD/////DENoYW5uZWwgUGF0aAAAGkBAAAH/////AEwNQ2hhbm5lbCBQYXRocwAQQFMLQ3VzdG9tIERhdGEAqwDxxieWWAAAAAEgY2x1c3Rlcl9TY3JlZW4gSXRlbSBTZXR0aW5ncy5jdGwAgkBQADYAAAABAAIAAwAEAAUABgAHAAgACQAKAAsADAANABIAEwAUABUAFgAXABgAGQAaABsAHAAdAB4AHwAgACEAIgAjACQAJQAmACcAKAApACoALAAuAC8AMAAxADMAPAA9AEcASABJAEoASwBNAE4LU2NyZWVuIEl0ZW0AEkBAAAH/////AE8FSXRlbXMADkAw/////wROYW1lAAAUQDD/////C0Rlc2NyaXB0aW9uAVMA8QAAAAAAAAABH2VudW1fVXNlciBBZG1pbiBQZXJtaXNzaW9ucy5jdGwBK0AWAA0HRGVmYXVsdA5BZG1pbmlzdHJhdGlvbhdDaGFubmVsIFNjYWxpbmcgVXRpbGl0eRFBZGQgRGlzcGxheSBJdGVtcxNDaGFuZ2UgVXNlciBQcm9maWxlI0VkaXQgU3RpbXVsdXMgUHJvZmlsZSBFZGl0b3IgSGVhZGVyGkVkaXQgRGlzcGxheSBJdGVtIFNldHRpbmdzG01vZGVsIFBhcmFtZXRlciBDYWxpYnJhdGlvbhJSdW50aW1lIEFsYXJtIEVkaXQPRWRpdCBUb29scyBNZW51FkVkaXQgRW5naW5lIENvbXBvbmVudHMaQ29uZmlndXJlIFZpc2libGUgQ2hhbm5lbHMNRmF1bHQgTWFuYWdlcgAAClBlcm1pc3Npb24AAAxAIQdMb2FkZWQ/ABRAIQ9BbHdheXMgVmlzaWJsZT8AVwDxAAAAAAAAAAEkY2x1c3Rlcl9FbnRpcmUgU2NyZWVuIERlZmluaXRpb24uY3RsACpAUAAKAFAAUQBSAAUAAQACAAYAUwBUAFULU2NyZWVuLkRhdGEAJkBAAAH/////AFYZU2NyZWVuIEl0ZW0gQ2x1c3RlciBBcnJheQABAFcAAAABAAAAAAAAAAxFbXB0eSBTY3JlZW4AAAAAAAARZAAAAAAAAAAAAAAAAQAAAAAA</Data>
				</Variant>
			</Property>
			<Property Name="Screen Order">
				<I32Array>
					<Elem>4452</Elem>
				</I32Array>
			</Property>
			<Property Name="EscapeEnabled">
				<Boolean>false</Boolean>
			</Property>
			<Property Name="ShowPropPageOnDrop">
				<Boolean>true</Boolean>
			</Property>
			<Property Name="Workspace Loc and Size Left">
				<U16>0</U16>
			</Property>
			<Property Name="Workspace Loc and Size Top">
				<U16>0</U16>
			</Property>
			<Property Name="Workspace Loc and Size Right">
				<U16>812</U16>
			</Property>
			<Property Name="Workspace Loc and Size Bottom">
				<U16>660</U16>
			</Property>
		</Properties>
		<Errors />
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/TestWorkspaceAPI/TestWorkspaceAPI.nivssdf sha256=2e5126ee26c605a32638ccae7e18e653b7c9e80d2070186e08c17c5ec0655df6 bytes=137167 -->
## FILE: tests/testutilities/legacy_files/TestWorkspaceAPI/TestWorkspaceAPI.nivssdf

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/TestWorkspaceAPI/TestWorkspaceAPI.nivssdf`
- sha256: `2e5126ee26c605a32638ccae7e18e653b7c9e80d2070186e08c17c5ec0655df6`
- bytes: 137167

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2010" Minor="0" Fix="0" Build="4" />
	<Content>Definition</Content>
	<Root Name="TestWorkspaceAPI" TypeGUID="03D3BA22-1485-13A6-56BD17DA950CCD00">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>TestWorkspaceAPI</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.6</String>
			</Property>
			<Property Name="Creator">
				<String>Administrator</String>
			</Property>
			<Property Name="Creation Date">
				<Double>3324654475.359375</Double>
			</Property>
		</Properties>
		<Errors />
		<TargetSections Name="Targets Section" TypeGUID="eb379619-68d7-4d81-be90-c0bc511cdc10">
			<Description />
			<Properties />
			<Errors />
			<Target Name="Controller" TypeGUID="775504BB-1485-13A6-56755DBF2C326980">
				<Description />
				<Properties>
					<Property Name="IP Address">
						<String>localhost</String>
					</Property>
					<Property Name="Control Rate">
						<Double>1</Double>
					</Property>
					<Property Name="HS Port">
						<I32>2040</I32>
					</Property>
					<Property Name="LS Port">
						<I32>2050</I32>
					</Property>
					<Property Name="HS Port Timeout">
						<I32>1000</I32>
					</Property>
					<Property Name="LS Port Timeout">
						<I32>1000</I32>
					</Property>
					<Property Name="Control Loop Processor">
						<I32>-2</I32>
					</Property>
					<Property Name="Streamed Channels">
						<I32>512</I32>
					</Property>
					<Property Name="Stream Rate">
						<I32>1</I32>
					</Property>
					<Property Name="Secondary Control Loop Processor">
						<I32>-2</I32>
					</Property>
					<Property Name="OS">
						<String>Windows</String>
					</Property>
					<Property Name="Engine Rate">
						<Double>100</Double>
					</Property>
					<Property Name="Execution Mode">
						<U32>0</U32>
					</Property>
					<Property Name="TS_Custom_Dev">
						<String />
					</Property>
					<Property Name="daq">
						<Variant>
							<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
							<Data>AAAAYwkAgAAAAAADABRAMP////8KREFRIERldmljZQAAJ0AHACBQcmltYXJ5IENvbnRyb2wgTG9vcCByYXRlICh1c2VjKQAAEEBQAAIAAAABBGRhdGEAAAEAAgAAAAAAACcQAAAAAA==</Data>
						</Variant>
					</Property>
					<Property Name="ts">
						<U32>0</U32>
					</Property>
					<Property Name="Filter Watchdog Errors">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Filter DAQ Errors">
						<Boolean>false</Boolean>
					</Property>
				</Properties>
				<Errors />
				<Section Name="System Channels" TypeGUID="03D3B753-1485-13A6-56B10ED0820CF410">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="Actual Loop Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Hz" BitFields="1">
						<Description>The execution rate of the Primary Control Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100000</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Index" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>The compiled index of the current procedure step</Description>
						<Properties>
							<Property Name="ID">
								<I32>100001</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The decimation of the Data Processing Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100002</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Time" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>The relative system time of the VeriStand Engine according to the iteration count and Delta T of the Primary Control Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100003</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100004</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="DAQ Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The last reported error code from a DAQmx function call. The value zero indicates no error has occurred.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100005</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Delta T" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>The period in seconds of the Primary Control Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100006</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Compiler Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100007</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 1" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>An internal register used by procedures to maintain the stack location when a procedure is preempted by a higher priorty procedure</Description>
						<Properties>
							<Property Name="ID">
								<I32>100008</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 2" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>An internal register used by procedures to maintain the stack location when a procedure is preempted by a higher priorty procedure</Description>
						<Properties>
							<Property Name="ID">
								<I32>100009</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 3" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>An internal register used by procedures to maintain the stack location when a procedure is preempted by a higher priorty procedure</Description>
						<Properties>
							<Property Name="ID">
								<I32>100010</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Resume Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100011</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 4" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>An internal register used by procedures to maintain the stack location when a procedure is preempted by a higher priorty procedure</Description>
						<Properties>
							<Property Name="ID">
								<I32>100012</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 5" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>An internal register used by procedures to maintain the stack location when a procedure is preempted by a higher priorty procedure</Description>
						<Properties>
							<Property Name="ID">
								<I32>100013</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 6" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>An internal register used by procedures to maintain the stack location when a procedure is preempted by a higher priorty procedure</Description>
						<Properties>
							<Property Name="ID">
								<I32>100014</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>The ID of the alarm that has tripped</Description>
						<Properties>
							<Property Name="ID">
								<I32>100015</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>The ID of the alarm that has tripped</Description>
						<Properties>
							<Property Name="ID">
								<I32>100016</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>The ID of the alarm that has tripped</Description>
						<Properties>
							<Property Name="ID">
								<I32>100017</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>The value of the channel that tripped the alarm</Description>
						<Properties>
							<Property Name="ID">
								<I32>100018</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>The value of the channel that tripped the alarm</Description>
						<Properties>
							<Property Name="ID">
								<I32>100019</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>The value of the channel that tripped the alarm</Description>
						<Properties>
							<Property Name="ID">
								<I32>100020</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="RT Engine Build" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>A value representing the build number of the NI VeriStand Engine</Description>
						<Properties>
							<Property Name="ID">
								<I32>100021</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Loop Duration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The duration of the Primary Control Loop in nanoseconds</Description>
						<Properties>
							<Property Name="ID">
								<I32>100022</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Loop Duration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The duration of the Data Processing Loop in nanoseconds</Description>
						<Properties>
							<Property Name="ID">
								<I32>100023</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Command" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="3">
						<Description>Internally commands the RT system with the following numeric values:

0: None
1: Restart System
2: Reset System
3: Shut Down System
4: Reboot System</Description>
						<Properties>
							<Property Name="ID">
								<I32>100024</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Streamed Channel Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of channels that the VeriStand Engine is currently streaming to the host</Description>
						<Properties>
							<Property Name="ID">
								<I32>100025</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Max Streamed Channels" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The maximum number of channels that the VeriStand Engine can stream to the host</Description>
						<Properties>
							<Property Name="ID">
								<I32>100026</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Model Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the models have not completed their execution in time</Description>
						<Properties>
							<Property Name="ID">
								<I32>100027</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Clients" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100028</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Maximum GENs" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of stimulus profile generators instantiated by the system</Description>
						<Properties>
							<Property Name="ID">
								<I32>100029</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Generator Engine State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The current state of the stimulus profile generator engine

0: Idle
1: Running
2: Stopped
3: Paused</Description>
						<Properties>
							<Property Name="ID">
								<I32>100030</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Watchdog Timer" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The amount of time in nanoseconds since the Watchdog Timer Loop last executed. The Watchdog Timer Loop is set to execute at a rate of 10Hz.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100031</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HS TCP Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the streaming data gets overwritten.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100032</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Host IP" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The 32-bit integer IP Address of the connected host. A zero value indicates no host is connected to the VeriStand Engine.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100033</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Trace Enabled Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100034</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Detailed Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100035</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="VI Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100036</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Trace Buffer Size" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100037</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Thread Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100038</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 39" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100039</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 40" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100040</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 41" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100041</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 42" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100042</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 43" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100043</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 44" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100044</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Iterations" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100045</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Min Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100046</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Actual Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100047</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Failure Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The failure count of current analysis settings</Description>
						<Properties>
							<Property Name="ID">
								<I32>100048</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Analysis State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The state of the analysis sub-system on the RT execution host</Description>
						<Properties>
							<Property Name="ID">
								<I32>100049</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="TCP Data Packet Loss" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the VeriStand Engine fails to send a data packet to the host. A non-zero number can indicate data loss in logged data. The value is reset every time a Workspace connects to the VeriStand Engine.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100050</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 51" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100051</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 52" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100052</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 53" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100053</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 54" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100054</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 55" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100055</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 56" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100056</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 57" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100057</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 58" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100058</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 59" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100059</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 60" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100060</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 61" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100061</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 62" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100062</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 63" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100063</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 64" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100064</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 65" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100065</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 66" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100066</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 67" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100067</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 68" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100068</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 69" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100069</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 70" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100070</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 71" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100071</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 72" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100072</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 73" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100073</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 74" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100074</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 75" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100075</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 76" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100076</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 77" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100077</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 78" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100078</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 79" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100079</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 80" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100080</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 81" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100081</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 82" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100082</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 83" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100083</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 84" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100084</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 85" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100085</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 86" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100086</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 87" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100087</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 88" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100088</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 89" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100089</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 90" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100090</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 91" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100091</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="AO1 Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100092</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Loop Wakeup Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Enum" BitFields="1">
						<Description>The wakeup status of the Primary Control Loop.

0: Normal
1: Aborted
2: Asynchronous wakeup
3: Timing source error
4: Timed loop error
5: Timeout</Description>
						<Properties>
							<Property Name="ID">
								<I32>100093</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HD Free Space" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100094</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP-LP Overwrite" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Primary Control Loop timed out writing channel data to the Data Processing Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100095</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Data Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Data Processing Loop timed out writing channel data to the Communication Send Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100096</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Primary Control Loop reported being late</Description>
						<Properties>
							<Property Name="ID">
								<I32>100097</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Data Processing Loop reported being late</Description>
						<Properties>
							<Property Name="ID">
								<I32>100098</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Log Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>The state of the logging sub-system on the RT execution host</Description>
						<Properties>
							<Property Name="ID">
								<I32>100099</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
				</Section>
				<Section Name="Hardware" TypeGUID="775504AB-1485-13A6-560018C1F4E3EEE1">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Chassis" TypeGUID="03D3BACD-1485-13A6-56E99D97B7543BAF">
						<Description />
						<Properties>
							<Property Name="Chassis master active edge">
								<I32>0</I32>
							</Property>
							<Property Name="Chassis master clock source">
								<I32>0</I32>
							</Property>
							<Property Name="Chassis master export clock on line">
								<I32>0</I32>
							</Property>
							<Property Name="Chassis master export sample clock">
								<I32>0</I32>
							</Property>
							<Property Name="Chassis master slope">
								<I32>0</I32>
							</Property>
							<Property Name="Chassis master trigger line">
								<I32>0</I32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Timing and Sync" TypeGUID="03D3BAED-1485-13A6-56E20B50F6E06D94">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="DAQ" TypeGUID="77550612-1485-13A6-56570AB5032158E9">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="FPGA" TypeGUID="03D3B659-1485-13A6-5652D8A07328ECB7">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="Data Sharing" TypeGUID="d56f3ac1-7b2c-422c-9d11-fd9cc7abf2a5">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="XNET" TypeGUID="6b693e6d-67b1-40b8-8108-4a4cc3147721">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
								</Property>
							</Properties>
							<Errors />
							<Section Name="LIN" TypeGUID="c9c30728-42cb-4dc3-b054-b80e7a54e833">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="FlexRay" TypeGUID="e33fae90-03f1-4f76-b2f1-6eb8fcac2676">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="CAN" TypeGUID="6c5bb91f-0da7-407d-aefc-acbe49c768df">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
					</Section>
				</Section>
				<Section Name="Stimulus" TypeGUID="03D3B7FF-1485-13A6-56B2328F9511AC8B">
					<Description />
					<Properties>
						<Property Name="Analysis Buffer Size">
							<I32>10000</I32>
						</Property>
						<Property Name="Analysis Result Size">
							<I32>5000</I32>
						</Property>
						<Property Name="Aux Buffer Size">
							<I32>10000</I32>
						</Property>
						<Property Name="Max Gen Maps">
							<I32>256</I32>
						</Property>
						<Property Name="Max Steps">
							<I32>128</I32>
						</Property>
					</Properties>
					<Errors />
					<Section Name="GEN001" TypeGUID="03D3B80E-1485-13A6-56528B60DC00DC89">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="GEN001 State" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100100</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100101</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100102</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100103</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100104</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100105</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100106</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100107</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100108</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100109</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100110</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100111</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100112</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100113</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100114</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100115</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100116</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100117</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100118</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100119</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
					</Section>
					<Section Name="GEN002" TypeGUID="03D3B80E-1485-13A6-56528B60DC00DC89">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="GEN002 State" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100120</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100121</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100122</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100123</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100124</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100125</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100126</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100127</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100128</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100129</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100130</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100131</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100132</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100133</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100134</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100135</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100136</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100137</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100138</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100139</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
					</Section>
					<Section Name="GEN003" TypeGUID="03D3B80E-1485-13A6-56528B60DC00DC89">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="GEN003 State" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100140</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100141</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100142</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100143</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100144</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100145</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100146</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100147</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100148</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100149</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100150</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100151</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100152</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100153</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100154</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100155</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100156</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100157</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100158</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100159</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
					</Section>
					<Section Name="GEN004" TypeGUID="03D3B80E-1485-13A6-56528B60DC00DC89">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="GEN004 State" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100160</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100161</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100162</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100163</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100164</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100165</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100166</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100167</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100168</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100169</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100170</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100171</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100172</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100173</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100174</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100175</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100176</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100177</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100178</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100179</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
					</Section>
					<Section Name="GEN005" TypeGUID="03D3B80E-1485-13A6-56528B60DC00DC89">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="GEN005 State" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100180</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100181</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100182</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100183</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100184</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100185</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100186</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100187</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100188</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100189</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100190</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100191</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100192</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100193</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100194</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100195</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100196</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100197</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100198</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100199</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
					</Section>
					<Section Name="GEN006" TypeGUID="03D3B80E-1485-13A6-56528B60DC00DC89">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="GEN006 State" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100200</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100201</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100202</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100203</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100204</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100205</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100206</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100207</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100208</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100209</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100210</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100211</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100212</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100213</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100214</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100215</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100216</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100217</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100218</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100219</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
					</Section>
					<Section Name="GEN007" TypeGUID="03D3B80E-1485-13A6-56528B60DC00DC89">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="GEN007 State" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100220</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100221</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100222</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100223</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100224</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100225</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100226</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100227</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100228</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100229</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100230</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100231</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100232</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100233</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100234</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100235</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100236</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100237</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100238</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100239</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
					</Section>
					<Section Name="GEN008" TypeGUID="03D3B80E-1485-13A6-56528B60DC00DC89">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="GEN008 State" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100240</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100241</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100242</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100243</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100244</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100245</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100246</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100247</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100248</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100249</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100250</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100251</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100252</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100253</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100254</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100255</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100256</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100257</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100258</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100259</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
					</Section>
					<Section Name="GEN009" TypeGUID="03D3B80E-1485-13A6-56528B60DC00DC89">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="GEN009 State" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100260</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100261</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100262</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100263</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100264</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100265</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100266</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100267</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100268</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100269</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100270</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100271</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100272</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100273</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100274</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100275</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100276</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100277</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100278</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100279</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
					</Section>
					<Section Name="GEN010" TypeGUID="03D3B80E-1485-13A6-56528B60DC00DC89">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="GEN010 State" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100280</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100281</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100282</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100283</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100284</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100285</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100286</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100287</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100288</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100289</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100290</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100291</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100292</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100293</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100294</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100295</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100296</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100297</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100298</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties>
								<Property Name="ID">
									<I32>100299</I32>
								</Property>
							</Properties>
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
					</Section>
				</Section>
				<Section Name="Simulation Models" TypeGUID="03D3B937-1485-13A6-5600F2871E269F9A">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Models" TypeGUID="03D3B976-1485-13A6-5604255F981010CE">
						<Description />
						<Properties />
						<Errors />
						<Section Name="sinewave" TypeGUID="03D3B9C4-1485-13A6-561FC9BB21813875">
							<Description />
							<Properties>
								<Property Name="Base Rate">
									<Double>10000</Double>
								</Property>
								<Property Name="Build Data">
									<Variant>
										<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
										<Data>AAAAFAkAgAAAAAABAAQAAAABAAAAAAAA</Data>
									</Variant>
								</Property>
								<Property Name="DLL Size">
									<I32>10240</I32>
								</Property>
								<Property Name="DLL Timestamp">
									<Double>3351020638</Double>
								</Property>
								<Property Name="Decimation">
									<I32>1</I32>
								</Property>
								<Property Name="ID">
									<I32>0</I32>
								</Property>
								<Property Name="Import Definition ID">
									<I32>0</I32>
								</Property>
								<Property Name="MD5">
									<String>854e31b31a325f1175c026374631107b</String>
								</Property>
								<Property Name="Model Timestamp">
									<Double>0</Double>
								</Property>
								<Property Name="NIVeriStandServer Port">
									<U32>6012</U32>
								</Property>
								<Property Name="Processor">
									<I32>-2</I32>
								</Property>
								<Property Name="Segment Vectors">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Show Unnamed Signals">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="User Rate">
									<Double>10000</Double>
								</Property>
								<Property Name="blocks only">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="visible">
									<U32>0</U32>
								</Property>
								<Property Name="DLL Path">
									<DependentFile Type="Relative" Path="sinewave.dll">
										<Version />
										<ForceDownload>false</ForceDownload>
										<RTDestination>c:\ni-rt\NIVeriStand2010\Models\sinewave.dll</RTDestination>
										<SupportedTarget>PharLap &amp; Windows</SupportedTarget>
										<MD5>854e31b31a325f1175c026374631107b</MD5>
									</DependentFile>
								</Property>
								<Property Name="Model Path">
									<DependentFile Type="Absolute" Path="">
										<Version />
										<RTDestination />
										<SupportedTarget />
										<MD5 />
									</DependentFile>
								</Property>
							</Properties>
							<Errors />
							<Section Name="Inports" TypeGUID="03D3B9E3-1485-13A6-56035B19B2245EB3">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In1" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
									<Description />
									<Properties>
										<Property Name="ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Index">
											<I32>0</I32>
										</Property>
										<Property Name="Mapped ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Task ID">
											<I32>0</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Outports" TypeGUID="03D3B9F3-1485-13A6-5698C14838D6AA3C">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out1" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
									<Description />
									<Properties>
										<Property Name="ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Index">
											<I32>1</I32>
										</Property>
										<Property Name="Mapped ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Task ID">
											<I32>0</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Execution" TypeGUID="03D3BA9F-1485-13A6-56E3D5196780015F">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Model Command" TypeGUID="03D3BABE-1485-13A6-56C34B877844B2C1" RowDim="1" ColDim="1" Units="" BitFields="11">
									<Description>0: Start
1: Pause
2: Reset
3: Save
4: Restore</Description>
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Model Time" TypeGUID="03D3BAAE-1485-13A6-5606A77AB57A7FC9" RowDim="1" ColDim="1" Units="sec" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Model Status" TypeGUID="03D3BB6A-1485-13A6-5643A7AFDA3A2658" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description>0: Running
1: Paused
2: Resetting
3: Idle
4: Stopped
5: Restoring
6: Saving</Description>
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Parameters" TypeGUID="03D3BB0C-1485-13A6-56E10CEFF755E7D3">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="Signals" TypeGUID="03D3BA31-1485-13A6-567CA69E9D2E71D5">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
					</Section>
					<Section Name="Execution Order" TypeGUID="03D3B966-1485-13A6-569CFF8A449BF90A">
						<Description />
						<Properties />
						<Errors />
					</Section>
				</Section>
				<Section Name="Alarms" TypeGUID="03D3B782-1485-13A6-56F58B35B6CBA484">
					<Description />
					<Properties>
						<Property Name="Alarm Rate">
							<I32>1</I32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Procedures" TypeGUID="03D3B7B1-1485-13A6-56649C7783203F22">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="Custom Devices" TypeGUID="03D3BB79-1485-13A6-5605EB7AFD7405AC">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="User Channel" TypeGUID="03D3B6B7-1485-13A6-567BE1E1E0DF999A">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="TEST_ID" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>1</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>124123</Elem>
						</DefaultValue>
					</Channel>
				</Section>
				<Section Name="Calculated Channels" TypeGUID="03D3B714-1485-13A6-56031C5F1CCB78A9">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="XNET Databases" TypeGUID="def5630b-577f-4ae9-9682-5f8ee445ee21">
					<Description />
					<Properties />
					<Errors />
				</Section>
			</Target>
		</TargetSections>
		<Section Name="Aliases" TypeGUID="e11f4519-09e6-4fb0-99df-2967c4313d67">
			<Description />
			<Properties />
			<Errors />
			<Alias Name="SinewaveIn1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/sinewave/Inports/In1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="SinewaveOut1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/sinewave/Outports/Out1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="TEST_ID" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/TEST_ID" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
		</Section>
		<Section Name="Data Sharing Network" TypeGUID="8288dbb9-8c87-4fda-9c66-acec90c46c03">
			<Description />
			<Properties>
				<Property Name="CD Status">
					<U32>2</U32>
				</Property>
			</Properties>
			<Errors />
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/logging_helpers.py sha256=135ff6027cb07024b1f2b40892f4488ff76042563b9bbef21a4f977c0860e656 bytes=247 -->
## FILE: tests/testutilities/logging_helpers.py

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/logging_helpers.py`
- sha256: `135ff6027cb07024b1f2b40892f4488ff76042563b9bbef21a4f977c0860e656`
- bytes: 247

````python
import logging


def enable_console_logging(log=None, level=logging.DEBUG):
    logger = logging.getLogger(log)
    logger.setLevel(level=level)
    console_ch = logging.StreamHandler()
    logger.addHandler(console_ch)
    return logger
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/rtseqrunner.py sha256=90e26413766d4bf0bc34f448444948e4d869b47dee0b52e0f622a0bc374ae2df bytes=1590 -->
## FILE: tests/testutilities/rtseqrunner.py

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/rtseqrunner.py`
- sha256: `90e26413766d4bf0bc34f448444948e4d869b47dee0b52e0f622a0bc374ae2df`
- bytes: 1590

````python
import os
import tempfile
import clr
from niveristand import realtimesequencetools
from niveristand.clientapi._datatypes import DataType
import pytest
import testutilities.configutilities as configutilities


rtseq_dll_path = os.path.join(
    configutilities.getbinariesfolder(),
    "NationalInstruments.VeriStand.RealTimeSequenceUtilities.dll",
)


def _check_can_run_local():
    if not os.path.isfile(rtseq_dll_path):
        pytest.skip("RealTimeSequenceRunner assembly not present.")


def run_rtseq_local(filepath, channel_names=[], channel_values=[], deltat=1):
    _check_can_run_local()
    clr.AddReference(rtseq_dll_path)
    from NationalInstruments.VeriStand.RealTimeSequenceUtilities import RealTimeSequenceRunner

    res = RealTimeSequenceRunner.Run(filepath, channel_names, channel_values, float(deltat))
    return res


def assert_run_python_equals_rtseq(func, expected):
    tempfolder = tempfile.mkdtemp()
    filename = realtimesequencetools.save_py_as_rtseq(func, tempfolder)
    rtseq_result = run_rtseq_local(filename)
    py_result = func()
    if isinstance(py_result, DataType):
        py_result = py_result.value
    assert py_result == expected
    assert rtseq_result.Value == py_result


def run_rtseq_in_VM(func, deltat=1):
    from NationalInstruments.VeriStand.Data import VoidValue

    filename = realtimesequencetools.save_py_as_rtseq(func, None)
    rtseq_result = run_rtseq_local(filename, deltat=deltat)
    if isinstance(rtseq_result, VoidValue):
        return None
    return rtseq_result.Value
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/testfunctions.py sha256=92dbd0bb347cd7bbc733d0a2df1aebd83a97868ffa7d57602cdaf06c982a3969 bytes=5187 -->
## FILE: tests/testutilities/testfunctions.py

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/testfunctions.py`
- sha256: `92dbd0bb347cd7bbc733d0a2df1aebd83a97868ffa7d57602cdaf06c982a3969`
- bytes: 5187

````python
import math
from math import pi
from niveristand import _decorators
from niveristand.clientapi._datatypes import (
    BooleanValue,
    BooleanValueArray,
    ChannelReference,
    DoubleValue,
    DoubleValueArray,
    I32Value,
    VectorChannelReference,
)
from niveristand.library.primitives import localhost_wait


def func_without_decorator():
    pass


@_decorators.nivs_rt_sequence
def empty_func():
    pass


@_decorators.nivs_rt_sequence
@_decorators.nivs_rt_sequence
def empty_func_with_double_decorator():
    pass


@_decorators.nivs_rt_sequence
def simple_local_assignment():
    a = I32Value(5)  # noqa: F841 it's ok for this variable to never be used


@_decorators.nivs_rt_sequence
def simple_float_local_assignment():
    a = DoubleValue(5.0)  # noqa: F841 it's ok for this variable to never be used


@_decorators.nivs_rt_sequence
def simple_assign_pi():
    a = DoubleValue(0.0)  # noqa: F841 it's ok for this variable to never be used
    a.value = math.pi
    a.value = pi


@_decorators.nivs_rt_sequence
def assign_untyped():
    a = math.pi  # noqa: F841 it's ok for this variable to never be used


@_decorators.nivs_rt_sequence
def return_var():
    a = DoubleValue(5)
    return a.value


@_decorators.nivs_rt_sequence
def return_var_value():
    a = DoubleValue(5)
    return a.value


@_decorators.nivs_rt_sequence
def return_var_invalid_value():
    a = DoubleValue(5)
    return a.value.value


@_decorators.nivs_rt_sequence
def return_named_type():
    return DoubleValue(5)


@_decorators.nivs_rt_sequence
def return_primitive_num():
    return 5.0


@_decorators.nivs_rt_sequence
def return_var_pi():
    a = DoubleValue(5)
    a.value = math.pi
    return a.value


@_decorators.nivs_rt_sequence
def return_untyped_symbol():
    return math.pi


@_decorators.nivs_rt_sequence
def return_true():
    a = BooleanValue(True)
    return a.value


@_decorators.nivs_rt_sequence
def return_false():
    a = BooleanValue(False)
    return a.value


@_decorators.nivs_rt_sequence
def return_boolean_array():
    a = BooleanValueArray([True, False])
    return a


@_decorators.nivs_rt_sequence
def return_double_array():
    a = DoubleValueArray([0, 1, 2, 3])
    return a


@_decorators.nivs_rt_sequence
def multiple_returns():
    a = DoubleValue(5)
    return a.value
    b = DoubleValue(5)
    return b.value


@_decorators.nivs_rt_sequence
def return_not_last():
    a = DoubleValue(5)
    return a.value
    a.value += 1


@_decorators.nivs_rt_sequence
def channel_ref_type_string():
    a = ChannelReference("Aliases/DesiredRPM")  # noqa: F841 it's ok not to be used


@_decorators.nivs_rt_sequence
def channel_ref_setter():
    a = ChannelReference("Aliases/DesiredRPM")
    a.value = 5


@_decorators.nivs_rt_sequence
def channel_ref_return():
    a = ChannelReference("Aliases/DesiredRPM")
    a.value = 5.0
    localhost_wait()
    return a.value


@_decorators.nivs_rt_sequence
def channel_ref_validate_getter():
    a = ChannelReference("Aliases/DesiredRPM")
    a.value = 5.0
    localhost_wait()
    b = DoubleValue(0)
    b.value = a.value
    return b.value


@_decorators.nivs_rt_sequence
def channel_ref_invalid_channel_set():
    a = ChannelReference("InvalidName")
    a.value = 5


@_decorators.nivs_rt_sequence
def channel_ref_invalid_channel_get():
    a = ChannelReference("InvalidName")
    b = DoubleValue(0)
    b.value = a.value


@_decorators.nivs_rt_sequence
def channel_ref_invalid_channel_transform():
    a = ChannelReference("InvalidName")  # noqa: F841 it's ok not to be used


@_decorators.nivs_rt_sequence
def channel_ref_array_type_string():
    a = VectorChannelReference(  # noqa: F841 it's ok not to be used
        "Targets/Controller/Simulation Models/Models/Engine Demo/Parameters/a"
    )


@_decorators.nivs_rt_sequence
def channel_ref_array_setter():
    a = VectorChannelReference(
        "Targets/Controller/Simulation Models/Models/Engine Demo/Parameters/a"
    )
    a[0].value = 5


@_decorators.nivs_rt_sequence
def channel_ref_array_return():
    a = VectorChannelReference(
        "Targets/Controller/Simulation Models/Models/Engine Demo/Parameters/a"
    )
    a[0].value = 5.0
    localhost_wait()
    return a[0].value


@_decorators.nivs_rt_sequence
def channel_ref_for_vector_channel():
    a = ChannelReference("Targets/Controller/Simulation Models/Models/Engine Demo/Parameters/a")
    a.value = 50


@_decorators.nivs_rt_sequence
def channel_ref_array_validate_getter():
    a = VectorChannelReference(
        "Targets/Controller/Simulation Models/Models/Engine Demo/Parameters/a"
    )
    a[3].value = 5.0
    localhost_wait()
    b = DoubleValue(0)
    b.value = a[3].value
    return b.value


@_decorators.nivs_rt_sequence
def a_value_value_assignment():
    a = DoubleValue(0)
    a.value = a.value.value
    return a.value


@_decorators.nivs_rt_sequence
def a_value_value_assign_to():
    a = DoubleValue(0)
    a.value.value = 1
    return a.value
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/validation.py sha256=83257d2db18d7c876de81bf28161974c1ca1a718e39658ca3c897a99bc7e476f bytes=1777 -->
## FILE: tests/testutilities/validation.py

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/validation.py`
- sha256: `83257d2db18d7c876de81bf28161974c1ca1a718e39658ca3c897a99bc7e476f`
- bytes: 1777

````python
import inspect
from niveristand._decorators import rt_seq_mode_id


def test_validate(testmodule):
    funcs = [
        n
        for n, f in inspect.getmembers(testmodule, inspect.isfunction)
        if getattr(f, rt_seq_mode_id, None) is not None
    ]
    test_lists = {}
    for a in dir(testmodule):
        if (
            a.startswith("run_tests")
            or a.startswith("skip_tests")
            or a.startswith("transform_tests")
            or a.startswith("fail_transform_tests")  # noqa: W504
            or a.startswith("python_tests")
            or a.startswith("py_only_different_behavior_tests")  # noqa: W504
            or a.startswith("py_only_errs")
        ):
            test_lists[a] = testmodule.__dict__.get(a)
    _validate_special_lists_are_subsets_of_overall_lists(
        test_lists, "py_only_different_behavior_tests", "run_tests"
    )
    _validate_special_lists_are_subsets_of_overall_lists(test_lists, "py_only_errs", "run_tests")
    final_list = []
    for key, value in test_lists.items():
        for item in value:
            final_list.append(item[0].__name__)
    not_assigned = [f for f in funcs if f not in final_list and not f.startswith("_")]
    assert not_assigned == [], (
        "Test "
        + not_assigned.__str__()
        + " in "
        + testmodule.__name__
        + " is not added to any list."
    )


def _validate_special_lists_are_subsets_of_overall_lists(
    test_lists, special_list_name, overall_list_name
):
    if special_list_name in test_lists:
        assert set(test_lists[special_list_name]).issubset(set(test_lists[overall_list_name])), (
            special_list_name + "list is not a subset of the " + overall_list_name + " list."
        )
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tox.ini sha256=7976aefb34ed278085fc281f3136deb576a2fd7d35e23933a4fc2817562dabd2 bytes=2475 -->
## FILE: tox.ini

- repository: `ni/niveristand-python`
- source_path: `tox.ini`
- sha256: `7976aefb34ed278085fc281f3136deb576a2fd7d35e23933a4fc2817562dabd2`
- bytes: 2475

````ini
# tox (https://tox.readthedocs.io/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox" from this directory.
#
# Examples:
#   * Run Python 3.11 tests:
#       `tox -e py311`
#   * Run linter:
#       `tox -e flake8`
#   * Build docs:
#       `tox -e docs`
#   * Run several options at once:
#       `tox -e py39,py311,flake8,docs`

[tox]
envlist = py38, py39, py310, py311, py312, flake8

[testenv]
commands = pytest --junitxml={envlogdir}/junit-{envname}.xml {posargs}
setenv = PYTHONPATH = {toxinidir}/tests
    vsdev.yaml = {toxinidir}/tests/vsdev.yaml
passenv = vsdev.json
deps =
    pytest
    pythonnet~=3.0.1
    pyyaml
    numpy

[pytest]
norecursedirs = .git examples docs dist tests/legacy
junit_suite_name = veristand_python

[testenv:flake8]
basepython = python
skip_install = true
deps =
    flake8
    flake8-docstrings>=0.2.7
    flake8-import-order>=0.9
    flake8-junit-report
commands =
    - flake8 src/niveristand/ tests/ examples/ setup.py --exclude tests/legacy,tests/sdf_api,_auto_generated_classes.py,src/niveristand/**/__init__.py --output-file {envlogdir}/{envname}.txt --tee
    flake8_junit {envlogdir}/{envname}.txt {envlogdir}/junit-{envname}.xml

[flake8]
# D100-D105, D107: Ignore docstring errors during development
# D203 1 blank line required before class docstring
# D401 First line should be in imperative mood
# H903 Windows style line endings not allowed in code (git should autoconvert to LF)
# I201 Missing newline before sections or imports makes files longer for no good reason
# W503: Line break occurred before a binary operator (black formatting contradicts this)
# E203: Whitespace before ':' (black formatting contradicts this)
ignore = D100,D101,D102,D103,D104,D105,D107,D203,D401,H903,I201,W503,E203
exclude =.git,__pycache__,docs/source/conf.py,old,build,dist,objects
max-line-length = 120
import-order-style = google

[testenv:docs]
description = invoke sphinx-build to build the HTML docs
basepython = python
deps =
    -rdocs/requirements.txt
commands =
    sphinx-build -a -E -c docs -d "{toxworkdir}/docs_doctree" docs "{toxworkdir}/docs_out" --color -bhtml
    python -c 'import pathlib; print("DOCUMENTATION: file://\{0\}".format(str(pathlib.Path(r"{toxworkdir}") / "docs_out" / "index.html").replace("\\", "/")))'
````
