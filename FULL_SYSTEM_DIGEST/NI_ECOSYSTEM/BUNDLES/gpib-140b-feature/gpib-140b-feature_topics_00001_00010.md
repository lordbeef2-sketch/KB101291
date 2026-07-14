# NI DOCUMENT BUNDLE: gpib-140b-feature

<!--NI_BUNDLE_CHUNK bundle=gpib-140b-feature start=1 end=10 -->
<!--NI_TOPIC bundle=gpib-140b-feature path=basic-information.html language=enus -->
## TOPIC 00001: Basic Information

- bundle_id: `gpib-140b-feature`
- source_path: `basic-information.html`
- source_url: https://docs-be.ni.com/bundle/gpib-140b-feature/raw/resource/enus/basic-information.html
- document_id: `gpib-140b-feature`
- page_type: `leaf`
- content_type: `reference`
- source_description: This section provides general information about the GPIB-140B. Conventions GPIB-140B Refers to a GPIB extender that extends the GPIB to a maximum distance of 1 km. GPIB extender Refers to the bus extender. IEEE 488 and IEEE 488.2 Refers to the ANSI/IEEE Standard 488.1-1987 and the ANSI/IEEE Standard

Basic Information

This section provides general information about the GPIB-140B.

#### Conventions

| GPIB-140B | Refers to a GPIB extender that extends the GPIB to a maximum distance of 1 km. |
| --- | --- |
| GPIB extender | Refers to the bus extender. |
| IEEE 488 and IEEE 488.2 | Refers to the ANSI/IEEE Standard 488.1-1987 and the ANSI/IEEE Standard 488.2-1992, respectively, which define the GPIB. |

#### Kit Contents

- A GPIB-140B bus extender
- 12 V DC power supply This power adapter can be used with an input AC voltage
 between 100 V AC and 240 V AC. Verify that the voltage you will be using is
 in the input range of this power adapter. org.dita.html5/xsl/topic.xsl 455 Note If using a different adapter
 than what ships with the GPIB-140B, ensure that the adapter provides 9 V DC to 15 V DC and has appropriate safety certification marks for country of
 use.

#### Optional Equipment

The following table
 lists some cables available for the GPIB-140B. For a complete list of GPIB accessories and ordering information, refer to the
 pricing section of the *Fiber-Optic Cable* and *GPIB Cable*
 product pages at [ni.com](http://www.ni.com).

Note

GPIB-140B

| Cable/Accessory | Part Number |  |
| --- | --- | --- |
| GPIB T7 fiber-optic cable - extends up to 1 km (10 m to 1000 m lengths) | 182805-010/020/030/050/100/200/500/01K |  |
| Type X2 double-shielded cable with shielded plug/receptacles | 0.5 m: 763061-005 | 3 m: 763061-003 |
| 1 m: 763061-01 | 4 m: 763061-04 |  |
| 2 m: 763061-02 |  |  |

Note

#### Related
 Documentation

The following documents contain information that you may
 find helpful as you read this manual:

- GPIB 140B
 Specifications
- GPIB-140B Safety, Environmental, and
 Regulatory Information
- ANSI/IEEE Standard 488.1-1987, IEEE Standard Digital Interface for
 Programmable Instrumentation
- ANSI/IEEE Standard 488.2-1992, IEEE Standard Codes, Formats, Protocols, and Common
 Commands

Parent topic:

GPIB-140B User Manual

<!--NI_TOPIC bundle=gpib-140b-feature path=Chunk2021228355.html language=enus -->
## TOPIC 00002: Hardware Configuration

- bundle_id: `gpib-140b-feature`
- source_path: `Chunk2021228355.html`
- source_url: https://docs-be.ni.com/bundle/gpib-140b-feature/raw/resource/enus/Chunk2021228355.html
- document_id: `gpib-140b-feature`
- page_type: `leaf`
- content_type: `topic`
- source_description: Hardware Configuration This section describes how to configure the operation modes supported by the GPIB-140B. Data Transfer Modes The GPIB extender has two data transfer modes—unbuffered mode and buffered mode. The data transfer mode determines how data is transmitted across the extension. Selectin

Hardware Configuration

Parent topic:

GPIB-140B User Manual

#### Hardware Configuration

This section describes how to configure the operation modes supported by the GPIB-140B.

##### Data Transfer Modes

The GPIB extender has two data transfer modes—unbuffered mode and buffered mode. The data
 transfer mode determines how data is transmitted across the extension.

###### Selecting a Data Transfer Mode

Refer to the following descriptions when selecting a data transfer mode.

###### Unbuffered Mode

In unbuffered mode, each data byte is transmitted
 using the GPIB double-interlocked handshaking protocol. For long data streams, transfers are
 slower than transfers using buffered mode. However, the GPIB extension is transparent in
 unbuffered mode.

###### Buffered Mode

In buffered mode, the GPIB extenders use FIFO
 (first-in-first-out) buffers to buffer data between the remote and local units. For long
 data streams, the data throughput is much higher than with unbuffered mode.

However,
 a few applications may not operate properly in buffered mode. For example, a GPIB device on
 the local side of the extension is addressed to talk, another device on the remote side is
 addressed to listen. When the Talker sources data bytes, the GPIB extenders accept the data
 bytes and store them in a FIFO buffer. At the same time, the GPIB extenders read data from
 the FIFO buffer and source data bytes to the Listener. If the FIFO buffer contains data, the
 number of bytes sourced by the Talker differs from the number of bytes accepted by the
 Listener.

GPIB command bytes are not stored in the FIFO buffers; they are transmitted
 using the GPIB double-interlocked handshaking protocol.

###### Setting the Data Transfer Mode

The two GPIB extenders in your extension system must use the same data transfer mode.

To use buffered mode, set the BUFFERED TRANSFER DIP switch to the
 ON position, as shown in the following figure. To use unbuffered mode, set this switch
 to the OFF position.

Figure 9.

[IMAGE alt='1378' src='GUID-576D178A-81DD-4C24-A1A9-F3B8959C73FA-a5.svg']

##### HS488 Mode

The GPIB extender can handle data transfers using the HS488 protocol. HS488 transfers
 data between two or more devices using a noninterlocked handshaking protocol. You can
 use HS488 to transfer data at rates higher than rates possible using the IEEE 488
 protocol. For more information about HS488, refer to [Introduction to HS488](theory-of-operation.html#GUID-63036462-2CB4-4AD3-BAA5-CE21253C9CC3).

###### Selecting an HS488 Mode

Refer to the following descriptions when selecting the HS488 mode.

###### HS488 Disabled

If you disable HS488, the
 GPIB extender sources and accepts data using a three-wire handshaking protocol, even
 if both the Talker and Listener can transfer data using the HS488 protocol.

###### HS488 Enabled

After the Talker indicates
 that it wants to issue HS488 transfers, HS488 is enabled and the GPIB extender
 accepts data using the HS488 protocol. Also, when talking, the GPIB extender always
 tries to use the HS488 mode. In HS488 mode, FIFO buffers buffer data during HS488
 transfers, even if the data transfer mode is set to unbuffered. When you use the
 HS488 protocol with the GPIB extender, you should set the GPIB cable length to 5 m
 for both the local and the remote system. To do so, use your IEEE 488.2 software
 configuration utility.

###### Setting the HS488 Mode

The two GPIB extenders in your extension system do not need to use the same HS488 mode,
 however, the system uses the maximum data transfer rate when both sides in your
 extension system use HS488.

To enable HS488, set the HS488 ENABLED DIP switch to the ON
 position, as shown in the following figure. To disable HS488, set this switch to the OFF
 position.

Figure 10.

[IMAGE alt='1378' src='GUID-3F340BA7-73B0-48BD-A307-95F37B4FD390-a5.svg']

##### Parallel Poll Response Modes

According to IEEE 488, devices must respond to a parallel poll within 200 ns
 after the Controller-In-Charge (CIC) asserts the Identify (IDY)
 message—Attention (ATN) and End or Identify (EOI). The CIC waits at least 2
 µs before reading the Parallel Poll Response (PPR). In many cases, a remote
 device on an extended system cannot respond to parallel polls this quickly
 because of cable propagation delays. To solve this problem, use one of the
 following two solutions in your application:

- If possible, specify in your application that the CIC must allow enough
 time to receive the response. For more information, refer to Immediate PPR Mode . If you are using NI-488.2 software, you
 can use the NI-488.2 Configuration utility to set the amount
 of time that the CIC waits.
- Execute two consecutive parallel polls and use the second response. For
 more information, refer to Latched PPR Mode .

###### PPR Mode Considerations

When
 selecting a PPR mode, consider the type of Controller present in
 your GPIB system and the length of cable between the GPIB-140B extenders. However, if your application does not use parallel
 polls, you do not need to select a PPR mode.

Some Hewlett
 Packard GPIB Controllers remain in a parallel poll state with IDY
 asserted if they are not performing another function. A change in
 the response interrupts the application. In some Controllers, the
 IDY signal is toggled on and off, and you can change the duration of
 the signal to accommodate delayed responses over extenders. If you
 are using these types of Controllers, you should set the GPIB
 extender to immediate PPR mode.

Most other Controllers pulse
 the IDY signal for approximately 2 µs and expect a response within
 that time. If you are using this type of Controller and if the cable
 between the extenders is longer than 60 m, you should set the GPIB
 extender to latched PPR mode. For shorter cable distances, use
 immediate PPR mode.

The two GPIB extenders in your extension
 system do not need to use the same PPR mode. Select the PPR mode of
 the local GPIB extender based on the Controllers on the local GPIB
 system. Likewise, select the PPR mode of the remote GPIB extender
 based on the Controllers on the remote GPIB system. If no
 Controllers are physically connected to one of the GPIB extenders,
 the PPR mode of that GPIB extender has no effect on your
 system.

###### Selecting a PPR Mode

Refer to the following descriptions when selecting the PPR mode.

###### Immediate PPR Mode

In immediate PPR
 mode, the GPIB extenders do not use the internal PPR data register. When a
 Controller on the local system asserts IDY, the local extender sends the IDY message
 to the remote bus and the response is returned as fast as propagation delays permit.
 Your application must allow enough time to receive the response.

###### Latched PPR Mode

In latched PPR mode,
 the GPIB extenders use an internal PPR data register. When a Controller on the local
 system asserts IDY, the local extender sends the contents of the PPR data register
 to the local data lines. At the same time, a parallel poll message is sent to the
 remote bus. When the local system unasserts IDY, the PPR from the remote system is
 loaded into the internal PPR data register. Consequently, the register always
 contains the response of the previous complete poll. To obtain the response of both
 local and remote systems, your application should execute two consecutive parallel
 polls and use the second response.

The software driver library of most
 Controllers contains an easy-to-use parallel poll function. For example, if the
 function is called ibrpp and your application is written in BASIC,
 the sequence to execute a poll in latched PPR mode might be similar to the following
 sequence:

```text
CALL ibrpp (brd0%, ppr%)
CALL ibrpp (brd0%, ppr%)
IF ppr > 0 GOTO 300
```

###### Setting the PPR Mode

To enable immediate PPR mode, set the PARALLEL POLL IMMEDIATE DIP
 switch to the ON position, as shown in the following figure. To enable latched PPR mode,
 set this switch to the OFF position.

Figure 11.

[IMAGE alt='1378' src='GUID-7C82D7D0-6FF5-4330-88D9-C0044039A905-a5.svg']

<!--NI_TOPIC bundle=gpib-140b-feature path=connecting-hw.html language=enus -->
## TOPIC 00003: Hardware Connections

- bundle_id: `gpib-140b-feature`
- source_path: `connecting-hw.html`
- source_url: https://docs-be.ni.com/bundle/gpib-140b-feature/raw/resource/enus/connecting-hw.html
- document_id: `gpib-140b-feature`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section explains how to connect the GPIB-140B to the fiber-optic cables and power supply, and how to run a self test to verify operation. Connecting the Cables The GPIB-140B is designed for use with multi-mode fiber-optic cable. Do not use with single-mode cable. Complete the following steps to

Hardware Connections

This section explains how to connect the GPIB-140B to the fiber-optic cables and power supply, and how to run a self test to verify
 operation.

Parent topic:

GPIB-140B User Manual

#### Connecting the Cables

Note

GPIB-140B

Complete the following steps to connect a multi-mode fiber-optic cable to both GPIB
 extenders.

1. Make sure that each GPIB-140B extender is powered off.
2. Connect the two connectors on each end of the fiber-optic cable to your GPIB
 extenders, as follows:
  1. As shown in the following figure, align the connector marked T 
 (transmit) with the connector labeled TRANSMIT on
 the side of the GPIB extender. Align the connector marked
 R (receive) with the connector labeled
 RECEIVE on the side of the GPIB extender.
 Figure 7.Connecting the
 Fiber-Optic Cable to Both GPIB Extenders 
[IMAGE alt='1378' src='GUID-7BCAC759-E4C7-4F06-875A-7F0CDD462EB8-a5.svg']
  2. Remove the caps on the connectors.
  3. Align the notch on each cable connector to the slot of the fiber-optic connector on the
 GPIB extender.
  4. Firmly push in the cable connector and rotate the sleeve clockwise until it locks on to
 the side notch of the fiber-optic connector on the GPIB extender.
3. Connect the end of the extender with the GPIB connector to your GPIB system.
 Make sure to follow all IEEE 488 cabling restrictions. For typical restrictions,
 refer to Configuration Requirements .

#### Connecting the External Power Supply

Complete the following steps to connect the external power supply.

1. Plug the utility power cord of your 12 V DC power supply into a 100 V AC to 240 V AC
 electrical outlet.
2. Plug the other end of the power cord into the power supply.
3. Connect the 12 V DC output of the power supply into the DC power connector on the GPIB-140B by rotating the sleeve by hand until it is firmly screwed in place.
4. Power on the GPIB-140B extender; the POWER LED lights green. If the LED does
 not light green make sure that the supply voltage is in the acceptable
 range.

The LINK LED lights green when multiple GPIB extenders are properly
 connected and turned on.

Note

LED Indicators

#### Verifying the Connection

Each GPIB extender has a self test that determines whether the GPIB extender receivers,
 transmitters, and packet transmission and reception circuitry are working
 properly.

1. Power off the GPIB extender.
2. Disconnect the fiber-optic cable from the GPIB extender.
3. Power on the GPIB extender. The POWER LED lights green,
 indicating that power is supplied to the extender. The
 LINK LED remains off, and the
 STATUS LED lights red.
4. Connect the connector marked T (transmit) on one end of the
 fiber-optic cable to the connector marked TRANSMIT on
 the side of the GPIB extender.
5. Connect the connector marked R (receive) on the opposite end of the
 fiber-optic cable to the connector marked RECEIVE on
 the side of the GPIB extender.

Figure 8.

[IMAGE alt='1378' src='GUID-1F896AC1-43BE-4998-87E7-B24F4525A15E-a5.svg']

The LINK LED lights green, indicating that a properly working cable is
 connected. The STATUS LED remains off during the
 self-test.

If the LINK LED is off and the STATUS LED is
 either solid or flashing red, there may be an issue with the fiber-optic
 transmission cable. Complete the following steps to troubleshoot:

1. Verify that the fiber-optic cable is properly connected to the GPIB extender as described in
 steps 4 and 5 above. If the problem persists, continue to the next step.
2. Repeat steps 4 and 5 using the unconnected ends of the fiber-optic cable. If switching the
 fiber-optic cable connectors solves the problem, you need to replace your
 fiber-optic cable. Refer to the Fiber-Optic Cable product page at
 ni.com for cable
 information. If switching the fiber-optic cable connectors does not solve
 the problem, continue to the next step.
3. Repeat steps 4 and 5 using a different fiber-optic cable. If the problem persists, you might
 need to replace your GPIB extender. For more information, contact NI for
 support.

Note

LED Indicators

<!--NI_TOPIC bundle=gpib-140b-feature path=hardware-symbol-definitions.html language=enus -->
## TOPIC 00004: Hardware Symbol Definitions

- bundle_id: `gpib-140b-feature`
- source_path: `hardware-symbol-definitions.html`
- source_url: https://docs-be.ni.com/bundle/gpib-140b-feature/raw/resource/enus/hardware-symbol-definitions.html
- document_id: `gpib-140b-feature`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following symbols are marked on the GPIB-140B. Caution Take precautions to avoid injury. Refer to the GPIB-140B Safety, Environmental, and Regulatory Information for safety guidelines. At the end of the product life cycle, all NI products must be disposed of according to local laws and regulatio

Hardware Symbol Definitions

The following symbols are marked on the GPIB-140B.

|  | Caution Take precautions to avoid injury. Refer to the GPIB-140B Safety, Environmental, and Regulatory Information for safety guidelines. |
| --- | --- |
|  | At the end of the product life cycle, all NI products must be disposed of according to local laws and regulations. For more information about how to recycle NI products in your region, visit ni.com/environment/weee. |
|  | NI符合中国电子信息产品中限制使用某些有害物质指令(RoHS)。关于NI中国RoHS合规性信息，请登录 ni.com/environment/rohs_china。(For information about China RoHS compliance, go to ni.com/environment/rohs_china.) |

Parent topic:

Basic Information

<!--NI_TOPIC bundle=gpib-140b-feature path=hw-overview.html language=enus -->
## TOPIC 00005: Hardware Overview

- bundle_id: `gpib-140b-feature`
- source_path: `hw-overview.html`
- source_url: https://docs-be.ni.com/bundle/gpib-140b-feature/raw/resource/enus/hw-overview.html
- document_id: `gpib-140b-feature`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes the GPIB-140Bfiber optic GPIB extender. GPIB-140B Description The GPIB-140B bus extender can communicate with either a GPIB-140B or a GPIB-140A bus extender. The GPIB-140B cannot communicate with a GPIB-140, a GPIB-140/2 or a GPIB-140A/2 bus extender since it uses a different

Hardware Overview

This section describes the GPIB-140Bfiber optic GPIB
 extender.

Parent topic:

GPIB-140B User Manual

#### GPIB-140B Description

Note

GPIB-140B

GPIB-140B

The GPIB-140B is a high-speed bus extender that you can use in pairs with multi-mode fiber-optic
 cable to connect two separate GPIB systems in a functionally transparent manner.

The two bus systems are physically separate, as shown in the following figure.

Figure 1.

[IMAGE alt='1378' src='GUID-FA6BCC86-7A6C-422B-B277-51FB5AB5E16B-a5.svg']

The devices logically appear to be located on the same bus, as shown in the following
 figure.

Figure 2.

[IMAGE alt='1378' src='GUID-97BBF13A-73BC-4216-B7B6-E4A2A772D792-a5.svg']

The bus extender complies with the specifications of the ANSI/IEEE Standard 488.1-1987 and the
 ANSI/IEEE Standard 488.2-1992, including the Find Listeners protocol. With the GPIB
 extenders, you can overcome the following two configuration restrictions imposed by IEEE
 488:

- A cable length limit of 20 m total per contiguous bus or 2 m per each device on the
 bus, whichever is smaller.
- An electrical loading limit of 15 devices per contiguous bus.

Each GPIB-140B system extends the GPIB to a maximum distance of 1 km, and extends the loading limit
 to 28 devices (including the GPIB extenders), without sacrificing speed or performance.
 You can connect these point-to-point extension systems in series for longer distances or
 in star patterns for additional loading.

Using the HS488 protocol, the maximum data transfer rate over the extension is greater
 than 2.8 MBytes/s. The GPIB extenders use a buffered transfer technique with a serial
 extension bus, which maximizes performance and minimizes the cabling cost. Furthermore,
 the extender does not affect the transfer rate between devices on the same side of the
 extension. The GPIB extender can also check for errors to make sure that the data
 transmitted successfully over the fiber-optic link.

Because the GPIB-140B is a functionally transparent extender, the GPIB communications and control programs
 that work with an unextended system also work with an extended system. However, the
 Parallel Poll Response Modes section describes one exception to this transparency in
 conducting parallel polls.

#### GPIB-140B Dimensions

GPIB-140B

ni.com/dimensions

Figure 3.

GPIB-140B

[IMAGE alt='1378' src='GUID-6769CD3A-BBC0-45D4-96E4-47424EADB9AD-a5.svg']

Figure 4.

GPIB-140B

[IMAGE alt='1378' src='GUID-039AA80C-E638-4ADF-880F-076C9084A621-a5.svg']

#### Grounding the GPIB-140B

You must connect the GPIB-140B grounding terminal to the grounding electrode system of the facility.

Note

ni.com/r/emcground

##### What to Use

- Standard ring lug
- Wire, 1.3 mm 2 (16 AWG) or larger
- Screwdriver, Phillips #2

##### What to Do

Complete the following steps to ground the GPIB-140B.

Figure 5.

[IMAGE alt='1378' src='GUID-AEA5C6F4-3214-43EE-919E-2D824FB53BFA-a5.svg']

1. Attach the ring lug to the wire.
2. Remove the grounding screw from the grounding terminal on the side panel of the
 product.
3. Fasten the ring lug to the grounding terminal.
4. Tighten the grounding screw to 1.3 N · m (11.5 in-lb) of torque.
5. Attach the other end of the wire to the chassis safety ground using a method that is appropriate for your application.

#### LED Indicators

| LED | Color | Behavior | Description |
| --- | --- | --- | --- |
| POWER | Green | Solid | GPIB-140B is powered on. |
| Red | Solid | GPIB-140B is powered on, but the input supply voltage is either out of the operating range or the overcurrent protection is active. |  |
| — | Off | The supply voltage is connected in reverse polarity (when the device is powered on), or the device is powered off. |  |
| LINK | Green | Solid | Both GPIB extenders are powered on and the fiber-optic transmission cable is properly connected between them. The GPIB-140B bus extenders are ready to use. |
| — | Off | The fiber-optic cable is defective or disconnected, or the remote GPIB-140B is turned off. |  |
| STATUS | Green | Flashing, 10 Hz | Activity is present on the GPIB bus. |
| Red | Solid | The fiber-optic cable is either defective or disconnected, or the GPIB-140B is turned off. |  |
| Red | Flashing, 10 Hz | The GPIB-140B is receiving corrupted data, and starts re-transmission. |  |
| The red LED turns off after 50 ms and flashes green when the extender receives retransmitted data bytes without error. |  |  |  |
| — | Off | There is no activity on the GPIB bus. |  |

#### DIP Switches

The 3-bit DIP switch sets the operation mode of the GPIB extender. The default switch
 setting is for unbuffered transfer mode, latched parallel poll response (PPR), and
 HS488 disabled mode, as shown here.

Figure 6.

[IMAGE alt='1378' src='GUID-D2FC33D3-0B6D-475C-A158-BA82A51CD49D-a5.svg']

Verify that the DIP switches on your GPIB extender are in these default positions. If you need
 to change these settings, refer to [Hardware Configuration](Chunk2021228355.html#GUID-239C490A-4759-4F96-BFCE-969FAE843455) for
 instructions about how to set the operation mode for your application.

<!--NI_TOPIC bundle=gpib-140b-feature path=introduction.html language=enus -->
## TOPIC 00006: GPIB-140B User Manual

- bundle_id: `gpib-140b-feature`
- source_path: `introduction.html`
- source_url: https://docs-be.ni.com/bundle/gpib-140b-feature/raw/resource/enus/introduction.html
- document_id: `gpib-140b-feature`
- page_type: `leaf`
- content_type: `concept`
- source_description: This document provides installation, configuration, and reference information for the GPIB-140Bfiber optic GPIB extender.

GPIB-140B User Manual

This document provides installation, configuration, and reference information for the
 GPIB-140Bfiber optic GPIB
 extender.

© 2021 National Instruments Corporation. All rights reserved. Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.

<!--NI_TOPIC bundle=gpib-140b-feature path=product-cert.html language=enus -->
## TOPIC 00007: Product Certifications and Declarations

- bundle_id: `gpib-140b-feature`
- source_path: `product-cert.html`
- source_url: https://docs-be.ni.com/bundle/gpib-140b-feature/raw/resource/enus/product-cert.html
- document_id: `gpib-140b-feature`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the product Declaration of Conformity (DoC) for additional regulatory compliance information. To obtain product certifications and the DoC for NI products, visit ni.com/product-certifications, search by model number, and click the appropriate link.

Product Certifications and Declarations

Refer to the product Declaration of Conformity (DoC) for additional regulatory compliance information. To obtain product certifications and the DoC for NI products, visit [ni.com/product-certifications](https://HTTP://WWW.NI.COM/EN-US/SUPPORT/DOCUMENTATION/PRODUCT-CERTIFICATIONS.HTML), search by model number, and click the appropriate link.

Parent topic:

GPIB-140B User Manual

<!--NI_TOPIC bundle=gpib-140b-feature path=support.html language=enus -->
## TOPIC 00008: NI Services

- bundle_id: `gpib-140b-feature`
- source_path: `support.html`
- source_url: https://docs-be.ni.com/bundle/gpib-140b-feature/raw/resource/enus/support.html
- document_id: `gpib-140b-feature`
- page_type: `leaf`
- content_type: `reference`
- source_description: Visit ni.com/support to find support resources including documentation, downloads, and troubleshooting and application development self-help such as tutorials and examples. Visit ni.com/services to learn about NI service offerings such as calibration options, repair, and replacement. Visit ni.com/re

NI Services

Visit [ni.com/support](https://HTTP://WWW.NI.COM/SUPPORT) to find support resources including documentation,
 downloads, and troubleshooting and application development self-help such as
 tutorials and examples.

Visit [ni.com/services](https://HTTP://WWW.NI.COM/SERVICES) to learn about NI service offerings such as calibration
 options, repair, and replacement.

Visit [ni.com/register](https://HTTP://WWW.NI.COM/REGISTER) to register your NI product. Product registration
 facilitates technical support and ensures that you receive important information
 updates from NI.

NI corporate headquarters is located at 11500 N Mopac Expwy, Austin, TX, 78759-3504,
 USA.

Parent topic:

GPIB-140B User Manual

<!--NI_TOPIC bundle=gpib-140b-feature path=theory-of-operation.html language=enus -->
## TOPIC 00009: Theory of Operation

- bundle_id: `gpib-140b-feature`
- source_path: `theory-of-operation.html`
- source_url: https://docs-be.ni.com/bundle/gpib-140b-feature/raw/resource/enus/theory-of-operation.html
- document_id: `gpib-140b-feature`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes how the GPIB extender circuitry operates. This section assumes that you are familiar with GPIB. If you are a first-time user or if you would like to review the basics about GPIB, refer to GPIB Basics. The following figure shows the five layers of a GPIB extender. To form a com

Theory of Operation

This section describes how the GPIB extender circuitry operates.

This section assumes that you are familiar with GPIB. If you are a first-time user or if
 you would like to review the basics about GPIB, refer to [GPIB Basics](#GUID-45A43A0C-E8A4-4276-9488-20DD65D26EE3).

The following figure shows the five layers of a GPIB extender. To form a complete link,
 you can connect each layer to the corresponding layer of another extender at the remote
 side.

Figure 12.

[IMAGE alt='1378' src='GUID-42B00BB9-0A72-4037-86D9-78B77531570B-a5.svg']

#### Message Interpreter Layer

The Message
 Interpreter Layer handles the handshake between the GPIB extender and other devices
 on the GPIB. At the same time, the layer monitors the activities that occur on the
 GPIB, translates them into equivalent local and remote GPIB messages, and sends
 these messages to the Packet Translation Layer.

#### Packet Translation Layer

The Packet
 Translation Layer converts the messages that it receives to packets and sends them
 to the Link Management Layer. It can also receive packets from the Link Management
 Layer and convert them back to local or remote GPIB messages.

#### Link
 Management Layer

The Link Management Layer receives packets from the
 Packet Translation Layer. It sends the packets to the Parallel-to-Serial Conversion
 Layer and it stores them in a local buffer. If a transmission error occurs, the Link
 Management Layer can re-send the packets from this local buffer. The Link Management
 Layer also receives packets from the Parallel-to-Serial Conversion Layer and checks
 the packets for transmission errors. If the Link Management Layer does not detect an
 error, it sends the packets to the Packet Translation Layer. However, if it detects
 a transmission error, then it re-transmits the packets.

#### Parallel-to-Serial Conversion Layer

The
 Parallel-to-Serial Conversion Layer accepts packets from the Link Management Layer,
 converts them into serial data, and sends the data to the Physical Layer. It also
 extracts serial bits from the Physical Layer, reconstructs them back into packets,
 and sends them to the Link Management Layer.

#### Physical Layer

The Physical Layer
 transmits and receives serial data over the fiber-optic link.

Parent topic:

GPIB-140B User Manual

#### GPIB Basics

This section describes the basic concepts of GPIB, including its physical and electrical
 characteristics, and configuration requirements.

The ANSI/IEEE Standard 488.1-1987, also known as General Purpose Interface Bus (GPIB),
 describes a standard interface for communication between instruments and controllers
 from various vendors. It contains information about electrical, mechanical, and
 functional specifications. GPIB is a digital, 8-bit parallel communications interface
 with data transfer rates of 1 Mbyte/s and higher, using a three-wire handshake. The bus
 supports one System Controller, usually a computer, and up to 14 additional instruments.
 The ANSI/IEEE Standard 488.2-1992 extends IEEE 488.1 by defining a bus communication
 protocol, a common set of data codes and formats, and a generic set of common device
 commands.

##### Types of Messages

Interconnected GPIB
 devices communicate by passing messages through the interface system, including
 device-dependent messages and interface messages.

- Device-dependent messages, also called data or data
 messages , contain device-specific information, such as programming
 instructions, measurement results, machine status, and data files.
- Interface messages, also called commands or command
 messages , manage the bus itself. Interface messages initialize the
 bus, address and unaddress devices, and set device modes for remote or local
 programming. The term *command* as used here does not refer to
 device instructions, which are also called commands. Those device-specific
 instructions are data messages.

##### Talkers, Listeners, and Controllers

GPIB
 devices can be Talkers, Listeners, or Controllers. A Talker sends out data messages.
 Listeners receive data messages. The Controller, usually a computer, manages the
 flow of information on the bus. It defines the communication links and sends GPIB
 commands to devices.

Some devices are capable of playing more than one role. A
 digital voltmeter, for example, can be a Talker and a Listener. If your system has a
 NI GPIB interface and software installed, it can function as a Talker, Listener, and
 Controller.

The GPIB is like a typical computer bus, except that the typical
 computer has circuit cards interconnected via a backplane bus, whereas the GPIB has
 standalone devices interconnected via a cable bus.

The role of the GPIB
 Controller is similar to the role of the CPU of a computer, but a better analogy is
 to the switching center of a city telephone system. The switching center
 (Controller) monitors the communications network (GPIB). When the center
 (Controller) notices that a party (device) wants to make a call (send a data
 message), it connects the caller (Talker) to the receiver (Listener).

The
 Controller addresses a Talker and a Listener before the Talker can send its message
 to the Listener. After the message is transmitted, the Controller may unaddress both
 devices.

Some bus configurations do not require a Controller. For example, one
 device may always be a Talker (called a Talk-only device) and there may be one or
 more Listen-only devices.

A Controller is necessary when the active or
 addressed Talker or Listener must be changed. The Controller function is usually
 handled by a computer.

With the GPIB interface board and its software your
 personal computer plays all three roles.

- Controller—to manage the GPIB
- Talker—to send data
- Listener—to receive data

##### Controller-In-Charge and System
 Controller

You can have multiple Controllers on the GPIB, but only one
 Controller at a time can be the active Controller, or Controller-In-Charge (CIC).
 The CIC can be either active or inactive (standby). Control can pass from the
 current CIC to an idle Controller, but only the System Controller, usually a GPIB
 interface, can make itself the CIC.

##### GPIB Signals and Lines

Devices on the bus
 communicate by sending messages. Signals and lines transfer these messages across
 the GPIB interface, which consists of 16 signal lines and 8 ground return (shield
 drain) lines. The 16 signal lines are discussed in the following
 sections.

##### Data Lines

Eight data lines, DIO1 through DIO8, carry both data
 and command messages.

##### Handshake Lines

Three hardware handshake lines asynchronously
 control the transfer of message bytes between devices. This process is a three-wire
 interlocked handshake, and it guarantees that devices send and receive message bytes
 on the data lines without transmission error. The following table summarizes the
 GPIB handshake lines.

| Line | Description |
| --- | --- |
| NRFD (not ready for data) | Listening device is ready/not ready to receive a message byte. Also used by the Talker to signal high-speed GPIB transfers. |
| NDAC (not data accepted) | Listening device has/has not accepted a message byte. |
| DAV (data valid) | Talking device indicates signals on data lines are stable (valid) data. |

##### Interface Management
 Lines

Five hardware lines manage the flow of information across the bus.
 The following table summarizes the GPIB interface management lines.

| Line | Description |
| --- | --- |
| ATN (attention) | Controller drives ATN true when it sends commands and false when it sends data messages. |
| IFC (interface clear) | System Controller drives the IFC line to initialize the bus and make itself CIC. |
| REN (remote enable) | System Controller drives the REN line to place devices in remote or local program mode. |
| SRQ (service request) | Any device can drive the SRQ line to asynchronously request service from the Controller. |
| EOI (end or identify) | Talker uses the EOI line to mark the end of a data message. Controller uses the EOI line when it conducts a parallel poll. |

##### Physical and Electrical
 Characteristics

Devices are usually connected with a cable assembly
 consisting of a shielded 24-conductor cable with both a plug and receptacle
 connector at each end, as shown in the following figure.

Figure 13.

[IMAGE alt='1378' src='GUID-213F6734-1851-4952-B1F5-08F7C650BD28-a5.svg']

With this design, you can link devices in a linear configuration, a star
 configuration, or a combination of the two configurations. The following figure
 shows both linear and star configurations.

Figure 14.

[IMAGE alt='1378' src='GUID-D77B7808-00E8-4573-B60A-248C8FFBCA38-a5.svg']

The standard connector is the Amphenol or Cinch Series 57
 *Microribbon* or *Amp Champ* type. For special
 interconnection applications, you use an adapter cable using a non-standard cable
 and/or connector.

The GPIB uses negative logic with standard TTL
 (transistor-transistor logic) level. For example, when DAV is true, it is a TTL low
 level (≤ 0.8 V), and when DAV is false, it is a TTL high level (≥ 2.0
 V).

##### Configuration Requirements

To achieve the high data transfer rate
 that the GPIB was designed for, you must limit the number of devices on the bus and
 the physical distance between devices. The following restrictions are typical:

- A maximum separation of 4 m between any two devices and an average separation of
 2 m over the entire bus.
- A maximum total cable length of 20 m.
- A maximum of 15 devices connected to each bus, with at least two-thirds powered
 on.

For high-speed operation, the following restrictions apply:

- All devices in the system must be powered on.
- Cable lengths must be as short as possible with up to a maximum of 15 m of cable
 for each system.
- There must be at least one equivalent device load per meter of cable.

If you want to exceed these limitations, you can use a bus expander to increase
 the number of device loads. You can order bus expanders from NI.

#### Introduction to HS488

This section describes HS488 and the sequence of events in high-speed data
 transfers.

NI has designed a high-speed data transfer protocol for IEEE 488 called HS488. This
 protocol increases performance for GPIB reads and writes up to 8 MBytes/s, depending on
 your system.

If HS488 is enabled, the TNT4882C hardware implements high-speed transfers automatically
 when communicating with HS488 instruments. If you attempt to enable HS488 on a GPIB
 interface that does not have the TNT4882C hardware, the ECAP error code is returned.

##### Objectives

The following sections describe the objectives of HS488.

###### Faster Transfer Rates

HS488 enables transfer rates that
 are substantially faster than the IEEE 488 standard. In small
 systems, the raw transfer rate can be up to 8 MBytes/s. The faster
 raw transfer rates improve system throughput in systems where
 devices send long blocks of data. The physical limitations of the
 cabling system, however, limit the transfer rate.

###### Compatibility with IEEE 488 Devices

HS488
 is a superset of the IEEE 488 standard; thus, you can mix IEEE 488.1, IEEE 488.2,
 and HS488 devices in the same system.

When connected to an HS488 device, the
 Controller does not need to be capable of HS488 non-interlocked transfers. While ATN
 is asserted, the Controller sources multiline messages to HS488 devices just as it
 sources multiline messages to any IEEE 488 devices.

###### Automatic HS488 Detection

Addressed HS488
 devices can detect whether other addressed devices are capable of HS488 transfers
 without the interaction of the Controller.

###### Compatibility with the IEEE 488.2
 Standard

The HS488 protocol requires no changes to the IEEE 488.2
 standard. Also, HS488 devices do not need to be compliant with IEEE
 488.2.

###### Same Cabling Restrictions as IEEE
 488.1

Systems that meet the IEEE 488.1 requirements for high-speed
 operation also meet the HS488 requirements. HS488 cabling requirements are also the
 same as the requirements in the IEEE 488.1 standard.

However, using HS488 does
 not reduce software overhead. Also, system throughput increases depend on data block
 size.

##### IEEE 488.1 Requirements for High-Speed
 Operation (T1 Delay ≥ 350 ns)

The IEEE 488.1 standard requires that devices used in high-speed operation must use
 three-state, 48 mA drivers on most signals. Each device must add no more than 50 pF
 capacitance on each signal, and all devices must be powered on.

The total cable length in a system must be no more than 15 m, or 1 m times the number of
 devices in the system.

##### HS488 System Requirements

An HS488 system must meet the IEEE 488.1 requirements and it must implement the following
 three new interface functions:

- Talking devices must use the Source Handshake Extended (SHE) interface
 function, which is an extension of the IEEE 488.1 SH function.
- Listening devices must use the Acceptor Handshake Extended (AHE) 
 interface function, which is an extension of the IEEE 488.1 AH function. Accepting
 devices must have a buffer of at least 3 bytes to store received data.
- HS488 devices must implement the Configuration (CF) interface function.
 At system power on, the Controller uses previously undefined multiline messages to
 configure HS488 devices. The CF function enables devices to interpret these
 multiline messages.

##### Sequence of Events in Data Transfers

The following figure shows a typical IEEE 488.1 data transfer.

Figure 15.

[IMAGE alt='1378' src='GUID-88EFBDDA-0A37-408E-9F6A-B1D2A4220123-a5.svg']

The following figure shows an HS488 data transfer. The HS488 protocol modifies the IEEE
 488.1 SH and AH functions. At the beginning of each data transfer, the HS488 SHE and AHE
 functions determine whether all active Talkers and Listeners are capable of HS488
 transfers. If the addressed devices are HS488-capable, they use the HS488 noninterlocked
 handshake protocol for that data transfer. If any addressed device is not HS488-capable,
 the transfer continues using the standard three-wire handshake.

Figure 16.

[IMAGE alt='1378' src='GUID-AAFEF1F1-3729-4CC1-BB32-F4FE6BE01F82-a5.svg']

###### Case
 1: Talker and Listener are HS488 Capable

The following figure and
 procedure describe a typical sequence of events in an HS488 data transfer in which
 both the Talker and Listener are HS488-capable.

Figure 17.

[IMAGE alt='1378' src='GUID-3A732266-2F1F-445B-97EE-0C2750F1AFCD-a5.svg']

1. The Controller addresses devices and becomes Standby Controller by unasserting
 ATN.
2. The Listener asserts NDAC and NRFD.
3. The Listener unasserts NRFD as it becomes ready to accept a byte.
4. After allowing time for the Listener to detect NRFD unasserted, the Talker
 indicates that it is HS488-capable by sending the HSC message. To send the HSC
 message true, the Talker asserts the NRFD signal.
5. After allowing time for the Listener to respond to the HSC message, the Talker
 sends the HSC message false. To send the HSC message false, the Talker unasserts
 the NRFD signal.
6. When the Talker has a byte ready to send, it drives the data on the DIO signal
 lines, allows some settling time, and asserts DAV.
7. The Listener unasserts NDAC. HS488-capable Listeners do not assert NRFD as IEEE
 488.1 devices would, so the Talker determines that the addressed Listener is
 HS488-capable.
8. The Talker unasserts DAV and drives the next data byte on the GPIB.
9. After allowing some settling time, the Talker asserts DAV.
10. The Listener latches the byte in response to the assertion (falling) edge of
 DAV.
11. After allowing some hold time, the Talker unasserts DAV and drives the next
 data byte on the DIO signal lines.

Steps 9-11 are repeated for each data byte.

###### Case
 2: Talker Is HS488-Capable, But Listener Is Not HS488-Capable

The
 following figure and procedure describe a typical sequence of events in an HS488
 data transfer in which the Talker is HS488-capable, but the Listener is not.

Figure 18.

[IMAGE alt='1378' src='GUID-08BF4480-B15B-44D5-849F-44993DA7DB1F-a5.svg']

Steps 1–6 in the sequence are identical to steps 1–6 in the previous procedure
 [Case 1: Talker and Listener are HS488 Capable](#GUID-6199ECF7-A9A1-4541-A0CD-D8F08A912ECB__SECTION_NPW_VCQ_LNB). The Listener ignores the HSC message from the
 Talker.

Then, the IEEE 488.1 Listener enters ACDS and asserts NRFD. As a
 result, the Talker determines that the addressed Listener is not HS488-capable. The
 Talker sources bytes using the IEEE 488.1 protocol.

###### Case 3: Talker Is Not HS488-Capable,
 But Listener Is HS488-Capable

The Talker does *not* send an HSC
 message to the Listener, but sources bytes using the IEEE 488.1 protocol.

The
 addressed Listener (HS488 or IEEE 488.1) accepts bytes using the IEEE 488.1 standard
 three-wire handshake, as shown in the following figure.

Figure 19.

[IMAGE alt='1378' src='GUID-374C633F-E7AD-424A-80B9-5F56E71E283C-a5.svg']

###### System Configuration

The HS488 AHE and SHE interface functions
 depend on several time delays. Some of these delays are a function of the total
 system cable length.

The Controller must communicate this system configuration
 data to HS488 devices after the system powers on. The Controller configures HS488
 devices by sourcing the following two multiline messages while ATN is true:

- Configuration Enable (CFE)—The Controller sends the CFE message by driving a bit
 pattern (1E hex) that the IEEE 488.1 standard does not define on the DIO signal
 lines. The CFE message enables HS488 devices to interpret the SCG message that
 follows.
- Secondary Command Group (SCG)—This message contains the configuration data. The
 Secondary Command has the bit pattern 6n hex, where n is the meters of cable in
 the system. The SCG includes CFG1-CFG15 in the Multiline Interface Messages section.

#### Multiline Interface Messages

This section lists the multiline interface messages and describes the mnemonics and
 messages that correspond to the interface functions.

The multiline interface messages are commands defined by the IEEE 488 standard. The
 messages are sent and received with ATN asserted. The interface functions include
 initializing the bus, addressing and unaddressing devices, and setting device modes
 for local or remote programming. For more information about these messages, refer to
 the ANSI/IEEE Standard 488.1-1987, IEEE Standard Digital Interface for Programmable
 Instrumentation.

| Hex | Dec | ASCII | Message |  | Hex | Dec | ASCII | Message |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00 | 0 | NUL | — |  | 20 | 32 | SP | MLA0 |
| 01 | 1 | SOH | GTL |  | 21 | 33 | ! | MLA1 |
| 02 | 2 | STX | — |  | 22 | 34 | " | MLA2 |
| 03 | 3 | ETX | — |  | 23 | 35 | # | MLA3 |
| 04 | 4 | EOT | SDC |  | 24 | 36 | $ | MLA4 |
| 05 | 5 | ENQ | PPC |  | 25 | 37 | % | MLA5 |
| 06 | 6 | ACK | — |  | 26 | 38 | & | MLA6 |
| 07 | 7 | BEL | — |  | 27 | 39 | ' | MLA7 |
| 08 | 8 | BS | GET |  | 28 | 40 | ( | MLA8 |
| 09 | 9 | HT | TCT |  | 29 | 41 | ) | MLA9 |
| 0A | 10 | LF | — |  | 2A | 42 | * | MLA10 |
| 0B | 11 | VT | — |  | 2B | 43 | + | MLA11 |
| 0C | 12 | FF | — |  | 2C | 44 | , | MLA12 |
| 0D | 13 | CR | — |  | 2D | 45 | - | MLA13 |
| 0E | 14 | SO | — |  | 2E | 46 | . | MLA14 |
| 0F | 15 | SI | — |  | 2F | 47 | / | MLA15 |
| 10 | 16 | DLE | — |  | 30 | 48 | 0 | MLA16 |
| 11 | 17 | DC1 | LLO |  | 31 | 49 | 1 | MLA17 |
| 12 | 18 | DC2 | — |  | 32 | 50 | 2 | MLA18 |
| 13 | 19 | DC3 | — |  | 33 | 51 | 3 | MLA19 |
| 14 | 20 | DC4 | DCL |  | 34 | 52 | 4 | MLA20 |
| 15 | 21 | NAK | PPU |  | 35 | 53 | 5 | MLA21 |
| 16 | 22 | SYN | — |  | 36 | 54 | 6 | MLA22 |
| 17 | 23 | ETB | — |  | 37 | 55 | 7 | MLA23 |
| 18 | 24 | CAN | SPE |  | 38 | 56 | 8 | MLA24 |
| 19 | 25 | EM | SPD |  | 39 | 57 | 9 | MLA25 |
| 1A | 26 | SUB | — |  | 3A | 58 | : | MLA26 |
| 1B | 27 | ESC | — |  | 3B | 59 | ; | MLA27 |
| 1C | 28 | FS | — |  | 3C | 60 | < | MLA28 |
| 1D | 29 | GS | — |  | 3D | 61 | = | MLA29 |
| 1E | 30 | RS | — |  | 3E | 62 | > | MLA30 |
| 1F | 31 | US | CFE |  | 3F | 63 | ? | UNL |
| 40 | 64 | @ | MTA0 |  | 60 | 96 | ` | MSA0, PPE |
| 41 | 65 | A | MTA1 |  | 61 | 97 | a | MSA1, PPE, CFG1 |
| 42 | 66 | B | MTA2 |  | 62 | 98 | b | MSA2, PPE, CFG2 |
| 43 | 67 | C | MTA3 |  | 63 | 99 | c | MSA3, PPE, CFG3 |
| 44 | 68 | D | MTA4 |  | 64 | 100 | d | MSA4, PPE, CFG4 |
| 45 | 69 | E | MTA5 |  | 65 | 101 | e | MSA5, PPE, CFG5 |
| 46 | 70 | F | MTA6 |  | 66 | 102 | f | MSA6, PPE, CFG6 |
| 47 | 71 | G | MTA7 |  | 67 | 103 | g | MSA7, PPE, CFG7 |
| 48 | 72 | H | MTA8 |  | 68 | 104 | h | MSA8, PPE, CFG8 |
| 49 | 73 | I | MTA9 |  | 69 | 105 | i | MSA9, PPE, CFG9 |
| 4A | 74 | J | MTA10 |  | 6A | 106 | j | MSA10, PPE, CFG10 |
| 4B | 75 | K | MTA11 |  | 6B | 107 | k | MSA11, PPE, CFG11 |
| 4C | 76 | L | MTA12 |  | 6C | 108 | l | MSA12, PPE, CFG12 |
| 4D | 77 | M | MTA13 |  | 6D | 109 | m | MSA13, PPE, CFG13 |
| 4E | 78 | N | MTA14 |  | 6E | 110 | n | MSA14, PPE, CFG14 |
| 4F | 79 | O | MTA15 |  | 6F | 111 | o | MSA15, PPE, CFG15 |
| 50 | 80 | P | MTA16 |  | 70 | 112 | p | MSA16, PPD |
| 51 | 81 | Q | MTA17 |  | 71 | 113 | q | MSA17, PPD |
| 52 | 82 | R | MTA18 |  | 72 | 114 | r | MSA18, PPD |
| 53 | 83 | S | MTA19 |  | 73 | 115 | s | MSA19, PPD |
| 54 | 84 | T | MTA20 |  | 74 | 116 | t | MSA20, PPD |
| 55 | 85 | U | MTA21 |  | 75 | 117 | u | MSA21, PPD |
| 56 | 86 | V | MTA22 |  | 76 | 118 | v | MSA22, PPD |
| 57 | 87 | W | MTA23 |  | 77 | 119 | w | MSA23, PPD |
| 58 | 88 | X | MTA24 |  | 78 | 120 | x | MSA24, PPD |
| 59 | 89 | Y | MTA25 |  | 79 | 121 | y | MSA25, PPD |
| 5A | 90 | Z | MTA26 |  | 7A | 122 | z | MSA26, PPD |
| 5B | 91 | [ | MTA27 |  | 7B | 123 | { | MSA27, PPD |
| 5C | 92 | \\ | MTA28 |  | 7C | 124 | \| | MSA28, PPD |
| 5D | 93 | ] | MTA29 |  | 7D | 125 | } | MSA29, PPD |
| 5E | 94 | ^ | MTA30 |  | 7E | 126 | ~ | MSA30, PPD |
| 5F | 95 | _ | UNT |  | 7F | 127 | DEL | — |

| Multiline Interface Message Definitions |  |  |  |
| --- | --- | --- | --- |
| CFE * | Configuration Enable | PPD | Parallel Poll Disable |
| CFG * | Configure | PPE | Parallel Poll Enable |
| DCL | Device Clear | PPU | Parallel Poll Unconfigure |
| GET | Group Execute Trigger | SDC | Selected Device Clear |
| GTL | Go To Local | SPD | Serial Poll Disable |
| LLO | Local Lockout | SPE | Serial Poll Enable |
| MLA | My Listen Address | TCT | Take Control |
| MSA | My Secondary Address | UNL | Unlisten |
| MTA | My Talk Address | UNT | Untalk |
| PPC | Parallel Poll Configure |  |  |
| * This multiline interface message is a proposed extension to the IEEE 488 specification to support the HS488 protocol. |  |  |  |

<!--NI_TOPIC bundle=gpib-140b-feature path=unpacking.html language=enus -->
## TOPIC 00010: Unpacking

- bundle_id: `gpib-140b-feature`
- source_path: `unpacking.html`
- source_url: https://docs-be.ni.com/bundle/gpib-140b-feature/raw/resource/enus/unpacking.html
- document_id: `gpib-140b-feature`
- page_type: `leaf`
- content_type: `concept`
- source_description: The GPIB-140B ships in an antistatic package to prevent electrostatic discharge (ESD). ESD can damage several components on the device. To avoid ESD damage in handling the device, take the following precautions: Ground yourself with a grounding strap or by touching a grounded object. Touch the antis

Unpacking

The GPIB-140B ships in an antistatic package to prevent electrostatic discharge (ESD). ESD can damage
 several components on the device.

To avoid ESD damage in handling the device, take the following precautions:

- Ground yourself with a grounding strap or by touching a grounded object.
- Touch the antistatic package to a metal part of your computer chassis before removing the device from the package.

Remove the device from the package and inspect it for loose components or any other signs of damage. Notify NI if the device appears damaged in any way. Do not install a damaged device.

Store the device in the antistatic package when the device is not in use.

Parent topic:

Basic Information
