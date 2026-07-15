# NI DOCUMENT BUNDLE: gpib-enet-1000-getting-started

<!--NI_BUNDLE_CHUNK bundle=gpib-enet-1000-getting-started start=1 end=8 -->
<!--NI_TOPIC bundle=gpib-enet-1000-getting-started path=cfg-reset.html language=enus -->
## TOPIC 00001: CFG RESET Switch

- bundle_id: `gpib-enet-1000-getting-started`
- source_path: `cfg-reset.html`
- source_url: https://docs-be.ni.com/bundle/gpib-enet-1000-getting-started/raw/resource/enus/cfg-reset.html
- document_id: `gpib-enet-1000-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Configuration Reset (CFG RESET) switch is a recessed switch located beside the power connector on the rear panel. You can use this switch at power on to reset the unit to its factory settings. By pressing and holding the CFG RESET switch while you power on the GPIB-ENET/1000, all settings revert

CFG RESET Switch

The Configuration Reset (CFG RESET) switch is a recessed switch located beside the power connector on the rear panel.

You can use this switch at power on to reset the unit to its factory settings. By pressing and holding the CFG RESET switch while you power on the GPIB-ENET/1000, all settings revert to the factory settings as follows:

- DHCP with Auto IP fallback.
- Default hostname as printed on the baseplate label.
- Administrator password is pass. You must press and hold the switch until the READY
 LED blinks yellow. If you release the switch prior to the READY LED blinks yellow, no
 change occurs to the network configuration, and the GPIB-ENET/1000 continues to boot
 normally. Once the READY LED blinks yellow, release the CFG RESET switch. The
 GPIB-ENET/1000 resets to its default network characteristics and resumes the boot
 process.

<!--NI_TOPIC bundle=gpib-enet-1000-getting-started path=ethernet-config.html language=enus -->
## TOPIC 00002: Ethernet Configuration

- bundle_id: `gpib-enet-1000-getting-started`
- source_path: `ethernet-config.html`
- source_url: https://docs-be.ni.com/bundle/gpib-enet-1000-getting-started/raw/resource/enus/ethernet-config.html
- document_id: `gpib-enet-1000-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: The GPIB-ENET/1000 uses a Web page for device configuration. If your network uses DHCP, the network configuration is performed automatically at startup, and you should not need the GPIB-ENET/1000 Configuration Web page unless you need to modify the hostname or update the firmware. In addition to man

Ethernet Configuration

The GPIB-ENET/1000 uses a Web page for device configuration. If your network uses DHCP, the network configuration is performed automatically at startup, and you should not need the GPIB-ENET/1000 Configuration Web page unless you need to modify the hostname or update the firmware.

In addition to manually configuring the network parameters, you can use the GPIB-ENET/1000 Configuration Web page for any of the following purposes:

- Enable DHCP/Auto IP addressing
- Verify or change the hostname
- Add or change a comment to help identify the device
- Change the administrator password
- Update firmware Once the GPIB-ENET/1000 has been added to your system, you may need to remove it and add it again if you modify the configuration of a GPIB-ENET/1000.

#### Using the GPIB-ENET/1000 Configuration Web Page

You can access the GPIB-ENET/1000 Configuration Web page in most browsers. Enter the IP address or hostname into the browser’s address bar. Anyone can view the current configuration at any time. However, changes to the configuration or firmware updates proceed only after you enter the proper password.

#### Changing the Network Settings

Complete the following steps to change the network settings:

1. Navigate to the GPIB-ENET/1000 Configuration Web page using a browser. 
 The current hostname is displayed. The hostname associates a name with a numerical IP address. Hostname is a required field.The GPIB-ENET/1000 attempts to use the hostname when registering with DHCP. Many DHCP servers have the ability to register the hostname and the assigned IP address. You then can reliably use the hostname to communicate with your GPIB-ENET/1000 even if the numerical IP address changes.Some DHCP servers do not implement hostname registration. The GPIB-ENET/1000 requires Domain Name Server (DNS) registration when using DHCP. If your DHCP server does not support DNS registration, you must use an Auto IP address or static network parameters.
2. Choose whether you need to use DHCP with Auto IP fallback or a static IP configuration. 
 Leaving the checkbox unchecked enables DHCP with Auto IP fallback. You do not need to enter any network parameters unless you want to change the Ethernet device hostname.
 To use static IP configuration, check the Static IP Configuration checkbox. Enter the [Static IP Parameters](#GUID-89071FF8-5098-4445-8AEE-ECD80C83F49F) you have chosen for the host IP Address, Subnet Mask, Default Gateway, Primary DNS Server, and Secondary DNS Server.
3. You can enter an optional comment to help you identify each device.
4. When your configuration is complete, save the configuration to the GPIB-ENET/1000. You must supply the correct administrator password prior to the settings being saved. 
 The GPIB-ENET/1000 applies the setting changes immediately. There is no need to reboot the interface.

#### Auto IP Addressing

Auto IP addressing, also referred to as link-local addressing, allows a network device to obtain its network identity automatically and advertise its presence without other network servers being required, such as DHCP and DNS. An Auto IP address is in the form of 169.254.x.x. This type of addressing is useful for connecting the GPIB-ENET/1000 directly to a Windows PC.

To determine the Auto IP address the GPIB-ENET/1000 is using, you need to discover the interface using Measurement & Automation Explorer or the GPIB Ethernet Wizard. In addition to an automatically assigned IP address, Auto IP also consists of a “local name” responder. You should be able to access the GPIB-ENET/1000 using the hostname followed by .local, such as nienetba5bf1.local.

#### Static IP Parameters

If DHCP is not available and you do not want to use Auto IP, you must provide the GPIB-ENET/1000 with several important network parameters.

- IP address—The unique, computer-readable address of a device on your network. An IP address typically is represented as four decimal numbers separated by periods (for example, 130.164.54.215). Refer to the Choosing a Static IP Address section.
- Subnet Mask—A bit mask that helps the network device determine whether another device is on the same network or a different network.
- Default Gateway—The IP address of a device that acts as a gateway, which is a connection between two networks. If your network does not have a gateway, set this parameter to 0.0.0.0.
- Primary DNS Server/Secondary DNS Server—The IP address of a network device that stores hostnames and translates them into IP addresses. If your network does not have a DNS server, leave these parameters blank.

#### Choosing a Static IP Address

##### For a Network Administered by a Network Administrator

If you are adding the GPIB-ENET/1000 to an existing Ethernet network, you must choose IP addresses carefully. Contact your network administrator to obtain an appropriate static IP address for your GPIB-ENET/1000. Also have the network administrator assign the proper subnet mask, gateway, and DNS server addresses.

##### For a Network without a Network Administrator

If you are assembling your own small Ethernet network, you can choose your own IP addresses. The format of the IP addresses is determined by the subnet mask. You should use the same subnet mask as the computer you are using with your GPIB-ENET/1000. If your subnet mask is 255.255.255.0, the first three numbers in every IP address on the network must be the same. If your subnet mask is 255.255.0.0, only the first two numbers in the IP addresses on the network must match.

For either subnet mask, numbers between 1 and 254 are valid choices for the last number of the IP address. Numbers between 0 and 255 are valid for the third number of the IP address, but this number must be the same as other devices on your network if your subnet mask is 255.255.255.0.

If you are setting up your own network, you probably do not have a gateway or DNS server. If this is the case, you should set the default gateway to 0.0.0.0 and leave the two DNS server parameters blank.

<!--NI_TOPIC bundle=gpib-enet-1000-getting-started path=firmware.html language=enus -->
## TOPIC 00003: Firmware Update

- bundle_id: `gpib-enet-1000-getting-started`
- source_path: `firmware.html`
- source_url: https://docs-be.ni.com/bundle/gpib-enet-1000-getting-started/raw/resource/enus/firmware.html
- document_id: `gpib-enet-1000-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: The GPIB-ENET/1000 software includes a firmware update feature you can use to access new features that may be added to the GPIB-ENET/1000 in the future. You must update the firmware to take advantage of any new features. You can obtain the latest upgrade by navigating to ni.com/info in a Web browser

Firmware Update

The GPIB-ENET/1000 software includes a firmware update feature you can use to access new
 features that may be added to the GPIB-ENET/1000 in the future. You must update the
 firmware to take advantage of any new features. You can obtain the latest upgrade by
 navigating to [ni.com/info](http://www.ni.com/info) in a
 Web browser and entering Info Code GPIBENET1000FW.

Notice

not

<!--NI_TOPIC bundle=gpib-enet-1000-getting-started path=installation.html language=enus -->
## TOPIC 00004: GPIB-ENET/1000 Installation

- bundle_id: `gpib-enet-1000-getting-started`
- source_path: `installation.html`
- source_url: https://docs-be.ni.com/bundle/gpib-enet-1000-getting-started/raw/resource/enus/installation.html
- document_id: `gpib-enet-1000-getting-started`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to install the GPIB-ENET/1000: Connect one end of your shielded Ethernet cable to your GPIB-ENET/1000. Connect the other end of the shielded Ethernet cable to your Ethernet network. Connect one end of the power cord to the power supply. Screw the power connector on the o

GPIB-ENET/1000 Installation

Complete the following steps to install the GPIB-ENET/1000:

1. Connect one end of your shielded Ethernet cable to your GPIB-ENET/1000. Connect the other end of the shielded Ethernet cable to your Ethernet network.
2. Connect one end of the power cord to the power supply. Screw the power connector on the other end of the power supply onto the power jack of the GPIB-ENET/1000.
3. Plug the other end of the power cord into an AC outlet. 
 Figure 1.Installing the GPIB-ENET/1000[IMAGE alt='1378' src='GUID-9C0BDE4E-A95E-4003-B80C-C39F9D8B8053-a5.svg']
 1 Front Panel LEDs2 GPIB Cable3 Power Cord
 4 Power Supply5 Ethernet Connector6 Power Connector
 7 Configuration Reset Switch8 Shielded Ethernet Cable9 To Ethernet Network
4. Refer to the [Baseplate Identification Label](#GUID-763A5A8A-1D0C-45F7-A6A5-B3D5A1E951EB) on the base of the GPIB-ENET/1000 and make a note of the serial number, MAC address (Ethernet address), and default hostname. You will need this information when you run some of the utilities.
5. Contact your network administrator to determine whether your network supports DHCP or if you need to manually perform the Ethernet configuration to set up the network parameters. If your network uses DHCP, the network configuration is performed automatically at startup. If your network does not use DHCP, Auto IP (link-local) addressing is used to acquire an initial IP address. A steady green READY LED indicates the GPIB-ENET/1000 finished its boot process and acquired its IP address. The unit is now ready to operate. You may need to run software configuration and verification utilities at this time.
6. Connect the GPIB cable to the GPIB-ENET/1000. Connect the other end to your GPIB instrument.

#### Baseplate Identification Label

When you configure the GPIB-ENET/1000 for use on your network, you will need to
 differentiate it from other network devices. Every GPIB-ENET/1000 has a unique serial number,
 Ethernet address, and default hostname. You can find this information on the baseplate
 identification label on the GPIB-ENET/1000.

Note

[IMAGE alt='1378' src='GUID-A03375C3-545B-4424-AD69-223BB954A807-a5.svg']

| 1 Serial Number | 2 MAC Address (Ethernet Address) | 3 Default Hostname |
| --- | --- | --- |

#### Startup

Turn on the front-panel power switch. The POWER LED lights steady green. The READY LED blinks green rapidly while the GPIB-ENET/1000 completes its boot process and attempts to acquire its network parameters.

By default, the GPIB-ENET/1000 attempts its network configuration automatically through DHCP. If there is no DHCP response, the GPIB-ENET/1000 reverts to Auto IP addressing and assigns itself an IP address in the range of 169.254.x.x. Refer to [Auto IP Addressing](ethernet-config.html#GUID-CEAFAF27-EEEC-4519-A1A1-632F740C7C99) for more information. The time required for assigning the IP address depends on your network and the configuration of your GPIB-ENET/1000. Allow up to 30 seconds and observe the state of the READY LED to determine the outcome of the boot process. One of the following should occur:

- A steady green READY LED indicates the GPIB-ENET/1000 finished the boot process and acquired its IP address. The unit is now ready to operate. When using DHCP, the GPIB-ENET/1000 typically is ready to operate about 15 seconds after you power it on.
- If the READY LED blinks a slow red pattern, the GPIB-ENET/1000 boot process failed. Refer to READY LED Signaling to interpret the flash pattern before calling National Instruments Technical Support.
- A steady red READY LED indicates that the GPIB-ENET/1000 has corrupt firmware and has entered Safe Mode. The only operation allowed in Safe Mode is to update the firmware. Refer to the Firmware Update section for instructions on how to update the firmware. Table[#GUID-A1C8E5AA-8481-4870-9D4F-5D20E071439A__ID-000001db](#GUID-A1C8E5AA-8481-4870-9D4F-5D20E071439A__ID-000001db) summarizes the functionality of all the front-panel LEDs on the GPIB-ENET/1000. Table 2.GPIB-ENET/1000 LED DescriptionsLED
 DescriptionPOWER
 Indicates the power cord is connected and the GPIB-ENET/1000 is switched on.
 READY
 Flashes green rapidly at startup while booting and acquiring network parameters. A steady green state indicates the unit is ready for operation. A steady red or slow red blinking pattern indicates an error occurred.
 TALK
 Indicates the GPIB-ENET/1000 is configured as a GPIB Talker.
 LISTEN
 Indicates the GPIB-ENET/1000 is configured as a GPIB Listener.
 ACT/LINK
 Indicates the GPIB-ENET/1000 detected an Ethernet link and blinks to indicate network activity.

##### Ethernet Connector LEDs

The Ethernet connector LEDs on the back panel, shown in the following figure, indicate your Ethernet connection status.

Figure 2.

[IMAGE alt='1378' src='GUID-41C96CCE-7917-4FA1-8918-56737E536805-a5.svg']

The 10/100/1000 LED indicates your Ethernet connection speed.

- Yellow—Indicates your network connection is 1000 Mbit/s.
- Green—Indicates your network connection is 100 Mbit/s.
- Off—Indicates your network connection is 10 Mbit/s, or the Ethernet is not connected if the ACT/LINK LED also is off. The ACT/LINK LED indicates network activity.
- Steady green—Indicates you have a network link, but no network activity is detected.
- Blinking green—Indicates you have a network link and network activity is detected.
- Off—Indicates you do not have a network link.

<!--NI_TOPIC bundle=gpib-enet-1000-getting-started path=overview.html language=enus -->
## TOPIC 00005: GPIB-ENET/1000 Getting Started

- bundle_id: `gpib-enet-1000-getting-started`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/gpib-enet-1000-getting-started/raw/resource/enus/overview.html
- document_id: `gpib-enet-1000-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: The GPIB‑ENET/1000 Instrument Control Device is an IEEE 488 controller device for computers with an Ethernet port. You can use this device to share a single GPIB system among many networked users or to control several test systems from a single networked host. The GPIB‑ENET/1000 features a password-

GPIB-ENET/1000 Getting Started

The GPIB‑ENET/1000 Instrument Control Device is an IEEE 488 controller device
 for computers with an Ethernet port. You can use this device to share a single
 GPIB system among many networked users or to control several test systems from a single
 networked host. The GPIB‑ENET/1000 features a password-protected web interface for easy
 configuration. It can also control IEEE 488 devices from anywhere on an Ethernet‑based (LAN)
 TCP/IP network (Gigabit, 100BASE‑TX, 10BASE‑T). Each device interfaces to and shares up to 14
 GPIB devices from several network hosts, and you can control up to 100 GPIB‑ENET/1000 interfaces
 with a single computer. The device includes a license for the NI‑488.2 driver software,
 providing maximum reliability for connecting to third-party instruments with GPIB.

© 2001–2023 National Instruments Corporation. All rights reserved. Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.

<!--NI_TOPIC bundle=gpib-enet-1000-getting-started path=pinout.html language=enus -->
## TOPIC 00006: GPIB Pinout

- bundle_id: `gpib-enet-1000-getting-started`
- source_path: `pinout.html`
- source_url: https://docs-be.ni.com/bundle/gpib-enet-1000-getting-started/raw/resource/enus/pinout.html
- document_id: `gpib-enet-1000-getting-started`
- page_type: `leaf`
- content_type: `reference`
- source_description: Signal Descriptions Signal Terminal Description DIO1 1 Data Input/Output Bit. DIO2 2 Data Input/Output Bit. DIO3 3 Data Input/Output Bit. DIO4 4 Data Input/Output Bit. EOI 5 End-Or-Identify. DAV 6 Data Valid. NRFD 7 Not Ready For Data. NDAC 8 Not Data Accepted. IFC 9 Interface Clear. SRQ 10 Service

GPIB Pinout

[IMAGE alt='1378' src='GUID-C222BF22-4A0A-4664-AD3C-064800201A7A-a5.svg']

| Signal | Terminal | Description |
| --- | --- | --- |
| DIO1 | 1 | Data Input/Output Bit. |
| DIO2 | 2 | Data Input/Output Bit. |
| DIO3 | 3 | Data Input/Output Bit. |
| DIO4 | 4 | Data Input/Output Bit. |
| EOI | 5 | End-Or-Identify. |
| DAV | 6 | Data Valid. |
| NRFD | 7 | Not Ready For Data. |
| NDAC | 8 | Not Data Accepted. |
| IFC | 9 | Interface Clear. |
| SRQ | 10 | Service Request. |
| ATN | 11 | Attention. |
| SHIELD | 12 | Shield. |
| DIO5 | 13 | Data Input/Output Bit. |
| DIO6 | 14 | Data Input/Output Bit. |
| DIO7 | 15 | Data Input/Output Bit. |
| DIO8 | 16 | Data Input/Output Bit. |
| REN | 17 | Remote Enable. |
| GND | 18 | Ground—Wire twisted with DAV. |
| GND | 19 | Ground—Wire twisted with NRFD. |
| GND | 20 | Ground—Wire twisted with NDAC. |
| GND | 21 | Ground—Wire twisted with IFC. |
| GND | 22 | Ground—Wire twisted with SRQ. |
| GND | 23 | Ground—Wire twisted with ATN. |
| SIGNAL GROUND | 24 | Logic Ground. |

Parent topic:

GPIB-ENET/1000 Getting Started

<!--NI_TOPIC bundle=gpib-enet-1000-getting-started path=ready-leds.html language=enus -->
## TOPIC 00007: READY LED Signaling

- bundle_id: `gpib-enet-1000-getting-started`
- source_path: `ready-leds.html`
- source_url: https://docs-be.ni.com/bundle/gpib-enet-1000-getting-started/raw/resource/enus/ready-leds.html
- document_id: `gpib-enet-1000-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: The READY LED blinks red slowly in a distinct pattern to alert you of internal errors. Use this section to interpret and record the pattern that the READY LED flashes, and then contact National Instruments. By recording the READY LED status messages before calling National Instruments, you can save

READY LED Signaling

The READY LED blinks red slowly in a distinct pattern to alert you of internal errors. Use this section to interpret and record the pattern that the READY LED flashes, and then contact National Instruments.

Note

Note

#### Step 1. Count the Long Flashes

A three-second interval, during which the READY LED is off, separates each repetition of the sequence. The sequence begins with a series of long one-second flashes—that is, one second red, one second off. These long flashes represent the digit in the tens column. There can be one to nine long flashes, which represent digits 1 through 9. For example, one long flash represents the digit 1 in the tens column, and nine long flashes represent the digit 9 in the tens column.

#### Step 2. Count the Short Flashes

The long flashes are followed by shorter flashes; each short flash lasts about one-fifth of a second—that is, one-fifth of a second red, one-fifth of a second off. These short flashes represent the digit in the ones column. Again, there can be one to nine flashes, which represent the digits 1 through 9. For example, one short flash represents the digit 1 in the ones column, and nine short flashes represent the digit 9 in the ones column.

Using this method, the READY LED flashes the following sequence to represent status message 11:

<three seconds off> <one long red flash> <one short red flash>
 <three seconds off>…

The READY LED flashes the following sequence to represent status message 31:

<three seconds off> <three long red flashes> <one short red flash> <three seconds off>…

#### Step 3. Record Your Status Code Number

When you have computed your error message number, write it down and also note the ON/OFF state of the ACT/LINK LED. Have this information available when calling National Instruments.

<!--NI_TOPIC bundle=gpib-enet-1000-getting-started path=software.html language=enus -->
## TOPIC 00008: Software Recognition

- bundle_id: `gpib-enet-1000-getting-started`
- source_path: `software.html`
- source_url: https://docs-be.ni.com/bundle/gpib-enet-1000-getting-started/raw/resource/enus/software.html
- document_id: `gpib-enet-1000-getting-started`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Windows, use the GPIB Ethernet Wizard to add the GPIB-ENET/1000 to your system. Launch the GPIB Ethernet Wizard from Start Programs National Instruments NI-488.2 . (Windows 8) Click NI Launcher and select GPIB Ethernet Wizard. Accept the GPIB-ENET/1000 default configuration settings or change the

Software Recognition

In Windows, use the GPIB Ethernet Wizard to add the GPIB-ENET/1000 to your system.
 Launch the GPIB Ethernet Wizard from Start»Programs»National Instruments»NI-488.2. (Windows 8) Click NI Launcher and select GPIB Ethernet Wizard. Accept the
 GPIB-ENET/1000 default configuration settings or change them while running the
 wizard.

On Mac and Linux, use the Add GPIB Hardware Wizard to add the GPIB-ENET/1000 to your system. Click New to launch the Add GPIB Hardware Wizard from the GPIB Explorer utility in the installed NI-488.2 or ni4882 directory. Once the GPIB-ENET/1000 is recognized, you can change the configuration settings as described in the Ethernet Configuration section.

Refer to the installation guide on the media for more details about the GPIB Ethernet Wizard, Add GPIB Hardware Wizard, and GPIB Explorer utility.
