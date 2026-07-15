# NI OSS SOURCE SNAPSHOT: niveristand-python

<!--NI_OSS_SNAPSHOT repo=ni/niveristand-python commit=9ced536d3414f04a8b6b9315ce4c71b879d02a96 -->

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ProceduresTest/ProceduresTest.nivssdf sha256=959a20098dc91c6e19dfa70b96d0acb84063de1dcb4c6b65e277731f382932d1 bytes=158858 -->
## FILE: tests/testutilities/legacy_files/ProceduresTest/ProceduresTest.nivssdf

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ProceduresTest/ProceduresTest.nivssdf`
- sha256: `959a20098dc91c6e19dfa70b96d0acb84063de1dcb4c6b65e277731f382932d1`
- bytes: 158858

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2013" Minor="0" Fix="0" Build="1" />
	<Content>Definition</Content>
	<Root Name="ProceduresTest" TypeGUID="03D3BA22-1485-13A6-56BD17DA950CCD00">
		<Description>Test configuration for running various procedures.

Test ID = 3000</Description>
		<Properties>
			<Property Name="Name">
				<String>ProceduresTest</String>
			</Property>
			<Property Name="Version">
				<String>1.0.5.63</String>
			</Property>
			<Property Name="Creator">
				<String>Administrator</String>
			</Property>
			<Property Name="Creation Date">
				<Double>3319799209.0740933</Double>
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
					<Property Name="TL sleep time">
						<U32>0</U32>
					</Property>
					<Property Name="TS_Custom_Dev">
						<String />
					</Property>
					<Property Name="ctr decimation">
						<U32>1</U32>
					</Property>
					<Property Name="custom loop time">
						<U32>1</U32>
					</Property>
					<Property Name="daq">
						<Variant>
							<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
							<Data>AAAAYwkAgAAAAAADABRAMP////8KREFRIERldmljZQAAJ0AHACBQcmltYXJ5IENvbnRyb2wgTG9vcCByYXRlICh1c2VjKQAAEEBQAAIAAAABBGRhdGEAAAEAAgAAAAAAACcQAAAAAA==</Data>
						</Variant>
					</Property>
					<Property Name="daq timeout">
						<U32>1000</U32>
					</Property>
					<Property Name="dio decimation">
						<U32>1</U32>
					</Property>
					<Property Name="loop time">
						<U32>10000</U32>
					</Property>
					<Property Name="name">
						<String />
					</Property>
					<Property Name="path">
						<Variant>
							<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
							<Data>AAAAuQkAgAAAAAADAB5AMv////8VU2ltdWxhdGlvbiBtb2RlbCBwYXRoAG0A8QAAAAAAAAACH1N5c3RlbSBFeHBsb3JlciBGcmFtZXdvcmsubHZsaWIdUGF0aCByZWxhdGl2ZSBvciBhYnNvbHV0ZS5jdGwAJ0AWAAIIQWJzb2x1dGUIUmVsYXRpdmUACVBhdGggdHlwZQAQQFAAAgAAAAEFVmFsdWUAAQACUFRIMAAAAAQAAAAAAAAAAAAA</Data>
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
					<Property Name="DIO Rate">
						<Double>100</Double>
					</Property>
					<Property Name="Timing Source Settings">
						<U16>0</U16>
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
					<Channel Name="Command Index" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="index" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100001</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
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
					<Channel Name="Alarm Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="Compiler Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
						<Description>Deprecated</Description>
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
						<Description>Deprecated</Description>
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
						<Description>Deprecated</Description>
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
					<Channel Name="Resume Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
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
						<Description>Deprecated</Description>
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
						<Description>Deprecated</Description>
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
						<Description>Deprecated</Description>
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
					<Channel Name="Tripped Low Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="3">
						<Description>Deprecated</Description>
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
					<Channel Name="Tripped Medium Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="3">
						<Description>Deprecated</Description>
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
					<Channel Name="Tripped High Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="3">
						<Description>Deprecated</Description>
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
					<Channel Name="Tripped Low Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
						<Description>Deprecated</Description>
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
					<Channel Name="Tripped Medium Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
						<Description>Deprecated</Description>
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
					<Channel Name="Tripped High Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
						<Description>Deprecated</Description>
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
					<Channel Name="System Command" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
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
					<Channel Name="Streamed Channel Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
						<Description />
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
					<Channel Name="Max Streamed Channels" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
						<Description />
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
					<Channel Name="Model Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
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
					<Channel Name="Clients" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
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
					<Channel Name="Generator Engine State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
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
					<Channel Name="Absolute Time" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>Returns the current date and time in seconds relative to 12:00 a.m., Friday, January 1, 1904, Universal Time [01-01-1904 00:00:00]. This value is coerced from a 128-bit value to double precision, which may impact resolution.</Description>
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
					<Channel Name="System Time - Microseconds" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="usec" BitFields="1">
						<Description>The relative system time in microseconds of the VeriStand Engine according to the iteration count and Delta T of the Primary Control Loop</Description>
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
					<Channel Name="System Reserved 41" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 42" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 43" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 44" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="PC Timing - Iterations" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
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
					<Channel Name="PC Timing - Min Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ms" BitFields="3">
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
					<Channel Name="PC Timing - Actual Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ms" BitFields="1">
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
					<Channel Name="Failure Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
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
					<Channel Name="Analysis State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
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
					<Channel Name="WPL Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop attempted to write to a waveform read session within the NI VeriStand engine and timed out.</Description>
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
					<Channel Name="WPL TCP Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop attempted to write to the TCP loop (for a host waveform stream session) and timed out.</Description>
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
					<Channel Name="WPL Error Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop encountered an error.</Description>
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
					<Channel Name="WPL Error Code" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The last error code encountered by the waveform processing loop.</Description>
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
					<Channel Name="Streamed Waveform Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of waveforms that the VeriStand Engine is currently streaming to the host</Description>
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
					<Channel Name="System Reserved 56" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 57" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 58" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 59" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 60" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 61" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 62" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 63" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 64" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 65" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 66" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 67" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 68" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 69" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 70" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 71" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 72" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 73" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 74" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 75" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 76" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 77" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 78" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 79" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 80" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 81" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 82" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 83" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 84" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 85" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 86" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 87" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 88" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 89" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 90" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 91" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="AO1 Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="HP Loop Wakeup Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="HD Free Space" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="KB" BitFields="3">
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
					<Channel Name="Log Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Section Name="Alarm 1" TypeGUID="03D3B791-1485-13A6-56D2B019287A4256">
						<Description>Alarm used to trigger Alarm 1 Procedure. Just to test we can run procedures using alarms. Triggers on Alarm Channel 1</Description>
						<Properties>
							<Property Name="Channel Path">
								<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 1" />
							</Property>
							<Property Name="Delay">
								<Double>0</Double>
							</Property>
							<Property Name="Disabled Color">
								<U32>9868950</U32>
							</Property>
							<Property Name="High Limit">
								<Double>0</Double>
							</Property>
							<Property Name="High Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="ID">
								<U32>214239</U32>
							</Property>
							<Property Name="Log Trips">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="Low Limit">
								<Double>0</Double>
							</Property>
							<Property Name="Low Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Normal Color">
								<U32>6618880</U32>
							</Property>
							<Property Name="Priority">
								<U32>25</U32>
							</Property>
							<Property Name="Procedure Path">
								<DependentNode Path="Targets Section/Controller/Procedures/Alarm 1 Procedure" />
							</Property>
							<Property Name="State">
								<U32>1</U32>
							</Property>
							<Property Name="Trip Color">
								<U32>16711680</U32>
							</Property>
							<Property Name="Trip Message">
								<String />
							</Property>
							<Property Name="Group Number">
								<U32>0</U32>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Alarm 2" TypeGUID="03D3B791-1485-13A6-56D2B019287A4256">
						<Description>Used to trigger Alarm 2 Procedure. Triggered by Alarm Channel 2</Description>
						<Properties>
							<Property Name="Channel Path">
								<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 2" />
							</Property>
							<Property Name="Delay">
								<Double>0</Double>
							</Property>
							<Property Name="Disabled Color">
								<U32>9868950</U32>
							</Property>
							<Property Name="High Limit">
								<Double>0</Double>
							</Property>
							<Property Name="High Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="ID">
								<U32>262552</U32>
							</Property>
							<Property Name="Log Trips">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="Low Limit">
								<Double>0</Double>
							</Property>
							<Property Name="Low Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Normal Color">
								<U32>6618880</U32>
							</Property>
							<Property Name="Priority">
								<U32>25</U32>
							</Property>
							<Property Name="Procedure Path">
								<DependentNode Path="Targets Section/Controller/Procedures/Alarm 2 Procedure" />
							</Property>
							<Property Name="State">
								<U32>1</U32>
							</Property>
							<Property Name="Trip Color">
								<U32>16711680</U32>
							</Property>
							<Property Name="Trip Message">
								<String />
							</Property>
							<Property Name="Group Number">
								<U32>0</U32>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Alarm 3" TypeGUID="03D3B791-1485-13A6-56D2B019287A4256">
						<Description>This will trigger Alarm 3 Procedure which will disable this alarm, so it shouldn't retrigger! This triggers on Alarm Channel 3. This alarm will start off disabled</Description>
						<Properties>
							<Property Name="Channel Path">
								<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 3" />
							</Property>
							<Property Name="Delay">
								<Double>0</Double>
							</Property>
							<Property Name="Disabled Color">
								<U32>9868950</U32>
							</Property>
							<Property Name="High Limit">
								<Double>0</Double>
							</Property>
							<Property Name="High Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="ID">
								<U32>283317</U32>
							</Property>
							<Property Name="Log Trips">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="Low Limit">
								<Double>0</Double>
							</Property>
							<Property Name="Low Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Normal Color">
								<U32>6618880</U32>
							</Property>
							<Property Name="Priority">
								<U32>25</U32>
							</Property>
							<Property Name="Procedure Path">
								<DependentNode Path="Targets Section/Controller/Procedures/Alarm 3 Procedure" />
							</Property>
							<Property Name="State">
								<U32>0</U32>
							</Property>
							<Property Name="Trip Color">
								<U32>16711680</U32>
							</Property>
							<Property Name="Trip Message">
								<String />
							</Property>
							<Property Name="Group Number">
								<U32>0</U32>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Alarm 4" TypeGUID="03D3B791-1485-13A6-56D2B019287A4256">
						<Description>Triggers Alarm 4 Procedure which should enable Alarm 3. Triggered on Alarm Channel 4</Description>
						<Properties>
							<Property Name="Channel Path">
								<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 4" />
							</Property>
							<Property Name="Delay">
								<Double>0</Double>
							</Property>
							<Property Name="Disabled Color">
								<U32>9868950</U32>
							</Property>
							<Property Name="High Limit">
								<Double>0</Double>
							</Property>
							<Property Name="High Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="ID">
								<U32>299899</U32>
							</Property>
							<Property Name="Log Trips">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="Low Limit">
								<Double>0</Double>
							</Property>
							<Property Name="Low Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Normal Color">
								<U32>6618880</U32>
							</Property>
							<Property Name="Priority">
								<U32>25</U32>
							</Property>
							<Property Name="Procedure Path">
								<DependentNode Path="Targets Section/Controller/Procedures/Alarm 4 Procedure" />
							</Property>
							<Property Name="State">
								<U32>1</U32>
							</Property>
							<Property Name="Trip Color">
								<U32>16711680</U32>
							</Property>
							<Property Name="Trip Message">
								<String />
							</Property>
							<Property Name="Group Number">
								<U32>0</U32>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Alarm 5" TypeGUID="03D3B791-1485-13A6-56D2B019287A4256">
						<Description>Used to trigger Alarm 5 Procedure. Triggered by Alarm Channel 5.  Will be reset by "Reset Multiple Alarms Sub Procedure"</Description>
						<Properties>
							<Property Name="Delay">
								<Double>0</Double>
							</Property>
							<Property Name="Priority">
								<U32>25</U32>
							</Property>
							<Property Name="State">
								<U32>1</U32>
							</Property>
							<Property Name="Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Channel Path">
								<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 5" />
							</Property>
							<Property Name="High Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="High Limit">
								<Double>0</Double>
							</Property>
							<Property Name="Low Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Low Limit">
								<Double>0</Double>
							</Property>
							<Property Name="Procedure Path">
								<DependentNode Path="Targets Section/Controller/Procedures/Alarm 5 Procedure" />
							</Property>
							<Property Name="Group Number">
								<U32>0</U32>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Alarm 6" TypeGUID="03D3B791-1485-13A6-56D2B019287A4256">
						<Description>Used to trigger Alarm 6 Procedure. Triggered by Alarm Channel 6.  Will be reset by "Reset Multiple Alarms Sub Procedure"</Description>
						<Properties>
							<Property Name="Delay">
								<Double>0</Double>
							</Property>
							<Property Name="Priority">
								<U32>25</U32>
							</Property>
							<Property Name="State">
								<U32>1</U32>
							</Property>
							<Property Name="Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Channel Path">
								<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 6" />
							</Property>
							<Property Name="High Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="High Limit">
								<Double>0</Double>
							</Property>
							<Property Name="Low Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Low Limit">
								<Double>0</Double>
							</Property>
							<Property Name="Procedure Path">
								<DependentNode Path="Targets Section/Controller/Procedures/Alarm 6 Procedure" />
							</Property>
							<Property Name="Group Number">
								<U32>0</U32>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Alarm 7" TypeGUID="03D3B791-1485-13A6-56D2B019287A4256">
						<Description>Used to trigger Alarm 7 Procedure. Triggered by Alarm Channel 7.  Will be reset by "Reset Triggered Alarm Sub-Procedure"</Description>
						<Properties>
							<Property Name="Delay">
								<Double>0</Double>
							</Property>
							<Property Name="Priority">
								<U32>25</U32>
							</Property>
							<Property Name="State">
								<U32>1</U32>
							</Property>
							<Property Name="Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Channel Path">
								<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 7" />
							</Property>
							<Property Name="High Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="High Limit">
								<Double>0</Double>
							</Property>
							<Property Name="Low Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Low Limit">
								<Double>0</Double>
							</Property>
							<Property Name="Procedure Path">
								<DependentNode Path="Targets Section/Controller/Procedures/Alarm 7 Proecedure" />
							</Property>
							<Property Name="Group Number">
								<U32>0</U32>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Alarm 8" TypeGUID="03D3B791-1485-13A6-56D2B019287A4256">
						<Description>Used to trigger Alarm 7 Procedure. Triggered by Alarm Channel 7.  Will be reset by "Reset Triggered Alarm Sub-Procedure"</Description>
						<Properties>
							<Property Name="Delay">
								<Double>0</Double>
							</Property>
							<Property Name="Priority">
								<U32>25</U32>
							</Property>
							<Property Name="State">
								<U32>1</U32>
							</Property>
							<Property Name="Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Channel Path">
								<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 8" />
							</Property>
							<Property Name="High Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="High Limit">
								<Double>0</Double>
							</Property>
							<Property Name="Low Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Low Limit">
								<Double>0</Double>
							</Property>
							<Property Name="Procedure Path">
								<DependentNode Path="Targets Section/Controller/Procedures/Alarm 8 Procedure" />
							</Property>
							<Property Name="Group Number">
								<U32>0</U32>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Alarm 9" TypeGUID="03D3B791-1485-13A6-56D2B019287A4256">
						<Description>Used to trigger Alarm 9 Procedure. Triggered by Alarm Channel 9.  Will be reset by "Reset Triggered Alarm Sub-Procedure"</Description>
						<Properties>
							<Property Name="Delay">
								<Double>0</Double>
							</Property>
							<Property Name="Priority">
								<U32>30</U32>
							</Property>
							<Property Name="State">
								<U32>1</U32>
							</Property>
							<Property Name="Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Channel Path">
								<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 9" />
							</Property>
							<Property Name="High Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="High Limit">
								<Double>0</Double>
							</Property>
							<Property Name="Low Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Low Limit">
								<Double>0</Double>
							</Property>
							<Property Name="Procedure Path">
								<DependentNode Path="Targets Section/Controller/Procedures/Alarm 9 Proecedure" />
							</Property>
							<Property Name="Group Number">
								<U32>1</U32>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Alarm 10" TypeGUID="03D3B791-1485-13A6-56D2B019287A4256">
						<Description>Used to trigger Alarm 7 Procedure. Triggered by Alarm Channel 7.  Will be reset by "Reset Triggered Alarm Sub-Procedure"</Description>
						<Properties>
							<Property Name="Delay">
								<Double>0</Double>
							</Property>
							<Property Name="Priority">
								<U32>20</U32>
							</Property>
							<Property Name="State">
								<U32>1</U32>
							</Property>
							<Property Name="Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Channel Path">
								<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 10" />
							</Property>
							<Property Name="High Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="High Limit">
								<Double>0</Double>
							</Property>
							<Property Name="Low Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Low Limit">
								<Double>0</Double>
							</Property>
							<Property Name="Procedure Path">
								<DependentNode Path="Targets Section/Controller/Procedures/Alarm 10 Proecedure" />
							</Property>
							<Property Name="Group Number">
								<U32>1</U32>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Alarm 11" TypeGUID="03D3B791-1485-13A6-56D2B019287A4256">
						<Description>Used to trigger Alarm 1 Procedure. Triggered by Alarm Channel 11.  Will be reset by "Reset Triggered Alarm Sub-Procedure"</Description>
						<Properties>
							<Property Name="Delay">
								<Double>0</Double>
							</Property>
							<Property Name="Priority">
								<U32>10</U32>
							</Property>
							<Property Name="State">
								<U32>1</U32>
							</Property>
							<Property Name="Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Channel Path">
								<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 11" />
							</Property>
							<Property Name="High Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="High Limit">
								<Double>0</Double>
							</Property>
							<Property Name="Low Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Low Limit">
								<Double>0</Double>
							</Property>
							<Property Name="Procedure Path">
								<DependentNode Path="Targets Section/Controller/Procedures/Alarm 11 Proecedure" />
							</Property>
							<Property Name="Group Number">
								<U32>1</U32>
							</Property>
						</Properties>
						<Errors />
					</Section>
				</Section>
				<Section Name="Procedures" TypeGUID="03D3B7B1-1485-13A6-56649C7783203F22">
					<Description />
					<Properties>
						<Property Name="Startup Procedure Ptr">
							<DependentNode Path="Targets Section/Controller/Procedures/Startup Procedure" />
						</Property>
					</Properties>
					<Errors />
					<Section Name="Skip this procedure" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description>This procedure should never run, even though it will be first in the list!</Description>
						<Properties>
							<Property Name="ID">
								<U32>859997</U32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Set TC6 to -9999" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>-9999</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>0</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 6" />
								</Property>
							</Properties>
							<Errors />
						</Section>
					</Section>
					<Section Name="Startup Procedure" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description>Procedure intended to run at startup. Make sure this gets invoked first.</Description>
						<Properties>
							<Property Name="ID">
								<U32>848661</U32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Set TC0 to 1000" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>1000</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>0</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 0" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Set TC1 = TC0*2" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>2</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>3</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Channel 1">
									<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 0" />
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 1" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Set TC2..4 to 20000..40000" TypeGUID="9befd21d-52c4-436d-80e3-13ccac078e82">
							<Description />
							<Properties>
								<Property Name="Command.Values">
									<DoubleArray>
										<Elem>20000</Elem>
										<Elem>30000</Elem>
										<Elem>40000</Elem>
									</DoubleArray>
								</Property>
								<Property Name="Variable 0">
									<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 2" />
								</Property>
								<Property Name="Variable 1">
									<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 3" />
								</Property>
								<Property Name="Variable 2">
									<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 4" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Call Sub Procedure 1" TypeGUID="78c1304c-b691-4751-853c-67994ac9a904">
							<Description>Calls into Sub Procedure 1 which calls Sub Procedure 2. These should set TC10 = 10, and TC11 = 11</Description>
							<Properties>
								<Property Name="Procedure">
									<DependentNode Path="Targets Section/Controller/Procedures/Sub Procedure 1" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Goto Dwell 0 to skip a step" TypeGUID="b485fef3-012c-4c9e-acdb-c204000d11e5">
							<Description />
							<Properties>
								<Property Name="Goto Label">
									<DependentNode Path="Targets Section/Controller/Procedures/Startup Procedure/Dwell 0" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Don't run this step! Set TC7 to -9999" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>-9999</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>0</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 7" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Dwell 0" TypeGUID="6dde8411-8c68-408b-8558-d18c0909c789">
							<Description />
							<Properties>
								<Property Name="Command.Value">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Mode">
									<U32>0</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Wait for TC5 to be &gt;= 50000" TypeGUID="f32eebe6-061f-487b-8d23-946e7a7024d0">
							<Description />
							<Properties>
								<Property Name="Command.Value1">
									<Double>50000</Double>
								</Property>
								<Property Name="Command.Comparison">
									<I32>1</I32>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 5" />
								</Property>
								<Property Name="Conditional Goto Label">
									<DependentNode Path="Targets Section/Controller/Procedures/Startup Procedure/Dwell 0" />
								</Property>
							</Properties>
							<Errors />
						</Section>
					</Section>
					<Section Name="After Startup Procedure" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description>Procedure should run directly after startup. Just to test ordering. It should end after resetting TC5.</Description>
						<Properties>
							<Property Name="ID">
								<U32>836332</U32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Reset TC5 to 0" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>-1</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>3</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Channel 1">
									<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 5" />
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 5" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="End" TypeGUID="536ad7a0-4f35-4c08-94b5-c651b94b0eee">
							<Description />
							<Properties />
							<Errors />
						</Section>
					</Section>
					<Section Name="Also Should not Run" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description>Set to run after After Startup Procedure, which ends with an End statement. So we shouldn't proceed to this procedure.</Description>
						<Properties>
							<Property Name="ID">
								<U32>836496</U32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Set TC6 to -9999" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>-9999</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>0</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 6" />
								</Property>
							</Properties>
							<Errors />
						</Section>
					</Section>
					<Section Name="Alarm 1 Procedure" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description>Triggered by Alarm 1</Description>
						<Properties>
							<Property Name="ID">
								<U32>836645</U32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Reset Alarm Channel 1" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>0</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 1" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Increment Alarm 1 Trigger Count" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>1</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>1</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Channel 1">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 1 Trigger Count" />
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 1 Trigger Count" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Reset Alarm &amp; Exit Subroutine" TypeGUID="e203af68-4b16-4bae-a211-7502c28a5642">
							<Description />
							<Properties>
								<Property Name="Command.Priority">
									<U32>25</U32>
								</Property>
								<Property Name="Command.Default State">
									<I32>0</I32>
								</Property>
								<Property Name="Command.Delay">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Upper Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Lower Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<I32>4</I32>
								</Property>
								<Property Name="Command.UL Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.LL Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Alarm">
									<DependentNode Path="Targets Section/Controller/Alarms/Alarm 1" />
								</Property>
								<Property Name="Command.Trig Alarm">
									<Boolean>false</Boolean>
								</Property>
							</Properties>
							<Errors />
						</Section>
					</Section>
					<Section Name="Alarm 2 Procedure" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description>Triggered by Alarm 2</Description>
						<Properties>
							<Property Name="ID">
								<U32>858053</U32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Reset Alarm Channel 2" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>0</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 2" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Increment Alarm 2 Trigger Count" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>1</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>1</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Channel 1">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 2 Trigger Count" />
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 2 Trigger Count" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Reset Alarm &amp; Exit Subroutine" TypeGUID="e203af68-4b16-4bae-a211-7502c28a5642">
							<Description />
							<Properties>
								<Property Name="Command.Priority">
									<U32>25</U32>
								</Property>
								<Property Name="Command.Default State">
									<I32>0</I32>
								</Property>
								<Property Name="Command.Delay">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Upper Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Lower Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<I32>4</I32>
								</Property>
								<Property Name="Command.UL Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.LL Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Alarm">
									<DependentNode Path="Targets Section/Controller/Alarms/Alarm 2" />
								</Property>
								<Property Name="Command.Trig Alarm">
									<Boolean>false</Boolean>
								</Property>
							</Properties>
							<Errors />
						</Section>
					</Section>
					<Section Name="Alarm 3 Procedure" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description>Disables Alarm 3 after running.</Description>
						<Properties>
							<Property Name="ID">
								<U32>899073</U32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Reset Alarm Channel 3" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>0</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 3" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Increment Alarm 3 Trigger Count" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>1</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>1</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Channel 1">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 3 Trigger Count" />
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 3 Trigger Count" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Disable Alarm and Exit Subroutine" TypeGUID="e203af68-4b16-4bae-a211-7502c28a5642">
							<Description />
							<Properties>
								<Property Name="Command.Priority">
									<U32>25</U32>
								</Property>
								<Property Name="Command.Default State">
									<I32>0</I32>
								</Property>
								<Property Name="Command.Delay">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Upper Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Lower Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<I32>5</I32>
								</Property>
								<Property Name="Command.UL Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.LL Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Alarm">
									<DependentNode Path="Targets Section/Controller/Alarms/Alarm 3" />
								</Property>
								<Property Name="Command.Trig Alarm">
									<Boolean>false</Boolean>
								</Property>
							</Properties>
							<Errors />
						</Section>
					</Section>
					<Section Name="Alarm 4 Procedure" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>814644</U32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Reset Alarm Channel 4" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>0</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 4" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Enable Alarm 3" TypeGUID="e203af68-4b16-4bae-a211-7502c28a5642">
							<Description />
							<Properties>
								<Property Name="Command.Priority">
									<U32>25</U32>
								</Property>
								<Property Name="Command.Default State">
									<I32>0</I32>
								</Property>
								<Property Name="Command.Delay">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Upper Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Lower Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<I32>2</I32>
								</Property>
								<Property Name="Command.UL Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.LL Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Alarm">
									<DependentNode Path="Targets Section/Controller/Alarms/Alarm 3" />
								</Property>
								<Property Name="Command.Trig Alarm">
									<Boolean>false</Boolean>
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Reset Alarm &amp; Exit Subroutine" TypeGUID="e203af68-4b16-4bae-a211-7502c28a5642">
							<Description />
							<Properties>
								<Property Name="Command.Priority">
									<U32>25</U32>
								</Property>
								<Property Name="Command.Default State">
									<I32>0</I32>
								</Property>
								<Property Name="Command.Delay">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Upper Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Lower Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<I32>4</I32>
								</Property>
								<Property Name="Command.UL Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.LL Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Alarm">
									<DependentNode Path="Targets Section/Controller/Alarms/Alarm 4" />
								</Property>
								<Property Name="Command.Trig Alarm">
									<Boolean>false</Boolean>
								</Property>
							</Properties>
							<Errors />
						</Section>
					</Section>
					<Section Name="Alarm 5 Procedure" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description>Triggered by Alarm 5</Description>
						<Properties />
						<Errors />
						<Section Name="Reset Alarm Channel 5" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>0</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 5" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Increment Alarm 5 Trigger Count" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>1</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>1</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 5 Trigger Count" />
								</Property>
								<Property Name="Channel 1">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 5 Trigger Count" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Call Procedure" TypeGUID="78c1304c-b691-4751-853c-67994ac9a904">
							<Description />
							<Properties>
								<Property Name="Procedure">
									<DependentNode Path="Targets Section/Controller/Procedures/Reset Multiple Alarms Sub Procedure" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Exit Subroutine" TypeGUID="a48694e4-1904-4215-b4b8-a6c6f5e4d7ac">
							<Description />
							<Properties />
							<Errors />
						</Section>
					</Section>
					<Section Name="Alarm 6 Procedure" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description>Triggered by Alarm 6</Description>
						<Properties />
						<Errors />
						<Section Name="Reset Alarm Channel 6" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>0</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 6" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Increment Alarm 6 Trigger Count" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>1</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>1</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 6 Trigger Count" />
								</Property>
								<Property Name="Channel 1">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 6 Trigger Count" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Call Procedure" TypeGUID="78c1304c-b691-4751-853c-67994ac9a904">
							<Description />
							<Properties>
								<Property Name="Procedure">
									<DependentNode Path="Targets Section/Controller/Procedures/Reset Multiple Alarms Sub Procedure" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Exit Subroutine" TypeGUID="a48694e4-1904-4215-b4b8-a6c6f5e4d7ac">
							<Description />
							<Properties />
							<Errors />
						</Section>
					</Section>
					<Section Name="Alarm 7 Proecedure" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description>Triggered by Alarm 7</Description>
						<Properties />
						<Errors />
						<Section Name="Reset Alarm Channel 7" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>0</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 7" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Increment Alarm 7 Trigger Count" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>1</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>1</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 7 Trigger Count" />
								</Property>
								<Property Name="Channel 1">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 7 Trigger Count" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Call Procedure" TypeGUID="78c1304c-b691-4751-853c-67994ac9a904">
							<Description />
							<Properties>
								<Property Name="Procedure">
									<DependentNode Path="Targets Section/Controller/Procedures/Reset Triggered Alarm Sub-Procedure" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Exit Subroutine" TypeGUID="a48694e4-1904-4215-b4b8-a6c6f5e4d7ac">
							<Description />
							<Properties />
							<Errors />
						</Section>
					</Section>
					<Section Name="Alarm 8 Procedure" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description>Triggered by Alarm 8</Description>
						<Properties />
						<Errors />
						<Section Name="Reset Alarm Channel 8" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>0</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 8" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Increment Alarm 8 Trigger Count" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>1</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>1</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 8 Trigger Count" />
								</Property>
								<Property Name="Channel 1">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 8 Trigger Count" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Call Procedure" TypeGUID="78c1304c-b691-4751-853c-67994ac9a904">
							<Description />
							<Properties>
								<Property Name="Procedure">
									<DependentNode Path="Targets Section/Controller/Procedures/Reset Triggered Alarm Sub-Procedure" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Exit Subroutine" TypeGUID="a48694e4-1904-4215-b4b8-a6c6f5e4d7ac">
							<Description />
							<Properties />
							<Errors />
						</Section>
					</Section>
					<Section Name="Alarm 9 Proecedure" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description>Triggered by Alarm 9</Description>
						<Properties />
						<Errors />
						<Section Name="Dwell" TypeGUID="6dde8411-8c68-408b-8558-d18c0909c789">
							<Description />
							<Properties>
								<Property Name="Command.Value">
									<Double>5</Double>
								</Property>
								<Property Name="Command.Mode">
									<U32>0</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Reset Alarm Channel 9" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>0</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 9" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Increment Alarm 9 Trigger Count" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>1</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>1</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 9 Trigger Count" />
								</Property>
								<Property Name="Channel 1">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 9 Trigger Count" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Call Procedure" TypeGUID="78c1304c-b691-4751-853c-67994ac9a904">
							<Description />
							<Properties>
								<Property Name="Procedure">
									<DependentNode Path="Targets Section/Controller/Procedures/Reset Triggered Alarm Sub-Procedure" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Exit Subroutine" TypeGUID="a48694e4-1904-4215-b4b8-a6c6f5e4d7ac">
							<Description />
							<Properties />
							<Errors />
						</Section>
					</Section>
					<Section Name="Alarm 10 Proecedure" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description>Triggered by Alarm 10</Description>
						<Properties />
						<Errors />
						<Section Name="Dwell" TypeGUID="6dde8411-8c68-408b-8558-d18c0909c789">
							<Description />
							<Properties>
								<Property Name="Command.Value">
									<Double>5</Double>
								</Property>
								<Property Name="Command.Mode">
									<U32>0</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Reset Alarm Channel 10" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>0</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 10" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Increment Alarm 10 Trigger Count" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>1</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>1</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 10 Trigger Count" />
								</Property>
								<Property Name="Channel 1">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 10 Trigger Count" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Call Procedure" TypeGUID="78c1304c-b691-4751-853c-67994ac9a904">
							<Description />
							<Properties>
								<Property Name="Procedure">
									<DependentNode Path="Targets Section/Controller/Procedures/Reset Triggered Alarm Sub-Procedure" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Exit Subroutine" TypeGUID="a48694e4-1904-4215-b4b8-a6c6f5e4d7ac">
							<Description />
							<Properties />
							<Errors />
						</Section>
					</Section>
					<Section Name="Alarm 11 Proecedure" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description>Triggered by Alarm 11</Description>
						<Properties />
						<Errors />
						<Section Name="Dwell" TypeGUID="6dde8411-8c68-408b-8558-d18c0909c789">
							<Description />
							<Properties>
								<Property Name="Command.Value">
									<Double>5</Double>
								</Property>
								<Property Name="Command.Mode">
									<U32>0</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Reset Alarm Channel 11" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>0</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 11" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Increment Alarm 11 Trigger Count" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>1</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>1</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 11 Trigger Count" />
								</Property>
								<Property Name="Channel 1">
									<DependentNode Path="Targets Section/Controller/User Channel/Alarm 11 Trigger Count" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Call Procedure" TypeGUID="78c1304c-b691-4751-853c-67994ac9a904">
							<Description />
							<Properties>
								<Property Name="Procedure">
									<DependentNode Path="Targets Section/Controller/Procedures/Reset Triggered Alarm Sub-Procedure" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Exit Subroutine" TypeGUID="a48694e4-1904-4215-b4b8-a6c6f5e4d7ac">
							<Description />
							<Properties />
							<Errors />
						</Section>
					</Section>
					<Section Name="Sub Procedure 1" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description>Sub Procedure executed by Startup. Calls into Sub Procedure 2</Description>
						<Properties>
							<Property Name="ID">
								<U32>864674</U32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Set TC10 to 10" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>10</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>0</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 10" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Call Sub Procedure 2" TypeGUID="78c1304c-b691-4751-853c-67994ac9a904">
							<Description />
							<Properties>
								<Property Name="Procedure">
									<DependentNode Path="Targets Section/Controller/Procedures/Sub Procedure 2" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Exit Subroutine" TypeGUID="a48694e4-1904-4215-b4b8-a6c6f5e4d7ac">
							<Description />
							<Properties />
							<Errors />
						</Section>
					</Section>
					<Section Name="Sub Procedure 2" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>805719</U32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Set TC11 to 11" TypeGUID="e41ddd95-eff3-4578-b5b7-4ad8fcaf6b9a">
							<Description />
							<Properties>
								<Property Name="Command.Value 1">
									<Double>11</Double>
								</Property>
								<Property Name="Command.Value 2">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<U16>0</U16>
								</Property>
								<Property Name="Command.Value 1 Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Value 2 Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Variable">
									<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 11" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Exit Subroutine" TypeGUID="a48694e4-1904-4215-b4b8-a6c6f5e4d7ac">
							<Description />
							<Properties />
							<Errors />
						</Section>
					</Section>
					<Section Name="Reset Multiple Alarms Sub Procedure" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description>This is called by Alarm 5 Procedure and Alarm 6 Proecedure.  It will reset both Alarm 5 and Alarm 6.</Description>
						<Properties />
						<Errors />
						<Section Name="Reset Alarm 5" TypeGUID="e203af68-4b16-4bae-a211-7502c28a5642">
							<Description />
							<Properties>
								<Property Name="Alarm">
									<DependentNode Path="Targets Section/Controller/Alarms/Alarm 5" />
								</Property>
								<Property Name="Command.Priority">
									<U32>0</U32>
								</Property>
								<Property Name="Command.Default State">
									<I32>0</I32>
								</Property>
								<Property Name="Command.Delay">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Upper Limit">
									<Double>1</Double>
								</Property>
								<Property Name="Command.Lower Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<I32>8</I32>
								</Property>
								<Property Name="Command.UL Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.LL Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Trig Alarm">
									<Boolean>false</Boolean>
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Reset Alarm 6" TypeGUID="e203af68-4b16-4bae-a211-7502c28a5642">
							<Description />
							<Properties>
								<Property Name="Command.Priority">
									<U32>25</U32>
								</Property>
								<Property Name="Command.Default State">
									<I32>1</I32>
								</Property>
								<Property Name="Command.Delay">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Upper Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Lower Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<I32>8</I32>
								</Property>
								<Property Name="Command.UL Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.LL Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Trig Alarm">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Alarm">
									<DependentNode Path="Targets Section/Controller/Alarms/Alarm 6" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Exit Subroutine" TypeGUID="a48694e4-1904-4215-b4b8-a6c6f5e4d7ac">
							<Description />
							<Properties />
							<Errors />
						</Section>
					</Section>
					<Section Name="Reset Triggered Alarm Sub-Procedure" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description>This is called by Alarm Procedures 7, 8, 9, 10, and 11.  It will reset whatever alarm triggered the parent procedure.</Description>
						<Properties />
						<Errors />
						<Section Name="Alarm Command" TypeGUID="e203af68-4b16-4bae-a211-7502c28a5642">
							<Description />
							<Properties>
								<Property Name="Command.Priority">
									<U32>0</U32>
								</Property>
								<Property Name="Command.Default State">
									<I32>0</I32>
								</Property>
								<Property Name="Command.Delay">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Upper Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Lower Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<I32>4</I32>
								</Property>
								<Property Name="Command.UL Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.LL Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.Trip Alarm">
									<Boolean>true</Boolean>
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
				<Section Name="User Channel" TypeGUID="03D3B6B7-1485-13A6-567BE1E1E0DF999A">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="Test Channel 0" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 1" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 2" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 3" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 4" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 5" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 6" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 7" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 8" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 9" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 10" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 11" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 12" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 13" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 14" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 15" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 16" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 17" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 18" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 19" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 20" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 21" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 22" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 23" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 24" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 25" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 26" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 27" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 28" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 29" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 30" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 31" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 32" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 33" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 34" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 35" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 36" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 37" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 38" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 39" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 40" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 41" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Test Channel 42" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Channel 4" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description>Watched by Alarm 4</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm 3 Trigger Count" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description>Alarm 3 Procedure increments this variable every time it is triggered. But it starts off disabled and the alarm proc disables it again after running</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Channel 3" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm 2 Trigger Count" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description>Used by Alarm 2 Procedure to indicate Alarm 2 was triggered and responded to. Increments every time.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm 1 Trigger Count" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description>Used by Alarm 1 Procedure to indicate Alarm 1 was triggered and responded to. Increments every time.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Channel 2" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Channel 1" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="TEST_ID" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description>Test ID for the procedures test</Description>
						<Properties>
							<Property Name="ID">
								<U32>1</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>3000</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Channel 5" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Channel 6" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Channel 7" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Channel 8" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm 5 Trigger Count" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description>Used by Alarm 5 Procedure to indicate Alarm 5 was triggered and responded to. Increments every time.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm 6 Trigger Count" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description>Used by Alarm 6 Procedure to indicate Alarm 6 was triggered and responded to. Increments every time.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm 7 Trigger Count" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description>Used by Alarm 7 Procedure to indicate Alarm 7 was triggered and responded to. Increments every time.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm 8 Trigger Count" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description>Used by Alarm 8 Procedure to indicate Alarm 8 was triggered and responded to. Increments every time.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm 9 Trigger Count" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm 10 Trigger Count" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Channel 9" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Channel 10" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Channel 11" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm 11 Trigger Count" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
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
			<Alias Name="System Time" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/System Channels/System Time" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 0" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 0" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 3" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 4" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 4" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 5" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 5" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 6" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 6" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 7" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 7" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 8" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 8" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 9" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 9" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 10" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 10" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 11" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 11" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 12" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 12" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 13" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 13" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 14" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 14" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 15" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 15" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 16" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 16" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 17" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 17" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 18" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 18" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 19" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 19" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 20" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 20" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 21" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 21" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 22" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 22" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 23" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 23" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 24" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 24" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 25" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 25" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 26" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 26" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 27" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 27" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 28" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 28" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 29" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 29" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 30" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 30" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 31" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 31" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 32" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 32" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 33" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 33" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 34" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 34" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 35" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 35" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 36" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 36" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 37" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 37" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 38" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 38" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 39" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 39" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 40" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 40" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 41" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 41" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 42" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Test Channel 42" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 43" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 4" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 44" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm 3 Trigger Count" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Test Channel 45" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm 2 Trigger Count" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm 2 Trigger Count" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm 1 Trigger Count" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm 1 Trigger Count" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm Channel 2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm Channel 1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 1" />
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
			<Alias Name="Alarm Channel 4" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 4" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm 3 Trigger Count" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm 3 Trigger Count" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm Channel 3" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm 5 Trigger Count" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm 5 Trigger Count" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm 6 Trigger Count" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm 6 Trigger Count" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm Channel 5" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 5" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm Channel 6" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 6" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm 7 Trigger Count" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm 7 Trigger Count" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm 8 Trigger Count" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm 8 Trigger Count" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm Channel 7" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 7" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm Channel 8" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 8" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm 10 Trigger Count" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm 10 Trigger Count" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm 11 Trigger Count" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm 11 Trigger Count" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm 9 Trigger Count" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm 9 Trigger Count" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm Channel 10" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 10" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm Channel 11" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 11" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Alarm Channel 9" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/Alarm Channel 9" />
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

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ProfileTest/All Step Types.nivstest sha256=e4eab2c185707fc852fb5be54fe0b983eca9338d71868d0a40b5ee489cd1fe18 bytes=15023 -->
## FILE: tests/testutilities/legacy_files/ProfileTest/All Step Types.nivstest

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ProfileTest/All Step Types.nivstest`
- sha256: `e4eab2c185707fc852fb5be54fe0b983eca9338d71868d0a40b5ee489cd1fe18`
- bytes: 15023

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
		<Section Name="Ramp Test [User Channel 1]" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray>
						<Elem>Target Section/Controller/User Channels/User Channel 1</Elem>
					</StringArray>
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Root Group 1" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
				<Properties />
				<Errors />
				<Section Name="Reset Pass Fail" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
					<Properties>
						<Property Name="Step Type">
							<String>Set Variable</String>
						</Property>
						<Property Name="Channel">
							<String>Target Section/Controller/User Channels/Pass Fail Channels/Gen 1 Pass Fail</String>
						</Property>
						<Property Name="Value1.Type">
							<String>Constant</String>
						</Property>
						<Property Name="Value1.Constant">
							<Double>-1</Double>
						</Property>
						<Property Name="Function">
							<String>None</String>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Run Rate Test" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
					<Description>Ramp up to 100 at a rate of 10 EUs/sec. Check that we reach 100 and that the duration is about 10 seconds.</Description>
					<Properties />
					<Errors />
					<Section Name="Tick" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Channel</String>
							</Property>
							<Property Name="Function">
								<String>None</String>
							</Property>
							<Property Name="Value1.Channel">
								<String>System Time</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Ramp to One Hundred" TypeGUID="d3a0c118-0577-4aae-9d76-9fdcf7c75eb6">
						<Properties>
							<Property Name="Step Type">
								<String>Ramp</String>
							</Property>
							<Property Name="End Point">
								<Double>100</Double>
							</Property>
							<Property Name="Mode">
								<String>Rate</String>
							</Property>
							<Property Name="Rate">
								<Double>10</Double>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Tock" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Channel</String>
							</Property>
							<Property Name="Function">
								<String>--</String>
							</Property>
							<Property Name="Value1.Channel">
								<String>System Time</String>
							</Property>
							<Property Name="Value2.Type">
								<String>Channel</String>
							</Property>
							<Property Name="Value2.Channel">
								<String>LV 1</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Check One Hundred 1" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
						<Properties>
							<Property Name="Step Type">
								<String>Conditional</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/User Channel 1</String>
							</Property>
							<Property Name="Comparison">
								<String>Not Equal</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>100</Double>
							</Property>
							<Property Name="Goto Step">
								<DependentNode Path="Ramp Test [User Channel 1]/Root Group 1/Fail" />
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Check Ramp Min Duration" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
						<Properties>
							<Property Name="Step Type">
								<String>Conditional</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Comparison">
								<String>Less</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>9.5</Double>
							</Property>
							<Property Name="Goto Step">
								<DependentNode Path="Ramp Test [User Channel 1]/Root Group 1/Fail" />
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Check Ramp Max Duration" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
						<Properties>
							<Property Name="Step Type">
								<String>Conditional</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Comparison">
								<String>Greater</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>10.5</Double>
							</Property>
							<Property Name="Goto Step">
								<DependentNode Path="Ramp Test [User Channel 1]/Root Group 1/Fail" />
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Run Duration Test" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
						<Description>Ramp down to 0 at a fixed duration of 5 seconds. Check the end value and duration.</Description>
						<Properties />
						<Errors />
						<Section Name="Tick" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
							<Properties>
								<Property Name="Step Type">
									<String>Set Variable</String>
								</Property>
								<Property Name="Channel">
									<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
								</Property>
								<Property Name="Value1.Type">
									<String>Channel</String>
								</Property>
								<Property Name="Function">
									<String>None</String>
								</Property>
								<Property Name="Value1.Channel">
									<String>System Time</String>
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Ramp to Zero" TypeGUID="d3a0c118-0577-4aae-9d76-9fdcf7c75eb6">
							<Properties>
								<Property Name="Step Type">
									<String>Ramp</String>
								</Property>
								<Property Name="End Point">
									<Double>0</Double>
								</Property>
								<Property Name="Mode">
									<String>Duration</String>
								</Property>
								<Property Name="Rate">
									<Double>10</Double>
								</Property>
								<Property Name="Duration">
									<Double>5</Double>
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Tock" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
							<Properties>
								<Property Name="Step Type">
									<String>Set Variable</String>
								</Property>
								<Property Name="Channel">
									<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
								</Property>
								<Property Name="Value1.Type">
									<String>Channel</String>
								</Property>
								<Property Name="Function">
									<String>--</String>
								</Property>
								<Property Name="Value1.Channel">
									<String>System Time</String>
								</Property>
								<Property Name="Value2.Type">
									<String>Channel</String>
								</Property>
								<Property Name="Value2.Channel">
									<String>LV 1</String>
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Check Zero" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
							<Properties>
								<Property Name="Step Type">
									<String>Conditional</String>
								</Property>
								<Property Name="Channel">
									<String>Target Section/Controller/User Channels/User Channel 1</String>
								</Property>
								<Property Name="Comparison">
									<String>Not Equal</String>
								</Property>
								<Property Name="Value1.Type">
									<String>Constant</String>
								</Property>
								<Property Name="Value1.Constant">
									<Double>0</Double>
								</Property>
								<Property Name="Goto Step">
									<DependentNode Path="Ramp Test [User Channel 1]/Root Group 1/Fail" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Check Ramp Min Duration" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
							<Properties>
								<Property Name="Step Type">
									<String>Conditional</String>
								</Property>
								<Property Name="Channel">
									<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
								</Property>
								<Property Name="Comparison">
									<String>Less</String>
								</Property>
								<Property Name="Value1.Type">
									<String>Constant</String>
								</Property>
								<Property Name="Value1.Constant">
									<Double>4.5</Double>
								</Property>
								<Property Name="Goto Step">
									<DependentNode Path="Ramp Test [User Channel 1]/Root Group 1/Fail" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Check Ramp Max Duration" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
							<Properties>
								<Property Name="Step Type">
									<String>Conditional</String>
								</Property>
								<Property Name="Channel">
									<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
								</Property>
								<Property Name="Comparison">
									<String>Greater</String>
								</Property>
								<Property Name="Value1.Type">
									<String>Constant</String>
								</Property>
								<Property Name="Value1.Constant">
									<Double>5.5</Double>
								</Property>
								<Property Name="Goto Step">
									<DependentNode Path="Ramp Test [User Channel 1]/Root Group 1/Fail" />
								</Property>
							</Properties>
							<Errors />
						</Section>
					</Section>
				</Section>
				<Section Name="Pass" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
					<Properties />
					<Errors />
					<Section Name="Set Pass" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Pass Fail Channels/Gen 1 Pass Fail</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>1</Double>
							</Property>
							<Property Name="Function">
								<String>None</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Stop Profile" TypeGUID="9f447d91-f09d-47c8-809b-a8a49ad8f6bd">
						<Properties>
							<Property Name="Step Type">
								<String>End</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
				</Section>
				<Section Name="Fail" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
					<Properties />
					<Errors />
					<Section Name="Set Fail" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Pass Fail Channels/Gen 1 Pass Fail</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>0</Double>
							</Property>
							<Property Name="Function">
								<String>None</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Stop Profile" TypeGUID="9f447d91-f09d-47c8-809b-a8a49ad8f6bd">
						<Properties>
							<Property Name="Step Type">
								<String>End</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
				</Section>
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ProfileTest/Aux Buffer Overflow.nivstest sha256=ddb46ffeae06a4a3e76488cf32bb913c5a55bf5a97a831069448216a533a7bca bytes=96878 -->
## FILE: tests/testutilities/legacy_files/ProfileTest/Aux Buffer Overflow.nivstest

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ProfileTest/Aux Buffer Overflow.nivstest`
- sha256: `ddb46ffeae06a4a3e76488cf32bb913c5a55bf5a97a831069448216a533a7bca`
- bytes: 96878

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
		<Section Name=" XY Replay: User Channel 0" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray>
						<Elem>User Channel 1</Elem>
					</StringArray>
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name=" XY Replay: User Channel 0" TypeGUID="15d33d3d-8d9c-47d0-b5b9-5ab880f4dc76">
				<Properties>
					<Property Name="Step Type">
						<String>XY Replay</String>
					</Property>
					<Property Name="Values">
						<DoubleArray>
							<Elem>5.319984</Elem>
							<Elem>5.207386</Elem>
							<Elem>5.091956</Elem>
							<Elem>4.975267</Elem>
							<Elem>4.858909</Elem>
							<Elem>4.74447</Elem>
							<Elem>4.633509</Elem>
							<Elem>4.527541</Elem>
							<Elem>4.428011</Elem>
							<Elem>4.336278</Elem>
							<Elem>4.253593</Elem>
							<Elem>4.181088</Elem>
							<Elem>4.119752</Elem>
							<Elem>4.070423</Elem>
							<Elem>4.033777</Elem>
							<Elem>4.010316</Elem>
							<Elem>4.000361</Elem>
							<Elem>4.004051</Elem>
							<Elem>4.021336</Elem>
							<Elem>4.051984</Elem>
							<Elem>4.095578</Elem>
							<Elem>4.151524</Elem>
							<Elem>4.219059</Elem>
							<Elem>4.297264</Elem>
							<Elem>4.385072</Elem>
							<Elem>4.481283</Elem>
							<Elem>4.584587</Elem>
							<Elem>4.69357</Elem>
							<Elem>4.806747</Elem>
							<Elem>4.922569</Elem>
							<Elem>5.039456</Elem>
							<Elem>5.155809</Elem>
							<Elem>5.270037</Elem>
							<Elem>5.38058</Elem>
							<Elem>5.485924</Elem>
							<Elem>5.584629</Elem>
							<Elem>5.675344</Elem>
							<Elem>5.756827</Elem>
							<Elem>5.827963</Elem>
							<Elem>5.887776</Elem>
							<Elem>5.935447</Elem>
							<Elem>5.970322</Elem>
							<Elem>5.991921</Elem>
							<Elem>5.999949</Elem>
							<Elem>5.994291</Elem>
							<Elem>5.975025</Elem>
							<Elem>5.942411</Elem>
							<Elem>5.896895</Elem>
							<Elem>5.839097</Elem>
							<Elem>5.769807</Elem>
							<Elem>5.689973</Elem>
							<Elem>5.600685</Elem>
							<Elem>5.503167</Elem>
							<Elem>5.398752</Elem>
							<Elem>5.288869</Elem>
							<Elem>5.175023</Elem>
							<Elem>5.058774</Elem>
							<Elem>4.941714</Elem>
							<Elem>4.825447</Elem>
							<Elem>4.711567</Elem>
							<Elem>4.601634</Elem>
							<Elem>4.497158</Elem>
							<Elem>4.399569</Elem>
							<Elem>4.310209</Elem>
							<Elem>4.230303</Elem>
							<Elem>4.160948</Elem>
							<Elem>4.103096</Elem>
							<Elem>4.057544</Elem>
							<Elem>4.024918</Elem>
							<Elem>4.005667</Elem>
							<Elem>4.000057</Elem>
							<Elem>4.008167</Elem>
							<Elem>4.029889</Elem>
							<Elem>4.064925</Elem>
							<Elem>4.112796</Elem>
							<Elem>4.172849</Elem>
							<Elem>4.244259</Elem>
							<Elem>4.326048</Elem>
							<Elem>4.417095</Elem>
							<Elem>4.516151</Elem>
							<Elem>4.621856</Elem>
							<Elem>4.73276</Elem>
							<Elem>4.84734</Elem>
							<Elem>4.964023</Elem>
							<Elem>5.081205</Elem>
							<Elem>5.197278</Elem>
							<Elem>5.310645</Elem>
							<Elem>5.419748</Elem>
							<Elem>5.523088</Elem>
							<Elem>5.619243</Elem>
							<Elem>5.70689</Elem>
							<Elem>5.784823</Elem>
							<Elem>5.85197</Elem>
							<Elem>5.907405</Elem>
							<Elem>5.950364</Elem>
							<Elem>5.980255</Elem>
							<Elem>5.996664</Elem>
							<Elem>5.999365</Elem>
							<Elem>5.988317</Elem>
							<Elem>5.963671</Elem>
							<Elem>5.925765</Elem>
							<Elem>5.875117</Elem>
							<Elem>5.812423</Elem>
							<Elem>5.738544</Elem>
							<Elem>5.654496</Elem>
							<Elem>5.561434</Elem>
							<Elem>5.460637</Elem>
							<Elem>5.353494</Elem>
							<Elem>5.241477</Elem>
							<Elem>5.12613</Elem>
							<Elem>5.00904</Elem>
							<Elem>4.89182</Elem>
							<Elem>4.776084</Elem>
							<Elem>4.663428</Elem>
							<Elem>4.555404</Elem>
							<Elem>4.4535</Elem>
							<Elem>4.359124</Elem>
							<Elem>4.273575</Elem>
							<Elem>4.198035</Elem>
							<Elem>4.133546</Elem>
							<Elem>4.080999</Elem>
							<Elem>4.04112</Elem>
							<Elem>4.014462</Elem>
							<Elem>4.001392</Elem>
							<Elem>4.002094</Elem>
							<Elem>4.01656</Elem>
							<Elem>4.044593</Elem>
							<Elem>4.085807</Elem>
							<Elem>4.139636</Elem>
							<Elem>4.205339</Elem>
							<Elem>4.28201</Elem>
							<Elem>4.368595</Elem>
							<Elem>4.463898</Elem>
							<Elem>4.566605</Elem>
							<Elem>4.675301</Elem>
							<Elem>4.788484</Elem>
							<Elem>4.904593</Elem>
							<Elem>5.022026</Elem>
							<Elem>5.13916</Elem>
							<Elem>5.254377</Elem>
							<Elem>5.366086</Elem>
							<Elem>5.472744</Elem>
							<Elem>5.572875</Elem>
							<Elem>5.665096</Elem>
							<Elem>5.748132</Elem>
							<Elem>5.820832</Elem>
							<Elem>5.882192</Elem>
							<Elem>5.931361</Elem>
							<Elem>5.967658</Elem>
							<Elem>5.990579</Elem>
							<Elem>5.999806</Elem>
							<Elem>5.995208</Elem>
							<Elem>5.976848</Elem>
							<Elem>5.944977</Elem>
							<Elem>5.900035</Elem>
							<Elem>5.84264</Elem>
							<Elem>5.773586</Elem>
							<Elem>5.693826</Elem>
							<Elem>5.604462</Elem>
							<Elem>5.506729</Elem>
							<Elem>5.401979</Elem>
							<Elem>5.29166</Elem>
							<Elem>5.177299</Elem>
							<Elem>5.060478</Elem>
							<Elem>4.942814</Elem>
							<Elem>4.825936</Elem>
							<Elem>4.711463</Elem>
							<Elem>4.60098</Elem>
							<Elem>4.496018</Elem>
							<Elem>4.398032</Elem>
							<Elem>4.30838</Elem>
							<Elem>4.228306</Elem>
							<Elem>4.158919</Elem>
							<Elem>4.101184</Elem>
							<Elem>4.055901</Elem>
							<Elem>4.023701</Elem>
							<Elem>4.005031</Elem>
							<Elem>4.000152</Elem>
							<Elem>4.009134</Elem>
							<Elem>4.031855</Elem>
							<Elem>4.068</Elem>
							<Elem>4.117071</Elem>
							<Elem>4.17839</Elem>
							<Elem>4.251107</Elem>
							<Elem>4.334215</Elem>
							<Elem>4.426564</Elem>
							<Elem>4.526872</Elem>
							<Elem>4.63375</Elem>
							<Elem>4.745716</Elem>
							<Elem>4.861215</Elem>
							<Elem>4.978647</Elem>
							<Elem>5.09638</Elem>
							<Elem>5.212781</Elem>
							<Elem>5.326234</Elem>
							<Elem>5.435162</Elem>
							<Elem>5.538053</Elem>
							<Elem>5.633477</Elem>
							<Elem>5.720108</Elem>
							<Elem>5.79674</Elem>
							<Elem>5.862309</Elem>
							<Elem>5.915901</Elem>
							<Elem>5.956771</Elem>
							<Elem>5.984348</Elem>
							<Elem>5.998248</Elem>
							<Elem>5.998275</Elem>
							<Elem>5.984427</Elem>
							<Elem>5.956894</Elem>
							<Elem>5.916057</Elem>
							<Elem>5.862483</Elem>
							<Elem>5.796914</Elem>
							<Elem>5.72026</Elem>
							<Elem>5.633586</Elem>
							<Elem>5.538095</Elem>
							<Elem>5.435115</Elem>
							<Elem>5.326078</Elem>
							<Elem>5.212498</Elem>
							<Elem>5.095957</Elem>
							<Elem>4.978075</Elem>
							<Elem>4.860492</Elem>
							<Elem>4.744845</Elem>
							<Elem>4.632745</Elem>
							<Elem>4.525751</Elem>
							<Elem>4.425354</Elem>
							<Elem>4.332954</Elem>
							<Elem>4.249837</Elem>
							<Elem>4.177163</Elem>
							<Elem>4.115945</Elem>
							<Elem>4.067038</Elem>
							<Elem>4.031124</Elem>
							<Elem>4.008705</Elem>
							<Elem>4.000097</Elem>
							<Elem>4.005421</Elem>
							<Elem>4.024604</Elem>
							<Elem>4.057382</Elem>
							<Elem>4.103299</Elem>
							<Elem>4.161717</Elem>
							<Elem>4.231825</Elem>
							<Elem>4.312645</Elem>
							<Elem>4.403053</Elem>
							<Elem>4.501789</Elem>
							<Elem>4.607477</Elem>
							<Elem>4.718646</Elem>
							<Elem>4.833744</Elem>
							<Elem>4.951166</Elem>
							<Elem>5.069276</Elem>
							<Elem>5.186425</Elem>
							<Elem>5.300977</Elem>
							<Elem>5.411336</Elem>
							<Elem>5.515958</Elem>
							<Elem>5.613385</Elem>
							<Elem>5.702253</Elem>
							<Elem>5.781322</Elem>
							<Elem>5.849486</Elem>
							<Elem>5.905793</Elem>
							<Elem>5.949453</Elem>
							<Elem>5.979855</Elem>
							<Elem>5.996573</Elem>
							<Elem>5.999372</Elem>
							<Elem>5.98821</Elem>
							<Elem>5.96324</Elem>
							<Elem>5.924812</Elem>
							<Elem>5.873458</Elem>
							<Elem>5.809895</Elem>
							<Elem>5.73501</Elem>
							<Elem>5.649847</Elem>
							<Elem>5.555596</Elem>
							<Elem>5.453574</Elem>
							<Elem>5.345204</Elem>
							<Elem>5.232003</Elem>
							<Elem>5.115552</Elem>
							<Elem>4.997479</Elem>
							<Elem>4.879436</Elem>
							<Elem>4.763073</Elem>
							<Elem>4.65002</Elem>
							<Elem>4.541858</Elem>
							<Elem>4.440101</Elem>
							<Elem>4.346175</Elem>
							<Elem>4.261394</Elem>
							<Elem>4.186947</Elem>
							<Elem>4.123877</Elem>
							<Elem>4.07307</Elem>
							<Elem>4.035237</Elem>
							<Elem>4.010911</Elem>
							<Elem>4.000434</Elem>
							<Elem>4.003954</Elem>
							<Elem>4.021426</Elem>
							<Elem>4.052605</Elem>
							<Elem>4.097057</Elem>
							<Elem>4.154161</Elem>
							<Elem>4.223119</Elem>
							<Elem>4.302966</Elem>
							<Elem>4.392585</Elem>
							<Elem>4.490721</Elem>
							<Elem>4.596</Elem>
							<Elem>4.706947</Elem>
							<Elem>4.822008</Elem>
							<Elem>4.93957</Elem>
							<Elem>5.057985</Elem>
							<Elem>5.175592</Elem>
							<Elem>5.290743</Elem>
							<Elem>5.401821</Elem>
							<Elem>5.507268</Elem>
							<Elem>5.605603</Elem>
							<Elem>5.695447</Elem>
							<Elem>5.775537</Elem>
							<Elem>5.844749</Elem>
							<Elem>5.902108</Elem>
							<Elem>5.946809</Elem>
							<Elem>5.978222</Elem>
							<Elem>5.995905</Elem>
							<Elem>5.999607</Elem>
							<Elem>5.989274</Elem>
							<Elem>5.96505</Elem>
							<Elem>5.927272</Elem>
							<Elem>5.876469</Elem>
							<Elem>5.813353</Elem>
							<Elem>5.738808</Elem>
							<Elem>5.653881</Elem>
							<Elem>5.559763</Elem>
							<Elem>5.457775</Elem>
							<Elem>5.34935</Elem>
							<Elem>5.236009</Elem>
							<Elem>5.119346</Elem>
							<Elem>5.001</Elem>
							<Elem>4.882635</Elem>
							<Elem>4.765913</Elem>
							<Elem>4.652478</Elem>
							<Elem>4.543924</Elem>
							<Elem>4.441778</Elem>
							<Elem>4.347479</Elem>
							<Elem>4.262354</Elem>
							<Elem>4.187602</Elem>
							<Elem>4.124275</Elem>
							<Elem>4.073267</Elem>
							<Elem>4.035296</Elem>
							<Elem>4.0109</Elem>
							<Elem>4.000423</Elem>
							<Elem>4.004014</Elem>
							<Elem>4.021627</Elem>
							<Elem>4.053013</Elem>
							<Elem>4.097734</Elem>
							<Elem>4.155161</Elem>
							<Elem>4.224489</Elem>
							<Elem>4.304741</Elem>
							<Elem>4.394789</Elem>
							<Elem>4.493367</Elem>
							<Elem>4.599087</Elem>
							<Elem>4.71046</Elem>
							<Elem>4.825918</Elem>
							<Elem>4.943834</Elem>
							<Elem>5.062548</Elem>
							<Elem>5.180385</Elem>
							<Elem>5.295686</Elem>
							<Elem>5.406824</Elem>
							<Elem>5.512231</Elem>
							<Elem>5.610422</Elem>
							<Elem>5.700009</Elem>
							<Elem>5.77973</Elem>
							<Elem>5.848457</Elem>
							<Elem>5.90522</Elem>
							<Elem>5.949217</Elem>
							<Elem>5.979825</Elem>
							<Elem>5.99661</Elem>
							<Elem>5.999334</Elem>
							<Elem>5.987956</Elem>
							<Elem>5.962634</Elem>
							<Elem>5.923724</Elem>
							<Elem>5.871774</Elem>
							<Elem>5.807515</Elem>
							<Elem>5.731852</Elem>
							<Elem>5.645852</Elem>
							<Elem>5.550727</Elem>
							<Elem>5.447821</Elem>
							<Elem>5.338585</Elem>
							<Elem>5.224562</Elem>
							<Elem>5.107361</Elem>
							<Elem>4.988637</Elem>
							<Elem>4.870069</Elem>
							<Elem>4.753331</Elem>
							<Elem>4.640073</Elem>
							<Elem>4.531897</Elem>
							<Elem>4.430332</Elem>
							<Elem>4.336814</Elem>
							<Elem>4.252668</Elem>
							<Elem>4.179084</Elem>
							<Elem>4.117103</Elem>
							<Elem>4.067605</Elem>
							<Elem>4.031291</Elem>
							<Elem>4.008676</Elem>
							<Elem>4.000082</Elem>
							<Elem>4.005633</Elem>
							<Elem>4.025253</Elem>
							<Elem>4.058665</Elem>
							<Elem>4.105399</Elem>
							<Elem>4.164795</Elem>
							<Elem>4.236015</Elem>
							<Elem>4.318052</Elem>
							<Elem>4.409746</Elem>
							<Elem>4.509801</Elem>
							<Elem>4.616801</Elem>
							<Elem>4.729232</Elem>
							<Elem>4.845503</Elem>
							<Elem>4.963968</Elem>
							<Elem>5.082948</Elem>
							<Elem>5.200759</Elem>
							<Elem>5.315732</Elem>
							<Elem>5.426237</Elem>
							<Elem>5.530707</Elem>
							<Elem>5.627662</Elem>
							<Elem>5.715727</Elem>
							<Elem>5.793651</Elem>
							<Elem>5.86033</Elem>
							<Elem>5.914815</Elem>
							<Elem>5.956334</Elem>
							<Elem>5.984295</Elem>
							<Elem>5.998301</Elem>
							<Elem>5.998149</Elem>
							<Elem>5.983842</Elem>
							<Elem>5.955578</Elem>
							<Elem>5.913759</Elem>
							<Elem>5.858974</Elem>
							<Elem>5.791999</Elem>
							<Elem>5.713783</Elem>
							<Elem>5.625435</Elem>
							<Elem>5.528206</Elem>
							<Elem>5.423475</Elem>
							<Elem>5.312729</Elem>
							<Elem>5.197537</Elem>
							<Elem>5.079536</Elem>
							<Elem>4.9604</Elem>
							<Elem>4.84182</Elem>
							<Elem>4.725482</Elem>
							<Elem>4.613036</Elem>
							<Elem>4.506082</Elem>
							<Elem>4.40614</Elem>
							<Elem>4.314629</Elem>
							<Elem>4.232852</Elem>
							<Elem>4.161972</Elem>
							<Elem>4.102997</Elem>
							<Elem>4.056769</Elem>
							<Elem>4.023945</Elem>
							<Elem>4.004994</Elem>
							<Elem>4.000187</Elem>
							<Elem>4.009595</Elem>
							<Elem>4.033086</Elem>
							<Elem>4.070328</Elem>
							<Elem>4.120793</Elem>
							<Elem>4.183765</Elem>
							<Elem>4.258351</Elem>
							<Elem>4.343491</Elem>
							<Elem>4.437975</Elem>
							<Elem>4.54046</Elem>
							<Elem>4.64949</Elem>
							<Elem>4.763512</Elem>
							<Elem>4.880906</Elem>
							<Elem>5</Elem>
							<Elem>5.1191</Elem>
							<Elem>5.23651</Elem>
							<Elem>5.350558</Elem>
							<Elem>5.45962</Elem>
							<Elem>5.562142</Elem>
							<Elem>5.656663</Elem>
							<Elem>5.741835</Elem>
							<Elem>5.816444</Elem>
							<Elem>5.879425</Elem>
							<Elem>5.929881</Elem>
							<Elem>5.967089</Elem>
							<Elem>5.990517</Elem>
							<Elem>5.999831</Elem>
							<Elem>5.994895</Elem>
							<Elem>5.975778</Elem>
							<Elem>5.942749</Elem>
							<Elem>5.896279</Elem>
							<Elem>5.837027</Elem>
							<Elem>5.765837</Elem>
							<Elem>5.683722</Elem>
							<Elem>5.591852</Elem>
							<Elem>5.491536</Elem>
							<Elem>5.384204</Elem>
							<Elem>5.271385</Elem>
							<Elem>5.154689</Elem>
							<Elem>5.03578</Elem>
							<Elem>4.916355</Elem>
							<Elem>4.798118</Elem>
							<Elem>4.682758</Elem>
							<Elem>4.57192</Elem>
							<Elem>4.467187</Elem>
							<Elem>4.370057</Elem>
							<Elem>4.281917</Elem>
							<Elem>4.204027</Elem>
							<Elem>4.1375</Elem>
							<Elem>4.083289</Elem>
							<Elem>4.042169</Elem>
							<Elem>4.014729</Elem>
							<Elem>4.001365</Elem>
							<Elem>4.002268</Elem>
							<Elem>4.017427</Elem>
							<Elem>4.046629</Elem>
							<Elem>4.089457</Elem>
							<Elem>4.145302</Elem>
							<Elem>4.213367</Elem>
							<Elem>4.292681</Elem>
							<Elem>4.382111</Elem>
							<Elem>4.48038</Elem>
							<Elem>4.586085</Elem>
							<Elem>4.697713</Elem>
							<Elem>4.813671</Elem>
							<Elem>4.932299</Elem>
							<Elem>5.051901</Elem>
							<Elem>5.170767</Elem>
							<Elem>5.287194</Elem>
							<Elem>5.399518</Elem>
							<Elem>5.506129</Elem>
							<Elem>5.605502</Elem>
							<Elem>5.696213</Elem>
							<Elem>5.776961</Elem>
							<Elem>5.846591</Elem>
							<Elem>5.904103</Elem>
							<Elem>5.948672</Elem>
							<Elem>5.979658</Elem>
							<Elem>5.996615</Elem>
							<Elem>5.999299</Elem>
							<Elem>5.987669</Elem>
							<Elem>5.961889</Elem>
							<Elem>5.922327</Elem>
							<Elem>5.869548</Elem>
							<Elem>5.804307</Elem>
							<Elem>5.727536</Elem>
							<Elem>5.640334</Elem>
							<Elem>5.543949</Elem>
							<Elem>5.439763</Elem>
							<Elem>5.329267</Elem>
							<Elem>5.214045</Elem>
							<Elem>5.095748</Elem>
							<Elem>4.976073</Elem>
							<Elem>4.856735</Elem>
							<Elem>4.739447</Elem>
							<Elem>4.62589</Elem>
							<Elem>4.517696</Elem>
							<Elem>4.416415</Elem>
							<Elem>4.323504</Elem>
							<Elem>4.240296</Elem>
							<Elem>4.167986</Elem>
							<Elem>4.107615</Elem>
							<Elem>4.06005</Elem>
							<Elem>4.025976</Elem>
							<Elem>4.005884</Elem>
							<Elem>4.000065</Elem>
							<Elem>4.008603</Elem>
							<Elem>4.03138</Elem>
							<Elem>4.068068</Elem>
							<Elem>4.118144</Elem>
							<Elem>4.180891</Elem>
							<Elem>4.255407</Elem>
							<Elem>4.340625</Elem>
							<Elem>4.435321</Elem>
							<Elem>4.538136</Elem>
							<Elem>4.647594</Elem>
							<Elem>4.762122</Elem>
							<Elem>4.880074</Elem>
							<Elem>4.999757</Elem>
							<Elem>5.119448</Elem>
							<Elem>5.237427</Elem>
							<Elem>5.351998</Elem>
							<Elem>5.461512</Elem>
							<Elem>5.564394</Elem>
							<Elem>5.659162</Elem>
							<Elem>5.744453</Elem>
							<Elem>5.819038</Elem>
							<Elem>5.881842</Elem>
							<Elem>5.93196</Elem>
							<Elem>5.968669</Elem>
							<Elem>5.991439</Elem>
							<Elem>5.999941</Elem>
							<Elem>5.994049</Elem>
							<Elem>5.973846</Elem>
							<Elem>5.939622</Elem>
							<Elem>5.891867</Elem>
							<Elem>5.831267</Elem>
							<Elem>5.758693</Elem>
							<Elem>5.675188</Elem>
							<Elem>5.581954</Elem>
							<Elem>5.480332</Elem>
							<Elem>5.371786</Elem>
							<Elem>5.257878</Elem>
							<Elem>5.140248</Elem>
							<Elem>5.020592</Elem>
							<Elem>4.900634</Elem>
							<Elem>4.782102</Elem>
							<Elem>4.666705</Elem>
							<Elem>4.556108</Elem>
							<Elem>4.451906</Elem>
							<Elem>4.355602</Elem>
							<Elem>4.268585</Elem>
							<Elem>4.192113</Elem>
							<Elem>4.127289</Elem>
							<Elem>4.075051</Elem>
							<Elem>4.036153</Elem>
							<Elem>4.011158</Elem>
							<Elem>4.00043</Elem>
							<Elem>4.004125</Elem>
							<Elem>4.022192</Elem>
							<Elem>4.054372</Elem>
							<Elem>4.100202</Elem>
							<Elem>4.159023</Elem>
							<Elem>4.229988</Elem>
							<Elem>4.312073</Elem>
							<Elem>4.404095</Elem>
							<Elem>4.504727</Elem>
							<Elem>4.612516</Elem>
							<Elem>4.725907</Elem>
							<Elem>4.843263</Elem>
							<Elem>4.962888</Elem>
							<Elem>5.083055</Elem>
							<Elem>5.202027</Elem>
							<Elem>5.318086</Elem>
							<Elem>5.429553</Elem>
							<Elem>5.534817</Elem>
							<Elem>5.632356</Elem>
							<Elem>5.720759</Elem>
							<Elem>5.798745</Elem>
							<Elem>5.865187</Elem>
							<Elem>5.919122</Elem>
							<Elem>5.959768</Elem>
							<Elem>5.986535</Elem>
							<Elem>5.999034</Elem>
							<Elem>5.997083</Elem>
							<Elem>5.980708</Elem>
							<Elem>5.950144</Elem>
							<Elem>5.90583</Elem>
							<Elem>5.848406</Elem>
							<Elem>5.778702</Elem>
							<Elem>5.697724</Elem>
							<Elem>5.606643</Elem>
							<Elem>5.506777</Elem>
							<Elem>5.399568</Elem>
							<Elem>5.28657</Elem>
							<Elem>5.169417</Elem>
							<Elem>5.049805</Elem>
							<Elem>4.929466</Elem>
							<Elem>4.810143</Elem>
							<Elem>4.693564</Elem>
							<Elem>4.58142</Elem>
							<Elem>4.475334</Elem>
							<Elem>4.376846</Elem>
							<Elem>4.287384</Elem>
							<Elem>4.208244</Elem>
							<Elem>4.140576</Elem>
							<Elem>4.085362</Elem>
							<Elem>4.043405</Elem>
							<Elem>4.015314</Elem>
							<Elem>4.001498</Elem>
							<Elem>4.002161</Elem>
							<Elem>4.017294</Elem>
							<Elem>4.046679</Elem>
							<Elem>4.089894</Elem>
							<Elem>4.146312</Elem>
							<Elem>4.215118</Elem>
							<Elem>4.295314</Elem>
							<Elem>4.385739</Elem>
							<Elem>4.485082</Elem>
							<Elem>4.591903</Elem>
							<Elem>4.704651</Elem>
							<Elem>4.821692</Elem>
							<Elem>4.941326</Elem>
							<Elem>5.061819</Elem>
							<Elem>5.181419</Elem>
							<Elem>5.29839</Elem>
							<Elem>5.411034</Elem>
							<Elem>5.517713</Elem>
							<Elem>5.616877</Elem>
							<Elem>5.707085</Elem>
							<Elem>5.787026</Elem>
							<Elem>5.855535</Elem>
							<Elem>5.911616</Elem>
							<Elem>5.954453</Elem>
							<Elem>5.983421</Elem>
							<Elem>5.998096</Elem>
							<Elem>5.998264</Elem>
							<Elem>5.983921</Elem>
							<Elem>5.955272</Elem>
							<Elem>5.912732</Elem>
							<Elem>5.856918</Elem>
							<Elem>5.78864</Elem>
							<Elem>5.708889</Elem>
							<Elem>5.618823</Elem>
							<Elem>5.519751</Elem>
							<Elem>5.413113</Elem>
							<Elem>5.300459</Elem>
							<Elem>5.183429</Elem>
							<Elem>5.063723</Elem>
							<Elem>4.943085</Elem>
							<Elem>4.82327</Elem>
							<Elem>4.706021</Elem>
							<Elem>4.593046</Elem>
							<Elem>4.485992</Elem>
							<Elem>4.386416</Elem>
							<Elem>4.29577</Elem>
							<Elem>4.215376</Elem>
							<Elem>4.146405</Elem>
							<Elem>4.089865</Elem>
							<Elem>4.04658</Elem>
							<Elem>4.017182</Elem>
							<Elem>4.002103</Elem>
							<Elem>4.001563</Elem>
							<Elem>4.015573</Elem>
							<Elem>4.043931</Elem>
							<Elem>4.086225</Elem>
							<Elem>4.141841</Elem>
							<Elem>4.209969</Elem>
							<Elem>4.289619</Elem>
							<Elem>4.37963</Elem>
							<Elem>4.478692</Elem>
							<Elem>4.58536</Elem>
							<Elem>4.698081</Elem>
							<Elem>4.815212</Elem>
							<Elem>4.935043</Elem>
							<Elem>5.055827</Elem>
							<Elem>5.175803</Elem>
							<Elem>5.293219</Elem>
							<Elem>5.406361</Elem>
							<Elem>5.513578</Elem>
							<Elem>5.613304</Elem>
							<Elem>5.704083</Elem>
							<Elem>5.784587</Elem>
							<Elem>5.85364</Elem>
							<Elem>5.910232</Elem>
							<Elem>5.953535</Elem>
							<Elem>5.982915</Elem>
							<Elem>5.997941</Elem>
							<Elem>5.99839</Elem>
							<Elem>5.984256</Elem>
							<Elem>5.955741</Elem>
							<Elem>5.913261</Elem>
							<Elem>5.857435</Elem>
							<Elem>5.789076</Elem>
							<Elem>5.709181</Elem>
							<Elem>5.618917</Elem>
							<Elem>5.519602</Elem>
							<Elem>5.412687</Elem>
							<Elem>5.299733</Elem>
							<Elem>5.182391</Elem>
							<Elem>5.062376</Elem>
							<Elem>4.941444</Elem>
							<Elem>4.821363</Elem>
							<Elem>4.703888</Elem>
							<Elem>4.590741</Elem>
							<Elem>4.483575</Elem>
							<Elem>4.38396</Elem>
							<Elem>4.293355</Elem>
							<Elem>4.213086</Elem>
							<Elem>4.14433</Elem>
							<Elem>4.088096</Elem>
							<Elem>4.045207</Elem>
							<Elem>4.016293</Elem>
							<Elem>4.001781</Elem>
							<Elem>4.001884</Elem>
							<Elem>4.016602</Elem>
							<Elem>4.045723</Elem>
							<Elem>4.088822</Elem>
							<Elem>4.14527</Elem>
							<Elem>4.214241</Elem>
							<Elem>4.294726</Elem>
							<Elem>4.385549</Elem>
							<Elem>4.48538</Elem>
							<Elem>4.592756</Elem>
							<Elem>4.706107</Elem>
							<Elem>4.82377</Elem>
							<Elem>4.944021</Elem>
							<Elem>5.065099</Elem>
							<Elem>5.185228</Elem>
							<Elem>5.302647</Elem>
							<Elem>5.415634</Elem>
							<Elem>5.52253</Elem>
							<Elem>5.621767</Elem>
							<Elem>5.711889</Elem>
							<Elem>5.791572</Elem>
							<Elem>5.859646</Elem>
							<Elem>5.91511</Elem>
							<Elem>5.957148</Elem>
							<Elem>5.985143</Elem>
							<Elem>5.998681</Elem>
							<Elem>5.997561</Elem>
							<Elem>5.981798</Elem>
							<Elem>5.951621</Elem>
							<Elem>5.907471</Elem>
							<Elem>5.849995</Elem>
							<Elem>5.780034</Elem>
							<Elem>5.698615</Elem>
							<Elem>5.606931</Elem>
							<Elem>5.506328</Elem>
							<Elem>5.398282</Elem>
							<Elem>5.284381</Elem>
							<Elem>5.166295</Elem>
							<Elem>5.04576</Elem>
							<Elem>4.924548</Elem>
							<Elem>4.804439</Elem>
							<Elem>4.687198</Elem>
							<Elem>4.57455</Elem>
							<Elem>4.468152</Elem>
							<Elem>4.369567</Elem>
							<Elem>4.280248</Elem>
							<Elem>4.201509</Elem>
							<Elem>4.134509</Elem>
							<Elem>4.080235</Elem>
							<Elem>4.039487</Elem>
							<Elem>4.012868</Elem>
							<Elem>4.000769</Elem>
							<Elem>4.003372</Elem>
							<Elem>4.02064</Elem>
							<Elem>4.052321</Elem>
							<Elem>4.097951</Elem>
							<Elem>4.156859</Elem>
							<Elem>4.228182</Elem>
							<Elem>4.31087</Elem>
							<Elem>4.403708</Elem>
							<Elem>4.50533</Elem>
							<Elem>4.614241</Elem>
							<Elem>4.728838</Elem>
							<Elem>4.847434</Elem>
							<Elem>4.968283</Elem>
							<Elem>5.089605</Elem>
							<Elem>5.209612</Elem>
							<Elem>5.326536</Elem>
							<Elem>5.438655</Elem>
							<Elem>5.544314</Elem>
							<Elem>5.641956</Elem>
							<Elem>5.730141</Elem>
							<Elem>5.807567</Elem>
							<Elem>5.873092</Elem>
							<Elem>5.925747</Elem>
							<Elem>5.964755</Elem>
							<Elem>5.989538</Elem>
							<Elem>5.999729</Elem>
							<Elem>5.995176</Elem>
							<Elem>5.975944</Elem>
							<Elem>5.942314</Elem>
							<Elem>5.894781</Elem>
							<Elem>5.834044</Elem>
							<Elem>5.760997</Elem>
							<Elem>5.676716</Elem>
							<Elem>5.582444</Elem>
							<Elem>5.479572</Elem>
							<Elem>5.369615</Elem>
							<Elem>5.254197</Elem>
							<Elem>5.13502</Elem>
							<Elem>5.013845</Elem>
							<Elem>4.892459</Elem>
							<Elem>4.772656</Elem>
							<Elem>4.656205</Elem>
							<Elem>4.544827</Elem>
							<Elem>4.440168</Elem>
							<Elem>4.343774</Elem>
							<Elem>4.257072</Elem>
							<Elem>4.181343</Elem>
							<Elem>4.117709</Elem>
							<Elem>4.067111</Elem>
							<Elem>4.030299</Elem>
							<Elem>4.007819</Elem>
							<Elem>4.000006</Elem>
							<Elem>4.006977</Elem>
							<Elem>4.028631</Elem>
							<Elem>4.064649</Elem>
							<Elem>4.114502</Elem>
							<Elem>4.177454</Elem>
							<Elem>4.252575</Elem>
							<Elem>4.338756</Elem>
							<Elem>4.434724</Elem>
							<Elem>4.539059</Elem>
							<Elem>4.65022</Elem>
							<Elem>4.766562</Elem>
							<Elem>4.886365</Elem>
							<Elem>5.007854</Elem>
							<Elem>5.129233</Elem>
							<Elem>5.248705</Elem>
							<Elem>5.3645</Elem>
							<Elem>5.474903</Elem>
							<Elem>5.578279</Elem>
							<Elem>5.673096</Elem>
							<Elem>5.757949</Elem>
							<Elem>5.831579</Elem>
							<Elem>5.892893</Elem>
							<Elem>5.940983</Elem>
							<Elem>5.975133</Elem>
							<Elem>5.994836</Elem>
							<Elem>5.999797</Elem>
							<Elem>5.989942</Elem>
							<Elem>5.965413</Elem>
							<Elem>5.926573</Elem>
							<Elem>5.873996</Elem>
							<Elem>5.808458</Elem>
							<Elem>5.73093</Elem>
							<Elem>5.642561</Elem>
							<Elem>5.544658</Elem>
							<Elem>5.438672</Elem>
							<Elem>5.326175</Elem>
							<Elem>5.208835</Elem>
							<Elem>5.088391</Elem>
							<Elem>4.96663</Elem>
							<Elem>4.845358</Elem>
							<Elem>4.726376</Elem>
							<Elem>4.611449</Elem>
							<Elem>4.502283</Elem>
							<Elem>4.400501</Elem>
							<Elem>4.307613</Elem>
							<Elem>4.225</Elem>
							<Elem>4.153891</Elem>
							<Elem>4.095342</Elem>
							<Elem>4.050225</Elem>
							<Elem>4.019212</Elem>
							<Elem>4.002765</Elem>
							<Elem>4.001131</Elem>
							<Elem>4.014336</Elem>
							<Elem>4.042186</Elem>
							<Elem>4.08427</Elem>
							<Elem>4.139962</Elem>
							<Elem>4.208439</Elem>
							<Elem>4.288684</Elem>
							<Elem>4.379506</Elem>
							<Elem>4.479556</Elem>
							<Elem>4.587348</Elem>
							<Elem>4.70128</Elem>
							<Elem>4.81966</Elem>
							<Elem>4.940727</Elem>
							<Elem>5.06268</Elem>
							<Elem>5.183708</Elem>
							<Elem>5.302008</Elem>
							<Elem>5.415821</Elem>
							<Elem>5.523452</Elem>
							<Elem>5.6233</Elem>
							<Elem>5.713877</Elem>
							<Elem>5.793835</Elem>
							<Elem>5.861981</Elem>
							<Elem>5.917299</Elem>
							<Elem>5.958966</Elem>
							<Elem>5.986357</Elem>
							<Elem>5.999064</Elem>
							<Elem>5.996895</Elem>
							<Elem>5.97988</Elem>
							<Elem>5.948271</Elem>
							<Elem>5.902537</Elem>
							<Elem>5.843356</Elem>
							<Elem>5.771609</Elem>
							<Elem>5.688363</Elem>
							<Elem>5.594856</Elem>
							<Elem>5.492481</Elem>
							<Elem>5.382762</Elem>
							<Elem>5.267333</Elem>
							<Elem>5.147914</Elem>
							<Elem>5.026285</Elem>
							<Elem>4.904258</Elem>
							<Elem>4.783653</Elem>
							<Elem>4.666268</Elem>
							<Elem>4.553855</Elem>
							<Elem>4.44809</Elem>
							<Elem>4.350552</Elem>
							<Elem>4.262697</Elem>
							<Elem>4.185837</Elem>
							<Elem>4.121121</Elem>
							<Elem>4.069515</Elem>
							<Elem>4.031791</Elem>
							<Elem>4.008515</Elem>
							<Elem>4.000035</Elem>
							<Elem>4.00648</Elem>
							<Elem>4.027757</Elem>
							<Elem>4.063549</Elem>
							<Elem>4.113325</Elem>
							<Elem>4.176342</Elem>
							<Elem>4.251662</Elem>
							<Elem>4.338161</Elem>
							<Elem>4.43455</Elem>
							<Elem>4.539389</Elem>
							<Elem>4.651114</Elem>
							<Elem>4.768057</Elem>
							<Elem>4.88847</Elem>
							<Elem>5.010556</Elem>
							<Elem>5.132489</Elem>
							<Elem>5.252448</Elem>
							<Elem>5.368639</Elem>
							<Elem>5.479325</Elem>
							<Elem>5.58285</Elem>
							<Elem>5.677666</Elem>
							<Elem>5.762353</Elem>
							<Elem>5.835645</Elem>
							<Elem>5.896442</Elem>
							<Elem>5.943834</Elem>
							<Elem>5.977111</Elem>
							<Elem>5.995773</Elem>
							<Elem>5.999538</Elem>
							<Elem>5.988348</Elem>
							<Elem>5.962368</Elem>
							<Elem>5.921985</Elem>
							<Elem>5.867802</Elem>
							<Elem>5.800628</Elem>
							<Elem>5.721465</Elem>
							<Elem>5.631499</Elem>
							<Elem>5.532074</Elem>
							<Elem>5.424677</Elem>
							<Elem>5.310916</Elem>
							<Elem>5.192494</Elem>
							<Elem>5.071183</Elem>
							<Elem>4.948801</Elem>
							<Elem>4.827179</Elem>
							<Elem>4.708142</Elem>
							<Elem>4.593471</Elem>
							<Elem>4.484887</Elem>
							<Elem>4.384017</Elem>
							<Elem>4.292374</Elem>
							<Elem>4.211334</Elem>
							<Elem>4.142111</Elem>
							<Elem>4.085746</Elem>
							<Elem>4.043085</Elem>
							<Elem>4.01477</Elem>
							<Elem>4.001227</Elem>
							<Elem>4.002662</Elem>
							<Elem>4.019056</Elem>
							<Elem>4.050163</Elem>
							<Elem>4.09552</Elem>
							<Elem>4.154449</Elem>
							<Elem>4.226066</Elem>
							<Elem>4.3093</Elem>
							<Elem>4.402902</Elem>
							<Elem>4.50547</Elem>
							<Elem>4.615464</Elem>
							<Elem>4.731236</Elem>
							<Elem>4.851048</Elem>
							<Elem>4.973101</Elem>
							<Elem>5.095564</Elem>
							<Elem>5.216598</Elem>
							<Elem>5.334384</Elem>
							<Elem>5.447154</Elem>
							<Elem>5.553213</Elem>
							<Elem>5.650966</Elem>
							<Elem>5.738945</Elem>
							<Elem>5.815825</Elem>
							<Elem>5.880451</Elem>
							<Elem>5.931849</Elem>
							<Elem>5.969245</Elem>
							<Elem>5.992075</Elem>
							<Elem>5.999995</Elem>
							<Elem>5.992882</Elem>
							<Elem>5.970841</Elem>
							<Elem>5.934203</Elem>
							<Elem>5.883516</Elem>
							<Elem>5.81954</Elem>
							<Elem>5.743236</Elem>
							<Elem>5.655749</Elem>
							<Elem>5.558394</Elem>
							<Elem>5.452635</Elem>
							<Elem>5.340061</Elem>
							<Elem>5.222365</Elem>
							<Elem>5.101317</Elem>
							<Elem>4.978739</Elem>
							<Elem>4.856475</Elem>
							<Elem>4.736367</Elem>
							<Elem>4.620221</Elem>
							<Elem>4.509787</Elem>
							<Elem>4.406729</Elem>
							<Elem>4.3126</Elem>
							<Elem>4.228818</Elem>
							<Elem>4.156646</Elem>
							<Elem>4.097173</Elem>
							<Elem>4.051296</Elem>
							<Elem>4.01971</Elem>
							<Elem>4.00289</Elem>
							<Elem>4.001094</Elem>
							<Elem>4.01435</Elem>
							<Elem>4.042459</Elem>
							<Elem>4.085002</Elem>
							<Elem>4.141338</Elem>
							<Elem>4.210621</Elem>
							<Elem>4.291806</Elem>
							<Elem>4.383673</Elem>
							<Elem>4.484838</Elem>
							<Elem>4.593775</Elem>
							<Elem>4.708844</Elem>
							<Elem>4.828309</Elem>
							<Elem>4.950369</Elem>
							<Elem>5.073184</Elem>
							<Elem>5.194901</Elem>
							<Elem>5.313682</Elem>
							<Elem>5.427735</Elem>
							<Elem>5.535339</Elem>
							<Elem>5.634868</Elem>
							<Elem>5.72482</Elem>
							<Elem>5.803834</Elem>
							<Elem>5.870717</Elem>
							<Elem>5.924457</Elem>
							<Elem>5.964242</Elem>
							<Elem>5.989467</Elem>
							<Elem>5.999751</Elem>
							<Elem>5.994936</Elem>
							<Elem>5.975093</Elem>
							<Elem>5.940519</Elem>
							<Elem>5.891734</Elem>
							<Elem>5.829475</Elem>
							<Elem>5.754678</Elem>
							<Elem>5.668474</Elem>
							<Elem>5.572164</Elem>
							<Elem>5.467201</Elem>
							<Elem>5.355171</Elem>
							<Elem>5.237767</Elem>
							<Elem>5.116763</Elem>
							<Elem>4.993988</Elem>
							<Elem>4.871299</Elem>
							<Elem>4.750549</Elem>
							<Elem>4.633568</Elem>
							<Elem>4.522123</Elem>
							<Elem>4.417902</Elem>
							<Elem>4.322482</Elem>
							<Elem>4.237309</Elem>
							<Elem>4.163671</Elem>
							<Elem>4.102687</Elem>
							<Elem>4.055279</Elem>
							<Elem>4.022167</Elem>
							<Elem>4.003855</Elem>
							<Elem>4.000622</Elem>
							<Elem>4.012519</Elem>
							<Elem>4.039367</Elem>
							<Elem>4.080763</Elem>
							<Elem>4.136081</Elem>
							<Elem>4.204485</Elem>
							<Elem>4.284942</Elem>
							<Elem>4.376233</Elem>
							<Elem>4.476979</Elem>
							<Elem>4.585653</Elem>
							<Elem>4.70061</Elem>
							<Elem>4.820109</Elem>
							<Elem>4.94234</Elem>
							<Elem>5.06545</Elem>
							<Elem>5.187574</Elem>
							<Elem>5.30686</Elem>
							<Elem>5.4215</Elem>
							<Elem>5.529754</Elem>
							<Elem>5.62998</Elem>
							<Elem>5.720658</Elem>
							<Elem>5.80041</Elem>
							<Elem>5.868026</Elem>
							<Elem>5.922479</Elem>
							<Elem>5.96294</Elem>
							<Elem>5.988794</Elem>
							<Elem>5.999647</Elem>
							<Elem>5.995331</Elem>
							<Elem>5.97591</Elem>
							<Elem>5.941677</Elem>
							<Elem>5.89315</Elem>
							<Elem>5.831063</Elem>
							<Elem>5.756356</Elem>
							<Elem>5.670163</Elem>
							<Elem>5.57379</Elem>
							<Elem>5.4687</Elem>
							<Elem>5.356487</Elem>
							<Elem>5.238855</Elem>
							<Elem>5.117589</Elem>
							<Elem>4.994531</Elem>
							<Elem>4.871551</Elem>
							<Elem>4.750516</Elem>
							<Elem>4.633267</Elem>
							<Elem>4.521586</Elem>
							<Elem>4.417171</Elem>
							<Elem>4.321609</Elem>
							<Elem>4.236355</Elem>
							<Elem>4.162705</Elem>
							<Elem>4.101782</Elem>
							<Elem>4.054514</Elem>
							<Elem>4.02162</Elem>
							<Elem>4.003604</Elem>
							<Elem>4.00074</Elem>
							<Elem>4.013076</Elem>
							<Elem>4.040425</Elem>
							<Elem>4.082373</Elem>
							<Elem>4.138285</Elem>
							<Elem>4.20731</Elem>
							<Elem>4.288402</Elem>
							<Elem>4.380326</Elem>
							<Elem>4.481686</Elem>
							<Elem>4.590941</Elem>
							<Elem>4.706427</Elem>
							<Elem>4.826388</Elem>
							<Elem>4.948998</Elem>
							<Elem>5.07239</Elem>
							<Elem>5.194685</Elem>
							<Elem>5.314021</Elem>
							<Elem>5.428579</Elem>
							<Elem>5.536614</Elem>
							<Elem>5.636479</Elem>
							<Elem>5.726652</Elem>
							<Elem>5.805758</Elem>
							<Elem>5.872588</Elem>
							<Elem>5.926124</Elem>
							<Elem>5.965547</Elem>
							<Elem>5.990255</Elem>
							<Elem>5.999869</Elem>
							<Elem>5.99424</Elem>
							<Elem>5.973453</Elem>
							<Elem>5.937821</Elem>
							<Elem>5.887887</Elem>
							<Elem>5.824409</Elem>
							<Elem>5.748355</Elem>
							<Elem>5.660882</Elem>
							<Elem>5.563323</Elem>
							<Elem>5.457166</Elem>
							<Elem>5.344029</Elem>
							<Elem>5.225637</Elem>
							<Elem>5.103797</Elem>
							<Elem>4.980366</Elem>
							<Elem>4.85723</Elem>
							<Elem>4.736268</Elem>
							<Elem>4.619326</Elem>
							<Elem>4.50819</Elem>
							<Elem>4.404559</Elem>
							<Elem>4.310016</Elem>
							<Elem>4.226006</Elem>
							<Elem>4.153813</Elem>
							<Elem>4.094541</Elem>
							<Elem>4.049099</Elem>
							<Elem>4.018181</Elem>
							<Elem>4.002263</Elem>
							<Elem>4.00159</Elem>
							<Elem>4.016174</Elem>
							<Elem>4.045793</Elem>
							<Elem>4.089999</Elem>
							<Elem>4.148116</Elem>
							<Elem>4.219259</Elem>
							<Elem>4.302341</Elem>
							<Elem>4.396093</Elem>
							<Elem>4.499085</Elem>
							<Elem>4.609741</Elem>
							<Elem>4.726371</Elem>
							<Elem>4.847192</Elem>
							<Elem>4.970356</Elem>
							<Elem>5.093978</Elem>
							<Elem>5.216169</Elem>
							<Elem>5.335057</Elem>
							<Elem>5.448824</Elem>
							<Elem>5.555727</Elem>
							<Elem>5.65413</Elem>
							<Elem>5.742524</Elem>
							<Elem>5.819556</Elem>
							<Elem>5.884045</Elem>
							<Elem>5.935002</Elem>
							<Elem>5.971644</Elem>
							<Elem>5.993408</Elem>
							<Elem>5.99996</Elem>
							<Elem>5.991196</Elem>
							<Elem>5.967249</Elem>
							<Elem>5.928484</Elem>
							<Elem>5.875492</Elem>
							<Elem>5.809083</Elem>
							<Elem>5.730274</Elem>
							<Elem>5.64027</Elem>
							<Elem>5.540449</Elem>
							<Elem>5.43234</Elem>
							<Elem>5.317598</Elem>
							<Elem>5.197983</Elem>
							<Elem>5.075327</Elem>
							<Elem>4.95151</Elem>
							<Elem>4.828431</Elem>
							<Elem>4.707978</Elem>
							<Elem>4.591998</Elem>
							<Elem>4.482271</Elem>
							<Elem>4.380481</Elem>
							<Elem>4.28819</Elem>
							<Elem>4.206817</Elem>
							<Elem>4.137611</Elem>
							<Elem>4.081635</Elem>
							<Elem>4.039751</Elem>
							<Elem>4.012604</Elem>
							<Elem>4.000611</Elem>
							<Elem>4.00396</Elem>
							<Elem>4.022601</Elem>
							<Elem>4.056249</Elem>
							<Elem>4.104391</Elem>
							<Elem>4.166288</Elem>
							<Elem>4.240993</Elem>
							<Elem>4.327359</Elem>
							<Elem>4.424062</Elem>
							<Elem>4.529617</Elem>
							<Elem>4.642403</Elem>
							<Elem>4.760689</Elem>
							<Elem>4.882658</Elem>
							<Elem>5.006435</Elem>
							<Elem>5.13012</Elem>
							<Elem>5.251809</Elem>
							<Elem>5.369634</Elem>
							<Elem>5.481781</Elem>
							<Elem>5.586526</Elem>
							<Elem>5.682257</Elem>
							<Elem>5.767501</Elem>
							<Elem>5.840945</Elem>
							<Elem>5.901459</Elem>
							<Elem>5.948108</Elem>
							<Elem>5.980175</Elem>
							<Elem>5.997164</Elem>
							<Elem>5.99881</Elem>
							<Elem>5.985088</Elem>
							<Elem>5.956205</Elem>
							<Elem>5.912605</Elem>
							<Elem>5.854956</Elem>
							<Elem>5.784144</Elem>
							<Elem>5.701257</Elem>
							<Elem>5.60757</Elem>
							<Elem>5.504524</Elem>
							<Elem>5.393704</Elem>
							<Elem>5.276816</Elem>
							<Elem>5.155659</Elem>
							<Elem>5.032099</Elem>
							<Elem>4.908039</Elem>
							<Elem>4.78539</Elem>
							<Elem>4.666042</Elem>
							<Elem>4.551834</Elem>
							<Elem>4.444528</Elem>
							<Elem>4.345777</Elem>
							<Elem>4.257106</Elem>
							<Elem>4.179881</Elem>
							<Elem>4.115295</Elem>
							<Elem>4.064346</Elem>
							<Elem>4.027821</Elem>
							<Elem>4.006286</Elem>
							<Elem>4.000073</Elem>
							<Elem>4.009282</Elem>
							<Elem>4.033772</Elem>
							<Elem>4.073167</Elem>
							<Elem>4.126862</Elem>
							<Elem>4.194031</Elem>
							<Elem>4.273639</Elem>
							<Elem>4.364459</Elem>
							<Elem>4.46509</Elem>
							<Elem>4.573982</Elem>
							<Elem>4.689455</Elem>
							<Elem>4.809726</Elem>
							<Elem>4.932941</Elem>
							<Elem>5.057196</Elem>
							<Elem>5.180574</Elem>
							<Elem>5.301169</Elem>
							<Elem>5.417119</Elem>
							<Elem>5.526631</Elem>
							<Elem>5.628013</Elem>
							<Elem>5.719699</Elem>
							<Elem>5.80027</Elem>
							<Elem>5.86848</Elem>
							<Elem>5.923273</Elem>
							<Elem>5.963801</Elem>
							<Elem>5.989435</Elem>
							<Elem>5.999778</Elem>
							<Elem>5.994667</Elem>
							<Elem>5.974178</Elem>
							<Elem>5.938628</Elem>
							<Elem>5.888563</Elem>
							<Elem>5.824756</Elem>
							<Elem>5.748191</Elem>
							<Elem>5.660052</Elem>
							<Elem>5.561699</Elem>
							<Elem>5.454652</Elem>
							<Elem>5.340567</Elem>
							<Elem>5.221208</Elem>
							<Elem>5.098421</Elem>
							<Elem>4.974105</Elem>
							<Elem>4.850184</Elem>
							<Elem>4.728576</Elem>
							<Elem>4.611165</Elem>
							<Elem>4.499767</Elem>
							<Elem>4.396108</Elem>
							<Elem>4.301795</Elem>
							<Elem>4.218289</Elem>
							<Elem>4.146884</Elem>
							<Elem>4.088689</Elem>
							<Elem>4.044605</Elem>
							<Elem>4.015319</Elem>
							<Elem>4.001286</Elem>
							<Elem>4.002725</Elem>
							<Elem>4.019615</Elem>
							<Elem>4.051699</Elem>
							<Elem>4.098479</Elem>
							<Elem>4.159234</Elem>
							<Elem>4.233023</Elem>
							<Elem>4.318705</Elem>
							<Elem>4.414952</Elem>
							<Elem>4.520274</Elem>
							<Elem>4.633039</Elem>
							<Elem>4.7515</Elem>
							<Elem>4.87382</Elem>
							<Elem>4.998103</Elem>
							<Elem>5.12242</Elem>
							<Elem>5.244844</Elem>
							<Elem>5.363476</Elem>
							<Elem>5.476473</Elem>
							<Elem>5.582082</Elem>
							<Elem>5.678663</Elem>
							<Elem>5.764715</Elem>
							<Elem>5.838903</Elem>
							<Elem>5.900072</Elem>
							<Elem>5.947272</Elem>
							<Elem>5.979767</Elem>
							<Elem>5.997051</Elem>
							<Elem>5.998854</Elem>
							<Elem>5.985146</Elem>
							<Elem>5.956136</Elem>
							<Elem>5.912275</Elem>
							<Elem>5.854241</Elem>
							<Elem>5.782933</Elem>
							<Elem>5.699459</Elem>
							<Elem>5.605113</Elem>
							<Elem>5.501359</Elem>
							<Elem>5.389809</Elem>
							<Elem>5.272196</Elem>
							<Elem>5.150347</Elem>
							<Elem>5.026155</Elem>
							<Elem>4.901551</Elem>
							<Elem>4.778472</Elem>
							<Elem>4.658832</Elem>
							<Elem>4.544492</Elem>
							<Elem>4.437231</Elem>
							<Elem>4.338717</Elem>
							<Elem>4.250486</Elem>
							<Elem>4.17391</Elem>
							<Elem>4.110182</Elem>
							<Elem>4.060296</Elem>
							<Elem>4.02503</Elem>
							<Elem>4.004934</Elem>
							<Elem>4.000324</Elem>
							<Elem>4.011273</Elem>
							<Elem>4.037613</Elem>
							<Elem>4.078936</Elem>
							<Elem>4.134601</Elem>
							<Elem>4.203742</Elem>
							<Elem>4.285286</Elem>
							<Elem>4.377964</Elem>
							<Elem>4.480333</Elem>
							<Elem>4.590802</Elem>
							<Elem>4.707649</Elem>
							<Elem>4.829056</Elem>
							<Elem>4.953132</Elem>
							<Elem>5.077944</Elem>
							<Elem>5.201547</Elem>
							<Elem>5.322015</Elem>
							<Elem>5.437469</Elem>
							<Elem>5.546109</Elem>
							<Elem>5.646241</Elem>
							<Elem>5.736303</Elem>
							<Elem>5.81489</Elem>
							<Elem>5.880773</Elem>
							<Elem>5.932924</Elem>
							<Elem>5.970529</Elem>
							<Elem>5.992998</Elem>
							<Elem>5.999978</Elem>
							<Elem>5.99136</Elem>
							<Elem>5.967275</Elem>
							<Elem>5.928097</Elem>
							<Elem>5.874435</Elem>
							<Elem>5.807125</Elem>
							<Elem>5.727215</Elem>
							<Elem>5.635951</Elem>
							<Elem>5.534756</Elem>
							<Elem>5.425208</Elem>
							<Elem>5.309017</Elem>
							<Elem>5.187996</Elem>
							<Elem>5.064033</Elem>
							<Elem>4.939065</Elem>
							<Elem>4.815044</Elem>
							<Elem>4.693905</Elem>
							<Elem>4.577543</Elem>
							<Elem>4.467775</Elem>
							<Elem>4.366317</Elem>
							<Elem>4.274756</Elem>
							<Elem>4.194525</Elem>
							<Elem>4.126877</Elem>
							<Elem>4.072873</Elem>
							<Elem>4.033358</Elem>
							<Elem>4.008952</Elem>
							<Elem>4.000039</Elem>
							<Elem>4.006759</Elem>
							<Elem>4.029011</Elem>
							<Elem>4.066448</Elem>
							<Elem>4.118486</Elem>
							<Elem>4.184314</Elem>
							<Elem>4.262905</Elem>
							<Elem>4.353029</Elem>
							<Elem>4.45328</Elem>
							<Elem>4.562089</Elem>
							<Elem>4.677755</Elem>
							<Elem>4.798469</Elem>
							<Elem>4.922343</Elem>
							<Elem>5.047438</Elem>
							<Elem>5.171796</Elem>
							<Elem>5.29347</Elem>
							<Elem>5.410555</Elem>
							<Elem>5.521217</Elem>
							<Elem>5.623722</Elem>
							<Elem>5.716464</Elem>
							<Elem>5.797989</Elem>
							<Elem>5.867018</Elem>
							<Elem>5.922469</Elem>
							<Elem>5.963471</Elem>
							<Elem>5.98938</Elem>
							<Elem>5.999788</Elem>
							<Elem>5.994529</Elem>
							<Elem>5.973683</Elem>
							<Elem>5.937576</Elem>
							<Elem>5.886772</Elem>
							<Elem>5.822064</Elem>
							<Elem>5.744465</Elem>
							<Elem>5.655191</Elem>
							<Elem>5.555639</Elem>
							<Elem>5.447369</Elem>
							<Elem>5.332079</Elem>
							<Elem>5.211575</Elem>
							<Elem>5.087746</Elem>
							<Elem>4.962536</Elem>
							<Elem>4.837907</Elem>
							<Elem>4.715816</Elem>
							<Elem>4.59818</Elem>
							<Elem>4.486843</Elem>
							<Elem>4.383555</Elem>
							<Elem>4.289938</Elem>
							<Elem>4.207463</Elem>
							<Elem>4.137426</Elem>
							<Elem>4.080928</Elem>
							<Elem>4.038859</Elem>
							<Elem>4.01188</Elem>
							<Elem>4.000417</Elem>
							<Elem>4.004654</Elem>
							<Elem>4.024524</Elem>
							<Elem>4.059718</Elem>
							<Elem>4.109686</Elem>
							<Elem>4.173644</Elem>
							<Elem>4.250589</Elem>
							<Elem>4.339314</Elem>
							<Elem>4.438426</Elem>
							<Elem>4.546369</Elem>
							<Elem>4.661447</Elem>
							<Elem>4.781852</Elem>
							<Elem>4.905692</Elem>
							<Elem>5.03102</Elem>
							<Elem>5.155866</Elem>
							<Elem>5.278267</Elem>
							<Elem>5.396297</Elem>
							<Elem>5.508099</Elem>
							<Elem>5.611914</Elem>
							<Elem>5.706107</Elem>
							<Elem>5.789196</Elem>
							<Elem>5.859871</Elem>
							<Elem>5.91702</Elem>
							<Elem>5.959739</Elem>
							<Elem>5.987356</Elem>
							<Elem>5.999434</Elem>
							<Elem>5.99578</Elem>
							<Elem>5.97645</Elem>
							<Elem>5.941746</Elem>
							<Elem>5.892212</Elem>
							<Elem>5.828627</Elem>
							<Elem>5.751989</Elem>
							<Elem>5.663505</Elem>
							<Elem>5.564566</Elem>
							<Elem>5.456729</Elem>
							<Elem>5.341692</Elem>
							<Elem>5.221267</Elem>
							<Elem>5.097349</Elem>
							<Elem>4.971892</Elem>
							<Elem>4.846873</Elem>
							<Elem>4.724261</Elem>
							<Elem>4.60599</Elem>
							<Elem>4.493925</Elem>
							<Elem>4.389833</Elem>
							<Elem>4.295357</Elem>
							<Elem>4.211987</Elem>
							<Elem>4.14104</Elem>
							<Elem>4.083636</Elem>
							<Elem>4.040683</Elem>
							<Elem>4.01286</Elem>
							<Elem>4.000608</Elem>
							<Elem>4.004122</Elem>
							<Elem>4.023349</Elem>
							<Elem>4.057988</Elem>
							<Elem>4.107494</Elem>
							<Elem>4.171087</Elem>
							<Elem>4.247767</Elem>
							<Elem>4.336325</Elem>
							<Elem>4.435363</Elem>
							<Elem>4.54332</Elem>
							<Elem>4.658492</Elem>
							<Elem>4.779063</Elem>
							<Elem>4.903128</Elem>
							<Elem>5.028728</Elem>
							<Elem>5.15388</Elem>
							<Elem>5.276607</Elem>
							<Elem>5.39497</Elem>
							<Elem>5.507097</Elem>
							<Elem>5.611218</Elem>
							<Elem>5.705685</Elem>
							<Elem>5.789003</Elem>
							<Elem>5.859855</Elem>
							<Elem>5.91712</Elem>
							<Elem>5.959889</Elem>
							<Elem>5.987485</Elem>
							<Elem>5.99947</Elem>
							<Elem>5.995652</Elem>
							<Elem>5.976089</Elem>
							<Elem>5.941089</Elem>
							<Elem>5.891203</Elem>
							<Elem>5.827217</Elem>
							<Elem>5.750143</Elem>
							<Elem>5.661199</Elem>
							<Elem>5.561788</Elem>
							<Elem>5.453484</Elem>
							<Elem>5.337999</Elem>
							<Elem>5.217159</Elem>
							<Elem>5.092877</Elem>
							<Elem>4.967119</Elem>
							<Elem>4.841877</Elem>
							<Elem>4.719131</Elem>
							<Elem>4.600828</Elem>
							<Elem>4.48884</Elem>
							<Elem>4.384942</Elem>
							<Elem>4.29078</Elem>
							<Elem>4.207847</Elem>
							<Elem>4.137458</Elem>
							<Elem>4.08073</Elem>
							<Elem>4.038564</Elem>
							<Elem>4.01163</Elem>
							<Elem>4.000356</Elem>
							<Elem>4.004924</Elem>
							<Elem>4.025262</Elem>
							<Elem>4.061052</Elem>
							<Elem>4.111726</Elem>
							<Elem>4.176485</Elem>
							<Elem>4.254303</Elem>
							<Elem>4.343949</Elem>
							<Elem>4.444002</Elem>
							<Elem>4.552876</Elem>
							<Elem>4.668847</Elem>
							<Elem>4.790076</Elem>
							<Elem>4.91464</Elem>
							<Elem>5.040564</Elem>
							<Elem>5.16585</Elem>
							<Elem>5.28851</Elem>
							<Elem>5.406598</Elem>
							<Elem>5.518237</Elem>
							<Elem>5.621657</Elem>
							<Elem>5.715213</Elem>
							<Elem>5.79742</Elem>
							<Elem>5.866971</Elem>
							<Elem>5.92276</Elem>
							<Elem>5.963899</Elem>
							<Elem>5.989733</Elem>
							<Elem>5.99985</Elem>
							<Elem>5.994087</Elem>
							<Elem>5.972533</Elem>
							<Elem>5.935528</Elem>
							<Elem>5.883659</Elem>
							<Elem>5.817748</Elem>
							<Elem>5.738839</Elem>
							<Elem>5.648186</Elem>
							<Elem>5.547227</Elem>
							<Elem>5.437565</Elem>
							<Elem>5.320944</Elem>
							<Elem>5.199215</Elem>
							<Elem>5.074313</Elem>
							<Elem>4.948224</Elem>
							<Elem>4.822953</Elem>
							<Elem>4.700492</Elem>
							<Elem>4.582789</Elem>
							<Elem>4.471717</Elem>
							<Elem>4.369043</Elem>
							<Elem>4.276402</Elem>
							<Elem>4.19527</Elem>
							<Elem>4.126938</Elem>
							<Elem>4.072497</Elem>
							<Elem>4.032813</Elem>
							<Elem>4.008521</Elem>
							<Elem>4.00001</Elem>
							<Elem>4.007416</Elem>
							<Elem>4.030625</Elem>
							<Elem>4.069269</Elem>
						</DoubleArray>
					</Property>
					<Property Name="Times">
						<DoubleArray>
							<Elem>0</Elem>
							<Elem>0.01</Elem>
							<Elem>0.02</Elem>
							<Elem>0.03</Elem>
							<Elem>0.04</Elem>
							<Elem>0.05</Elem>
							<Elem>0.06</Elem>
							<Elem>0.07</Elem>
							<Elem>0.08</Elem>
							<Elem>0.09</Elem>
							<Elem>0.1</Elem>
							<Elem>0.11</Elem>
							<Elem>0.12</Elem>
							<Elem>0.13</Elem>
							<Elem>0.14</Elem>
							<Elem>0.15</Elem>
							<Elem>0.16</Elem>
							<Elem>0.17</Elem>
							<Elem>0.18</Elem>
							<Elem>0.19</Elem>
							<Elem>0.2</Elem>
							<Elem>0.21</Elem>
							<Elem>0.22</Elem>
							<Elem>0.23</Elem>
							<Elem>0.24</Elem>
							<Elem>0.25</Elem>
							<Elem>0.26</Elem>
							<Elem>0.27</Elem>
							<Elem>0.28</Elem>
							<Elem>0.29</Elem>
							<Elem>0.3</Elem>
							<Elem>0.31</Elem>
							<Elem>0.32</Elem>
							<Elem>0.33</Elem>
							<Elem>0.34</Elem>
							<Elem>0.35</Elem>
							<Elem>0.36</Elem>
							<Elem>0.37</Elem>
							<Elem>0.38</Elem>
							<Elem>0.39</Elem>
							<Elem>0.4</Elem>
							<Elem>0.41</Elem>
							<Elem>0.42</Elem>
							<Elem>0.43</Elem>
							<Elem>0.44</Elem>
							<Elem>0.45</Elem>
							<Elem>0.46</Elem>
							<Elem>0.47</Elem>
							<Elem>0.48</Elem>
							<Elem>0.49</Elem>
							<Elem>0.5</Elem>
							<Elem>0.51</Elem>
							<Elem>0.52</Elem>
							<Elem>0.53</Elem>
							<Elem>0.54</Elem>
							<Elem>0.55</Elem>
							<Elem>0.56</Elem>
							<Elem>0.57</Elem>
							<Elem>0.58</Elem>
							<Elem>0.59</Elem>
							<Elem>0.6</Elem>
							<Elem>0.61</Elem>
							<Elem>0.62</Elem>
							<Elem>0.63</Elem>
							<Elem>0.64</Elem>
							<Elem>0.65</Elem>
							<Elem>0.66</Elem>
							<Elem>0.67</Elem>
							<Elem>0.68</Elem>
							<Elem>0.69</Elem>
							<Elem>0.7</Elem>
							<Elem>0.71</Elem>
							<Elem>0.72</Elem>
							<Elem>0.73</Elem>
							<Elem>0.74</Elem>
							<Elem>0.75</Elem>
							<Elem>0.76</Elem>
							<Elem>0.77</Elem>
							<Elem>0.78</Elem>
							<Elem>0.79</Elem>
							<Elem>0.8</Elem>
							<Elem>0.81</Elem>
							<Elem>0.82</Elem>
							<Elem>0.83</Elem>
							<Elem>0.84</Elem>
							<Elem>0.85</Elem>
							<Elem>0.86</Elem>
							<Elem>0.87</Elem>
							<Elem>0.88</Elem>
							<Elem>0.89</Elem>
							<Elem>0.9</Elem>
							<Elem>0.91</Elem>
							<Elem>0.92</Elem>
							<Elem>0.93</Elem>
							<Elem>0.94</Elem>
							<Elem>0.95</Elem>
							<Elem>0.96</Elem>
							<Elem>0.97</Elem>
							<Elem>0.98</Elem>
							<Elem>0.99</Elem>
							<Elem>1</Elem>
							<Elem>1.01</Elem>
							<Elem>1.02</Elem>
							<Elem>1.03</Elem>
							<Elem>1.04</Elem>
							<Elem>1.05</Elem>
							<Elem>1.06</Elem>
							<Elem>1.07</Elem>
							<Elem>1.08</Elem>
							<Elem>1.09</Elem>
							<Elem>1.1</Elem>
							<Elem>1.11</Elem>
							<Elem>1.12</Elem>
							<Elem>1.13</Elem>
							<Elem>1.14</Elem>
							<Elem>1.15</Elem>
							<Elem>1.16</Elem>
							<Elem>1.17</Elem>
							<Elem>1.18</Elem>
							<Elem>1.19</Elem>
							<Elem>1.2</Elem>
							<Elem>1.21</Elem>
							<Elem>1.22</Elem>
							<Elem>1.23</Elem>
							<Elem>1.24</Elem>
							<Elem>1.25</Elem>
							<Elem>1.26</Elem>
							<Elem>1.27</Elem>
							<Elem>1.28</Elem>
							<Elem>1.29</Elem>
							<Elem>1.3</Elem>
							<Elem>1.31</Elem>
							<Elem>1.32</Elem>
							<Elem>1.33</Elem>
							<Elem>1.34</Elem>
							<Elem>1.35</Elem>
							<Elem>1.36</Elem>
							<Elem>1.37</Elem>
							<Elem>1.38</Elem>
							<Elem>1.39</Elem>
							<Elem>1.4</Elem>
							<Elem>1.41</Elem>
							<Elem>1.42</Elem>
							<Elem>1.43</Elem>
							<Elem>1.44</Elem>
							<Elem>1.45</Elem>
							<Elem>1.46</Elem>
							<Elem>1.47</Elem>
							<Elem>1.48</Elem>
							<Elem>1.49</Elem>
							<Elem>1.5</Elem>
							<Elem>1.51</Elem>
							<Elem>1.52</Elem>
							<Elem>1.53</Elem>
							<Elem>1.54</Elem>
							<Elem>1.55</Elem>
							<Elem>1.56</Elem>
							<Elem>1.57</Elem>
							<Elem>1.58</Elem>
							<Elem>1.59</Elem>
							<Elem>1.6</Elem>
							<Elem>1.61</Elem>
							<Elem>1.62</Elem>
							<Elem>1.63</Elem>
							<Elem>1.64</Elem>
							<Elem>1.65</Elem>
							<Elem>1.66</Elem>
							<Elem>1.67</Elem>
							<Elem>1.68</Elem>
							<Elem>1.69</Elem>
							<Elem>1.7</Elem>
							<Elem>1.71</Elem>
							<Elem>1.72</Elem>
							<Elem>1.73</Elem>
							<Elem>1.74</Elem>
							<Elem>1.75</Elem>
							<Elem>1.76</Elem>
							<Elem>1.77</Elem>
							<Elem>1.78</Elem>
							<Elem>1.79</Elem>
							<Elem>1.8</Elem>
							<Elem>1.81</Elem>
							<Elem>1.82</Elem>
							<Elem>1.83</Elem>
							<Elem>1.84</Elem>
							<Elem>1.85</Elem>
							<Elem>1.86</Elem>
							<Elem>1.87</Elem>
							<Elem>1.88</Elem>
							<Elem>1.89</Elem>
							<Elem>1.9</Elem>
							<Elem>1.91</Elem>
							<Elem>1.92</Elem>
							<Elem>1.93</Elem>
							<Elem>1.94</Elem>
							<Elem>1.95</Elem>
							<Elem>1.96</Elem>
							<Elem>1.97</Elem>
							<Elem>1.98</Elem>
							<Elem>1.99</Elem>
							<Elem>2</Elem>
							<Elem>2.01</Elem>
							<Elem>2.02</Elem>
							<Elem>2.03</Elem>
							<Elem>2.04</Elem>
							<Elem>2.05</Elem>
							<Elem>2.06</Elem>
							<Elem>2.07</Elem>
							<Elem>2.08</Elem>
							<Elem>2.09</Elem>
							<Elem>2.1</Elem>
							<Elem>2.11</Elem>
							<Elem>2.12</Elem>
							<Elem>2.13</Elem>
							<Elem>2.14</Elem>
							<Elem>2.15</Elem>
							<Elem>2.16</Elem>
							<Elem>2.17</Elem>
							<Elem>2.18</Elem>
							<Elem>2.19</Elem>
							<Elem>2.2</Elem>
							<Elem>2.21</Elem>
							<Elem>2.22</Elem>
							<Elem>2.23</Elem>
							<Elem>2.24</Elem>
							<Elem>2.25</Elem>
							<Elem>2.26</Elem>
							<Elem>2.27</Elem>
							<Elem>2.28</Elem>
							<Elem>2.29</Elem>
							<Elem>2.3</Elem>
							<Elem>2.31</Elem>
							<Elem>2.32</Elem>
							<Elem>2.33</Elem>
							<Elem>2.34</Elem>
							<Elem>2.35</Elem>
							<Elem>2.36</Elem>
							<Elem>2.37</Elem>
							<Elem>2.38</Elem>
							<Elem>2.39</Elem>
							<Elem>2.4</Elem>
							<Elem>2.41</Elem>
							<Elem>2.42</Elem>
							<Elem>2.43</Elem>
							<Elem>2.44</Elem>
							<Elem>2.45</Elem>
							<Elem>2.46</Elem>
							<Elem>2.47</Elem>
							<Elem>2.48</Elem>
							<Elem>2.49</Elem>
							<Elem>2.5</Elem>
							<Elem>2.51</Elem>
							<Elem>2.52</Elem>
							<Elem>2.53</Elem>
							<Elem>2.54</Elem>
							<Elem>2.55</Elem>
							<Elem>2.56</Elem>
							<Elem>2.57</Elem>
							<Elem>2.58</Elem>
							<Elem>2.59</Elem>
							<Elem>2.6</Elem>
							<Elem>2.61</Elem>
							<Elem>2.62</Elem>
							<Elem>2.63</Elem>
							<Elem>2.64</Elem>
							<Elem>2.65</Elem>
							<Elem>2.66</Elem>
							<Elem>2.67</Elem>
							<Elem>2.68</Elem>
							<Elem>2.69</Elem>
							<Elem>2.7</Elem>
							<Elem>2.71</Elem>
							<Elem>2.72</Elem>
							<Elem>2.73</Elem>
							<Elem>2.74</Elem>
							<Elem>2.75</Elem>
							<Elem>2.76</Elem>
							<Elem>2.77</Elem>
							<Elem>2.78</Elem>
							<Elem>2.79</Elem>
							<Elem>2.8</Elem>
							<Elem>2.81</Elem>
							<Elem>2.82</Elem>
							<Elem>2.83</Elem>
							<Elem>2.84</Elem>
							<Elem>2.85</Elem>
							<Elem>2.86</Elem>
							<Elem>2.87</Elem>
							<Elem>2.88</Elem>
							<Elem>2.89</Elem>
							<Elem>2.9</Elem>
							<Elem>2.91</Elem>
							<Elem>2.92</Elem>
							<Elem>2.93</Elem>
							<Elem>2.94</Elem>
							<Elem>2.95</Elem>
							<Elem>2.96</Elem>
							<Elem>2.97</Elem>
							<Elem>2.98</Elem>
							<Elem>2.99</Elem>
							<Elem>3</Elem>
							<Elem>3.01</Elem>
							<Elem>3.02</Elem>
							<Elem>3.03</Elem>
							<Elem>3.04</Elem>
							<Elem>3.05</Elem>
							<Elem>3.06</Elem>
							<Elem>3.07</Elem>
							<Elem>3.08</Elem>
							<Elem>3.09</Elem>
							<Elem>3.1</Elem>
							<Elem>3.11</Elem>
							<Elem>3.12</Elem>
							<Elem>3.13</Elem>
							<Elem>3.14</Elem>
							<Elem>3.15</Elem>
							<Elem>3.16</Elem>
							<Elem>3.17</Elem>
							<Elem>3.18</Elem>
							<Elem>3.19</Elem>
							<Elem>3.2</Elem>
							<Elem>3.21</Elem>
							<Elem>3.22</Elem>
							<Elem>3.23</Elem>
							<Elem>3.24</Elem>
							<Elem>3.25</Elem>
							<Elem>3.26</Elem>
							<Elem>3.27</Elem>
							<Elem>3.28</Elem>
							<Elem>3.29</Elem>
							<Elem>3.3</Elem>
							<Elem>3.31</Elem>
							<Elem>3.32</Elem>
							<Elem>3.33</Elem>
							<Elem>3.34</Elem>
							<Elem>3.35</Elem>
							<Elem>3.36</Elem>
							<Elem>3.37</Elem>
							<Elem>3.38</Elem>
							<Elem>3.39</Elem>
							<Elem>3.4</Elem>
							<Elem>3.41</Elem>
							<Elem>3.42</Elem>
							<Elem>3.43</Elem>
							<Elem>3.44</Elem>
							<Elem>3.45</Elem>
							<Elem>3.46</Elem>
							<Elem>3.47</Elem>
							<Elem>3.48</Elem>
							<Elem>3.49</Elem>
							<Elem>3.5</Elem>
							<Elem>3.51</Elem>
							<Elem>3.52</Elem>
							<Elem>3.53</Elem>
							<Elem>3.54</Elem>
							<Elem>3.55</Elem>
							<Elem>3.56</Elem>
							<Elem>3.57</Elem>
							<Elem>3.58</Elem>
							<Elem>3.59</Elem>
							<Elem>3.6</Elem>
							<Elem>3.61</Elem>
							<Elem>3.62</Elem>
							<Elem>3.63</Elem>
							<Elem>3.64</Elem>
							<Elem>3.65</Elem>
							<Elem>3.66</Elem>
							<Elem>3.67</Elem>
							<Elem>3.68</Elem>
							<Elem>3.69</Elem>
							<Elem>3.7</Elem>
							<Elem>3.71</Elem>
							<Elem>3.72</Elem>
							<Elem>3.73</Elem>
							<Elem>3.74</Elem>
							<Elem>3.75</Elem>
							<Elem>3.76</Elem>
							<Elem>3.77</Elem>
							<Elem>3.78</Elem>
							<Elem>3.79</Elem>
							<Elem>3.8</Elem>
							<Elem>3.81</Elem>
							<Elem>3.82</Elem>
							<Elem>3.83</Elem>
							<Elem>3.84</Elem>
							<Elem>3.85</Elem>
							<Elem>3.86</Elem>
							<Elem>3.87</Elem>
							<Elem>3.88</Elem>
							<Elem>3.89</Elem>
							<Elem>3.9</Elem>
							<Elem>3.91</Elem>
							<Elem>3.92</Elem>
							<Elem>3.93</Elem>
							<Elem>3.94</Elem>
							<Elem>3.95</Elem>
							<Elem>3.96</Elem>
							<Elem>3.97</Elem>
							<Elem>3.98</Elem>
							<Elem>3.99</Elem>
							<Elem>4</Elem>
							<Elem>4.01</Elem>
							<Elem>4.02</Elem>
							<Elem>4.03</Elem>
							<Elem>4.04</Elem>
							<Elem>4.05</Elem>
							<Elem>4.06</Elem>
							<Elem>4.07</Elem>
							<Elem>4.08</Elem>
							<Elem>4.09</Elem>
							<Elem>4.1</Elem>
							<Elem>4.11</Elem>
							<Elem>4.12</Elem>
							<Elem>4.13</Elem>
							<Elem>4.14</Elem>
							<Elem>4.15</Elem>
							<Elem>4.16</Elem>
							<Elem>4.17</Elem>
							<Elem>4.18</Elem>
							<Elem>4.19</Elem>
							<Elem>4.2</Elem>
							<Elem>4.21</Elem>
							<Elem>4.22</Elem>
							<Elem>4.23</Elem>
							<Elem>4.24</Elem>
							<Elem>4.25</Elem>
							<Elem>4.26</Elem>
							<Elem>4.27</Elem>
							<Elem>4.28</Elem>
							<Elem>4.29</Elem>
							<Elem>4.3</Elem>
							<Elem>4.31</Elem>
							<Elem>4.32</Elem>
							<Elem>4.33</Elem>
							<Elem>4.34</Elem>
							<Elem>4.35</Elem>
							<Elem>4.36</Elem>
							<Elem>4.37</Elem>
							<Elem>4.38</Elem>
							<Elem>4.39</Elem>
							<Elem>4.4</Elem>
							<Elem>4.41</Elem>
							<Elem>4.42</Elem>
							<Elem>4.43</Elem>
							<Elem>4.44</Elem>
							<Elem>4.45</Elem>
							<Elem>4.46</Elem>
							<Elem>4.47</Elem>
							<Elem>4.48</Elem>
							<Elem>4.49</Elem>
							<Elem>4.5</Elem>
							<Elem>4.51</Elem>
							<Elem>4.52</Elem>
							<Elem>4.53</Elem>
							<Elem>4.54</Elem>
							<Elem>4.55</Elem>
							<Elem>4.56</Elem>
							<Elem>4.57</Elem>
							<Elem>4.58</Elem>
							<Elem>4.59</Elem>
							<Elem>4.6</Elem>
							<Elem>4.61</Elem>
							<Elem>4.62</Elem>
							<Elem>4.63</Elem>
							<Elem>4.64</Elem>
							<Elem>4.65</Elem>
							<Elem>4.66</Elem>
							<Elem>4.67</Elem>
							<Elem>4.68</Elem>
							<Elem>4.69</Elem>
							<Elem>4.7</Elem>
							<Elem>4.71</Elem>
							<Elem>4.72</Elem>
							<Elem>4.73</Elem>
							<Elem>4.74</Elem>
							<Elem>4.75</Elem>
							<Elem>4.76</Elem>
							<Elem>4.77</Elem>
							<Elem>4.78</Elem>
							<Elem>4.79</Elem>
							<Elem>4.8</Elem>
							<Elem>4.81</Elem>
							<Elem>4.82</Elem>
							<Elem>4.83</Elem>
							<Elem>4.84</Elem>
							<Elem>4.85</Elem>
							<Elem>4.86</Elem>
							<Elem>4.87</Elem>
							<Elem>4.88</Elem>
							<Elem>4.89</Elem>
							<Elem>4.9</Elem>
							<Elem>4.91</Elem>
							<Elem>4.92</Elem>
							<Elem>4.93</Elem>
							<Elem>4.94</Elem>
							<Elem>4.95</Elem>
							<Elem>4.96</Elem>
							<Elem>4.97</Elem>
							<Elem>4.98</Elem>
							<Elem>4.99</Elem>
							<Elem>5</Elem>
							<Elem>5.01</Elem>
							<Elem>5.02</Elem>
							<Elem>5.03</Elem>
							<Elem>5.04</Elem>
							<Elem>5.05</Elem>
							<Elem>5.06</Elem>
							<Elem>5.07</Elem>
							<Elem>5.08</Elem>
							<Elem>5.09</Elem>
							<Elem>5.1</Elem>
							<Elem>5.11</Elem>
							<Elem>5.12</Elem>
							<Elem>5.13</Elem>
							<Elem>5.14</Elem>
							<Elem>5.15</Elem>
							<Elem>5.16</Elem>
							<Elem>5.17</Elem>
							<Elem>5.18</Elem>
							<Elem>5.19</Elem>
							<Elem>5.2</Elem>
							<Elem>5.21</Elem>
							<Elem>5.22</Elem>
							<Elem>5.23</Elem>
							<Elem>5.24</Elem>
							<Elem>5.25</Elem>
							<Elem>5.26</Elem>
							<Elem>5.27</Elem>
							<Elem>5.28</Elem>
							<Elem>5.29</Elem>
							<Elem>5.3</Elem>
							<Elem>5.31</Elem>
							<Elem>5.32</Elem>
							<Elem>5.33</Elem>
							<Elem>5.34</Elem>
							<Elem>5.35</Elem>
							<Elem>5.36</Elem>
							<Elem>5.37</Elem>
							<Elem>5.38</Elem>
							<Elem>5.39</Elem>
							<Elem>5.4</Elem>
							<Elem>5.41</Elem>
							<Elem>5.42</Elem>
							<Elem>5.43</Elem>
							<Elem>5.44</Elem>
							<Elem>5.45</Elem>
							<Elem>5.46</Elem>
							<Elem>5.47</Elem>
							<Elem>5.48</Elem>
							<Elem>5.49</Elem>
							<Elem>5.5</Elem>
							<Elem>5.51</Elem>
							<Elem>5.52</Elem>
							<Elem>5.53</Elem>
							<Elem>5.54</Elem>
							<Elem>5.55</Elem>
							<Elem>5.56</Elem>
							<Elem>5.57</Elem>
							<Elem>5.58</Elem>
							<Elem>5.59</Elem>
							<Elem>5.6</Elem>
							<Elem>5.61</Elem>
							<Elem>5.62</Elem>
							<Elem>5.63</Elem>
							<Elem>5.64</Elem>
							<Elem>5.65</Elem>
							<Elem>5.66</Elem>
							<Elem>5.67</Elem>
							<Elem>5.68</Elem>
							<Elem>5.69</Elem>
							<Elem>5.7</Elem>
							<Elem>5.71</Elem>
							<Elem>5.72</Elem>
							<Elem>5.73</Elem>
							<Elem>5.74</Elem>
							<Elem>5.75</Elem>
							<Elem>5.76</Elem>
							<Elem>5.77</Elem>
							<Elem>5.78</Elem>
							<Elem>5.79</Elem>
							<Elem>5.8</Elem>
							<Elem>5.81</Elem>
							<Elem>5.82</Elem>
							<Elem>5.83</Elem>
							<Elem>5.84</Elem>
							<Elem>5.85</Elem>
							<Elem>5.86</Elem>
							<Elem>5.87</Elem>
							<Elem>5.88</Elem>
							<Elem>5.89</Elem>
							<Elem>5.9</Elem>
							<Elem>5.91</Elem>
							<Elem>5.92</Elem>
							<Elem>5.93</Elem>
							<Elem>5.94</Elem>
							<Elem>5.95</Elem>
							<Elem>5.96</Elem>
							<Elem>5.97</Elem>
							<Elem>5.98</Elem>
							<Elem>5.99</Elem>
							<Elem>6</Elem>
							<Elem>6.01</Elem>
							<Elem>6.02</Elem>
							<Elem>6.03</Elem>
							<Elem>6.04</Elem>
							<Elem>6.05</Elem>
							<Elem>6.06</Elem>
							<Elem>6.07</Elem>
							<Elem>6.08</Elem>
							<Elem>6.09</Elem>
							<Elem>6.1</Elem>
							<Elem>6.11</Elem>
							<Elem>6.12</Elem>
							<Elem>6.13</Elem>
							<Elem>6.14</Elem>
							<Elem>6.15</Elem>
							<Elem>6.16</Elem>
							<Elem>6.17</Elem>
							<Elem>6.18</Elem>
							<Elem>6.19</Elem>
							<Elem>6.2</Elem>
							<Elem>6.21</Elem>
							<Elem>6.22</Elem>
							<Elem>6.23</Elem>
							<Elem>6.24</Elem>
							<Elem>6.25</Elem>
							<Elem>6.26</Elem>
							<Elem>6.27</Elem>
							<Elem>6.28</Elem>
							<Elem>6.29</Elem>
							<Elem>6.3</Elem>
							<Elem>6.31</Elem>
							<Elem>6.32</Elem>
							<Elem>6.33</Elem>
							<Elem>6.34</Elem>
							<Elem>6.35</Elem>
							<Elem>6.36</Elem>
							<Elem>6.37</Elem>
							<Elem>6.38</Elem>
							<Elem>6.39</Elem>
							<Elem>6.4</Elem>
							<Elem>6.41</Elem>
							<Elem>6.42</Elem>
							<Elem>6.43</Elem>
							<Elem>6.44</Elem>
							<Elem>6.45</Elem>
							<Elem>6.46</Elem>
							<Elem>6.47</Elem>
							<Elem>6.48</Elem>
							<Elem>6.49</Elem>
							<Elem>6.5</Elem>
							<Elem>6.51</Elem>
							<Elem>6.52</Elem>
							<Elem>6.53</Elem>
							<Elem>6.54</Elem>
							<Elem>6.55</Elem>
							<Elem>6.56</Elem>
							<Elem>6.57</Elem>
							<Elem>6.58</Elem>
							<Elem>6.59</Elem>
							<Elem>6.6</Elem>
							<Elem>6.61</Elem>
							<Elem>6.62</Elem>
							<Elem>6.63</Elem>
							<Elem>6.64</Elem>
							<Elem>6.65</Elem>
							<Elem>6.66</Elem>
							<Elem>6.67</Elem>
							<Elem>6.68</Elem>
							<Elem>6.69</Elem>
							<Elem>6.7</Elem>
							<Elem>6.71</Elem>
							<Elem>6.72</Elem>
							<Elem>6.73</Elem>
							<Elem>6.74</Elem>
							<Elem>6.75</Elem>
							<Elem>6.76</Elem>
							<Elem>6.77</Elem>
							<Elem>6.78</Elem>
							<Elem>6.79</Elem>
							<Elem>6.8</Elem>
							<Elem>6.81</Elem>
							<Elem>6.82</Elem>
							<Elem>6.83</Elem>
							<Elem>6.84</Elem>
							<Elem>6.85</Elem>
							<Elem>6.86</Elem>
							<Elem>6.87</Elem>
							<Elem>6.88</Elem>
							<Elem>6.89</Elem>
							<Elem>6.9</Elem>
							<Elem>6.91</Elem>
							<Elem>6.92</Elem>
							<Elem>6.93</Elem>
							<Elem>6.94</Elem>
							<Elem>6.95</Elem>
							<Elem>6.96</Elem>
							<Elem>6.97</Elem>
							<Elem>6.98</Elem>
							<Elem>6.99</Elem>
							<Elem>7</Elem>
							<Elem>7.01</Elem>
							<Elem>7.02</Elem>
							<Elem>7.03</Elem>
							<Elem>7.04</Elem>
							<Elem>7.05</Elem>
							<Elem>7.06</Elem>
							<Elem>7.07</Elem>
							<Elem>7.08</Elem>
							<Elem>7.09</Elem>
							<Elem>7.1</Elem>
							<Elem>7.11</Elem>
							<Elem>7.12</Elem>
							<Elem>7.13</Elem>
							<Elem>7.14</Elem>
							<Elem>7.15</Elem>
							<Elem>7.16</Elem>
							<Elem>7.17</Elem>
							<Elem>7.18</Elem>
							<Elem>7.19</Elem>
							<Elem>7.2</Elem>
							<Elem>7.21</Elem>
							<Elem>7.22</Elem>
							<Elem>7.23</Elem>
							<Elem>7.24</Elem>
							<Elem>7.25</Elem>
							<Elem>7.26</Elem>
							<Elem>7.27</Elem>
							<Elem>7.28</Elem>
							<Elem>7.29</Elem>
							<Elem>7.3</Elem>
							<Elem>7.31</Elem>
							<Elem>7.32</Elem>
							<Elem>7.33</Elem>
							<Elem>7.34</Elem>
							<Elem>7.35</Elem>
							<Elem>7.36</Elem>
							<Elem>7.37</Elem>
							<Elem>7.38</Elem>
							<Elem>7.39</Elem>
							<Elem>7.4</Elem>
							<Elem>7.41</Elem>
							<Elem>7.42</Elem>
							<Elem>7.43</Elem>
							<Elem>7.44</Elem>
							<Elem>7.45</Elem>
							<Elem>7.46</Elem>
							<Elem>7.47</Elem>
							<Elem>7.48</Elem>
							<Elem>7.49</Elem>
							<Elem>7.5</Elem>
							<Elem>7.51</Elem>
							<Elem>7.52</Elem>
							<Elem>7.53</Elem>
							<Elem>7.54</Elem>
							<Elem>7.55</Elem>
							<Elem>7.56</Elem>
							<Elem>7.57</Elem>
							<Elem>7.58</Elem>
							<Elem>7.59</Elem>
							<Elem>7.6</Elem>
							<Elem>7.61</Elem>
							<Elem>7.62</Elem>
							<Elem>7.63</Elem>
							<Elem>7.64</Elem>
							<Elem>7.65</Elem>
							<Elem>7.66</Elem>
							<Elem>7.67</Elem>
							<Elem>7.68</Elem>
							<Elem>7.69</Elem>
							<Elem>7.7</Elem>
							<Elem>7.71</Elem>
							<Elem>7.72</Elem>
							<Elem>7.73</Elem>
							<Elem>7.74</Elem>
							<Elem>7.75</Elem>
							<Elem>7.76</Elem>
							<Elem>7.77</Elem>
							<Elem>7.78</Elem>
							<Elem>7.79</Elem>
							<Elem>7.8</Elem>
							<Elem>7.81</Elem>
							<Elem>7.82</Elem>
							<Elem>7.83</Elem>
							<Elem>7.84</Elem>
							<Elem>7.85</Elem>
							<Elem>7.86</Elem>
							<Elem>7.87</Elem>
							<Elem>7.88</Elem>
							<Elem>7.89</Elem>
							<Elem>7.9</Elem>
							<Elem>7.91</Elem>
							<Elem>7.92</Elem>
							<Elem>7.93</Elem>
							<Elem>7.94</Elem>
							<Elem>7.95</Elem>
							<Elem>7.96</Elem>
							<Elem>7.97</Elem>
							<Elem>7.98</Elem>
							<Elem>7.99</Elem>
							<Elem>8</Elem>
							<Elem>8.01</Elem>
							<Elem>8.02</Elem>
							<Elem>8.03</Elem>
							<Elem>8.04</Elem>
							<Elem>8.05</Elem>
							<Elem>8.06</Elem>
							<Elem>8.07</Elem>
							<Elem>8.08</Elem>
							<Elem>8.09</Elem>
							<Elem>8.1</Elem>
							<Elem>8.11</Elem>
							<Elem>8.12</Elem>
							<Elem>8.13</Elem>
							<Elem>8.14</Elem>
							<Elem>8.15</Elem>
							<Elem>8.16</Elem>
							<Elem>8.17</Elem>
							<Elem>8.18</Elem>
							<Elem>8.19</Elem>
							<Elem>8.2</Elem>
							<Elem>8.21</Elem>
							<Elem>8.22</Elem>
							<Elem>8.23</Elem>
							<Elem>8.24</Elem>
							<Elem>8.25</Elem>
							<Elem>8.26</Elem>
							<Elem>8.27</Elem>
							<Elem>8.28</Elem>
							<Elem>8.29</Elem>
							<Elem>8.3</Elem>
							<Elem>8.31</Elem>
							<Elem>8.32</Elem>
							<Elem>8.33</Elem>
							<Elem>8.34</Elem>
							<Elem>8.35</Elem>
							<Elem>8.36</Elem>
							<Elem>8.37</Elem>
							<Elem>8.38</Elem>
							<Elem>8.39</Elem>
							<Elem>8.4</Elem>
							<Elem>8.41</Elem>
							<Elem>8.42</Elem>
							<Elem>8.43</Elem>
							<Elem>8.44</Elem>
							<Elem>8.45</Elem>
							<Elem>8.46</Elem>
							<Elem>8.47</Elem>
							<Elem>8.48</Elem>
							<Elem>8.49</Elem>
							<Elem>8.5</Elem>
							<Elem>8.51</Elem>
							<Elem>8.52</Elem>
							<Elem>8.53</Elem>
							<Elem>8.54</Elem>
							<Elem>8.55</Elem>
							<Elem>8.56</Elem>
							<Elem>8.57</Elem>
							<Elem>8.58</Elem>
							<Elem>8.59</Elem>
							<Elem>8.6</Elem>
							<Elem>8.61</Elem>
							<Elem>8.62</Elem>
							<Elem>8.63</Elem>
							<Elem>8.64</Elem>
							<Elem>8.65</Elem>
							<Elem>8.66</Elem>
							<Elem>8.67</Elem>
							<Elem>8.68</Elem>
							<Elem>8.69</Elem>
							<Elem>8.7</Elem>
							<Elem>8.71</Elem>
							<Elem>8.72</Elem>
							<Elem>8.73</Elem>
							<Elem>8.74</Elem>
							<Elem>8.75</Elem>
							<Elem>8.76</Elem>
							<Elem>8.77</Elem>
							<Elem>8.78</Elem>
							<Elem>8.79</Elem>
							<Elem>8.8</Elem>
							<Elem>8.81</Elem>
							<Elem>8.82</Elem>
							<Elem>8.83</Elem>
							<Elem>8.84</Elem>
							<Elem>8.85</Elem>
							<Elem>8.86</Elem>
							<Elem>8.87</Elem>
							<Elem>8.88</Elem>
							<Elem>8.89</Elem>
							<Elem>8.9</Elem>
							<Elem>8.91</Elem>
							<Elem>8.92</Elem>
							<Elem>8.93</Elem>
							<Elem>8.94</Elem>
							<Elem>8.95</Elem>
							<Elem>8.96</Elem>
							<Elem>8.97</Elem>
							<Elem>8.98</Elem>
							<Elem>8.99</Elem>
							<Elem>9</Elem>
							<Elem>9.01</Elem>
							<Elem>9.02</Elem>
							<Elem>9.03</Elem>
							<Elem>9.04</Elem>
							<Elem>9.05</Elem>
							<Elem>9.06</Elem>
							<Elem>9.07</Elem>
							<Elem>9.08</Elem>
							<Elem>9.09</Elem>
							<Elem>9.1</Elem>
							<Elem>9.11</Elem>
							<Elem>9.12</Elem>
							<Elem>9.13</Elem>
							<Elem>9.14</Elem>
							<Elem>9.15</Elem>
							<Elem>9.16</Elem>
							<Elem>9.17</Elem>
							<Elem>9.18</Elem>
							<Elem>9.19</Elem>
							<Elem>9.2</Elem>
							<Elem>9.21</Elem>
							<Elem>9.22</Elem>
							<Elem>9.23</Elem>
							<Elem>9.24</Elem>
							<Elem>9.25</Elem>
							<Elem>9.26</Elem>
							<Elem>9.27</Elem>
							<Elem>9.28</Elem>
							<Elem>9.29</Elem>
							<Elem>9.3</Elem>
							<Elem>9.31</Elem>
							<Elem>9.32</Elem>
							<Elem>9.33</Elem>
							<Elem>9.34</Elem>
							<Elem>9.35</Elem>
							<Elem>9.36</Elem>
							<Elem>9.37</Elem>
							<Elem>9.38</Elem>
							<Elem>9.39</Elem>
							<Elem>9.4</Elem>
							<Elem>9.41</Elem>
							<Elem>9.42</Elem>
							<Elem>9.43</Elem>
							<Elem>9.44</Elem>
							<Elem>9.45</Elem>
							<Elem>9.46</Elem>
							<Elem>9.47</Elem>
							<Elem>9.48</Elem>
							<Elem>9.49</Elem>
							<Elem>9.5</Elem>
							<Elem>9.51</Elem>
							<Elem>9.52</Elem>
							<Elem>9.53</Elem>
							<Elem>9.54</Elem>
							<Elem>9.55</Elem>
							<Elem>9.56</Elem>
							<Elem>9.57</Elem>
							<Elem>9.58</Elem>
							<Elem>9.59</Elem>
							<Elem>9.6</Elem>
							<Elem>9.61</Elem>
							<Elem>9.62</Elem>
							<Elem>9.63</Elem>
							<Elem>9.64</Elem>
							<Elem>9.65</Elem>
							<Elem>9.66</Elem>
							<Elem>9.67</Elem>
							<Elem>9.68</Elem>
							<Elem>9.69</Elem>
							<Elem>9.7</Elem>
							<Elem>9.71</Elem>
							<Elem>9.72</Elem>
							<Elem>9.73</Elem>
							<Elem>9.74</Elem>
							<Elem>9.75</Elem>
							<Elem>9.76</Elem>
							<Elem>9.77</Elem>
							<Elem>9.78</Elem>
							<Elem>9.79</Elem>
							<Elem>9.8</Elem>
							<Elem>9.81</Elem>
							<Elem>9.82</Elem>
							<Elem>9.83</Elem>
							<Elem>9.84</Elem>
							<Elem>9.85</Elem>
							<Elem>9.86</Elem>
							<Elem>9.87</Elem>
							<Elem>9.88</Elem>
							<Elem>9.89</Elem>
							<Elem>9.9</Elem>
							<Elem>9.91</Elem>
							<Elem>9.92</Elem>
							<Elem>9.93</Elem>
							<Elem>9.94</Elem>
							<Elem>9.95</Elem>
							<Elem>9.96</Elem>
							<Elem>9.97</Elem>
							<Elem>9.98</Elem>
							<Elem>9.99</Elem>
							<Elem>10</Elem>
							<Elem>10.01</Elem>
							<Elem>10.02</Elem>
							<Elem>10.03</Elem>
							<Elem>10.04</Elem>
							<Elem>10.05</Elem>
							<Elem>10.06</Elem>
							<Elem>10.07</Elem>
							<Elem>10.08</Elem>
							<Elem>10.09</Elem>
							<Elem>10.1</Elem>
							<Elem>10.11</Elem>
							<Elem>10.12</Elem>
							<Elem>10.13</Elem>
							<Elem>10.14</Elem>
							<Elem>10.15</Elem>
							<Elem>10.16</Elem>
							<Elem>10.17</Elem>
							<Elem>10.18</Elem>
							<Elem>10.19</Elem>
							<Elem>10.2</Elem>
							<Elem>10.21</Elem>
							<Elem>10.22</Elem>
							<Elem>10.23</Elem>
							<Elem>10.24</Elem>
							<Elem>10.25</Elem>
							<Elem>10.26</Elem>
							<Elem>10.27</Elem>
							<Elem>10.28</Elem>
							<Elem>10.29</Elem>
							<Elem>10.3</Elem>
							<Elem>10.31</Elem>
							<Elem>10.32</Elem>
							<Elem>10.33</Elem>
							<Elem>10.34</Elem>
							<Elem>10.35</Elem>
							<Elem>10.36</Elem>
							<Elem>10.37</Elem>
							<Elem>10.38</Elem>
							<Elem>10.39</Elem>
							<Elem>10.4</Elem>
							<Elem>10.41</Elem>
							<Elem>10.42</Elem>
							<Elem>10.43</Elem>
							<Elem>10.44</Elem>
							<Elem>10.45</Elem>
							<Elem>10.46</Elem>
							<Elem>10.47</Elem>
							<Elem>10.48</Elem>
							<Elem>10.49</Elem>
							<Elem>10.5</Elem>
							<Elem>10.51</Elem>
							<Elem>10.52</Elem>
							<Elem>10.53</Elem>
							<Elem>10.54</Elem>
							<Elem>10.55</Elem>
							<Elem>10.56</Elem>
							<Elem>10.57</Elem>
							<Elem>10.58</Elem>
							<Elem>10.59</Elem>
							<Elem>10.6</Elem>
							<Elem>10.61</Elem>
							<Elem>10.62</Elem>
							<Elem>10.63</Elem>
							<Elem>10.64</Elem>
							<Elem>10.65</Elem>
							<Elem>10.66</Elem>
							<Elem>10.67</Elem>
							<Elem>10.68</Elem>
							<Elem>10.69</Elem>
							<Elem>10.7</Elem>
							<Elem>10.71</Elem>
							<Elem>10.72</Elem>
							<Elem>10.73</Elem>
							<Elem>10.74</Elem>
							<Elem>10.75</Elem>
							<Elem>10.76</Elem>
							<Elem>10.77</Elem>
							<Elem>10.78</Elem>
							<Elem>10.79</Elem>
							<Elem>10.8</Elem>
							<Elem>10.81</Elem>
							<Elem>10.82</Elem>
							<Elem>10.83</Elem>
							<Elem>10.84</Elem>
							<Elem>10.85</Elem>
							<Elem>10.86</Elem>
							<Elem>10.87</Elem>
							<Elem>10.88</Elem>
							<Elem>10.89</Elem>
							<Elem>10.9</Elem>
							<Elem>10.91</Elem>
							<Elem>10.92</Elem>
							<Elem>10.93</Elem>
							<Elem>10.94</Elem>
							<Elem>10.95</Elem>
							<Elem>10.96</Elem>
							<Elem>10.97</Elem>
							<Elem>10.98</Elem>
							<Elem>10.99</Elem>
							<Elem>11</Elem>
							<Elem>11.01</Elem>
							<Elem>11.02</Elem>
							<Elem>11.03</Elem>
							<Elem>11.04</Elem>
							<Elem>11.05</Elem>
							<Elem>11.06</Elem>
							<Elem>11.07</Elem>
							<Elem>11.08</Elem>
							<Elem>11.09</Elem>
							<Elem>11.1</Elem>
							<Elem>11.11</Elem>
							<Elem>11.12</Elem>
							<Elem>11.13</Elem>
							<Elem>11.14</Elem>
							<Elem>11.15</Elem>
							<Elem>11.16</Elem>
							<Elem>11.17</Elem>
							<Elem>11.18</Elem>
							<Elem>11.19</Elem>
							<Elem>11.2</Elem>
							<Elem>11.21</Elem>
							<Elem>11.22</Elem>
							<Elem>11.23</Elem>
							<Elem>11.24</Elem>
							<Elem>11.25</Elem>
							<Elem>11.26</Elem>
							<Elem>11.27</Elem>
							<Elem>11.28</Elem>
							<Elem>11.29</Elem>
							<Elem>11.3</Elem>
							<Elem>11.31</Elem>
							<Elem>11.32</Elem>
							<Elem>11.33</Elem>
							<Elem>11.34</Elem>
							<Elem>11.35</Elem>
							<Elem>11.36</Elem>
							<Elem>11.37</Elem>
							<Elem>11.38</Elem>
							<Elem>11.39</Elem>
							<Elem>11.4</Elem>
							<Elem>11.41</Elem>
							<Elem>11.42</Elem>
							<Elem>11.43</Elem>
							<Elem>11.44</Elem>
							<Elem>11.45</Elem>
							<Elem>11.46</Elem>
							<Elem>11.47</Elem>
							<Elem>11.48</Elem>
							<Elem>11.49</Elem>
							<Elem>11.5</Elem>
							<Elem>11.51</Elem>
							<Elem>11.52</Elem>
							<Elem>11.53</Elem>
							<Elem>11.54</Elem>
							<Elem>11.55</Elem>
							<Elem>11.56</Elem>
							<Elem>11.57</Elem>
							<Elem>11.58</Elem>
							<Elem>11.59</Elem>
							<Elem>11.6</Elem>
							<Elem>11.61</Elem>
							<Elem>11.62</Elem>
							<Elem>11.63</Elem>
							<Elem>11.64</Elem>
							<Elem>11.65</Elem>
							<Elem>11.66</Elem>
							<Elem>11.67</Elem>
							<Elem>11.68</Elem>
							<Elem>11.69</Elem>
							<Elem>11.7</Elem>
							<Elem>11.71</Elem>
							<Elem>11.72</Elem>
							<Elem>11.73</Elem>
							<Elem>11.74</Elem>
							<Elem>11.75</Elem>
							<Elem>11.76</Elem>
							<Elem>11.77</Elem>
							<Elem>11.78</Elem>
							<Elem>11.79</Elem>
							<Elem>11.8</Elem>
							<Elem>11.81</Elem>
							<Elem>11.82</Elem>
							<Elem>11.83</Elem>
							<Elem>11.84</Elem>
							<Elem>11.85</Elem>
							<Elem>11.86</Elem>
							<Elem>11.87</Elem>
							<Elem>11.88</Elem>
							<Elem>11.89</Elem>
							<Elem>11.9</Elem>
							<Elem>11.91</Elem>
							<Elem>11.92</Elem>
							<Elem>11.93</Elem>
							<Elem>11.94</Elem>
							<Elem>11.95</Elem>
							<Elem>11.96</Elem>
							<Elem>11.97</Elem>
							<Elem>11.98</Elem>
							<Elem>11.99</Elem>
							<Elem>12</Elem>
							<Elem>12.01</Elem>
							<Elem>12.02</Elem>
							<Elem>12.03</Elem>
							<Elem>12.04</Elem>
							<Elem>12.05</Elem>
							<Elem>12.06</Elem>
							<Elem>12.07</Elem>
							<Elem>12.08</Elem>
							<Elem>12.09</Elem>
							<Elem>12.1</Elem>
							<Elem>12.11</Elem>
							<Elem>12.12</Elem>
							<Elem>12.13</Elem>
							<Elem>12.14</Elem>
							<Elem>12.15</Elem>
							<Elem>12.16</Elem>
							<Elem>12.17</Elem>
							<Elem>12.18</Elem>
							<Elem>12.19</Elem>
							<Elem>12.2</Elem>
							<Elem>12.21</Elem>
							<Elem>12.22</Elem>
							<Elem>12.23</Elem>
							<Elem>12.24</Elem>
							<Elem>12.25</Elem>
							<Elem>12.26</Elem>
							<Elem>12.27</Elem>
							<Elem>12.28</Elem>
							<Elem>12.29</Elem>
							<Elem>12.3</Elem>
							<Elem>12.31</Elem>
							<Elem>12.32</Elem>
							<Elem>12.33</Elem>
							<Elem>12.34</Elem>
							<Elem>12.35</Elem>
							<Elem>12.36</Elem>
							<Elem>12.37</Elem>
							<Elem>12.38</Elem>
							<Elem>12.39</Elem>
							<Elem>12.4</Elem>
							<Elem>12.41</Elem>
							<Elem>12.42</Elem>
							<Elem>12.43</Elem>
							<Elem>12.44</Elem>
							<Elem>12.45</Elem>
							<Elem>12.46</Elem>
							<Elem>12.47</Elem>
							<Elem>12.48</Elem>
							<Elem>12.49</Elem>
							<Elem>12.5</Elem>
							<Elem>12.51</Elem>
							<Elem>12.52</Elem>
							<Elem>12.53</Elem>
							<Elem>12.54</Elem>
							<Elem>12.55</Elem>
							<Elem>12.56</Elem>
							<Elem>12.57</Elem>
							<Elem>12.58</Elem>
							<Elem>12.59</Elem>
							<Elem>12.6</Elem>
							<Elem>12.61</Elem>
							<Elem>12.62</Elem>
							<Elem>12.63</Elem>
							<Elem>12.64</Elem>
							<Elem>12.65</Elem>
							<Elem>12.66</Elem>
							<Elem>12.67</Elem>
							<Elem>12.68</Elem>
							<Elem>12.69</Elem>
							<Elem>12.7</Elem>
							<Elem>12.71</Elem>
							<Elem>12.72</Elem>
							<Elem>12.73</Elem>
							<Elem>12.74</Elem>
							<Elem>12.75</Elem>
							<Elem>12.76</Elem>
							<Elem>12.77</Elem>
							<Elem>12.78</Elem>
							<Elem>12.79</Elem>
							<Elem>12.8</Elem>
							<Elem>12.81</Elem>
							<Elem>12.82</Elem>
							<Elem>12.83</Elem>
							<Elem>12.84</Elem>
							<Elem>12.85</Elem>
							<Elem>12.86</Elem>
							<Elem>12.87</Elem>
							<Elem>12.88</Elem>
							<Elem>12.89</Elem>
							<Elem>12.9</Elem>
							<Elem>12.91</Elem>
							<Elem>12.92</Elem>
							<Elem>12.93</Elem>
							<Elem>12.94</Elem>
							<Elem>12.95</Elem>
							<Elem>12.96</Elem>
							<Elem>12.97</Elem>
							<Elem>12.98</Elem>
							<Elem>12.99</Elem>
							<Elem>13</Elem>
							<Elem>13.01</Elem>
							<Elem>13.02</Elem>
							<Elem>13.03</Elem>
							<Elem>13.04</Elem>
							<Elem>13.05</Elem>
							<Elem>13.06</Elem>
							<Elem>13.07</Elem>
							<Elem>13.08</Elem>
							<Elem>13.09</Elem>
							<Elem>13.1</Elem>
							<Elem>13.11</Elem>
							<Elem>13.12</Elem>
							<Elem>13.13</Elem>
							<Elem>13.14</Elem>
							<Elem>13.15</Elem>
							<Elem>13.16</Elem>
							<Elem>13.17</Elem>
							<Elem>13.18</Elem>
							<Elem>13.19</Elem>
							<Elem>13.2</Elem>
							<Elem>13.21</Elem>
							<Elem>13.22</Elem>
							<Elem>13.23</Elem>
							<Elem>13.24</Elem>
							<Elem>13.25</Elem>
							<Elem>13.26</Elem>
							<Elem>13.27</Elem>
							<Elem>13.28</Elem>
							<Elem>13.29</Elem>
							<Elem>13.3</Elem>
							<Elem>13.31</Elem>
							<Elem>13.32</Elem>
							<Elem>13.33</Elem>
							<Elem>13.34</Elem>
							<Elem>13.35</Elem>
							<Elem>13.36</Elem>
							<Elem>13.37</Elem>
							<Elem>13.38</Elem>
							<Elem>13.39</Elem>
							<Elem>13.4</Elem>
							<Elem>13.41</Elem>
							<Elem>13.42</Elem>
							<Elem>13.43</Elem>
							<Elem>13.44</Elem>
							<Elem>13.45</Elem>
							<Elem>13.46</Elem>
							<Elem>13.47</Elem>
							<Elem>13.48</Elem>
							<Elem>13.49</Elem>
							<Elem>13.5</Elem>
							<Elem>13.51</Elem>
							<Elem>13.52</Elem>
							<Elem>13.53</Elem>
							<Elem>13.54</Elem>
							<Elem>13.55</Elem>
							<Elem>13.56</Elem>
							<Elem>13.57</Elem>
							<Elem>13.58</Elem>
							<Elem>13.59</Elem>
							<Elem>13.6</Elem>
							<Elem>13.61</Elem>
							<Elem>13.62</Elem>
							<Elem>13.63</Elem>
							<Elem>13.64</Elem>
							<Elem>13.65</Elem>
							<Elem>13.66</Elem>
							<Elem>13.67</Elem>
							<Elem>13.68</Elem>
							<Elem>13.69</Elem>
							<Elem>13.7</Elem>
							<Elem>13.71</Elem>
							<Elem>13.72</Elem>
							<Elem>13.73</Elem>
							<Elem>13.74</Elem>
							<Elem>13.75</Elem>
							<Elem>13.76</Elem>
							<Elem>13.77</Elem>
							<Elem>13.78</Elem>
							<Elem>13.79</Elem>
							<Elem>13.8</Elem>
							<Elem>13.81</Elem>
							<Elem>13.82</Elem>
							<Elem>13.83</Elem>
							<Elem>13.84</Elem>
							<Elem>13.85</Elem>
							<Elem>13.86</Elem>
							<Elem>13.87</Elem>
							<Elem>13.88</Elem>
							<Elem>13.89</Elem>
							<Elem>13.9</Elem>
							<Elem>13.91</Elem>
							<Elem>13.92</Elem>
							<Elem>13.93</Elem>
							<Elem>13.94</Elem>
							<Elem>13.95</Elem>
							<Elem>13.96</Elem>
							<Elem>13.97</Elem>
							<Elem>13.98</Elem>
							<Elem>13.99</Elem>
							<Elem>14</Elem>
							<Elem>14.01</Elem>
							<Elem>14.02</Elem>
							<Elem>14.03</Elem>
							<Elem>14.04</Elem>
							<Elem>14.05</Elem>
							<Elem>14.06</Elem>
							<Elem>14.07</Elem>
							<Elem>14.08</Elem>
							<Elem>14.09</Elem>
							<Elem>14.1</Elem>
							<Elem>14.11</Elem>
							<Elem>14.12</Elem>
							<Elem>14.13</Elem>
							<Elem>14.14</Elem>
							<Elem>14.15</Elem>
							<Elem>14.16</Elem>
							<Elem>14.17</Elem>
							<Elem>14.18</Elem>
							<Elem>14.19</Elem>
							<Elem>14.2</Elem>
							<Elem>14.21</Elem>
							<Elem>14.22</Elem>
							<Elem>14.23</Elem>
							<Elem>14.24</Elem>
							<Elem>14.25</Elem>
							<Elem>14.26</Elem>
							<Elem>14.27</Elem>
							<Elem>14.28</Elem>
							<Elem>14.29</Elem>
							<Elem>14.3</Elem>
							<Elem>14.31</Elem>
							<Elem>14.32</Elem>
							<Elem>14.33</Elem>
							<Elem>14.34</Elem>
							<Elem>14.35</Elem>
							<Elem>14.36</Elem>
							<Elem>14.37</Elem>
							<Elem>14.38</Elem>
							<Elem>14.39</Elem>
							<Elem>14.4</Elem>
							<Elem>14.41</Elem>
							<Elem>14.42</Elem>
							<Elem>14.43</Elem>
							<Elem>14.44</Elem>
							<Elem>14.45</Elem>
							<Elem>14.46</Elem>
							<Elem>14.47</Elem>
							<Elem>14.48</Elem>
							<Elem>14.49</Elem>
							<Elem>14.5</Elem>
							<Elem>14.51</Elem>
							<Elem>14.52</Elem>
							<Elem>14.53</Elem>
							<Elem>14.54</Elem>
							<Elem>14.55</Elem>
							<Elem>14.56</Elem>
							<Elem>14.57</Elem>
							<Elem>14.58</Elem>
							<Elem>14.59</Elem>
							<Elem>14.6</Elem>
							<Elem>14.61</Elem>
							<Elem>14.62</Elem>
							<Elem>14.63</Elem>
							<Elem>14.64</Elem>
							<Elem>14.65</Elem>
							<Elem>14.66</Elem>
							<Elem>14.67</Elem>
							<Elem>14.68</Elem>
							<Elem>14.69</Elem>
							<Elem>14.7</Elem>
							<Elem>14.71</Elem>
							<Elem>14.72</Elem>
							<Elem>14.73</Elem>
							<Elem>14.74</Elem>
							<Elem>14.75</Elem>
							<Elem>14.76</Elem>
							<Elem>14.77</Elem>
							<Elem>14.78</Elem>
							<Elem>14.79</Elem>
							<Elem>14.8</Elem>
							<Elem>14.81</Elem>
							<Elem>14.82</Elem>
							<Elem>14.83</Elem>
							<Elem>14.84</Elem>
							<Elem>14.85</Elem>
							<Elem>14.86</Elem>
							<Elem>14.87</Elem>
							<Elem>14.88</Elem>
							<Elem>14.89</Elem>
							<Elem>14.9</Elem>
							<Elem>14.91</Elem>
							<Elem>14.92</Elem>
							<Elem>14.93</Elem>
							<Elem>14.94</Elem>
							<Elem>14.95</Elem>
							<Elem>14.96</Elem>
							<Elem>14.97</Elem>
							<Elem>14.98</Elem>
							<Elem>14.99</Elem>
							<Elem>15</Elem>
							<Elem>15.01</Elem>
							<Elem>15.02</Elem>
							<Elem>15.03</Elem>
							<Elem>15.04</Elem>
							<Elem>15.05</Elem>
							<Elem>15.06</Elem>
							<Elem>15.07</Elem>
							<Elem>15.08</Elem>
							<Elem>15.09</Elem>
							<Elem>15.1</Elem>
							<Elem>15.11</Elem>
							<Elem>15.12</Elem>
							<Elem>15.13</Elem>
							<Elem>15.14</Elem>
							<Elem>15.15</Elem>
							<Elem>15.16</Elem>
							<Elem>15.17</Elem>
							<Elem>15.18</Elem>
							<Elem>15.19</Elem>
							<Elem>15.2</Elem>
							<Elem>15.21</Elem>
							<Elem>15.22</Elem>
							<Elem>15.23</Elem>
							<Elem>15.24</Elem>
							<Elem>15.25</Elem>
							<Elem>15.26</Elem>
							<Elem>15.27</Elem>
							<Elem>15.28</Elem>
							<Elem>15.29</Elem>
							<Elem>15.3</Elem>
							<Elem>15.31</Elem>
							<Elem>15.32</Elem>
							<Elem>15.33</Elem>
							<Elem>15.34</Elem>
							<Elem>15.35</Elem>
							<Elem>15.36</Elem>
							<Elem>15.37</Elem>
							<Elem>15.38</Elem>
							<Elem>15.39</Elem>
							<Elem>15.4</Elem>
							<Elem>15.41</Elem>
							<Elem>15.42</Elem>
							<Elem>15.43</Elem>
							<Elem>15.44</Elem>
							<Elem>15.45</Elem>
							<Elem>15.46</Elem>
							<Elem>15.47</Elem>
							<Elem>15.48</Elem>
							<Elem>15.49</Elem>
							<Elem>15.5</Elem>
							<Elem>15.51</Elem>
							<Elem>15.52</Elem>
							<Elem>15.53</Elem>
							<Elem>15.54</Elem>
							<Elem>15.55</Elem>
							<Elem>15.56</Elem>
							<Elem>15.57</Elem>
							<Elem>15.58</Elem>
							<Elem>15.59</Elem>
							<Elem>15.6</Elem>
							<Elem>15.61</Elem>
							<Elem>15.62</Elem>
							<Elem>15.63</Elem>
							<Elem>15.64</Elem>
							<Elem>15.65</Elem>
							<Elem>15.66</Elem>
							<Elem>15.67</Elem>
							<Elem>15.68</Elem>
							<Elem>15.69</Elem>
							<Elem>15.7</Elem>
							<Elem>15.71</Elem>
							<Elem>15.72</Elem>
							<Elem>15.73</Elem>
							<Elem>15.74</Elem>
							<Elem>15.75</Elem>
							<Elem>15.76</Elem>
							<Elem>15.77</Elem>
							<Elem>15.78</Elem>
							<Elem>15.79</Elem>
							<Elem>15.8</Elem>
							<Elem>15.81</Elem>
							<Elem>15.82</Elem>
							<Elem>15.83</Elem>
							<Elem>15.84</Elem>
							<Elem>15.85</Elem>
							<Elem>15.86</Elem>
							<Elem>15.87</Elem>
							<Elem>15.88</Elem>
							<Elem>15.89</Elem>
							<Elem>15.9</Elem>
							<Elem>15.91</Elem>
							<Elem>15.92</Elem>
							<Elem>15.93</Elem>
							<Elem>15.94</Elem>
							<Elem>15.95</Elem>
							<Elem>15.96</Elem>
							<Elem>15.97</Elem>
							<Elem>15.98</Elem>
							<Elem>15.99</Elem>
							<Elem>16</Elem>
							<Elem>16.01</Elem>
							<Elem>16.02</Elem>
							<Elem>16.03</Elem>
							<Elem>16.04</Elem>
							<Elem>16.05</Elem>
							<Elem>16.06</Elem>
							<Elem>16.07</Elem>
							<Elem>16.08</Elem>
							<Elem>16.09</Elem>
							<Elem>16.1</Elem>
							<Elem>16.11</Elem>
							<Elem>16.12</Elem>
							<Elem>16.13</Elem>
							<Elem>16.14</Elem>
							<Elem>16.15</Elem>
							<Elem>16.16</Elem>
							<Elem>16.17</Elem>
							<Elem>16.18</Elem>
							<Elem>16.19</Elem>
							<Elem>16.2</Elem>
							<Elem>16.21</Elem>
							<Elem>16.22</Elem>
							<Elem>16.23</Elem>
							<Elem>16.24</Elem>
							<Elem>16.25</Elem>
							<Elem>16.26</Elem>
							<Elem>16.27</Elem>
							<Elem>16.28</Elem>
							<Elem>16.29</Elem>
							<Elem>16.3</Elem>
							<Elem>16.31</Elem>
							<Elem>16.32</Elem>
							<Elem>16.33</Elem>
							<Elem>16.34</Elem>
							<Elem>16.35</Elem>
							<Elem>16.36</Elem>
							<Elem>16.37</Elem>
							<Elem>16.38</Elem>
							<Elem>16.39</Elem>
							<Elem>16.4</Elem>
							<Elem>16.41</Elem>
							<Elem>16.42</Elem>
							<Elem>16.43</Elem>
							<Elem>16.44</Elem>
							<Elem>16.45</Elem>
							<Elem>16.46</Elem>
							<Elem>16.47</Elem>
							<Elem>16.48</Elem>
							<Elem>16.49</Elem>
							<Elem>16.5</Elem>
							<Elem>16.51</Elem>
							<Elem>16.52</Elem>
							<Elem>16.53</Elem>
							<Elem>16.54</Elem>
							<Elem>16.55</Elem>
							<Elem>16.56</Elem>
							<Elem>16.57</Elem>
							<Elem>16.58</Elem>
							<Elem>16.59</Elem>
							<Elem>16.6</Elem>
							<Elem>16.61</Elem>
							<Elem>16.62</Elem>
							<Elem>16.63</Elem>
							<Elem>16.64</Elem>
							<Elem>16.65</Elem>
							<Elem>16.66</Elem>
							<Elem>16.67</Elem>
							<Elem>16.68</Elem>
							<Elem>16.69</Elem>
							<Elem>16.7</Elem>
							<Elem>16.71</Elem>
							<Elem>16.72</Elem>
							<Elem>16.73</Elem>
						</DoubleArray>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ProfileTest/Conditional Test.nivstest sha256=ce510e73dae1161c1af21f90259569b67cb1b3443358810453bd84c331efb20f bytes=14906 -->
## FILE: tests/testutilities/legacy_files/ProfileTest/Conditional Test.nivstest

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ProfileTest/Conditional Test.nivstest`
- sha256: `ce510e73dae1161c1af21f90259569b67cb1b3443358810453bd84c331efb20f`
- bytes: 14906

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
		<Section Name="Generator 1" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray>
						<Elem>Target Section/Controller/User Channels/User Channel 1</Elem>
					</StringArray>
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Root Group 1" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
				<Properties />
				<Errors />
				<Section Name="Reset Pass Fail" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
					<Properties>
						<Property Name="Step Type">
							<String>Set Variable</String>
						</Property>
						<Property Name="Channel">
							<String>Target Section/Controller/User Channels/Pass Fail Channels/Gen 1 Pass Fail</String>
						</Property>
						<Property Name="Value1.Type">
							<String>Constant</String>
						</Property>
						<Property Name="Value1.Constant">
							<Double>-1</Double>
						</Property>
						<Property Name="Function">
							<String>None</String>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Static Conditional Test" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
					<Properties />
					<Errors />
					<Section Name="LV 1 = 0" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>0</Double>
							</Property>
							<Property Name="Function">
								<String>None</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="LV 1 = LV 1 + 1" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Channel</String>
							</Property>
							<Property Name="Function">
								<String>+</String>
							</Property>
							<Property Name="Value1.Channel">
								<String>LV 1</String>
							</Property>
							<Property Name="Value2.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value2.Constant">
								<Double>1</Double>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Dwell 1" TypeGUID="376cd3a2-af99-4855-a664-842d3500812d">
						<Properties>
							<Property Name="Step Type">
								<String>Dwell</String>
							</Property>
							<Property Name="Time">
								<Double>0.01</Double>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Wait until LV 1 = 200" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
						<Properties>
							<Property Name="Step Type">
								<String>Conditional</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Comparison">
								<String>Less</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>200</Double>
							</Property>
							<Property Name="Goto Step">
								<DependentNode Path="Generator 1/Root Group 1/Static Conditional Test/LV 1 = LV 1 + 1" />
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Check if LV 1 = 200" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
						<Properties>
							<Property Name="Step Type">
								<String>Conditional</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Comparison">
								<String>Not Equal</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>200</Double>
							</Property>
							<Property Name="Goto Step">
								<DependentNode Path="Generator 1/Root Group 1/Fail" />
							</Property>
						</Properties>
						<Errors />
					</Section>
				</Section>
				<Section Name="Dynamic Conditional Test" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
					<Properties />
					<Errors />
					<Section Name="LV 1 = 0" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>0</Double>
							</Property>
							<Property Name="Function">
								<String>None</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="LV 2 = 200" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 2</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>200</Double>
							</Property>
							<Property Name="Function">
								<String>None</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="LV 1 = LV 1 + 1" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Channel</String>
							</Property>
							<Property Name="Function">
								<String>+</String>
							</Property>
							<Property Name="Value1.Channel">
								<String>LV 1</String>
							</Property>
							<Property Name="Value2.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value2.Constant">
								<Double>1</Double>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Dwell 1" TypeGUID="376cd3a2-af99-4855-a664-842d3500812d">
						<Properties>
							<Property Name="Step Type">
								<String>Dwell</String>
							</Property>
							<Property Name="Time">
								<Double>0.01</Double>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Wait until LV 1 = LV 2" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
						<Properties>
							<Property Name="Step Type">
								<String>Conditional</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Comparison">
								<String>Less</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Channel</String>
							</Property>
							<Property Name="Goto Step">
								<DependentNode Path="Generator 1/Root Group 1/Dynamic Conditional Test/LV 1 = LV 1 + 1" />
							</Property>
							<Property Name="Value1.Channel">
								<String>LV 2</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="LV3 = LV1 - LV 2" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 3</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Channel</String>
							</Property>
							<Property Name="Function">
								<String>--</String>
							</Property>
							<Property Name="Value1.Channel">
								<String>LV 1</String>
							</Property>
							<Property Name="Value2.Type">
								<String>Channel</String>
							</Property>
							<Property Name="Value2.Channel">
								<String>LV 2</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Check if LV 3 &gt; 0.1" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
						<Properties>
							<Property Name="Step Type">
								<String>Conditional</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 3</String>
							</Property>
							<Property Name="Comparison">
								<String>Greater</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Goto Step">
								<DependentNode Path="Generator 1/Root Group 1/Fail" />
							</Property>
							<Property Name="Value1.Constant">
								<Double>0.1</Double>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Check if LV 3 &lt; -0.1" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
						<Properties>
							<Property Name="Step Type">
								<String>Conditional</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 3</String>
							</Property>
							<Property Name="Comparison">
								<String>Less</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Goto Step">
								<DependentNode Path="Generator 1/Root Group 1/Fail" />
							</Property>
							<Property Name="Value1.Constant">
								<Double>-0.1</Double>
							</Property>
						</Properties>
						<Errors />
					</Section>
				</Section>
				<Section Name="Pass" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
					<Properties />
					<Errors />
					<Section Name="Set Pass" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Pass Fail Channels/Gen 1 Pass Fail</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>1</Double>
							</Property>
							<Property Name="Function">
								<String>None</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Stop Profile" TypeGUID="9f447d91-f09d-47c8-809b-a8a49ad8f6bd">
						<Properties>
							<Property Name="Step Type">
								<String>End</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
				</Section>
				<Section Name="Fail" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
					<Properties />
					<Errors />
					<Section Name="Set Fail" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Pass Fail Channels/Gen 1 Pass Fail</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>0</Double>
							</Property>
							<Property Name="Function">
								<String>None</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Stop Profile" TypeGUID="9f447d91-f09d-47c8-809b-a8a49ad8f6bd">
						<Properties>
							<Property Name="Step Type">
								<String>End</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
				</Section>
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ProfileTest/Dwell Test.nivstest sha256=12aa86823d3457cc251dee8aa21c137ceec2dc22bbec2c16212afa21c60ca32b bytes=8837 -->
## FILE: tests/testutilities/legacy_files/ProfileTest/Dwell Test.nivstest

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ProfileTest/Dwell Test.nivstest`
- sha256: `12aa86823d3457cc251dee8aa21c137ceec2dc22bbec2c16212afa21c60ca32b`
- bytes: 8837

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
		<Section Name="Generator 1" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Root Group 1" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
				<Properties />
				<Errors />
				<Section Name="Reset Pass Fail" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
					<Properties>
						<Property Name="Step Type">
							<String>Set Variable</String>
						</Property>
						<Property Name="Channel">
							<String>Target Section/Controller/User Channels/Pass Fail Channels/Gen 1 Pass Fail</String>
						</Property>
						<Property Name="Value1.Type">
							<String>Constant</String>
						</Property>
						<Property Name="Value1.Constant">
							<Double>-1</Double>
						</Property>
						<Property Name="Function">
							<String>None</String>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Run Rate Test" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
					<Properties />
					<Errors />
					<Section Name="Tick" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Channel</String>
							</Property>
							<Property Name="Function">
								<String>None</String>
							</Property>
							<Property Name="Value1.Channel">
								<String>System Time</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Dwell" TypeGUID="376cd3a2-af99-4855-a664-842d3500812d">
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
					<Section Name="Tock" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Channel</String>
							</Property>
							<Property Name="Function">
								<String>--</String>
							</Property>
							<Property Name="Value1.Channel">
								<String>System Time</String>
							</Property>
							<Property Name="Value2.Type">
								<String>Channel</String>
							</Property>
							<Property Name="Value2.Channel">
								<String>LV 1</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Check Dwell Min Duration" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
						<Properties>
							<Property Name="Step Type">
								<String>Conditional</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Comparison">
								<String>Less</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>9.5</Double>
							</Property>
							<Property Name="Goto Step">
								<DependentNode Path="Generator 1/Root Group 1/Fail" />
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Check Dwell Max Duration" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
						<Properties>
							<Property Name="Step Type">
								<String>Conditional</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Comparison">
								<String>Greater</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>10.5</Double>
							</Property>
							<Property Name="Goto Step">
								<DependentNode Path="Generator 1/Root Group 1/Fail" />
							</Property>
						</Properties>
						<Errors />
					</Section>
				</Section>
				<Section Name="Pass" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
					<Properties />
					<Errors />
					<Section Name="Set Pass" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Pass Fail Channels/Gen 1 Pass Fail</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>1</Double>
							</Property>
							<Property Name="Function">
								<String>None</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Stop Profile" TypeGUID="9f447d91-f09d-47c8-809b-a8a49ad8f6bd">
						<Properties>
							<Property Name="Step Type">
								<String>End</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
				</Section>
				<Section Name="Fail" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
					<Properties />
					<Errors />
					<Section Name="Set Fail" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Pass Fail Channels/Gen 1 Pass Fail</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>0</Double>
							</Property>
							<Property Name="Function">
								<String>None</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Stop Profile" TypeGUID="9f447d91-f09d-47c8-809b-a8a49ad8f6bd">
						<Properties>
							<Property Name="Step Type">
								<String>End</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
				</Section>
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ProfileTest/Invalid Channel.nivstest sha256=54911b1fb1a9118bc5e775f04ab8b114774cf4926da944c3ab59ac18308bef08 bytes=3105 -->
## FILE: tests/testutilities/legacy_files/ProfileTest/Invalid Channel.nivstest

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ProfileTest/Invalid Channel.nivstest`
- sha256: `54911b1fb1a9118bc5e775f04ab8b114774cf4926da944c3ab59ac18308bef08`
- bytes: 3105

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
		<Section Name="Generator 1" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Set Variable" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
				<Properties>
					<Property Name="Step Type">
						<String>Set Variable</String>
					</Property>
					<Property Name="Channel">
						<String>This Channel Does not Exist</String>
					</Property>
					<Property Name="Value1.Type">
						<String>Constant</String>
					</Property>
					<Property Name="Value1.Constant">
						<Double>0</Double>
					</Property>
					<Property Name="Function">
						<String>None</String>
					</Property>
				</Properties>
				<Errors>
					<Error Key="K_ERR_INV_CHAN (Channel)" IsError="true" Code="-307662">
						<Message>Property: Channel</Message>
					</Error>
				</Errors>
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ProfileTest/Profile Test.nivsproj sha256=78c9dea4578b2b19ef690cda31c0f03dff91ff59d727b3371db8b4ffe5a46086 bytes=17489 -->
## FILE: tests/testutilities/legacy_files/ProfileTest/Profile Test.nivsproj

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ProfileTest/Profile Test.nivsproj`
- sha256: `78c9dea4578b2b19ef690cda31c0f03dff91ff59d727b3371db8b4ffe5a46086`
- bytes: 17489

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2012" Minor="0" Fix="0" Build="1" />
	<Content>Definition</Content>
	<Root Name="Profile Test" TypeGUID="d9313aae-3554-45e5-93f3-86454275d4f2">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>Profile Test</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.0</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3351165825.58459</Double>
			</Property>
		</Properties>
		<Errors />
		<Section Name="System Definition File" TypeGUID="b9227a5b-2770-4a62-8621-ac414d4124fb">
			<Description />
			<Properties />
			<Errors />
			<Section Name="Profile Test.nivssdf" TypeGUID="3a41ca74-36ec-4aff-9219-9d05c8f91208">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="Profile Test.nivssdf">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5>c52070ad28fbaa2c43cbc38a8dba9a72</MD5>
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
						<Data>AAAGcwkAgAAAAAAIAA5AMP////8ETmFtZQAAEkAw/////whGdW5jdGlvbgAAYQDxAAAAAAAAAAETVG9vbGJhciBCdXR0b25zLmN0bABFQBYAAwROb25lF1N0aW11bHVzIFByb2ZpbGUgRWRpdG9yC0RhdGEgVmlld2VyAAAOVG9vbGJhciBCdXR0b24AAVMA8QAAAAAAAAABH2VudW1fVXNlciBBZG1pbiBQZXJtaXNzaW9ucy5jdGwBK0AWAA0HRGVmYXVsdA5BZG1pbmlzdHJhdGlvbhdDaGFubmVsIFNjYWxpbmcgVXRpbGl0eRFBZGQgRGlzcGxheSBJdGVtcxNDaGFuZ2UgVXNlciBQcm9maWxlI0VkaXQgU3RpbXVsdXMgUHJvZmlsZSBFZGl0b3IgSGVhZGVyGkVkaXQgRGlzcGxheSBJdGVtIFNldHRpbmdzG01vZGVsIFBhcmFtZXRlciBDYWxpYnJhdGlvbhJSdW50aW1lIEFsYXJtIEVkaXQPRWRpdCBUb29scyBNZW51FkVkaXQgRW5naW5lIENvbXBvbmVudHMaQ29uZmlndXJlIFZpc2libGUgQ2hhbm5lbHMNRmF1bHQgTWFuYWdlcgAAClBlcm1pc3Npb24AABpAMv////8QQ3VzdG9tIFRvb2wgUGF0aAAAaQDxxyxnxAAAAAIRTklWU19TaGFyZWQubHZsaWINUGF0aCB0eXBlLmN0bABBQBYAAwhBYnNvbHV0ZQhSZWxhdGl2ZQxUb0FwcERhdGFEaXIAABVDdXN0b20gVG9vbCBQYXRoIFR5cGUAYwDxAAAAAAAAAAIaTklWU1Byb2pfRmlsZW1hbmFnZXIubHZsaWIZVG9vbHMgTWVudSBJdGVtcyBUeXBlLmN0bAAmQFAABgAAAAEAAgADAAQABQ9Ub29scyBNZW51IEl0ZW0AHkBAAAH/////AAYQVG9vbHMgTWVudSBJdGVtcwAAAQAHAAAADwAAAA1BbGFybSBNb25pdG9yAAAAFHN1Yl9BbGFybSBNb25pdG9yLnZpAAAAAVBUSDAAAAAEAAAAAAAAAAAAF01vZGVsIFBhcmFtZXRlciBNYW5hZ2VyAAAAGk1vZGVsIFBhcmFtZXRlciBNYW5hZ2VyLnZpAAAAAVBUSDAAAAAEAAAAAAAAAAAAAS0AAAABLQAAAAFQVEgwAAAABAAAAAAAAAAAABdTdGltdWx1cyBQcm9maWxlIEVkaXRvcgAAABpTdGltdWx1cyBQcm9maWxlIEVkaXRvci52aQABAAFQVEgwAAAABAAAAAAAAAAAACBTdGltdWx1cyBQcm9maWxlIFNlcXVlbmNlIEVkaXRvcgAAABZUZXN0IEVkaXRvciAoQmF0Y2gpLnZpAAAAAVBUSDAAAAAEAAAAAAAAAAAAAS0AAAABLQAAAAFQVEgwAAAABAAAAAAAAAAAAB1DaGFubmVsIFNjYWxpbmcgJiBDYWxpYnJhdGlvbgAAABJzdWJfQ2FsaWJyYXRpb24udmkAAAABUFRIMAAAAAQAAAAAAAAAAAAVQ2hhbm5lbCBGYXVsdCBNYW5hZ2VyAAAAFHNjcl9GYXVsdCBNYW5hZ2VyLnZpAAAAAVBUSDAAAAAEAAAAAAAAAAAAAS0AAAABLQAAAAFQVEgwAAAABAAAAAAAAAAAAA5NYWNybyBSZWNvcmRlcgAAADBXb3Jrc3BhY2UgTWFjcm9cUmVjb3JkZXJQbGF5ZXJcTWFjcm8gUmVjb3JkZXIudmkAAAABUFRIMAAAAAQAAAAAAAAAAAAMTWFjcm8gUGxheWVyAAAALldvcmtzcGFjZSBNYWNyb1xSZWNvcmRlclBsYXllclxNYWNybyBQbGF5ZXIudmkAAAABUFRIMAAAAAQAAAAAAAAAAAABLQAAAAEtAAAAAVBUSDAAAAAEAAAAAAAAAAAAE0NoYW5uZWwgRGF0YSBWaWV3ZXIAAAAWQ2hhbm5lbCBEYXRhIFZpZXdlci52aQAAAAFQVEgwAAAABAAAAAAAAAAAAA5Db25zb2xlIFZpZXdlcgAAABJWaWV3IFJUIENvbnNvbGUudmkAAAABUFRIMAAAAAQAAAAAAAAAAAAQVERNUyBGaWxlIFZpZXdlcgAAABdzY3JfVERNUyBEYXRhIFZpZXdlci52aQACAAFQVEgwAAAABAAAAAAAAAAAAAA=</Data>
					</Variant>
				</Property>
			</Properties>
			<Errors />
			<Section Name="Screens" TypeGUID="cdfadfe0-c84a-4268-a677-4f2f3525465e">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="Profile Test.nivsscreen">
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
			<Section Name="Channel Data Viewer" TypeGUID="cc686646-9933-410d-a553-6308e6e06897">
				<Description />
				<Properties>
					<Property Name="Function">
						<String>Channel Data Viewer.vi</String>
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
						<String>None</String>
					</Property>
					<Property Name="Sync Timeout">
						<I32>0</I32>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Profiles" TypeGUID="c3bd79ec-3336-4b06-868e-3217c640edd5">
			<Description />
			<Properties />
			<Errors />
			<Section Name="Step Tests" TypeGUID="c23d9309-697b-4ae0-827b-ceafb29f7389">
				<Description />
				<Properties />
				<Errors />
				<Section Name="Ramp Test.nivstest" TypeGUID="abf90cfe-5857-440d-9231-18a95fb3d451">
					<Description />
					<Properties>
						<Property Name="Path">
							<DependentFile Type="Relative" Path="Ramp Test.nivstest">
								<Version />
								<RTDestination />
								<SupportedTarget />
								<MD5>bc96671866dfa63a346bd605cf03d566</MD5>
							</DependentFile>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Conditional Test.nivstest" TypeGUID="abf90cfe-5857-440d-9231-18a95fb3d451">
					<Description />
					<Properties>
						<Property Name="Path">
							<DependentFile Type="Relative" Path="Conditional Test.nivstest">
								<Version />
								<RTDestination />
								<SupportedTarget />
								<MD5>8ca0cde2df5fe4847f12c3fe34bb873c</MD5>
							</DependentFile>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Dwell Test.nivstest" TypeGUID="abf90cfe-5857-440d-9231-18a95fb3d451">
					<Description />
					<Properties>
						<Property Name="Path">
							<DependentFile Type="Relative" Path="Dwell Test.nivstest">
								<Version />
								<RTDestination />
								<SupportedTarget />
								<MD5>ef7c4306b4198bf1e211b21065d3fb51</MD5>
							</DependentFile>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Too Many Gens.nivstest" TypeGUID="abf90cfe-5857-440d-9231-18a95fb3d451">
					<Description />
					<Properties>
						<Property Name="Path">
							<DependentFile Type="Relative" Path="Too Many Gens.nivstest">
								<Version />
								<RTDestination />
								<SupportedTarget />
								<MD5>8ca0cde2df5fe4847f12c3fe34bb873c</MD5>
							</DependentFile>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Too Many Steps.nivstest" TypeGUID="abf90cfe-5857-440d-9231-18a95fb3d451">
					<Description />
					<Properties>
						<Property Name="Path">
							<DependentFile Type="Relative" Path="Too Many Steps.nivstest">
								<Version />
								<RTDestination />
								<SupportedTarget />
								<MD5>e72727e1a3f6c81783f7023e8398c48b</MD5>
							</DependentFile>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Aux Buffer Overflow.nivstest" TypeGUID="abf90cfe-5857-440d-9231-18a95fb3d451">
					<Description />
					<Properties>
						<Property Name="Path">
							<DependentFile Type="Relative" Path="Aux Buffer Overflow.nivstest">
								<Version />
								<RTDestination />
								<SupportedTarget />
								<MD5>8ca0cde2df5fe4847f12c3fe34bb873c</MD5>
							</DependentFile>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Invalid Channel.nivstest" TypeGUID="abf90cfe-5857-440d-9231-18a95fb3d451">
					<Description />
					<Properties>
						<Property Name="Path">
							<DependentFile Type="Relative" Path="Invalid Channel.nivstest">
								<Version />
								<RTDestination />
								<SupportedTarget />
								<MD5>8ca0cde2df5fe4847f12c3fe34bb873c</MD5>
							</DependentFile>
						</Property>
					</Properties>
					<Errors />
				</Section>
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
			<Section Name="Profile Test.nivssdf [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\ProfileTest\Profile Test.nivssdf]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\ProfileTest\Profile Test.nivssdf</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Profile Test.nivsscreen [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\ProfileTest\Profile Test.nivsscreen]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\ProfileTest\Profile Test.nivsscreen</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Ramp Test.nivstest [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\ProfileTest\Ramp Test.nivstest]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\ProfileTest\Ramp Test.nivstest</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Conditional Test.nivstest [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\ProfileTest\Conditional Test.nivstest]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\ProfileTest\Conditional Test.nivstest</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Dwell Test.nivstest [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\ProfileTest\Dwell Test.nivstest]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\ProfileTest\Dwell Test.nivstest</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Too Many Gens.nivstest [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\ProfileTest\Too Many Gens.nivstest]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\ProfileTest\Too Many Gens.nivstest</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Too Many Steps.nivstest [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\ProfileTest\Too Many Steps.nivstest]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\ProfileTest\Too Many Steps.nivstest</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Aux Buffer Overflow.nivstest [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\ProfileTest\Aux Buffer Overflow.nivstest]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\ProfileTest\Aux Buffer Overflow.nivstest</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Invalid Channel.nivstest [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\ProfileTest\Invalid Channel.nivstest]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\ProfileTest\Invalid Channel.nivstest</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ProfileTest/Profile Test.nivsscreen sha256=71bf487a9438860831d894dad7af2d8b2b6a2083e7360b973d3d5ae04ea52339 bytes=4113 -->
## FILE: tests/testutilities/legacy_files/ProfileTest/Profile Test.nivsscreen

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ProfileTest/Profile Test.nivsscreen`
- sha256: `71bf487a9438860831d894dad7af2d8b2b6a2083e7360b973d3d5ae04ea52339`
- bytes: 4113

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2010" Minor="0" Fix="0" Build="0" />
	<Content>Definition</Content>
	<Root Name="WorkspaceScreen" TypeGUID="2e39a440-e372-11de-8a39-0800200c9a66">
		<Properties>
			<Property Name="EscapeEnabled">
				<Boolean>true</Boolean>
			</Property>
			<Property Name="ShowPropPageOnDrop">
				<Boolean>true</Boolean>
			</Property>
			<Property Name="Screen Data">
				<Variant>
					<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
					<Data>AAAIkAkAgAAAAABYABRAMP////8LVGVtcGxhdGUgVkkAEUADAApQb3NpdGlvbiBYAAARQAMAClBvc2l0aW9uIFkAABBAMP////8GQ3VzdG9tAAAUQCEOU2hvdyBUaXRsZSBCYXIAAAlAAwACSUQAABJAIQ1BbHdheXMgT24gVG9wABJAIQxBbGxvdyBSZXNpemUAABRAIQ5BbGxvdyBNaW5pbWl6ZQAAEEAhC0FsbG93IENsb3NlABRAIQ5TaXplIHRvIFNjcmVlbgAAD0ADAAlTY3JlZW4uSUQAGUAWAAIGTm9ybWFsA05ldwAABVN0YXRlAA5AMP////8FVGl0bGUACUACAANbMF0ACUACAANbMV0ACUACAANbMl0ACUACAANbM10AHEBQAAQADgAPABAAEQ1XaW5kb3cgQm91bmRzABFACAALQ2hhbm5lbCBSZWYADkAw/////wRVbml0AAAUQCEORGVmYXVsdCBVbml0cz8AABJAIQxGbGFzaCBMaW1pdD8AAA1ABwAHQ29sb3IgMQANQAcAB0NvbG9yIDIADUAHAAdDb2xvciAzAA1ABwAHQ29sb3IgNAAPQAcACUJjayBDb2xvcgARQAcACkZvcmUgQ29sb3IAAA1ACgAHTGltaXQgMQANQAoAB0xpbWl0IDIADUAKAAdMaW1pdCAzAA1ACgAHTGltaXQgNAATQAMADExpbWl0IE1vZGUgMQAAE0ADAAxMaW1pdCBNb2RlIDIAABNAAwAMTGltaXQgTW9kZSAzAAATQAMADExpbWl0IE1vZGUgNAAAFUADAA9TY2FsZSBQcmVjaXNpb24AD0AKAAlTY2FsZSBNaW4AD0AKAAlTY2FsZSBNYXgADUADAAZGb3JtYXQAAA9AAwAJUHJlY2lzaW9uABVAAwAPQmFja2dyb3VuZCBUeXBlABFAAwALVmFyaWFibGUgSUQAEEBAAAH/////ACsDSURzABRAMP////8LVmFyaWFibGUgSUQAEkBAAAH/////AC0FVW5pdHMAFEBAAAH/////AC0GTGFiZWxzAAATQAoADFNjYWxlIEZhY3RvcgAAE0AKAAxTY2FsZSBPZmZzZXQAABFABwALVmFyaWFibGUgSUQAGkBAAAH/////ADIMWVNjYWxlIEluZGV4AAANQAUABkZvcm1hdAAAD0AFAAlQcmVjaXNpb24ACUAFAANGaXQADkAw/////wVMYWJlbAAWQCERVXNlIERlZmF1bHQgTGFiZWwAEkAhDUxhYmVsIFZpc2libGUACUAKAANNaW4ACUAKAANNYXgASwDxAAAAAAAAAAEgY2x1c3Rlcl9HcmFwaCBTY2FsZSBTZXR0aW5ncy5jdGwAIkBQAAgANAA1ADYANwA4ADkAOgA7BlhTY2FsZQAAFEBAAAH/////ADwHWVNjYWxlcwAPQAUACUJhciBTdHlsZQANQAIAB0ZpbGwgVG8AE0AHAAxGaWxsL1B0Q29sb3IAABFABQAKTGluZSBTdHlsZQAAEUAFAApMaW5lIFdpZHRoAAALQAcABUNvbG9yAA1ABQAGSW50ZXJwAAARQAUAC1BvaW50IFN0eWxlAEgA8QAAAAAAAAABH2NsdXN0ZXJfR3JhcGggUGxvdCBTZXR0aW5ncy5jdGwAIEBQAAgAPgA/AEAAQQBCAEMARABFBFBsb3QAABJAQAAB/////wBGBVBsb3RzABNACgANVXBkYXRlIFBlcmlvZAAVQAoADkhpc3RvcnkgTGVuZ3RoAAAUQHAACAAAAAIAAAZNeS5SZWYAABBAIQtJcyBDb250cm9sPwAWQDD/////DENoYW5uZWwgUGF0aAAAGkBAAAH/////AEwNQ2hhbm5lbCBQYXRocwAQQFMLQ3VzdG9tIERhdGEAqwDxxieWWAAAAAEgY2x1c3Rlcl9TY3JlZW4gSXRlbSBTZXR0aW5ncy5jdGwAgkBQADYAAAABAAIAAwAEAAUABgAHAAgACQAKAAsADAANABIAEwAUABUAFgAXABgAGQAaABsAHAAdAB4AHwAgACEAIgAjACQAJQAmACcAKAApACoALAAuAC8AMAAxADMAPAA9AEcASABJAEoASwBNAE4LU2NyZWVuIEl0ZW0AEkBAAAH/////AE8FSXRlbXMADkAw/////wROYW1lAAAUQDD/////C0Rlc2NyaXB0aW9uAVMA8QAAAAAAAAABH2VudW1fVXNlciBBZG1pbiBQZXJtaXNzaW9ucy5jdGwBK0AWAA0HRGVmYXVsdA5BZG1pbmlzdHJhdGlvbhdDaGFubmVsIFNjYWxpbmcgVXRpbGl0eRFBZGQgRGlzcGxheSBJdGVtcxNDaGFuZ2UgVXNlciBQcm9maWxlI0VkaXQgU3RpbXVsdXMgUHJvZmlsZSBFZGl0b3IgSGVhZGVyGkVkaXQgRGlzcGxheSBJdGVtIFNldHRpbmdzG01vZGVsIFBhcmFtZXRlciBDYWxpYnJhdGlvbhJSdW50aW1lIEFsYXJtIEVkaXQPRWRpdCBUb29scyBNZW51FkVkaXQgRW5naW5lIENvbXBvbmVudHMaQ29uZmlndXJlIFZpc2libGUgQ2hhbm5lbHMNRmF1bHQgTWFuYWdlcgAAClBlcm1pc3Npb24AAAxAIQdMb2FkZWQ/ABRAIQ9BbHdheXMgVmlzaWJsZT8AVwDxAAAAAAAAAAEkY2x1c3Rlcl9FbnRpcmUgU2NyZWVuIERlZmluaXRpb24uY3RsACpAUAAKAFAAUQBSAAUAAQACAAYAUwBUAFULU2NyZWVuLkRhdGEAJkBAAAH/////AFYZU2NyZWVuIEl0ZW0gQ2x1c3RlciBBcnJheQABAFcAAAABAAAAAAAAAAZTY3JlZW4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA</Data>
				</Variant>
			</Property>
			<Property Name="Screen Order">
				<I32Array>
					<Elem>0</Elem>
				</I32Array>
			</Property>
			<Property Name="Workspace Loc and Size Left">
				<U16>50</U16>
			</Property>
			<Property Name="Workspace Loc and Size Top">
				<U16>50</U16>
			</Property>
			<Property Name="Workspace Loc and Size Right">
				<U16>850</U16>
			</Property>
			<Property Name="Workspace Loc and Size Bottom">
				<U16>650</U16>
			</Property>
		</Properties>
		<Errors />
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ProfileTest/Profile Test.nivssdf sha256=ab17986d79ca6e145f455bcb343308538b56612fbadf0d257097ac4d52d9e5e8 bytes=284317 -->
## FILE: tests/testutilities/legacy_files/ProfileTest/Profile Test.nivssdf

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ProfileTest/Profile Test.nivssdf`
- sha256: `ab17986d79ca6e145f455bcb343308538b56612fbadf0d257097ac4d52d9e5e8`
- bytes: 284317

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2010" Minor="0" Fix="0" Build="4" />
	<Content>Definition</Content>
	<Root Name="Profile Test" TypeGUID="03D3BA22-1485-13A6-56BD17DA950CCD00">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>Profile Test</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.8</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3351165824.350215</Double>
			</Property>
		</Properties>
		<Errors />
		<TargetSections Name="Target Section" TypeGUID="eb379619-68d7-4d81-be90-c0bc511cdc10">
			<Description />
			<Properties />
			<Errors />
			<Target Name="Controller" TypeGUID="775504BB-1485-13A6-56755DBF2C326980">
				<Description />
				<Properties>
					<Property Name="IP Address">
						<String />
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
					<Property Name="Deployment Group">
						<I32>0</I32>
					</Property>
					<Property Name="Engine Rate">
						<Double>100</Double>
					</Property>
					<Property Name="OS">
						<String>Windows</String>
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
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Index" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>The compiled index of the current procedure step</Description>
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
						<Description>An internal register used by procedures to maintain the stack location when a procedure is preempted by a higher priorty procedure</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 2" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>An internal register used by procedures to maintain the stack location when a procedure is preempted by a higher priorty procedure</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 3" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>An internal register used by procedures to maintain the stack location when a procedure is preempted by a higher priorty procedure</Description>
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
						<Description>An internal register used by procedures to maintain the stack location when a procedure is preempted by a higher priorty procedure</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 5" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>An internal register used by procedures to maintain the stack location when a procedure is preempted by a higher priorty procedure</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 6" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>An internal register used by procedures to maintain the stack location when a procedure is preempted by a higher priorty procedure</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>The ID of the alarm that has tripped</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>The ID of the alarm that has tripped</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="1">
						<Description>The ID of the alarm that has tripped</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>The value of the channel that tripped the alarm</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>The value of the channel that tripped the alarm</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
						<Description>The value of the channel that tripped the alarm</Description>
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
						<Description>Specifies whether execution tracing is currently active on the RT Target.</Description>
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
					<Channel Name="System Reserved 39" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 40" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
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
					<Channel Name="System Reserved 51" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 52" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 53" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 54" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 55" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
						<Description>Deprecated</Description>
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
				<Section Name="Hardware" TypeGUID="775504AB-1485-13A6-560018C1F4E3EEE1">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Chassis" TypeGUID="03D3BACD-1485-13A6-56E99D97B7543BAF">
						<Description />
						<Properties />
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
						<Section Name="XNET" TypeGUID="6b693e6d-67b1-40b8-8108-4a4cc3147721">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
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
					<Section Name="Pass Fail Channels" TypeGUID="7f9b2ef4-f3fc-4448-975a7018fe511e0d">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="Gen 1 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 2 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 3 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 4 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 5 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 6 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 7 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 8 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 9 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 10 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 11 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 12 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 13 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 14 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 15 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 16 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 17 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 18 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 19 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 20 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 21 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 22 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 23 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 24 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 25 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 26 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 27 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 28 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 29 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 30 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 31 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 32 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 33 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 34 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 35 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 36 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 37 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 38 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 39 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 40 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 41 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 42 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 43 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 44 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 45 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 46 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 47 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 48 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 49 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 50 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 51 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 52 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 53 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 54 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 55 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 56 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 57 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 58 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 59 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 60 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 61 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 62 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 63 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 64 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 65 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 66 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 67 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 68 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 69 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 70 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 71 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 72 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 73 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 74 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 75 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 76 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 77 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 78 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 79 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 80 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 81 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 82 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 83 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 84 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 85 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 86 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 87 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 88 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 89 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 90 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 91 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 92 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 93 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 94 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 95 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 96 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 97 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 98 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 99 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="Gen 100 Pass Fail" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="Boolean" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
					</Section>
					<Section Name="Local Variables" TypeGUID="7f9b2ef4-f3fc-4448-975a7018fe511e0d">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="LV 1" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 2" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 3" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 4" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 5" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 6" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 7" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 8" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 9" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 10" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 11" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 12" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 13" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 14" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 15" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 16" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 17" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 18" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 19" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 20" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 21" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 22" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 23" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 24" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 25" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 26" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 27" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 28" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 29" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 30" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 31" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 32" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 33" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 34" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 35" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 36" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 37" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 38" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 39" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 40" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 41" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 42" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 43" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 44" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 45" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 46" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 47" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 48" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 49" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 50" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 51" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 52" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 53" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 54" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 55" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 56" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 57" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 58" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 59" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 60" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 61" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 62" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 63" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 64" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 65" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 66" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 67" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 68" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 69" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 70" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 71" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 72" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 73" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 74" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 75" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 76" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 77" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 78" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 79" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 80" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 81" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 82" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 83" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 84" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 85" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 86" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 87" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 88" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 89" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 90" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 91" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 92" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 93" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 94" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 95" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 96" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 97" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 98" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 99" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="LV 100" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
					</Section>
					<Section Name="Test" TypeGUID="7f9b2ef4-f3fc-4448-975a7018fe511e0d">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="TEST_ID" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>12000</Elem>
							</DefaultValue>
						</Channel>
					</Section>
					<Channel Name="User Channel 100" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
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
					<Channel Name="User Channel 5" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 6" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 7" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 8" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 9" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 10" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 11" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 12" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 13" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 14" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 15" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 16" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 17" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 18" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 19" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 20" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 21" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 22" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 23" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 24" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 25" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 26" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 27" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 28" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 29" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 30" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 31" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 32" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 33" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 34" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 35" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 36" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 37" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 38" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 39" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 40" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 41" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 42" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 43" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 44" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 45" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 46" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 47" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 48" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 49" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 50" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 51" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 52" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 53" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 54" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 55" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 56" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 57" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 58" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 59" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 60" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 61" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 62" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 63" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 64" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 65" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 66" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 67" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 68" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 69" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 70" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 71" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 72" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 73" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 74" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 75" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 76" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 77" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 78" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 79" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 80" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 81" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 82" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 83" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 84" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 85" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 86" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 87" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 88" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 89" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 90" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 91" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 92" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 93" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 94" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 95" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 96" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 97" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 98" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="User Channel 99" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
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
							<I32>1000</I32>
						</Property>
						<Property Name="Analysis Buffer Size">
							<I32>10000</I32>
						</Property>
						<Property Name="Analysis Result Size">
							<I32>5000</I32>
						</Property>
					</Properties>
					<Errors />
					<Section Name="GEN001" TypeGUID="03D3B80E-1485-13A6-56528B60DC00DC89">
						<Description />
						<Properties />
						<Errors />
						<Channel Name="GEN001 State" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN001 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
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
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN002 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
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
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN003 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
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
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN004 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
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
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN005 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
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
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN006 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
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
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN007 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
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
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN008 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
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
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN009 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
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
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Rate" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec/loop" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Current Step" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Current Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Hold Flag" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Hold Release" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Total # Steps" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Group" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Client" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Total # Blocks" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Current Block" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Cycle" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Total Cycles" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Time in Function" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Total Time" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Timer" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="sec" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Output" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Ramp Setpoint" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Ramp Rate Eu/sec" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="EUs/sec" BitFields="3">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
						<Channel Name="GEN010 Spare" TypeGUID="03D3B83D-1485-13A6-567FA3A221DFFB5E" RowDim="1" ColDim="1" Units="" BitFields="1">
							<Description />
							<Properties />
							<Errors />
							<DefaultValue>
								<Elem>0</Elem>
							</DefaultValue>
						</Channel>
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
				<Section Name="XNET Databases" TypeGUID="def5630b-577f-4ae9-9682-5f8ee445ee21">
					<Description />
					<Properties>
						<Property Name="CD Status">
							<U32>2</U32>
						</Property>
					</Properties>
					<Errors />
				</Section>
			</Target>
		</TargetSections>
		<Section Name="Aliases" TypeGUID="e11f4519-09e6-4fb0-99df-2967c4313d67">
			<Description />
			<Properties />
			<Errors />
			<Alias Name="User Channel 100" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 100" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 10" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 10" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 11" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 11" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 12" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 12" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 13" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 13" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 14" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 14" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 15" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 15" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 16" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 16" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 17" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 17" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 18" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 18" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 19" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 19" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 20" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 20" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 21" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 21" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 22" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 22" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 23" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 23" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 24" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 24" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 25" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 25" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 26" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 26" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 27" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 27" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 28" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 28" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 29" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 29" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 3" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 30" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 30" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 31" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 31" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 32" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 32" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 33" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 33" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 34" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 34" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 35" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 35" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 36" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 36" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 37" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 37" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 38" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 38" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 39" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 39" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 4" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 4" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 40" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 40" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 41" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 41" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 42" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 42" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 43" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 43" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 44" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 44" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 45" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 45" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 46" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 46" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 47" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 47" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 48" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 48" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 49" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 49" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 5" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 5" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 50" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 50" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 51" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 51" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 52" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 52" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 53" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 53" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 54" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 54" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 55" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 55" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 56" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 56" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 57" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 57" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 58" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 58" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 59" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 59" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 6" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 6" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 60" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 60" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 61" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 61" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 62" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 62" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 63" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 63" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 64" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 64" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 65" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 65" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 66" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 66" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 67" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 67" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 68" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 68" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 69" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 69" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 7" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 7" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 70" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 70" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 71" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 71" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 72" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 72" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 73" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 73" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 74" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 74" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 75" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 75" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 76" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 76" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 77" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 77" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 78" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 78" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 79" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 79" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 8" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 8" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 80" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 80" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 81" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 81" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 82" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 82" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 83" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 83" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 84" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 84" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 85" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 85" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 86" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 86" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 87" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 87" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 88" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 88" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 89" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 89" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 9" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 9" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 90" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 90" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 91" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 91" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 92" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 92" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 93" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 93" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 94" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 94" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 95" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 95" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 96" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 96" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 97" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 97" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 98" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 98" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="User Channel 99" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/User Channel 99" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 1 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 1 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 10 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 10 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 100 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 100 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 11 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 11 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 12 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 12 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 13 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 13 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 14 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 14 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 15 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 15 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 16 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 16 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 17 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 17 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 18 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 18 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 19 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 19 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 2 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 2 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 20 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 20 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 21 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 21 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 22 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 22 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 23 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 23 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 24 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 24 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 25 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 25 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 26 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 26 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 27 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 27 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 28 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 28 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 29 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 29 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 3 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 3 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 30 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 30 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 31 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 31 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 32 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 32 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 33 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 33 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 34 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 34 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 35 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 35 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 36 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 36 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 37 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 37 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 38 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 38 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 39 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 39 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 4 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 4 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 40 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 40 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 41 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 41 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 42 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 42 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 43 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 43 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 44 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 44 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 45 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 45 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 46 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 46 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 47 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 47 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 48 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 48 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 49 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 49 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 5 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 5 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 50 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 50 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 51 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 51 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 52 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 52 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 53 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 53 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 54 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 54 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 55 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 55 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 56 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 56 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 57 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 57 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 58 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 58 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 59 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 59 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 6 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 6 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 60 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 60 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 61 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 61 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 62 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 62 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 63 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 63 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 64 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 64 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 65 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 65 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 66 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 66 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 67 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 67 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 68 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 68 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 69 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 69 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 7 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 7 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 70 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 70 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 71 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 71 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 72 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 72 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 73 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 73 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 74 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 74 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 75 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 75 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 76 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 76 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 77 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 77 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 78 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 78 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 79 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 79 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 8 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 8 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 80 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 80 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 81 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 81 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 82 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 82 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 83 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 83 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 84 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 84 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 85 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 85 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 86 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 86 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 87 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 87 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 88 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 88 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 89 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 89 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 9 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 9 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 90 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 90 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 91 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 91 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 92 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 92 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 93 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 93 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 94 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 94 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 95 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 95 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 96 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 96 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 97 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 97 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 98 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 98 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Gen 99 Pass Fail" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Pass Fail Channels/Gen 99 Pass Fail" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 10" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 10" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 100" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 100" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 11" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 11" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 12" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 12" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 13" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 13" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 14" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 14" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 15" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 15" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 16" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 16" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 17" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 17" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 18" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 18" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 19" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 19" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 20" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 20" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 21" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 21" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 22" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 22" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 23" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 23" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 24" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 24" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 25" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 25" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 26" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 26" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 27" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 27" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 28" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 28" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 29" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 29" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 3" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 30" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 30" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 31" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 31" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 32" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 32" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 33" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 33" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 34" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 34" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 35" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 35" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 36" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 36" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 37" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 37" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 38" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 38" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 39" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 39" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 4" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 4" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 40" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 40" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 41" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 41" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 42" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 42" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 43" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 43" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 44" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 44" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 45" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 45" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 46" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 46" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 47" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 47" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 48" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 48" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 49" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 49" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 5" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 5" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 50" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 50" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 51" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 51" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 52" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 52" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 53" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 53" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 54" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 54" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 55" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 55" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 56" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 56" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 57" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 57" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 58" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 58" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 59" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 59" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 6" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 6" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 60" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 60" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 61" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 61" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 62" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 62" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 63" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 63" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 64" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 64" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 65" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 65" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 66" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 66" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 67" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 67" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 68" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 68" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 69" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 69" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 7" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 7" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 70" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 70" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 71" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 71" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 72" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 72" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 73" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 73" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 74" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 74" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 75" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 75" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 76" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 76" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 77" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 77" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 78" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 78" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 79" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 79" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 8" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 8" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 80" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 80" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 81" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 81" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 82" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 82" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 83" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 83" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 84" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 84" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 85" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 85" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 86" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 86" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 87" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 87" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 88" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 88" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 89" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 89" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 9" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 9" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 90" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 90" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 91" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 91" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 92" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 92" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 93" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 93" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 94" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 94" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 95" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 95" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 96" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 96" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 97" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 97" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 98" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 98" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="LV 99" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Local Variables/LV 99" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="System Time" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/System Channels/System Time" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="TEST_ID" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/Test/TEST_ID" />
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

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ProfileTest/Ramp Test.nivstest sha256=adcd6405f923a2d10a79bd93564bd3ad72960000fe0e2f2f06d77a816c3e961e bytes=14769 -->
## FILE: tests/testutilities/legacy_files/ProfileTest/Ramp Test.nivstest

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ProfileTest/Ramp Test.nivstest`
- sha256: `adcd6405f923a2d10a79bd93564bd3ad72960000fe0e2f2f06d77a816c3e961e`
- bytes: 14769

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
		<Section Name="Ramp Test [User Channel 1]" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray>
						<Elem>Target Section/Controller/User Channels/User Channel 1</Elem>
					</StringArray>
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Root Group 1" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
				<Properties />
				<Errors />
				<Section Name="Reset Pass Fail" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
					<Properties>
						<Property Name="Step Type">
							<String>Set Variable</String>
						</Property>
						<Property Name="Channel">
							<String>Target Section/Controller/User Channels/Pass Fail Channels/Gen 1 Pass Fail</String>
						</Property>
						<Property Name="Value1.Type">
							<String>Constant</String>
						</Property>
						<Property Name="Value1.Constant">
							<Double>-1</Double>
						</Property>
						<Property Name="Function">
							<String>None</String>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Run Rate Test" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
					<Description>Ramp up to 100 at a rate of 10 EUs/sec. Check that we reach 100 and that the duration is about 10 seconds.</Description>
					<Properties />
					<Errors />
					<Section Name="Tick" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Channel</String>
							</Property>
							<Property Name="Function">
								<String>None</String>
							</Property>
							<Property Name="Value1.Channel">
								<String>System Time</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Ramp to One Hundred" TypeGUID="d3a0c118-0577-4aae-9d76-9fdcf7c75eb6">
						<Properties>
							<Property Name="Step Type">
								<String>Ramp</String>
							</Property>
							<Property Name="End Point">
								<Double>100</Double>
							</Property>
							<Property Name="Mode">
								<String>Rate</String>
							</Property>
							<Property Name="Rate">
								<Double>10</Double>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Tock" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Channel</String>
							</Property>
							<Property Name="Function">
								<String>--</String>
							</Property>
							<Property Name="Value1.Channel">
								<String>System Time</String>
							</Property>
							<Property Name="Value2.Type">
								<String>Channel</String>
							</Property>
							<Property Name="Value2.Channel">
								<String>LV 1</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Check One Hundred 1" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
						<Properties>
							<Property Name="Step Type">
								<String>Conditional</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/User Channel 1</String>
							</Property>
							<Property Name="Comparison">
								<String>Not Equal</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>100</Double>
							</Property>
							<Property Name="Goto Step">
								<DependentNode Path="Ramp Test [User Channel 1]/Root Group 1/Fail" />
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Check Ramp Min Duration" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
						<Properties>
							<Property Name="Step Type">
								<String>Conditional</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Comparison">
								<String>Less</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>9.5</Double>
							</Property>
							<Property Name="Goto Step">
								<DependentNode Path="Ramp Test [User Channel 1]/Root Group 1/Fail" />
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Check Ramp Max Duration 1" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
						<Properties>
							<Property Name="Step Type">
								<String>Conditional</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Comparison">
								<String>Greater</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>10.5</Double>
							</Property>
							<Property Name="Goto Step">
								<DependentNode Path="Ramp Test [User Channel 1]/Root Group 1/Fail" />
							</Property>
						</Properties>
						<Errors />
					</Section>
				</Section>
				<Section Name="Run Duration Test" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
					<Properties />
					<Errors />
					<Section Name="Tick" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Channel</String>
							</Property>
							<Property Name="Function">
								<String>None</String>
							</Property>
							<Property Name="Value1.Channel">
								<String>System Time</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Ramp to Zero" TypeGUID="d3a0c118-0577-4aae-9d76-9fdcf7c75eb6">
						<Properties>
							<Property Name="Step Type">
								<String>Ramp</String>
							</Property>
							<Property Name="End Point">
								<Double>0</Double>
							</Property>
							<Property Name="Mode">
								<String>Duration</String>
							</Property>
							<Property Name="Rate">
								<Double>10</Double>
							</Property>
							<Property Name="Duration">
								<Double>5</Double>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Tock" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Channel</String>
							</Property>
							<Property Name="Function">
								<String>--</String>
							</Property>
							<Property Name="Value1.Channel">
								<String>System Time</String>
							</Property>
							<Property Name="Value2.Type">
								<String>Channel</String>
							</Property>
							<Property Name="Value2.Channel">
								<String>LV 1</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Check Zero" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
						<Properties>
							<Property Name="Step Type">
								<String>Conditional</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/User Channel 1</String>
							</Property>
							<Property Name="Comparison">
								<String>Not Equal</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>0</Double>
							</Property>
							<Property Name="Goto Step">
								<DependentNode Path="Ramp Test [User Channel 1]/Root Group 1/Fail" />
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Check Ramp Min Duration" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
						<Properties>
							<Property Name="Step Type">
								<String>Conditional</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Comparison">
								<String>Less</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>4.5</Double>
							</Property>
							<Property Name="Goto Step">
								<DependentNode Path="Ramp Test [User Channel 1]/Root Group 1/Fail" />
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Check Ramp Max Duration" TypeGUID="1cc0b58b-eddf-4401-b482-2ed7a69bfcca">
						<Properties>
							<Property Name="Step Type">
								<String>Conditional</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Local Variables/LV 1</String>
							</Property>
							<Property Name="Comparison">
								<String>Greater</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>5.5</Double>
							</Property>
							<Property Name="Goto Step">
								<DependentNode Path="Ramp Test [User Channel 1]/Root Group 1/Fail" />
							</Property>
						</Properties>
						<Errors />
					</Section>
				</Section>
				<Section Name="Pass" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
					<Properties />
					<Errors />
					<Section Name="Set Pass" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Pass Fail Channels/Gen 1 Pass Fail</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>1</Double>
							</Property>
							<Property Name="Function">
								<String>None</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Stop Profile" TypeGUID="9f447d91-f09d-47c8-809b-a8a49ad8f6bd">
						<Properties>
							<Property Name="Step Type">
								<String>End</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
				</Section>
				<Section Name="Fail" TypeGUID="fdbc195f-2c8c-4f6f-a694-00e8e781f450">
					<Properties />
					<Errors />
					<Section Name="Set Fail" TypeGUID="0d53449c-c8cd-4777-92a7-cad4d65f1a57">
						<Properties>
							<Property Name="Step Type">
								<String>Set Variable</String>
							</Property>
							<Property Name="Channel">
								<String>Target Section/Controller/User Channels/Pass Fail Channels/Gen 1 Pass Fail</String>
							</Property>
							<Property Name="Value1.Type">
								<String>Constant</String>
							</Property>
							<Property Name="Value1.Constant">
								<Double>0</Double>
							</Property>
							<Property Name="Function">
								<String>None</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Stop Profile" TypeGUID="9f447d91-f09d-47c8-809b-a8a49ad8f6bd">
						<Properties>
							<Property Name="Step Type">
								<String>End</String>
							</Property>
						</Properties>
						<Errors />
					</Section>
				</Section>
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ProfileTest/Stop Profile Test.nivstest sha256=332d91cbd4d1dd759b799c06dcc0c7b0540ee165ac6c40af8be455811beec44c bytes=2366 -->
## FILE: tests/testutilities/legacy_files/ProfileTest/Stop Profile Test.nivstest

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ProfileTest/Stop Profile Test.nivstest`
- sha256: `332d91cbd4d1dd759b799c06dcc0c7b0540ee165ac6c40af8be455811beec44c`
- bytes: 2366

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
		<Section Name="Generator 1" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ProfileTest/Too Many Gens.nivstest sha256=a8baf70b81b57f3150f5c9a5948e565b9c93676de225caf4ff4dee4cea38a5b6 bytes=9201 -->
## FILE: tests/testutilities/legacy_files/ProfileTest/Too Many Gens.nivstest

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ProfileTest/Too Many Gens.nivstest`
- sha256: `a8baf70b81b57f3150f5c9a5948e565b9c93676de225caf4ff4dee4cea38a5b6`
- bytes: 9201

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
		<Section Name="Generator 1" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Dwell" TypeGUID="376cd3a2-af99-4855-a664-842d3500812d">
				<Properties>
					<Property Name="Step Type">
						<String>Dwell</String>
					</Property>
					<Property Name="Time">
						<Double>1</Double>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Generator 2" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Dwell" TypeGUID="376cd3a2-af99-4855-a664-842d3500812d">
				<Properties>
					<Property Name="Step Type">
						<String>Dwell</String>
					</Property>
					<Property Name="Time">
						<Double>1</Double>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Generator 3" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Dwell" TypeGUID="376cd3a2-af99-4855-a664-842d3500812d">
				<Properties>
					<Property Name="Step Type">
						<String>Dwell</String>
					</Property>
					<Property Name="Time">
						<Double>1</Double>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Generator 4" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Dwell" TypeGUID="376cd3a2-af99-4855-a664-842d3500812d">
				<Properties>
					<Property Name="Step Type">
						<String>Dwell</String>
					</Property>
					<Property Name="Time">
						<Double>1</Double>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Generator 5" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Dwell" TypeGUID="376cd3a2-af99-4855-a664-842d3500812d">
				<Properties>
					<Property Name="Step Type">
						<String>Dwell</String>
					</Property>
					<Property Name="Time">
						<Double>1</Double>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Generator 6" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Dwell" TypeGUID="376cd3a2-af99-4855-a664-842d3500812d">
				<Properties>
					<Property Name="Step Type">
						<String>Dwell</String>
					</Property>
					<Property Name="Time">
						<Double>1</Double>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Generator 7" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Dwell" TypeGUID="376cd3a2-af99-4855-a664-842d3500812d">
				<Properties>
					<Property Name="Step Type">
						<String>Dwell</String>
					</Property>
					<Property Name="Time">
						<Double>1</Double>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Generator 8" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Dwell" TypeGUID="376cd3a2-af99-4855-a664-842d3500812d">
				<Properties>
					<Property Name="Step Type">
						<String>Dwell</String>
					</Property>
					<Property Name="Time">
						<Double>1</Double>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Generator 9" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Dwell" TypeGUID="376cd3a2-af99-4855-a664-842d3500812d">
				<Properties>
					<Property Name="Step Type">
						<String>Dwell</String>
					</Property>
					<Property Name="Time">
						<Double>1</Double>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Generator 10" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Dwell" TypeGUID="376cd3a2-af99-4855-a664-842d3500812d">
				<Properties>
					<Property Name="Step Type">
						<String>Dwell</String>
					</Property>
					<Property Name="Time">
						<Double>1</Double>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Generator 11" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Dwell" TypeGUID="376cd3a2-af99-4855-a664-842d3500812d">
				<Properties>
					<Property Name="Step Type">
						<String>Dwell</String>
					</Property>
					<Property Name="Time">
						<Double>1</Double>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Generator 12" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Dwell" TypeGUID="376cd3a2-af99-4855-a664-842d3500812d">
				<Properties>
					<Property Name="Step Type">
						<String>Dwell</String>
					</Property>
					<Property Name="Time">
						<Double>1</Double>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ProfileTest/Too Many Steps.nivstest sha256=f12c8ff3a109bc664ca6db31a363099111f6e97403f377b7bdd57af027b39fbb bytes=52886 -->
## FILE: tests/testutilities/legacy_files/ProfileTest/Too Many Steps.nivstest

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ProfileTest/Too Many Steps.nivstest`
- sha256: `f12c8ff3a109bc664ca6db31a363099111f6e97403f377b7bdd57af027b39fbb`
- bytes: 52886

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
		<Section Name="Generator 1" TypeGUID="7e9683c6-0873-4667-af75-a66f455873f1">
			<Properties>
				<Property Name="Mapped Channels">
					<StringArray />
				</Property>
				<Property Name="Execution Target">
					<String />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Replay" TypeGUID="1b93aef3-0d7b-458b-8975-1eaf91a6db2c">
				<Properties>
					<Property Name="Step Type">
						<String>Replay</String>
					</Property>
					<Property Name="Data Points">
						<DoubleArray>
							<Elem>0</Elem>
							<Elem>5.319984</Elem>
							<Elem>5.207386</Elem>
							<Elem>5.091956</Elem>
							<Elem>4.975267</Elem>
							<Elem>4.858909</Elem>
							<Elem>4.74447</Elem>
							<Elem>4.633509</Elem>
							<Elem>4.527541</Elem>
							<Elem>4.428011</Elem>
							<Elem>4.336278</Elem>
							<Elem>4.253593</Elem>
							<Elem>4.181088</Elem>
							<Elem>4.119752</Elem>
							<Elem>4.070423</Elem>
							<Elem>4.033777</Elem>
							<Elem>4.010316</Elem>
							<Elem>4.000361</Elem>
							<Elem>4.004051</Elem>
							<Elem>4.021336</Elem>
							<Elem>4.051984</Elem>
							<Elem>4.095578</Elem>
							<Elem>4.151524</Elem>
							<Elem>4.219059</Elem>
							<Elem>4.297264</Elem>
							<Elem>4.385072</Elem>
							<Elem>4.481283</Elem>
							<Elem>4.584587</Elem>
							<Elem>4.69357</Elem>
							<Elem>4.806747</Elem>
							<Elem>4.922569</Elem>
							<Elem>5.039456</Elem>
							<Elem>5.155809</Elem>
							<Elem>5.270037</Elem>
							<Elem>5.38058</Elem>
							<Elem>5.485924</Elem>
							<Elem>5.584629</Elem>
							<Elem>5.675344</Elem>
							<Elem>5.756827</Elem>
							<Elem>5.827963</Elem>
							<Elem>5.887776</Elem>
							<Elem>5.935447</Elem>
							<Elem>5.970322</Elem>
							<Elem>5.991921</Elem>
							<Elem>5.999949</Elem>
							<Elem>5.994291</Elem>
							<Elem>5.975025</Elem>
							<Elem>5.942411</Elem>
							<Elem>5.896895</Elem>
							<Elem>5.839097</Elem>
							<Elem>5.769807</Elem>
							<Elem>5.689973</Elem>
							<Elem>5.600685</Elem>
							<Elem>5.503167</Elem>
							<Elem>5.398752</Elem>
							<Elem>5.288869</Elem>
							<Elem>5.175023</Elem>
							<Elem>5.058774</Elem>
							<Elem>4.941714</Elem>
							<Elem>4.825447</Elem>
							<Elem>4.711567</Elem>
							<Elem>4.601634</Elem>
							<Elem>4.497158</Elem>
							<Elem>4.399569</Elem>
							<Elem>4.310209</Elem>
							<Elem>4.230303</Elem>
							<Elem>4.160948</Elem>
							<Elem>4.103096</Elem>
							<Elem>4.057544</Elem>
							<Elem>4.024918</Elem>
							<Elem>4.005667</Elem>
							<Elem>4.000057</Elem>
							<Elem>4.008167</Elem>
							<Elem>4.029889</Elem>
							<Elem>4.064925</Elem>
							<Elem>4.112796</Elem>
							<Elem>4.172849</Elem>
							<Elem>4.244259</Elem>
							<Elem>4.326048</Elem>
							<Elem>4.417095</Elem>
							<Elem>4.516151</Elem>
							<Elem>4.621856</Elem>
							<Elem>4.73276</Elem>
							<Elem>4.84734</Elem>
							<Elem>4.964023</Elem>
							<Elem>5.081205</Elem>
							<Elem>5.197278</Elem>
							<Elem>5.310645</Elem>
							<Elem>5.419748</Elem>
							<Elem>5.523088</Elem>
							<Elem>5.619243</Elem>
							<Elem>5.70689</Elem>
							<Elem>5.784823</Elem>
							<Elem>5.85197</Elem>
							<Elem>5.907405</Elem>
							<Elem>5.950364</Elem>
							<Elem>5.980255</Elem>
							<Elem>5.996664</Elem>
							<Elem>5.999365</Elem>
							<Elem>5.988317</Elem>
							<Elem>5.963671</Elem>
							<Elem>5.925765</Elem>
							<Elem>5.875117</Elem>
							<Elem>5.812423</Elem>
							<Elem>5.738544</Elem>
							<Elem>5.654496</Elem>
							<Elem>5.561434</Elem>
							<Elem>5.460637</Elem>
							<Elem>5.353494</Elem>
							<Elem>5.241477</Elem>
							<Elem>5.12613</Elem>
							<Elem>5.00904</Elem>
							<Elem>4.89182</Elem>
							<Elem>4.776084</Elem>
							<Elem>4.663428</Elem>
							<Elem>4.555404</Elem>
							<Elem>4.4535</Elem>
							<Elem>4.359124</Elem>
							<Elem>4.273575</Elem>
							<Elem>4.198035</Elem>
							<Elem>4.133546</Elem>
							<Elem>4.080999</Elem>
							<Elem>4.04112</Elem>
							<Elem>4.014462</Elem>
							<Elem>4.001392</Elem>
							<Elem>4.002094</Elem>
							<Elem>4.01656</Elem>
							<Elem>4.044593</Elem>
							<Elem>4.085807</Elem>
							<Elem>4.139636</Elem>
							<Elem>4.205339</Elem>
							<Elem>4.28201</Elem>
							<Elem>4.368595</Elem>
							<Elem>4.463898</Elem>
							<Elem>4.566605</Elem>
							<Elem>4.675301</Elem>
							<Elem>4.788484</Elem>
							<Elem>4.904593</Elem>
							<Elem>5.022026</Elem>
							<Elem>5.13916</Elem>
							<Elem>5.254377</Elem>
							<Elem>5.366086</Elem>
							<Elem>5.472744</Elem>
							<Elem>5.572875</Elem>
							<Elem>5.665096</Elem>
							<Elem>5.748132</Elem>
							<Elem>5.820832</Elem>
							<Elem>5.882192</Elem>
							<Elem>5.931361</Elem>
							<Elem>5.967658</Elem>
							<Elem>5.990579</Elem>
							<Elem>5.999806</Elem>
							<Elem>5.995208</Elem>
							<Elem>5.976848</Elem>
							<Elem>5.944977</Elem>
							<Elem>5.900035</Elem>
							<Elem>5.84264</Elem>
							<Elem>5.773586</Elem>
							<Elem>5.693826</Elem>
							<Elem>5.604462</Elem>
							<Elem>5.506729</Elem>
							<Elem>5.401979</Elem>
							<Elem>5.29166</Elem>
							<Elem>5.177299</Elem>
							<Elem>5.060478</Elem>
							<Elem>4.942814</Elem>
							<Elem>4.825936</Elem>
							<Elem>4.711463</Elem>
							<Elem>4.60098</Elem>
							<Elem>4.496018</Elem>
							<Elem>4.398032</Elem>
							<Elem>4.30838</Elem>
							<Elem>4.228306</Elem>
							<Elem>4.158919</Elem>
							<Elem>4.101184</Elem>
							<Elem>4.055901</Elem>
							<Elem>4.023701</Elem>
							<Elem>4.005031</Elem>
							<Elem>4.000152</Elem>
							<Elem>4.009134</Elem>
							<Elem>4.031855</Elem>
							<Elem>4.068</Elem>
							<Elem>4.117071</Elem>
							<Elem>4.17839</Elem>
							<Elem>4.251107</Elem>
							<Elem>4.334215</Elem>
							<Elem>4.426564</Elem>
							<Elem>4.526872</Elem>
							<Elem>4.63375</Elem>
							<Elem>4.745716</Elem>
							<Elem>4.861215</Elem>
							<Elem>4.978647</Elem>
							<Elem>5.09638</Elem>
							<Elem>5.212781</Elem>
							<Elem>5.326234</Elem>
							<Elem>5.435162</Elem>
							<Elem>5.538053</Elem>
							<Elem>5.633477</Elem>
							<Elem>5.720108</Elem>
							<Elem>5.79674</Elem>
							<Elem>5.862309</Elem>
							<Elem>5.915901</Elem>
							<Elem>5.956771</Elem>
							<Elem>5.984348</Elem>
							<Elem>5.998248</Elem>
							<Elem>5.998275</Elem>
							<Elem>5.984427</Elem>
							<Elem>5.956894</Elem>
							<Elem>5.916057</Elem>
							<Elem>5.862483</Elem>
							<Elem>5.796914</Elem>
							<Elem>5.72026</Elem>
							<Elem>5.633586</Elem>
							<Elem>5.538095</Elem>
							<Elem>5.435115</Elem>
							<Elem>5.326078</Elem>
							<Elem>5.212498</Elem>
							<Elem>5.095957</Elem>
							<Elem>4.978075</Elem>
							<Elem>4.860492</Elem>
							<Elem>4.744845</Elem>
							<Elem>4.632745</Elem>
							<Elem>4.525751</Elem>
							<Elem>4.425354</Elem>
							<Elem>4.332954</Elem>
							<Elem>4.249837</Elem>
							<Elem>4.177163</Elem>
							<Elem>4.115945</Elem>
							<Elem>4.067038</Elem>
							<Elem>4.031124</Elem>
							<Elem>4.008705</Elem>
							<Elem>4.000097</Elem>
							<Elem>4.005421</Elem>
							<Elem>4.024604</Elem>
							<Elem>4.057382</Elem>
							<Elem>4.103299</Elem>
							<Elem>4.161717</Elem>
							<Elem>4.231825</Elem>
							<Elem>4.312645</Elem>
							<Elem>4.403053</Elem>
							<Elem>4.501789</Elem>
							<Elem>4.607477</Elem>
							<Elem>4.718646</Elem>
							<Elem>4.833744</Elem>
							<Elem>4.951166</Elem>
							<Elem>5.069276</Elem>
							<Elem>5.186425</Elem>
							<Elem>5.300977</Elem>
							<Elem>5.411336</Elem>
							<Elem>5.515958</Elem>
							<Elem>5.613385</Elem>
							<Elem>5.702253</Elem>
							<Elem>5.781322</Elem>
							<Elem>5.849486</Elem>
							<Elem>5.905793</Elem>
							<Elem>5.949453</Elem>
							<Elem>5.979855</Elem>
							<Elem>5.996573</Elem>
							<Elem>5.999372</Elem>
							<Elem>5.98821</Elem>
							<Elem>5.96324</Elem>
							<Elem>5.924812</Elem>
							<Elem>5.873458</Elem>
							<Elem>5.809895</Elem>
							<Elem>5.73501</Elem>
							<Elem>5.649847</Elem>
							<Elem>5.555596</Elem>
							<Elem>5.453574</Elem>
							<Elem>5.345204</Elem>
							<Elem>5.232003</Elem>
							<Elem>5.115552</Elem>
							<Elem>4.997479</Elem>
							<Elem>4.879436</Elem>
							<Elem>4.763073</Elem>
							<Elem>4.65002</Elem>
							<Elem>4.541858</Elem>
							<Elem>4.440101</Elem>
							<Elem>4.346175</Elem>
							<Elem>4.261394</Elem>
							<Elem>4.186947</Elem>
							<Elem>4.123877</Elem>
							<Elem>4.07307</Elem>
							<Elem>4.035237</Elem>
							<Elem>4.010911</Elem>
							<Elem>4.000434</Elem>
							<Elem>4.003954</Elem>
							<Elem>4.021426</Elem>
							<Elem>4.052605</Elem>
							<Elem>4.097057</Elem>
							<Elem>4.154161</Elem>
							<Elem>4.223119</Elem>
							<Elem>4.302966</Elem>
							<Elem>4.392585</Elem>
							<Elem>4.490721</Elem>
							<Elem>4.596</Elem>
							<Elem>4.706947</Elem>
							<Elem>4.822008</Elem>
							<Elem>4.93957</Elem>
							<Elem>5.057985</Elem>
							<Elem>5.175592</Elem>
							<Elem>5.290743</Elem>
							<Elem>5.401821</Elem>
							<Elem>5.507268</Elem>
							<Elem>5.605603</Elem>
							<Elem>5.695447</Elem>
							<Elem>5.775537</Elem>
							<Elem>5.844749</Elem>
							<Elem>5.902108</Elem>
							<Elem>5.946809</Elem>
							<Elem>5.978222</Elem>
							<Elem>5.995905</Elem>
							<Elem>5.999607</Elem>
							<Elem>5.989274</Elem>
							<Elem>5.96505</Elem>
							<Elem>5.927272</Elem>
							<Elem>5.876469</Elem>
							<Elem>5.813353</Elem>
							<Elem>5.738808</Elem>
							<Elem>5.653881</Elem>
							<Elem>5.559763</Elem>
							<Elem>5.457775</Elem>
							<Elem>5.34935</Elem>
							<Elem>5.236009</Elem>
							<Elem>5.119346</Elem>
							<Elem>5.001</Elem>
							<Elem>4.882635</Elem>
							<Elem>4.765913</Elem>
							<Elem>4.652478</Elem>
							<Elem>4.543924</Elem>
							<Elem>4.441778</Elem>
							<Elem>4.347479</Elem>
							<Elem>4.262354</Elem>
							<Elem>4.187602</Elem>
							<Elem>4.124275</Elem>
							<Elem>4.073267</Elem>
							<Elem>4.035296</Elem>
							<Elem>4.0109</Elem>
							<Elem>4.000423</Elem>
							<Elem>4.004014</Elem>
							<Elem>4.021627</Elem>
							<Elem>4.053013</Elem>
							<Elem>4.097734</Elem>
							<Elem>4.155161</Elem>
							<Elem>4.224489</Elem>
							<Elem>4.304741</Elem>
							<Elem>4.394789</Elem>
							<Elem>4.493367</Elem>
							<Elem>4.599087</Elem>
							<Elem>4.71046</Elem>
							<Elem>4.825918</Elem>
							<Elem>4.943834</Elem>
							<Elem>5.062548</Elem>
							<Elem>5.180385</Elem>
							<Elem>5.295686</Elem>
							<Elem>5.406824</Elem>
							<Elem>5.512231</Elem>
							<Elem>5.610422</Elem>
							<Elem>5.700009</Elem>
							<Elem>5.77973</Elem>
							<Elem>5.848457</Elem>
							<Elem>5.90522</Elem>
							<Elem>5.949217</Elem>
							<Elem>5.979825</Elem>
							<Elem>5.99661</Elem>
							<Elem>5.999334</Elem>
							<Elem>5.987956</Elem>
							<Elem>5.962634</Elem>
							<Elem>5.923724</Elem>
							<Elem>5.871774</Elem>
							<Elem>5.807515</Elem>
							<Elem>5.731852</Elem>
							<Elem>5.645852</Elem>
							<Elem>5.550727</Elem>
							<Elem>5.447821</Elem>
							<Elem>5.338585</Elem>
							<Elem>5.224562</Elem>
							<Elem>5.107361</Elem>
							<Elem>4.988637</Elem>
							<Elem>4.870069</Elem>
							<Elem>4.753331</Elem>
							<Elem>4.640073</Elem>
							<Elem>4.531897</Elem>
							<Elem>4.430332</Elem>
							<Elem>4.336814</Elem>
							<Elem>4.252668</Elem>
							<Elem>4.179084</Elem>
							<Elem>4.117103</Elem>
							<Elem>4.067605</Elem>
							<Elem>4.031291</Elem>
							<Elem>4.008676</Elem>
							<Elem>4.000082</Elem>
							<Elem>4.005633</Elem>
							<Elem>4.025253</Elem>
							<Elem>4.058665</Elem>
							<Elem>4.105399</Elem>
							<Elem>4.164795</Elem>
							<Elem>4.236015</Elem>
							<Elem>4.318052</Elem>
							<Elem>4.409746</Elem>
							<Elem>4.509801</Elem>
							<Elem>4.616801</Elem>
							<Elem>4.729232</Elem>
							<Elem>4.845503</Elem>
							<Elem>4.963968</Elem>
							<Elem>5.082948</Elem>
							<Elem>5.200759</Elem>
							<Elem>5.315732</Elem>
							<Elem>5.426237</Elem>
							<Elem>5.530707</Elem>
							<Elem>5.627662</Elem>
							<Elem>5.715727</Elem>
							<Elem>5.793651</Elem>
							<Elem>5.86033</Elem>
							<Elem>5.914815</Elem>
							<Elem>5.956334</Elem>
							<Elem>5.984295</Elem>
							<Elem>5.998301</Elem>
							<Elem>5.998149</Elem>
							<Elem>5.983842</Elem>
							<Elem>5.955578</Elem>
							<Elem>5.913759</Elem>
							<Elem>5.858974</Elem>
							<Elem>5.791999</Elem>
							<Elem>5.713783</Elem>
							<Elem>5.625435</Elem>
							<Elem>5.528206</Elem>
							<Elem>5.423475</Elem>
							<Elem>5.312729</Elem>
							<Elem>5.197537</Elem>
							<Elem>5.079536</Elem>
							<Elem>4.9604</Elem>
							<Elem>4.84182</Elem>
							<Elem>4.725482</Elem>
							<Elem>4.613036</Elem>
							<Elem>4.506082</Elem>
							<Elem>4.40614</Elem>
							<Elem>4.314629</Elem>
							<Elem>4.232852</Elem>
							<Elem>4.161972</Elem>
							<Elem>4.102997</Elem>
							<Elem>4.056769</Elem>
							<Elem>4.023945</Elem>
							<Elem>4.004994</Elem>
							<Elem>4.000187</Elem>
							<Elem>4.009595</Elem>
							<Elem>4.033086</Elem>
							<Elem>4.070328</Elem>
							<Elem>4.120793</Elem>
							<Elem>4.183765</Elem>
							<Elem>4.258351</Elem>
							<Elem>4.343491</Elem>
							<Elem>4.437975</Elem>
							<Elem>4.54046</Elem>
							<Elem>4.64949</Elem>
							<Elem>4.763512</Elem>
							<Elem>4.880906</Elem>
							<Elem>5</Elem>
							<Elem>5.1191</Elem>
							<Elem>5.23651</Elem>
							<Elem>5.350558</Elem>
							<Elem>5.45962</Elem>
							<Elem>5.562142</Elem>
							<Elem>5.656663</Elem>
							<Elem>5.741835</Elem>
							<Elem>5.816444</Elem>
							<Elem>5.879425</Elem>
							<Elem>5.929881</Elem>
							<Elem>5.967089</Elem>
							<Elem>5.990517</Elem>
							<Elem>5.999831</Elem>
							<Elem>5.994895</Elem>
							<Elem>5.975778</Elem>
							<Elem>5.942749</Elem>
							<Elem>5.896279</Elem>
							<Elem>5.837027</Elem>
							<Elem>5.765837</Elem>
							<Elem>5.683722</Elem>
							<Elem>5.591852</Elem>
							<Elem>5.491536</Elem>
							<Elem>5.384204</Elem>
							<Elem>5.271385</Elem>
							<Elem>5.154689</Elem>
							<Elem>5.03578</Elem>
							<Elem>4.916355</Elem>
							<Elem>4.798118</Elem>
							<Elem>4.682758</Elem>
							<Elem>4.57192</Elem>
							<Elem>4.467187</Elem>
							<Elem>4.370057</Elem>
							<Elem>4.281917</Elem>
							<Elem>4.204027</Elem>
							<Elem>4.1375</Elem>
							<Elem>4.083289</Elem>
							<Elem>4.042169</Elem>
							<Elem>4.014729</Elem>
							<Elem>4.001365</Elem>
							<Elem>4.002268</Elem>
							<Elem>4.017427</Elem>
							<Elem>4.046629</Elem>
							<Elem>4.089457</Elem>
							<Elem>4.145302</Elem>
							<Elem>4.213367</Elem>
							<Elem>4.292681</Elem>
							<Elem>4.382111</Elem>
							<Elem>4.48038</Elem>
							<Elem>4.586085</Elem>
							<Elem>4.697713</Elem>
							<Elem>4.813671</Elem>
							<Elem>4.932299</Elem>
							<Elem>5.051901</Elem>
							<Elem>5.170767</Elem>
							<Elem>5.287194</Elem>
							<Elem>5.399518</Elem>
							<Elem>5.506129</Elem>
							<Elem>5.605502</Elem>
							<Elem>5.696213</Elem>
							<Elem>5.776961</Elem>
							<Elem>5.846591</Elem>
							<Elem>5.904103</Elem>
							<Elem>5.948672</Elem>
							<Elem>5.979658</Elem>
							<Elem>5.996615</Elem>
							<Elem>5.999299</Elem>
							<Elem>5.987669</Elem>
							<Elem>5.961889</Elem>
							<Elem>5.922327</Elem>
							<Elem>5.869548</Elem>
							<Elem>5.804307</Elem>
							<Elem>5.727536</Elem>
							<Elem>5.640334</Elem>
							<Elem>5.543949</Elem>
							<Elem>5.439763</Elem>
							<Elem>5.329267</Elem>
							<Elem>5.214045</Elem>
							<Elem>5.095748</Elem>
							<Elem>4.976073</Elem>
							<Elem>4.856735</Elem>
							<Elem>4.739447</Elem>
							<Elem>4.62589</Elem>
							<Elem>4.517696</Elem>
							<Elem>4.416415</Elem>
							<Elem>4.323504</Elem>
							<Elem>4.240296</Elem>
							<Elem>4.167986</Elem>
							<Elem>4.107615</Elem>
							<Elem>4.06005</Elem>
							<Elem>4.025976</Elem>
							<Elem>4.005884</Elem>
							<Elem>4.000065</Elem>
							<Elem>4.008603</Elem>
							<Elem>4.03138</Elem>
							<Elem>4.068068</Elem>
							<Elem>4.118144</Elem>
							<Elem>4.180891</Elem>
							<Elem>4.255407</Elem>
							<Elem>4.340625</Elem>
							<Elem>4.435321</Elem>
							<Elem>4.538136</Elem>
							<Elem>4.647594</Elem>
							<Elem>4.762122</Elem>
							<Elem>4.880074</Elem>
							<Elem>4.999757</Elem>
							<Elem>5.119448</Elem>
							<Elem>5.237427</Elem>
							<Elem>5.351998</Elem>
							<Elem>5.461512</Elem>
							<Elem>5.564394</Elem>
							<Elem>5.659162</Elem>
							<Elem>5.744453</Elem>
							<Elem>5.819038</Elem>
							<Elem>5.881842</Elem>
							<Elem>5.93196</Elem>
							<Elem>5.968669</Elem>
							<Elem>5.991439</Elem>
							<Elem>5.999941</Elem>
							<Elem>5.994049</Elem>
							<Elem>5.973846</Elem>
							<Elem>5.939622</Elem>
							<Elem>5.891867</Elem>
							<Elem>5.831267</Elem>
							<Elem>5.758693</Elem>
							<Elem>5.675188</Elem>
							<Elem>5.581954</Elem>
							<Elem>5.480332</Elem>
							<Elem>5.371786</Elem>
							<Elem>5.257878</Elem>
							<Elem>5.140248</Elem>
							<Elem>5.020592</Elem>
							<Elem>4.900634</Elem>
							<Elem>4.782102</Elem>
							<Elem>4.666705</Elem>
							<Elem>4.556108</Elem>
							<Elem>4.451906</Elem>
							<Elem>4.355602</Elem>
							<Elem>4.268585</Elem>
							<Elem>4.192113</Elem>
							<Elem>4.127289</Elem>
							<Elem>4.075051</Elem>
							<Elem>4.036153</Elem>
							<Elem>4.011158</Elem>
							<Elem>4.00043</Elem>
							<Elem>4.004125</Elem>
							<Elem>4.022192</Elem>
							<Elem>4.054372</Elem>
							<Elem>4.100202</Elem>
							<Elem>4.159023</Elem>
							<Elem>4.229988</Elem>
							<Elem>4.312073</Elem>
							<Elem>4.404095</Elem>
							<Elem>4.504727</Elem>
							<Elem>4.612516</Elem>
							<Elem>4.725907</Elem>
							<Elem>4.843263</Elem>
							<Elem>4.962888</Elem>
							<Elem>5.083055</Elem>
							<Elem>5.202027</Elem>
							<Elem>5.318086</Elem>
							<Elem>5.429553</Elem>
							<Elem>5.534817</Elem>
							<Elem>5.632356</Elem>
							<Elem>5.720759</Elem>
							<Elem>5.798745</Elem>
							<Elem>5.865187</Elem>
							<Elem>5.919122</Elem>
							<Elem>5.959768</Elem>
							<Elem>5.986535</Elem>
							<Elem>5.999034</Elem>
							<Elem>5.997083</Elem>
							<Elem>5.980708</Elem>
							<Elem>5.950144</Elem>
							<Elem>5.90583</Elem>
							<Elem>5.848406</Elem>
							<Elem>5.778702</Elem>
							<Elem>5.697724</Elem>
							<Elem>5.606643</Elem>
							<Elem>5.506777</Elem>
							<Elem>5.399568</Elem>
							<Elem>5.28657</Elem>
							<Elem>5.169417</Elem>
							<Elem>5.049805</Elem>
							<Elem>4.929466</Elem>
							<Elem>4.810143</Elem>
							<Elem>4.693564</Elem>
							<Elem>4.58142</Elem>
							<Elem>4.475334</Elem>
							<Elem>4.376846</Elem>
							<Elem>4.287384</Elem>
							<Elem>4.208244</Elem>
							<Elem>4.140576</Elem>
							<Elem>4.085362</Elem>
							<Elem>4.043405</Elem>
							<Elem>4.015314</Elem>
							<Elem>4.001498</Elem>
							<Elem>4.002161</Elem>
							<Elem>4.017294</Elem>
							<Elem>4.046679</Elem>
							<Elem>4.089894</Elem>
							<Elem>4.146312</Elem>
							<Elem>4.215118</Elem>
							<Elem>4.295314</Elem>
							<Elem>4.385739</Elem>
							<Elem>4.485082</Elem>
							<Elem>4.591903</Elem>
							<Elem>4.704651</Elem>
							<Elem>4.821692</Elem>
							<Elem>4.941326</Elem>
							<Elem>5.061819</Elem>
							<Elem>5.181419</Elem>
							<Elem>5.29839</Elem>
							<Elem>5.411034</Elem>
							<Elem>5.517713</Elem>
							<Elem>5.616877</Elem>
							<Elem>5.707085</Elem>
							<Elem>5.787026</Elem>
							<Elem>5.855535</Elem>
							<Elem>5.911616</Elem>
							<Elem>5.954453</Elem>
							<Elem>5.983421</Elem>
							<Elem>5.998096</Elem>
							<Elem>5.998264</Elem>
							<Elem>5.983921</Elem>
							<Elem>5.955272</Elem>
							<Elem>5.912732</Elem>
							<Elem>5.856918</Elem>
							<Elem>5.78864</Elem>
							<Elem>5.708889</Elem>
							<Elem>5.618823</Elem>
							<Elem>5.519751</Elem>
							<Elem>5.413113</Elem>
							<Elem>5.300459</Elem>
							<Elem>5.183429</Elem>
							<Elem>5.063723</Elem>
							<Elem>4.943085</Elem>
							<Elem>4.82327</Elem>
							<Elem>4.706021</Elem>
							<Elem>4.593046</Elem>
							<Elem>4.485992</Elem>
							<Elem>4.386416</Elem>
							<Elem>4.29577</Elem>
							<Elem>4.215376</Elem>
							<Elem>4.146405</Elem>
							<Elem>4.089865</Elem>
							<Elem>4.04658</Elem>
							<Elem>4.017182</Elem>
							<Elem>4.002103</Elem>
							<Elem>4.001563</Elem>
							<Elem>4.015573</Elem>
							<Elem>4.043931</Elem>
							<Elem>4.086225</Elem>
							<Elem>4.141841</Elem>
							<Elem>4.209969</Elem>
							<Elem>4.289619</Elem>
							<Elem>4.37963</Elem>
							<Elem>4.478692</Elem>
							<Elem>4.58536</Elem>
							<Elem>4.698081</Elem>
							<Elem>4.815212</Elem>
							<Elem>4.935043</Elem>
							<Elem>5.055827</Elem>
							<Elem>5.175803</Elem>
							<Elem>5.293219</Elem>
							<Elem>5.406361</Elem>
							<Elem>5.513578</Elem>
							<Elem>5.613304</Elem>
							<Elem>5.704083</Elem>
							<Elem>5.784587</Elem>
							<Elem>5.85364</Elem>
							<Elem>5.910232</Elem>
							<Elem>5.953535</Elem>
							<Elem>5.982915</Elem>
							<Elem>5.997941</Elem>
							<Elem>5.99839</Elem>
							<Elem>5.984256</Elem>
							<Elem>5.955741</Elem>
							<Elem>5.913261</Elem>
							<Elem>5.857435</Elem>
							<Elem>5.789076</Elem>
							<Elem>5.709181</Elem>
							<Elem>5.618917</Elem>
							<Elem>5.519602</Elem>
							<Elem>5.412687</Elem>
							<Elem>5.299733</Elem>
							<Elem>5.182391</Elem>
							<Elem>5.062376</Elem>
							<Elem>4.941444</Elem>
							<Elem>4.821363</Elem>
							<Elem>4.703888</Elem>
							<Elem>4.590741</Elem>
							<Elem>4.483575</Elem>
							<Elem>4.38396</Elem>
							<Elem>4.293355</Elem>
							<Elem>4.213086</Elem>
							<Elem>4.14433</Elem>
							<Elem>4.088096</Elem>
							<Elem>4.045207</Elem>
							<Elem>4.016293</Elem>
							<Elem>4.001781</Elem>
							<Elem>4.001884</Elem>
							<Elem>4.016602</Elem>
							<Elem>4.045723</Elem>
							<Elem>4.088822</Elem>
							<Elem>4.14527</Elem>
							<Elem>4.214241</Elem>
							<Elem>4.294726</Elem>
							<Elem>4.385549</Elem>
							<Elem>4.48538</Elem>
							<Elem>4.592756</Elem>
							<Elem>4.706107</Elem>
							<Elem>4.82377</Elem>
							<Elem>4.944021</Elem>
							<Elem>5.065099</Elem>
							<Elem>5.185228</Elem>
							<Elem>5.302647</Elem>
							<Elem>5.415634</Elem>
							<Elem>5.52253</Elem>
							<Elem>5.621767</Elem>
							<Elem>5.711889</Elem>
							<Elem>5.791572</Elem>
							<Elem>5.859646</Elem>
							<Elem>5.91511</Elem>
							<Elem>5.957148</Elem>
							<Elem>5.985143</Elem>
							<Elem>5.998681</Elem>
							<Elem>5.997561</Elem>
							<Elem>5.981798</Elem>
							<Elem>5.951621</Elem>
							<Elem>5.907471</Elem>
							<Elem>5.849995</Elem>
							<Elem>5.780034</Elem>
							<Elem>5.698615</Elem>
							<Elem>5.606931</Elem>
							<Elem>5.506328</Elem>
							<Elem>5.398282</Elem>
							<Elem>5.284381</Elem>
							<Elem>5.166295</Elem>
							<Elem>5.04576</Elem>
							<Elem>4.924548</Elem>
							<Elem>4.804439</Elem>
							<Elem>4.687198</Elem>
							<Elem>4.57455</Elem>
							<Elem>4.468152</Elem>
							<Elem>4.369567</Elem>
							<Elem>4.280248</Elem>
							<Elem>4.201509</Elem>
							<Elem>4.134509</Elem>
							<Elem>4.080235</Elem>
							<Elem>4.039487</Elem>
							<Elem>4.012868</Elem>
							<Elem>4.000769</Elem>
							<Elem>4.003372</Elem>
							<Elem>4.02064</Elem>
							<Elem>4.052321</Elem>
							<Elem>4.097951</Elem>
							<Elem>4.156859</Elem>
							<Elem>4.228182</Elem>
							<Elem>4.31087</Elem>
							<Elem>4.403708</Elem>
							<Elem>4.50533</Elem>
							<Elem>4.614241</Elem>
							<Elem>4.728838</Elem>
							<Elem>4.847434</Elem>
							<Elem>4.968283</Elem>
							<Elem>5.089605</Elem>
							<Elem>5.209612</Elem>
							<Elem>5.326536</Elem>
							<Elem>5.438655</Elem>
							<Elem>5.544314</Elem>
							<Elem>5.641956</Elem>
							<Elem>5.730141</Elem>
							<Elem>5.807567</Elem>
							<Elem>5.873092</Elem>
							<Elem>5.925747</Elem>
							<Elem>5.964755</Elem>
							<Elem>5.989538</Elem>
							<Elem>5.999729</Elem>
							<Elem>5.995176</Elem>
							<Elem>5.975944</Elem>
							<Elem>5.942314</Elem>
							<Elem>5.894781</Elem>
							<Elem>5.834044</Elem>
							<Elem>5.760997</Elem>
							<Elem>5.676716</Elem>
							<Elem>5.582444</Elem>
							<Elem>5.479572</Elem>
							<Elem>5.369615</Elem>
							<Elem>5.254197</Elem>
							<Elem>5.13502</Elem>
							<Elem>5.013845</Elem>
							<Elem>4.892459</Elem>
							<Elem>4.772656</Elem>
							<Elem>4.656205</Elem>
							<Elem>4.544827</Elem>
							<Elem>4.440168</Elem>
							<Elem>4.343774</Elem>
							<Elem>4.257072</Elem>
							<Elem>4.181343</Elem>
							<Elem>4.117709</Elem>
							<Elem>4.067111</Elem>
							<Elem>4.030299</Elem>
							<Elem>4.007819</Elem>
							<Elem>4.000006</Elem>
							<Elem>4.006977</Elem>
							<Elem>4.028631</Elem>
							<Elem>4.064649</Elem>
							<Elem>4.114502</Elem>
							<Elem>4.177454</Elem>
							<Elem>4.252575</Elem>
							<Elem>4.338756</Elem>
							<Elem>4.434724</Elem>
							<Elem>4.539059</Elem>
							<Elem>4.65022</Elem>
							<Elem>4.766562</Elem>
							<Elem>4.886365</Elem>
							<Elem>5.007854</Elem>
							<Elem>5.129233</Elem>
							<Elem>5.248705</Elem>
							<Elem>5.3645</Elem>
							<Elem>5.474903</Elem>
							<Elem>5.578279</Elem>
							<Elem>5.673096</Elem>
							<Elem>5.757949</Elem>
							<Elem>5.831579</Elem>
							<Elem>5.892893</Elem>
							<Elem>5.940983</Elem>
							<Elem>5.975133</Elem>
							<Elem>5.994836</Elem>
							<Elem>5.999797</Elem>
							<Elem>5.989942</Elem>
							<Elem>5.965413</Elem>
							<Elem>5.926573</Elem>
							<Elem>5.873996</Elem>
							<Elem>5.808458</Elem>
							<Elem>5.73093</Elem>
							<Elem>5.642561</Elem>
							<Elem>5.544658</Elem>
							<Elem>5.438672</Elem>
							<Elem>5.326175</Elem>
							<Elem>5.208835</Elem>
							<Elem>5.088391</Elem>
							<Elem>4.96663</Elem>
							<Elem>4.845358</Elem>
							<Elem>4.726376</Elem>
							<Elem>4.611449</Elem>
							<Elem>4.502283</Elem>
							<Elem>4.400501</Elem>
							<Elem>4.307613</Elem>
							<Elem>4.225</Elem>
							<Elem>4.153891</Elem>
							<Elem>4.095342</Elem>
							<Elem>4.050225</Elem>
							<Elem>4.019212</Elem>
							<Elem>4.002765</Elem>
							<Elem>4.001131</Elem>
							<Elem>4.014336</Elem>
							<Elem>4.042186</Elem>
							<Elem>4.08427</Elem>
							<Elem>4.139962</Elem>
							<Elem>4.208439</Elem>
							<Elem>4.288684</Elem>
							<Elem>4.379506</Elem>
							<Elem>4.479556</Elem>
							<Elem>4.587348</Elem>
							<Elem>4.70128</Elem>
							<Elem>4.81966</Elem>
							<Elem>4.940727</Elem>
							<Elem>5.06268</Elem>
							<Elem>5.183708</Elem>
							<Elem>5.302008</Elem>
							<Elem>5.415821</Elem>
							<Elem>5.523452</Elem>
							<Elem>5.6233</Elem>
							<Elem>5.713877</Elem>
							<Elem>5.793835</Elem>
							<Elem>5.861981</Elem>
							<Elem>5.917299</Elem>
							<Elem>5.958966</Elem>
							<Elem>5.986357</Elem>
							<Elem>5.999064</Elem>
							<Elem>5.996895</Elem>
							<Elem>5.97988</Elem>
							<Elem>5.948271</Elem>
							<Elem>5.902537</Elem>
							<Elem>5.843356</Elem>
							<Elem>5.771609</Elem>
							<Elem>5.688363</Elem>
							<Elem>5.594856</Elem>
							<Elem>5.492481</Elem>
							<Elem>5.382762</Elem>
							<Elem>5.267333</Elem>
							<Elem>5.147914</Elem>
							<Elem>5.026285</Elem>
							<Elem>4.904258</Elem>
							<Elem>4.783653</Elem>
							<Elem>4.666268</Elem>
							<Elem>4.553855</Elem>
							<Elem>4.44809</Elem>
							<Elem>4.350552</Elem>
							<Elem>4.262697</Elem>
							<Elem>4.185837</Elem>
							<Elem>4.121121</Elem>
							<Elem>4.069515</Elem>
							<Elem>4.031791</Elem>
							<Elem>4.008515</Elem>
							<Elem>4.000035</Elem>
							<Elem>4.00648</Elem>
							<Elem>4.027757</Elem>
							<Elem>4.063549</Elem>
							<Elem>4.113325</Elem>
							<Elem>4.176342</Elem>
							<Elem>4.251662</Elem>
							<Elem>4.338161</Elem>
							<Elem>4.43455</Elem>
							<Elem>4.539389</Elem>
							<Elem>4.651114</Elem>
							<Elem>4.768057</Elem>
							<Elem>4.88847</Elem>
							<Elem>5.010556</Elem>
							<Elem>5.132489</Elem>
							<Elem>5.252448</Elem>
							<Elem>5.368639</Elem>
							<Elem>5.479325</Elem>
							<Elem>5.58285</Elem>
							<Elem>5.677666</Elem>
							<Elem>5.762353</Elem>
							<Elem>5.835645</Elem>
							<Elem>5.896442</Elem>
							<Elem>5.943834</Elem>
							<Elem>5.977111</Elem>
							<Elem>5.995773</Elem>
							<Elem>5.999538</Elem>
							<Elem>5.988348</Elem>
							<Elem>5.962368</Elem>
							<Elem>5.921985</Elem>
							<Elem>5.867802</Elem>
							<Elem>5.800628</Elem>
							<Elem>5.721465</Elem>
							<Elem>5.631499</Elem>
							<Elem>5.532074</Elem>
							<Elem>5.424677</Elem>
							<Elem>5.310916</Elem>
							<Elem>5.192494</Elem>
							<Elem>5.071183</Elem>
							<Elem>4.948801</Elem>
							<Elem>4.827179</Elem>
							<Elem>4.708142</Elem>
							<Elem>4.593471</Elem>
							<Elem>4.484887</Elem>
							<Elem>4.384017</Elem>
							<Elem>4.292374</Elem>
							<Elem>4.211334</Elem>
							<Elem>4.142111</Elem>
							<Elem>4.085746</Elem>
							<Elem>4.043085</Elem>
							<Elem>4.01477</Elem>
							<Elem>4.001227</Elem>
							<Elem>4.002662</Elem>
							<Elem>4.019056</Elem>
							<Elem>4.050163</Elem>
							<Elem>4.09552</Elem>
							<Elem>4.154449</Elem>
							<Elem>4.226066</Elem>
							<Elem>4.3093</Elem>
							<Elem>4.402902</Elem>
							<Elem>4.50547</Elem>
							<Elem>4.615464</Elem>
							<Elem>4.731236</Elem>
							<Elem>4.851048</Elem>
							<Elem>4.973101</Elem>
							<Elem>5.095564</Elem>
							<Elem>5.216598</Elem>
							<Elem>5.334384</Elem>
							<Elem>5.447154</Elem>
							<Elem>5.553213</Elem>
							<Elem>5.650966</Elem>
							<Elem>5.738945</Elem>
							<Elem>5.815825</Elem>
							<Elem>5.880451</Elem>
							<Elem>5.931849</Elem>
							<Elem>5.969245</Elem>
							<Elem>5.992075</Elem>
							<Elem>5.999995</Elem>
							<Elem>5.992882</Elem>
							<Elem>5.970841</Elem>
							<Elem>5.934203</Elem>
							<Elem>5.883516</Elem>
							<Elem>5.81954</Elem>
							<Elem>5.743236</Elem>
							<Elem>5.655749</Elem>
							<Elem>5.558394</Elem>
							<Elem>5.452635</Elem>
							<Elem>5.340061</Elem>
							<Elem>5.222365</Elem>
							<Elem>5.101317</Elem>
							<Elem>4.978739</Elem>
							<Elem>4.856475</Elem>
							<Elem>4.736367</Elem>
							<Elem>4.620221</Elem>
							<Elem>4.509787</Elem>
							<Elem>4.406729</Elem>
							<Elem>4.3126</Elem>
							<Elem>4.228818</Elem>
							<Elem>4.156646</Elem>
							<Elem>4.097173</Elem>
							<Elem>4.051296</Elem>
							<Elem>4.01971</Elem>
							<Elem>4.00289</Elem>
							<Elem>4.001094</Elem>
							<Elem>4.01435</Elem>
							<Elem>4.042459</Elem>
							<Elem>4.085002</Elem>
							<Elem>4.141338</Elem>
							<Elem>4.210621</Elem>
							<Elem>4.291806</Elem>
							<Elem>4.383673</Elem>
							<Elem>4.484838</Elem>
							<Elem>4.593775</Elem>
							<Elem>4.708844</Elem>
							<Elem>4.828309</Elem>
							<Elem>4.950369</Elem>
							<Elem>5.073184</Elem>
							<Elem>5.194901</Elem>
							<Elem>5.313682</Elem>
							<Elem>5.427735</Elem>
							<Elem>5.535339</Elem>
							<Elem>5.634868</Elem>
							<Elem>5.72482</Elem>
							<Elem>5.803834</Elem>
							<Elem>5.870717</Elem>
							<Elem>5.924457</Elem>
							<Elem>5.964242</Elem>
							<Elem>5.989467</Elem>
							<Elem>5.999751</Elem>
							<Elem>5.994936</Elem>
							<Elem>5.975093</Elem>
							<Elem>5.940519</Elem>
							<Elem>5.891734</Elem>
							<Elem>5.829475</Elem>
							<Elem>5.754678</Elem>
							<Elem>5.668474</Elem>
							<Elem>5.572164</Elem>
							<Elem>5.467201</Elem>
							<Elem>5.355171</Elem>
							<Elem>5.237767</Elem>
							<Elem>5.116763</Elem>
							<Elem>4.993988</Elem>
							<Elem>4.871299</Elem>
							<Elem>4.750549</Elem>
							<Elem>4.633568</Elem>
							<Elem>4.522123</Elem>
							<Elem>4.417902</Elem>
							<Elem>4.322482</Elem>
							<Elem>4.237309</Elem>
							<Elem>4.163671</Elem>
							<Elem>4.102687</Elem>
							<Elem>4.055279</Elem>
							<Elem>4.022167</Elem>
							<Elem>4.003855</Elem>
							<Elem>4.000622</Elem>
							<Elem>4.012519</Elem>
							<Elem>4.039367</Elem>
							<Elem>4.080763</Elem>
							<Elem>4.136081</Elem>
							<Elem>4.204485</Elem>
							<Elem>4.284942</Elem>
							<Elem>4.376233</Elem>
							<Elem>4.476979</Elem>
							<Elem>4.585653</Elem>
							<Elem>4.70061</Elem>
							<Elem>4.820109</Elem>
							<Elem>4.94234</Elem>
							<Elem>5.06545</Elem>
							<Elem>5.187574</Elem>
							<Elem>5.30686</Elem>
							<Elem>5.4215</Elem>
							<Elem>5.529754</Elem>
							<Elem>5.62998</Elem>
							<Elem>5.720658</Elem>
							<Elem>5.80041</Elem>
							<Elem>5.868026</Elem>
							<Elem>5.922479</Elem>
							<Elem>5.96294</Elem>
							<Elem>5.988794</Elem>
							<Elem>5.999647</Elem>
							<Elem>5.995331</Elem>
							<Elem>5.97591</Elem>
							<Elem>5.941677</Elem>
							<Elem>5.89315</Elem>
							<Elem>5.831063</Elem>
							<Elem>5.756356</Elem>
							<Elem>5.670163</Elem>
							<Elem>5.57379</Elem>
							<Elem>5.4687</Elem>
							<Elem>5.356487</Elem>
							<Elem>5.238855</Elem>
							<Elem>5.117589</Elem>
							<Elem>4.994531</Elem>
							<Elem>4.871551</Elem>
							<Elem>4.750516</Elem>
							<Elem>4.633267</Elem>
							<Elem>4.521586</Elem>
							<Elem>4.417171</Elem>
							<Elem>4.321609</Elem>
							<Elem>4.236355</Elem>
							<Elem>4.162705</Elem>
							<Elem>4.101782</Elem>
							<Elem>4.054514</Elem>
							<Elem>4.02162</Elem>
							<Elem>4.003604</Elem>
							<Elem>4.00074</Elem>
							<Elem>4.013076</Elem>
							<Elem>4.040425</Elem>
							<Elem>4.082373</Elem>
							<Elem>4.138285</Elem>
							<Elem>4.20731</Elem>
							<Elem>4.288402</Elem>
							<Elem>4.380326</Elem>
							<Elem>4.481686</Elem>
							<Elem>4.590941</Elem>
							<Elem>4.706427</Elem>
							<Elem>4.826388</Elem>
							<Elem>4.948998</Elem>
							<Elem>5.07239</Elem>
							<Elem>5.194685</Elem>
							<Elem>5.314021</Elem>
							<Elem>5.428579</Elem>
							<Elem>5.536614</Elem>
							<Elem>5.636479</Elem>
							<Elem>5.726652</Elem>
							<Elem>5.805758</Elem>
							<Elem>5.872588</Elem>
							<Elem>5.926124</Elem>
							<Elem>5.965547</Elem>
							<Elem>5.990255</Elem>
							<Elem>5.999869</Elem>
							<Elem>5.99424</Elem>
							<Elem>5.973453</Elem>
							<Elem>5.937821</Elem>
							<Elem>5.887887</Elem>
							<Elem>5.824409</Elem>
							<Elem>5.748355</Elem>
							<Elem>5.660882</Elem>
							<Elem>5.563323</Elem>
							<Elem>5.457166</Elem>
							<Elem>5.344029</Elem>
							<Elem>5.225637</Elem>
							<Elem>5.103797</Elem>
							<Elem>4.980366</Elem>
							<Elem>4.85723</Elem>
							<Elem>4.736268</Elem>
							<Elem>4.619326</Elem>
							<Elem>4.50819</Elem>
							<Elem>4.404559</Elem>
							<Elem>4.310016</Elem>
							<Elem>4.226006</Elem>
							<Elem>4.153813</Elem>
							<Elem>4.094541</Elem>
							<Elem>4.049099</Elem>
							<Elem>4.018181</Elem>
							<Elem>4.002263</Elem>
							<Elem>4.00159</Elem>
							<Elem>4.016174</Elem>
							<Elem>4.045793</Elem>
							<Elem>4.089999</Elem>
							<Elem>4.148116</Elem>
							<Elem>4.219259</Elem>
							<Elem>4.302341</Elem>
							<Elem>4.396093</Elem>
							<Elem>4.499085</Elem>
							<Elem>4.609741</Elem>
							<Elem>4.726371</Elem>
							<Elem>4.847192</Elem>
							<Elem>4.970356</Elem>
							<Elem>5.093978</Elem>
							<Elem>5.216169</Elem>
							<Elem>5.335057</Elem>
							<Elem>5.448824</Elem>
							<Elem>5.555727</Elem>
							<Elem>5.65413</Elem>
							<Elem>5.742524</Elem>
							<Elem>5.819556</Elem>
							<Elem>5.884045</Elem>
							<Elem>5.935002</Elem>
							<Elem>5.971644</Elem>
							<Elem>5.993408</Elem>
							<Elem>5.99996</Elem>
							<Elem>5.991196</Elem>
							<Elem>5.967249</Elem>
							<Elem>5.928484</Elem>
							<Elem>5.875492</Elem>
							<Elem>5.809083</Elem>
							<Elem>5.730274</Elem>
							<Elem>5.64027</Elem>
							<Elem>5.540449</Elem>
							<Elem>5.43234</Elem>
							<Elem>5.317598</Elem>
							<Elem>5.197983</Elem>
							<Elem>5.075327</Elem>
							<Elem>4.95151</Elem>
							<Elem>4.828431</Elem>
							<Elem>4.707978</Elem>
							<Elem>4.591998</Elem>
							<Elem>4.482271</Elem>
							<Elem>4.380481</Elem>
							<Elem>4.28819</Elem>
							<Elem>4.206817</Elem>
							<Elem>4.137611</Elem>
							<Elem>4.081635</Elem>
							<Elem>4.039751</Elem>
							<Elem>4.012604</Elem>
							<Elem>4.000611</Elem>
							<Elem>4.00396</Elem>
							<Elem>4.022601</Elem>
							<Elem>4.056249</Elem>
							<Elem>4.104391</Elem>
							<Elem>4.166288</Elem>
							<Elem>4.240993</Elem>
							<Elem>4.327359</Elem>
							<Elem>4.424062</Elem>
							<Elem>4.529617</Elem>
							<Elem>4.642403</Elem>
							<Elem>4.760689</Elem>
							<Elem>4.882658</Elem>
							<Elem>5.006435</Elem>
							<Elem>5.13012</Elem>
							<Elem>5.251809</Elem>
							<Elem>5.369634</Elem>
							<Elem>5.481781</Elem>
							<Elem>5.586526</Elem>
							<Elem>5.682257</Elem>
							<Elem>5.767501</Elem>
							<Elem>5.840945</Elem>
							<Elem>5.901459</Elem>
							<Elem>5.948108</Elem>
							<Elem>5.980175</Elem>
							<Elem>5.997164</Elem>
							<Elem>5.99881</Elem>
							<Elem>5.985088</Elem>
							<Elem>5.956205</Elem>
							<Elem>5.912605</Elem>
							<Elem>5.854956</Elem>
							<Elem>5.784144</Elem>
							<Elem>5.701257</Elem>
							<Elem>5.60757</Elem>
							<Elem>5.504524</Elem>
							<Elem>5.393704</Elem>
							<Elem>5.276816</Elem>
							<Elem>5.155659</Elem>
							<Elem>5.032099</Elem>
							<Elem>4.908039</Elem>
							<Elem>4.78539</Elem>
							<Elem>4.666042</Elem>
							<Elem>4.551834</Elem>
							<Elem>4.444528</Elem>
							<Elem>4.345777</Elem>
							<Elem>4.257106</Elem>
							<Elem>4.179881</Elem>
							<Elem>4.115295</Elem>
							<Elem>4.064346</Elem>
							<Elem>4.027821</Elem>
							<Elem>4.006286</Elem>
							<Elem>4.000073</Elem>
							<Elem>4.009282</Elem>
							<Elem>4.033772</Elem>
							<Elem>4.073167</Elem>
							<Elem>4.126862</Elem>
							<Elem>4.194031</Elem>
							<Elem>4.273639</Elem>
							<Elem>4.364459</Elem>
							<Elem>4.46509</Elem>
							<Elem>4.573982</Elem>
							<Elem>4.689455</Elem>
							<Elem>4.809726</Elem>
							<Elem>4.932941</Elem>
							<Elem>5.057196</Elem>
							<Elem>5.180574</Elem>
							<Elem>5.301169</Elem>
							<Elem>5.417119</Elem>
							<Elem>5.526631</Elem>
							<Elem>5.628013</Elem>
							<Elem>5.719699</Elem>
							<Elem>5.80027</Elem>
							<Elem>5.86848</Elem>
							<Elem>5.923273</Elem>
							<Elem>5.963801</Elem>
							<Elem>5.989435</Elem>
							<Elem>5.999778</Elem>
							<Elem>5.994667</Elem>
							<Elem>5.974178</Elem>
							<Elem>5.938628</Elem>
							<Elem>5.888563</Elem>
							<Elem>5.824756</Elem>
							<Elem>5.748191</Elem>
							<Elem>5.660052</Elem>
							<Elem>5.561699</Elem>
							<Elem>5.454652</Elem>
							<Elem>5.340567</Elem>
							<Elem>5.221208</Elem>
							<Elem>5.098421</Elem>
							<Elem>4.974105</Elem>
							<Elem>4.850184</Elem>
							<Elem>4.728576</Elem>
							<Elem>4.611165</Elem>
							<Elem>4.499767</Elem>
							<Elem>4.396108</Elem>
							<Elem>4.301795</Elem>
							<Elem>4.218289</Elem>
							<Elem>4.146884</Elem>
							<Elem>4.088689</Elem>
							<Elem>4.044605</Elem>
							<Elem>4.015319</Elem>
							<Elem>4.001286</Elem>
							<Elem>4.002725</Elem>
							<Elem>4.019615</Elem>
							<Elem>4.051699</Elem>
							<Elem>4.098479</Elem>
							<Elem>4.159234</Elem>
							<Elem>4.233023</Elem>
							<Elem>4.318705</Elem>
							<Elem>4.414952</Elem>
							<Elem>4.520274</Elem>
							<Elem>4.633039</Elem>
							<Elem>4.7515</Elem>
							<Elem>4.87382</Elem>
							<Elem>4.998103</Elem>
							<Elem>5.12242</Elem>
							<Elem>5.244844</Elem>
							<Elem>5.363476</Elem>
							<Elem>5.476473</Elem>
							<Elem>5.582082</Elem>
							<Elem>5.678663</Elem>
							<Elem>5.764715</Elem>
							<Elem>5.838903</Elem>
							<Elem>5.900072</Elem>
							<Elem>5.947272</Elem>
							<Elem>5.979767</Elem>
							<Elem>5.997051</Elem>
							<Elem>5.998854</Elem>
							<Elem>5.985146</Elem>
							<Elem>5.956136</Elem>
							<Elem>5.912275</Elem>
							<Elem>5.854241</Elem>
							<Elem>5.782933</Elem>
							<Elem>5.699459</Elem>
							<Elem>5.605113</Elem>
							<Elem>5.501359</Elem>
							<Elem>5.389809</Elem>
							<Elem>5.272196</Elem>
							<Elem>5.150347</Elem>
							<Elem>5.026155</Elem>
							<Elem>4.901551</Elem>
							<Elem>4.778472</Elem>
							<Elem>4.658832</Elem>
							<Elem>4.544492</Elem>
							<Elem>4.437231</Elem>
							<Elem>4.338717</Elem>
							<Elem>4.250486</Elem>
							<Elem>4.17391</Elem>
							<Elem>4.110182</Elem>
							<Elem>4.060296</Elem>
							<Elem>4.02503</Elem>
							<Elem>4.004934</Elem>
							<Elem>4.000324</Elem>
							<Elem>4.011273</Elem>
							<Elem>4.037613</Elem>
							<Elem>4.078936</Elem>
							<Elem>4.134601</Elem>
							<Elem>4.203742</Elem>
							<Elem>4.285286</Elem>
							<Elem>4.377964</Elem>
							<Elem>4.480333</Elem>
							<Elem>4.590802</Elem>
							<Elem>4.707649</Elem>
							<Elem>4.829056</Elem>
							<Elem>4.953132</Elem>
							<Elem>5.077944</Elem>
							<Elem>5.201547</Elem>
							<Elem>5.322015</Elem>
							<Elem>5.437469</Elem>
							<Elem>5.546109</Elem>
							<Elem>5.646241</Elem>
							<Elem>5.736303</Elem>
							<Elem>5.81489</Elem>
							<Elem>5.880773</Elem>
							<Elem>5.932924</Elem>
							<Elem>5.970529</Elem>
							<Elem>5.992998</Elem>
							<Elem>5.999978</Elem>
							<Elem>5.99136</Elem>
							<Elem>5.967275</Elem>
							<Elem>5.928097</Elem>
							<Elem>5.874435</Elem>
							<Elem>5.807125</Elem>
							<Elem>5.727215</Elem>
							<Elem>5.635951</Elem>
							<Elem>5.534756</Elem>
							<Elem>5.425208</Elem>
							<Elem>5.309017</Elem>
							<Elem>5.187996</Elem>
							<Elem>5.064033</Elem>
							<Elem>4.939065</Elem>
							<Elem>4.815044</Elem>
							<Elem>4.693905</Elem>
							<Elem>4.577543</Elem>
							<Elem>4.467775</Elem>
							<Elem>4.366317</Elem>
							<Elem>4.274756</Elem>
							<Elem>4.194525</Elem>
							<Elem>4.126877</Elem>
							<Elem>4.072873</Elem>
							<Elem>4.033358</Elem>
							<Elem>4.008952</Elem>
							<Elem>4.000039</Elem>
							<Elem>4.006759</Elem>
							<Elem>4.029011</Elem>
							<Elem>4.066448</Elem>
							<Elem>4.118486</Elem>
							<Elem>4.184314</Elem>
							<Elem>4.262905</Elem>
							<Elem>4.353029</Elem>
							<Elem>4.45328</Elem>
							<Elem>4.562089</Elem>
							<Elem>4.677755</Elem>
							<Elem>4.798469</Elem>
							<Elem>4.922343</Elem>
							<Elem>5.047438</Elem>
							<Elem>5.171796</Elem>
							<Elem>5.29347</Elem>
							<Elem>5.410555</Elem>
							<Elem>5.521217</Elem>
							<Elem>5.623722</Elem>
							<Elem>5.716464</Elem>
							<Elem>5.797989</Elem>
							<Elem>5.867018</Elem>
							<Elem>5.922469</Elem>
							<Elem>5.963471</Elem>
							<Elem>5.98938</Elem>
							<Elem>5.999788</Elem>
							<Elem>5.994529</Elem>
							<Elem>5.973683</Elem>
							<Elem>5.937576</Elem>
							<Elem>5.886772</Elem>
							<Elem>5.822064</Elem>
							<Elem>5.744465</Elem>
							<Elem>5.655191</Elem>
							<Elem>5.555639</Elem>
							<Elem>5.447369</Elem>
							<Elem>5.332079</Elem>
							<Elem>5.211575</Elem>
							<Elem>5.087746</Elem>
							<Elem>4.962536</Elem>
							<Elem>4.837907</Elem>
							<Elem>4.715816</Elem>
							<Elem>4.59818</Elem>
							<Elem>4.486843</Elem>
							<Elem>4.383555</Elem>
							<Elem>4.289938</Elem>
							<Elem>4.207463</Elem>
							<Elem>4.137426</Elem>
							<Elem>4.080928</Elem>
							<Elem>4.038859</Elem>
							<Elem>4.01188</Elem>
							<Elem>4.000417</Elem>
							<Elem>4.004654</Elem>
							<Elem>4.024524</Elem>
							<Elem>4.059718</Elem>
							<Elem>4.109686</Elem>
							<Elem>4.173644</Elem>
							<Elem>4.250589</Elem>
							<Elem>4.339314</Elem>
							<Elem>4.438426</Elem>
							<Elem>4.546369</Elem>
							<Elem>4.661447</Elem>
							<Elem>4.781852</Elem>
							<Elem>4.905692</Elem>
							<Elem>5.03102</Elem>
							<Elem>5.155866</Elem>
							<Elem>5.278267</Elem>
							<Elem>5.396297</Elem>
							<Elem>5.508099</Elem>
							<Elem>5.611914</Elem>
							<Elem>5.706107</Elem>
							<Elem>5.789196</Elem>
							<Elem>5.859871</Elem>
							<Elem>5.91702</Elem>
							<Elem>5.959739</Elem>
							<Elem>5.987356</Elem>
							<Elem>5.999434</Elem>
							<Elem>5.99578</Elem>
							<Elem>5.97645</Elem>
							<Elem>5.941746</Elem>
							<Elem>5.892212</Elem>
							<Elem>5.828627</Elem>
							<Elem>5.751989</Elem>
							<Elem>5.663505</Elem>
							<Elem>5.564566</Elem>
							<Elem>5.456729</Elem>
							<Elem>5.341692</Elem>
							<Elem>5.221267</Elem>
							<Elem>5.097349</Elem>
							<Elem>4.971892</Elem>
							<Elem>4.846873</Elem>
							<Elem>4.724261</Elem>
							<Elem>4.60599</Elem>
							<Elem>4.493925</Elem>
							<Elem>4.389833</Elem>
							<Elem>4.295357</Elem>
							<Elem>4.211987</Elem>
							<Elem>4.14104</Elem>
							<Elem>4.083636</Elem>
							<Elem>4.040683</Elem>
							<Elem>4.01286</Elem>
							<Elem>4.000608</Elem>
							<Elem>4.004122</Elem>
							<Elem>4.023349</Elem>
							<Elem>4.057988</Elem>
							<Elem>4.107494</Elem>
							<Elem>4.171087</Elem>
							<Elem>4.247767</Elem>
							<Elem>4.336325</Elem>
							<Elem>4.435363</Elem>
							<Elem>4.54332</Elem>
							<Elem>4.658492</Elem>
							<Elem>4.779063</Elem>
							<Elem>4.903128</Elem>
							<Elem>5.028728</Elem>
							<Elem>5.15388</Elem>
							<Elem>5.276607</Elem>
							<Elem>5.39497</Elem>
							<Elem>5.507097</Elem>
							<Elem>5.611218</Elem>
							<Elem>5.705685</Elem>
							<Elem>5.789003</Elem>
							<Elem>5.859855</Elem>
							<Elem>5.91712</Elem>
							<Elem>5.959889</Elem>
							<Elem>5.987485</Elem>
							<Elem>5.99947</Elem>
							<Elem>5.995652</Elem>
							<Elem>5.976089</Elem>
							<Elem>5.941089</Elem>
							<Elem>5.891203</Elem>
							<Elem>5.827217</Elem>
							<Elem>5.750143</Elem>
							<Elem>5.661199</Elem>
							<Elem>5.561788</Elem>
							<Elem>5.453484</Elem>
							<Elem>5.337999</Elem>
							<Elem>5.217159</Elem>
							<Elem>5.092877</Elem>
							<Elem>4.967119</Elem>
							<Elem>4.841877</Elem>
							<Elem>4.719131</Elem>
							<Elem>4.600828</Elem>
							<Elem>4.48884</Elem>
							<Elem>4.384942</Elem>
							<Elem>4.29078</Elem>
							<Elem>4.207847</Elem>
							<Elem>4.137458</Elem>
							<Elem>4.08073</Elem>
							<Elem>4.038564</Elem>
							<Elem>4.01163</Elem>
							<Elem>4.000356</Elem>
							<Elem>4.004924</Elem>
							<Elem>4.025262</Elem>
							<Elem>4.061052</Elem>
							<Elem>4.111726</Elem>
							<Elem>4.176485</Elem>
							<Elem>4.254303</Elem>
							<Elem>4.343949</Elem>
							<Elem>4.444002</Elem>
							<Elem>4.552876</Elem>
							<Elem>4.668847</Elem>
							<Elem>4.790076</Elem>
							<Elem>4.91464</Elem>
							<Elem>5.040564</Elem>
							<Elem>5.16585</Elem>
							<Elem>5.28851</Elem>
							<Elem>5.406598</Elem>
							<Elem>5.518237</Elem>
							<Elem>5.621657</Elem>
							<Elem>5.715213</Elem>
							<Elem>5.79742</Elem>
							<Elem>5.866971</Elem>
							<Elem>5.92276</Elem>
							<Elem>5.963899</Elem>
							<Elem>5.989733</Elem>
							<Elem>5.99985</Elem>
							<Elem>5.994087</Elem>
							<Elem>5.972533</Elem>
							<Elem>5.935528</Elem>
							<Elem>5.883659</Elem>
							<Elem>5.817748</Elem>
							<Elem>5.738839</Elem>
							<Elem>5.648186</Elem>
							<Elem>5.547227</Elem>
							<Elem>5.437565</Elem>
							<Elem>5.320944</Elem>
							<Elem>5.199215</Elem>
							<Elem>5.074313</Elem>
							<Elem>4.948224</Elem>
							<Elem>4.822953</Elem>
							<Elem>4.700492</Elem>
							<Elem>4.582789</Elem>
							<Elem>4.471717</Elem>
							<Elem>4.369043</Elem>
							<Elem>4.276402</Elem>
							<Elem>4.19527</Elem>
							<Elem>4.126938</Elem>
							<Elem>4.072497</Elem>
							<Elem>4.032813</Elem>
							<Elem>4.008521</Elem>
							<Elem>4.00001</Elem>
							<Elem>4.007416</Elem>
							<Elem>4.030625</Elem>
							<Elem>4.069269</Elem>
						</DoubleArray>
					</Property>
					<Property Name="Interpolate">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Rate">
						<Double>1</Double>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/TestAlarmAPI/TestAlarmAPI.nivsproj sha256=671d312a7c083e24199336757af5af8204384fe6b8796caab5b22ed29cfc4059 bytes=10974 -->
## FILE: tests/testutilities/legacy_files/TestAlarmAPI/TestAlarmAPI.nivsproj

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/TestAlarmAPI/TestAlarmAPI.nivsproj`
- sha256: `671d312a7c083e24199336757af5af8204384fe6b8796caab5b22ed29cfc4059`
- bytes: 10974

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2012" Minor="0" Fix="0" Build="1" />
	<Content>Definition</Content>
	<Root Name="TestAlarmAPI" TypeGUID="d9313aae-3554-45e5-93f3-86454275d4f2">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>TestAlarmAPI</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.0</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3351079554.3776822</Double>
			</Property>
		</Properties>
		<Errors />
		<Section Name="System Definition File" TypeGUID="b9227a5b-2770-4a62-8621-ac414d4124fb">
			<Description />
			<Properties />
			<Errors />
			<Section Name="TestAlarmAPI.nivssdf" TypeGUID="3a41ca74-36ec-4aff-9219-9d05c8f91208">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="TestAlarmAPI.nivssdf">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5>36ad9bc139b43e0600c21b00b2c96772</MD5>
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
						<DependentFile Type="Relative" Path="TestAlarmAPI.nivsscreen">
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
			<Section Name="TestAlarmAPI.nivssdf [C:\Users\Public\Documents\National Instruments\NI VeriStand 2011\Projects\TestAlarmAPI\TestAlarmAPI.nivssdf]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2011\Projects\TestAlarmAPI\TestAlarmAPI.nivssdf</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="TestAlarmAPI.nivsscreen [C:\Users\Public\Documents\National Instruments\NI VeriStand 2011\Projects\TestAlarmAPI\TestAlarmAPI.nivsscreen]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2011\Projects\TestAlarmAPI\TestAlarmAPI.nivsscreen</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/TestAlarmAPI/TestAlarmAPI.nivsscreen sha256=955fa42287813ff6bde93f9d16f4345efb18bb9a48107c68c7588e99258074ee bytes=4128 -->
## FILE: tests/testutilities/legacy_files/TestAlarmAPI/TestAlarmAPI.nivsscreen

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/TestAlarmAPI/TestAlarmAPI.nivsscreen`
- sha256: `955fa42287813ff6bde93f9d16f4345efb18bb9a48107c68c7588e99258074ee`
- bytes: 4128

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
					<Data>AAAIlgkAgAAAAABYABRAMP////8LVGVtcGxhdGUgVkkAEUADAApQb3NpdGlvbiBYAAARQAMAClBvc2l0aW9uIFkAABBAMP////8GQ3VzdG9tAAAUQCEOU2hvdyBUaXRsZSBCYXIAAAlAAwACSUQAABJAIQ1BbHdheXMgT24gVG9wABJAIQxBbGxvdyBSZXNpemUAABRAIQ5BbGxvdyBNaW5pbWl6ZQAAEEAhC0FsbG93IENsb3NlABRAIQ5TaXplIHRvIFNjcmVlbgAAD0ADAAlTY3JlZW4uSUQAGUAWAAIGTm9ybWFsA05ldwAABVN0YXRlAA5AMP////8FVGl0bGUACUACAANbMF0ACUACAANbMV0ACUACAANbMl0ACUACAANbM10AHEBQAAQADgAPABAAEQ1XaW5kb3cgQm91bmRzABFACAALQ2hhbm5lbCBSZWYADkAw/////wRVbml0AAAUQCEORGVmYXVsdCBVbml0cz8AABJAIQxGbGFzaCBMaW1pdD8AAA1ABwAHQ29sb3IgMQANQAcAB0NvbG9yIDIADUAHAAdDb2xvciAzAA1ABwAHQ29sb3IgNAAPQAcACUJjayBDb2xvcgARQAcACkZvcmUgQ29sb3IAAA1ACgAHTGltaXQgMQANQAoAB0xpbWl0IDIADUAKAAdMaW1pdCAzAA1ACgAHTGltaXQgNAATQAMADExpbWl0IE1vZGUgMQAAE0ADAAxMaW1pdCBNb2RlIDIAABNAAwAMTGltaXQgTW9kZSAzAAATQAMADExpbWl0IE1vZGUgNAAAFUADAA9TY2FsZSBQcmVjaXNpb24AD0AKAAlTY2FsZSBNaW4AD0AKAAlTY2FsZSBNYXgADUADAAZGb3JtYXQAAA9AAwAJUHJlY2lzaW9uABVAAwAPQmFja2dyb3VuZCBUeXBlABFAAwALVmFyaWFibGUgSUQAEEBAAAH/////ACsDSURzABRAMP////8LVmFyaWFibGUgSUQAEkBAAAH/////AC0FVW5pdHMAFEBAAAH/////AC0GTGFiZWxzAAATQAoADFNjYWxlIEZhY3RvcgAAE0AKAAxTY2FsZSBPZmZzZXQAABFABwALVmFyaWFibGUgSUQAGkBAAAH/////ADIMWVNjYWxlIEluZGV4AAANQAUABkZvcm1hdAAAD0AFAAlQcmVjaXNpb24ACUAFAANGaXQADkAw/////wVMYWJlbAAWQCERVXNlIERlZmF1bHQgTGFiZWwAEkAhDUxhYmVsIFZpc2libGUACUAKAANNaW4ACUAKAANNYXgASwDxAAAAAAAAAAEgY2x1c3Rlcl9HcmFwaCBTY2FsZSBTZXR0aW5ncy5jdGwAIkBQAAgANAA1ADYANwA4ADkAOgA7BlhTY2FsZQAAFEBAAAH/////ADwHWVNjYWxlcwAPQAUACUJhciBTdHlsZQANQAIAB0ZpbGwgVG8AE0AHAAxGaWxsL1B0Q29sb3IAABFABQAKTGluZSBTdHlsZQAAEUAFAApMaW5lIFdpZHRoAAALQAcABUNvbG9yAA1ABQAGSW50ZXJwAAARQAUAC1BvaW50IFN0eWxlAEgA8QAAAAAAAAABH2NsdXN0ZXJfR3JhcGggUGxvdCBTZXR0aW5ncy5jdGwAIEBQAAgAPgA/AEAAQQBCAEMARABFBFBsb3QAABJAQAAB/////wBGBVBsb3RzABNACgANVXBkYXRlIFBlcmlvZAAVQAoADkhpc3RvcnkgTGVuZ3RoAAAUQHAACAAAAAIAAAZNeS5SZWYAABBAIQtJcyBDb250cm9sPwAWQDD/////DENoYW5uZWwgUGF0aAAAGkBAAAH/////AEwNQ2hhbm5lbCBQYXRocwAQQFMLQ3VzdG9tIERhdGEAqwDxxieWWAAAAAEgY2x1c3Rlcl9TY3JlZW4gSXRlbSBTZXR0aW5ncy5jdGwAgkBQADYAAAABAAIAAwAEAAUABgAHAAgACQAKAAsADAANABIAEwAUABUAFgAXABgAGQAaABsAHAAdAB4AHwAgACEAIgAjACQAJQAmACcAKAApACoALAAuAC8AMAAxADMAPAA9AEcASABJAEoASwBNAE4LU2NyZWVuIEl0ZW0AEkBAAAH/////AE8FSXRlbXMADkAw/////wROYW1lAAAUQDD/////C0Rlc2NyaXB0aW9uAVMA8QAAAAAAAAABH2VudW1fVXNlciBBZG1pbiBQZXJtaXNzaW9ucy5jdGwBK0AWAA0HRGVmYXVsdA5BZG1pbmlzdHJhdGlvbhdDaGFubmVsIFNjYWxpbmcgVXRpbGl0eRFBZGQgRGlzcGxheSBJdGVtcxNDaGFuZ2UgVXNlciBQcm9maWxlI0VkaXQgU3RpbXVsdXMgUHJvZmlsZSBFZGl0b3IgSGVhZGVyGkVkaXQgRGlzcGxheSBJdGVtIFNldHRpbmdzG01vZGVsIFBhcmFtZXRlciBDYWxpYnJhdGlvbhJSdW50aW1lIEFsYXJtIEVkaXQPRWRpdCBUb29scyBNZW51FkVkaXQgRW5naW5lIENvbXBvbmVudHMaQ29uZmlndXJlIFZpc2libGUgQ2hhbm5lbHMNRmF1bHQgTWFuYWdlcgAAClBlcm1pc3Npb24AAAxAIQdMb2FkZWQ/ABRAIQ9BbHdheXMgVmlzaWJsZT8AVwDxAAAAAAAAAAEkY2x1c3Rlcl9FbnRpcmUgU2NyZWVuIERlZmluaXRpb24uY3RsACpAUAAKAFAAUQBSAAUAAQACAAYAUwBUAFULU2NyZWVuLkRhdGEAJkBAAAH/////AFYZU2NyZWVuIEl0ZW0gQ2x1c3RlciBBcnJheQABAFcAAAABAAAAAAAAAAxFbXB0eSBTY3JlZW4AAAAAAAAdWgAAAAAAAAAAAAAAAQAAAAAA</Data>
				</Variant>
			</Property>
			<Property Name="Screen Order">
				<I32Array>
					<Elem>7514</Elem>
				</I32Array>
			</Property>
			<Property Name="EscapeEnabled">
				<Boolean>false</Boolean>
			</Property>
			<Property Name="ShowPropPageOnDrop">
				<Boolean>true</Boolean>
			</Property>
			<Property Name="Workspace Loc and Size Left">
				<U16>529</U16>
			</Property>
			<Property Name="Workspace Loc and Size Top">
				<U16>268</U16>
			</Property>
			<Property Name="Workspace Loc and Size Right">
				<U16>1341</U16>
			</Property>
			<Property Name="Workspace Loc and Size Bottom">
				<U16>928</U16>
			</Property>
		</Properties>
		<Errors />
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/TestAlarmAPI/TestAlarmAPI.nivssdf sha256=fed5c3cb2bf74972b21109797ce5a947276c02781178f6861fa279d3da51b33f bytes=145939 -->
## FILE: tests/testutilities/legacy_files/TestAlarmAPI/TestAlarmAPI.nivssdf

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/TestAlarmAPI/TestAlarmAPI.nivssdf`
- sha256: `fed5c3cb2bf74972b21109797ce5a947276c02781178f6861fa279d3da51b33f`
- bytes: 145939

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2011" Minor="0" Fix="0" Build="0" />
	<Content>Definition</Content>
	<Root Name="TestAlarmAPI" TypeGUID="03D3BA22-1485-13A6-56BD17DA950CCD00">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>TestAlarmAPI</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.37</String>
			</Property>
			<Property Name="Creator">
				<String>Administrator</String>
			</Property>
			<Property Name="Creation Date">
				<Double>3324641639.21875</Double>
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
					<Property Name="TL sleep time">
						<U32>0</U32>
					</Property>
					<Property Name="TS_Custom_Dev">
						<String />
					</Property>
					<Property Name="ctr decimation">
						<U32>1</U32>
					</Property>
					<Property Name="custom loop time">
						<U32>0</U32>
					</Property>
					<Property Name="daq">
						<Variant>
							<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
							<Data>AAAAYwkAgAAAAAADABRAMP////8KREFRIERldmljZQAAJ0AHACBQcmltYXJ5IENvbnRyb2wgTG9vcCByYXRlICh1c2VjKQAAEEBQAAIAAAABBGRhdGEAAAEAAgAAAAAAACcQAAAAAA==</Data>
						</Variant>
					</Property>
					<Property Name="daq timeout">
						<U32>1000</U32>
					</Property>
					<Property Name="dio decimation">
						<U32>1</U32>
					</Property>
					<Property Name="loop time">
						<U32>10000</U32>
					</Property>
					<Property Name="name">
						<String />
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
					<Section Name="ConstantBoundAlarm" TypeGUID="03D3B791-1485-13A6-56D2B019287A4256">
						<Description />
						<Properties>
							<Property Name="Audio File">
								<DependentFile Type="Absolute" Path="">
									<Version />
									<RTDestination />
									<SupportedTarget />
									<MD5 />
								</DependentFile>
							</Property>
							<Property Name="Channel Path">
								<DependentNode Path="Targets Section/Controller/User Channel/AlarmChannel2" />
							</Property>
							<Property Name="Delay">
								<Double>0</Double>
							</Property>
							<Property Name="Disabled Color">
								<U32>9868950</U32>
							</Property>
							<Property Name="High Limit">
								<Double>5</Double>
							</Property>
							<Property Name="High Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="ID">
								<U32>245104</U32>
							</Property>
							<Property Name="Log Trips">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="Low Limit">
								<Double>-5</Double>
							</Property>
							<Property Name="Low Limit Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Normal Color">
								<U32>6618880</U32>
							</Property>
							<Property Name="Priority">
								<U32>15</U32>
							</Property>
							<Property Name="Procedure Path">
								<DependentNode Path="Targets Section/Controller/Procedures/ResetAlarmTest2" />
							</Property>
							<Property Name="State">
								<U32>1</U32>
							</Property>
							<Property Name="Trip Color">
								<U32>16711680</U32>
							</Property>
							<Property Name="Trip Message">
								<String />
							</Property>
							<Property Name="Group Number">
								<U32>0</U32>
							</Property>
						</Properties>
						<Errors />
					</Section>
					<Section Name="Alarm Group" TypeGUID="76AFF34A-9374-FCEB-1E7E-EE1084A48EF5">
						<Description />
						<Properties />
						<Errors />
						<Section Name="AlarmTest2" TypeGUID="03D3B791-1485-13A6-56D2B019287A4256">
							<Description />
							<Properties>
								<Property Name="Delay">
									<Double>0</Double>
								</Property>
								<Property Name="Priority">
									<U32>15</U32>
								</Property>
								<Property Name="State">
									<U32>0</U32>
								</Property>
								<Property Name="Mode">
									<U32>0</U32>
								</Property>
								<Property Name="Channel Path">
									<DependentNode Path="Targets Section/Controller/User Channel/AlarmChannel2" />
								</Property>
								<Property Name="High Limit Mode">
									<U32>0</U32>
								</Property>
								<Property Name="High Limit">
									<Double>5</Double>
								</Property>
								<Property Name="Low Limit Mode">
									<U32>0</U32>
								</Property>
								<Property Name="Low Limit">
									<Double>-5</Double>
								</Property>
								<Property Name="Procedure Path">
									<DependentNode Path="Targets Section/Controller/Procedures/ResetAlarmTest3" />
								</Property>
								<Property Name="Group Number">
									<U32>1</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="AlarmTest1" TypeGUID="03D3B791-1485-13A6-56D2B019287A4256">
							<Description />
							<Properties>
								<Property Name="Audio File">
									<DependentFile Type="Absolute" Path="">
										<Version />
										<RTDestination />
										<SupportedTarget />
										<MD5 />
									</DependentFile>
								</Property>
								<Property Name="Channel Path">
									<DependentNode Path="Targets Section/Controller/User Channel/AlarmChannel1" />
								</Property>
								<Property Name="Delay">
									<Double>0.5</Double>
								</Property>
								<Property Name="Disabled Color">
									<U32>9868950</U32>
								</Property>
								<Property Name="High Limit">
									<Double>0</Double>
								</Property>
								<Property Name="High Limit Channel Path">
									<DependentNode Path="Targets Section/Controller/User Channel/AlarmChannel1High" />
								</Property>
								<Property Name="High Limit Mode">
									<U32>1</U32>
								</Property>
								<Property Name="ID">
									<U32>256209</U32>
								</Property>
								<Property Name="Log Trips">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Low Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Low Limit Channel Path">
									<DependentNode Path="Targets Section/Controller/User Channel/AlarmChannel1Low" />
								</Property>
								<Property Name="Low Limit Mode">
									<U32>1</U32>
								</Property>
								<Property Name="Mode">
									<U32>0</U32>
								</Property>
								<Property Name="Normal Color">
									<U32>6618880</U32>
								</Property>
								<Property Name="Priority">
									<U32>5</U32>
								</Property>
								<Property Name="Procedure Path">
									<DependentNode Path="Targets Section/Controller/Procedures/ResetAlarmTest1" />
								</Property>
								<Property Name="State">
									<U32>1</U32>
								</Property>
								<Property Name="Trip Color">
									<U32>16711680</U32>
								</Property>
								<Property Name="Trip Message">
									<String />
								</Property>
								<Property Name="Group Number">
									<U32>1</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
					</Section>
				</Section>
				<Section Name="Procedures" TypeGUID="03D3B7B1-1485-13A6-56649C7783203F22">
					<Description />
					<Properties />
					<Errors />
					<Section Name="ResetAlarmTest1" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>844023</U32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Dwell" TypeGUID="6dde8411-8c68-408b-8558-d18c0909c789">
							<Description />
							<Properties>
								<Property Name="Command.Value">
									<Double>20</Double>
								</Property>
								<Property Name="Command.Mode">
									<U32>0</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Reset Alarm &amp; Exit Subroutine" TypeGUID="e203af68-4b16-4bae-a211-7502c28a5642">
							<Description />
							<Properties>
								<Property Name="Command.Priority">
									<U32>25</U32>
								</Property>
								<Property Name="Command.Default State">
									<I32>0</I32>
								</Property>
								<Property Name="Command.Delay">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Upper Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Lower Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<I32>4</I32>
								</Property>
								<Property Name="Command.UL Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.LL Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Alarm">
									<DependentNode Path="Targets Section/Controller/Alarms/Alarm Group/AlarmTest1" />
								</Property>
							</Properties>
							<Errors />
						</Section>
					</Section>
					<Section Name="ResetAlarmTest2" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>834632</U32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Dwell" TypeGUID="6dde8411-8c68-408b-8558-d18c0909c789">
							<Description />
							<Properties>
								<Property Name="Command.Value">
									<Double>25</Double>
								</Property>
								<Property Name="Command.Mode">
									<U32>0</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Enable AlarmTest2" TypeGUID="e203af68-4b16-4bae-a211-7502c28a5642">
							<Description />
							<Properties>
								<Property Name="Command.Priority">
									<U32>15</U32>
								</Property>
								<Property Name="Command.Default State">
									<I32>1</I32>
								</Property>
								<Property Name="Command.Delay">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Upper Limit">
									<Double>5</Double>
								</Property>
								<Property Name="Command.Lower Limit">
									<Double>-5</Double>
								</Property>
								<Property Name="Command.Function">
									<I32>0</I32>
								</Property>
								<Property Name="Command.UL Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.LL Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Watch Channel">
									<DependentNode Path="Targets Section/Controller/User Channel/AlarmChannel2" />
								</Property>
								<Property Name="Procedure">
									<DependentNode Path="Targets Section/Controller/Procedures/ResetAlarmTest3" />
								</Property>
								<Property Name="Alarm">
									<DependentNode Path="Targets Section/Controller/Alarms/Alarm Group/AlarmTest2" />
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="Reset ConstantBoundAlarm &amp; Exit Subroutine" TypeGUID="e203af68-4b16-4bae-a211-7502c28a5642">
							<Description />
							<Properties>
								<Property Name="Command.Priority">
									<U32>25</U32>
								</Property>
								<Property Name="Command.Default State">
									<I32>0</I32>
								</Property>
								<Property Name="Command.Delay">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Upper Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Lower Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<I32>4</I32>
								</Property>
								<Property Name="Command.UL Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Command.LL Const">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="Alarm">
									<DependentNode Path="Targets Section/Controller/Alarms/ConstantBoundAlarm" />
								</Property>
							</Properties>
							<Errors />
						</Section>
					</Section>
					<Section Name="ResetAlarmTest3" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description />
						<Properties />
						<Errors />
						<Section Name="Reset Alarm &amp; Exit Subroutine" TypeGUID="e203af68-4b16-4bae-a211-7502c28a5642">
							<Description />
							<Properties>
								<Property Name="Command.Priority">
									<U32>0</U32>
								</Property>
								<Property Name="Command.Default State">
									<I32>1</I32>
								</Property>
								<Property Name="Command.Delay">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Upper Limit">
									<Double>1</Double>
								</Property>
								<Property Name="Command.Lower Limit">
									<Double>0</Double>
								</Property>
								<Property Name="Command.Function">
									<I32>4</I32>
								</Property>
								<Property Name="Command.UL Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Command.LL Const">
									<Boolean>true</Boolean>
								</Property>
								<Property Name="Alarm">
									<DependentNode Path="Targets Section/Controller/Alarms/Alarm Group/AlarmTest2" />
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
				<Section Name="User Channel" TypeGUID="03D3B6B7-1485-13A6-567BE1E1E0DF999A">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="AlarmChannel1" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
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
					<Channel Name="AlarmChannel1High" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>2</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>10</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="AlarmChannel1Low" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>3</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-10</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="AlarmChannel2" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>4</U32>
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
								<U32>5</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>12234</Elem>
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
			<Alias Name="AlarmChannel1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/AlarmChannel1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="AlarmChannel1High" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/AlarmChannel1High" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="AlarmChannel1Low" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/AlarmChannel1Low" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="AlarmChannel2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/AlarmChannel2" />
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

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/TestModelAPI/ParameterValues.txt sha256=b92d3ffa77ba0e1b65efd7dd6356dd1000d415cfee218e1d311fc0ca2fea09a3 bytes=69 -->
## FILE: tests/testutilities/legacy_files/TestModelAPI/ParameterValues.txt

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/TestModelAPI/ParameterValues.txt`
- sha256: `b92d3ffa77ba0e1b65efd7dd6356dd1000d415cfee218e1d311fc0ca2fea09a3`
- bytes: 69

````text
Gain_1x1	15
Gain_10x1	[1; 2; 3; 4; 5; 6; 7; 8; 9; 10]
Offset_1x1	20
````
