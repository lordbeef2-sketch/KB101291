# NI DOCUMENT BUNDLE: veristand-electric-motor-simulation-toolkit-api-ref

<!--NI_BUNDLE_CHUNK bundle=veristand-electric-motor-simulation-toolkit-api-ref start=1 end=26 -->
<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=emsimvs/emsimvs.html language=enus -->
## TOPIC 00001: NI Electric Motor Simulation Custom Devices (Electric Motor Simulation Toolkit)

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `emsimvs/emsimvs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/emsimvs/emsimvs.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### NI Electric Motor Simulation Custom Devices (Electric Motor Simulation Toolkit)

October 2015, 374169C-01

The NI Electric Motor Simulation Toolkit is an add-on for both the LabVIEW platform and NI VeriStand. On VeriStand, this toolkit allows you to simulate an electric motor. This toolkit extends the functionality of VeriStand by providing a series of custom devices for you to design and implement a real-time motor simulation application. Using this add-on for VeriStand, you can easily run high-fidelity finite element motor models in real time.

This toolkit also combines NI real-time testing software technology with third-party software. You can use this toolkit with JSOL JMAG-RT, part of the [finite element analysis (FEA)](../lvemsimshared/fea_model.html) tool suite from JSOL Corporation. You also can use this toolkit with ANSYS simulation software.

The Electric Motor Simulation Toolkit provides the following custom devices:

- ACIM Constant Parameter Model Custom Device —Enables you to simulate an AC induction motor (ACIM) using the constant parameter model function.
- PMSM Constant Parameter Model Custom Device —Enables you to simulate a permanent magnet synchronous motor (PMSM) using the constant parameter model function.
- PMSM FEA Model Custom Device —Enables you to simulate a PMSM using the FEA model function.
- PMSM Variable Parameter Model Custom Device —Enables you to simulate a PMSM using the variable parameter model function.
- SRM Linear Model Custom Device —Enables you to simulate a switched reluctance motor (SRM) using the linear model function.
- SRM FEA Model Custom Device —Enables you to simulate an SRM using the FEA model function.

JSOL JMAG is a registered trademark of JSOL Corporation. ANSYS is a registered trademark of ANSYS Incorporated.

© 2013–2015 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=emsimvs/emsimvs_acim_cons.html language=enus -->
## TOPIC 00002: ACIM Constant Parameter Model Custom Device

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `emsimvs/emsimvs_acim_cons.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/emsimvs/emsimvs_acim_cons.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### ACIM Constant Parameter Model Custom Device

**Requires:** Electric Motor Simulation Toolkit

After creating an Electric Motor Simulation custom device, you can use the **Custom Device Configuration** page to view or configure the device. This custom device simulates an AC induction motor (ACIM) using the constant parameter model function. Visit ni.com/info and enter the Info Code ex7s7w for more information about configuring the device.

- Custom Device Settings
  - Name —Specifies the name of the custom device. After you change the name of the custom device, the device name in the configuration tree gets updated.
  - Description —Provides a description for the custom device. You can enter customized descriptions in this field.
- ACIM Constant Parameter Model Settings
  - ACIM Parameters —Specifies the parameters describing the characteristics of an ACIM.
    - Number of Poles —Specifies the number of poles in the electric motor. The Number of Poles must be an even number.
    - Stator Leakage Inductance —Specifies the leakage inductance, in henries, of the stator windings. The value of Stator Leakage Inductance must be greater than 0.
    - Rotor Leakage Inductance —Specifies the leakage inductance, in henries, of the rotor windings. The value of Rotor Leakage Inductance must be greater than 0.
    - Magnetizing Inductance —Specifies the magnetizing inductance, in henries, of the motor. The value of Magnetizing Inductance must be greater than 0.
    - Stator Resistance —Specifies the resistance, in ohms, of the stator windings. The value of Stator Resistance must be greater than 0.
    - Rotor Resistance —Specifies the resistance, in ohms, of the rotor windings. The value of Rotor Resistance must be greater than 0.
    - Base Temperature —Specifies the base temperature, in kelvins, for the stator resistance and the rotor resistance. The value of Base Temperature must be equal to or greater than 0.
    - Stator Temperature Coefficient —Specifies the temperature correction coefficient, in K^-1, of the stator resistance.
    - Rotor Temperature Coefficient —Specifies the temperature correction coefficient, in K^-1, of the rotor resistance.
  - Mechanical Parameters —Specifies the mechanical parameters of the electric motor. The mechanical parameters impact the forces and movement of the motor.
    - Inertia —Specifies the moment of inertia, in kgm^2, of the electric motor. The value of Inertia must be equal to or greater than 0.
    - Friction Coefficient —Specifies the friction coefficient of the electric motor. The value of Friction Coefficient must be equal to or greater than 0.
  - dt —Specifies the time interval, in seconds, at which VeriStand simulates the electric motor. The value of dt must be greater than 0. The default value is 9.5E-7.
- Hardware Settings
  - RIO Device —Displays the address to the RIO device.
  - FPGA Bitfile —Displays the path to the FPGA bitfile.
  - Reset —Resets the hardware. Click Reset to reconfigure the RIO device and FPGA bitfile in the Configure FPGA dialog box.

**Related Information**

[Creating and Configuring Custom Devices](../emsimvs/emsimvs_cusdevice.html)

[Configure FPGA Dialog Box](../emsimvs/emsimvs_config_fpga.html)

[Temperature Correction](../lvemsimshared/temp_correction.html)

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=emsimvs/emsimvs_cusdevice.html language=enus -->
## TOPIC 00003: Creating and Configuring Custom Devices (Electric Motor Simulation Toolkit)

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `emsimvs/emsimvs_cusdevice.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/emsimvs/emsimvs_cusdevice.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating and Configuring Custom Devices (Electric Motor Simulation Toolkit)

To create an Electric Motor Simulation custom device in your VeriStand project, open the **System Explorer** window, navigate to **Targets»Controller»Custom Devices**, right-click **Custom Devices**, and select a custom device for electric motor simulation from the shortcut menu. Specify a RIO device and an FPGA bitfile in the **Configure FPGA** dialog box. A new custom device appears under **Custom Devices** in the configuration tree.

The Electric Motor Simulation custom device contains the following channels and folders.

- Inputs channel —Includes the inputs for a custom device.
- Inverter Model channel —Includes the inverter model settings for a custom device.
- Log file channel —Includes the log settings for a custom device.
- Outputs channel —Returns the outputs from a custom device.
- Status channel —Returns the status from a custom device.
- Waveforms channel —Streams the outputs from a custom device as waveforms.

To view or configure a custom device, select the custom device name in the configuration tree of the **System Explorer** window. The **Custom Device Configuration** page appears to the right of the configuration tree. The configuration options that appear can vary depending on the different motor type or model type that you select.

##### Related Information

[System Explorer Window](/csh?topicname=veristand/system_explorer.html)

[Electric Motor Simulation Custom Devices](emsimvs.html)

[Configure FPGA Dialog Box](../emsimvs/emsimvs_config_fpga.html)

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=emsimvs/emsimvs_inputs.html language=enus -->
## TOPIC 00004: Inputs Channels

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `emsimvs/emsimvs_inputs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/emsimvs/emsimvs_inputs.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Inputs Channels

**Requires:** Electric Motor Simulation Toolkit

Lists the **Inputs** channels that the Electric Motor Simulation custom devices provide.

- Coil Temperature —Specifies the temperature, in kelvins, of the motor coil. If the value of Coil Temperature is greater than 0, the custom device performs the temperature correction functionality for the motor resistance. The default is 0.
- Enable —Specifies whether to enable a motor simulator. On the Enable channel, place a checkmark in the Default Enable Value checkbox to indicate that the motor simulator is enabled when the custom device starts running. By default, the motor simulator is off. After the custom device starts running, a nonzero value specifies that the motor simulator is enabled.
- Load Torque —Specifies the load torque, in newton meters, that you apply externally to the motor.
- Magnet Temperature —Specifies the temperature, in kelvins, of the motor magnet. If the value of Magnet Temperature is greater than 0, the custom device performs the temperature correction functionality for the magnet flux. The default is 0.
- Rotor Temperature —Specifies the temperature, in kelvins, of the motor rotor. If the value of Rotor Temperature is greater than 0, the custom device performs the temperature correction functionality for the rotor resistance. The default is 0.
- Stator Temperature —Specifies the temperature, in kelvins, of the motor stator. If the value of Stator Temperature is greater than 0, the custom device performs the temperature correction functionality for the stator resistance. The default is 0.

**Related Information**

[Temperature Correction](../lvemsimshared/temp_correction.html)

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=emsimvs/emsimvs_inverter.html language=enus -->
## TOPIC 00005: Inverter Model Channels

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `emsimvs/emsimvs_inverter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/emsimvs/emsimvs_inverter.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Inverter Model Channels

**Requires:** Electric Motor Simulation Toolkit

Lists the [inverter model](../lvemsimshared/inverter.html) settings for the PMSM custom devices.

- Inverter Model Settings
  - Default Inverter Type —Specifies whether the default type of the inverter model is ideal or advanced.
  - Inverter Parameters —Specifies the parameters describing the characteristics of the advanced inverter.
    - IGBT Forward Voltage Drop —Specifies the forward voltage drop, in volts, of the insulated gate bipolar transistor (IGBT) in the inverter. The value of IGBT Forward Voltage Drop must be equal to or greater than 0. The default is 0.
    - Diode Forward Voltage Drop —Specifies the forward voltage drop, in volts, of the diode in the inverter. The value of Diode Forward Voltage Drop must be equal to or greater than 0. The default is 0.
    - Conductance —Specifies the conductance, in siemens, of the switches in the inverter. The value of Conductance must be greater than 0. The default is 1.
- Fault Switch Index —Specifies the index of the switch which is in fault state. The following table shows details about the fault switch indexes. 
 0
**Phase A Upper Switch** (default)
1
**Phase A Lower Switch**
2
**Phase B Upper Switch**
3
**Phase B Lower Switch**
4
**Phase C Upper Switch**
5
**Phase C Lower Switch**
- Fault Type —Controls the fault type of the advanced inverter. The following table shows details about the fault types. 
 0
**No Fault** (default)—No fault occurs.
1
**IGBT Open Fault**—Any IGBT is interrupted.
2
**Diode Open Fault**—Any diode is interrupted.
3
**IGBT and Diode Open Fault**—Any IGBT with diode is interrupted.
4
**IGBT or Diode Short Fault**—Any IGBT or diode is bypassed.
- Inverter Type —Controls the type of the inverter. The following table shows details about the inverter types. 
 0
**Ideal** (default)—The inverter is an ideal three-phase inverter.
1
**Advanced**—The inverter is an advanced three-phase inverter.

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=emsimvs/emsimvs_log.html language=enus -->
## TOPIC 00006: Log File Channels

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `emsimvs/emsimvs_log.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/emsimvs/emsimvs_log.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Log File Channels

**Requires:** Electric Motor Simulation Toolkit

Lists the log settings for the custom device.

The log file stores the data logging from the [Waveforms channel](emsimvs_waveforms.html). You can use the log file to track how the motor is running, review details about the motor status, and analyze the data changes.

The custom device logs data in .tdms format. You can use the .tdms files to exchange data between NI software, such as LabVIEW and DIAdem.

- Log File Settings
  - Base File Name —Specifies the base filename of the log file. The custom device appends a timestamp to the base filename.
  - Log File Directory —Specifies the path to save the log file. The default value is c:\logs\EMSim .
  - Example Log File Path —Provides a preview of the path to the log file. The log file is a .tdms file and the filename consists of the Base File Name and the timestamp when you create the log file.
  - Decimation Factor —Specifies the decimation factor at which the custom device decimates the state of the motor simulator running on the FPGA target. For example, if you specify a decimation factor of 10, the custom device gets the state of the simulator after every tenth iteration. The default value is 10.
 [IMAGE alt='image' src='note.gif']**Note** NI recommends that you specify a decimation factor that is greater than 5. When the decimation factor is less than 5, data loss may occur depending on the hardware you use and the network activity.
  - Max File Size —Specifies the maximum size limit for each log file. If the size of the current log file exceeds the Max File Size , the custom device closes the current log file and creates a new file for data logging. The default value is 750 MB.
  - Max Disk Usage —Specifies the maximum disk usage limit for all the log files. If the total size of the log files in the Log File Directory exceeds the Max Disk Usage , the custom device frees disk space by deleting the oldest log files. The default value is 20 GB. [IMAGE alt='image' src='note.gif']**Note** Set the value of **Max Disk Usage** according to the size of available disk space on the hardware that you use. The value of **Max Disk Usage** must be smaller than the size of available disk space.
- Log Command —Controls the data logging operation. The following table shows details about the log commands. 
 0
**Idle** (default)—No command.
1
**Create New Log File**—Logs data to a new file and closes the current log file.
2
**Close Log File**—Closes the current log file. 
This channel is reset to 0 (Idle) after the custom device processes the log command each time.
- Stream Trigger —Specifies whether to stream data from the simulator to the Waveforms channel and the log file. On the Stream Trigger channel, place a checkmark in the Default Trigger Value checkbox to indicate that the stream is on when the custom device starts running. By default, the stream trigger is off. After the custom device starts running, a nonzero value specifies that the stream trigger is on, and the custom device starts streaming data to the Waveforms channel and log files.

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=emsimvs/emsimvs_outputs.html language=enus -->
## TOPIC 00007: Outputs Channels

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `emsimvs/emsimvs_outputs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/emsimvs/emsimvs_outputs.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Outputs Channels

**Requires:** Electric Motor Simulation Toolkit

Lists the **Outputs** channels that the Electric Motor Simulation custom devices provide.

- Electromagnetic Torque —Returns the electromagnetic torque, in newton meters, that the electric motor generates inside the motor while the motor is running.
- Hall A, B, and C —Returns the state of Hall A, B, and C in three channels.
- Ia, Ib, Ic, … —Returns the phase current, in amperes, of the electric motor. Permanent magnet synchronous motors (PMSM) return three-phase current in three channels, while switched reluctance motors (SRM) return five-phase current in five channels. [IMAGE alt='image' src='note.gif']**Note** For three-phase SRMs, the **Id** and **Ie** channels return null. For four-phase SRMs, the **Ie** channel returns null.
- Position —Returns the mechanical rotor position, in degrees, of the electric motor.
- Resolver Cosine, Resolver Reference, and Resolver Sine —Returns the resolver outputs in three channels, including the reference signals, sine signals, and cosine signals.
- Speed —Returns the speed, in revolutions per minute, of the motor.
- Va, Vb, Vc, … —Returns the phase voltage in volts. Permanent magnet synchronous motors (PMSM) return three-phase voltage in three channels, while switched reluctance motors (SRM) return five-phase voltage in five channels. [IMAGE alt='image' src='note.gif']**Note** For three-phase SRMs, the **Vd** and **Ve** channels return null. For four-phase SRMs, the **Ve** channel returns null.

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=emsimvs/emsimvs_pmsm_cons.html language=enus -->
## TOPIC 00008: PMSM Constant Parameter Model Custom Device

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `emsimvs/emsimvs_pmsm_cons.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/emsimvs/emsimvs_pmsm_cons.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### PMSM Constant Parameter Model Custom Device

**Requires:** Electric Motor Simulation Toolkit

After creating an Electric Motor Simulation custom device, you can use the **Custom Device Configuration** page to view or configure the device. This custom device simulates a permanent magnet synchronous motor (PMSM) using the constant parameter model function. Visit ni.com/info and enter the Info Code ex7s7w for more information about configuring the device.

- Custom Device Settings
  - Name —Specifies the name of the custom device. After you change the name of the custom device, the device name in the configuration tree gets updated.
  - Description —Provides a description for the custom device. You can enter customized descriptions in this field.
- PMSM Constant Parameter Model Settings
  - PMSM Parameters —Specifies the parameters describing the characteristics of a PMSM.
    - Number of Poles —Specifies the number of poles in the electric motor. The Number of Poles must be an even number.
    - Resistance —Specifies the resistance, in ohms, of the electric motor. The value of Resistance must be greater than 0.
    - D Inductance —Specifies the inductance, in henries, along the d or direct axis. The value of D Inductance must be greater than 0.
    - Q Inductance —Specifies the inductance, in henries, along the q or quad axis. The value of Q Inductance must be greater than 0.
    - Flux Linkage —Specifies the flux linkage, in webers, between the rotor and the stator. The value of Flux Linkage must be greater than 0.
  - Mechanical Parameters —Specifies the mechanical parameters of the electric motor. The mechanical parameters impact the forces and movement of the motor.
    - Inertia —Specifies the moment of inertia, in kgm^2, of the electric motor. The value of Inertia must be equal to or greater than 0.
    - Friction Coefficient —Specifies the friction coefficient of the electric motor. The value of Friction Coefficient must be equal to or greater than 0.
  - DC Voltage —Specifies the voltage, in volts, of the direct current (DC) to apply to the inverter in the electric motor. The value of DC Voltage must be greater than 0.
  - dt —Specifies the time interval, in seconds, at which VeriStand simulates the electric motor. The value of dt must be greater than 0. The default value is 9.5E-7.
- Hardware Settings
  - RIO Device —Displays the address to the RIO device.
  - FPGA Bitfile —Displays the path to the FPGA bitfile.
  - Reset —Resets the hardware. Click Reset to reconfigure the RIO device and FPGA bitfile in the Configure FPGA dialog box.

**Related Information**

[Creating and Configuring Custom Devices](../emsimvs/emsimvs_cusdevice.html)

[Configure FPGA Dialog Box](../emsimvs/emsimvs_config_fpga.html)

[Three-Phase Inverter](../lvemsimshared/inverter.html)

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=emsimvs/emsimvs_pmsm_fea.html language=enus -->
## TOPIC 00009: PMSM FEA Model Custom Device

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `emsimvs/emsimvs_pmsm_fea.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/emsimvs/emsimvs_pmsm_fea.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### PMSM FEA Model Custom Device

**Requires:** Electric Motor Simulation Toolkit

After creating an Electric Motor Simulation custom device, you can use the **Custom Device Configuration** page to view or configure the device. This custom device simulates a permanent magnet synchronous motor (PMSM) using the finite element analysis (FEA) model function. Visit ni.com/info and enter the Info Code ex7s7w for more information about configuring the device.

- Custom Device Settings
  - Name —Specifies the name of the custom device. After you change the name of the custom device, the device name in the configuration tree gets updated.
  - Description —Provides a description for the custom device. You can enter customized descriptions in this field.
- PMSM FEA Model Settings
  - RTT File —Specifies the path to an RTT file. The RTT file contains motor parameters and data that the JMAG-RT software generates. For an FEA model, the RTT file is required. You must specify an RTT file that matches the FPGA bitfile you specify in the Configure FPGA dialog box. For example, you must not use an RTT file for PMSMs with an FPGA bitfile for SRMs. Even for the same type of motor, you must not use an RTT file for three-phase SRMs with an FPGA bitfile for four-phase SRMs.
  - Motor and Mechanical Parameters
    - Base Values —Specifies the voltage, current, and speed in a defined base unit quantity. Using base quantities simplifies the calculations because quantities expressed as per-unit are the same regardless of the voltage level. The FPGA VIs utilize the per-unit system for electric motor simulation.
      - Voltage Base —Specifies the base value of the voltage, in volts, that you use to convert an engineering unit to a per-unit, and vice versa. The default value is 1 volt.
      - Current Base —Specifies the base value of the current, in amperes, that you use to convert an engineering unit to a per-unit, and vice versa. The default value is 1 ampere.
      - Speed Base —Specifies the base value of the speed, in revolutions per minute, that you use to convert an engineering unit to a per-unit, and vice versa. The default value is 1 revolution per minute.
    - Mechanical Parameters —Specifies the mechanical parameters of the electric motor. The mechanical parameters impact the forces and movement of the motor.
      - Inertia —Specifies the moment of inertia, in kgm^2, of the electric motor. The value of Inertia must be equal to or greater than 0.
      - Friction Coefficient —Specifies the friction coefficient of the electric motor. The value of Friction Coefficient must be equal to or greater than 0.
    - Resistances —Specifies the resistances, in ohms, of the stator winding under all phases of the three-phase current. All resistances must be greater than 0. If all resistances are equal to or less than 0, this custom device reads Resistances from the RTT File for calculation. Otherwise, this custom device returns an error.
      - A Resistance —Specifies the resistance, in ohms, of the stator winding under phase A of the three-phase current.
      - B Resistance —Specifies the resistance, in ohms, of the stator winding under phase B of the three-phase current.
      - C Resistance —Specifies the resistance, in ohms, of the stator winding under phase C of the three-phase current.
    - DC Voltage —Specifies the voltage, in volts, of the direct current (DC) to apply to the inverter in the electric motor. The value of DC Voltage must be greater than 0.
    - dt —Specifies the time interval, in seconds, at which VeriStand simulates the electric motor. The value of dt must be greater than 0. The default value is 1.6E-6.
  - Temperature Correction Parameters —Specifies the characteristics of the electric motor for temperature correction. If the value of any temperature correction parameter is not a number ( NaN ), the custom device reads the temperature correction parameter from the RTT file you specified in RTT File .
    - Coil Base Temperature —Specifies the base temperature, in kelvins, of the motor coil. The value of Coil Base Temperature must be equal to or greater than 0. The default is NaN .
    - Coil Temperature Coefficient —Specifies the temperature correction coefficient, in K^-1, of the motor resistance. The material of the coil determines the value of Coil Temperature Coefficient . The default is NaN .
    - Magnet Base Temperature —Specifies the base temperature, in kelvins, of the motor magnet. The value of Magnet Base Temperature must be equal to or greater than 0. The default is NaN .
    - Magnet Temperature Coefficient —Specifies the temperature correction coefficient, in K^-1, of the magnet flux. The material of the magnet determines the value of Magnet Temperature Coefficient . The default is NaN .
- Hardware Settings
  - RIO Device —Displays the address to the RIO device.
  - FPGA Bitfile —Displays the path to the FPGA bitfile.
  - Reset —Resets the hardware. Click Reset to reconfigure the RIO device and FPGA bitfile in the Configure FPGA dialog box.

**Related Information**

[Creating and Configuring Custom Devices](../emsimvs/emsimvs_cusdevice.html)

[Configure FPGA Dialog Box](../emsimvs/emsimvs_config_fpga.html)

[Base Value](../lvemsimshared/base_value.html)

[Three-Phase Inverter](../lvemsimshared/inverter.html)

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=emsimvs/emsimvs_pmsm_vari.html language=enus -->
## TOPIC 00010: PMSM Variable Parameter Model Custom Device

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `emsimvs/emsimvs_pmsm_vari.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/emsimvs/emsimvs_pmsm_vari.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### PMSM Variable Parameter Model Custom Device

**Requires:** Electric Motor Simulation Toolkit

After creating an Electric Motor Simulation custom device, you can use the **Custom Device Configuration** page to view or configure the device. This custom device simulates a permanent magnet synchronous motor (PMSM) using the variable parameter model function. Visit ni.com/info and enter the Info Code ex7s7w for more information about configuring the device.

- Custom Device Settings
  - Name —Specifies the name of the custom device. After you change the name of the custom device, the device name in the configuration tree gets updated.
  - Description —Provides a description for the custom device. You can enter customized descriptions in this field.
- PMSM Variable Parameter Model Settings
  - Model File (*.rtt, *.txt, *.csv) —Specifies the path to a model file that contains motor parameters information. For a variable parameter model, the model file can be an RTT file, a TXT file, or a CSV file. The RTT file contains motor parameters and data that the JMAG-RT software generates. The RTT file must match the FPGA bitfile you specify in the Configure FPGA dialog box. For example, you must not use an RTT file for PMSMs with an FPGA bitfile for SRMs.
 The TXT file contains motor parameters and data that the ANSYS simulation software generates.
 The CSV file contains motor parameters information for an external model. Visit ni.com/info and enter the Info Code exvd68 for a template CSV file.
  - Table Size —Specifies the number of rows and columns in a two-dimensional table. By default, the table has the same number of rows and columns. The value of Table Size must be greater than 0. The default is 100. Table Size is enabled only when you specify an RTT file in Model File (*.rtt, *.txt, *.csv) .
  - Delimiter —Specifies the character or string of characters to use to separate fields in the CSV file. For example, a value of , (comma) specifies a single comma as the delimiter. The default is , (comma). Delimiter is enabled only when you specify a CSV file in Model File (*.rtt, *.txt, *.csv) .
  - Resistance —Specifies the resistance, in ohms, of the electric motor. If the value of Resistance is equal or less than 0, this custom device reads Resistance from Model File (*.rtt, *.txt, *.csv) . The default is -1.
  - DC Voltage —Specifies the voltage, in volts, of the direct current (DC) to apply to the inverter in the electric motor. The value of DC Voltage must be greater than 0.
  - dt —Specifies the time interval, in seconds, at which this custom device simulates the electric motor. The value of dt must be greater than 0. The default is 1E-6.
  - Mechanical Parameters —Specifies the mechanical parameters of the electric motor. The mechanical parameters impact the forces and movement of the motor.
    - Inertia —Specifies the moment of inertia, in kgm^2, of the electric motor. The value of Inertia must be equal to or greater than 0.
    - Friction Coefficient —Specifies the friction coefficient of the electric motor. The value of Friction Coefficient must be equal to or greater than 0.
  - Temperature Correction Parameters —Specifies the characteristics of the electric motor for temperature correction. If the value of any temperature correction parameter is not a number ( NaN ), the custom device reads the temperature correction parameter from the model file which you specified in Model File (*.rtt, *.txt, *.csv) .
    - Coil Base Temperature —Specifies the base temperature, in kelvins, of the motor coil. The value of Coil Base Temperature must be equal to or greater than 0. The default is NaN .
    - Coil Temperature Coefficient —Specifies the temperature correction coefficient, in K^-1, of the motor resistance. The material of the coil determines the value of Coil Temperature Coefficient . The default is NaN .
    - Magnet Base Temperature —Specifies the base temperature, in kelvins, of the motor magnet. The value of Magnet Base Temperature must be equal to or greater than 0. The default is NaN .
    - Magnet Temperature Coefficient —Specifies the temperature correction coefficient, in K^-1, of the magnet flux. The material of the magnet determines the value of Magnet Temperature Coefficient . The default is NaN .
- Hardware Settings
  - RIO Device —Displays the address to the RIO device.
  - FPGA Bitfile —Displays the path to the FPGA bitfile.
  - Reset —Resets the hardware. Click Reset to reconfigure the RIO device and FPGA bitfile in the Configure FPGA dialog box.

**Related Information**

[Creating and Configuring Custom Devices](../emsimvs/emsimvs_cusdevice.html)

[Configure FPGA Dialog Box](../emsimvs/emsimvs_config_fpga.html)

[Three-Phase Inverter](../lvemsimshared/inverter.html)

[Temperature Correction](../lvemsimshared/temp_correction.html)

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=emsimvs/emsimvs_related_doc.html language=enus -->
## TOPIC 00011: Related Documentation (Electric Motor Simulation Toolkit)

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `emsimvs/emsimvs_related_doc.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/emsimvs/emsimvs_related_doc.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Related Documentation (Electric Motor Simulation Toolkit)

The following documents contain information that you may find helpful as you use the Electric Motor Simulation Toolkit.

- Electric Motor Simulation Toolkit Readme —Use this file to obtain introductory information about the Electric Motor Simulation Toolkit, such as a product overview, system requirements, installation instructions, activation instructions, help resources, and known issues. Open this readme by navigating to the veristand\readme directory and opening readme_EMSim.html . If you install the LabVIEW component of this toolkit, you also can find this readme document by navigating to the labview\readme directory.
- LabVIEW Help —This help file contains information about LabVIEW palettes, VIs, examples, and sample projects. This help file also includes step-by-step instructions and tutorials for using LabVIEW features. Refer to the Toolkits»Electric Motor Simulation Toolkit book on the Contents tab of the LabVIEW Help for more information about the using this toolkit on the LabVIEW platform. 
 [IMAGE alt='image' src='note.gif']
 **Note** You must install LabVIEW to access the LabVIEW Help. If you do not have LabVIEW installed but want to see the help, you can find the online help on the NI website at ni.com. Refer to the NI Product Manuals Library at ni.com/manuals for updated documentation resources.
- NI VeriStand Help —This help file contains information about the VeriStand environment, projects, and custom devices. This help file also includes instructions about using the custom devices with VeriStand projects.

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=emsimvs/emsimvs_srm_fea.html language=enus -->
## TOPIC 00012: SRM FEA Model Custom Device

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `emsimvs/emsimvs_srm_fea.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/emsimvs/emsimvs_srm_fea.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SRM FEA Model Custom Device

**Requires:** Electric Motor Simulation Toolkit

After creating an Electric Motor Simulation custom device, you can use the **Custom Device Configuration** page to view or configure the device. This custom device simulates a switched reluctance motor (SRM) using the finite element analysis (FEA) model function. Visit ni.com/info and enter the Info Code ex7s7w for more information about configuring the device.

- Custom Device Settings
  - Name —Specifies the name of the custom device. After you change the name of the custom device, the device name in the configuration tree gets updated.
  - Description —Provides a description for the custom device. You can enter customized descriptions in this field.
- SRM FEA Model Settings
  - RTT File —Specifies the path to an RTT file. The RTT file contains motor parameters and data that the JMAG-RT software generates. For an FEA model, the RTT file is required. You must specify an RTT file that matches the FPGA bitfile you specify in the Configure FPGA dialog box. For example, you must not use an RTT file for PMSMs with an FPGA bitfile for SRMs. Even for the same type of motor, you must not use an RTT file for three-phase SRMs with an FPGA bitfile for four-phase SRMs.
  - Base Values —Specifies the voltage, current, and speed in a defined base unit quantity. Using base quantities simplifies the calculations because quantities expressed as per-unit are the same regardless of the voltage level. The FPGA VIs utilize the per-unit system for electric motor simulation.
    - Voltage Base —Specifies the base value of the voltage, in volts, that you use to convert an engineering unit to a per-unit, and vice versa. The default value is 1 volt.
    - Current Base —Specifies the base value of the current, in amperes, that you use to convert an engineering unit to a per-unit, and vice versa. The default value is 1 ampere.
    - Speed Base —Specifies the base value of the speed, in revolutions per minute, that you use to convert an engineering unit to a per-unit, and vice versa. The default value is 1 revolution per minute.
  - dt —Specifies the time interval, in seconds, at which VeriStand simulates the electric motor. The value of dt must be greater than 0. The default value is 0. You must specify dt according to the number of phases in the SRM. NI recommends that you set dt to 0.95E-6 for three-phase SRMs, 1.3E-6 for four-phase SRMs, and 1.7E-6 for five-phase SRMs.
  - Initial Rotor Position —Specifies the mechanical rotor position, in degrees, when the motor starts.
  - Mechanical Parameters —Specifies the mechanical parameters of the electric motor. The mechanical parameters impact the forces and movement of the motor.
    - Inertia —Specifies the moment of inertia, in kgm^2, of the electric motor. The value of Inertia must be equal to or greater than 0.
    - Friction Coefficient —Specifies the friction coefficient of the electric motor. The value of Friction Coefficient must be equal to or greater than 0.
  - DC Voltage —Specifies the voltage, in volts, of the direct current (DC) to apply to the inverter in the electric motor. The value of DC Voltage must be greater than 0.
  - Resistance —Specifies resistance, in ohms, of the stator winding. The value of Resistance must be greater than 0. If the value of Resistance is equal to or less than 0, this custom device uses the resistance in the RTT file for calculation. The default value is -1.
- Hardware Settings
  - RIO Device —Displays the address to the RIO device.
  - FPGA Bitfile —Displays the path to the FPGA bitfile.
  - Reset —Resets the hardware. Click Reset to reconfigure the RIO device and FPGA bitfile in the Configure FPGA dialog box.

**Related Information**

[Creating and Configuring Custom Devices](../emsimvs/emsimvs_cusdevice.html)

[Configure FPGA Dialog Box](../emsimvs/emsimvs_config_fpga.html)

[Base Value](../lvemsimshared/base_value.html)

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=emsimvs/emsimvs_srm_line.html language=enus -->
## TOPIC 00013: SRM Linear Model Custom Device

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `emsimvs/emsimvs_srm_line.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/emsimvs/emsimvs_srm_line.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SRM Linear Model Custom Device

**Requires:** Electric Motor Simulation Toolkit

After creating an Electric Motor Simulation custom device, you can use the **Custom Device Configuration** page to view or configure the device. This custom device simulates a switched reluctance motor (SRM) using the linear model function. Visit ni.com/info and enter the Info Code ex7s7w for more information about configuring the device.

- Custom Device Settings
  - Name —Specifies the name of the custom device. After you change the name of the custom device, the device name in the configuration tree gets updated.
  - Description —Provides a description for the custom device. You can enter customized descriptions in this field.
- SRM Linear Model Settings
  - SRM Parameters —Specifies the parameters describing the linear model of an SRM.
    - Number of Phases —Specifies the number of phases in an electric motor. The Number of Phases must be 3, 4, or 5.
    - Number of Poles —Specifies the number of poles in the electric motor. The Number of Poles must be an even number.
    - Initial Rotor Position —Specifies the mechanical rotor position, in degrees, when the motor starts.
    - Rotor Position Offset —Specifies the angle, in degrees, between the rotor salient pole and the stator salient pole when the rotor position is 0.
    - Unaligned Inductance —Specifies the equivalent inductance, in henries, of the coil at the unaligned position. The value of Unaligned Inductance must be greater than 0.
    - Aligned Flux —Specifies the flux, in webers, of the Saturated Position Current at the aligned position. The value of Aligned Flux must be greater than 0.
    - Saturated Position Current —Specifies the current, in amperes, of the coil at the saturated position. The value of Saturated Position Current must be greater than 0.
    - Maximum Current —Specifies the maximum current in amperes. The value of Maximum Current must be greater than 0.
  - Mechanical Parameters —Specifies the mechanical parameters of the electric motor. The mechanical parameters impact the forces and movement of the motor.
    - Inertia —Specifies the moment of inertia, in kgm^2, of the electric motor. The value of Inertia must be equal to or greater than 0.
    - Friction Coefficient —Specifies the friction coefficient of the electric motor. The value of Friction Coefficient must be equal to or greater than 0.
  - dt —Specifies the time interval, in seconds, at which VeriStand simulates the electric motor. The value of dt must be greater than 0. The default value is 8E-7.
  - DC Voltage —Specifies the voltage, in volts, of the direct current (DC) to apply to the inverter in the electric motor. The value of DC Voltage must be greater than 0.
  - Resistance —Specifies the resistance, in ohms, of the electric motor. The value of Resistance must be greater than 0.
- Hardware Settings
  - RIO Device —Displays the address to the RIO device.
  - FPGA Bitfile —Displays the path to the FPGA bitfile.
  - Reset —Resets the hardware. Click Reset to reconfigure the RIO device and FPGA bitfile in the Configure FPGA dialog box.

**Related Information**

[Creating and Configuring Custom Devices](../emsimvs/emsimvs_cusdevice.html)

[Configure FPGA Dialog Box](../emsimvs/emsimvs_config_fpga.html)

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=emsimvs/emsimvs_status.html language=enus -->
## TOPIC 00014: Status Channel

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `emsimvs/emsimvs_status.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/emsimvs/emsimvs_status.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Status Channel

**Requires:** Electric Motor Simulation Toolkit

Lists the **Status** channel that the Electric Motor Simulation custom devices provide.

- Simulation Loop Rate —Returns the loop rate, in microseconds, of the simulator. The loop rate is the time between loop iterations that the motor simulator runs on an FPGA target.

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=emsimvs/emsimvs_waveforms.html language=enus -->
## TOPIC 00015: Waveforms Channels

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `emsimvs/emsimvs_waveforms.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/emsimvs/emsimvs_waveforms.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Waveforms Channels

**Requires:** Electric Motor Simulation Toolkit

Lists the outputs from a custom device as [waveforms](/csh?topicname=veristandmerge/planning_cd_chans.html). Using waveforms allows you to acquire outputs from a custom device at a rate faster than the rate at which the system runs.

The **Waveforms** channels consist of the **Coil Temperature** channel, the **Load Torque** channel, the **Magnet Temperature** channel, the **Rotor Temperature** channel, the **Stator Temperature** channel, and all [outputs channels](../emsimvs/emsimvs_outputs.html).

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/ansys_file.html language=enus -->
## TOPIC 00016: ANSYS Motor Model File (Electric Motor Simulation Toolkit)

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/ansys_file.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/ansys_file.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### ANSYS Motor Model File (Electric Motor Simulation Toolkit)

ANSYS is a company that provides engineering simulation solutions. The ANSYS motor model file is the motor model file that the ANSYS simulation software generates. The ANSYS motor model file is in the TXT file format. The TXT file contains basic motor characteristics, such as the three-phase resistances and the number of poles. The TXT file also contains detailed motor parameters information, which are the analysis results of the ANSYS simulation software.

You can use the Electric Motor Simulation Toolkit to read an ANSYS motor model file if you use the variable parameter model for permanent magnet synchronous motors (PMSM). Refer to the ANSYS Incorporated website at www.ansys.com for more information about the ANSYS simulation software and the ANSYS motor model files.

##### Related Information

[Variable Parameter Model](../lvemsimshared/vari_para_model.html)

[PMSM](../lvemsimshared/motor_type.html#pmsm)

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/base_value.html language=enus -->
## TOPIC 00017: Base Value (Electric Motor Simulation Toolkit)

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/base_value.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/base_value.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Base Value (Electric Motor Simulation Toolkit)

Apart from the engineering units, electrical engineers also use per-unit to measure quantities in physics. A per-unit system expresses system quantities as fractions of a defined base unit quantity. The per-unit system scales the actual value of a physical quantity, such as current, voltage, and speed, with a selected constant of the same measuring unit. The ratio of the actual value to the constant is the per-unit value of the physical quantity. The selected constant, also known as base value, has the same measuring unit as the actual value.

The following equation explains the relationship between a per-unit value and a base value.

[IMAGE alt='image' src='eq_per_unit.gif']

For example, suppose you have two voltages, *U<sub>1</sub>*=99 KV and *U<sub>2</sub>*=110 KV. When selecting 110 KV as the base value of voltages, you can express the per-unit value of *U<sub>1</sub>* and *U<sub>2</sub>* as follows.

[IMAGE alt='image' src='eq_per_unit_example1.gif']

[IMAGE alt='image' src='eq_per_unit_example2.gif']

The results show that the real value of *U<sub>1</sub>* is 0.9 times of the base value, while the real value of *U<sub>2</sub>* is the same as the base value. In other words, the per-unit value of *U<sub>1</sub>* is 0.9 and the per-unit value of *U<sub>2</sub>* is 1.

The per-unit system is ideal for fixed-point implementation. Per-unit helps to make the fixed-point model usable for various motors. All quantities are multiples of the base value that you select.

#### Troubleshooting Improper Base Value Error

When you use the Electric Motor Simulation VIs to generate FPGA data for electric motor simulation, an error occurs if improper **base values** lead to overflow. Complete the following steps to resolve the error.

1. Keep the value of speed base as default.
2. Gradually increase the value of current base . Keep the per-unit value of the maximum current within the range from 0.1 to 10. For example, suppose the maximum current of an electric motor is 300 A, you can select a value in the range from 30 A to 3000 A as the current base.
3. Gradually increase the value of voltage base . Keep the per-unit value of the maximum voltage within the range from 0.1 to 10.
4. Repeat steps 2 and 3 until the error stops occurring.

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/cons_para_model.html language=enus -->
## TOPIC 00018: Constant Parameter Model (Electric Motor Simulation Toolkit)

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/cons_para_model.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/cons_para_model.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Constant Parameter Model (Electric Motor Simulation Toolkit)

Use the constant parameter model function to simulate an AC induction motor (ACIM) or a permanent magnet synchronous motor (PMSM).

#### Constant Parameter Model for ACIM Simulation

The constant parameter model simulates the electromagnetic behavior of an ACIM by using the (α,β) orthogonal coordinate system.

In an (α,β) orthogonal coordinate system, the α axis usually coincides with the direction of the A current of the three-phase current in the stator. The β axis is the axis at an angle of 90 degrees from the α axis.

The following figure illustrates the relationship between the (α,β) orthogonal coordinate system and the three-phase current.

[IMAGE alt='image' src='noloc_eps_alpha_beta.gif']

Because of the three-phase current in the stator windings, the magnetizing currents of the stator produce a magnetic field. The magnetic field generates a current in the rotor. The voltage equations for ACIM simulation with the constant parameter model are as follows.

[IMAGE alt='image' src='eq_acim_vs1.gif']

[IMAGE alt='image' src='eq_acim_vs2.gif']

[IMAGE alt='image' src='eq_acim_vr1.gif']

[IMAGE alt='image' src='eq_acim_vr2.gif']

| where | Vsα is the stator voltage along the α axis |
| --- | --- |
|  | Vsβ is the stator voltage along the β axis |
|  | Rs is the stator resistance |
|  | Isα is the stator current along the α axis |
|  | Isβ is the stator current along the β axis |
|  | λsα is the stator flux linkage along the α axis |
|  | λsβ is the stator flux linkage along the β axis |
|  | Vrα is the rotor voltage along the α axis |
|  | Vrβ is the rotor voltage along the β axis |
|  | Rr is the rotor resistance |
|  | Irα is the rotor current along the α axis |
|  | Irβ is the rotor current along the β axis |
|  | λrα is the rotor flux linkage along the α axis |
|  | λrβ is the rotor flux linkage along the β axis |
|  | ωr is the electrical speed, in rad/s, which equals to rotor speed times the number of pole pairs |

The flux linkage equations are as follows.

[IMAGE alt='image' src='eq_acim_fluxs1.gif']

[IMAGE alt='image' src='eq_acim_fluxs2.gif']

[IMAGE alt='image' src='eq_acim_fluxr1.gif']

[IMAGE alt='image' src='eq_acim_fluxr2.gif']

| where | Lls is the stator leakage inductance |
| --- | --- |
|  | Llr is the rotor leakage inductance |
|  | Lm is the magnetizing inductance |

The voltage equations calculate the derivatives of stator flux linkage and rotor flux linkage.

[IMAGE alt='image' src='eq_acim_flux_de1.gif']

[IMAGE alt='image' src='eq_acim_flux_de2.gif']

[IMAGE alt='image' src='eq_acim_flux_de3.gif']

[IMAGE alt='image' src='eq_acim_flux_de4.gif']

where *k* and *k-1* are the simulation steps. For example, *λ<sub>sα</sub>*(*k*) is the stator flux linkage along the α axis at the *k* step, while *λ<sub>sα</sub>*(*k-1*) is the stator flux linkage along the α axis at the *k-1* step.

The flux linkage equations calculate the current by defining *λ<sub>mα</sub>*, *λ<sub>mβ</sub>*, and *L<sub>M</sub>*.

[IMAGE alt='image' src='eq_acim_cur_de1.gif']

[IMAGE alt='image' src='eq_acim_cur_de2.gif']

[IMAGE alt='image' src='eq_acim_cur_de3.gif']

The following equations can be derived to obtain the current in the (α,β) orthogonal coordinate system.

[IMAGE alt='image' src='eq_acim_cur1.gif']

[IMAGE alt='image' src='eq_acim_cur2.gif']

[IMAGE alt='image' src='eq_acim_cur3.gif']

[IMAGE alt='image' src='eq_acim_cur4.gif']

The constant parameter model calculates the electric torque of an ACIM by using the following equation.

[IMAGE alt='image' src='eq_acim_torque.gif']

where *p* is the number of poles.

#### Constant Parameter Model for PMSM Simulation

The constant parameter model simulates the electromagnetic behavior of a PMSM by using the d-q axes mathematical method.

The d-q axes are the axes in a (d,q) coordinate system. The d axis, or the direct axis, usually coincides with the axis of the rotor magnet pole. The q axis, or the quad axis, is the axis at an angle of 90 degrees from the d axis. When the rotor is stationary, the (d,q) coordinate system is a stationary reference frame. When the rotor starts rotating, the system is a rotor reference frame where the (d,q) coordinate system rotates at the rotor speed.

The following figure illustrates a (d,q) coordinate system.

[IMAGE alt='image' src='loc_eps_dqaxes.gif']

While the rotor is rotating, electromagnetic current is generated inside the electric motor. The voltage equations of the (d,q) rotor reference frame are as follows.

[IMAGE alt='image' src='eq_pmsm_vd.gif']

[IMAGE alt='image' src='eq_pmsm_vq.gif']

The flux linkage equations are as follows.

*λ<sub>d</sub>=L<sub>d</sub>I<sub>d</sub>+λ<sub>f</sub>*

*λ<sub>q</sub>=L<sub>q</sub>I<sub>q</sub>*

| where | ωr is electrical speed, in rad/s, which equals to rotor speed times the number of pole pairs |
| --- | --- |
|  | Id is the current along the d axis |
|  | Iq is the current along the q axis |
|  | λd is the flux linkage along the d axis |
|  | λq is the flux linkage along the q axis |
|  | λf is the flux linkage in the rotor magnet |
|  | Ld is the inductance along the d axis |
|  | Lq is the inductance along the q axis |

The following equation calculates the electric torque of the (d,q) rotor reference frame.

[IMAGE alt='image' src='eq_pmsm_torque.gif']

where *p* is the number of poles.

The following discrete equations calculate the current for PMSM simulation with the constant parameter model.

[IMAGE alt='image' src='eq_pmsm_cons_dis1.gif']

[IMAGE alt='image' src='eq_pmsm_cons_dis2.gif']

where *k* and *k-1* are the simulation steps. For example, *I<sub>d</sub>*(*k*) is the current along the d axis at the *k* step, while *I<sub>d</sub>*(*k-1*) is the current along the d axis at the *k-1* step.

##### Related Information

[Supported Motor Types](../lvemsimshared/motor_type.html)

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/fea_model.html language=enus -->
## TOPIC 00019: FEA Model (Electric Motor Simulation Toolkit)

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/fea_model.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/fea_model.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### FEA Model (Electric Motor Simulation Toolkit)

The finite element analysis (FEA) model function implements high-fidelity model simulation of an electric motor. The FEA model takes real motor characteristics into account and uses the FEA method to describe the motor behaviors.

In mathematics, the FEA method is a numerical technique to find approximate solutions to boundary value problems. This method connects many simple element equations over many small subdomains, named finite elements, to approximate a more complex equation over a larger domain. In mechanics and computer science, the FEA method is also a method of mechanical computer simulation and a computational tool to perform engineering analysis. The FEA model uses software programs based on finite element method algorithms to divide a complex problem into smaller elements.

The FEA model function obtains real motor characteristics from the RTT files. Among the characteristics, motor parameters are analyzed using the FEA method. As part of the simulation process, the FEA model function looks up the motor parameters and characteristics in these files.

The FEA model uses the following voltage equation to calculate the current for a PMSM.

[IMAGE alt='image' src='eq_fea_pmsm.gif']

| where | Va, Vb, and Vc are the three-phase voltages |
| --- | --- |
|  | R is the phase resistance |
|  | Ia, Ib, and Ic are the three-phase currents |
|  | L'aa, L'bb, and L'cc are the differential self-inductances |
|  | L'ab, L'ac, L'ba, L'bc, L'ca, and L'cb are the differential mutual inductances |
|  | λa, λb, and λc are the magnetic fluxes generated by the permanent magnet |

The FEA model uses the following voltage equation to calculate the current for a three-phase SRM.

[IMAGE alt='image' src='eq_fea_srm.gif']

| where | Laa, Lbb, and Lcc are the self-inductances |
| --- | --- |
|  | Lab, Lac, Lba, Lbc, Lca, and Lcb are the mutual inductances |

##### Related Information

[RTT File](../lvemsimshared/rtt_file.html)

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/inverter.html language=enus -->
## TOPIC 00020: Three-Phase Inverter (Electric Motor Simulation Toolkit)

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/inverter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/inverter.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Three-Phase Inverter (Electric Motor Simulation Toolkit)

An inverter is an electrical device that converts direct current (DC) to alternating current (AC). A three-phase inverter is a commonly-used inverter for powering a variable-speed motor like the permanent magnet synchronous motor (PMSM). The three-phase inverter consists of three single-phase branches which connect to three load terminals. Each single-phase branch contains two power switches. The following figure illustrates the circuit diagram of a three-phase inverter. In this circuit, the three resistances represent the load. In real applications, the load can be an electric motor.

[IMAGE alt='image' src='noloc_eps_inverter_model.gif']

The following symbols apply to the circuit diagram:

- S<sub>au</sub> is the phase A upper switch.
- S<sub>al</sub> is the phase A lower switch.
- S<sub>bu</sub> is the phase B upper switch.
- S<sub>bl</sub> is the phase B lower switch.
- S<sub>cu</sub> is the phase C upper switch.
- S<sub>cl</sub> is the phase C lower switch.
- V<sub>ab</sub> , V<sub>bc</sub> , and V<sub>ca</sub> are the line-to-line voltages.
- V<sub>a</sub> , V<sub>b</sub> , and V<sub>c</sub> are the phase voltages.

The Electric Motor Simulation Toolkit allows you to simulate an ideal three-phase inverter or an advanced three-phase inverter. In the ideal three-phase inverter model, the switches are simple on-off switches. When the switch is on, no voltage drop happens on the switch. When the switch is off, no current flows through the switch. In the advanced three-phase inverter model, the switches are insulated gate bipolar transistors (IGBT) with diodes. The advanced three-phase inverter model simulates the transient behavior of the inverter. By using the advanced three-phase inverter model, you can specify the forward voltage drops of the switches and insert fault to the inverter at run time.

#### Ideal Three-Phase Inverter Model

The ideal three-phase inverter model assumes that the switch state changes between on and off instantaneously. The two switches in the same single-phase branch are complementary. The following table lists the phase voltages and line-to-line voltages of the ideal three-phase inverter model. *V<sub>DC</sub>* is the DC voltage that connects to the inverter. In the **Switch State** column, *1* indicates that the switch is on, while *0* indicates that the switch is off.

| Switch State | Phase Voltage (V) | Line-to-Line Voltage (V) |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sau | Sbu | Scu | Va | Vb | Vc | Vab | Vbc | Vca |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 2VDC/3 | -VDC/3 | -VDC/3 | VDC | 0 | -VDC |
| 1 | 1 | 0 | VDC/3 | VDC/3 | -2VDC/3 | 0 | VDC | -VDC |
| 0 | 1 | 0 | -VDC/3 | 2VDC/3 | -VDC/3 | -VDC | VDC | 0 |
| 0 | 1 | 1 | -2VDC/3 | VDC/3 | VDC/3 | -VDC | 0 | VDC |
| 0 | 0 | 1 | -VDC/3 | -VDC/3 | 2VDC/3 | 0 | -VDC | VDC |
| 1 | 0 | 1 | VDC/3 | -2VDC/3 | VDC/3 | VDC | -VDC | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

The Electric Motor Simulation Toolkit only calculates the phase voltages. The following equations demonstrate the relationship between the line-to-line voltages and the phase voltages.

[IMAGE alt='image' src='eq_l2l_ab.gif']

[IMAGE alt='image' src='eq_l2l_bc.gif']

[IMAGE alt='image' src='eq_l2l_ca.gif']

#### Advanced Three-Phase Inverter Model

The advanced three-phase inverter model regards the IGBT-with-diode switch as a small inductance (*L*) when the switch is on. When the switch is off, the model regards the switch as a small capacitance (*C*). A conductance (*G*) in parallel with a dependent current source (*J*) represents a switch. The following figure illustrates how the advanced three-phase inverter model simulates the switch.

[IMAGE alt='image' src='loc_eps_inverter_switch.gif']

The advanced three-phase inverter model regards the conductance as a constant to simplify the calculation process. The following equations show the relationship between the conductance and the simulation time interval (*dt*).

[IMAGE alt='image' src='eq_inverter_conduc1.gif']

[IMAGE alt='image' src='eq_inverter_conduc2.gif']

[IMAGE alt='image' src='eq_inverter_conduc3.gif']

The following equation determines the current source. The subscript *k* and *k-1* denote the simulation steps.

[IMAGE alt='image' src='eq_inverter_current.gif']

| where | Ik-1 is the current on the switch at the k-1 step |
| --- | --- |
|  | Vk-1 is the voltage on the switch at the k-1 step |
|  | sk=1 denotes that the switch is on at the k step |
|  | sk=0 denotes that the switch is off at the k step |

The following equation determines the state of the IGBT-with-diode switch.

[IMAGE alt='image' src='eq_inverter_switch.gif']

where [IMAGE alt='image' src='eq_inverter_s.gif'] denotes the complement of *s*. *g* is the gate signal for the switch. *g*=1 denotes that the gate signal commands the switch to be on, while *g*=0 denotes that the gate signal commands the switch to be off.

##### Inserting Fault to the Inverter

The advanced three-phase inverter model allows you to simulate the behavior of an inverter when the switch has faults. The model provides four types of faults and only supports one fault at a time. The four fault types are as follows.

- IGBT open fault —This fault occurs if any IGBT is interrupted. No current flows through the IGBT with fault. It is equivalent to replacing the switch with a diode.
- Diode open fault —This fault occurs if any diode is interrupted. No current flows through the diode with fault. It is equivalent to replacing the switch with an IGBT.
- IGBT and diode open fault —This fault occurs if any IGBT-with-diode switch is interrupted. No current flows through the IGBT-with-diode switch with fault. It is equivalent to removing the switch from the circuit.
- IGBT or diode short fault —This fault occurs if any IGBT or diode is bypassed. It is equivalent to replacing the switch with a wire. In this case, the protection circuit turns off the other switch in the same single-phase branch as the switch with fault. As a result, short circuit does not happen to the voltage source.

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/line_model.html language=enus -->
## TOPIC 00021: Linear Model (Electric Motor Simulation Toolkit)

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/line_model.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/line_model.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Linear Model (Electric Motor Simulation Toolkit)

The [switched reluctance motor (SRM)](../lvemsimshared/motor_type.html) shows strong nonlinearity because the flux of a stator winding depends on both the phase current and the rotor position. Therefore, the linear model utilizes the piece-wise linear method to describe the flux of an SRM.

In an SRM, the non-linear characteristics of the magnet affect the operation of the SRM. High levels of saturation occur cyclically as the rotor continuously moves from an unaligned position to an aligned position, with reference to the poles on the stator. The following figure depicts different rotor positions.

[IMAGE alt='image' src='loc_fp_linearaligned.gif']

The positions are specific to one of the phases. The aligned position means that the pole of the rotor and the pole of the stator are in the same line. The unaligned position means that the rotor of the specific phase is completely detached from the stator. The middle position is when the pole of the rotor has intersection with the pole of the stator. The flux linkage of the motor phase varies at different positions.

The SRM linear model function complies with the following equations.

Phase voltage equation:

[IMAGE alt='image' src='eq_srm_vol.gif']

Instant torque equation:

[IMAGE alt='image' src='eq_srm_torque.gif']

| where | λ is the flux linkage |
| --- | --- |
|  | θ is the rotor position |
|  | R is the resistance |
|  | I is the current |
|  | V is the voltage |
|  | T is the torque |

The following figure shows an analytical expression for the flux linkage of a linear model. The aligned and unaligned curves represent the flux changes at the aligned position and unaligned position. The two curves in the middle represent the flux changes at the middle positions.

[IMAGE alt='image' src='loc_eps_flux.gif']

In the following figure, the curves with dots show the flux linkage of a real motor at different rotor position. The curves without dots represent the linear model approximation.

[IMAGE alt='image' src='noloc_fp_linear.gif']

The slope of the straight line in the figure approximates the flux curve for the unaligned position, as shown in the following equation.

[IMAGE alt='image' src='eq_srm_flux1.gif']

where *L<sub>u</sub>* is a constant that represents the equivalent inductance of the coil for the unaligned position. The *u* subscript means unaligned.

For aligned positions, when *I* is no greater than *I<sub>s</sub>*,

[IMAGE alt='image' src='eq_srm_flux2_1.gif']

where *λ<sub>a</sub>* is the flux of *I<sub>s</sub>* at the aligned position. The *a* subscript means aligned and the *s* subscript means saturated.

When *I* is greater than *I<sub>s</sub>*,

[IMAGE alt='image' src='eq_srm_flux2_2.gif']

The dependency of *λ* on the rotor position *θ* is approximated by a sine wave oscillating between the maximum value *λ<sub>a</sub>(I)* and the minimum value *λ<sub>u</sub>(I)*, as illustrated in the following equation.

[IMAGE alt='image' src='eq_srm_flux3.gif']

where *p* is the number of poles in pairs.

From the previous equations, a linear model function solves the current and torque in the SRM.

When *I* is no greater than *I<sub>s</sub>*,

[IMAGE alt='image' src='eq_srm_current1.gif']

where the *k* subscript indicates the variable calculated at the *k* step, while the *k-1* subscript indicates the variable calculated at the *k-1* step. For example, *I<sub>k</sub>* is the phase current at the *k* step, while *I<sub>k-1</sub>* is the phase current at the *k-1* step.

[IMAGE alt='image' src='eq_srm_torque1.gif']

When *I* is greater than *I<sub>s</sub>*,

[IMAGE alt='image' src='eq_srm_current2.gif']

[IMAGE alt='image' src='eq_srm_torque2.gif']

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/lvemsimshared.html language=enus -->
## TOPIC 00022: Electric Motor Simulation Concepts (Electric Motor Simulation Toolkit)

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/lvemsimshared.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/lvemsimshared.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Electric Motor Simulation Concepts (Electric Motor Simulation Toolkit)

October 2015, 374207C-01

Electric motor simulation is the process of imitating the control and operation of a real-world electric motor over time. The simulated electric motor is typically a part of the hardware-in-the-loop (HIL) simulation, which is widely used in the development and test of complex real-time embedded systems. Simulating an electric motor that runs in the HIL system allows you to design and debug the application without depending on the physical electric motor. When you simulate an electric motor, you can validate the mechanical parameters of the motor, test algorithms for controlling the motor behaviors, and verify if the simulated motor works with the controller and I/O modules in the HIL system before you deploy and run the application on real hardware. The technique of electric motor simulation is becoming increasingly popular in industrial development because of its efficiency, safety, duration, and advantage of saving the cost of all tools and effort.

With the Electric Motor Simulation Toolkit, you use the palette VIs, examples, and sample projects to design an HIL system and model the motion of real electric motors in a real-world system. You configure the motor parameters and test the control algorithms with efficiency in a simulated system. When you can ensure that the control algorithms work satisfactorily, replace the simulated motor with a real electric motor. You can further replace the control algorithms with a real controller, such as an electronic control unit (ECU).

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

© 2013–2015 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/motor_type.html language=enus -->
## TOPIC 00023: Supported Motor Types (Electric Motor Simulation Toolkit)

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/motor_type.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/motor_type.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Supported Motor Types (Electric Motor Simulation Toolkit)

The Electric Motor Simulation Toolkit allows you to simulate the following types of electric motors.

- AC induction motors (ACIM)
- Permanent magnet synchronous motors (PMSM)
- Switched reluctance motors (SRM)

#### ACIM

An ACIM is a type of electric motor that has a stationary stator outside and a rotor which spins inside. By supplying alternating current to the stator, the ACIM uses the electromagnet of the stator to generate current in the rotor and produce torque. The stator is a hollow metal cylinder with slots for coils of wires. The rotor consists of metal bars which have end rings at both ends to form short circuits. The following figure illustrates a typical ACIM.

[IMAGE alt='image' src='noloc_eps_acim.gif']

#### PMSM

A PMSM is a type of electric motor that utilizes permanent magnets in the rotor. The poles of a PMSM indicates how many even numbers of magnet poles that the rotor has. The following figure is an example of a typical PMSM. This motor has four permanent magnets on the rotor, as shown in the figure.

[IMAGE alt='image' src='noloc_eps_pmsm.gif']

#### SRM

An SRM is a type of electric motor that produces torque from a slight misalignment of poles on the rotor with poles on the stator. The rotor tends to align itself with the stator to maximize the inductance of the stator, while the stator is consequently energized to force the rotor to rotate. The phase of the SRM indicates the number of pole pairs in the stator. For example, the following figure illustrates a three-phase SRM. The stator of this motor has three pairs of poles.

[IMAGE alt='image' src='noloc_eps_srm.gif']

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/rtt_file.html language=enus -->
## TOPIC 00024: RTT File (Electric Motor Simulation Toolkit)

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/rtt_file.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/rtt_file.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### RTT File (Electric Motor Simulation Toolkit)

An RTT file, or the JMAG-RT motor model, is a third-party product provided by the JSOL company. The file, with an extension of .rtt, contains basic motor characteristics, such as the motor type, connection type, and number of poles. The RTT file also contains detailed motor parameters information, which are the analysis results of the JMAG-RT software.

You can use the Electric Motor Simulation Toolkit to read an RTT file for the FEA model or the variable parameter model. You can either download RTT files from the JSOL website at www.jmag-international.com or create an RTT file by using the JMAG-RT software.

##### Related Information

[Variable Parameter Model](../lvemsimshared/vari_para_model.html)

[FEA Model](../lvemsimshared/fea_model.html)

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/temp_correction.html language=enus -->
## TOPIC 00025: Temperature Correction (Electric Motor Simulation Toolkit)

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/temp_correction.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/temp_correction.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Temperature Correction (Electric Motor Simulation Toolkit)

Temperature correction is a functionality that simulates the changes of resistance, magnet flux, or torque in an electric motor according to temperature variations. In a permanent magnet synchronous motor (PMSM), when the magnet temperature and the coil temperature change, the resistance and the magnet flux change accordingly. Magnet temperature variations also affect the electromagnetic torque. In an AC induction motor (ACIM), when the rotor temperature and the stator temperature change, the rotor resistance and the stator resistance change accordingly. The Electric Motor Simulation Toolkit provides the temperature correction functionality for ACIM simulation with the constant parameter model and PMSM simulation with the FEA and the variable parameter models.

To perform the temperature correction functionality, you must obtain motor parameters for temperature correction. By using the Electric Motor Simulation VIs, you can either manually specify the temperature correction parameters, or obtain the temperature correction parameters from an RTT file.

The following equation calculates the PMSM coil resistance, the ACIM stator resistance, and the ACIM rotor resistance after temperature correction:

[IMAGE alt='image' src='eq_temp_correction1.gif']

| where | R' is the resistance after temperature correction |
| --- | --- |
|  | R is the resistance under the base temperature before temperature correction |
|  | k is the temperature correction coefficient |
|  | T is the real-time temperature |
|  | Tbase is the base temperature |

The following equation calculates the PMSM magnet flux after temperature correction:

[IMAGE alt='image' src='eq_temp_correction2.gif']

| where | F' is the magnet flux after temperature correction |
| --- | --- |
|  | F is the magnet flux under the magnet base temperature before temperature correction |
|  | km is the magnet temperature correction coefficient |
|  | Tm is the real-time magnet temperature |
|  | Tm-base is the magnet base temperature |

##### Related Information

[Constant Parameter Model](../lvemsimshared/cons_para_model.html)

[Variable Parameter Model](../lvemsimshared/vari_para_model.html)

[FEA Model](../lvemsimshared/fea_model.html)

[RTT File](../lvemsimshared/rtt_file.html)

[Electric Motor Simulation VIs](/csh?topicname=lvemsimvi/emsim_vis.html)

<!--NI_TOPIC bundle=veristand-electric-motor-simulation-toolkit-api-ref path=lvemsimshared/vari_para_model.html language=enus -->
## TOPIC 00026: Variable Parameter Model (Electric Motor Simulation Toolkit)

- bundle_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- source_path: `lvemsimshared/vari_para_model.html`
- source_url: https://docs-be.ni.com/bundle/veristand-electric-motor-simulation-toolkit-api-ref/raw/resource/enus/lvemsimshared/vari_para_model.html
- document_id: `veristand-electric-motor-simulation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Variable Parameter Model (Electric Motor Simulation Toolkit)

Use the variable parameter model function to implement medium-fidelity model simulation of a permanent magnet synchronous motor (PMSM). Like the constant parameter model, the variable parameter model uses the voltage equations, flux linkage equations, and torque equation of the (d,q) rotor reference frame. Unlike the constant parameter model, the motor inductance in the variable parameter model is a variable due to magnet saturation. The variable parameter model can obtain real motor characteristics from an RTT file, an ANSYS motor model file, or an external model.

The variable parameter model uses the following discrete equations to calculate the current for a PMSM.

[IMAGE alt='image' src='eq_pmsm_vari_dis1.gif']

[IMAGE alt='image' src='eq_pmsm_vari_dis2.gif']

| where | ωr is electrical speed, in rad/s, which equals to rotor speed times the number of pole pairs |
| --- | --- |
|  | R is the resistance |
|  | Vd is the voltage along the d axis |
|  | Vq is the voltage along the q axis |
|  | λd is the flux linkage along the d axis |
|  | λq is the flux linkage along the q axis |
|  | λf is the flux linkage in the rotor magnet |
|  | Ld is the inductance along the d axis |
|  | Lq is the inductance along the q axis |
|  | k, k-1, and k-2 are the simulation steps |

For example, *I<sub>d</sub>*(*k*) is the current along the d axis at the *k* step. *I<sub>d</sub>*(*k-1*) is the current along the d axis at the *k-1* step. *L<sub>q</sub>*(*k-2*) is the inductance along the q axis at the *k-2* step.

#### External Model

An external model is a model function you create by using the Electric Motor Simulation Toolkit. You can import the external model to get motor characteristics for simulating a PMSM with the variable parameter model. Motor characteristics include number of poles, resistance, temperature correction parameters, direct inductance table, quad inductance table, flux table, and so on.

##### Related Information

[Supported Motor Types](../lvemsimshared/motor_type.html)

[Constant Parameter Model for PMSM Simulation](../lvemsimshared/cons_para_model.html#cons_pmsm)

[RTT File](../lvemsimshared/rtt_file.html)

[ANSYS Motor Model File](../lvemsimshared/ansys_file.html)

[Temperature Correction](../lvemsimshared/temp_correction.html)
