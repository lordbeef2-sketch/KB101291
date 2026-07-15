# NI OSS SOURCE SNAPSHOT: niveristand-python

<!--NI_OSS_SNAPSHOT repo=ni/niveristand-python commit=9ced536d3414f04a8b6b9315ce4c71b879d02a96 -->

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/CustomDevices/CustomDevices.nivssdf sha256=87c65d49e4d889a1e408964653cc5fa677607b7f60a26f307a25a8b379a7f4bc bytes=527194 -->
## FILE: tests/testutilities/legacy_files/CustomDevices/CustomDevices.nivssdf

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/CustomDevices/CustomDevices.nivssdf`
- sha256: `87c65d49e4d889a1e408964653cc5fa677607b7f60a26f307a25a8b379a7f4bc`
- bytes: 527194

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2010" Minor="0" Fix="0" Build="4" />
	<Content>Definition</Content>
	<Root Name="CustomDevices" TypeGUID="03D3BA22-1485-13A6-56BD17DA950CCD00">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>CustomDevices</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.4</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3352110308.5029216</Double>
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
						<Section Name="NI-XNET" TypeGUID="6b693e6d-67b1-40b8-8108-4a4cc3147721">
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
					<Section Name="Async" TypeGUID="71956C63-B316-94F5-5872-01854D7DF3CE">
						<Description />
						<Properties>
							<Property Name="CD Status">
								<U32>1</U32>
							</Property>
							<Property Name="Driver VI Exec Mode">
								<U32>0</U32>
							</Property>
							<Property Name="Driver VI Path_0">
								<DependentFile Type="To Common Doc Dir" Path="Custom Devices\Async Device Test\Async Device Test Engine.llb\Async Device Test RT Driver VI.vi">
									<Version>1.0</Version>
									<ForceDownload>false</ForceDownload>
									<RTDestination>c:\ni-rt\VeriStand\Custom Devices\Async Device Test\Async Device Test Engine.llb\Async Device Test RT Driver VI.vi</RTDestination>
									<SupportedTarget>PharLap &amp; Windows</SupportedTarget>
									<MD5 />
								</DependentFile>
							</Property>
							<Property Name="Version">
								<String>1.0</String>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Outputs" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
							<Description />
							<Properties />
							<Errors />
							<Section Name="Section1" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out13" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out39" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out51" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out60" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out71" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out73" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out82" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out85" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section2" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out15" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out23" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out70" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out79" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out81" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section3" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out7" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out11" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out58" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out59" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out72" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out93" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section4" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out3" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out10" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out18" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out19" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out26" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out32" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out36" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out66" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out76" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out87" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out96" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out99" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section5" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out5" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out17" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out31" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out33" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out34" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out35" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out37" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out43" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out45" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out52" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out62" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out64" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out89" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out92" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out97" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section6" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out9" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out22" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out24" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out42" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out46" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out47" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out48" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out55" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out80" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out83" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out94" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section7" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out1" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out20" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out28" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out29" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out38" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out44" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out53" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out57" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out63" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out75" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out95" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section8" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out25" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out27" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out30" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out40" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out54" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out61" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out65" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out69" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out77" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out78" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out84" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out90" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out91" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section9" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out2" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out4" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out6" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out8" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out12" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out14" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out41" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out49" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out50" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out56" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out67" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out68" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out86" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out88" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out98" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section10" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out0" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out16" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out21" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out74" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
						</Section>
						<Section Name="Inputs" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
							<Description />
							<Properties />
							<Errors />
							<Section Name="Section1" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In11" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section3</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In12" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In17" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In32" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In63" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In74" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In78" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In81" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section2" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In6" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In21" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In26" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In34" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In60" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In62" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In68" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In72" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section3</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In77" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In92" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section3" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In23" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In42" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In50" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In59" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section3</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In84" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In85" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In89" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In93" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section3</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In96" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In99" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section4" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In9" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In19" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In28" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In30" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In31" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In41" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In46" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In47" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In56" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In76" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In88" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In90" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section5" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In0" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In2" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In24" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In33" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In44" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In48" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In82" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In91" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In98" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section6" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In8" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In38" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In43" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In83" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In97" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section7" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In3" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In4" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In5" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In14" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In18" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In40" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In45" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In51" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In52" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In53" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In58" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section3</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In71" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In79" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section8" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In1" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In7" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section3</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In15" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In16" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In25" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In27" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In35" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In39" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In55" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In64" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In65" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In69" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In75" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In80" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In86" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section9" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In20" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In66" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In67" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In70" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In87" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section10" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In10" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In13" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In22" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In29" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In36" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In37" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In49" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In54" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In57" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In61" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In73" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In94" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In95" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
						</Section>
					</Section>
					<Section Name="InlineMdl" TypeGUID="0238886C-C0B3-5F18-4465-55268E5F5D6A">
						<Description />
						<Properties>
							<Property Name="CD Status">
								<U32>1</U32>
							</Property>
							<Property Name="Driver VI Exec Mode">
								<U32>2</U32>
							</Property>
							<Property Name="Driver VI Path_0">
								<DependentFile Type="To Common Doc Dir" Path="Custom Devices\Inline Model Device Test\Inline Model Device Test Engine.llb\Inline Model Device Test RT Driver VI.vi">
									<Version>1.0</Version>
									<ForceDownload>false</ForceDownload>
									<RTDestination>c:\ni-rt\VeriStand\Custom Devices\Inline Model Device Test\Inline Model Device Test Engine.llb\Inline Model Device Test RT Driver VI.vi</RTDestination>
									<SupportedTarget>PharLap &amp; Windows</SupportedTarget>
									<MD5 />
								</DependentFile>
							</Property>
							<Property Name="Version">
								<String>1.0</String>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Outputs" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
							<Description />
							<Properties />
							<Errors />
							<Section Name="Section1" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out0" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out13" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out18" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out27" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out34" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out51" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out62" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out72" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out78" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out82" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out84" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out88" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section2" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out4" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out11" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out20" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out21" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out25" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out52" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out55" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out60" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out67" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out68" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out79" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out85" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out89" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section3" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out7" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out17" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out22" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out46" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out56" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out64" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section4" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out1" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out2" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out5" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out9" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out15" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out33" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out36" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out69" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section5" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out30" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out38" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out42" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out50" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out58" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out70" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out71" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out73" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out77" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out83" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out86" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out92" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out99" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section6" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out6" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out35" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out40" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out41" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out48" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out61" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out81" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out93" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out94" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section7" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out8" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out10" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out12" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out37" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out44" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out53" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out59" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out76" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out90" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out91" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out96" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out98" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section8" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out14" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out26" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out28" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out31" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out32" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out39" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out57" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out63" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out65" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out80" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out95" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out97" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section9" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out3" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out16" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out19" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out54" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out75" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out87" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section10" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out23" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out24" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out29" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out43" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out45" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out47" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out49" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out66" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out74" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
						</Section>
						<Section Name="Inputs" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
							<Description />
							<Properties />
							<Errors />
							<Section Name="Section1" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In8" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In14" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In51" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In62" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In68" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In74" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section2" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In3" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In4" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In24" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In54" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In96" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section3" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In7" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section3</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In19" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In20" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In31" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In49" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In61" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In69" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section4" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In22" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section3</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In41" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In46" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section3</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In57" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In67" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In72" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In73" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In89" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In91" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In97" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section5" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In11" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In37" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In64" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section3</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In66" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In81" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In99" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section6" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In0" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In10" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In17" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section3</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In21" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In43" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In45" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In52" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In59" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In63" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In70" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In85" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section7" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In2" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In6" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In13" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In15" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In25" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In26" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In28" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In36" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In38" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In40" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In48" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In50" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In53" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In58" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In78" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In83" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In87" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In93" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section8" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In5" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In16" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In18" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In34" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In55" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In56" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section3</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In60" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In65" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In76" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In79" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In86" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In90" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In92" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section9" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In1" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In12" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In23" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In27" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In29" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In35" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In39" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In44" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In75" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In80" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In82" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In84" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In98" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section10" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In9" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In30" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In32" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In33" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In42" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In47" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In71" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In77" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In88" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In94" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In95" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
						</Section>
					</Section>
					<Section Name="InlineHW" TypeGUID="B8E9FD5F-B38F-2536-C07E-44D4441640C0">
						<Description />
						<Properties>
							<Property Name="CD Status">
								<U32>1</U32>
							</Property>
							<Property Name="Driver VI Exec Mode">
								<U32>1</U32>
							</Property>
							<Property Name="Driver VI Path_0">
								<DependentFile Type="To Common Doc Dir" Path="Custom Devices\Inline HW Device Test\Inline HW Device Test Engine.llb\Inline HW Device Test RT Driver VI.vi">
									<Version>1.0</Version>
									<ForceDownload>false</ForceDownload>
									<RTDestination>c:\ni-rt\VeriStand\Custom Devices\Inline HW Device Test\Inline HW Device Test Engine.llb\Inline HW Device Test RT Driver VI.vi</RTDestination>
									<SupportedTarget>PharLap &amp; Windows</SupportedTarget>
									<MD5 />
								</DependentFile>
							</Property>
							<Property Name="Version">
								<String>1.0</String>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Outputs" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
							<Description />
							<Properties />
							<Errors />
							<Section Name="Section1" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out11" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out12" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out44" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out54" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out55" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out57" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out68" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out78" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out81" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out82" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out87" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section2" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out4" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out24" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out40" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out48" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out52" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out74" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section3" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out18" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out58" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out62" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out66" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out80" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out99" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section4" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out2" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out10" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out16" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out30" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out43" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out47" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out50" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out51" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out70" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out77" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out84" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section5" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out15" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out19" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out23" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out27" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out28" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out29" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out42" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out88" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out93" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section6" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out0" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out7" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out17" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out20" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out26" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out34" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out36" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out37" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out71" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out85" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out89" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section7" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out3" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out13" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out31" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out33" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out38" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out41" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out69" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out96" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out97" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section8" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out9" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out14" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out21" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out39" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out60" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out67" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out72" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out79" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out86" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out94" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out95" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section9" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out5" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out6" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out8" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out22" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out35" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out56" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out64" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out73" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out75" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out76" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out90" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section10" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Out1" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out25" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out32" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out45" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out46" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out49" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out53" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out59" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out61" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out63" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out65" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out83" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out91" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out92" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Out98" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties />
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
						</Section>
						<Section Name="Inputs" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
							<Description />
							<Properties />
							<Errors />
							<Section Name="Section1" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In8" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In10" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In15" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In21" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In44" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In67" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In70" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In72" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section2" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In5" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In16" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In18" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section3</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In32" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In33" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In40" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In45" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In59" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In87" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In93" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section3" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In1" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In3" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In17" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In35" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In66" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section3</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In68" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In74" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In86" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In89" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In90" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In99" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section3</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section4" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In13" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In19" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In20" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In27" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In38" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In47" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In55" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In64" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In71" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In78" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In81" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In88" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In91" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In94" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In95" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section5" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In2" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In24" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In28" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In51" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In58" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section3</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In61" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In62" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section3</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section6" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In0" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In9" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In11" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In22" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In31" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In39" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In41" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In56" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In73" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In76" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In77" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In79" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In80" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section3</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In83" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In84" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In85" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In96" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section7" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In6" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In7" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In12" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In23" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In42" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section8" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In26" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In29" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section5</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In30" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In36" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In46" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In50" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In57" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In60" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In82" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In97" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section9" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In4" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In34" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In37" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section6</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In49" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In53" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In54" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section1</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In63" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Section10" TypeGUID="03D3BB89-1485-13A6-56005DE6430FF8B7">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In14" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section8</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In25" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In43" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section4</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In48" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In52" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section2</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In65" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In69" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section7</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In75" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section9</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In92" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="In98" TypeGUID="03D3BB99-1485-13A6-561D1F898F032919" RowDim="1" ColDim="1" Units="" BitFields="3">
									<Description />
									<Properties>
										<Property Name="user.CD.Map Section">
											<String>Section10</String>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
						</Section>
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
				<Section Name="User Channels" TypeGUID="03D3B6B7-1485-13A6-567BE1E1E0DF999A">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="TEST_ID" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description>ID of the current running test.</Description>
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>10239</Elem>
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
			<Alias Name="Async.In0" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section5/In0" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section8/In1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In10" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section10/In10" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In11" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section1/In11" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In12" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section1/In12" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In13" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section10/In13" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In14" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section7/In14" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In15" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section8/In15" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In16" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section8/In16" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In17" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section1/In17" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In18" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section7/In18" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In19" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section4/In19" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section5/In2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In20" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section9/In20" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In21" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section2/In21" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In22" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section10/In22" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In23" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section3/In23" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In24" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section5/In24" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In25" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section8/In25" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In26" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section2/In26" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In27" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section8/In27" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In28" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section4/In28" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In29" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section10/In29" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In3" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section7/In3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In30" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section4/In30" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In31" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section4/In31" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In32" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section1/In32" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In33" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section5/In33" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In34" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section2/In34" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In35" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section8/In35" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In36" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section10/In36" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In37" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section10/In37" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In38" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section6/In38" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In39" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section8/In39" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In4" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section7/In4" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In40" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section7/In40" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In41" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section4/In41" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In42" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section3/In42" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In43" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section6/In43" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In44" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section5/In44" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In45" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section7/In45" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In46" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section4/In46" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In47" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section4/In47" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In48" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section5/In48" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In49" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section10/In49" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In5" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section7/In5" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In50" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section3/In50" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In51" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section7/In51" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In52" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section7/In52" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In53" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section7/In53" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In54" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section10/In54" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In55" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section8/In55" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In56" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section4/In56" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In57" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section10/In57" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In58" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section7/In58" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In59" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section3/In59" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In6" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section2/In6" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In60" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section2/In60" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In61" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section10/In61" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In62" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section2/In62" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In63" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section1/In63" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In64" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section8/In64" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In65" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section8/In65" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In66" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section9/In66" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In67" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section9/In67" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In68" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section2/In68" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In69" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section8/In69" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In7" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section8/In7" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In70" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section9/In70" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In71" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section7/In71" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In72" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section2/In72" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In73" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section10/In73" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In74" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section1/In74" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In75" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section8/In75" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In76" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section4/In76" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In77" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section2/In77" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In78" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section1/In78" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In79" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section7/In79" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In8" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section6/In8" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In80" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section8/In80" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In81" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section1/In81" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In82" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section5/In82" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In83" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section6/In83" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In84" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section3/In84" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In85" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section3/In85" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In86" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section8/In86" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In87" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section9/In87" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In88" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section4/In88" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In89" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section3/In89" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In9" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section4/In9" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In90" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section4/In90" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In91" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section5/In91" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In92" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section2/In92" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In93" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section3/In93" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In94" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section10/In94" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In95" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section10/In95" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In96" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section3/In96" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In97" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section6/In97" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In98" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section5/In98" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.In99" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Inputs/Section3/In99" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out0" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section10/Out0" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section7/Out1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out10" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section4/Out10" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out11" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section3/Out11" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out12" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section9/Out12" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out13" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section1/Out13" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out14" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section9/Out14" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out15" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section2/Out15" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out16" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section10/Out16" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out17" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section5/Out17" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out18" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section4/Out18" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out19" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section4/Out19" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section9/Out2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out20" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section7/Out20" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out21" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section10/Out21" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out22" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section6/Out22" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out23" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section2/Out23" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out24" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section6/Out24" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out25" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section8/Out25" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out26" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section4/Out26" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out27" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section8/Out27" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out28" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section7/Out28" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out29" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section7/Out29" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out3" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section4/Out3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out30" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section8/Out30" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out31" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section5/Out31" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out32" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section4/Out32" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out33" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section5/Out33" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out34" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section5/Out34" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out35" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section5/Out35" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out36" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section4/Out36" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out37" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section5/Out37" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out38" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section7/Out38" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out39" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section1/Out39" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out4" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section9/Out4" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out40" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section8/Out40" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out41" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section9/Out41" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out42" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section6/Out42" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out43" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section5/Out43" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out44" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section7/Out44" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out45" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section5/Out45" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out46" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section6/Out46" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out47" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section6/Out47" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out48" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section6/Out48" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out49" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section9/Out49" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out5" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section5/Out5" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out50" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section9/Out50" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out51" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section1/Out51" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out52" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section5/Out52" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out53" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section7/Out53" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out54" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section8/Out54" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out55" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section6/Out55" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out56" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section9/Out56" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out57" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section7/Out57" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out58" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section3/Out58" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out59" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section3/Out59" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out6" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section9/Out6" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out60" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section1/Out60" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out61" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section8/Out61" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out62" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section5/Out62" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out63" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section7/Out63" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out64" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section5/Out64" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out65" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section8/Out65" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out66" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section4/Out66" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out67" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section9/Out67" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out68" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section9/Out68" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out69" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section8/Out69" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out7" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section3/Out7" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out70" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section2/Out70" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out71" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section1/Out71" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out72" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section3/Out72" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out73" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section1/Out73" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out74" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section10/Out74" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out75" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section7/Out75" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out76" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section4/Out76" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out77" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section8/Out77" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out78" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section8/Out78" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out79" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section2/Out79" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out8" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section9/Out8" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out80" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section6/Out80" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out81" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section2/Out81" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out82" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section1/Out82" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out83" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section6/Out83" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out84" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section8/Out84" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out85" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section1/Out85" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out86" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section9/Out86" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out87" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section4/Out87" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out88" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section9/Out88" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out89" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section5/Out89" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out9" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section6/Out9" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out90" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section8/Out90" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out91" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section8/Out91" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out92" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section5/Out92" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out93" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section3/Out93" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out94" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section6/Out94" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out95" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section7/Out95" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out96" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section4/Out96" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out97" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section5/Out97" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out98" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section9/Out98" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Async.Out99" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/Async/Outputs/Section4/Out99" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In0" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section6/In0" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section3/In1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In10" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section1/In10" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In11" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section6/In11" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In12" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section7/In12" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In13" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section4/In13" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In14" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section10/In14" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In15" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section1/In15" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In16" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section2/In16" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In17" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section3/In17" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In18" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section2/In18" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In19" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section4/In19" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section5/In2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In20" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section4/In20" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In21" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section1/In21" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In22" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section6/In22" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In23" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section7/In23" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In24" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section5/In24" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In25" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section10/In25" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In26" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section8/In26" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In27" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section4/In27" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In28" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section5/In28" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In29" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section8/In29" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In3" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section3/In3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In30" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section8/In30" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In31" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section6/In31" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In32" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section2/In32" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In33" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section2/In33" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In34" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section9/In34" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In35" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section3/In35" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In36" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section8/In36" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In37" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section9/In37" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In38" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section4/In38" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In39" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section6/In39" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In4" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section9/In4" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In40" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section2/In40" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In41" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section6/In41" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In42" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section7/In42" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In43" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section10/In43" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In44" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section1/In44" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In45" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section2/In45" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In46" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section8/In46" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In47" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section4/In47" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In48" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section10/In48" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In49" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section9/In49" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In5" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section2/In5" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In50" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section8/In50" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In51" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section5/In51" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In52" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section10/In52" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In53" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section9/In53" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In54" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section9/In54" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In55" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section4/In55" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In56" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section6/In56" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In57" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section8/In57" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In58" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section5/In58" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In59" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section2/In59" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In6" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section7/In6" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In60" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section8/In60" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In61" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section5/In61" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In62" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section5/In62" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In63" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section9/In63" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In64" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section4/In64" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In65" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section10/In65" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In66" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section3/In66" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In67" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section1/In67" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In68" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section3/In68" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In69" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section10/In69" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In7" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section7/In7" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In70" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section1/In70" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In71" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section4/In71" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In72" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section1/In72" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In73" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section6/In73" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In74" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section3/In74" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In75" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section10/In75" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In76" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section6/In76" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In77" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section6/In77" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In78" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section4/In78" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In79" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section6/In79" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In8" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section1/In8" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In80" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section6/In80" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In81" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section4/In81" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In82" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section8/In82" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In83" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section6/In83" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In84" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section6/In84" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In85" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section6/In85" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In86" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section3/In86" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In87" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section2/In87" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In88" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section4/In88" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In89" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section3/In89" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In9" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section6/In9" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In90" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section3/In90" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In91" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section4/In91" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In92" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section10/In92" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In93" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section2/In93" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In94" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section4/In94" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In95" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section4/In95" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In96" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section6/In96" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In97" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section8/In97" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In98" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section10/In98" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.In99" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Inputs/Section3/In99" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out0" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section6/Out0" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section10/Out1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out10" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section4/Out10" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out11" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section1/Out11" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out12" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section1/Out12" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out13" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section7/Out13" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out14" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section8/Out14" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out15" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section5/Out15" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out16" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section4/Out16" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out17" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section6/Out17" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out18" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section3/Out18" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out19" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section5/Out19" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section4/Out2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out20" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section6/Out20" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out21" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section8/Out21" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out22" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section9/Out22" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out23" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section5/Out23" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out24" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section2/Out24" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out25" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section10/Out25" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out26" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section6/Out26" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out27" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section5/Out27" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out28" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section5/Out28" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out29" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section5/Out29" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out3" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section7/Out3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out30" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section4/Out30" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out31" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section7/Out31" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out32" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section10/Out32" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out33" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section7/Out33" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out34" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section6/Out34" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out35" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section9/Out35" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out36" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section6/Out36" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out37" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section6/Out37" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out38" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section7/Out38" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out39" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section8/Out39" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out4" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section2/Out4" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out40" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section2/Out40" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out41" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section7/Out41" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out42" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section5/Out42" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out43" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section4/Out43" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out44" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section1/Out44" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out45" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section10/Out45" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out46" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section10/Out46" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out47" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section4/Out47" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out48" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section2/Out48" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out49" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section10/Out49" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out5" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section9/Out5" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out50" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section4/Out50" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out51" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section4/Out51" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out52" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section2/Out52" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out53" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section10/Out53" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out54" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section1/Out54" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out55" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section1/Out55" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out56" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section9/Out56" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out57" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section1/Out57" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out58" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section3/Out58" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out59" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section10/Out59" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out6" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section9/Out6" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out60" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section8/Out60" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out61" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section10/Out61" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out62" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section3/Out62" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out63" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section10/Out63" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out64" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section9/Out64" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out65" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section10/Out65" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out66" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section3/Out66" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out67" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section8/Out67" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out68" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section1/Out68" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out69" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section7/Out69" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out7" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section6/Out7" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out70" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section4/Out70" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out71" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section6/Out71" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out72" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section8/Out72" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out73" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section9/Out73" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out74" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section2/Out74" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out75" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section9/Out75" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out76" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section9/Out76" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out77" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section4/Out77" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out78" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section1/Out78" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out79" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section8/Out79" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out8" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section9/Out8" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out80" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section3/Out80" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out81" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section1/Out81" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out82" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section1/Out82" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out83" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section10/Out83" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out84" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section4/Out84" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out85" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section6/Out85" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out86" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section8/Out86" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out87" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section1/Out87" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out88" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section5/Out88" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out89" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section6/Out89" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out9" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section8/Out9" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out90" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section9/Out90" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out91" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section10/Out91" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out92" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section10/Out92" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out93" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section5/Out93" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out94" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section8/Out94" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out95" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section8/Out95" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out96" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section7/Out96" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out97" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section7/Out97" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out98" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section10/Out98" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="HW.Out99" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineHW/Outputs/Section3/Out99" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In0" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section6/In0" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section9/In1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In10" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section6/In10" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In11" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section5/In11" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In12" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section9/In12" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In13" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section7/In13" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In14" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section1/In14" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In15" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section7/In15" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In16" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section8/In16" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In17" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section6/In17" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In18" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section8/In18" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In19" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section3/In19" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section7/In2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In20" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section3/In20" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In21" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section6/In21" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In22" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section4/In22" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In23" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section9/In23" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In24" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section2/In24" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In25" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section7/In25" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In26" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section7/In26" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In27" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section9/In27" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In28" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section7/In28" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In29" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section9/In29" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In3" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section2/In3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In30" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section10/In30" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In31" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section3/In31" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In32" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section10/In32" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In33" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section10/In33" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In34" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section8/In34" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In35" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section9/In35" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In36" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section7/In36" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In37" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section5/In37" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In38" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section7/In38" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In39" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section9/In39" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In4" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section2/In4" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In40" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section7/In40" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In41" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section4/In41" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In42" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section10/In42" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In43" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section6/In43" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In44" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section9/In44" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In45" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section6/In45" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In46" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section4/In46" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In47" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section10/In47" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In48" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section7/In48" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In49" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section3/In49" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In5" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section8/In5" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In50" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section7/In50" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In51" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section1/In51" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In52" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section6/In52" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In53" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section7/In53" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In54" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section2/In54" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In55" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section8/In55" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In56" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section8/In56" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In57" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section4/In57" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In58" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section7/In58" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In59" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section6/In59" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In6" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section7/In6" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In60" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section8/In60" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In61" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section3/In61" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In62" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section1/In62" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In63" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section6/In63" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In64" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section5/In64" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In65" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section8/In65" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In66" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section5/In66" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In67" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section4/In67" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In68" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section1/In68" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In69" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section3/In69" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In7" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section3/In7" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In70" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section6/In70" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In71" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section10/In71" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In72" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section4/In72" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In73" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section4/In73" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In74" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section1/In74" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In75" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section9/In75" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In76" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section8/In76" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In77" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section10/In77" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In78" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section7/In78" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In79" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section8/In79" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In8" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section1/In8" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In80" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section9/In80" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In81" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section5/In81" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In82" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section9/In82" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In83" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section7/In83" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In84" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section9/In84" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In85" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section6/In85" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In86" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section8/In86" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In87" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section7/In87" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In88" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section10/In88" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In89" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section4/In89" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In9" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section10/In9" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In90" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section8/In90" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In91" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section4/In91" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In92" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section8/In92" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In93" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section7/In93" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In94" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section10/In94" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In95" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section10/In95" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In96" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section2/In96" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In97" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section4/In97" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In98" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section9/In98" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.In99" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Inputs/Section5/In99" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out0" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section1/Out0" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section4/Out1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out10" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section7/Out10" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out11" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section2/Out11" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out12" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section7/Out12" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out13" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section1/Out13" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out14" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section8/Out14" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out15" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section4/Out15" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out16" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section9/Out16" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out17" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section3/Out17" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out18" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section1/Out18" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out19" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section9/Out19" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section4/Out2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out20" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section2/Out20" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out21" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section2/Out21" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out22" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section3/Out22" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out23" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section10/Out23" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out24" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section10/Out24" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out25" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section2/Out25" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out26" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section8/Out26" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out27" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section1/Out27" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out28" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section8/Out28" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out29" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section10/Out29" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out3" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section9/Out3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out30" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section5/Out30" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out31" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section8/Out31" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out32" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section8/Out32" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out33" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section4/Out33" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out34" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section1/Out34" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out35" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section6/Out35" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out36" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section4/Out36" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out37" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section7/Out37" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out38" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section5/Out38" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out39" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section8/Out39" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out4" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section2/Out4" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out40" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section6/Out40" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out41" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section6/Out41" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out42" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section5/Out42" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out43" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section10/Out43" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out44" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section7/Out44" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out45" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section10/Out45" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out46" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section3/Out46" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out47" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section10/Out47" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out48" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section6/Out48" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out49" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section10/Out49" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out5" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section4/Out5" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out50" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section5/Out50" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out51" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section1/Out51" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out52" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section2/Out52" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out53" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section7/Out53" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out54" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section9/Out54" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out55" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section2/Out55" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out56" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section3/Out56" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out57" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section8/Out57" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out58" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section5/Out58" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out59" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section7/Out59" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out6" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section6/Out6" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out60" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section2/Out60" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out61" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section6/Out61" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out62" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section1/Out62" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out63" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section8/Out63" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out64" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section3/Out64" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out65" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section8/Out65" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out66" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section10/Out66" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out67" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section2/Out67" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out68" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section2/Out68" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out69" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section4/Out69" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out7" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section3/Out7" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out70" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section5/Out70" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out71" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section5/Out71" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out72" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section1/Out72" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out73" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section5/Out73" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out74" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section10/Out74" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out75" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section9/Out75" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out76" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section7/Out76" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out77" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section5/Out77" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out78" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section1/Out78" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out79" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section2/Out79" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out8" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section7/Out8" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out80" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section8/Out80" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out81" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section6/Out81" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out82" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section1/Out82" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out83" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section5/Out83" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out84" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section1/Out84" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out85" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section2/Out85" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out86" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section5/Out86" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out87" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section9/Out87" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out88" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section1/Out88" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out89" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section2/Out89" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out9" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section4/Out9" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out90" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section7/Out90" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out91" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section7/Out91" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out92" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section5/Out92" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out93" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section6/Out93" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out94" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section6/Out94" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out95" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section8/Out95" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out96" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section7/Out96" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out97" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section8/Out97" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out98" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section7/Out98" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Mdl.Out99" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/Custom Devices/InlineMdl/Outputs/Section5/Out99" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="TEST_ID" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Target Section/Controller/User Channels/TEST_ID" />
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

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/FaultChannelTest/FaultChannelTest.nivsproj sha256=38c7b5dab87d8ccde4a592982ce4d36f9a1f9a35ecc0d1a24d480c1aa22841c2 bytes=11066 -->
## FILE: tests/testutilities/legacy_files/FaultChannelTest/FaultChannelTest.nivsproj

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/FaultChannelTest/FaultChannelTest.nivsproj`
- sha256: `38c7b5dab87d8ccde4a592982ce4d36f9a1f9a35ecc0d1a24d480c1aa22841c2`
- bytes: 11066

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2012" Minor="0" Fix="0" Build="1" />
	<Content>Definition</Content>
	<Root Name="FaultChannelTest" TypeGUID="d9313aae-3554-45e5-93f3-86454275d4f2">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>FaultChannelTest</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.0</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3351079549.6280775</Double>
			</Property>
		</Properties>
		<Errors />
		<Section Name="System Definition File" TypeGUID="b9227a5b-2770-4a62-8621-ac414d4124fb">
			<Description />
			<Properties />
			<Errors />
			<Section Name="FaultChannelTest.nivssdf" TypeGUID="3a41ca74-36ec-4aff-9219-9d05c8f91208">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="FaultChannelTest.nivssdf">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5>df3ea443f36858c4a4acf47fe064b380</MD5>
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
						<DependentFile Type="Relative" Path="FaultChannelTest.nivsscreen">
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
			<Section Name="FaultChannelTest.nivssdf [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\FaultChannelTest\FaultChannelTest.nivssdf]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\FaultChannelTest\FaultChannelTest.nivssdf</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="FaultChannelTest.nivsscreen [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\FaultChannelTest\FaultChannelTest.nivsscreen]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\FaultChannelTest\FaultChannelTest.nivsscreen</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/FaultChannelTest/FaultChannelTest.nivsscreen sha256=80d5c4bd6aac22885c6cce870bd82920bfec3d9796775372a58182170bce7363 bytes=4571 -->
## FILE: tests/testutilities/legacy_files/FaultChannelTest/FaultChannelTest.nivsscreen

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/FaultChannelTest/FaultChannelTest.nivsscreen`
- sha256: `80d5c4bd6aac22885c6cce870bd82920bfec3d9796775372a58182170bce7363`
- bytes: 4571

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
					<Data>AAAJ4QkAgAAAAABYABRAMP////8LVGVtcGxhdGUgVkkAEUADAApQb3NpdGlvbiBYAAARQAMAClBvc2l0aW9uIFkAABBAMP////8GQ3VzdG9tAAAUQCEOU2hvdyBUaXRsZSBCYXIAAAlAAwACSUQAABJAIQ1BbHdheXMgT24gVG9wABJAIQxBbGxvdyBSZXNpemUAABRAIQ5BbGxvdyBNaW5pbWl6ZQAAEEAhC0FsbG93IENsb3NlABRAIQ5TaXplIHRvIFNjcmVlbgAAD0ADAAlTY3JlZW4uSUQAGUAWAAIGTm9ybWFsA05ldwAABVN0YXRlAA5AMP////8FVGl0bGUACUACAANbMF0ACUACAANbMV0ACUACAANbMl0ACUACAANbM10AHEBQAAQADgAPABAAEQ1XaW5kb3cgQm91bmRzABFACAALQ2hhbm5lbCBSZWYADkAw/////wRVbml0AAAUQCEORGVmYXVsdCBVbml0cz8AABJAIQxGbGFzaCBMaW1pdD8AAA1ABwAHQ29sb3IgMQANQAcAB0NvbG9yIDIADUAHAAdDb2xvciAzAA1ABwAHQ29sb3IgNAAPQAcACUJjayBDb2xvcgARQAcACkZvcmUgQ29sb3IAAA1ACgAHTGltaXQgMQANQAoAB0xpbWl0IDIADUAKAAdMaW1pdCAzAA1ACgAHTGltaXQgNAATQAMADExpbWl0IE1vZGUgMQAAE0ADAAxMaW1pdCBNb2RlIDIAABNAAwAMTGltaXQgTW9kZSAzAAATQAMADExpbWl0IE1vZGUgNAAAFUADAA9TY2FsZSBQcmVjaXNpb24AD0AKAAlTY2FsZSBNaW4AD0AKAAlTY2FsZSBNYXgADUADAAZGb3JtYXQAAA9AAwAJUHJlY2lzaW9uABVAAwAPQmFja2dyb3VuZCBUeXBlABFAAwALVmFyaWFibGUgSUQAEEBAAAH/////ACsDSURzABRAMP////8LVmFyaWFibGUgSUQAEkBAAAH/////AC0FVW5pdHMAFEBAAAH/////AC0GTGFiZWxzAAATQAoADFNjYWxlIEZhY3RvcgAAE0AKAAxTY2FsZSBPZmZzZXQAABFABwALVmFyaWFibGUgSUQAGkBAAAH/////ADIMWVNjYWxlIEluZGV4AAANQAUABkZvcm1hdAAAD0AFAAlQcmVjaXNpb24ACUAFAANGaXQADkAw/////wVMYWJlbAAWQCERVXNlIERlZmF1bHQgTGFiZWwAEkAhDUxhYmVsIFZpc2libGUACUAKAANNaW4ACUAKAANNYXgASwDxAAAAAAAAAAEgY2x1c3Rlcl9HcmFwaCBTY2FsZSBTZXR0aW5ncy5jdGwAIkBQAAgANAA1ADYANwA4ADkAOgA7BlhTY2FsZQAAFEBAAAH/////ADwHWVNjYWxlcwAPQAUACUJhciBTdHlsZQANQAIAB0ZpbGwgVG8AE0AHAAxGaWxsL1B0Q29sb3IAABFABQAKTGluZSBTdHlsZQAAEUAFAApMaW5lIFdpZHRoAAALQAcABUNvbG9yAA1ABQAGSW50ZXJwAAARQAUAC1BvaW50IFN0eWxlAEgA8QAAAAAAAAABH2NsdXN0ZXJfR3JhcGggUGxvdCBTZXR0aW5ncy5jdGwAIEBQAAgAPgA/AEAAQQBCAEMARABFBFBsb3QAABJAQAAB/////wBGBVBsb3RzABNACgANVXBkYXRlIFBlcmlvZAAVQAoADkhpc3RvcnkgTGVuZ3RoAAAUQHAACAAAAAIAAAZNeS5SZWYAABBAIQtJcyBDb250cm9sPwAWQDD/////DENoYW5uZWwgUGF0aAAAGkBAAAH/////AEwNQ2hhbm5lbCBQYXRocwAQQFMLQ3VzdG9tIERhdGEAqwDxxieWWAAAAAEgY2x1c3Rlcl9TY3JlZW4gSXRlbSBTZXR0aW5ncy5jdGwAgkBQADYAAAABAAIAAwAEAAUABgAHAAgACQAKAAsADAANABIAEwAUABUAFgAXABgAGQAaABsAHAAdAB4AHwAgACEAIgAjACQAJQAmACcAKAApACoALAAuAC8AMAAxADMAPAA9AEcASABJAEoASwBNAE4LU2NyZWVuIEl0ZW0AEkBAAAH/////AE8FSXRlbXMADkAw/////wROYW1lAAAUQDD/////C0Rlc2NyaXB0aW9uAVMA8QAAAAAAAAABH2VudW1fVXNlciBBZG1pbiBQZXJtaXNzaW9ucy5jdGwBK0AWAA0HRGVmYXVsdA5BZG1pbmlzdHJhdGlvbhdDaGFubmVsIFNjYWxpbmcgVXRpbGl0eRFBZGQgRGlzcGxheSBJdGVtcxNDaGFuZ2UgVXNlciBQcm9maWxlI0VkaXQgU3RpbXVsdXMgUHJvZmlsZSBFZGl0b3IgSGVhZGVyGkVkaXQgRGlzcGxheSBJdGVtIFNldHRpbmdzG01vZGVsIFBhcmFtZXRlciBDYWxpYnJhdGlvbhJSdW50aW1lIEFsYXJtIEVkaXQPRWRpdCBUb29scyBNZW51FkVkaXQgRW5naW5lIENvbXBvbmVudHMaQ29uZmlndXJlIFZpc2libGUgQ2hhbm5lbHMNRmF1bHQgTWFuYWdlcgAAClBlcm1pc3Npb24AAAxAIQdMb2FkZWQ/ABRAIQ9BbHdheXMgVmlzaWJsZT8AVwDxAAAAAAAAAAEkY2x1c3Rlcl9FbnRpcmUgU2NyZWVuIERlZmluaXRpb24uY3RsACpAUAAKAFAAUQBSAAUAAQACAAYAUwBUAFULU2NyZWVuLkRhdGEAJkBAAAH/////AFYZU2NyZWVuIEl0ZW0gQ2x1c3RlciBBcnJheQABAFcAAAABAAAAAQAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAABZrAQAAAAAAACSvAAAAAAANRmF1bHRDaGFubmVsMAGaAQQCYgFBAAAAfwAAn9MAAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOyQAVUAAAAAAQAAAA1GYXVsdENoYW5uZWwwCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAMRW1wdHkgU2NyZWVuAAAAAAAAJK8AAAAAAAAAAAAAAAEAAAAAAA==</Data>
				</Variant>
			</Property>
			<Property Name="Screen Order">
				<I32Array>
					<Elem>9391</Elem>
				</I32Array>
			</Property>
			<Property Name="EscapeEnabled">
				<Boolean>false</Boolean>
			</Property>
			<Property Name="ShowPropPageOnDrop">
				<Boolean>true</Boolean>
			</Property>
			<Property Name="Workspace Loc and Size Left">
				<U16>219</U16>
			</Property>
			<Property Name="Workspace Loc and Size Top">
				<U16>57</U16>
			</Property>
			<Property Name="Workspace Loc and Size Right">
				<U16>1031</U16>
			</Property>
			<Property Name="Workspace Loc and Size Bottom">
				<U16>717</U16>
			</Property>
		</Properties>
		<Errors />
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/FaultChannelTest/FaultChannelTest.nivssdf sha256=b046e5e4d7430a7ecb841b7d95d6372bd51417d2326579776940c519e10eb405 bytes=137874 -->
## FILE: tests/testutilities/legacy_files/FaultChannelTest/FaultChannelTest.nivssdf

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/FaultChannelTest/FaultChannelTest.nivssdf`
- sha256: `b046e5e4d7430a7ecb841b7d95d6372bd51417d2326579776940c519e10eb405`
- bytes: 137874

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2010" Minor="0" Fix="0" Build="4" />
	<Content>Definition</Content>
	<Root Name="FaultChannelTest" TypeGUID="03D3BA22-1485-13A6-56BD17DA950CCD00">
		<Description>Test Fault Channel</Description>
		<Properties>
			<Property Name="Name">
				<String>FaultChannelTest</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.7</String>
			</Property>
			<Property Name="Creator">
				<String>Administrator</String>
			</Property>
			<Property Name="Creation Date">
				<Double>3324485326.515625</Double>
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
					<Channel Name="Max Streamed Channels" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="0">
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
					<Channel Name="FaultChannel0" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="DataSource">
								<DataSourceNode Channel="Targets Section/Controller/User Channel/ConstantValue" />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="FaultChannel1" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="FaultChannel2" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="FaultChannel3" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="FaultChannel4" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="FaultChannel5" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="FaultChannel6" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="FaultChannel7" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="FaultChannel8" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="FaultChannel9" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties />
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="TEST_ID" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>1</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>1879</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="ConstantValue" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>2</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>56594</Elem>
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
			<Alias Name="FaultChannel0" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/FaultChannel0" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="FaultChannel1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/FaultChannel1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="FaultChannel2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/FaultChannel2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="FaultChannel3" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/FaultChannel3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="FaultChannel4" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/FaultChannel4" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="FaultChannel5" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/FaultChannel5" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="FaultChannel6" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/FaultChannel6" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="FaultChannel7" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/FaultChannel7" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="FaultChannel8" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/FaultChannel8" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="FaultChannel9" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/FaultChannel9" />
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

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ModelParameterAPI_AUTOTEST/ModelParameterAPI_AUTOTEST.nivsprj sha256=eb6e79d070930b4c0f352f03f2c7eeb4b55f9a419ca01ae56a2be5e789a5475b bytes=2717 -->
## FILE: tests/testutilities/legacy_files/ModelParameterAPI_AUTOTEST/ModelParameterAPI_AUTOTEST.nivsprj

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ModelParameterAPI_AUTOTEST/ModelParameterAPI_AUTOTEST.nivsprj`
- sha256: `eb6e79d070930b4c0f352f03f2c7eeb4b55f9a419ca01ae56a2be5e789a5475b`
- bytes: 2717

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<SourceFile Checksum="E4DD93980756883C59602EC819D278ED0CA75FC562B7D7D45DDB528A5691CD104350929CBBDF6BC6C5F97C037F4ED823B99C5B69542180B979CD560F142D85FB" xmlns="http://www.ni.com/PlatformFramework">
	<SourceModelFeatureSet>
		<ParsableNamespace AssemblyFileVersion="9.6.0.49854" FeatureSetName="Editor" Name="http://www.ni.com/PlatformFramework" OldestCompatibleVersion="8.1.0.49152" Version="8.1.0.49152" />
		<ParsableNamespace AssemblyFileVersion="9.6.0.49854" FeatureSetName="VeriStand Core Components" Name="http://www.ni.com/VeriStand" OldestCompatibleVersion="9.0.0.49152" Version="9.0.0.49152" />
		<ApplicationVersionInfo Build="9.3.0.49854" Name="VeriStand" Version="9.6.0.49854" />
	</SourceModelFeatureSet>
	<Project p2:ProjectVersion="1.0.0.0" xmlns:p2="http://www.ni.com/VeriStand" xmlns="http://www.ni.com/PlatformFramework">
		<EnvoyManagerRootEnvoy Id="15994ba212e43358ee97455091182c3" ModelDefinitionType="EnvoyManagerRootEnvoy" Name="RootEnvoy" />
		<EmbeddedDefinitionReference Id="d581174782364bec8e65893ee631e0cb" ModelDefinitionType="NationalInstruments.ProjectExplorer.Modeling.ProjectDataManager" Name="ProjectExplorer">
			<ProjectExplorer />
		</EmbeddedDefinitionReference>
		<NameScopingEnvoy Id="9c22fe703a81435782608a94bc0471c5" ModelDefinitionType="DefaultTarget" Name="DefaultTarget">
			<DefaultTarget />
			<EmbeddedDefinitionReference Id="8eee80089fe842cab3b3fe62e122628a" ModelDefinitionType="GatewayDefinition" Name="Gateway" Reparentable="False">
				<p2:GatewayDefinition />
			</EmbeddedDefinitionReference>
			<FileReference Bindings=".nivsproj" Id="c4828ad0f53c49d9bd5397642eed4878" ModelDefinitionType="{http://www.ni.com/PlatformFramework}ExternalFile" Name="ModelParameterAPI_AUTOTEST.nivsproj" StoragePath="ModelParameterAPI_AUTOTEST.nivsproj" />
			<SourceFileReference Bindings="EnvoyManager" Id="83a274b6fbe34ea3b224c53c08e0391a" ModelDefinitionType="{http://www.ni.com/VeriStand}SystemDefinition" Name="ModelParameterAPI_AUTOTEST.nivssdf" StoragePath="ModelParameterAPI_AUTOTEST.nivssdf" />
			<FileReference Bindings=".nivsscreen" Id="6c9ec24e04324005bb953967786165b0" ModelDefinitionType="{http://www.ni.com/PlatformFramework}ExternalFile" Name="ModelParameterAPI_AUTOTEST.nivsscreen" StoragePath="ModelParameterAPI_AUTOTEST.nivsscreen" />
			<EmbeddedDefinitionReference Id="77424b0dface4e2e8ac68cbd76e90fec" ModelDefinitionType="SdfFilePath" Name="SdfPath" Reparentable="False">
				<p2:SdfFilePath SdfPath="ModelParameterAPI_AUTOTEST.nivssdf" />
			</EmbeddedDefinitionReference>
		</NameScopingEnvoy>
	</Project>
	<ProjectInformation xmlns="http://www.ni.com/PlatformFramework" />
</SourceFile>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ModelParameterAPI_AUTOTEST/ModelParameterAPI_AUTOTEST.nivsproj sha256=e68f4b4269aae29126afacd599517d040296520def94f9f8b112b100dc6c1bbe bytes=14112 -->
## FILE: tests/testutilities/legacy_files/ModelParameterAPI_AUTOTEST/ModelParameterAPI_AUTOTEST.nivsproj

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ModelParameterAPI_AUTOTEST/ModelParameterAPI_AUTOTEST.nivsproj`
- sha256: `e68f4b4269aae29126afacd599517d040296520def94f9f8b112b100dc6c1bbe`
- bytes: 14112

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2020" Minor="0" Fix="0" Build="0" />
	<Content>Definition</Content>
	<Root Name="ModelParameterAPI_AUTOTEST" TypeGUID="d9313aae-3554-45e5-93f3-86454275d4f2" Identifier="f29f8f80-7fef-44d0-9f35-0d3f00ad0523">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>ModelParameterAPI_AUTOTEST</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.0</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3351079551.2373185</Double>
			</Property>
		</Properties>
		<Errors />
		<Section Name="System Definition File" TypeGUID="b9227a5b-2770-4a62-8621-ac414d4124fb" Identifier="aec7951f-d2ab-4677-8165-1baf8778aeab">
			<Description />
			<Properties />
			<Errors />
			<Section Name="ModelParameterAPI_AUTOTEST.nivssdf" TypeGUID="3a41ca74-36ec-4aff-9219-9d05c8f91208" Identifier="3acda691-1383-4743-b773-e19e26847f05">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="ModelParameterAPI_AUTOTEST.nivssdf">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5>eb4abf3d93bd7b3b51ea8672888c94e9</MD5>
						</DependentFile>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="User Interface" TypeGUID="bc98486f-7b49-4949-9504-949cbe254c85" Identifier="1d9d4cf2-d070-4a54-baf6-7998b65a4fda">
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
						<Data>AAAG6wkAgAAAAAAIAA5AMP////8ETmFtZQAAEkAw/////whGdW5jdGlvbgAAYQDxAAAAAAAAAAETVG9vbGJhciBCdXR0b25zLmN0bABFQBYAAwROb25lF1N0aW11bHVzIFByb2ZpbGUgRWRpdG9yC0RhdGEgVmlld2VyAAAOVG9vbGJhciBCdXR0b24AAVMA8QAAAAAAAAABH2VudW1fVXNlciBBZG1pbiBQZXJtaXNzaW9ucy5jdGwBK0AWAA0HRGVmYXVsdA5BZG1pbmlzdHJhdGlvbhdDaGFubmVsIFNjYWxpbmcgVXRpbGl0eRFBZGQgRGlzcGxheSBJdGVtcxNDaGFuZ2UgVXNlciBQcm9maWxlI0VkaXQgU3RpbXVsdXMgUHJvZmlsZSBFZGl0b3IgSGVhZGVyGkVkaXQgRGlzcGxheSBJdGVtIFNldHRpbmdzG01vZGVsIFBhcmFtZXRlciBDYWxpYnJhdGlvbhJSdW50aW1lIEFsYXJtIEVkaXQPRWRpdCBUb29scyBNZW51FkVkaXQgRW5naW5lIENvbXBvbmVudHMaQ29uZmlndXJlIFZpc2libGUgQ2hhbm5lbHMNRmF1bHQgTWFuYWdlcgAAClBlcm1pc3Npb24AABpAMv////8QQ3VzdG9tIFRvb2wgUGF0aAAAdwDxx+1IGQAAAAIRTklWU19TaGFyZWQubHZsaWINUGF0aCB0eXBlLmN0bABPQBYABAhBYnNvbHV0ZQhSZWxhdGl2ZQ5Ub0NvbW1vbkRvY0RpcgxUb0FwcERhdGFEaXIAFUN1c3RvbSBUb29sIFBhdGggVHlwZQBjAPEAAAAAAAAAAhpOSVZTUHJval9GaWxlbWFuYWdlci5sdmxpYhlUb29scyBNZW51IEl0ZW1zIFR5cGUuY3RsACZAUAAGAAAAAQACAAMABAAFD1Rvb2xzIE1lbnUgSXRlbQAeQEAAAf////8ABhBUb29scyBNZW51IEl0ZW1zAAABAAcAAAARAAAADUFsYXJtIE1vbml0b3IAAAAUc3ViX0FsYXJtIE1vbml0b3IudmkAAAABUFRIMAAAAAQAAAAAAAAAAAAXTW9kZWwgUGFyYW1ldGVyIE1hbmFnZXIAAAAaTW9kZWwgUGFyYW1ldGVyIE1hbmFnZXIudmkAAAABUFRIMAAAAAQAAAAAAAAAAAABLQAAAAEtAAAAAVBUSDAAAAAEAAAAAAAAAAAAF1N0aW11bHVzIFByb2ZpbGUgRWRpdG9yAAAAGlN0aW11bHVzIFByb2ZpbGUgRWRpdG9yLnZpAAEAAVBUSDAAAAAEAAAAAAAAAAAAIFN0aW11bHVzIFByb2ZpbGUgU2VxdWVuY2UgRWRpdG9yAAAAFlRlc3QgRWRpdG9yIChCYXRjaCkudmkAAAABUFRIMAAAAAQAAAAAAAAAAAABLQAAAAEtAAAAAVBUSDAAAAAEAAAAAAAAAAAAHUNoYW5uZWwgU2NhbGluZyAmIENhbGlicmF0aW9uAAAAEnN1Yl9DYWxpYnJhdGlvbi52aQAAAAFQVEgwAAAABAAAAAAAAAAAABVDaGFubmVsIEZhdWx0IE1hbmFnZXIAAAAUc2NyX0ZhdWx0IE1hbmFnZXIudmkAAAABUFRIMAAAAAQAAAAAAAAAAAABLQAAAAEtAAAAAVBUSDAAAAAEAAAAAAAAAAAADk1hY3JvIFJlY29yZGVyAAAAMFdvcmtzcGFjZSBNYWNyb1xSZWNvcmRlclBsYXllclxNYWNybyBSZWNvcmRlci52aQAAAAFQVEgwAAAABAAAAAAAAAAAAAxNYWNybyBQbGF5ZXIAAAAuV29ya3NwYWNlIE1hY3JvXFJlY29yZGVyUGxheWVyXE1hY3JvIFBsYXllci52aQAAAAFQVEgwAAAABAAAAAAAAAAAAAEtAAAAAS0AAAABUFRIMAAAAAQAAAAAAAAAAAAQWE5FVCBCdXMgTW9uaXRvcgAAACRYTkVUIEJ1cyBNb25pdG9yXFhORVQgQnVzIE1vbml0b3IudmkAAAABUFRIMAAAAAQAAAAAAAAAAAABLQAAAAEtAAAAAVBUSDAAAAAEAAAAAAAAAAAAE0NoYW5uZWwgRGF0YSBWaWV3ZXIAAAAWQ2hhbm5lbCBEYXRhIFZpZXdlci52aQAAAAFQVEgwAAAABAAAAAAAAAAAAA5Db25zb2xlIFZpZXdlcgAAABJWaWV3IFJUIENvbnNvbGUudmkAAAABUFRIMAAAAAQAAAAAAAAAAAAQVERNUyBGaWxlIFZpZXdlcgAAABdzY3JfVERNUyBEYXRhIFZpZXdlci52aQACAAFQVEgwAAAABAAAAAAAAAAAAAA=</Data>
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
			<Section Name="Screens" TypeGUID="cdfadfe0-c84a-4268-a677-4f2f3525465e" Identifier="a85a3af1-d51c-4a06-812f-8f97accc704e">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="ModelParameterAPI_AUTOTEST.nivsscreen">
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
		<Section Name="Services" TypeGUID="736a951c-d9c8-457f-96a9-cd0ef16011a5" Identifier="9ab6d443-e8aa-4a27-a0f1-5eabc0e63dd8">
			<Description />
			<Properties />
			<Errors />
			<Section Name="Model Parameter Manager" TypeGUID="cc686646-9933-410d-a553-6308e6e06897" Identifier="016ce052-d9fd-49ca-88d5-2f014a772715">
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
		<Section Name="Profiles" TypeGUID="c3bd79ec-3336-4b06-868e-3217c640edd5" Identifier="a04af5b4-1919-486d-9edf-1377d9f1807c">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Calibration" TypeGUID="38433223-24A0-4b32-9339-370EC5AA31B4" Identifier="2556d5d2-b770-4339-be8a-39828efa7ff9">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Alarm Responses" TypeGUID="3b1ab560-d77a-41f2-adb4-0c0250b010b3" Identifier="03b5473f-086d-4c6b-aa47-09c3e7af45d7">
			<Description />
			<Properties />
			<Errors />
			<Section Name="Response High" TypeGUID="99267DF5-8C59-4AAC-B020-7591F4886206" Identifier="2de723b9-615c-46e4-b61a-e4a6f6fef0e6">
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
			<Section Name="Response Med" TypeGUID="99267DF5-8C59-4AAC-B020-7591F4886206" Identifier="673c878f-64f3-41de-84ca-e910fda0c7d1">
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
			<Section Name="Response Low" TypeGUID="99267DF5-8C59-4AAC-B020-7591F4886206" Identifier="55988c12-a490-4c03-8756-8b5aff2ae997">
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
		<Section Name="Custom Files" TypeGUID="9e2cb626-3583-4345-aeb6-b9fead6ec565" Identifier="d5614697-7ebc-4ec0-b81c-7f493ae77999">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Dependencies" TypeGUID="e5b093fa-a709-4df2-807e-a403422ba675" Identifier="13ffbe4c-50ab-49fa-9eb0-726b831cf429">
			<Description />
			<Properties />
			<Errors />
			<Section Name="ModelParameterAPI_AUTOTEST.nivssdf" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666" Identifier="a5b91f3d-49b2-422e-992c-b1fd924df457">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\virtual\Desktop\AutoTestProjects\ModelParameterAPI_AUTOTEST\ModelParameterAPI_AUTOTEST.nivssdf</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="ModelParameterAPI_AUTOTEST.nivsscreen" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666" Identifier="c290bdc0-a725-4c0e-a416-8d9c64036f22">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\virtual\Desktop\AutoTestProjects\ModelParameterAPI_AUTOTEST\ModelParameterAPI_AUTOTEST.nivsscreen</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="VectorModelInOutParam.dll" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666" Identifier="67d05f76-7f92-4ee0-8d0a-be16d907d0a1">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\virtual\Desktop\AutoTestProjects\ModelParameterAPI_AUTOTEST\VectorModelInOutParam.dll</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="VectorModelInOutNonWorkspace.dll" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666" Identifier="db2060f3-1428-44b3-ba13-3cd026579abb">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\virtual\Desktop\AutoTestProjects\ModelParameterAPI_AUTOTEST\VectorModelInOutNonWorkspace.dll</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="clocktest.dll" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666" Identifier="a59792fe-202e-4c48-b782-a7cb526d958d">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\virtual\Desktop\AutoTestProjects\ModelParameterAPI_AUTOTEST\clocktest.dll</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="sinewave.dll" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666" Identifier="1e400a77-36db-43e6-8e01-8462c32f0437">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\virtual\Desktop\AutoTestProjects\ModelParameterAPI_AUTOTEST\sinewave.dll</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ModelParameterAPI_AUTOTEST/ModelParameterAPI_AUTOTEST.nivsscreen sha256=4a250ed79307061cf7a3eabbe3e8c93af7c78d164a30beb8cf5e00fe9269fac3 bytes=18254 -->
## FILE: tests/testutilities/legacy_files/ModelParameterAPI_AUTOTEST/ModelParameterAPI_AUTOTEST.nivsscreen

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ModelParameterAPI_AUTOTEST/ModelParameterAPI_AUTOTEST.nivsscreen`
- sha256: `4a250ed79307061cf7a3eabbe3e8c93af7c78d164a30beb8cf5e00fe9269fac3`
- bytes: 18254

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
					<Data>AAAx+QkAgAAAAABYABRAMP////8LVGVtcGxhdGUgVkkAEUADAApQb3NpdGlvbiBYAAARQAMAClBvc2l0aW9uIFkAABBAMP////8GQ3VzdG9tAAAUQCEOU2hvdyBUaXRsZSBCYXIAAAlAAwACSUQAABJAIQ1BbHdheXMgT24gVG9wABJAIQxBbGxvdyBSZXNpemUAABRAIQ5BbGxvdyBNaW5pbWl6ZQAAEEAhC0FsbG93IENsb3NlABRAIQ5TaXplIHRvIFNjcmVlbgAAD0ADAAlTY3JlZW4uSUQAGUAWAAIGTm9ybWFsA05ldwAABVN0YXRlAA5AMP////8FVGl0bGUACUACAANbMF0ACUACAANbMV0ACUACAANbMl0ACUACAANbM10AHEBQAAQADgAPABAAEQ1XaW5kb3cgQm91bmRzABFACAALQ2hhbm5lbCBSZWYADkAw/////wRVbml0AAAUQCEORGVmYXVsdCBVbml0cz8AABJAIQxGbGFzaCBMaW1pdD8AAA1ABwAHQ29sb3IgMQANQAcAB0NvbG9yIDIADUAHAAdDb2xvciAzAA1ABwAHQ29sb3IgNAAPQAcACUJjayBDb2xvcgARQAcACkZvcmUgQ29sb3IAAA1ACgAHTGltaXQgMQANQAoAB0xpbWl0IDIADUAKAAdMaW1pdCAzAA1ACgAHTGltaXQgNAATQAMADExpbWl0IE1vZGUgMQAAE0ADAAxMaW1pdCBNb2RlIDIAABNAAwAMTGltaXQgTW9kZSAzAAATQAMADExpbWl0IE1vZGUgNAAAFUADAA9TY2FsZSBQcmVjaXNpb24AD0AKAAlTY2FsZSBNaW4AD0AKAAlTY2FsZSBNYXgADUADAAZGb3JtYXQAAA9AAwAJUHJlY2lzaW9uABVAAwAPQmFja2dyb3VuZCBUeXBlABFAAwALVmFyaWFibGUgSUQAEEBAAAH/////ACsDSURzABRAMP////8LVmFyaWFibGUgSUQAEkBAAAH/////AC0FVW5pdHMAFEBAAAH/////AC0GTGFiZWxzAAATQAoADFNjYWxlIEZhY3RvcgAAE0AKAAxTY2FsZSBPZmZzZXQAABFABwALVmFyaWFibGUgSUQAGkBAAAH/////ADIMWVNjYWxlIEluZGV4AAANQAUABkZvcm1hdAAAD0AFAAlQcmVjaXNpb24ACUAFAANGaXQADkAw/////wVMYWJlbAAWQCERVXNlIERlZmF1bHQgTGFiZWwAEkAhDUxhYmVsIFZpc2libGUACUAKAANNaW4ACUAKAANNYXgASwDxAAAAAAAAAAEgY2x1c3Rlcl9HcmFwaCBTY2FsZSBTZXR0aW5ncy5jdGwAIkBQAAgANAA1ADYANwA4ADkAOgA7BlhTY2FsZQAAFEBAAAH/////ADwHWVNjYWxlcwAPQAUACUJhciBTdHlsZQANQAIAB0ZpbGwgVG8AE0AHAAxGaWxsL1B0Q29sb3IAABFABQAKTGluZSBTdHlsZQAAEUAFAApMaW5lIFdpZHRoAAALQAcABUNvbG9yAA1ABQAGSW50ZXJwAAARQAUAC1BvaW50IFN0eWxlAEgA8QAAAAAAAAABH2NsdXN0ZXJfR3JhcGggUGxvdCBTZXR0aW5ncy5jdGwAIEBQAAgAPgA/AEAAQQBCAEMARABFBFBsb3QAABJAQAAB/////wBGBVBsb3RzABNACgANVXBkYXRlIFBlcmlvZAAVQAoADkhpc3RvcnkgTGVuZ3RoAAAUQHAACAAAAAIAAAZNeS5SZWYAABBAIQtJcyBDb250cm9sPwAWQDD/////DENoYW5uZWwgUGF0aAAAGkBAAAH/////AEwNQ2hhbm5lbCBQYXRocwAQQFMLQ3VzdG9tIERhdGEAqwDxxieWWAAAAAEgY2x1c3Rlcl9TY3JlZW4gSXRlbSBTZXR0aW5ncy5jdGwAgkBQADYAAAABAAIAAwAEAAUABgAHAAgACQAKAAsADAANABIAEwAUABUAFgAXABgAGQAaABsAHAAdAB4AHwAgACEAIgAjACQAJQAmACcAKAApACoALAAuAC8AMAAxADMAPAA9AEcASABJAEoASwBNAE4LU2NyZWVuIEl0ZW0AEkBAAAH/////AE8FSXRlbXMADkAw/////wROYW1lAAAUQDD/////C0Rlc2NyaXB0aW9uAVMA8QAAAAAAAAABH2VudW1fVXNlciBBZG1pbiBQZXJtaXNzaW9ucy5jdGwBK0AWAA0HRGVmYXVsdA5BZG1pbmlzdHJhdGlvbhdDaGFubmVsIFNjYWxpbmcgVXRpbGl0eRFBZGQgRGlzcGxheSBJdGVtcxNDaGFuZ2UgVXNlciBQcm9maWxlI0VkaXQgU3RpbXVsdXMgUHJvZmlsZSBFZGl0b3IgSGVhZGVyGkVkaXQgRGlzcGxheSBJdGVtIFNldHRpbmdzG01vZGVsIFBhcmFtZXRlciBDYWxpYnJhdGlvbhJSdW50aW1lIEFsYXJtIEVkaXQPRWRpdCBUb29scyBNZW51FkVkaXQgRW5naW5lIENvbXBvbmVudHMaQ29uZmlndXJlIFZpc2libGUgQ2hhbm5lbHMNRmF1bHQgTWFuYWdlcgAAClBlcm1pc3Npb24AAAxAIQdMb2FkZWQ/ABRAIQ9BbHdheXMgVmlzaWJsZT8AVwDxAAAAAAAAAAEkY2x1c3Rlcl9FbnRpcmUgU2NyZWVuIERlZmluaXRpb24uY3RsACpAUAAKAFAAUQBSAAUAAQACAAYAUwBUAFULU2NyZWVuLkRhdGEAJkBAAAH/////AFYZU2NyZWVuIEl0ZW0gQ2x1c3RlciBBcnJheQABAFcAAAABAAAAGwAAACRNb2RlbCBDYWxpYnJhdGlvbiBDb250cm9sIC0gQXJyYXkudmkAAAAAAAAAAAAAAAAAAAAeogABAAAAAAAe2AAAAAAAF1ZlY3RNb2QvMmJ5M1BhcmFtL1ZhbHVlAPoCCALCAq7//////////wAAAAABAADvAAAA7wAAAP/+AAD//gAA////AAAAAAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEBZAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAF1ZlY3RNb2QvMmJ5M1BhcmFtL1ZhbHVlP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7HABUAAAAAAACQCAAAAAAAEABAAAAAEAAAAAAAAAAAAkTW9kZWwgQ2FsaWJyYXRpb24gQ29udHJvbCAtIEFycmF5LnZpAAAAAAAAAAAAAAAAAAAADgcAAQAAAAAAHtgAAAAAABdWZWN0TW9kLzVieTFQYXJhbS9WYWx1ZQD6AV4CwgIE//////////8AAAAAAQAA7wAAAO8AAAD//gAA//4AAP///wAAAAAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAWQAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAQAAABdWZWN0TW9kLzVieTFQYXJhbS9WYWx1ZT/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOzQAVUAAAAAAAkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAAAXwBAAAAAAAAHtgAAAAAAAkyYnkzUGFyYW0CxgJYA44ClQAAAAAAAAGxAAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADtMAFaAAAAAAEAAABaVGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvU2ltdWxhdGlvbiBNb2RlbHMvTW9kZWxzL1ZlY3RNb2QvUGFyYW1ldGVycy8yYnkzUGFyYW0vMmJ5M1BhcmFtCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAjsgEAAAAAAAAe2AAAAAAACTJieTNQYXJhbQNcAlgEJAKVAAAAAAAAAbEAAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO2gAWAAAAAAAQAAAFpUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9TaW11bGF0aW9uIE1vZGVscy9Nb2RlbHMvVmVjdE1vZC9QYXJhbWV0ZXJzLzJieTNQYXJhbS8yYnkzUGFyYW0JAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAACH8AQAAAAAAAB7YAAAAAAAJMmJ5M1BhcmFtA/ICWAS6ApUAAAAAAAABsQAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7iABZwAAAAABAAAAWlRhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL1NpbXVsYXRpb24gTW9kZWxzL01vZGVscy9WZWN0TW9kL1BhcmFtZXRlcnMvMmJ5M1BhcmFtLzJieTNQYXJhbQkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAAAp0BAAAAAAAAHtgAAAAAAAkyYnkzUGFyYW0CxgIcA44CWf//////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADukAFtAAAAAAEAAABaVGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvU2ltdWxhdGlvbiBNb2RlbHMvTW9kZWxzL1ZlY3RNb2QvUGFyYW1ldGVycy8yYnkzUGFyYW0vMmJ5M1BhcmFtCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAiKQEAAAAAAAAe2AAAAAAACTJieTNQYXJhbQNcAhwEJAJZAAAAAAAAAbEAAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO8AAXMAAAAAAQAAAFpUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9TaW11bGF0aW9uIE1vZGVscy9Nb2RlbHMvVmVjdE1vZC9QYXJhbWV0ZXJzLzJieTNQYXJhbS8yYnkzUGFyYW0JAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAAARYAQAAAAAAAB7YAAAAAAAJMmJ5M1BhcmFtA/ICHAS6AlkAAAAAAAABsQAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA73ABeQAAAAABAAAAWlRhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL1NpbXVsYXRpb24gTW9kZWxzL01vZGVscy9WZWN0TW9kL1BhcmFtZXRlcnMvMmJ5M1BhcmFtLzJieTNQYXJhbQkAgAAAAAABAAQAAAABAAAAAAAAAAAAJE1vZGVsIENhbGlicmF0aW9uIENvbnRyb2wgLSBBcnJheS52aQAAAAAAAAAAAAAAAAAAACHYAAEAAAAAAB7YAAAAAAAXVmVjdE1vZC8xYnk1UGFyYW0vVmFsdWUCxgFeBI4CBP//////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAD///8AAAAAAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQFkAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAEAAAAXVmVjdE1vZC8xYnk1UGFyYW0vVmFsdWU/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADv4AF/AAAAAAAJAIAAAAAAAQAEAAAAAQAAAAAAAAAAACNNb2RlbCBDYWxpYnJhdGlvbiBDb250cm9sIC0gTGlzdC52aQAAAAAAAAAAAAAAAAAAAAk7AAAAAAAAAB7YAAAAAAAQQ2FsaWJyYXRpb24gTGlzdAEOAGQC1wEJ//////////8AAAAAAQAA7wAAAO8AAAD//gAA//4AAP///wAAAAAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAWQAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAABQAAAAlBbXBsaXR1ZGUAAAAEQmlhcwAAAAlGcmVxdWVuY3kAAAAER2FpbgAAAAVQaGFzZT/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPBAAYQAAAAAAAkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAACakBAAAAAAAAHtgAAAAAAAk1YnkxUGFyYW0AMgISAPoCTwAAAAAAAAGzAAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwsAGKAAAAAAEAAABaVGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvU2ltdWxhdGlvbiBNb2RlbHMvTW9kZWxzL1ZlY3RNb2QvUGFyYW1ldGVycy81YnkxUGFyYW0vNWJ5MVBhcmFtCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAALvwEAAAAAAAAe2AAAAAAACTVieTFQYXJhbQAyAdYA+gITAAAAAAAAAbMAAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPEgAZAAAAAAAQAAAFpUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9TaW11bGF0aW9uIE1vZGVscy9Nb2RlbHMvVmVjdE1vZC9QYXJhbWV0ZXJzLzVieTFQYXJhbS81YnkxUGFyYW0JAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAAB/YAQAAAAAAAB7YAAAAAAAJNWJ5MVBhcmFtADIBmgD6AdcAAAAAAAABswAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8ZABlgAAAAABAAAAWlRhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL1NpbXVsYXRpb24gTW9kZWxzL01vZGVscy9WZWN0TW9kL1BhcmFtZXRlcnMvNWJ5MVBhcmFtLzVieTFQYXJhbQkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAADJkBAAAAAAAAHtgAAAAAAAk1YnkxUGFyYW0AMgFeAPoBmwAAAAAAAAGzAAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADyAAGcAAAAAAEAAABaVGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvU2ltdWxhdGlvbiBNb2RlbHMvTW9kZWxzL1ZlY3RNb2QvUGFyYW1ldGVycy81YnkxUGFyYW0vNWJ5MVBhcmFtCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAcUgEAAAAAAAAe2AAAAAAACTVieTFQYXJhbQAyASIA+gFf//////////8AAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPJwAaIAAAAAAQAAAFpUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9TaW11bGF0aW9uIE1vZGVscy9Nb2RlbHMvVmVjdE1vZC9QYXJhbWV0ZXJzLzVieTFQYXJhbS81YnkxUGFyYW0JAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAAASSAQAAAAAAAB7YAAAAAAAJMWJ5NVBhcmFtAXIBGAI6AVX//////////wAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8uABqAAAAAABAAAAWlRhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL1NpbXVsYXRpb24gTW9kZWxzL01vZGVscy9WZWN0TW9kL1BhcmFtZXRlcnMvMWJ5NVBhcmFtLzFieTVQYXJhbQkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAADi4BAAAAAAAAHtgAAAAAAAkxYnk1UGFyYW0CCAEYAtABVQAAAAAAAAGvAAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADzUAGuAAAAAAEAAABaVGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvU2ltdWxhdGlvbiBNb2RlbHMvTW9kZWxzL1ZlY3RNb2QvUGFyYW1ldGVycy8xYnk1UGFyYW0vMWJ5NVBhcmFtCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAABvAEAAAAAAAAe2AAAAAAACTFieTVQYXJhbQKeARgDZgFVAAAAAAAAAa8AAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPPAAbQAAAAAAQAAAFpUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9TaW11bGF0aW9uIE1vZGVscy9Nb2RlbHMvVmVjdE1vZC9QYXJhbWV0ZXJzLzFieTVQYXJhbS8xYnk1UGFyYW0JAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAACUgAQAAAAAAAB7YAAAAAAAJMWJ5NVBhcmFtAzQBGAP8AVUAAAAAAAABrwAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA9DABugAAAAABAAAAWlRhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL1NpbXVsYXRpb24gTW9kZWxzL01vZGVscy9WZWN0TW9kL1BhcmFtZXRlcnMvMWJ5NVBhcmFtLzFieTVQYXJhbQkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAADXoBAAAAAAAAHtgAAAAAAAkxYnk1UGFyYW0DygEYBJIBVQAAAAAAAAGvAAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD0oAHAAAAAAAEAAABaVGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvU2ltdWxhdGlvbiBNb2RlbHMvTW9kZWxzL1ZlY3RNb2QvUGFyYW1ldGVycy8xYnk1UGFyYW0vMWJ5NVBhcmFtCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAUbwEAAAAAAAAe2AAAAAAABVBoYXNlA6wAtAR0APH//////////wAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA9RABxgAAAAABAAAATVRhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL1NpbXVsYXRpb24gTW9kZWxzL01vZGVscy9zaW5ld2F2ZS9QYXJhbWV0ZXJzL1BoYXNlCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAaWAEAAAAAAAAe2AAAAAAABEdhaW4DrAB4BHQAtf//////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD1gAHMAAAAAAEAAABMVGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvU2ltdWxhdGlvbiBNb2RlbHMvTW9kZWxzL3NpbmV3YXZlL1BhcmFtZXRlcnMvR2FpbgkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAAC1UBAAAAAAAAHtgAAAAAAAlGcmVxdWVuY3kC5ADSA6wBD///////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD18AHSAAAAAAEAAABRVGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvU2ltdWxhdGlvbiBNb2RlbHMvTW9kZWxzL3NpbmV3YXZlL1BhcmFtZXRlcnMvRnJlcXVlbmN5CQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAO3gEAAAAAAAAe2AAAAAAABEJpYXMC5ACWA6wA0///////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD2YAHYAAAAAAEAAABMVGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvU2ltdWxhdGlvbiBNb2RlbHMvTW9kZWxzL3NpbmV3YXZlL1BhcmFtZXRlcnMvQmlhcwkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAAD/oBAAAAAAAAHtgAAAAAAAlBbXBsaXR1ZGUC5ABaA6wAl///////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD2wAHdAAAAAAEAAABRVGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvU2ltdWxhdGlvbiBNb2RlbHMvTW9kZWxzL3NpbmV3YXZlL1BhcmFtZXRlcnMvQW1wbGl0dWRlCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAYTW9kZWwgLSBNb2RlbCBDb250cm9sLnZpAAAAAAAAAAAAAAAAAAAAIG4BAAAAAAAAHtgAAAAAAAljbG9ja3Rlc3QAPABaAPIAvgAAAAAAAAHLAAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAAAAAAAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQFkAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD3QAHkAAAAAAEAAAA9VGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvU2ltdWxhdGlvbiBNb2RlbHMvTW9kZWxzL2Nsb2NrdGVzdAkAgAAAAAABAAQAAAABAAAAAAAAAAAAGE1vZGVsIC0gTW9kZWwgQ29udHJvbC52aQAAAAAAAAAAAAAAAAAAAACTAQAAAAAAAB7YAAAAAAAHVmVjdE1vZAA8AL4A8gEiAAAAAAAAAaoAAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAAAAAAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAWQAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPeQAegAAAAAAQAAADtUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9TaW11bGF0aW9uIE1vZGVscy9Nb2RlbHMvVmVjdE1vZAkAgAAAAAABAAQAAAABAAAAAAAAAAAADEVtcHR5IFNjcmVlbgAAAAAAAB7YAAAAAAAAAAAAAAABAAAAAAA=</Data>
				</Variant>
			</Property>
			<Property Name="Screen Order">
				<I32Array>
					<Elem>7896</Elem>
				</I32Array>
			</Property>
			<Property Name="EscapeEnabled">
				<Boolean>false</Boolean>
			</Property>
			<Property Name="ShowPropPageOnDrop">
				<Boolean>true</Boolean>
			</Property>
			<Property Name="Workspace Loc and Size Left">
				<U16>36</U16>
			</Property>
			<Property Name="Workspace Loc and Size Top">
				<U16>45</U16>
			</Property>
			<Property Name="Workspace Loc and Size Right">
				<U16>1243</U16>
			</Property>
			<Property Name="Workspace Loc and Size Bottom">
				<U16>777</U16>
			</Property>
		</Properties>
		<Errors />
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ModelParameterAPI_AUTOTEST/ModelParameterAPI_AUTOTEST.nivssdf sha256=af81a2678313788b9a0cb0000d117813ca33a6346f5e067042eba289cf4f8a3a bytes=113672 -->
## FILE: tests/testutilities/legacy_files/ModelParameterAPI_AUTOTEST/ModelParameterAPI_AUTOTEST.nivssdf

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ModelParameterAPI_AUTOTEST/ModelParameterAPI_AUTOTEST.nivssdf`
- sha256: `af81a2678313788b9a0cb0000d117813ca33a6346f5e067042eba289cf4f8a3a`
- bytes: 113672

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2010" Minor="0" Fix="0" Build="4" />
	<Content>Definition</Content>
	<Root Name="ModelParameterAPI_AUTOTEST" TypeGUID="03D3BA22-1485-13A6-56BD17DA950CCD00">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>ModelParameterAPI_AUTOTEST</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.10</String>
			</Property>
			<Property Name="Creator">
				<String>Administrator</String>
			</Property>
			<Property Name="Creation Date">
				<Double>3319713756.4602208</Double>
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
						<Section Name="VectModWorkspace" TypeGUID="03D3B9C4-1485-13A6-561FC9BB21813875">
							<Description />
							<Properties>
								<Property Name="Base Rate">
									<Double>0</Double>
								</Property>
								<Property Name="Build Data">
									<Variant>
										<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
										<Data>AAAAFAkAgAAAAAABAAQAAAABAAAAAAAA</Data>
									</Variant>
								</Property>
								<Property Name="DLL Size">
									<I32>65536</I32>
								</Property>
								<Property Name="DLL Timestamp">
									<Double>0</Double>
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
									<Double>0</Double>
								</Property>
								<Property Name="blocks only">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="visible">
									<U32>0</U32>
								</Property>
								<Property Name="DLL Path">
									<DependentFile Type="Relative" Path="VectorModelInOutParam.dll">
										<Version />
										<ForceDownload>false</ForceDownload>
										<RTDestination>c:\ni-rt\NIVeriStand2010\Models\VectorModelInOutParam.dll</RTDestination>
										<SupportedTarget>PharLap &amp; Windows</SupportedTarget>
										<MD5>652e0d20cd75caa79d1c947b5dd2f8b4</MD5>
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
								<Property Name="Segment Vectors">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="MD5">
									<String>652e0d20cd75caa79d1c947b5dd2f8b4</String>
								</Property>
								<Property Name="NIVeriStandServer Port">
									<U32>0</U32>
								</Property>
							</Properties>
							<Errors />
							<Section Name="Inports" TypeGUID="03D3B9E3-1485-13A6-56035B19B2245EB3">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="1by5In" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="5" Units="" BitFields="7">
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
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="2by3In" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="2" ColDim="3" Units="" BitFields="7">
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
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="5by1In" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="5" ColDim="1" Units="" BitFields="7">
									<Description />
									<Properties>
										<Property Name="ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Index">
											<I32>2</I32>
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
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Outports" TypeGUID="03D3B9F3-1485-13A6-5698C14838D6AA3C">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="2by3Out" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="2" ColDim="3" Units="" BitFields="5">
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
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="5by1Out" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="5" ColDim="1" Units="" BitFields="5">
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
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="1by5Out" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="5" Units="" BitFields="5">
									<Description />
									<Properties>
										<Property Name="ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Index">
											<I32>2</I32>
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
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Execution" TypeGUID="03D3BA9F-1485-13A6-56E3D5196780015F">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Model Command" TypeGUID="03D3BABE-1485-13A6-56C34B877844B2C1" RowDim="1" ColDim="1" Units="" BitFields="11">
									<Description />
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
									<Description />
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
								<Channel Name="CONST1by5" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="1" ColDim="5" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Added">
											<Boolean>false</Boolean>
										</Property>
										<Property Name="Data Type">
											<I32>14</I32>
										</Property>
										<Property Name="Dep.Vars">
											<String>CONST1by5</String>
										</Property>
										<Property Name="Expression">
											<String>CONST1by5</String>
										</Property>
										<Property Name="Group ID">
											<I32>-1</I32>
										</Property>
										<Property Name="ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Mapped ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Model Path">
											<String>vectormodelinoutparam/CONST1by5</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>0</I32>
										</Property>
										<Property Name="Type">
											<U16>3</U16>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>1</Elem>
										<Elem>2</Elem>
										<Elem>3</Elem>
										<Elem>4</Elem>
										<Elem>5</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="CONST2by3" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="2" ColDim="3" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Added">
											<Boolean>false</Boolean>
										</Property>
										<Property Name="Data Type">
											<I32>15</I32>
										</Property>
										<Property Name="Dep.Vars">
											<String>CONST2by3</String>
										</Property>
										<Property Name="Expression">
											<String>CONST2by3</String>
										</Property>
										<Property Name="Group ID">
											<I32>-1</I32>
										</Property>
										<Property Name="ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Mapped ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Model Path">
											<String>vectormodelinoutparam/CONST2by3</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>1</I32>
										</Property>
										<Property Name="Type">
											<U16>3</U16>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>1</Elem>
										<Elem>10</Elem>
										<Elem>2</Elem>
										<Elem>20</Elem>
										<Elem>3</Elem>
										<Elem>30</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="CONST5by1" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="5" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Added">
											<Boolean>false</Boolean>
										</Property>
										<Property Name="Data Type">
											<I32>16</I32>
										</Property>
										<Property Name="Dep.Vars">
											<String>CONST5by1</String>
										</Property>
										<Property Name="Expression">
											<String>CONST5by1</String>
										</Property>
										<Property Name="Group ID">
											<I32>-1</I32>
										</Property>
										<Property Name="ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Mapped ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Model Path">
											<String>vectormodelinoutparam/CONST5by1</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>2</I32>
										</Property>
										<Property Name="Type">
											<U16>3</U16>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>1</Elem>
										<Elem>2</Elem>
										<Elem>3</Elem>
										<Elem>4</Elem>
										<Elem>5</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Signals" TypeGUID="03D3BA31-1485-13A6-567CA69E9D2E71D5">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
						<Section Name="VectMod" TypeGUID="03D3B9C4-1485-13A6-561FC9BB21813875">
							<Description />
							<Properties>
								<Property Name="Base Rate">
									<Double>0</Double>
								</Property>
								<Property Name="Build Data">
									<Variant>
										<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
										<Data>AAAAFAkAgAAAAAABAAQAAAABAAAAAAAA</Data>
									</Variant>
								</Property>
								<Property Name="DLL Size">
									<I32>65536</I32>
								</Property>
								<Property Name="DLL Timestamp">
									<Double>0</Double>
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
									<Double>0</Double>
								</Property>
								<Property Name="blocks only">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="visible">
									<U32>0</U32>
								</Property>
								<Property Name="DLL Path">
									<DependentFile Type="Relative" Path="VectorModelInOutNonWorkspace.dll">
										<Version />
										<ForceDownload>false</ForceDownload>
										<RTDestination>c:\ni-rt\NIVeriStand2010\Models\VectorModelInOutNonWorkspace.dll</RTDestination>
										<SupportedTarget>PharLap &amp; Windows</SupportedTarget>
										<MD5>ed64b36ed7bd4a2d3947c502614a38f3</MD5>
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
								<Property Name="Segment Vectors">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="MD5">
									<String>ed64b36ed7bd4a2d3947c502614a38f3</String>
								</Property>
								<Property Name="NIVeriStandServer Port">
									<U32>0</U32>
								</Property>
							</Properties>
							<Errors />
							<Section Name="Inports" TypeGUID="03D3B9E3-1485-13A6-56035B19B2245EB3">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="1by5In" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="5" Units="" BitFields="7">
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
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="2by3In" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="2" ColDim="3" Units="" BitFields="7">
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
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="5by1In" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="5" ColDim="1" Units="" BitFields="7">
									<Description />
									<Properties>
										<Property Name="ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Index">
											<I32>2</I32>
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
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Outports" TypeGUID="03D3B9F3-1485-13A6-5698C14838D6AA3C">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="2by3Out" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="2" ColDim="3" Units="" BitFields="5">
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
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="5by1Out" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="5" ColDim="1" Units="" BitFields="5">
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
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="1by5Out" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="5" Units="" BitFields="5">
									<Description />
									<Properties>
										<Property Name="ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Index">
											<I32>2</I32>
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
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Execution" TypeGUID="03D3BA9F-1485-13A6-56E3D5196780015F">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Model Command" TypeGUID="03D3BABE-1485-13A6-56C34B877844B2C1" RowDim="1" ColDim="1" Units="" BitFields="11">
									<Description />
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
									<Description />
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
								<Section Name="1by5Param" TypeGUID="03D3B9D3-1485-13A6-56351D6DFA577AE9">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="1by5Param" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="1" ColDim="5" Units="" BitFields="1">
										<Description />
										<Properties>
											<Property Name="Added">
												<Boolean>false</Boolean>
											</Property>
											<Property Name="Data Type">
												<I32>14</I32>
											</Property>
											<Property Name="Dep.Vars">
												<String>vectormodelinoutnonworkspace/1by5Param/Value</String>
											</Property>
											<Property Name="Expression">
												<String>vectormodelinoutnonworkspace/1by5Param/Value</String>
											</Property>
											<Property Name="Group ID">
												<I32>-1</I32>
											</Property>
											<Property Name="ID">
												<I32>-1</I32>
											</Property>
											<Property Name="Mapped ID">
												<I32>-1</I32>
											</Property>
											<Property Name="Model Path">
												<String>vectormodelinoutnonworkspace/1by5Param/Value</String>
											</Property>
											<Property Name="Parameter Index">
												<I32>2</I32>
											</Property>
											<Property Name="Type">
												<U16>3</U16>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>1</Elem>
											<Elem>2</Elem>
											<Elem>3</Elem>
											<Elem>4</Elem>
											<Elem>5</Elem>
										</DefaultValue>
									</Channel>
								</Section>
								<Section Name="2by3Param" TypeGUID="03D3B9D3-1485-13A6-56351D6DFA577AE9">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="2by3Param" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="2" ColDim="3" Units="" BitFields="1">
										<Description />
										<Properties>
											<Property Name="Added">
												<Boolean>false</Boolean>
											</Property>
											<Property Name="Data Type">
												<I32>15</I32>
											</Property>
											<Property Name="Dep.Vars">
												<String>vectormodelinoutnonworkspace/2by3Param/Value</String>
											</Property>
											<Property Name="Expression">
												<String>vectormodelinoutnonworkspace/2by3Param/Value</String>
											</Property>
											<Property Name="Group ID">
												<I32>-1</I32>
											</Property>
											<Property Name="ID">
												<I32>-1</I32>
											</Property>
											<Property Name="Mapped ID">
												<I32>-1</I32>
											</Property>
											<Property Name="Model Path">
												<String>vectormodelinoutnonworkspace/2by3Param/Value</String>
											</Property>
											<Property Name="Parameter Index">
												<I32>0</I32>
											</Property>
											<Property Name="Type">
												<U16>3</U16>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>1</Elem>
											<Elem>10</Elem>
											<Elem>2</Elem>
											<Elem>20</Elem>
											<Elem>3</Elem>
											<Elem>30</Elem>
										</DefaultValue>
									</Channel>
								</Section>
								<Section Name="5by1Param" TypeGUID="03D3B9D3-1485-13A6-56351D6DFA577AE9">
									<Description />
									<Properties />
									<Errors />
									<Channel Name="5by1Param" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="5" ColDim="1" Units="" BitFields="1">
										<Description />
										<Properties>
											<Property Name="Added">
												<Boolean>false</Boolean>
											</Property>
											<Property Name="Data Type">
												<I32>16</I32>
											</Property>
											<Property Name="Dep.Vars">
												<String>vectormodelinoutnonworkspace/5by1Param/Value</String>
											</Property>
											<Property Name="Expression">
												<String>vectormodelinoutnonworkspace/5by1Param/Value</String>
											</Property>
											<Property Name="Group ID">
												<I32>-1</I32>
											</Property>
											<Property Name="ID">
												<I32>-1</I32>
											</Property>
											<Property Name="Mapped ID">
												<I32>-1</I32>
											</Property>
											<Property Name="Model Path">
												<String>vectormodelinoutnonworkspace/5by1Param/Value</String>
											</Property>
											<Property Name="Parameter Index">
												<I32>1</I32>
											</Property>
											<Property Name="Type">
												<U16>3</U16>
											</Property>
										</Properties>
										<Errors />
										<DefaultValue>
											<Elem>1</Elem>
											<Elem>2</Elem>
											<Elem>3</Elem>
											<Elem>4</Elem>
											<Elem>5</Elem>
										</DefaultValue>
									</Channel>
								</Section>
							</Section>
							<Section Name="Signals" TypeGUID="03D3BA31-1485-13A6-567CA69E9D2E71D5">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
						<Section Name="VectModWorkspace2" TypeGUID="03D3B9C4-1485-13A6-561FC9BB21813875">
							<Description />
							<Properties>
								<Property Name="Base Rate">
									<Double>0</Double>
								</Property>
								<Property Name="Build Data">
									<Variant>
										<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
										<Data>AAAAFAkAgAAAAAABAAQAAAABAAAAAAAA</Data>
									</Variant>
								</Property>
								<Property Name="DLL Size">
									<I32>65536</I32>
								</Property>
								<Property Name="DLL Timestamp">
									<Double>0</Double>
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
									<Double>0</Double>
								</Property>
								<Property Name="blocks only">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="visible">
									<U32>0</U32>
								</Property>
								<Property Name="DLL Path">
									<DependentFile Type="Relative" Path="VectorModelInOutParam.dll">
										<Version />
										<ForceDownload>false</ForceDownload>
										<RTDestination>c:\ni-rt\NIVeriStand2010\Models\VectorModelInOutParam.dll</RTDestination>
										<SupportedTarget>PharLap &amp; Windows</SupportedTarget>
										<MD5>652e0d20cd75caa79d1c947b5dd2f8b4</MD5>
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
								<Property Name="Segment Vectors">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="MD5">
									<String>652e0d20cd75caa79d1c947b5dd2f8b4</String>
								</Property>
								<Property Name="NIVeriStandServer Port">
									<U32>0</U32>
								</Property>
							</Properties>
							<Errors />
							<Section Name="Inports" TypeGUID="03D3B9E3-1485-13A6-56035B19B2245EB3">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="1by5In" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="5" Units="" BitFields="7">
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
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="2by3In" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="2" ColDim="3" Units="" BitFields="7">
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
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="5by1In" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="5" ColDim="1" Units="" BitFields="7">
									<Description />
									<Properties>
										<Property Name="ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Index">
											<I32>2</I32>
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
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Outports" TypeGUID="03D3B9F3-1485-13A6-5698C14838D6AA3C">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="2by3Out" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="2" ColDim="3" Units="" BitFields="5">
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
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="5by1Out" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="5" ColDim="1" Units="" BitFields="5">
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
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="1by5Out" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="5" Units="" BitFields="5">
									<Description />
									<Properties>
										<Property Name="ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Index">
											<I32>2</I32>
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
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Execution" TypeGUID="03D3BA9F-1485-13A6-56E3D5196780015F">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Model Command" TypeGUID="03D3BABE-1485-13A6-56C34B877844B2C1" RowDim="1" ColDim="1" Units="" BitFields="11">
									<Description />
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
									<Description />
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
								<Channel Name="CONST1by5" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="1" ColDim="5" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Added">
											<Boolean>false</Boolean>
										</Property>
										<Property Name="Data Type">
											<I32>14</I32>
										</Property>
										<Property Name="Dep.Vars">
											<String>CONST1by5</String>
										</Property>
										<Property Name="Expression">
											<String>CONST1by5</String>
										</Property>
										<Property Name="Group ID">
											<I32>-1</I32>
										</Property>
										<Property Name="ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Mapped ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Model Path">
											<String>vectormodelinoutparam/CONST1by5</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>0</I32>
										</Property>
										<Property Name="Type">
											<U16>3</U16>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>1</Elem>
										<Elem>2</Elem>
										<Elem>3</Elem>
										<Elem>4</Elem>
										<Elem>5</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="CONST2by3" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="2" ColDim="3" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Added">
											<Boolean>false</Boolean>
										</Property>
										<Property Name="Data Type">
											<I32>15</I32>
										</Property>
										<Property Name="Dep.Vars">
											<String>CONST2by3</String>
										</Property>
										<Property Name="Expression">
											<String>CONST2by3</String>
										</Property>
										<Property Name="Group ID">
											<I32>-1</I32>
										</Property>
										<Property Name="ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Mapped ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Model Path">
											<String>vectormodelinoutparam/CONST2by3</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>1</I32>
										</Property>
										<Property Name="Type">
											<U16>3</U16>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>1</Elem>
										<Elem>10</Elem>
										<Elem>2</Elem>
										<Elem>20</Elem>
										<Elem>3</Elem>
										<Elem>30</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="CONST5by1" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="5" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Added">
											<Boolean>false</Boolean>
										</Property>
										<Property Name="Data Type">
											<I32>16</I32>
										</Property>
										<Property Name="Dep.Vars">
											<String>CONST5by1</String>
										</Property>
										<Property Name="Expression">
											<String>CONST5by1</String>
										</Property>
										<Property Name="Group ID">
											<I32>-1</I32>
										</Property>
										<Property Name="ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Mapped ID">
											<I32>-1</I32>
										</Property>
										<Property Name="Model Path">
											<String>vectormodelinoutparam/CONST5by1</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>2</I32>
										</Property>
										<Property Name="Type">
											<U16>3</U16>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>1</Elem>
										<Elem>2</Elem>
										<Elem>3</Elem>
										<Elem>4</Elem>
										<Elem>5</Elem>
									</DefaultValue>
								</Channel>
							</Section>
							<Section Name="Signals" TypeGUID="03D3BA31-1485-13A6-567CA69E9D2E71D5">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
						<Section Name="clocktest" TypeGUID="03D3B9C4-1485-13A6-561FC9BB21813875">
							<Description />
							<Properties>
								<Property Name="Base Rate">
									<Double>0</Double>
								</Property>
								<Property Name="Build Data">
									<Variant>
										<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
										<Data>AAAAFAkAgAAAAAABAAQAAAABAAAAAAAA</Data>
									</Variant>
								</Property>
								<Property Name="DLL Size">
									<I32>143360</I32>
								</Property>
								<Property Name="DLL Timestamp">
									<Double>0</Double>
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
									<String>b8080dd1c4daf175256174e4a54367a1</String>
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
									<Double>0</Double>
								</Property>
								<Property Name="blocks only">
									<Boolean>false</Boolean>
								</Property>
								<Property Name="visible">
									<U32>0</U32>
								</Property>
								<Property Name="DLL Path">
									<DependentFile Type="Relative" Path="clocktest.dll">
										<Version />
										<ForceDownload>false</ForceDownload>
										<RTDestination>c:\ni-rt\NIVeriStand2010\Models\clocktest.dll</RTDestination>
										<SupportedTarget>PharLap &amp; Windows</SupportedTarget>
										<MD5>b8080dd1c4daf175256174e4a54367a1</MD5>
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
							</Section>
							<Section Name="Outports" TypeGUID="03D3B9F3-1485-13A6-5698C14838D6AA3C">
								<Description />
								<Properties />
								<Errors />
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
						<Section Name="sinewave" TypeGUID="03D3B9C4-1485-13A6-561FC9BB21813875">
							<Description />
							<Properties>
								<Property Name="Base Rate">
									<Double>0</Double>
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
									<Double>0</Double>
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
									<Double>0</Double>
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
									<String>854e31b31a325f1175c026374631107b</String>
								</Property>
								<Property Name="NIVeriStandServer Port">
									<U32>6012</U32>
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
							<Section Name="Inports" TypeGUID="03D3B9E3-1485-13A6-56035B19B2245EB3">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="In1" TypeGUID="03D3B985-1485-13A6-56FC3200A1C00087" RowDim="1" ColDim="1" Units="" BitFields="7">
									<Description />
									<Properties>
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
								<Channel Name="Out1" TypeGUID="03D3B995-1485-13A6-56ABA0860ADF91DF" RowDim="1" ColDim="1" Units="" BitFields="5">
									<Description />
									<Properties>
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
							<Section Name="Parameters" TypeGUID="03D3BB0C-1485-13A6-56E10CEFF755E7D3">
								<Description />
								<Properties />
								<Errors />
								<Channel Name="Amplitude" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>sinewave/Amplitude</String>
										</Property>
										<Property Name="Expression">
											<String>Amplitude</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>0</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>1.2</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Bias" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>sinewave/Bias</String>
										</Property>
										<Property Name="Expression">
											<String>Bias</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>1</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0.8</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Frequency" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>sinewave/Frequency</String>
										</Property>
										<Property Name="Expression">
											<String>Frequency</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>2</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>2</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Phase" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>sinewave/Phase</String>
										</Property>
										<Property Name="Expression">
											<String>Phase</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>3</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>0</Elem>
									</DefaultValue>
								</Channel>
								<Channel Name="Gain" TypeGUID="03D3B9A5-1485-13A6-56C6D6209A7E7998" RowDim="1" ColDim="1" Units="" BitFields="1">
									<Description />
									<Properties>
										<Property Name="Model Path">
											<String>sinewave/Gain</String>
										</Property>
										<Property Name="Expression">
											<String>Gain</String>
										</Property>
										<Property Name="Parameter Index">
											<I32>4</I32>
										</Property>
									</Properties>
									<Errors />
									<DefaultValue>
										<Elem>3</Elem>
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
							<Elem>1122</Elem>
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
			<Alias Name="TEST_ID" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Channel/TEST_ID" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectModWorkspace_1by5In" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectModWorkspace/Inports/1by5In" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectModWorkspace_2by3In" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectModWorkspace/Inports/2by3In" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectModWorkspace_5by1In" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectModWorkspace/Inports/5by1In" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectModWorkspace_2by3Out" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectModWorkspace/Outports/2by3Out" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectModWorkspace_5by1Out" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectModWorkspace/Outports/5by1Out" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectModWorkspace_1by5Out" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectModWorkspace/Outports/1by5Out" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectModWorkspace_CONST1by5" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectModWorkspace/Parameters/CONST1by5" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectModWorkspace_CONST2by3" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectModWorkspace/Parameters/CONST2by3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectModWorkspace_CONST5by1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectModWorkspace/Parameters/CONST5by1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectMod_1by5In" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectMod/Inports/1by5In" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectMod_2by3In" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectMod/Inports/2by3In" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectMod_5by1In" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectMod/Inports/5by1In" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectMod_2by3Out" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectMod/Outports/2by3Out" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectMod_5by1Out" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectMod/Outports/5by1Out" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectMod_1by5Out" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectMod/Outports/1by5Out" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectMod_1by5Param" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectMod/Parameters/1by5Param/1by5Param" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectMod_2by3Param" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectMod/Parameters/2by3Param/2by3Param" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectMod_5by1Param" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectMod/Parameters/5by1Param/5by1Param" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectModWorkspace2_1by5In" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectModWorkspace2/Inports/1by5In" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectModWorkspace2_2by3In" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectModWorkspace2/Inports/2by3In" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectModWorkspace2_5by1In" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectModWorkspace2/Inports/5by1In" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectModWorkspace2_2by3Out" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectModWorkspace2/Outports/2by3Out" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectModWorkspace2_5by1Out" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectModWorkspace2/Outports/5by1Out" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectModWorkspace2_1by5Out" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectModWorkspace2/Outports/1by5Out" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectModWorkspace2_CONST1by5" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectModWorkspace2/Parameters/CONST1by5" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectModWorkspace2_CONST2by3" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectModWorkspace2/Parameters/CONST2by3" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="VectModWorkspace2_CONST5by1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Simulation Models/Models/VectModWorkspace2/Parameters/CONST5by1" />
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

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ProceduresTest/ProceduresTest.nivsproj sha256=df14162b0626a5c5f3831a9611168b0fca6fb00ae4bc8db6ed3cda703af6f34b bytes=10883 -->
## FILE: tests/testutilities/legacy_files/ProceduresTest/ProceduresTest.nivsproj

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ProceduresTest/ProceduresTest.nivsproj`
- sha256: `df14162b0626a5c5f3831a9611168b0fca6fb00ae4bc8db6ed3cda703af6f34b`
- bytes: 10883

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2012" Minor="0" Fix="0" Build="1" />
	<Content>Definition</Content>
	<Root Name="ProceduresTest" TypeGUID="d9313aae-3554-45e5-93f3-86454275d4f2">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>ProceduresTest</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.0</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3351079552.5965805</Double>
			</Property>
		</Properties>
		<Errors />
		<Section Name="System Definition File" TypeGUID="b9227a5b-2770-4a62-8621-ac414d4124fb">
			<Description />
			<Properties />
			<Errors />
			<Section Name="ProceduresTest.nivssdf" TypeGUID="3a41ca74-36ec-4aff-9219-9d05c8f91208">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="ProceduresTest.nivssdf">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5>e83994c13bf07dd9f40ad304a4576ec5</MD5>
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
						<DependentFile Type="Relative" Path="ProceduresTest.nivsscreen">
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
			<Section Name="ProceduresTest.nivssdf" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2014\AutoTestProjects\ProceduresTest\ProceduresTest.nivssdf</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="ProceduresTest.nivsscreen" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2014\AutoTestProjects\ProceduresTest\ProceduresTest.nivsscreen</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/ProceduresTest/ProceduresTest.nivsscreen sha256=760a9df2aee8e5b1b3e4eafdd9a7723322b6004400e45f99b2f6de70e581b17d bytes=6820 -->
## FILE: tests/testutilities/legacy_files/ProceduresTest/ProceduresTest.nivsscreen

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/ProceduresTest/ProceduresTest.nivsscreen`
- sha256: `760a9df2aee8e5b1b3e4eafdd9a7723322b6004400e45f99b2f6de70e581b17d`
- bytes: 6820

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
					<Data>AAAQeAkAgAAAAABYABRAMP////8LVGVtcGxhdGUgVkkAEUADAApQb3NpdGlvbiBYAAARQAMAClBvc2l0aW9uIFkAABBAMP////8GQ3VzdG9tAAAUQCEOU2hvdyBUaXRsZSBCYXIAAAlAAwACSUQAABJAIQ1BbHdheXMgT24gVG9wABJAIQxBbGxvdyBSZXNpemUAABRAIQ5BbGxvdyBNaW5pbWl6ZQAAEEAhC0FsbG93IENsb3NlABRAIQ5TaXplIHRvIFNjcmVlbgAAD0ADAAlTY3JlZW4uSUQAGUAWAAIGTm9ybWFsA05ldwAABVN0YXRlAA5AMP////8FVGl0bGUACUACAANbMF0ACUACAANbMV0ACUACAANbMl0ACUACAANbM10AHEBQAAQADgAPABAAEQ1XaW5kb3cgQm91bmRzABFACAALQ2hhbm5lbCBSZWYADkAw/////wRVbml0AAAUQCEORGVmYXVsdCBVbml0cz8AABJAIQxGbGFzaCBMaW1pdD8AAA1ABwAHQ29sb3IgMQANQAcAB0NvbG9yIDIADUAHAAdDb2xvciAzAA1ABwAHQ29sb3IgNAAPQAcACUJjayBDb2xvcgARQAcACkZvcmUgQ29sb3IAAA1ACgAHTGltaXQgMQANQAoAB0xpbWl0IDIADUAKAAdMaW1pdCAzAA1ACgAHTGltaXQgNAATQAMADExpbWl0IE1vZGUgMQAAE0ADAAxMaW1pdCBNb2RlIDIAABNAAwAMTGltaXQgTW9kZSAzAAATQAMADExpbWl0IE1vZGUgNAAAFUADAA9TY2FsZSBQcmVjaXNpb24AD0AKAAlTY2FsZSBNaW4AD0AKAAlTY2FsZSBNYXgADUADAAZGb3JtYXQAAA9AAwAJUHJlY2lzaW9uABVAAwAPQmFja2dyb3VuZCBUeXBlABFAAwALVmFyaWFibGUgSUQAEEBAAAH/////ACsDSURzABRAMP////8LVmFyaWFibGUgSUQAEkBAAAH/////AC0FVW5pdHMAFEBAAAH/////AC0GTGFiZWxzAAATQAoADFNjYWxlIEZhY3RvcgAAE0AKAAxTY2FsZSBPZmZzZXQAABFABwALVmFyaWFibGUgSUQAGkBAAAH/////ADIMWVNjYWxlIEluZGV4AAANQAUABkZvcm1hdAAAD0AFAAlQcmVjaXNpb24ACUAFAANGaXQADkAw/////wVMYWJlbAAWQCERVXNlIERlZmF1bHQgTGFiZWwAEkAhDUxhYmVsIFZpc2libGUACUAKAANNaW4ACUAKAANNYXgASwDxAAAAAAAAAAEgY2x1c3Rlcl9HcmFwaCBTY2FsZSBTZXR0aW5ncy5jdGwAIkBQAAgANAA1ADYANwA4ADkAOgA7BlhTY2FsZQAAFEBAAAH/////ADwHWVNjYWxlcwAPQAUACUJhciBTdHlsZQANQAIAB0ZpbGwgVG8AE0AHAAxGaWxsL1B0Q29sb3IAABFABQAKTGluZSBTdHlsZQAAEUAFAApMaW5lIFdpZHRoAAALQAcABUNvbG9yAA1ABQAGSW50ZXJwAAARQAUAC1BvaW50IFN0eWxlAEgA8QAAAAAAAAABH2NsdXN0ZXJfR3JhcGggUGxvdCBTZXR0aW5ncy5jdGwAIEBQAAgAPgA/AEAAQQBCAEMARABFBFBsb3QAABJAQAAB/////wBGBVBsb3RzABNACgANVXBkYXRlIFBlcmlvZAAVQAoADkhpc3RvcnkgTGVuZ3RoAAAUQHAACAAAAAIAAAZNeS5SZWYAABBAIQtJcyBDb250cm9sPwAWQDD/////DENoYW5uZWwgUGF0aAAAGkBAAAH/////AEwNQ2hhbm5lbCBQYXRocwAQQFMLQ3VzdG9tIERhdGEAqwDxxieWWAAAAAEgY2x1c3Rlcl9TY3JlZW4gSXRlbSBTZXR0aW5ncy5jdGwAgkBQADYAAAABAAIAAwAEAAUABgAHAAgACQAKAAsADAANABIAEwAUABUAFgAXABgAGQAaABsAHAAdAB4AHwAgACEAIgAjACQAJQAmACcAKAApACoALAAuAC8AMAAxADMAPAA9AEcASABJAEoASwBNAE4LU2NyZWVuIEl0ZW0AEkBAAAH/////AE8FSXRlbXMADkAw/////wROYW1lAAAUQDD/////C0Rlc2NyaXB0aW9uAVMA8QAAAAAAAAABH2VudW1fVXNlciBBZG1pbiBQZXJtaXNzaW9ucy5jdGwBK0AWAA0HRGVmYXVsdA5BZG1pbmlzdHJhdGlvbhdDaGFubmVsIFNjYWxpbmcgVXRpbGl0eRFBZGQgRGlzcGxheSBJdGVtcxNDaGFuZ2UgVXNlciBQcm9maWxlI0VkaXQgU3RpbXVsdXMgUHJvZmlsZSBFZGl0b3IgSGVhZGVyGkVkaXQgRGlzcGxheSBJdGVtIFNldHRpbmdzG01vZGVsIFBhcmFtZXRlciBDYWxpYnJhdGlvbhJSdW50aW1lIEFsYXJtIEVkaXQPRWRpdCBUb29scyBNZW51FkVkaXQgRW5naW5lIENvbXBvbmVudHMaQ29uZmlndXJlIFZpc2libGUgQ2hhbm5lbHMNRmF1bHQgTWFuYWdlcgAAClBlcm1pc3Npb24AAAxAIQdMb2FkZWQ/ABRAIQ9BbHdheXMgVmlzaWJsZT8AVwDxAAAAAAAAAAEkY2x1c3Rlcl9FbnRpcmUgU2NyZWVuIERlZmluaXRpb24uY3RsACpAUAAKAFAAUQBSAAUAAQACAAYAUwBUAFULU2NyZWVuLkRhdGEAJkBAAAH/////AFYZU2NyZWVuIEl0ZW0gQ2x1c3RlciBBcnJheQABAFcAAAABAAAABgAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAACapAQAAAAAAABgzAAAAAAAVQWxhcm0gMiBUcmlnZ2VyIENvdW50AbgAyAKAAQUAAACxAAAk+gAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4JABUgAAAAABAAAAFUFsYXJtIDIgVHJpZ2dlciBDb3VudAkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAAFSIBAAAAAAAAGDMAAAAAABVBbGFybSAxIFRyaWdnZXIgQ291bnQA8ADIAbgBBQAAALIAACT7AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADg8AFOAAAAAAEAAAAVQWxhcm0gMSBUcmlnZ2VyIENvdW50CQCAAAAAAAEABAAAAAEAAAAAAAAAAAAbTnVtZXJpYyBDb250cm9sIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAAHVwBAAAAAAAAGDMAAAAAAA9BbGFybSBDaGFubmVsIDIBuACMAoAAyf//////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADhYAFWAQAAAAEAAAAPQWxhcm0gQ2hhbm5lbCAyCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAbTnVtZXJpYyBDb250cm9sIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAADPkBAAAAAAAAGDMAAAAAAA9BbGFybSBDaGFubmVsIDEA8ACMAbgAyf//////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADhwAFDAQAAAAEAAAAPQWxhcm0gQ2hhbm5lbCAxCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAbTnVtZXJpYyBDb250cm9sIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAAG7wBAAAAAAAAGDMAAAAAAA5UZXN0IENoYW5uZWwgNQAoAMgA8AEF//////////8AAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOJAATQBAAAAAQAAAA5UZXN0IENoYW5uZWwgNQkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAAGvQBAAAAAAAAGDMAAAAAAAtTeXN0ZW0gVGltZQAoAIwA8ADJ//////////8AAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOKwAWAAAAAAAQAAAAtTeXN0ZW0gVGltZQkAgAAAAAABAAQAAAABAAAAAAAAAAAADEVtcHR5IFNjcmVlbgAAAAAAABgzAAAAAAAAAAAAAAABAAAAAAA=</Data>
				</Variant>
			</Property>
			<Property Name="Screen Order">
				<I32Array>
					<Elem>6195</Elem>
				</I32Array>
			</Property>
			<Property Name="EscapeEnabled">
				<Boolean>false</Boolean>
			</Property>
			<Property Name="ShowPropPageOnDrop">
				<Boolean>true</Boolean>
			</Property>
			<Property Name="Workspace Loc and Size Left">
				<U16>359</U16>
			</Property>
			<Property Name="Workspace Loc and Size Top">
				<U16>118</U16>
			</Property>
			<Property Name="Workspace Loc and Size Right">
				<U16>1856</U16>
			</Property>
			<Property Name="Workspace Loc and Size Bottom">
				<U16>898</U16>
			</Property>
		</Properties>
		<Errors />
	</Root>
</Document>
````
