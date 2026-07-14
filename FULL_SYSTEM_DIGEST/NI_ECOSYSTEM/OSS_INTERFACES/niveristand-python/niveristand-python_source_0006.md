# NI OSS SOURCE SNAPSHOT: niveristand-python

<!--NI_OSS_SNAPSHOT repo=ni/niveristand-python commit=9ced536d3414f04a8b6b9315ce4c71b879d02a96 -->

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/CalcChanLatchTest/CalcChanLatchTest.nivssdf sha256=789292fc485f3e85a36cb58a997339e55e795e2eb680bb88e1513a602beef924 bytes=147694 -->
## FILE: tests/testutilities/legacy_files/CalcChanLatchTest/CalcChanLatchTest.nivssdf

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/CalcChanLatchTest/CalcChanLatchTest.nivssdf`
- sha256: `789292fc485f3e85a36cb58a997339e55e795e2eb680bb88e1513a602beef924`
- bytes: 147694

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2012" Minor="0" Fix="0" Build="9" />
	<Content>Definition</Content>
	<Root Name="CalcChanLatchTest" TypeGUID="03D3BA22-1485-13A6-56BD17DA950CCD00">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>CalcChanLatchTest</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.97</String>
			</Property>
			<Property Name="Creator">
				<String>Administrator</String>
			</Property>
			<Property Name="Creation Date">
				<Double>3318358984.5011888</Double>
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
						<Double>0</Double>
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
						<I32>0</I32>
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
						<Double>10</Double>
					</Property>
					<Property Name="Execution Mode">
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
					<Property Name="dio decimation">
						<U32>1</U32>
					</Property>
					<Property Name="loop time">
						<U32>100000</U32>
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
						<Double>10</Double>
					</Property>
				</Properties>
				<Errors />
				<Section Name="System Variables" TypeGUID="03D3B753-1485-13A6-56B10ED0820CF410">
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
							<U32>0</U32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Procedures" TypeGUID="03D3B7B1-1485-13A6-56649C7783203F22">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Main" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description />
						<Properties />
						<Errors />
						<Section Name="Dwell" TypeGUID="6dde8411-8c68-408b-8558-d18c0909c789">
							<Description />
							<Properties>
								<Property Name="Command.Value">
									<Double>1</Double>
								</Property>
								<Property Name="Command.Mode">
									<U32>0</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="End of Main" TypeGUID="b485fef3-012c-4c9e-acdb-c204000d11e5">
							<Description />
							<Properties>
								<Property Name="Goto Label">
									<DependentNode Path="Targets Section/Controller/Procedures/Main/Dwell" />
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
				<Section Name="User Variables" TypeGUID="03D3B6B7-1485-13A6-567BE1E1E0DF999A">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="P" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>3</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0.5</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Q" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>4</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="R" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>9</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="S" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>10</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>4</Elem>
						</DefaultValue>
					</Channel>
				</Section>
				<Section Name="Calculated Variables" TypeGUID="03D3B714-1485-13A6-56031C5F1CCB78A9">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="T_Km10" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km9" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="T_Km9" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km8" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="T_Km8" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km7" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="T_Km7" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km6" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="T_Km6" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km5" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="T_Km5" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km4" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="T_Km4" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km3" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="T_Km3" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km2" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="T_Km2" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km1" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="T_Km1" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_K" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="T_K" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/System Variables/System Time" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_T_0" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km10" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_0" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_T_1" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km9" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_1" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_T_2" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km8" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_2" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_T_3" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km7" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_3" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_T_4" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km6" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_4" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_T_5" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km5" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_5" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_T_6" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km4" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_6" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_T_7" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km3" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_7" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_T_8" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km2" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_8" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_T_9" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_Km1" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_9" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_T_10" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/T_K" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_10" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="fT_Km10" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km9" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="fT_Km9" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km8" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="fT_Km8" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km7" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="fT_Km7" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km6" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="fT_Km6" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km5" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="fT_Km5" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km4" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="fT_Km4" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km3" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="fT_Km3" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km2" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="fT_Km2" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km1" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="fT_Km1" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_K" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="fT_K" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAA1AkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAALAAAABltWYXIwXQAAAAEqAAAABHNpbigAAAAGW1ZhcjFdAAAAASoAAAAGW1ZhcjJdAAAAASsAAAAGW1ZhcjNdAAAAASkAAAABKwAAAAZbVmFyNF0AAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>*</Elem>
									<Elem>sin(</Elem>
									<Elem>[Var1]</Elem>
									<Elem>*</Elem>
									<Elem>(</Elem>
									<Elem>[Var2]</Elem>
									<Elem>+</Elem>
									<Elem>[Var3]</Elem>
									<Elem>)</Elem>
									<Elem>+</Elem>
									<Elem>[Var4]</Elem>
									<Elem>)</Elem>
									<Elem>+</Elem>
									<Elem>[Var5]</Elem>
								</StringArray>
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/System Variables/System Time" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/System Variables/Delta T" />
							</Property>
							<Property Name="Var4">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="Var5">
								<DependentNode Path="Targets Section/Controller/User Variables/S" />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_fT_0" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km10" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_0" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_fT_1" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km9" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_1" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_fT_2" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km8" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_2" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_fT_3" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km7" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_3" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_fT_4" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km6" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_4" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_fT_5" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km5" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_5" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_fT_6" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km4" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_6" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_fT_7" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km3" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_7" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_fT_8" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km2" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_8" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_fT_9" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_Km1" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_9" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Latch_fT_10" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>7</U16>
							</Property>
							<Property Name="CC:Cond:ComparisonMode">
								<U16>2</U16>
							</Property>
							<Property Name="CC:Cond:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CC:Cond:ZConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:ZConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Cond:YConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CC:Cond:WConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Cond:WConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Cond:WChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/fT_K" />
							</Property>
							<Property Name="CC:Cond:ZChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_10" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Exact_fT_0" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAA1AkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAALAAAABltWYXIwXQAAAAEqAAAABHNpbigAAAAGW1ZhcjFdAAAAASoAAAAGW1ZhcjJdAAAAASsAAAAGW1ZhcjNdAAAAASkAAAABKwAAAAZbVmFyNF0AAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/System Variables/Delta T" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="Var4">
								<DependentNode Path="Targets Section/Controller/User Variables/S" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>*</Elem>
									<Elem>sin(</Elem>
									<Elem>[Var1]</Elem>
									<Elem>*</Elem>
									<Elem>[Var2]</Elem>
									<Elem>+</Elem>
									<Elem>[Var3]</Elem>
									<Elem>)</Elem>
									<Elem>+</Elem>
									<Elem>[Var4]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Exact_fT_1" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAA3gkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAANAAAABltWYXIwXQAAAAEqAAAABHNpbigAAAABMgAAAAEqAAAABltWYXIxXQAAAAEqAAAABltWYXIyXQAAAAErAAAABltWYXIzXQAAAAEpAAAAASsAAAAGW1ZhcjRdAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/System Variables/Delta T" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="Var4">
								<DependentNode Path="Targets Section/Controller/User Variables/S" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>*</Elem>
									<Elem>sin(</Elem>
									<Elem>2</Elem>
									<Elem>*</Elem>
									<Elem>[Var1]</Elem>
									<Elem>*</Elem>
									<Elem>[Var2]</Elem>
									<Elem>+</Elem>
									<Elem>[Var3]</Elem>
									<Elem>)</Elem>
									<Elem>+</Elem>
									<Elem>[Var4]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Exact_fT_2" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAA3gkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAANAAAABltWYXIwXQAAAAEqAAAABHNpbigAAAABMwAAAAEqAAAABltWYXIxXQAAAAEqAAAABltWYXIyXQAAAAErAAAABltWYXIzXQAAAAEpAAAAASsAAAAGW1ZhcjRdAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/System Variables/Delta T" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="Var4">
								<DependentNode Path="Targets Section/Controller/User Variables/S" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>*</Elem>
									<Elem>sin(</Elem>
									<Elem>3</Elem>
									<Elem>*</Elem>
									<Elem>[Var1]</Elem>
									<Elem>*</Elem>
									<Elem>[Var2]</Elem>
									<Elem>+</Elem>
									<Elem>[Var3]</Elem>
									<Elem>)</Elem>
									<Elem>+</Elem>
									<Elem>[Var4]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Exact_fT_3" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAA3gkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAANAAAABltWYXIwXQAAAAEqAAAABHNpbigAAAABNAAAAAEqAAAABltWYXIxXQAAAAEqAAAABltWYXIyXQAAAAErAAAABltWYXIzXQAAAAEpAAAAASsAAAAGW1ZhcjRdAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/System Variables/Delta T" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="Var4">
								<DependentNode Path="Targets Section/Controller/User Variables/S" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>*</Elem>
									<Elem>sin(</Elem>
									<Elem>4</Elem>
									<Elem>*</Elem>
									<Elem>[Var1]</Elem>
									<Elem>*</Elem>
									<Elem>[Var2]</Elem>
									<Elem>+</Elem>
									<Elem>[Var3]</Elem>
									<Elem>)</Elem>
									<Elem>+</Elem>
									<Elem>[Var4]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Exact_fT_4" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAA3gkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAANAAAABltWYXIwXQAAAAEqAAAABHNpbigAAAABNQAAAAEqAAAABltWYXIxXQAAAAEqAAAABltWYXIyXQAAAAErAAAABltWYXIzXQAAAAEpAAAAASsAAAAGW1ZhcjRdAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/System Variables/Delta T" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="Var4">
								<DependentNode Path="Targets Section/Controller/User Variables/S" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>*</Elem>
									<Elem>sin(</Elem>
									<Elem>5</Elem>
									<Elem>*</Elem>
									<Elem>[Var1]</Elem>
									<Elem>*</Elem>
									<Elem>[Var2]</Elem>
									<Elem>+</Elem>
									<Elem>[Var3]</Elem>
									<Elem>)</Elem>
									<Elem>+</Elem>
									<Elem>[Var4]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Exact_fT_5" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAA3gkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAANAAAABltWYXIwXQAAAAEqAAAABHNpbigAAAABNgAAAAEqAAAABltWYXIxXQAAAAEqAAAABltWYXIyXQAAAAErAAAABltWYXIzXQAAAAEpAAAAASsAAAAGW1ZhcjRdAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/System Variables/Delta T" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="Var4">
								<DependentNode Path="Targets Section/Controller/User Variables/S" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>*</Elem>
									<Elem>sin(</Elem>
									<Elem>6</Elem>
									<Elem>*</Elem>
									<Elem>[Var1]</Elem>
									<Elem>*</Elem>
									<Elem>[Var2]</Elem>
									<Elem>+</Elem>
									<Elem>[Var3]</Elem>
									<Elem>)</Elem>
									<Elem>+</Elem>
									<Elem>[Var4]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Exact_fT_6" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAA3gkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAANAAAABltWYXIwXQAAAAEqAAAABHNpbigAAAABNwAAAAEqAAAABltWYXIxXQAAAAEqAAAABltWYXIyXQAAAAErAAAABltWYXIzXQAAAAEpAAAAASsAAAAGW1ZhcjRdAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/System Variables/Delta T" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="Var4">
								<DependentNode Path="Targets Section/Controller/User Variables/S" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>*</Elem>
									<Elem>sin(</Elem>
									<Elem>7</Elem>
									<Elem>*</Elem>
									<Elem>[Var1]</Elem>
									<Elem>*</Elem>
									<Elem>[Var2]</Elem>
									<Elem>+</Elem>
									<Elem>[Var3]</Elem>
									<Elem>)</Elem>
									<Elem>+</Elem>
									<Elem>[Var4]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Exact_fT_7" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAA3gkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAANAAAABltWYXIwXQAAAAEqAAAABHNpbigAAAABOAAAAAEqAAAABltWYXIxXQAAAAEqAAAABltWYXIyXQAAAAErAAAABltWYXIzXQAAAAEpAAAAASsAAAAGW1ZhcjRdAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/System Variables/Delta T" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="Var4">
								<DependentNode Path="Targets Section/Controller/User Variables/S" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>*</Elem>
									<Elem>sin(</Elem>
									<Elem>8</Elem>
									<Elem>*</Elem>
									<Elem>[Var1]</Elem>
									<Elem>*</Elem>
									<Elem>[Var2]</Elem>
									<Elem>+</Elem>
									<Elem>[Var3]</Elem>
									<Elem>)</Elem>
									<Elem>+</Elem>
									<Elem>[Var4]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Exact_fT_8" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAA3gkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAANAAAABltWYXIwXQAAAAEqAAAABHNpbigAAAABOQAAAAEqAAAABltWYXIxXQAAAAEqAAAABltWYXIyXQAAAAErAAAABltWYXIzXQAAAAEpAAAAASsAAAAGW1ZhcjRdAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/System Variables/Delta T" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="Var4">
								<DependentNode Path="Targets Section/Controller/User Variables/S" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>*</Elem>
									<Elem>sin(</Elem>
									<Elem>9</Elem>
									<Elem>*</Elem>
									<Elem>[Var1]</Elem>
									<Elem>*</Elem>
									<Elem>[Var2]</Elem>
									<Elem>+</Elem>
									<Elem>[Var3]</Elem>
									<Elem>)</Elem>
									<Elem>+</Elem>
									<Elem>[Var4]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Exact_fT_9" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAA4wkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAOAAAABltWYXIwXQAAAAEqAAAABHNpbigAAAABMQAAAAEwAAAAASoAAAAGW1ZhcjFdAAAAASoAAAAGW1ZhcjJdAAAAASsAAAAGW1ZhcjNdAAAAASkAAAABKwAAAAZbVmFyNF0AAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/System Variables/Delta T" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="Var4">
								<DependentNode Path="Targets Section/Controller/User Variables/S" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>*</Elem>
									<Elem>sin(</Elem>
									<Elem>1</Elem>
									<Elem>0</Elem>
									<Elem>*</Elem>
									<Elem>[Var1]</Elem>
									<Elem>*</Elem>
									<Elem>[Var2]</Elem>
									<Elem>+</Elem>
									<Elem>[Var3]</Elem>
									<Elem>)</Elem>
									<Elem>+</Elem>
									<Elem>[Var4]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Exact_fT_10" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAA4wkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAOAAAABltWYXIwXQAAAAEqAAAABHNpbigAAAABMQAAAAExAAAAASoAAAAGW1ZhcjFdAAAAASoAAAAGW1ZhcjJdAAAAASsAAAAGW1ZhcjNdAAAAASkAAAABKwAAAAZbVmFyNF0AAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/System Variables/Delta T" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="Var4">
								<DependentNode Path="Targets Section/Controller/User Variables/S" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>*</Elem>
									<Elem>sin(</Elem>
									<Elem>1</Elem>
									<Elem>1</Elem>
									<Elem>*</Elem>
									<Elem>[Var1]</Elem>
									<Elem>*</Elem>
									<Elem>[Var2]</Elem>
									<Elem>+</Elem>
									<Elem>[Var3]</Elem>
									<Elem>)</Elem>
									<Elem>+</Elem>
									<Elem>[Var4]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Counter" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAlQkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABltWYXIwXQAAAAErAAAAATEAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>1</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
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
			<Alias Name="P" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/P" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Q" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/Q" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="S" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/S" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="R" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/R" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Delta T" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/System Variables/Delta T" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Exact_fT_0" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Exact_fT_0" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Exact_fT_1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Exact_fT_1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Exact_fT_10" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Exact_fT_10" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Exact_fT_2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Exact_fT_2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Exact_fT_3" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Exact_fT_3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Exact_fT_4" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Exact_fT_4" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Exact_fT_5" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Exact_fT_5" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Exact_fT_6" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Exact_fT_6" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Exact_fT_7" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Exact_fT_7" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Exact_fT_8" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Exact_fT_8" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Exact_fT_9" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Exact_fT_9" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_T_0" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_0" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_T_1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_T_10" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_10" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_T_2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_T_3" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_T_4" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_4" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_T_5" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_5" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_T_6" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_6" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_T_7" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_7" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_T_8" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_8" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_T_9" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_T_9" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_fT_0" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_0" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_fT_1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_fT_10" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_10" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_fT_2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_fT_3" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_fT_4" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_4" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_fT_5" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_5" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_fT_6" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_6" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_fT_7" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_7" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_fT_8" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_8" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Latch_fT_9" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Latch_fT_9" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Counter" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Counter" />
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

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/CalcChanUnitTest/CalcChanUnitTest.nivsproj sha256=f0008477f581eb51ead1bb18dea2ec4c8561bc53a680cf987990c46ad7a2bb3a bytes=11122 -->
## FILE: tests/testutilities/legacy_files/CalcChanUnitTest/CalcChanUnitTest.nivsproj

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/CalcChanUnitTest/CalcChanUnitTest.nivsproj`
- sha256: `f0008477f581eb51ead1bb18dea2ec4c8561bc53a680cf987990c46ad7a2bb3a`
- bytes: 11122

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2012" Minor="0" Fix="0" Build="1" />
	<Content>Definition</Content>
	<Root Name="CalcChanUnitTest" TypeGUID="d9313aae-3554-45e5-93f3-86454275d4f2">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>CalcChanUnitTest</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.0</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3351079547.9250941</Double>
			</Property>
		</Properties>
		<Errors />
		<Section Name="System Definition File" TypeGUID="b9227a5b-2770-4a62-8621-ac414d4124fb">
			<Description />
			<Properties />
			<Errors />
			<Section Name="CalcChanUnitTest.nivssdf" TypeGUID="3a41ca74-36ec-4aff-9219-9d05c8f91208">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="CalcChanUnitTest.nivssdf">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5>89c477b2e9b9e1b98ff0aad0eb9aec91</MD5>
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
						<Data>AAAA7QkAgAAAAAAFAA5AMP////8ETmFtZQAADEAhB0Jvb2xlYW4AGEBAAAH/////AAELUGVybWlzc2lvbnMASwDxAAAAAAAAAAIYU2VjIEFkbWluaXN0cmF0aW9uLmx2bGliDUdyb3VwVHlwZS5jdGwAHEBQAAIAAAACDUdyb3VwIEFjY291bnQAHEBAAAH/////AAMOR3JvdXAgQWNjb3VudHMAAAEABAAAAAIAAAAOQWRtaW5pc3RyYXRpb24AAAANAQEBAQEBAQEBAQEBAQAAAAhPcGVyYXRvcgAAAA0BAAAAAQAAAQEAAAABAAAAAA==</Data>
					</Variant>
				</Property>
				<Property Name="Tools Menu Items">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAAEsAkAgAAAAAAIAA5AMP////8ETmFtZQAAEkAw/////whGdW5jdGlvbgAAYQDxAAAAAAAAAAETVG9vbGJhciBCdXR0b25zLmN0bABFQBYAAwROb25lF1N0aW11bHVzIFByb2ZpbGUgRWRpdG9yC0RhdGEgVmlld2VyAAAOVG9vbGJhciBCdXR0b24AAVMA8QAAAAAAAAABH2VudW1fVXNlciBBZG1pbiBQZXJtaXNzaW9ucy5jdGwBK0AWAA0HRGVmYXVsdA5BZG1pbmlzdHJhdGlvbhdDaGFubmVsIFNjYWxpbmcgVXRpbGl0eRFBZGQgRGlzcGxheSBJdGVtcxNDaGFuZ2UgVXNlciBQcm9maWxlI0VkaXQgU3RpbXVsdXMgUHJvZmlsZSBFZGl0b3IgSGVhZGVyGkVkaXQgRGlzcGxheSBJdGVtIFNldHRpbmdzG01vZGVsIFBhcmFtZXRlciBDYWxpYnJhdGlvbhJSdW50aW1lIEFsYXJtIEVkaXQPRWRpdCBUb29scyBNZW51FkVkaXQgRW5naW5lIENvbXBvbmVudHMaQ29uZmlndXJlIFZpc2libGUgQ2hhbm5lbHMNRmF1bHQgTWFuYWdlcgAAClBlcm1pc3Npb24AABpAMv////8QQ3VzdG9tIFRvb2wgUGF0aAAAaQDxxyxnxAAAAAIRTklWU19TaGFyZWQubHZsaWINUGF0aCB0eXBlLmN0bABBQBYAAwhBYnNvbHV0ZQhSZWxhdGl2ZQxUb0FwcERhdGFEaXIAABVDdXN0b20gVG9vbCBQYXRoIFR5cGUAYwDxAAAAAAAAAAIaTklWU1Byb2pfRmlsZW1hbmFnZXIubHZsaWIZVG9vbHMgTWVudSBJdGVtcyBUeXBlLmN0bAAmQFAABgAAAAEAAgADAAQABQ9Ub29scyBNZW51IEl0ZW0AHkBAAAH/////AAYQVG9vbHMgTWVudSBJdGVtcwAAAQAHAAAACAAAABdNb2RlbCBQYXJhbWV0ZXIgTWFuYWdlcgAAABpNb2RlbCBQYXJhbWV0ZXIgTWFuYWdlci52aQAAAABQVEgwAAAABAAAAAAAAAAAAAEtAAAAAS0AAAAAUFRIMAAAAAQAAAAAAAAAAAATVGVzdCBQcm9maWxlIEVkaXRvcgAAABVUZXN0IEVkaXRvciAoU3RlcCkudmkAAQAAUFRIMAAAAAQAAAAAAAAAAAARQmF0Y2ggVGVzdCBFZGl0b3IAAAAWVGVzdCBFZGl0b3IgKEJhdGNoKS52aQAAAABQVEgwAAAABAAAAAAAAAAAABBURE1TIEZpbGUgVmlld2VyAAAAF3Njcl9URE1TIERhdGEgVmlld2VyLnZpAAIAAFBUSDAAAAAEAAAAAAAAAAAAAS0AAAABLQAAAABQVEgwAAAABAAAAAAAAAAAABNDaGFubmVsIERhdGEgVmlld2VyAAAAFkNoYW5uZWwgRGF0YSBWaWV3ZXIudmkAAAAAUFRIMAAAAAQAAAAAAAAAAAAOQ29uc29sZSBWaWV3ZXIAAAASVmlldyBSVCBDb25zb2xlLnZpAAAAAFBUSDAAAAAEAAAAAAAAAAAAAA==</Data>
					</Variant>
				</Property>
				<Property Name="Engine Components">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAACOQkAgAAAAAAIABJAMP////8IRnVuY3Rpb24AAA5AIQlTaG93SXRlbT8AL0AWAAMETm9uZQxXYWl0Q29tcGxldGUIV2FpdFN5bmMAAApMYXVuY2hUeXBlAAARQAMAC1N5bmNUaW1lb3V0ABpAMv////8QQ3VzdG9tIFRvb2wgUGF0aAAAaQDxxyxnxAAAAAIRTklWU19TaGFyZWQubHZsaWINUGF0aCB0eXBlLmN0bABBQBYAAwhBYnNvbHV0ZQhSZWxhdGl2ZQxUb0FwcERhdGFEaXIAABVDdXN0b20gVG9vbCBQYXRoIFR5cGUAaQDxAAAAAAAAAAIaTklWU1Byb2pfRmlsZW1hbmFnZXIubHZsaWIZRW5naW5lIENvbXBvbmVudCBUeXBlLmN0bAAsQFAABgAAAAEAAgADAAQABRVFbmdpbmUgQ29tcG9uZW50IEl0ZW0AHkBAAAH/////AAYRRW5naW5lIENvbXBvbmVudHMAAQAHAAAABAAAABJzdWJfQ2FsaWJyYXRpb24udmkAAAAAAAAAUFRIMAAAAAQAAAAAAAAAAAAVVGVzdCBFZGl0b3IgKFN0ZXApLnZpAAAAAAAAAFBUSDAAAAAEAAAAAAAAAAAAFlRlc3QgRWRpdG9yIChCYXRjaCkudmkAAAAAAAAAUFRIMAAAAAQAAAAAAAAAAAAaTW9kZWwgUGFyYW1ldGVyIE1hbmFnZXIudmkAAAAAAAAAUFRIMAAAAAQAAAAAAAAAAAAA</Data>
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
						<DependentFile Type="Relative" Path="CalcChanUnitTest.nivsscreen">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
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
			<Section Name="CalcChanUnitTest.nivssdf [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CalcChanUnitTest\CalcChanUnitTest.nivssdf]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CalcChanUnitTest\CalcChanUnitTest.nivssdf</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="CalcChanUnitTest.nivsscreen [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CalcChanUnitTest\CalcChanUnitTest.nivsscreen]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CalcChanUnitTest\CalcChanUnitTest.nivsscreen</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/CalcChanUnitTest/CalcChanUnitTest.nivsscreen sha256=4178ad012e0edb8abb74f471d3541e91e06236822fb6780110d5676816ef125f bytes=6903 -->
## FILE: tests/testutilities/legacy_files/CalcChanUnitTest/CalcChanUnitTest.nivsscreen

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/CalcChanUnitTest/CalcChanUnitTest.nivsscreen`
- sha256: `4178ad012e0edb8abb74f471d3541e91e06236822fb6780110d5676816ef125f`
- bytes: 6903

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
					<Data>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</Data>
				</Variant>
			</Property>
			<Property Name="Screen Order">
				<I32Array>
					<Elem>1488</Elem>
				</I32Array>
			</Property>
			<Property Name="EscapeEnabled">
				<Boolean>false</Boolean>
			</Property>
			<Property Name="ShowPropPageOnDrop">
				<Boolean>true</Boolean>
			</Property>
			<Property Name="Workspace Loc and Size Left">
				<U16>281</U16>
			</Property>
			<Property Name="Workspace Loc and Size Top">
				<U16>39</U16>
			</Property>
			<Property Name="Workspace Loc and Size Right">
				<U16>1228</U16>
			</Property>
			<Property Name="Workspace Loc and Size Bottom">
				<U16>701</U16>
			</Property>
		</Properties>
		<Errors />
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/CalcChanUnitTest/CalcChanUnitTest.nivssdf sha256=78680703bfb82f5816a121ce385205834357ad263c817c37af834b4bfe746305 bytes=111279 -->
## FILE: tests/testutilities/legacy_files/CalcChanUnitTest/CalcChanUnitTest.nivssdf

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/CalcChanUnitTest/CalcChanUnitTest.nivssdf`
- sha256: `78680703bfb82f5816a121ce385205834357ad263c817c37af834b4bfe746305`
- bytes: 111279

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2010" Minor="0" Fix="0" Build="4" />
	<Content>Definition</Content>
	<Root Name="CalcChanUnitTest" TypeGUID="03D3BA22-1485-13A6-56BD17DA950CCD00">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>CalcChanUnitTest</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.123</String>
			</Property>
			<Property Name="Creator">
				<String>Administrator</String>
			</Property>
			<Property Name="Creation Date">
				<Double>3318358984.5011888</Double>
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
						<Double>0</Double>
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
						<I32>0</I32>
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
						<Double>10</Double>
					</Property>
					<Property Name="Execution Mode">
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
					<Property Name="dio decimation">
						<U32>1</U32>
					</Property>
					<Property Name="loop time">
						<U32>100000</U32>
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
				</Properties>
				<Errors />
				<Section Name="System Variables" TypeGUID="03D3B753-1485-13A6-56B10ED0820CF410">
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
						<Description>The compiled index of the current procedure step</Description>
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
					<Channel Name="Tripped Low Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="3">
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
					<Channel Name="Tripped Medium Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="3">
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
					<Channel Name="Tripped High Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="3">
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
					<Channel Name="Tripped Low Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
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
					<Channel Name="Tripped Medium Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
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
					<Channel Name="Tripped High Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
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
					<Channel Name="System Reserved 39" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 40" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 51" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 52" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 53" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 54" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 55" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
							<U32>0</U32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Procedures" TypeGUID="03D3B7B1-1485-13A6-56649C7783203F22">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Main" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description />
						<Properties />
						<Errors />
						<Section Name="Dwell" TypeGUID="6dde8411-8c68-408b-8558-d18c0909c789">
							<Description />
							<Properties>
								<Property Name="Command.Value">
									<Double>1</Double>
								</Property>
								<Property Name="Command.Mode">
									<U32>0</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="End of Main" TypeGUID="b485fef3-012c-4c9e-acdb-c204000d11e5">
							<Description />
							<Properties>
								<Property Name="Goto Label">
									<DependentNode Path="Targets Section/Controller/Procedures/Main/Dwell" />
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
				<Section Name="User Variables" TypeGUID="03D3B6B7-1485-13A6-567BE1E1E0DF999A">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="P" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>3</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>12</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Q" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>4</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>6</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="R" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>9</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>3</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="X" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>10</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0.1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Z" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>17</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>3</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Y" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>18</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>2</Elem>
						</DefaultValue>
					</Channel>
				</Section>
				<Section Name="Calculated Variables" TypeGUID="03D3B714-1485-13A6-56031C5F1CCB78A9">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="Time" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/System Variables/System Time" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Zero" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmgkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABltWYXIwXQAAAAEtAAAABltWYXIxXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/System Variables/Delta T" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/System Variables/Delta T" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>-</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Exp(X)" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmAkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABGV4cCgAAAAGW1ZhcjBdAAAAASkAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>exp(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Sqrt(X)" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmQkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABXNxcnQoAAAABltWYXIwXQAAAAEpAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>sqrt(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Sin(X)" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmAkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABHNpbigAAAAGW1ZhcjBdAAAAASkAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>sin(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Asin(X)" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmQkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABWFzaW4oAAAABltWYXIwXQAAAAEpAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>asin(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Sign(X)" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmQkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABXNpZ24oAAAABltWYXIwXQAAAAEpAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>sign(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Cos(X)" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmAkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABGNvcygAAAAGW1ZhcjBdAAAAASkAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>cos(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Acos(X)" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmQkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABWFjb3MoAAAABltWYXIwXQAAAAEpAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>acos(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Abs(X)" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmAkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABGFicygAAAAGW1ZhcjBdAAAAASkAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>abs(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Int(X)" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmAkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABGludCgAAAAGW1ZhcjBdAAAAASkAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>int(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tan(X)" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmAkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABHRhbigAAAAGW1ZhcjBdAAAAASkAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>tan(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Atan(X)" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmQkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABWF0YW4oAAAABltWYXIwXQAAAAEpAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>atan(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="X + Y" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmgkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABltWYXIwXQAAAAErAAAABltWYXIxXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="-X + Y" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAnwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAEAAAAAS0AAAAGW1ZhcjBdAAAAASsAAAAGW1ZhcjFdAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>-</Elem>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="X + -Y" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAnwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAEAAAABltWYXIwXQAAAAErAAAAAS0AAAAGW1ZhcjFdAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>-</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="-X + -Y" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAApAkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAFAAAAAS0AAAAGW1ZhcjBdAAAAASsAAAABLQAAAAZbVmFyMV0AAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>-</Elem>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>-</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="X - Y" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmgkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABltWYXIwXQAAAAEtAAAABltWYXIxXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>-</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="-X - Y" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAnwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAEAAAAAS0AAAAGW1ZhcjBdAAAAAS0AAAAGW1ZhcjFdAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>-</Elem>
									<Elem>[Var0]</Elem>
									<Elem>-</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="X - -Y" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAnwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAEAAAABltWYXIwXQAAAAEtAAAAAS0AAAAGW1ZhcjFdAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>-</Elem>
									<Elem>-</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="-X - -Y" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAApAkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAFAAAAAS0AAAAGW1ZhcjBdAAAAAS0AAAABLQAAAAZbVmFyMV0AAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>-</Elem>
									<Elem>[Var0]</Elem>
									<Elem>-</Elem>
									<Elem>-</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="X * Y" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmgkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABltWYXIwXQAAAAEqAAAABltWYXIxXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>*</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="-X * Y" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAnwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAEAAAAAS0AAAAGW1ZhcjBdAAAAASoAAAAGW1ZhcjFdAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>-</Elem>
									<Elem>[Var0]</Elem>
									<Elem>*</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="X div Y" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmgkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABltWYXIwXQAAAAEvAAAABltWYXIxXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>/</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="-X div Y" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAnwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAEAAAAAS0AAAAGW1ZhcjBdAAAAAS8AAAAGW1ZhcjFdAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>-</Elem>
									<Elem>[Var0]</Elem>
									<Elem>/</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="X ^ Y" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmgkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABltWYXIwXQAAAAFeAAAABltWYXIxXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>^</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="-X ^ Y" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAnwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAEAAAAAS0AAAAGW1ZhcjBdAAAAAV4AAAAGW1ZhcjFdAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>-</Elem>
									<Elem>[Var0]</Elem>
									<Elem>^</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="P+(Q*(R^2))" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Computed without parens to test precedence of operators</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAswkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAHAAAABltWYXIwXQAAAAErAAAABltWYXIxXQAAAAEqAAAABltWYXIyXQAAAAFeAAAAATIAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>[Var1]</Elem>
									<Elem>*</Elem>
									<Elem>[Var2]</Elem>
									<Elem>^</Elem>
									<Elem>2</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="(P*Q) + (X*Z)" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Computed without parens to test precedence of operators</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAuAkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAHAAAABltWYXIwXQAAAAEqAAAABltWYXIxXQAAAAErAAAABltWYXIyXQAAAAEqAAAABltWYXIzXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/User Variables/X" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/User Variables/Z" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>*</Elem>
									<Elem>[Var1]</Elem>
									<Elem>+</Elem>
									<Elem>[Var2]</Elem>
									<Elem>*</Elem>
									<Elem>[Var3]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="(P ^ Z) ^ Y" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Computed without parens to test left to right evaluation</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAqQkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAFAAAABltWYXIwXQAAAAFeAAAABltWYXIxXQAAAAFeAAAABltWYXIyXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Z" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>^</Elem>
									<Elem>[Var1]</Elem>
									<Elem>^</Elem>
									<Elem>[Var2]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="(Q div R) div Y" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Computed without parens to test left to right evaluation</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAqQkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAFAAAABltWYXIwXQAAAAEvAAAABltWYXIxXQAAAAEvAAAABltWYXIyXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>/</Elem>
									<Elem>[Var1]</Elem>
									<Elem>/</Elem>
									<Elem>[Var2]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="(P - Q) - R" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Computed without parens to test left to right evaluation</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAqQkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAFAAAABltWYXIwXQAAAAEtAAAABltWYXIxXQAAAAEtAAAABltWYXIyXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>-</Elem>
									<Elem>[Var1]</Elem>
									<Elem>-</Elem>
									<Elem>[Var2]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="P + Z*((Q^4)^Y)*R + (P^2)^Y" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Computed without parens to test precedence of operators</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAA+QkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAARAAAABltWYXIwXQAAAAErAAAABltWYXIxXQAAAAEqAAAABltWYXIyXQAAAAFeAAAAATQAAAABXgAAAAZbVmFyM10AAAABKgAAAAZbVmFyNF0AAAABKwAAAAZbVmFyNV0AAAABXgAAAAEyAAAAAV4AAAAGW1ZhcjZdAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Z" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="Var4">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="Var5">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var6">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>[Var1]</Elem>
									<Elem>*</Elem>
									<Elem>[Var2]</Elem>
									<Elem>^</Elem>
									<Elem>4</Elem>
									<Elem>^</Elem>
									<Elem>[Var3]</Elem>
									<Elem>*</Elem>
									<Elem>[Var4]</Elem>
									<Elem>+</Elem>
									<Elem>[Var5]</Elem>
									<Elem>^</Elem>
									<Elem>2</Elem>
									<Elem>^</Elem>
									<Elem>[Var6]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="(P+R)*(Q^(Y*Z)+21)" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Computed with parens to test grouping</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAA9AkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAASAAAAASgAAAAGW1ZhcjBdAAAAASsAAAAGW1ZhcjFdAAAAASkAAAABKgAAAAEoAAAABltWYXIyXQAAAAFeAAAAASgAAAAGW1ZhcjNdAAAAASoAAAAGW1ZhcjRdAAAAASkAAAABKwAAAAEyAAAAATEAAAABKQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="Var4">
								<DependentNode Path="Targets Section/Controller/User Variables/Z" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>[Var1]</Elem>
									<Elem>)</Elem>
									<Elem>*</Elem>
									<Elem>(</Elem>
									<Elem>[Var2]</Elem>
									<Elem>^</Elem>
									<Elem>(</Elem>
									<Elem>[Var3]</Elem>
									<Elem>*</Elem>
									<Elem>[Var4]</Elem>
									<Elem>)</Elem>
									<Elem>+</Elem>
									<Elem>2</Elem>
									<Elem>1</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
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
			<Alias Name="P" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/P" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Q" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/Q" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="X" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/X" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Z" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/Z" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/Y" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="R" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/R" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Abs(X)" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Abs(X)" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Acos(X)" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Acos(X)" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Asin(X)" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Asin(X)" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Atan(X)" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Atan(X)" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Cos(X)" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Cos(X)" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Exp(X)" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Exp(X)" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Int(X)" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Int(X)" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Sign(X)" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Sign(X)" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Sin(X)" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Sin(X)" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Sqrt(X)" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Sqrt(X)" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Tan(X)" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Tan(X)" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Zero" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Zero" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Time" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Time" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="(P*Q) + (X*Z)" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/(P*Q) + (X*Z)" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="(P+R)*(Q^(Y*Z)+21)" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/(P+R)*(Q^(Y*Z)+21)" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="(P ^ Z) ^ Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/(P ^ Z) ^ Y" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="P + Z*((Q^4)^Y)*R + (P^2)^Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/P + Z*((Q^4)^Y)*R + (P^2)^Y" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="P+(Q*(R^2))" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/P+(Q*(R^2))" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Abs_X" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Abs(X)" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="-X + -Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/-X + -Y" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="-X + Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/-X + Y" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="X + -Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/X + -Y" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="X + Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/X + Y" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="-X * Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/-X * Y" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="-X - -Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/-X - -Y" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="-X - Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/-X - Y" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="-X div Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/-X div Y" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="-X ^ Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/-X ^ Y" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="X * Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/X * Y" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="X - -Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/X - -Y" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="X - Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/X - Y" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="X div Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/X div Y" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="X ^ Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/X ^ Y" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="(P - Q) - R" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/(P - Q) - R" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="(Q div R) div Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/(Q div R) div Y" />
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

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/CalculatedChannelTest/CalculatedChannelTest.nivsproj sha256=076f4ffc6a0f1190e4f85bd353268ac0be3a1ddf366a2bee730f5a06eb4ae202 bytes=11233 -->
## FILE: tests/testutilities/legacy_files/CalculatedChannelTest/CalculatedChannelTest.nivsproj

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/CalculatedChannelTest/CalculatedChannelTest.nivsproj`
- sha256: `076f4ffc6a0f1190e4f85bd353268ac0be3a1ddf366a2bee730f5a06eb4ae202`
- bytes: 11233

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2012" Minor="0" Fix="0" Build="1" />
	<Content>Definition</Content>
	<Root Name="CalculatedChannelTest" TypeGUID="d9313aae-3554-45e5-93f3-86454275d4f2">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>CalculatedChannelTest</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.0</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3351079547.9250941</Double>
			</Property>
		</Properties>
		<Errors />
		<Section Name="System Definition File" TypeGUID="b9227a5b-2770-4a62-8621-ac414d4124fb">
			<Description />
			<Properties />
			<Errors />
			<Section Name="CalculatedChannelTest.nivssdf" TypeGUID="3a41ca74-36ec-4aff-9219-9d05c8f91208">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="CalculatedChannelTest.nivssdf">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5>89c477b2e9b9e1b98ff0aad0eb9aec91</MD5>
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
						<Data>AAAA7QkAgAAAAAAFAA5AMP////8ETmFtZQAADEAhB0Jvb2xlYW4AGEBAAAH/////AAELUGVybWlzc2lvbnMASwDxAAAAAAAAAAIYU2VjIEFkbWluaXN0cmF0aW9uLmx2bGliDUdyb3VwVHlwZS5jdGwAHEBQAAIAAAACDUdyb3VwIEFjY291bnQAHEBAAAH/////AAMOR3JvdXAgQWNjb3VudHMAAAEABAAAAAIAAAAOQWRtaW5pc3RyYXRpb24AAAANAQEBAQEBAQEBAQEBAQAAAAhPcGVyYXRvcgAAAA0BAAAAAQAAAQEAAAABAAAAAA==</Data>
					</Variant>
				</Property>
				<Property Name="Tools Menu Items">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAAEsAkAgAAAAAAIAA5AMP////8ETmFtZQAAEkAw/////whGdW5jdGlvbgAAYQDxAAAAAAAAAAETVG9vbGJhciBCdXR0b25zLmN0bABFQBYAAwROb25lF1N0aW11bHVzIFByb2ZpbGUgRWRpdG9yC0RhdGEgVmlld2VyAAAOVG9vbGJhciBCdXR0b24AAVMA8QAAAAAAAAABH2VudW1fVXNlciBBZG1pbiBQZXJtaXNzaW9ucy5jdGwBK0AWAA0HRGVmYXVsdA5BZG1pbmlzdHJhdGlvbhdDaGFubmVsIFNjYWxpbmcgVXRpbGl0eRFBZGQgRGlzcGxheSBJdGVtcxNDaGFuZ2UgVXNlciBQcm9maWxlI0VkaXQgU3RpbXVsdXMgUHJvZmlsZSBFZGl0b3IgSGVhZGVyGkVkaXQgRGlzcGxheSBJdGVtIFNldHRpbmdzG01vZGVsIFBhcmFtZXRlciBDYWxpYnJhdGlvbhJSdW50aW1lIEFsYXJtIEVkaXQPRWRpdCBUb29scyBNZW51FkVkaXQgRW5naW5lIENvbXBvbmVudHMaQ29uZmlndXJlIFZpc2libGUgQ2hhbm5lbHMNRmF1bHQgTWFuYWdlcgAAClBlcm1pc3Npb24AABpAMv////8QQ3VzdG9tIFRvb2wgUGF0aAAAaQDxxyxnxAAAAAIRTklWU19TaGFyZWQubHZsaWINUGF0aCB0eXBlLmN0bABBQBYAAwhBYnNvbHV0ZQhSZWxhdGl2ZQxUb0FwcERhdGFEaXIAABVDdXN0b20gVG9vbCBQYXRoIFR5cGUAYwDxAAAAAAAAAAIaTklWU1Byb2pfRmlsZW1hbmFnZXIubHZsaWIZVG9vbHMgTWVudSBJdGVtcyBUeXBlLmN0bAAmQFAABgAAAAEAAgADAAQABQ9Ub29scyBNZW51IEl0ZW0AHkBAAAH/////AAYQVG9vbHMgTWVudSBJdGVtcwAAAQAHAAAACAAAABdNb2RlbCBQYXJhbWV0ZXIgTWFuYWdlcgAAABpNb2RlbCBQYXJhbWV0ZXIgTWFuYWdlci52aQAAAABQVEgwAAAABAAAAAAAAAAAAAEtAAAAAS0AAAAAUFRIMAAAAAQAAAAAAAAAAAATVGVzdCBQcm9maWxlIEVkaXRvcgAAABVUZXN0IEVkaXRvciAoU3RlcCkudmkAAQAAUFRIMAAAAAQAAAAAAAAAAAARQmF0Y2ggVGVzdCBFZGl0b3IAAAAWVGVzdCBFZGl0b3IgKEJhdGNoKS52aQAAAABQVEgwAAAABAAAAAAAAAAAABBURE1TIEZpbGUgVmlld2VyAAAAF3Njcl9URE1TIERhdGEgVmlld2VyLnZpAAIAAFBUSDAAAAAEAAAAAAAAAAAAAS0AAAABLQAAAABQVEgwAAAABAAAAAAAAAAAABNDaGFubmVsIERhdGEgVmlld2VyAAAAFkNoYW5uZWwgRGF0YSBWaWV3ZXIudmkAAAAAUFRIMAAAAAQAAAAAAAAAAAAOQ29uc29sZSBWaWV3ZXIAAAASVmlldyBSVCBDb25zb2xlLnZpAAAAAFBUSDAAAAAEAAAAAAAAAAAAAA==</Data>
					</Variant>
				</Property>
				<Property Name="Engine Components">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAACOQkAgAAAAAAIABJAMP////8IRnVuY3Rpb24AAA5AIQlTaG93SXRlbT8AL0AWAAMETm9uZQxXYWl0Q29tcGxldGUIV2FpdFN5bmMAAApMYXVuY2hUeXBlAAARQAMAC1N5bmNUaW1lb3V0ABpAMv////8QQ3VzdG9tIFRvb2wgUGF0aAAAaQDxxyxnxAAAAAIRTklWU19TaGFyZWQubHZsaWINUGF0aCB0eXBlLmN0bABBQBYAAwhBYnNvbHV0ZQhSZWxhdGl2ZQxUb0FwcERhdGFEaXIAABVDdXN0b20gVG9vbCBQYXRoIFR5cGUAaQDxAAAAAAAAAAIaTklWU1Byb2pfRmlsZW1hbmFnZXIubHZsaWIZRW5naW5lIENvbXBvbmVudCBUeXBlLmN0bAAsQFAABgAAAAEAAgADAAQABRVFbmdpbmUgQ29tcG9uZW50IEl0ZW0AHkBAAAH/////AAYRRW5naW5lIENvbXBvbmVudHMAAQAHAAAABAAAABJzdWJfQ2FsaWJyYXRpb24udmkAAAAAAAAAUFRIMAAAAAQAAAAAAAAAAAAVVGVzdCBFZGl0b3IgKFN0ZXApLnZpAAAAAAAAAFBUSDAAAAAEAAAAAAAAAAAAFlRlc3QgRWRpdG9yIChCYXRjaCkudmkAAAAAAAAAUFRIMAAAAAQAAAAAAAAAAAAaTW9kZWwgUGFyYW1ldGVyIE1hbmFnZXIudmkAAAAAAAAAUFRIMAAAAAQAAAAAAAAAAAAA</Data>
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
						<DependentFile Type="Relative" Path="CalculatedChannelTest.nivsscreen">
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
			<Section Name="CalculatedChannelTest.nivssdf [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CalculatedChannelTest\CalculatedChannelTest.nivssdf]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CalculatedChannelTest\CalculatedChannelTest.nivssdf</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="CalculatedChannelTest.nivsscreen [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CalculatedChannelTest\CalculatedChannelTest.nivsscreen]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CalculatedChannelTest\CalculatedChannelTest.nivsscreen</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/CalculatedChannelTest/CalculatedChannelTest.nivsscreen sha256=1b5169c4810ab77a3cd04364198f28c2b3638f03ebd06276ffea577a7fcb3a54 bytes=10278 -->
## FILE: tests/testutilities/legacy_files/CalculatedChannelTest/CalculatedChannelTest.nivsscreen

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/CalculatedChannelTest/CalculatedChannelTest.nivsscreen`
- sha256: `1b5169c4810ab77a3cd04364198f28c2b3638f03ebd06276ffea577a7fcb3a54`
- bytes: 10278

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
					<Data>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dXMgUHJvZmlsZSBFZGl0b3IgSGVhZGVyGkVkaXQgRGlzcGxheSBJdGVtIFNldHRpbmdzG01vZGVsIFBhcmFtZXRlciBDYWxpYnJhdGlvbhJSdW50aW1lIEFsYXJtIEVkaXQPRWRpdCBUb29scyBNZW51FkVkaXQgRW5naW5lIENvbXBvbmVudHMaQ29uZmlndXJlIFZpc2libGUgQ2hhbm5lbHMNRmF1bHQgTWFuYWdlcgAAClBlcm1pc3Npb24AAAxAIQdMb2FkZWQ/ABRAIQ9BbHdheXMgVmlzaWJsZT8AVwDxAAAAAAAAAAEkY2x1c3Rlcl9FbnRpcmUgU2NyZWVuIERlZmluaXRpb24uY3RsACpAUAAKAFAAUQBSAAUAAQACAAYAUwBUAFULU2NyZWVuLkRhdGEAJkBAAAH/////AFYZU2NyZWVuIEl0ZW0gQ2x1c3RlciBBcnJheQABAFcAAAABAAAADAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAACLOAQAAAAAAAAXQAAAAAAA1Q29udHJvbGxlci9DYWxjdWxhdGVkIFZhcmlhYmxlcy9DaGFuVG9BdmVyYWdlTWluNFN0ZXAAWgImASICYwAAAJ4AAE9cAAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD/oAFvAAAAAAEAAAA1Q29udHJvbGxlci9DYWxjdWxhdGVkIFZhcmlhYmxlcy9DaGFuVG9BdmVyYWdlTWluNFN0ZXAJAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAABjfAQAAAAAAAAXQAAAAAAA1Q29udHJvbGxlci9DYWxjdWxhdGVkIFZhcmlhYmxlcy9DaGFuVG9BdmVyYWdlTWluM1N0ZXAAWgHgASICHQAA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</Data>
				</Variant>
			</Property>
			<Property Name="Screen Order">
				<I32Array>
					<Elem>1488</Elem>
				</I32Array>
			</Property>
			<Property Name="EscapeEnabled">
				<Boolean>false</Boolean>
			</Property>
			<Property Name="ShowPropPageOnDrop">
				<Boolean>true</Boolean>
			</Property>
			<Property Name="Workspace Loc and Size Left">
				<U16>74</U16>
			</Property>
			<Property Name="Workspace Loc and Size Top">
				<U16>79</U16>
			</Property>
			<Property Name="Workspace Loc and Size Right">
				<U16>1021</U16>
			</Property>
			<Property Name="Workspace Loc and Size Bottom">
				<U16>741</U16>
			</Property>
		</Properties>
		<Errors />
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/CalculatedChannelTest/CalculatedChannelTest.nivssdf sha256=c8d31d36b4c48732a0fbfb6b331fb275271ff032787aad5edce6fbb75ac69d66 bytes=85253 -->
## FILE: tests/testutilities/legacy_files/CalculatedChannelTest/CalculatedChannelTest.nivssdf

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/CalculatedChannelTest/CalculatedChannelTest.nivssdf`
- sha256: `c8d31d36b4c48732a0fbfb6b331fb275271ff032787aad5edce6fbb75ac69d66`
- bytes: 85253

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2010" Minor="0" Fix="0" Build="4" />
	<Content>Definition</Content>
	<Root Name="CalculatedChannelTest" TypeGUID="03D3BA22-1485-13A6-56BD17DA950CCD00">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>CalculatedChannelTest</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.5</String>
			</Property>
			<Property Name="Creator">
				<String>Administrator</String>
			</Property>
			<Property Name="Creation Date">
				<Double>3318358984.5011888</Double>
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
						<Double>0</Double>
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
						<I32>0</I32>
					</Property>
					<Property Name="Streamed Channels">
						<I32>0</I32>
					</Property>
					<Property Name="Stream Rate">
						<I32>2</I32>
					</Property>
					<Property Name="Secondary Control Loop Processor">
						<I32>0</I32>
					</Property>
					<Property Name="OS">
						<String>Windows</String>
					</Property>
					<Property Name="Engine Rate">
						<Double>10</Double>
					</Property>
					<Property Name="Execution Mode">
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
					<Property Name="dio decimation">
						<U32>1</U32>
					</Property>
					<Property Name="loop time">
						<U32>100000</U32>
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
				</Properties>
				<Errors />
				<Section Name="System Variables" TypeGUID="03D3B753-1485-13A6-56B10ED0820CF410">
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
						<Description>The compiled index of the current procedure step</Description>
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
					<Channel Name="Tripped Low Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="3">
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
					<Channel Name="Tripped Medium Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="3">
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
					<Channel Name="Tripped High Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="3">
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
					<Channel Name="Tripped Low Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
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
					<Channel Name="Tripped Medium Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
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
					<Channel Name="Tripped High Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
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
					<Channel Name="System Reserved 39" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 40" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 51" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 52" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 53" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 54" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
					<Channel Name="System Reserved 55" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
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
							<U32>0</U32>
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
				<Section Name="User Variables" TypeGUID="03D3B6B7-1485-13A6-567BE1E1E0DF999A">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="MaxUV1" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>3</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="MaxUV2" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
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
					<Channel Name="MinUV1" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>9</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="MinUV2" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>10</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="VelocityChan" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>17</U32>
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
								<U32>18</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>1112</Elem>
						</DefaultValue>
					</Channel>
				</Section>
				<Section Name="Calculated Variables" TypeGUID="03D3B714-1485-13A6-56031C5F1CCB78A9">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="MaxConstant" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>1</U16>
							</Property>
							<Property Name="ID">
								<U32>1</U32>
							</Property>
							<Property Name="CC:Max:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Max:YConstValue">
								<Double>5</Double>
							</Property>
							<Property Name="CC:Max:XConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Max:XConstValue">
								<Double>-4</Double>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="MaxUV2ToConstVal10" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>1</U16>
							</Property>
							<Property Name="ID">
								<U32>2</U32>
							</Property>
							<Property Name="CC:Max:YChan">
								<DependentNode Path="Targets Section/Controller/User Variables/MaxUV2" />
							</Property>
							<Property Name="CC:Max:YConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Max:YConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Max:XConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Max:XConstValue">
								<Double>10</Double>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="MaxUV1ToConstVal5" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>1</U16>
							</Property>
							<Property Name="ID">
								<U32>5</U32>
							</Property>
							<Property Name="CC:Max:XChan">
								<DependentNode Path="Targets Section/Controller/User Variables/MaxUV1" />
							</Property>
							<Property Name="CC:Max:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Max:YConstValue">
								<Double>5</Double>
							</Property>
							<Property Name="CC:Max:XConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Max:XConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Max2Var" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>1</U16>
							</Property>
							<Property Name="ID">
								<U32>6</U32>
							</Property>
							<Property Name="CC:Max:XChan">
								<DependentNode Path="Targets Section/Controller/User Variables/MaxUV1" />
							</Property>
							<Property Name="CC:Max:YChan">
								<DependentNode Path="Targets Section/Controller/User Variables/MaxUV2" />
							</Property>
							<Property Name="CC:Max:YConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Max:YConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Max:XConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Max:XConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="MinConstant" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>2</U16>
							</Property>
							<Property Name="ID">
								<U32>7</U32>
							</Property>
							<Property Name="CC:Min:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Min:YConstValue">
								<Double>6</Double>
							</Property>
							<Property Name="CC:Min:XConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Min:XConstValue">
								<Double>-5</Double>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Min2Var" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>2</U16>
							</Property>
							<Property Name="ID">
								<U32>8</U32>
							</Property>
							<Property Name="CC:Min:XValue">
								<DependentNode Path="Targets Section/Controller/User Variables/MinUV1" />
							</Property>
							<Property Name="CC:Min:YValue">
								<DependentNode Path="Targets Section/Controller/User Variables/MinUV2" />
							</Property>
							<Property Name="CC:Min:YConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Min:YConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Min:XConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Min:XConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="MinUV1ToConstVal2" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>2</U16>
							</Property>
							<Property Name="ID">
								<U32>11</U32>
							</Property>
							<Property Name="CC:Min:XValue">
								<DependentNode Path="Targets Section/Controller/User Variables/MinUV1" />
							</Property>
							<Property Name="CC:Min:YConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Min:YConstValue">
								<Double>2</Double>
							</Property>
							<Property Name="CC:Min:XConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Min:XConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="MinUV2ToConstVal3" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>2</U16>
							</Property>
							<Property Name="ID">
								<U32>12</U32>
							</Property>
							<Property Name="CC:Min:YValue">
								<DependentNode Path="Targets Section/Controller/User Variables/MinUV2" />
							</Property>
							<Property Name="CC:Min:YConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Min:YConstValue">
								<Double>0</Double>
							</Property>
							<Property Name="CC:Min:XConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Min:XConstValue">
								<Double>3</Double>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="3PointAverager" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>6</U16>
							</Property>
							<Property Name="ID">
								<U32>13</U32>
							</Property>
							<Property Name="CC:Ave:Chan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/ChanToAverage" />
							</Property>
							<Property Name="CC:Ave:NPoints">
								<U32>3</U32>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="DistanceChannelPrevIteration" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="ID">
								<U32>21</U32>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/DistanceChannel" />
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="VelocityChanPrevIteration" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="ID">
								<U32>20</U32>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/VelocityChan" />
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="DeltaDistance" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="ID">
								<U32>19</U32>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/DeltaDistance" />
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAApAkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAGAAAABltWYXIwXQAAAAErAAAAAS4AAAABMAAAAAEwAAAAATEAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>.</Elem>
									<Elem>0</Elem>
									<Elem>0</Elem>
									<Elem>1</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="DistanceChannel" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="ID">
								<U32>16</U32>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/DistanceChannel" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/DeltaDistance" />
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmgkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABltWYXIwXQAAAAErAAAABltWYXIxXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="AccelerationOnDistanceChannel" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>5</U16>
							</Property>
							<Property Name="ID">
								<U32>15</U32>
							</Property>
							<Property Name="CC:Accel:VelChan">
								<DependentNode Path="Targets Section/Controller/User Variables/VelocityChan" />
							</Property>
							<Property Name="CC:Accel:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/DistanceChannel" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="ChanToAverageMin6Step" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="ID">
								<U32>27</U32>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/ChanToAverageMin5Step" />
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="ChanToAverageMin5Step" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="ID">
								<U32>26</U32>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/ChanToAverageMin4Step" />
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="ChanToAverageMin4Step" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="ID">
								<U32>25</U32>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/ChanToAverageMin3Step" />
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="ChanToAverageMin3Step" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="ID">
								<U32>24</U32>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/ChanToAverageMin2Step" />
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="ChanToAverageMin2Step" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="ID">
								<U32>23</U32>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/ChanToAverageMin1Step" />
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="ChanToAverageMin1Step" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="ID">
								<U32>14</U32>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/ChanToAverage" />
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="ChanToAverage" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="ID">
								<U32>22</U32>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/ChanToAverage" />
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmgkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAEAAAABltWYXIwXQAAAAErAAAAAS4AAAABMQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>.</Elem>
									<Elem>1</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
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
			<Alias Name="MaxUV1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/MaxUV1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="MaxUV2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/MaxUV2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="MinUV1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/MinUV1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="MinUV2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/MinUV2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VelocityChan" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/VelocityChan" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="TEST_ID" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/TEST_ID" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="MaxConstant" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/MaxConstant" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="MaxUV2ToConstVal10" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/MaxUV2ToConstVal10" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="MaxUV1ToConstVal5" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/MaxUV1ToConstVal5" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Max2Var" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Max2Var" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="MinConstant" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/MinConstant" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Min2Var" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Min2Var" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="MinUV1ToConstVal2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/MinUV1ToConstVal2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="MinUV2ToConstVal3" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/MinUV2ToConstVal3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="3PointAverager" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/3PointAverager" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="DistanceChannelPrevIteration" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/DistanceChannelPrevIteration" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VelocityChanPrevIteration" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/VelocityChanPrevIteration" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="DeltaDistance" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/DeltaDistance" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="DistanceChannel" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/DistanceChannel" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="AccelerationOnDistanceChannel" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/AccelerationOnDistanceChannel" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="ChanToAverageMin4Step" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/ChanToAverageMin4Step" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="ChanToAverageMin3Step" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/ChanToAverageMin3Step" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="ChanToAverageMin2Step" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/ChanToAverageMin2Step" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="ChanToAverageMin1Step" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/ChanToAverageMin1Step" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="ChanToAverage" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/ChanToAverage" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="ChanToAverageMin5Step" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/ChanToAverageMin5Step" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="ChanToAverageMin6Step" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/ChanToAverageMin6Step" />
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

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/CustomDevices/CustomDevices.nivsproj sha256=6783ee8baeee9d153b1c506d9bb3281b846f1cb38107e91548929d55dbd945ba bytes=12303 -->
## FILE: tests/testutilities/legacy_files/CustomDevices/CustomDevices.nivsproj

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/CustomDevices/CustomDevices.nivsproj`
- sha256: `6783ee8baeee9d153b1c506d9bb3281b846f1cb38107e91548929d55dbd945ba`
- bytes: 12303

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2012" Minor="0" Fix="0" Build="1" />
	<Content>Definition</Content>
	<Root Name="CustomDevices" TypeGUID="d9313aae-3554-45e5-93f3-86454275d4f2">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>CustomDevices</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.0</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3352110309.5341716</Double>
			</Property>
		</Properties>
		<Errors />
		<Section Name="System Definition File" TypeGUID="b9227a5b-2770-4a62-8621-ac414d4124fb">
			<Description />
			<Properties />
			<Errors />
			<Section Name="CustomDevices.nivssdf" TypeGUID="3a41ca74-36ec-4aff-9219-9d05c8f91208">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="CustomDevices.nivssdf">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5>89b0858288415abf3de97303c18a3836</MD5>
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
						<DependentFile Type="Relative" Path="CustomDevices.nivsscreen">
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
			<Section Name="CustomDevices.nivssdf [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CustomDevices\CustomDevices.nivssdf]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CustomDevices\CustomDevices.nivssdf</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="CustomDevices.nivsscreen [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CustomDevices\CustomDevices.nivsscreen]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CustomDevices\CustomDevices.nivsscreen</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Async Device Test Engine.llb [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\Custom Devices\Async Device Test\Async Device Test Engine.llb]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\Custom Devices\Async Device Test\Async Device Test Engine.llb</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Inline Model Device Test Engine.llb [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\Custom Devices\Inline Model Device Test\Inline Model Device Test Engine.llb]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\Custom Devices\Inline Model Device Test\Inline Model Device Test Engine.llb</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Inline HW Device Test Engine.llb [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\Custom Devices\Inline HW Device Test\Inline HW Device Test Engine.llb]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\Custom Devices\Inline HW Device Test\Inline HW Device Test Engine.llb</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/CustomDevices/CustomDevices.nivsscreen sha256=56ac5274816848aadd4a2ab4f3094488cb2036a252ec8e0c4455f0bad452d505 bytes=5149 -->
## FILE: tests/testutilities/legacy_files/CustomDevices/CustomDevices.nivsscreen

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/CustomDevices/CustomDevices.nivsscreen`
- sha256: `56ac5274816848aadd4a2ab4f3094488cb2036a252ec8e0c4455f0bad452d505`
- bytes: 5149

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
					<Data>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</Data>
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
				<U16>862</U16>
			</Property>
			<Property Name="Workspace Loc and Size Bottom">
				<U16>710</U16>
			</Property>
		</Properties>
		<Errors />
	</Root>
</Document>
````
