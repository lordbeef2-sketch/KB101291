# NI DOCUMENT BUNDLE: using-eye-scan-flexrio-high-speed-serial

<!--NI_BUNDLE_CHUNK bundle=using-eye-scan-flexrio-high-speed-serial start=1 end=2 -->
<!--NI_TOPIC bundle=using-eye-scan-flexrio-high-speed-serial path=configure-eyescan.html language=enus -->
## TOPIC 00001: Configuring the Eye Scan API

- bundle_id: `using-eye-scan-flexrio-high-speed-serial`
- source_path: `configure-eyescan.html`
- source_url: https://docs-be.ni.com/bundle/using-eye-scan-flexrio-high-speed-serial/raw/resource/enus/configure-eyescan.html
- document_id: `using-eye-scan-flexrio-high-speed-serial`
- page_type: `leaf`
- content_type: `concept`
- source_description: To debug link connections in your FlexRIO high-speed serial application, use the Eye Scan API located on the NI Eye Scan palette at FPGA Interface»Software-Designed Instrument»NI High-Speed Serial»NI Eye Scan. The Eye Scan API offers two types of Eye Scan:Rectangular Eye Scan obtains a traditional e

Configuring the Eye Scan API

To debug link connections in your FlexRIO high-speed serial application, use the Eye Scan API
 located on the NI Eye Scan palette at FPGA Interface»Software-Designed Instrument»NI High-Speed Serial»NI Eye
 Scan.

- Rectangular Eye Scan obtains a traditional eye that sweeps the unit interval and
 nominal voltage.
- N Point Eye Scan measures the Bit Error Ratio at arbitrary unit intervals and
 nominal voltage offsets. org.dita.html5/xsl/topic.xsl 455 Note The
 Aurora Streaming example projects do not include an example of N Point Eye
 Scan. To use N Point Eye Scan, refer to the example in *Programming Eye
 Scan to Debug Link Connections*.

#### Connecting Signals to Enable Eye Scan

Note

#### Using the Create GTH AXI4-Lite VI

Create GTH AXI4-Lite

Add Address Map Element

Note

Create GTY
 AXI4-Lite.vi

Figure 1.

[IMAGE alt='1378' src='GUID-58BD46BB-E02C-4B20-99C2-9FBBAF686371-a5.png']

#### Connecting CLIP Resources to the Instruction
 Framework

Create GTH AXI4-Lite

Note

Create GTH AXI4-Lite

Add Subsystems.vi

Figure 2.

[IMAGE alt='1378' src='GUID-2E608101-BDF0-4D1C-8C08-31BAA69DF2D7-a5.png']

Refer to the following figure for the AXI DRP Channel CLIP Resources.

Figure 3.

[IMAGE alt='1378' src='GUID-EF7F5A0D-DCEE-43DB-B2A2-90838E1CEB88-a5.png']

<!--NI_TOPIC bundle=using-eye-scan-flexrio-high-speed-serial path=program-eye-scan-debug.html language=enus -->
## TOPIC 00002: Programming Eye Scan to Debug Link Connections

- bundle_id: `using-eye-scan-flexrio-high-speed-serial`
- source_path: `program-eye-scan-debug.html`
- source_url: https://docs-be.ni.com/bundle/using-eye-scan-flexrio-high-speed-serial/raw/resource/enus/program-eye-scan-debug.html
- document_id: `using-eye-scan-flexrio-high-speed-serial`
- page_type: `leaf`
- content_type: `reference`
- source_description: Understanding the Eye Scan State Model The Eye Scan API abstracts the Eye Scan algorithm provided by Xilinx into a simple API with few states. The general programming flow is as follows: Open Session»Configure Properties»Start»Measure»Close Session.You can loop measurements for frequent updates. Eye

Programming Eye Scan to Debug Link
 Connections

#### Understanding the Eye Scan State Model

Open Session»Configure Properties»Start»Measure»Close
 Session

Note

Figure 4.

[IMAGE alt='1378' src='GUID-50FE5B6C-4C58-4045-A1FA-D9D01545762C-a5.png']

#### Programming Eye Scan

1. Open a session with Open Session (Poly).vi.
2. Configure the properties using the Property Node, located on the NI
 Eye Scan VI palette (FPGA Interface»Software-Designed Instruments»NI High-Speed
 Serial»NI Eye Scan). Some properties have default values, but you must configure the
 following properties before starting the scan: 
 Data Width
 Rx Output Divider
 Equalization Mode
 org.dita.html5/xsl/topic.xsl 455Note These properties
 must match the confiuration of the FPGA core in order for Eye Scan
 to work properly. Refer to your CLIP settings to determine the
 settings to specify for the properties above.
3. Call Start.vi to begin measuring on the first point.
4. Call Measure (Poly).vi. Once Eye Scan finishes measuring
 the active point, it automatically reconfigures for the next point and begins
 measuring that point. This process continues until one of the following occurs: 
 Number of New Points Requested completes
 Every requested point is scanned
 org.dita.html5/xsl/topic.xsl 455Note To receive updates to the
 progress of Eye Scan while taking measurements and without using a large
 amount of computational resources, call Measure
 (Poly).vi with a a small timeout value in a loop.
 org.dita.html5/xsl/topic.xsl 455Note To stop Eye Scan before
 measurement is complete, call Stop.vi. Calling
 Stop.vi moves Eye Scan to the Stopped state and
 discards the data from the point currently being measured. Previously
 acquired points may no longer be obtained by calling Measure
 (Poly).vi. Once Eye Scan is stopped, you can reconfigure
 properties and call Start.vi to restart the
 measurement.
5. Once the last point has been measured, Eye Scan moves to the Finished state. In
 the Finished state, call Measure (Poly).vi to retrieve all
 previously acquired data since the last Start.vi call.
6. To begin a new Eye Scan, reconfigure and call Start.vi
 again. 
 org.dita.html5/xsl/topic.xsl 455Notice When you call
 Start.vi, all previously acquired data is
 discarded.

#### Rectangular and N Point Eye Scan
 Examples

Note

Horizontal Step
 Size

Vertical Step Size

Figure 5.

[IMAGE alt='1378' src='GUID-547D985D-9FB3-4B63-85A8-7779649E6208-a5.png']

Note

Array of Points to
 Measure

Figure 6.

[IMAGE alt='1378' src='GUID-D60AE67F-2941-46F9-82D6-B8182C630B80-a5.png']
